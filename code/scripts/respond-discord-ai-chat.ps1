param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$ChannelId = $env:DISCORD_AI_CHAT_CHANNEL_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$OpenAIApiKey = $env:OPENAI_API_KEY,
    [string]$Model = $env:OPENAI_AI_CHAT_MODEL,
    [string]$SelfUserId = $env:DISCORD_SELF_USER_ID,
    [string]$TimeZoneOffset = "+09:00",
    [int]$MaxMessages = 5,
    [int]$IntervalSeconds = 30,
    [string]$RepositoryRoot,
    [string]$StatePath,
    [string]$ResearchInboxPath,
    [string]$ResearchLogPath,
    [switch]$ResearchMode,
    [switch]$SaveResearchMusings,
    [switch]$AllowAnyAuthor,
    [switch]$NoConversationState,
    [switch]$Loop,
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
if ([string]::IsNullOrWhiteSpace($OpenAIApiKey)) {
    $OpenAIApiKey = [Environment]::GetEnvironmentVariable("OPENAI_API_KEY", "User")
}
if ([string]::IsNullOrWhiteSpace($Model)) {
    $Model = [Environment]::GetEnvironmentVariable("OPENAI_AI_CHAT_MODEL", "User")
}
if ([string]::IsNullOrWhiteSpace($Model)) {
    $Model = "gpt-5.5"
}
if ([string]::IsNullOrWhiteSpace($SelfUserId)) {
    $SelfUserId = [Environment]::GetEnvironmentVariable("DISCORD_SELF_USER_ID", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}
if (-not [string]::IsNullOrWhiteSpace($OpenAIApiKey)) {
    $OpenAIApiKey = ([regex]::Replace($OpenAIApiKey, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) { throw "Set DISCORD_AI_CHAT_CHANNEL_ID or pass -ChannelId." }
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }
if (-not $AllowAnyAuthor -and [string]::IsNullOrWhiteSpace($SelfUserId)) {
    throw "Set DISCORD_SELF_USER_ID before running the AI chat responder, or pass -AllowAnyAuthor explicitly."
}
if ([string]::IsNullOrWhiteSpace($OpenAIApiKey) -and -not $DryRun) {
    throw "Set OPENAI_API_KEY. Do not paste API keys into chat or commit them."
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
        [string[]]$Headers,
        [object]$Body = $null
    )

    $methodName = $Method.ToUpperInvariant()
    $args = @("-sS", "-X", $methodName)
    foreach ($header in $Headers) {
        $args += @("-H", $header)
    }

    $bodyFile = $null
    if ($null -ne $Body) {
        $bodyFile = ConvertTo-JsonBodyFile -Body $Body
        $args += @("--data-binary", "@$bodyFile")
    }
    $args += $Uri

    try {
        $raw = & curl.exe @args
    } finally {
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path -LiteralPath $bodyFile)) {
            Remove-Item -LiteralPath $bodyFile -Force
        }
    }

    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $methodName $Uri." }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    return ($raw | ConvertFrom-Json)
}

function Invoke-DiscordJson {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null
    )

    $json = Invoke-JsonApi -Method $Method -Uri "https://discord.com/api/v10$Path" -Headers @(
        "Authorization: Bot $BotToken",
        "Content-Type: application/json; charset=utf-8"
    ) -Body $Body
    if ($null -ne $json -and $json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $Method $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Invoke-OpenAIResponse {
    param([object]$Body)

    $json = Invoke-JsonApi -Method Post -Uri "https://api.openai.com/v1/responses" -Headers @(
        "Authorization: Bearer $OpenAIApiKey",
        "Content-Type: application/json; charset=utf-8"
    ) -Body $Body
    if ($null -ne $json -and $json.PSObject.Properties.Name -contains "error") {
        throw "OpenAI API error: $($json.error.message)"
    }
    return $json
}

function Convert-DiscordTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
}

function Get-StateRows {
    if (-not (Test-Path -LiteralPath $StatePath)) { return @() }
    return @(Import-Csv -LiteralPath $StatePath)
}

