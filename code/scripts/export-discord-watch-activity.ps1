param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$ChannelId = $env:DISCORD_WATCH_CHANNEL_ID,
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
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_WATCH_CHANNEL_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    Write-Host "DISCORD_WATCH_CHANNEL_ID is not configured. Skipping watch-log export."
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

function Get-Urls {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return @() }
    return @([regex]::Matches($Text, "https?://\S+") | ForEach-Object { $_.Value.TrimEnd(")", "]", ">", "。", "、", ",", ".") })
}

function Get-NormalizedUrlKey {
    param([string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) { return "" }
    $clean = $Url.Trim().TrimEnd(")", "]", ">", "。", "、", ",", ".")
    if ($clean -match "youtu\.be/([^?&#/]+)") { return "youtube:$($Matches[1])" }
    if ($clean -match "youtube(?:-nocookie)?\.com/.*[?&]v=([^?&#/]+)") { return "youtube:$($Matches[1])" }
    if ($clean -match "youtube(?:-nocookie)?\.com/(?:shorts|live|embed)/([^?&#/]+)") { return "youtube:$($Matches[1])" }
    return (($clean -replace "([?&])si=[^&#]+", '$1') -replace "[?&]+$", "").ToLowerInvariant()
}

function Get-WatchStatus {
    param(
        [string]$Text,
        [string]$DefaultStatus = "watched"
    )

    if ([string]::IsNullOrWhiteSpace($Text)) { return $DefaultStatus }
    if ($Text -match "\u307F\u305F\u3044|\u898B\u305F\u3044|\u898B\u3066\u306A\u3044|\u672A\u8996\u8074|\u898B\u3088\u3046|\u307E\u3060|want[- ]?to[- ]?watch|watch later|later") {
        return "want_to_watch"
    }
    if ($Text -match "\u90E8\u5206|\u9014\u4E2D|途中まで|見始めた|半分|partial") {
        return "partial"
    }
    if ($Text -match "\u307F\u305F|\u898B\u305F|\u8996\u8074\u6E08|見終わった|全部見た|完走|watched|done") {
        return "watched"
    }
    return $DefaultStatus
}

$start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
$end = $start.AddDays(1)

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\watch\$Date.jsonl"
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

        $content = [string]$message.content
        $attachmentUrls = @($message.attachments | ForEach-Object { $_.url })
        $urls = @(Get-Urls -Text $content) + $attachmentUrls

        $records.Add([ordered]@{
            date = $Date
            timestamp = $timestamp.ToString("o")
            channel_id = $ChannelId
            channel = $channel.name
            author = $message.author.username
            author_id = $message.author.id
            message_id = $message.id
            content = $content
            status = Get-WatchStatus -Text $content -DefaultStatus "watched"
            urls = @($urls | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
            attachments = $attachmentUrls
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
    Group-Object {
        $keys = @($_.urls | ForEach-Object { Get-NormalizedUrlKey -Url ([string]$_) } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -Unique)
        if ($keys.Count -gt 0) { ($keys -join "|") } else { "message:$($_.message_id)" }
    } |
    ForEach-Object {
        $_.Group | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } | Select-Object -Last 1
    } |
    Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
    ForEach-Object { ConvertTo-JsonLine -Value $_ } |
    Set-Content -LiteralPath $OutPath -Encoding UTF8

Write-Host "Exported $($records.Count) watch-log message(s) to $OutPath."


