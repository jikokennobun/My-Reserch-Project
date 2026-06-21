param(
    [string]$Date,
    [ValidateSet("QueueOnly", "OpenAI")]
    [string]$Mode = "QueueOnly",
    [string]$PendingPath,
    [string]$StatePath,
    [string]$ChannelId = $env:DISCORD_AI_CHAT_CHANNEL_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$SelfUserId = $env:DISCORD_SELF_USER_ID,
    [string]$OpenAIApiKey = $env:OPENAI_API_KEY,
    [string]$Model = $env:OPENAI_AI_CHAT_MODEL,
    [string]$RepositoryRoot,
    [int]$MaxMessages = 1,
    [int]$ClaimStaleMinutes = 10,
    [switch]$SaveResearchMusings,
    [switch]$AllowAnyAuthor,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($Date)) {
    $Date = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9)).ToString("yyyy-MM-dd")
}
if ([string]::IsNullOrWhiteSpace($PendingPath)) {
    $PendingPath = Join-Path $RepositoryRoot "records\inbox\ai-chat\$Date-pending.jsonl"
}
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv"
}
if ([string]::IsNullOrWhiteSpace($Model)) {
    $Model = [Environment]::GetEnvironmentVariable("OPENAI_AI_CHAT_MODEL", "User")
}
if ([string]::IsNullOrWhiteSpace($Model)) {
    $Model = "gpt-5.5"
}

function Get-UserEnv {
    param([string]$Name, [string]$Current)
    if (-not [string]::IsNullOrWhiteSpace($Current)) { return $Current }
    return [Environment]::GetEnvironmentVariable($Name, "User")
}

$ChannelId = Get-UserEnv -Name "DISCORD_AI_CHAT_CHANNEL_ID" -Current $ChannelId
$BotToken = Get-UserEnv -Name "DISCORD_BOT_TOKEN" -Current $BotToken
$SelfUserId = Get-UserEnv -Name "DISCORD_SELF_USER_ID" -Current $SelfUserId
$OpenAIApiKey = Get-UserEnv -Name "OPENAI_API_KEY" -Current $OpenAIApiKey

if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}
if (-not [string]::IsNullOrWhiteSpace($OpenAIApiKey)) {
    $OpenAIApiKey = ([regex]::Replace($OpenAIApiKey, "\p{C}", "")).Trim()
}

if (-not $AllowAnyAuthor -and [string]::IsNullOrWhiteSpace($SelfUserId)) {
    throw "Set DISCORD_SELF_USER_ID before processing AI chat pending messages, or pass -AllowAnyAuthor explicitly."
}
if ($Mode -eq "OpenAI") {
    if ([string]::IsNullOrWhiteSpace($ChannelId)) { throw "Set DISCORD_AI_CHAT_CHANNEL_ID or pass -ChannelId." }
    if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }
    if ([string]::IsNullOrWhiteSpace($OpenAIApiKey) -and -not $DryRun) {
        throw "Set OPENAI_API_KEY for -Mode OpenAI. QueueOnly mode does not need an API key."
    }
}

function ConvertTo-JsonBodyFile {
    param([object]$Body)

    $tmp = [IO.Path]::GetTempFileName()
    $json = $Body | ConvertTo-Json -Depth 32
    [IO.File]::WriteAllText($tmp, $json, [Text.UTF8Encoding]::new($false))
    return $tmp
}

function Invoke-JsonApi {
    param(
        [string]$Method,
        [string]$Uri,
        [hashtable]$Headers,
        [object]$Body = $null
    )

    $methodName = $Method.ToUpperInvariant()
    $bodyFile = $null
    $bodyText = $null
    if ($null -ne $Body) {
        $bodyFile = ConvertTo-JsonBodyFile -Body $Body
        $bodyText = Get-Content -LiteralPath $bodyFile -Raw -Encoding UTF8
    }

    try {
        if ($null -ne $Body) {
            return Invoke-RestMethod -Method $methodName -Uri $Uri -Headers $Headers -ContentType "application/json; charset=utf-8" -Body $bodyText -TimeoutSec 60
        }
        return Invoke-RestMethod -Method $methodName -Uri $Uri -Headers $Headers -TimeoutSec 30
    } finally {
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path -LiteralPath $bodyFile)) {
            Remove-Item -LiteralPath $bodyFile -Force
        }
    }
}

