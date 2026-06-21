param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("activity", "mood", "wake", "reflection")]
    [string]$LogKind,
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$ChannelId,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
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

$envName = switch ($LogKind) {
    "activity" { "DISCORD_ACTIVITY_CHANNEL_ID" }
    "mood" { "DISCORD_MOOD_CHANNEL_ID" }
    "wake" { "DISCORD_WAKE_CHANNEL_ID" }
    "reflection" { "DISCORD_REFLECTION_CHANNEL_ID" }
}
if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable($envName, "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    Write-Host "$envName is not configured. Skipping $LogKind export."
    exit 0
}
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }

function Invoke-DiscordGetJson {
    param(
        [string]$Path,
        [string]$Token
    )

    $raw = & curl.exe -sS -H "Authorization: Bot $Token" "https://discord.com/api/v10$Path"
    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $Path." }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
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
    return ($Value | ConvertTo-Json -Depth 16 -Compress)
}

$start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
$end = $start.AddDays(1)

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\$LogKind\$Date.jsonl"
}
$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$channel = Invoke-DiscordGetJson -Path "/channels/$ChannelId" -Token $BotToken
$records = New-Object 'System.Collections.Generic.List[object]'
$before = $null

for ($batch = 0; $batch -lt $MaxBatches; $batch++) {
    $path = "/channels/$ChannelId/messages?limit=100"
    if (-not [string]::IsNullOrWhiteSpace($before)) { $path += "&before=$before" }

    $messages = @(Invoke-DiscordGetJson -Path $path -Token $BotToken)
    if ($messages.Count -eq 0) { break }

    foreach ($message in $messages) {
        $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
        if ($null -eq $timestamp) { continue }
        if ($timestamp -lt $start -or $timestamp -ge $end) { continue }

        $records.Add([ordered]@{
            date = $Date
            kind = $LogKind
            timestamp = $timestamp.ToString("o")
            channel_id = $ChannelId
            channel = $channel.name
            author = $message.author.username
            author_id = $message.author.id
            author_is_bot = [bool]$message.author.bot
            message_id = $message.id
            content = [string]$message.content
            attachments = @($message.attachments | ForEach-Object { $_.url })
        })
    }

    $oldest = $messages |
        Where-Object { $null -ne (Convert-DiscordTimestamp -Value $_.timestamp) } |
        Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
        Select-Object -First 1

    if ($null -eq $oldest) { break }
    if ((Convert-DiscordTimestamp -Value $oldest.timestamp) -lt $start) { break }
    $before = $oldest.id
}

$records |
    Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
    ForEach-Object { ConvertTo-JsonLine -Value $_ } |
    Set-Content -LiteralPath $OutPath -Encoding UTF8

Write-Host "Exported $($records.Count) $LogKind message(s) to $OutPath."

