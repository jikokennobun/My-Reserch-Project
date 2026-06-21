param(
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$SelfUserId = $env:DISCORD_SELF_USER_ID,
    [string]$AiChatChannelId = $env:DISCORD_AI_CHAT_CHANNEL_ID,
    [string[]]$WatchChannelIds = @(),
    [string]$RepositoryRoot,
    [int]$MaxMinutes = 0,
    [bool]$QueueAiChat = $true,
    [bool]$ProcessNaturalLanguage = $true,
    [string]$AiReplyMode = $env:DISCORD_AI_REPLY_MODE,
    [int]$AiReplyMaxMessages = 1,
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

function Get-UserEnv {
    param([string]$Name, [string]$Current)
    if (-not [string]::IsNullOrWhiteSpace($Current)) { return $Current }
    return [Environment]::GetEnvironmentVariable($Name, "User")
}

$BotToken = Get-UserEnv -Name "DISCORD_BOT_TOKEN" -Current $BotToken
$GuildId = Get-UserEnv -Name "DISCORD_GUILD_ID" -Current $GuildId
$SelfUserId = Get-UserEnv -Name "DISCORD_SELF_USER_ID" -Current $SelfUserId
$AiChatChannelId = Get-UserEnv -Name "DISCORD_AI_CHAT_CHANNEL_ID" -Current $AiChatChannelId
if ([string]::IsNullOrWhiteSpace($AiReplyMode)) {
    $AiReplyMode = [Environment]::GetEnvironmentVariable("DISCORD_AI_REPLY_MODE", "User")
}
if ([string]::IsNullOrWhiteSpace($AiReplyMode)) {
    $AiReplyMode = "QueueOnly"
}
if ($AiReplyMode -notin @("QueueOnly", "OpenAI")) {
    throw "DISCORD_AI_REPLY_MODE / -AiReplyMode must be QueueOnly or OpenAI."
}

if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }
if ([string]::IsNullOrWhiteSpace($GuildId)) { throw "Set DISCORD_GUILD_ID or pass -GuildId." }
if (-not $AllowAnyAuthor -and [string]::IsNullOrWhiteSpace($SelfUserId)) {
    throw "Set DISCORD_SELF_USER_ID before event listening, or pass -AllowAnyAuthor explicitly."
}

$watchSet = New-Object 'System.Collections.Generic.HashSet[string]'
foreach ($id in @($WatchChannelIds)) {
    if (-not [string]::IsNullOrWhiteSpace([string]$id)) {
        [void]$watchSet.Add([string]$id)
    }
}

$statePath = Join-Path $RepositoryRoot "records\logs\discord-gateway-listener-state.csv"
$aiChatTriggerPath = Join-Path $RepositoryRoot "records\inbox\ai-chat\pending-trigger.json"

function Invoke-DiscordRest {
    param([string]$Path)
    $headers = @{
        Authorization = "Bot $BotToken"
        "User-Agent" = "codex-local-discord-event-listener"
    }
    return Invoke-RestMethod -Method Get -Uri "https://discord.com/api/v10$Path" -Headers $headers -TimeoutSec 20
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 24 -Compress)
}

function Add-JsonLine {
    param([string]$Path, [object]$Value)
    if ($DryRun) {
        Write-Host (ConvertTo-JsonLine -Value $Value)
        return
    }
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    Add-Content -LiteralPath $Path -Value (ConvertTo-JsonLine -Value $Value) -Encoding UTF8
}

function Get-JapanDate {
    param([string]$Timestamp)
    $dto = [DateTimeOffset]::Parse($Timestamp, [Globalization.CultureInfo]::InvariantCulture)
    return $dto.ToOffset([TimeSpan]::FromHours(9)).ToString("yyyy-MM-dd")
}

function Get-StateKeys {
    param([string]$Path)
    $keys = New-Object 'System.Collections.Generic.HashSet[string]'
    if (Test-Path -LiteralPath $Path) {
        foreach ($row in @(Import-Csv -LiteralPath $Path)) {
            if (-not [string]::IsNullOrWhiteSpace($row.MessageId)) {
                [void]$keys.Add([string]$row.MessageId)
            }
        }
    }
    return ,$keys
}

function Save-StateRow {
    param([string]$MessageId, [string]$ChannelId, [string]$Kind)
    if ($DryRun) { return }
    $dir = Split-Path -Parent $statePath
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    $row = [pscustomobject]@{
        MessageId = $MessageId
        ChannelId = $ChannelId
        Kind = $Kind
        SeenAt = (Get-Date).ToString("o")
    }
    if (Test-Path -LiteralPath $statePath) {
        $row | Export-Csv -LiteralPath $statePath -NoTypeInformation -Append -Encoding UTF8
    } else {
        $row | Export-Csv -LiteralPath $statePath -NoTypeInformation -Encoding UTF8
    }
}