function Invoke-OpenAIResponse {
    param([object]$Body)

    $headers = @{
        Authorization = "Bearer $OpenAIApiKey"
    }
    $json = Invoke-JsonApi -Method Post -Uri "https://api.openai.com/v1/responses" -Headers $headers -Body $Body
    if ($null -ne $json -and $json.PSObject.Properties.Name -contains "error") {
        throw "OpenAI API error: $($json.error.message)"
    }
    return $json
}

function Get-OutputText {
    param([object]$Response)

    if ($null -eq $Response) { return "" }
    if ($Response.PSObject.Properties.Name -contains "output_text" -and -not [string]::IsNullOrWhiteSpace([string]$Response.output_text)) {
        return [string]$Response.output_text
    }

    $parts = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in @($Response.output)) {
        foreach ($content in @($item.content)) {
            if ($content.PSObject.Properties.Name -contains "text" -and -not [string]::IsNullOrWhiteSpace([string]$content.text)) {
                $parts.Add([string]$content.text) | Out-Null
            }
        }
    }
    return (($parts.ToArray()) -join "`n").Trim()
}

function Limit-DiscordContent {
    param([string]$Text)

    $value = $Text.Trim()
    if ($value.Length -le 1900) { return $value }
    return $value.Substring(0, 1880).TrimEnd() + "`n...(truncated)"
}

function Convert-DiscordTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
}

function Get-StateRows {
    $paths = New-Object 'System.Collections.Generic.List[string]'
    $paths.Add($StatePath) | Out-Null
    foreach ($legacy in @(
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-codex-state.csv"),
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv")
    )) {
        if (-not $paths.Contains($legacy)) { $paths.Add($legacy) | Out-Null }
    }

    $rows = New-Object 'System.Collections.Generic.List[object]'
    foreach ($path in $paths) {
        if (Test-Path -LiteralPath $path) {
            foreach ($row in @(Import-Csv -LiteralPath $path)) {
                $rows.Add($row) | Out-Null
            }
        }
    }
    return @($rows.ToArray())
}

function Get-RowStatus {
    param([object]$Row)

    if ($null -eq $Row) { return "" }
    if ($Row.PSObject.Properties.Name -contains "Status" -and -not [string]::IsNullOrWhiteSpace([string]$Row.Status)) {
        return ([string]$Row.Status).ToLowerInvariant()
    }
    if ($Row.PSObject.Properties.Name -contains "RepliedAt" -and -not [string]::IsNullOrWhiteSpace([string]$Row.RepliedAt)) {
        return "replied"
    }
    return ""
}

function Get-RowUpdatedAt {
    param([object]$Row)

    foreach ($name in @("UpdatedAt", "RepliedAt", "SeenAt", "CreatedAt")) {
        if ($Row.PSObject.Properties.Name -contains $name -and -not [string]::IsNullOrWhiteSpace([string]$Row.$name)) {
            try { return [DateTimeOffset]::Parse([string]$Row.$name, [Globalization.CultureInfo]::InvariantCulture) } catch {}
        }
    }
    return [DateTimeOffset]::MinValue
}

function Get-LatestState {
    param([string]$MessageId)

    $matched = @($script:StateRows | Where-Object { [string]$_.MessageId -eq [string]$MessageId })
    if ($matched.Count -eq 0) { return $null }
    return ($matched | Sort-Object { Get-RowUpdatedAt -Row $_ } | Select-Object -Last 1)
}

function Add-StateRow {
    param(
        [string]$MessageId,
        [string]$ChannelIdValue,
        [string]$Status,
        [string]$Source,
        [string]$Detail = "",
        [string]$ResponseId = "",
        [string]$ReplyMessageId = ""
    )

    if ($DryRun) { return }
    $dir = Split-Path -Parent $StatePath
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

    $updatedAt = (Get-Date).ToString("o")
    $repliedAt = if ($Status -eq "replied") { $updatedAt } else { "" }
    $row = [pscustomobject][ordered]@{
        MessageId = $MessageId
        ChannelId = $ChannelIdValue
        Status = $Status
        Source = $Source
        ReplyMessageId = $ReplyMessageId
        RepliedAt = $repliedAt
        UpdatedAt = $updatedAt
    }
    if (Test-Path -LiteralPath $StatePath) {
        $row | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Append -Encoding UTF8
    } else {
        $row | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Encoding UTF8
    }
}

