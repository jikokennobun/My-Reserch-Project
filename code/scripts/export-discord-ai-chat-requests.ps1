param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$ChannelId = $env:DISCORD_AI_CHAT_CHANNEL_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$SelfUserId = $env:DISCORD_SELF_USER_ID,
    [string]$TimeZoneOffset = "+09:00",
    [int]$MaxMessages = 10,
    [string]$RepositoryRoot,
    [string]$StatePath,
    [string]$OutPath,
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
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv"
}
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\ai-chat\$Date-pending.jsonl"
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if ([string]::IsNullOrWhiteSpace($SelfUserId)) {
    $SelfUserId = [Environment]::GetEnvironmentVariable("DISCORD_SELF_USER_ID", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) { throw "Set DISCORD_AI_CHAT_CHANNEL_ID or pass -ChannelId." }
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }
if (-not $AllowAnyAuthor -and [string]::IsNullOrWhiteSpace($SelfUserId)) {
    throw "Set DISCORD_SELF_USER_ID before exporting AI chat requests, or pass -AllowAnyAuthor explicitly."
}

function Invoke-DiscordJson {
    param([string]$Path)

    $raw = & curl.exe -sS --connect-timeout 8 --max-time 15 -H "Authorization: Bot $BotToken" "https://discord.com/api/v10$Path"
    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $Path." }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    $json = $raw | ConvertFrom-Json
    if ($null -ne $json -and $json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Convert-DiscordTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 24 -Compress)
}

function Get-HandledMessageIds {
    $ids = New-Object 'System.Collections.Generic.HashSet[string]'
    $paths = @(
        $StatePath,
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-codex-state.csv"),
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv")
    ) | Select-Object -Unique
    foreach ($path in $paths) {
        if (Test-Path -LiteralPath $path) {
            foreach ($row in @(Import-Csv -LiteralPath $path)) {
                if (-not [string]::IsNullOrWhiteSpace($row.MessageId)) {
                    [void]$ids.Add([string]$row.MessageId)
                }
            }
        }
    }
    return ,$ids
}

$botUser = Invoke-DiscordJson -Path "/users/@me"
$botUserId = [string]$botUser.id
$channel = Invoke-DiscordJson -Path "/channels/$ChannelId"

$start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
$end = $start.AddDays(1)
$handled = Get-HandledMessageIds
$messages = @(Invoke-DiscordJson -Path "/channels/$ChannelId/messages?limit=50")
$pending = New-Object 'System.Collections.Generic.List[object]'

foreach ($message in $messages) {
    $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
    if ($null -eq $timestamp) { continue }
    if ($timestamp -lt $start -or $timestamp -ge $end) { continue }

    $authorId = [string]$message.author.id
    if ($authorId -eq $botUserId) { continue }
    if (-not $AllowAnyAuthor -and -not [string]::IsNullOrWhiteSpace($SelfUserId) -and $authorId -ne $SelfUserId) { continue }
    if ($handled.Contains([string]$message.id)) { continue }
    if ([string]::IsNullOrWhiteSpace([string]$message.content) -and @($message.attachments).Count -eq 0) { continue }

    $attachmentUrls = @($message.attachments | ForEach-Object { [string]$_.url })
    $pending.Add([pscustomobject][ordered]@{
        timestamp = [string]$message.timestamp
        channel_id = $ChannelId
        channel = [string]$channel.name
        author = [string]$message.author.username
        author_id = $authorId
        message_id = [string]$message.id
        content = [string]$message.content
        attachments = $attachmentUrls
    })
}

$ordered = @($pending.ToArray()) | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } | Select-Object -First $MaxMessages

if (Test-Path -LiteralPath $OutPath) {
    $existing = New-Object 'System.Collections.Generic.List[object]'
    foreach ($line in Get-Content -LiteralPath $OutPath -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try { $existing.Add(($line | ConvertFrom-Json)) | Out-Null } catch {}
    }
    $byId = @{}
    foreach ($item in @($existing.ToArray()) + @($ordered)) {
        if (-not [string]::IsNullOrWhiteSpace([string]$item.message_id)) {
            $byId[[string]$item.message_id] = $item
        }
    }
    $ordered = @($byId.Values) | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } | Select-Object -First $MaxMessages
}

if ($DryRun) {
    Write-Host "Would export $(@($ordered).Count) pending AI chat request(s)."
    foreach ($item in @($ordered)) {
        Write-Host ("- " + $item.timestamp + " " + $item.message_id + " " + (($item.content -replace "\s+", " ").Trim()))
    }
    exit 0
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
@($ordered) | ForEach-Object { ConvertTo-JsonLine -Value $_ } | Set-Content -LiteralPath $OutPath -Encoding UTF8

Write-Host "Exported $(@($ordered).Count) pending AI chat request(s) to $OutPath."

