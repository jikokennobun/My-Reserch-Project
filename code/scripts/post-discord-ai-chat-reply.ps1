param(
    [Parameter(Mandatory = $true)]
    [string]$MessageId,
    [string]$Content,
    [string]$ContentPath,
    [string]$ChannelId = $env:DISCORD_AI_CHAT_CHANNEL_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$OriginalText,
    [string]$OriginalTimestamp,
    [string]$ChannelName = "ai-chat",
    [string]$RepositoryRoot,
    [string]$StatePath,
    [string]$ResearchInboxPath,
    [string]$ResearchLogPath,
    [string]$Source = "codex-automation",
    [switch]$SaveResearchMusing,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv"
}
if ([string]::IsNullOrWhiteSpace($ResearchInboxPath)) {
    $ResearchInboxPath = Join-Path $RepositoryRoot "research\ideas\inbox.md"
}
if ([string]::IsNullOrWhiteSpace($ResearchLogPath)) {
    $ResearchLogPath = Join-Path $RepositoryRoot "records\research-triage\discord-ai-chat-$Date.md"
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}
if ([string]::IsNullOrWhiteSpace($Content) -and -not [string]::IsNullOrWhiteSpace($ContentPath) -and (Test-Path -LiteralPath $ContentPath)) {
    $Content = Get-Content -LiteralPath $ContentPath -Raw -Encoding UTF8
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) { throw "Set DISCORD_AI_CHAT_CHANNEL_ID or pass -ChannelId." }
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }
if ([string]::IsNullOrWhiteSpace($Content)) { throw "Pass -Content or -ContentPath." }

function ConvertTo-JsonBodyFile {
    param([object]$Body)

    $tmp = [IO.Path]::GetTempFileName()
    $json = $Body | ConvertTo-Json -Depth 16
    [IO.File]::WriteAllText($tmp, $json, [Text.UTF8Encoding]::new($false))
    return $tmp
}

function Invoke-DiscordJson {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null
    )

    $methodName = $Method.ToUpperInvariant()
    $args = @("-sS", "--connect-timeout", "8", "--max-time", "15", "-X", $methodName, "-H", "Authorization: Bot $BotToken", "-H", "Content-Type: application/json; charset=utf-8")
    $bodyFile = $null
    if ($null -ne $Body) {
        $bodyFile = ConvertTo-JsonBodyFile -Body $Body
        $args += @("--data-binary", "@$bodyFile")
    }
    $args += "https://discord.com/api/v10$Path"

    try {
        $raw = & curl.exe @args
    } finally {
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path -LiteralPath $bodyFile)) {
            Remove-Item -LiteralPath $bodyFile -Force
        }
    }
    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $methodName $Path." }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $methodName $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Limit-DiscordContent {
    param([string]$Text)

    $value = $Text.Trim()
    if ($value.Length -le 1900) { return $value }
    return $value.Substring(0, 1880).TrimEnd() + "`n...(truncated)"
}

function Get-ResearchMusingTitle {
    param([string]$Text)

    $first = (($Text -split "\r?\n") | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($first)) { return "Discord math musing" }
    $first = ($first -replace "\s+", " ").Trim()
    if ($first.Length -gt 70) { $first = $first.Substring(0, 70) + "..." }
    return $first
}

function Save-State {
    $dir = Split-Path -Parent $StatePath
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    $row = [pscustomobject]@{
        MessageId = $MessageId
        ChannelId = $ChannelId
        Status = "replied"
        Source = $Source
        ReplyMessageId = $script:ReplyMessageId
        RepliedAt = (Get-Date).ToString("o")
        UpdatedAt = (Get-Date).ToString("o")
    }
    if (Test-Path -LiteralPath $StatePath) {
        $row | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Append -Encoding UTF8
    } else {
        $row | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Encoding UTF8
    }
}

function Test-AlreadyReplied {
    $paths = @(
        $StatePath,
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-codex-state.csv"),
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv")
    ) | Select-Object -Unique

    foreach ($path in $paths) {
        if (-not (Test-Path -LiteralPath $path)) { continue }
        foreach ($row in @(Import-Csv -LiteralPath $path)) {
            if ([string]$row.MessageId -ne [string]$MessageId) { continue }
            $status = ""
            if ($row.PSObject.Properties.Name -contains "Status") {
                $status = ([string]$row.Status).ToLowerInvariant()
            }
            if ([string]::IsNullOrWhiteSpace($status) -and $row.PSObject.Properties.Name -contains "RepliedAt" -and -not [string]::IsNullOrWhiteSpace([string]$row.RepliedAt)) {
                return $true
            }
            if ($status -eq "replied") { return $true }
        }
    }
    return $false
}