function Save-AiChatTrigger {
    param([object]$Record, [string]$DateValue, [string]$PendingPath)
    if ($DryRun) { return }
    $dir = Split-Path -Parent $aiChatTriggerPath
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    $payload = [ordered]@{
        needs_response = $true
        date = $DateValue
        pending_path = $PendingPath
        message_id = [string]$Record.message_id
        channel_id = [string]$Record.channel_id
        channel = [string]$Record.channel
        timestamp = [string]$Record.timestamp
        updated_at = (Get-Date).ToString("o")
        source = "discord-gateway"
    }
    $payload | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $aiChatTriggerPath -Encoding UTF8
}

function Send-GatewayJson {
    param([System.Net.WebSockets.ClientWebSocket]$Socket, [object]$Payload)
    $json = $Payload | ConvertTo-Json -Depth 16 -Compress
    $bytes = [Text.Encoding]::UTF8.GetBytes($json)
    $segment = [ArraySegment[byte]]::new($bytes)
    [void]$Socket.SendAsync($segment, [System.Net.WebSockets.WebSocketMessageType]::Text, $true, [Threading.CancellationToken]::None).GetAwaiter().GetResult()
}

function Receive-GatewayJson {
    param([System.Net.WebSockets.ClientWebSocket]$Socket)
    $buffer = New-Object byte[] 65536
    $stream = [IO.MemoryStream]::new()
    try {
        do {
            $segment = [ArraySegment[byte]]::new($buffer)
            $task = $Socket.ReceiveAsync($segment, [Threading.CancellationToken]::None)
            while (-not $task.IsCompleted) {
                $waitMs = 1000
                if ($script:NextGatewayHeartbeatAt -is [DateTimeOffset]) {
                    $untilHeartbeat = ($script:NextGatewayHeartbeatAt - [DateTimeOffset]::UtcNow).TotalMilliseconds
                    $waitMs = [int][Math]::Max(1, [Math]::Min(1000, $untilHeartbeat))
                }
                if ($task.Wait($waitMs)) { break }
                if (
                    $script:GatewayHeartbeatIntervalMs -gt 0 -and
                    $script:NextGatewayHeartbeatAt -is [DateTimeOffset] -and
                    [DateTimeOffset]::UtcNow -ge $script:NextGatewayHeartbeatAt
                ) {
                    try {
                        Send-GatewayJson -Socket $Socket -Payload @{ op = 1; d = $script:GatewaySequence }
                    } catch {
                        Write-Warning "Gateway heartbeat failed: $($_.Exception.Message)"
                    }
                    $script:NextGatewayHeartbeatAt = [DateTimeOffset]::UtcNow.AddMilliseconds($script:GatewayHeartbeatIntervalMs)
                }
            }
            $result = $task.GetAwaiter().GetResult()
            if ($result.MessageType -eq [System.Net.WebSockets.WebSocketMessageType]::Close) {
                return $null
            }
            $stream.Write($buffer, 0, $result.Count)
        } while (-not $result.EndOfMessage)
        $text = [Text.Encoding]::UTF8.GetString($stream.ToArray())
        if ([string]::IsNullOrWhiteSpace($text)) { return $null }
        return ($text | ConvertFrom-Json)
    } finally {
        $stream.Dispose()
    }
}

$channelNames = @{}
try {
    foreach ($channel in @(Invoke-DiscordRest -Path "/guilds/$GuildId/channels")) {
        if ($channel.PSObject.Properties.Name -contains "id") {
            $channelNames[[string]$channel.id] = [string]$channel.name
        }
    }
} catch {
    Write-Warning "Could not load channel names: $($_.Exception.Message)"
}

$stateKeys = Get-StateKeys -Path $statePath
$gateway = Invoke-DiscordRest -Path "/gateway/bot"
$gatewayUrl = [string]$gateway.url
if ([string]::IsNullOrWhiteSpace($gatewayUrl)) { throw "Discord did not return a gateway URL." }

$socket = [System.Net.WebSockets.ClientWebSocket]::new()
$script:GatewaySocket = $socket
$script:GatewaySequence = $null
$script:GatewayHeartbeatIntervalMs = 0
$script:NextGatewayHeartbeatAt = $null
$startedAt = Get-Date