function Acquire-Lock {
    param([string]$Path, [int]$StaleMinutes = 10)

    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

    if (Test-Path -LiteralPath $Path) {
        $age = ([DateTime]::Now - (Get-Item -LiteralPath $Path).LastWriteTime).TotalMinutes
        if ($age -lt $StaleMinutes) { throw "AI chat pending worker is already running. Lock: $Path" }
        Remove-Item -LiteralPath $Path -Force
        Write-Warning "Removed stale AI chat pending worker lock: $Path"
    }

    if (-not $DryRun) {
        New-Item -ItemType File -Path $Path -Value ((Get-Date).ToString("o")) -ErrorAction Stop | Out-Null
    }
}

function Release-Lock {
    param([string]$Path)
    if (-not $DryRun -and (Test-Path -LiteralPath $Path)) {
        Remove-Item -LiteralPath $Path -Force
    }
}

function Test-ResearchMusing {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return $false }
    $value = ($Text -replace "\s+", " ").Trim()
    if ($value.Length -lt 8) { return $false }
    $asciiPattern = "(?i)\b(aps|ams|g2|fg2|loeb|lob|fixed\s*point|provability|modal|logic|theorem|proof|model|algebra|topology|category|survey|paper|literature|conjecture|lemma|axiom|arithmetic|ordinal|sequent|cut\s*elimination|realizability|domain\s*theory)\b"
    if ($value -match $asciiPattern) { return $true }
    $jpPattern = [regex]::Unescape("\u6570\u5B66|\u5B9A\u7406|\u8A3C\u660E|\u8AD6\u6587|\u89E3\u8AAC|\u30B5\u30FC\u30D9\u30A4|\u7814\u7A76|\u516C\u7406|\u30E2\u30C7\u30EB|\u4E0D\u5B8C\u5168|\u56FA\u5B9A\u70B9|\u7B97\u8853|\u69D8\u76F8|\u8AD6\u7406|\u4F4D\u76F8|\u570F|\u4EE3\u6570|\u30DC\u30E4\u30AD")
    return ($value -match $jpPattern)
}

function New-AiReply {
    param([object]$Record)

    $attachments = @($Record.attachments)
    $attachmentText = if ($attachments.Count -gt 0) { "`nAttachments:`n- " + ($attachments -join "`n- ") } else { "" }
    $userText = @(
        "Discord channel: $($Record.channel)"
        "Timestamp: $($Record.timestamp)"
        "Author: $($Record.author)"
        ""
        [string]$Record.content
        $attachmentText
    ) -join "`n"

    $developerPrompt = @(
        "You are Jiko-Manzokubun, a private mathematical and research companion replying inside Discord."
        "Reply in Japanese with a casual, direct style; avoid stiff honorific prose."
        "Keep the reply short, usually 6 to 10 lines and under about 900 Japanese characters."
        "For mathematical musings, include compact formulas or logical notation when useful."
        "Do not invent citations, bibliographic facts, or fake links."
        "If source-backed survey is needed, say that Codex should be asked to verify sources."
        "Separate known facts from conjectural connections."
    ) -join " "

    $body = [ordered]@{
        model = $Model
        input = @(
            [ordered]@{
                role = "developer"
                content = @([ordered]@{ type = "input_text"; text = $developerPrompt })
            },
            [ordered]@{
                role = "user"
                content = @([ordered]@{ type = "input_text"; text = $userText })
            }
        )
        store = $true
    }

    $response = Invoke-OpenAIResponse -Body $body
    $answer = Limit-DiscordContent -Text (Get-OutputText -Response $response)
    if ([string]::IsNullOrWhiteSpace($answer)) {
        $answer = "うまく返答を生成できなかった。もう一回投げて。"
    }
    return [pscustomobject]@{
        text = $answer
        response_id = [string]$response.id
    }
}