function Save-ResearchMusing {
    if ([string]::IsNullOrWhiteSpace($OriginalText)) { return }

    $title = Get-ResearchMusingTitle -Text $OriginalText
    $inboxDir = Split-Path -Parent $ResearchInboxPath
    if (-not (Test-Path -LiteralPath $inboxDir)) { New-Item -ItemType Directory -Path $inboxDir | Out-Null }

    if (Test-Path -LiteralPath $ResearchInboxPath) {
        $inboxLines = New-Object 'System.Collections.Generic.List[string]'
        foreach ($line in Get-Content -LiteralPath $ResearchInboxPath -Encoding UTF8) { $inboxLines.Add($line) }
    } else {
        $inboxLines = New-Object 'System.Collections.Generic.List[string]'
        $inboxLines.Add("# Idea Inbox")
        $inboxLines.Add("")
        $inboxLines.Add("## Unsorted")
    }

    if (-not ($inboxLines | Where-Object { $_ -match [regex]::Escape($MessageId) })) {
        $timestamp = if ([string]::IsNullOrWhiteSpace($OriginalTimestamp)) { (Get-Date).ToString("o") } else { $OriginalTimestamp }
        $block = @(
            "",
            "### $Date - $title",
            "",
            ("Source: Discord self-manzokubun " + $MessageId + " in " + $ChannelName + " at " + $timestamp),
            "",
            "Musing:",
            $OriginalText.Trim(),
            "",
            "AI reply:",
            $Content.Trim(),
            "",
            "Next action:",
            "- [ ] Ask Codex for a source-backed literature survey or promote this into a stable research note.",
            ""
        )

        $unsortedIndex = -1
        for ($i = 0; $i -lt $inboxLines.Count; $i++) {
            if ($inboxLines[$i].Trim() -eq "## Unsorted") { $unsortedIndex = $i; break }
        }
        if ($unsortedIndex -lt 0) {
            $inboxLines.Add("")
            $inboxLines.Add("## Unsorted")
            $unsortedIndex = $inboxLines.Count - 1
        }
        $insertIndex = $unsortedIndex + 1
        for ($i = $block.Count - 1; $i -ge 0; $i--) {
            $inboxLines.Insert($insertIndex, $block[$i])
        }
        Set-Content -LiteralPath $ResearchInboxPath -Encoding UTF8 -Value $inboxLines
    }

    $logDir = Split-Path -Parent $ResearchLogPath
    if (-not (Test-Path -LiteralPath $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
    if (-not (Test-Path -LiteralPath $ResearchLogPath)) {
        Set-Content -LiteralPath $ResearchLogPath -Encoding UTF8 -Value @("# Discord AI Chat Research Musings - $Date", "")
    }
    Add-Content -LiteralPath $ResearchLogPath -Encoding UTF8 -Value @(
        "",
        "## $Date - $title",
        "",
        "MessageId: $MessageId",
        "Channel: $ChannelName",
        "",
        "Musing:",
        $OriginalText.Trim(),
        "",
        "AI reply:",
        $Content.Trim(),
        ""
    )
}

$contentToPost = Limit-DiscordContent -Text $Content

if ($DryRun) {
    Write-Host "Would post reply to Discord message $MessageId."
    Write-Host $contentToPost
    exit 0
}

if (Test-AlreadyReplied) {
    Write-Host "Message $MessageId already has a recorded AI chat reply. Skipping duplicate post."
    exit 0
}

$posted = Invoke-DiscordJson -Method Post -Path "/channels/$ChannelId/messages" -Body ([ordered]@{
    content = $contentToPost
    message_reference = [ordered]@{
        message_id = $MessageId
        channel_id = $ChannelId
        fail_if_not_exists = $false
    }
    allowed_mentions = [ordered]@{ parse = @() }
})
$script:ReplyMessageId = if ($null -ne $posted -and $posted.PSObject.Properties.Name -contains "id") { [string]$posted.id } else { "" }

if ($SaveResearchMusing) { Save-ResearchMusing }
Save-State

Write-Host "Posted AI chat reply to message $MessageId."

