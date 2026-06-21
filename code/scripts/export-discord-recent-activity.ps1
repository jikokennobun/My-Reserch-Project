param(
    [string]$StartDate = (Get-Date).AddDays(-6).ToString("yyyy-MM-dd"),
    [string]$EndDate = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$TimeZoneOffset = "+09:00",
    [int]$MaxBatchesPerChannel = 20,
    [int]$MaxSeconds = 75,
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

if ([string]::IsNullOrWhiteSpace($GuildId)) {
    $GuildId = [Environment]::GetEnvironmentVariable("DISCORD_GUILD_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($GuildId)) { throw "Set DISCORD_GUILD_ID or pass -GuildId." }
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }

function Invoke-DiscordGetJson {
    param(
        [string]$Path,
        [string]$Token
    )

    $raw = & curl.exe -sS --connect-timeout 8 --max-time 15 -H "Authorization: Bot $Token" "https://discord.com/api/v10$Path"
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

$start = [DateTimeOffset]::Parse("$StartDate`T00:00:00$TimeZoneOffset")
$end = ([DateTimeOffset]::Parse("$EndDate`T00:00:00$TimeZoneOffset")).AddDays(1)

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\discord\recent-$StartDate-$EndDate.jsonl"
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$deadline = if ($MaxSeconds -gt 0) { (Get-Date).AddSeconds($MaxSeconds) } else { [datetime]::MaxValue }
$channels = @(Invoke-DiscordGetJson -Path "/guilds/$GuildId/channels" -Token $BotToken)
$textChannels = @($channels | Where-Object { $_.type -eq 0 } | Sort-Object position)

$records = New-Object 'System.Collections.Generic.List[object]'

:channelLoop foreach ($channel in $textChannels) {
    if ((Get-Date) -ge $deadline) {
        Write-Warning "Stopping Discord recent activity export early after reaching MaxSeconds=$MaxSeconds."
        break channelLoop
    }
    $before = $null

    for ($batch = 0; $batch -lt $MaxBatchesPerChannel; $batch++) {
        if ((Get-Date) -ge $deadline) {
            Write-Warning "Stopping Discord recent activity export early after reaching MaxSeconds=$MaxSeconds."
            break channelLoop
        }
        $path = "/channels/$($channel.id)/messages?limit=100"
        if (-not [string]::IsNullOrWhiteSpace($before)) {
            $path += "&before=$before"
        }

        try {
            $messages = @(Invoke-DiscordGetJson -Path $path -Token $BotToken)
        } catch {
            Write-Warning "Skipping channel $($channel.name) ($($channel.id)): $($_.Exception.Message)"
            break
        }
        if ($messages.Count -eq 0) { break }

        foreach ($message in $messages) {
            $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
            if ($null -eq $timestamp) { continue }
            if ($timestamp -ge $start -and $timestamp -lt $end) {
                $records.Add([ordered]@{
                    timestamp = $timestamp.ToString("o")
                    channel_id = $channel.id
                    channel = $channel.name
                    author = $message.author.username
                    author_id = $message.author.id
                    author_is_bot = [bool]$message.author.bot
                    message_id = $message.id
                    content = $message.content
                    attachments = @($message.attachments | ForEach-Object { $_.url })
                })
            }
        }

        $oldest = $messages |
            Where-Object { $null -ne (Convert-DiscordTimestamp -Value $_.timestamp) } |
            Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
            Select-Object -First 1

        if ($null -eq $oldest) { break }
        if ((Convert-DiscordTimestamp -Value $oldest.timestamp) -lt $start) { break }
        $before = $oldest.id
    }
}

$records |
    Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
    ForEach-Object { ConvertTo-JsonLine -Value $_ } |
    Set-Content -LiteralPath $OutPath -Encoding UTF8

$summary = $records | Group-Object channel | Sort-Object Count -Descending | ForEach-Object {
    [pscustomobject]@{ Channel = $_.Name; Count = $_.Count }
}

Write-Host "Exported $($records.Count) Discord message(s) from $($textChannels.Count) channel(s) to $OutPath."
$summary | Format-Table -AutoSize
