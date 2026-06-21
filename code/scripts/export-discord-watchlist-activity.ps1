param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$ChannelId = $env:DISCORD_WATCHLIST_CHANNEL_ID,
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
if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_WATCHLIST_CHANNEL_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    Write-Host "DISCORD_WATCHLIST_CHANNEL_ID is not configured. Skipping watchlist export."
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

function Read-JsonLines {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return @() }
    $items = @()
    foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $items += ($line | ConvertFrom-Json)
    }
    return $items
}

function Get-Urls {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return @() }
    return @([regex]::Matches($Text, "https?://\S+") | ForEach-Object { $_.Value.TrimEnd(")", "]", ">", ",", ".") })
}

function Get-NormalizedUrlKey {
    param([string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) { return "" }
    $clean = $Url.Trim().TrimEnd(")", "]", ">", ",", ".")
    if ($clean -match "youtu\.be/([^?&#/]+)") { return "youtube:$($Matches[1])" }
    if ($clean -match "youtube(?:-nocookie)?\.com/.*[?&]v=([^?&#/]+)") { return "youtube:$($Matches[1])" }
    if ($clean -match "youtube(?:-nocookie)?\.com/(?:shorts|live|embed)/([^?&#/]+)") { return "youtube:$($Matches[1])" }
    return (($clean -replace "([?&])si=[^&#]+", '$1') -replace "[?&]+$", "").ToLowerInvariant()
}

$start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
$end = $start.AddDays(1)

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\watch\$Date.jsonl"
}
$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$seen = New-Object 'System.Collections.Generic.HashSet[string]'
$seenUrlKeys = New-Object 'System.Collections.Generic.HashSet[string]'
foreach ($item in @(Read-JsonLines -Path $OutPath)) {
    if ($item.PSObject.Properties.Name -contains "message_id" -and -not [string]::IsNullOrWhiteSpace([string]$item.message_id)) {
        [void]$seen.Add([string]$item.message_id)
    }
    foreach ($url in @($item.urls)) {
        $key = Get-NormalizedUrlKey -Url ([string]$url)
        if (-not [string]::IsNullOrWhiteSpace($key)) { [void]$seenUrlKeys.Add($key) }
    }
}

$channel = Invoke-DiscordGetJson -Path "/channels/$ChannelId" -Token $BotToken
$records = New-Object 'System.Collections.Generic.List[object]'
$before = $null

for ($batch = 0; $batch -lt $MaxBatches; $batch++) {
    $path = "/channels/$ChannelId/messages?limit=100"
    if (-not [string]::IsNullOrWhiteSpace($before)) { $path += "&before=$before" }

    $messages = @(Invoke-DiscordGetJson -Path $path -Token $BotToken)
    if ($messages.Count -eq 0) { break }

    foreach ($message in $messages) {
        if ($message.author -and $message.author.bot) { continue }
        $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
        if ($null -eq $timestamp) { continue }
        if ($timestamp -lt $start -or $timestamp -ge $end) { continue }
        if ($seen.Contains([string]$message.id)) { continue }

        $content = [string]$message.content
        $attachmentUrls = @($message.attachments | ForEach-Object { $_.url })
        $urls = @(Get-Urls -Text $content) + $attachmentUrls
        $urlKeys = @($urls | ForEach-Object { Get-NormalizedUrlKey -Url ([string]$_) } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -Unique)
        if ($urlKeys.Count -gt 0 -and @($urlKeys | Where-Object { -not $seenUrlKeys.Contains($_) }).Count -eq 0) {
            continue
        }

        $records.Add([ordered]@{
            date = $Date
            timestamp = $timestamp.ToString("o")
            source = "discord-watchlist"
            channel_id = $ChannelId
            channel = $channel.name
            author = $message.author.username
            author_id = $message.author.id
            message_id = $message.id
            content = $content
            status = "want_to_watch"
            urls = @($urls | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
            attachments = $attachmentUrls
        })
        foreach ($key in $urlKeys) { [void]$seenUrlKeys.Add($key) }
    }

    $oldest = $messages |
        Where-Object { $null -ne (Convert-DiscordTimestamp -Value $_.timestamp) } |
        Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
        Select-Object -First 1

    if ($null -eq $oldest) { break }
    if ((Convert-DiscordTimestamp -Value $oldest.timestamp) -lt $start) { break }
    $before = $oldest.id
}

foreach ($record in ($records | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp })) {
    Add-Content -LiteralPath $OutPath -Encoding UTF8 -Value (ConvertTo-JsonLine -Value $record)
}

Write-Host "Exported $($records.Count) watchlist message(s) to $OutPath."