try {
    $uri = [Uri]::new("$gatewayUrl/?v=10&encoding=json")
    [void]$socket.ConnectAsync($uri, [Threading.CancellationToken]::None).GetAwaiter().GetResult()

    $hello = Receive-GatewayJson -Socket $socket
    if ($null -eq $hello -or [int]$hello.op -ne 10) { throw "Discord Gateway did not send Hello." }
    $interval = [int]$hello.d.heartbeat_interval
    if ($interval -lt 10000) { $interval = 40000 }
    $script:GatewayHeartbeatIntervalMs = $interval
    $script:NextGatewayHeartbeatAt = [DateTimeOffset]::UtcNow.AddMilliseconds($interval)

    $identify = @{
        op = 2
        d = @{
            token = $BotToken
            intents = 33281
            properties = @{
                os = "windows"
                browser = "codex-local"
                device = "codex-local"
            }
        }
    }
    Send-GatewayJson -Socket $socket -Payload $identify
    Save-StateRow -MessageId ("listener-start-" + [Guid]::NewGuid().ToString("N")) -ChannelId "" -Kind "listener-start"
    Write-Host "Discord event listener started. Press Ctrl+C to stop."

    while ($socket.State -eq [System.Net.WebSockets.WebSocketState]::Open) {
        if ($MaxMinutes -gt 0 -and ((Get-Date) - $startedAt).TotalMinutes -ge $MaxMinutes) { break }
        $payload = Receive-GatewayJson -Socket $socket
        if ($null -eq $payload) { break }
        if ($payload.PSObject.Properties.Name -contains "s" -and $null -ne $payload.s) {
            $script:GatewaySequence = [int]$payload.s
        }

        if ([int]$payload.op -eq 7) {
            Write-Warning "Discord requested reconnect. Restart this script."
            break
        }
        if ([int]$payload.op -eq 9) {
            Write-Warning "Discord invalidated the session. Restart this script."
            break
        }
        if ([int]$payload.op -ne 0 -or [string]$payload.t -ne "MESSAGE_CREATE") { continue }

        $message = $payload.d
        if ([string]$message.guild_id -ne [string]$GuildId) { continue }
        $channelId = [string]$message.channel_id
        if ($watchSet.Count -gt 0 -and -not $watchSet.Contains($channelId)) { continue }

        $messageId = [string]$message.id
        if ($stateKeys.Contains($messageId)) { continue }

        $authorId = [string]$message.author.id
        if (-not $AllowAnyAuthor -and $authorId -ne [string]$SelfUserId) { continue }
        if ($message.author.PSObject.Properties.Name -contains "bot" -and [bool]$message.author.bot) { continue }

        $timestamp = [string]$message.timestamp
        if ([string]::IsNullOrWhiteSpace($timestamp)) { $timestamp = (Get-Date).ToString("o") }
        $date = Get-JapanDate -Timestamp $timestamp
        $channelName = if ($channelNames.ContainsKey($channelId)) { $channelNames[$channelId] } else { $channelId }
        $attachments = @($message.attachments | ForEach-Object { [string]$_.url })
        $record = [pscustomobject][ordered]@{
            timestamp = $timestamp
            channel_id = $channelId
            channel = $channelName
            author = [string]$message.author.username
            author_id = $authorId
            message_id = $messageId
            content = [string]$message.content
            attachments = $attachments
            source = "discord-gateway"
        }

        $eventPath = Join-Path $RepositoryRoot "records\inbox\discord\events-$date.jsonl"
        Add-JsonLine -Path $eventPath -Value $record
        [void]$stateKeys.Add($messageId)
        Save-StateRow -MessageId $messageId -ChannelId $channelId -Kind "event"

        if ($QueueAiChat -and -not [string]::IsNullOrWhiteSpace($AiChatChannelId) -and $channelId -eq [string]$AiChatChannelId) {
            $pendingPath = Join-Path $RepositoryRoot "records\inbox\ai-chat\$date-pending.jsonl"
            Add-JsonLine -Path $pendingPath -Value $record
            Save-AiChatTrigger -Record $record -DateValue $date -PendingPath $pendingPath
            Save-StateRow -MessageId $messageId -ChannelId $channelId -Kind "ai-chat-pending"
            if ([string]::IsNullOrWhiteSpace([string]$message.content) -and @($message.attachments).Count -eq 0) {
                Write-Warning "AI chat event had empty content and no attachments. Check Message Content intent and channel permissions."
            }
            if ($AiReplyMode -ne "QueueOnly") {
                & (Join-Path $ScriptRoot "invoke-discord-ai-chat-pending.ps1") `
                    -Date $date `
                    -RepositoryRoot $RepositoryRoot `
                    -Mode $AiReplyMode `
                    -MaxMessages $AiReplyMaxMessages `
                    -SaveResearchMusings:$SaveResearchMusings `
                    -AllowAnyAuthor:$AllowAnyAuthor `
                    -DryRun:$DryRun
            }
        }

        if ($ProcessNaturalLanguage) {
            & (Join-Path $ScriptRoot "process-discord-codex-commands.ps1") `
                -Date $date `
                -RepositoryRoot $RepositoryRoot `
                -SourcePath $eventPath `
                -NaturalLanguage
        }
    }
} catch {
    Save-StateRow -MessageId ("listener-error-" + [Guid]::NewGuid().ToString("N")) -ChannelId "" -Kind "listener-error"
    throw "Discord event listener failed: $($_.Exception.Message)"
} finally {
    Save-StateRow -MessageId ("listener-stop-" + [Guid]::NewGuid().ToString("N")) -ChannelId "" -Kind "listener-stop"
    if ($null -ne $socket) {
        try {
            if ($socket.State -eq [System.Net.WebSockets.WebSocketState]::Open) {
                [void]$socket.CloseAsync([System.Net.WebSockets.WebSocketCloseStatus]::NormalClosure, "stopping", [Threading.CancellationToken]::None).GetAwaiter().GetResult()
            }
        } catch {
            Write-Warning "Could not close Discord Gateway cleanly: $($_.Exception.Message)"
        }
        $socket.Dispose()
    }
}

