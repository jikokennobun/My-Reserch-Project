param(
    [string]$ChannelId = $env:DISCORD_DAILY_CHANNEL_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$TimeZoneOffset = "+09:00",
    [int]$MaxBatches = 20,
    [string]$RepositoryRoot,
    [string]$OutPath
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}

function Invoke-DiscordApi {
    param([string]$Path)

    $raw = & curl.exe -sS -H "Authorization: Bot $BotToken" "https://discord.com/api/v10$Path"
    if ($LASTEXITCODE -ne 0) {
        throw "curl.exe failed for $Path."
    }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Convert-DiscordTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) {
        return $null
    }
    return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
}

function ConvertTo-JsonLine {
    param([object]$Value)

    return ($Value | ConvertTo-Json -Depth 12 -Compress)
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_DAILY_CHANNEL_ID", "User")
}

if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    throw "Set DISCORD_DAILY_CHANNEL_ID or pass -ChannelId."
}

if ([string]::IsNullOrWhiteSpace($BotToken)) {
    throw "Set DISCORD_BOT_TOKEN or pass -BotToken. Do not commit bot tokens."
}

$start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
$end = $start.AddDays(1)

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\discord\$Date.jsonl"
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

$all = @()
$before = $null

for ($batch = 0; $batch -lt $MaxBatches; $batch++) {
    $path = "/channels/$ChannelId/messages?limit=100"
    if (-not [string]::IsNullOrWhiteSpace($before)) {
        $path += "&before=$before"
    }

    $messages = @(Invoke-DiscordApi -Path $path)
    if ($messages.Count -eq 0) {
        break
    }

    foreach ($message in $messages) {
        $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
        if ($null -eq $timestamp) {
            continue
        }
        if ($timestamp -ge $start -and $timestamp -lt $end) {
            $all += $message
        }
    }

    $oldest = $messages |
        Where-Object { $null -ne (Convert-DiscordTimestamp -Value $_.timestamp) } |
        Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
        Select-Object -First 1
    if ($null -eq $oldest) {
        break
    }

    if ((Convert-DiscordTimestamp -Value $oldest.timestamp) -lt $start) {
        break
    }

    $before = $oldest.id
}

$records = $all |
    Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
    ForEach-Object {
        $timestamp = Convert-DiscordTimestamp -Value $_.timestamp
        [ordered]@{
            timestamp = $timestamp.ToString("o")
            channel_id = $ChannelId
            author = $_.author.username
            author_id = $_.author.id
            author_is_bot = [bool]$_.author.bot
            message_id = $_.id
            content = $_.content
            attachments = @($_.attachments | ForEach-Object { $_.url })
        }
    }

$records | ForEach-Object { ConvertTo-JsonLine -Value $_ } | Set-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Exported $($records.Count) Discord message(s) to $OutPath."