function Read-PendingRecords {
    if (-not (Test-Path -LiteralPath $PendingPath)) { return @() }
    $records = New-Object 'System.Collections.Generic.List[object]'
    foreach ($line in Get-Content -LiteralPath $PendingPath -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try {
            $records.Add(($line | ConvertFrom-Json)) | Out-Null
        } catch {
            Write-Warning "Ignoring invalid pending JSONL line in $PendingPath`: $($_.Exception.Message)"
        }
    }
    return @($records.ToArray())
}

$lockPath = Join-Path $RepositoryRoot "records\logs\discord-ai-chat-reply.lock"
$claimed = 0
$replied = 0
$queued = 0
$failed = 0

Acquire-Lock -Path $lockPath -StaleMinutes $ClaimStaleMinutes
try {
    $script:StateRows = @(Get-StateRows)
    $pending = @(Read-PendingRecords)
    if ($pending.Count -eq 0) {
        Write-Host "No pending AI chat message(s) in $PendingPath."
        return
    }

    $targets = New-Object 'System.Collections.Generic.List[object]'
    foreach ($record in ($pending | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp })) {
        $messageId = [string]$record.message_id
        if ([string]::IsNullOrWhiteSpace($messageId)) { continue }
        if (-not $AllowAnyAuthor -and [string]$record.author_id -ne [string]$SelfUserId) { continue }
        if ([string]::IsNullOrWhiteSpace([string]$record.content) -and @($record.attachments).Count -eq 0) { continue }

        $latest = Get-LatestState -MessageId $messageId
        $status = Get-RowStatus -Row $latest
        if ($status -eq "replied") { continue }
        if ($status -eq "claimed") {
            $updatedAt = Get-RowUpdatedAt -Row $latest
            if (([DateTimeOffset]::Now - $updatedAt).TotalMinutes -lt $ClaimStaleMinutes) { continue }
        }
        $targets.Add($record) | Out-Null
    }

    foreach ($record in ($targets.ToArray() | Select-Object -First $MaxMessages)) {
        $messageId = [string]$record.message_id
        $recordChannelId = if (-not [string]::IsNullOrWhiteSpace([string]$record.channel_id)) { [string]$record.channel_id } else { $ChannelId }

        if ($Mode -eq "QueueOnly") {
            Add-StateRow -MessageId $messageId -ChannelIdValue $recordChannelId -Status "queued" -Source "gateway-queue" -Detail "Waiting for Codex/manual responder."
            $queued++
            continue
        }

        Add-StateRow -MessageId $messageId -ChannelIdValue $recordChannelId -Status "claimed" -Source "event-openai" -Detail "Generating reply."
        $claimed++
        try {
            $reply = New-AiReply -Record $record
            $replyDir = Join-Path $RepositoryRoot "tmp\self-manzokubun-replies"
            if (-not (Test-Path -LiteralPath $replyDir)) { New-Item -ItemType Directory -Path $replyDir | Out-Null }
            $replyPath = Join-Path $replyDir "$messageId.txt"
            Set-Content -LiteralPath $replyPath -Value $reply.text -Encoding UTF8

            $save = $SaveResearchMusings -or (Test-ResearchMusing -Text ([string]$record.content))
            & (Join-Path $ScriptRoot "post-discord-ai-chat-reply.ps1") `
                -MessageId $messageId `
                -ContentPath $replyPath `
                -ChannelId $recordChannelId `
                -Date $Date `
                -OriginalText ([string]$record.content) `
                -OriginalTimestamp ([string]$record.timestamp) `
                -ChannelName ([string]$record.channel) `
                -RepositoryRoot $RepositoryRoot `
                -StatePath $StatePath `
                -Source "event-openai" `
                -SaveResearchMusing:$save `
                -DryRun:$DryRun

            Add-StateRow -MessageId $messageId -ChannelIdValue $recordChannelId -Status "replied" -Source "event-openai" -Detail "OpenAI response posted." -ResponseId $reply.response_id
            $replied++
        } catch {
            Add-StateRow -MessageId $messageId -ChannelIdValue $recordChannelId -Status "failed" -Source "event-openai" -Detail $_.Exception.Message
            $failed++
            Write-Warning "AI chat reply failed for $messageId`: $($_.Exception.Message)"
        }
    }
} finally {
    Release-Lock -Path $lockPath
}

Write-Host "AI chat pending worker: mode=$Mode queued=$queued claimed=$claimed replied=$replied failed=$failed."