function Save-StateRows {
    param([object[]]$Rows)

    if ($DryRun -or $Rows.Count -eq 0) { return }
    $dir = Split-Path -Parent $StatePath
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    if (Test-Path -LiteralPath $StatePath) {
        $Rows | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Append -Encoding UTF8
    } else {
        $Rows | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Encoding UTF8
    }
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
                $parts.Add([string]$content.text)
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

function Get-ResearchMusingTitle {
    param([string]$Text)

    $first = (($Text -split "\r?\n") | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($first)) { return "Discord math musing" }
    $first = ($first -replace "\s+", " ").Trim()
    if ($first.Length -gt 70) { $first = $first.Substring(0, 70) + "..." }
    return $first
}

function Add-ResearchMusing {
    param(
        [string]$InboxPath,
        [string]$LogPath,
        [string]$Text,
        [string]$Answer,
        [string]$DateValue,
        [string]$Timestamp,
        [string]$MessageId,
        [string]$ChannelName
    )

    if ($DryRun) {
        Write-Host "Would save research musing from Discord message $MessageId."
        return $true
    }

    $title = Get-ResearchMusingTitle -Text $Text
    $inboxDir = Split-Path -Parent $InboxPath
    if (-not (Test-Path -LiteralPath $inboxDir)) { New-Item -ItemType Directory -Path $inboxDir | Out-Null }

    if (Test-Path -LiteralPath $InboxPath) {
        $inboxLines = New-Object 'System.Collections.Generic.List[string]'
        foreach ($line in Get-Content -LiteralPath $InboxPath -Encoding UTF8) { $inboxLines.Add($line) }
    } else {
        $inboxLines = New-Object 'System.Collections.Generic.List[string]'
        $inboxLines.Add("# Idea Inbox")
        $inboxLines.Add("")
        $inboxLines.Add("## Unsorted")
    }

    if (-not ($inboxLines | Where-Object { $_ -match [regex]::Escape($MessageId) })) {
        $block = @(
            "",
            "### $DateValue - $title",
            "",
            ("Source: Discord AI chat " + $MessageId + " in " + $ChannelName + " at " + $Timestamp),
            "",
            "Musing:",
            $Text.Trim(),
            "",
            "AI reply:",
            $Answer.Trim(),
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
        Set-Content -LiteralPath $InboxPath -Encoding UTF8 -Value $inboxLines
    }

    $logDir = Split-Path -Parent $LogPath
    if (-not (Test-Path -LiteralPath $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
    if (-not (Test-Path -LiteralPath $LogPath)) {
        Set-Content -LiteralPath $LogPath -Encoding UTF8 -Value @("# Discord AI Chat Research Musings - $DateValue", "")
    }
    Add-Content -LiteralPath $LogPath -Encoding UTF8 -Value @(
        "",
        "## $Timestamp - $title",
        "",
        "MessageId: $MessageId",
        "Channel: $ChannelName",
        "",
        "Musing:",
        $Text.Trim(),
        "",
        "AI reply:",
        $Answer.Trim(),
        ""
    )
    return $true
}

function Invoke-AiChatOnce {
    $stateRows = @(Get-StateRows)
    $handled = New-Object 'System.Collections.Generic.HashSet[string]'
    foreach ($row in $stateRows) {
        if (-not [string]::IsNullOrWhiteSpace($row.MessageId)) {
            [void]$handled.Add([string]$row.MessageId)
        }
    }

    $botUser = Invoke-DiscordJson -Method Get -Path "/users/@me"
    $botUserId = [string]$botUser.id
    $channel = Invoke-DiscordJson -Method Get -Path "/channels/$ChannelId"

    $start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
    $end = $start.AddDays(1)
    $messages = @(Invoke-DiscordJson -Method Get -Path "/channels/$ChannelId/messages?limit=50")
    $targets = New-Object 'System.Collections.Generic.List[object]'

    foreach ($message in $messages) {
        $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
        if ($null -eq $timestamp) { continue }
        if ($timestamp -lt $start -or $timestamp -ge $end) { continue }
        $authorId = [string]$message.author.id
        if ($authorId -eq $botUserId) { continue }
        if (-not $AllowAnyAuthor -and -not [string]::IsNullOrWhiteSpace($SelfUserId) -and $authorId -ne $SelfUserId) { continue }
        if ($handled.Contains([string]$message.id)) { continue }
        if ([string]::IsNullOrWhiteSpace([string]$message.content) -and @($message.attachments).Count -eq 0) { continue }
        $targets.Add($message)
    }

    $newRows = New-Object 'System.Collections.Generic.List[object]'
    $latestResponseId = ""
    if (-not $NoConversationState) {
        $latest = $stateRows |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_.ResponseId) } |
            Sort-Object RepliedAt |
            Select-Object -Last 1
        if ($null -ne $latest) { $latestResponseId = [string]$latest.ResponseId }
    }

    foreach ($message in (@($targets.ToArray()) | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } | Select-Object -First $MaxMessages)) {
        $attachmentUrls = @($message.attachments | ForEach-Object { $_.url })
        $attachmentText = if ($attachmentUrls.Count -gt 0) { "`nAttachments:`n- " + ($attachmentUrls -join "`n- ") } else { "" }
        $userText = @(
            "Discord channel: $($channel.name)"
            "Timestamp: $($message.timestamp)"
            "Author: $($message.author.username)"
            ""
            [string]$message.content
            $attachmentText
        ) -join "`n"

        $isResearchMusing = Test-ResearchMusing -Text ([string]$message.content)
        $developerPromptParts = @(
            "You are a compact AI assistant replying inside a private Discord channel."
            "Your persona name is Jiko-Manzokubun, a private research companion for the user."
            "Reply in Japanese unless the user asks otherwise."
            "Use a friendly, direct style; avoid stiff honorific prose."
            "Be warm, specific, and concise."
            "You may help plan todos, study, research, daily reflection, or email triage."
            "Do not claim that you changed files, read private mail, or performed actions unless the user explicitly asks and the message context shows it."
            "When the user wants durable automation or file changes, tell them to ask Codex or use the codex-command channel."
        )
        if ($ResearchMode -or $isResearchMusing) {
            $developerPromptParts += @(
                "For mathematical musings, act like a careful mathematical survey partner."
                "Separate what seems known from what is only a conjectural connection."
                "Do not invent exact bibliographic citations."
                "If a citation or theorem name is uncertain, mark it as needing verification."
                "Use LaTeX-style notation such as $T \\vdash \\varphi$ and $\\Box(\\Box A \\to A) \\to \\Box A$ when it clarifies the point."
                "Discord does not render TeX reliably, so keep formulas short or put longer derivations in fenced code blocks."
                "Only include paper or source links when you can verify them from context or a reliable source; otherwise label them as search keywords, not citations."
                "Prefer this compact shape: quick reading, possible adjacent theories, search keywords or paper families, and next action."
                "When useful, suggest asking Codex for a source-backed literature survey."
            )
        }
        $developerPrompt = $developerPromptParts -join " "

        $input = @(
            [ordered]@{
                role = "developer"
                content = @([ordered]@{ type = "input_text"; text = $developerPrompt })
            },
            [ordered]@{
                role = "user"
                content = @([ordered]@{ type = "input_text"; text = $userText })
            }
        )

        $body = [ordered]@{
            model = $Model
            input = $input
            store = $true
        }
        if (-not $NoConversationState -and -not [string]::IsNullOrWhiteSpace($latestResponseId)) {
            $body.previous_response_id = $latestResponseId
        }

        if ($DryRun) {
            Write-Host "Would answer Discord message $($message.id) with model $Model."
            $responseId = ""
        } else {
            $response = Invoke-OpenAIResponse -Body $body
            $responseId = [string]$response.id
            $answer = Limit-DiscordContent -Text (Get-OutputText -Response $response)
            if ([string]::IsNullOrWhiteSpace($answer)) {
                $answer = "I could not generate a reply. Please send it again."
            }
            [void](Invoke-DiscordJson -Method Post -Path "/channels/$ChannelId/messages" -Body ([ordered]@{
                content = $answer
                message_reference = [ordered]@{
                    message_id = [string]$message.id
                    channel_id = $ChannelId
                    fail_if_not_exists = $false
                }
                allowed_mentions = [ordered]@{ parse = @() }
            }))
            $latestResponseId = $responseId
            if ($ResearchMode -or $SaveResearchMusings -or $isResearchMusing) {
                [void](Add-ResearchMusing -InboxPath $ResearchInboxPath -LogPath $ResearchLogPath -Text ([string]$message.content) -Answer $answer -DateValue $Date -Timestamp ([string]$message.timestamp) -MessageId ([string]$message.id) -ChannelName ([string]$channel.name))
            }
        }

        $newRows.Add([pscustomobject]@{
            MessageId = [string]$message.id
            ResponseId = $responseId
            ChannelId = $ChannelId
            Model = $Model
            RepliedAt = (Get-Date).ToString("o")
        })
    }

    Save-StateRows -Rows @($newRows.ToArray())
    Write-Host "AI chat handled $($newRows.Count) message(s)."
}

do {
    Invoke-AiChatOnce
    if (-not $Loop) { break }
    Start-Sleep -Seconds $IntervalSeconds
} while ($true)

