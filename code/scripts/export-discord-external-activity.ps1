param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$StartDate,
    [string]$EndDate,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string[]]$IncludeGuildIds,
    [string[]]$ExcludeGuildIds,
    [string[]]$ExcludeGuildNames,
    [string]$TimeZoneOffset = "+09:00",
    [int]$MaxBatchesPerChannel = 20,
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

if ([string]::IsNullOrWhiteSpace($StartDate)) { $StartDate = $Date }
if ([string]::IsNullOrWhiteSpace($EndDate)) { $EndDate = $StartDate }

if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    throw "Set DISCORD_BOT_TOKEN or pass -BotToken."
}

function Split-EnvList {
    param([string]$Value)
    if ([string]::IsNullOrWhiteSpace($Value)) { return @() }
    return @($Value -split "," | ForEach-Object { $_.Trim() } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
}

if ($null -eq $IncludeGuildIds -or $IncludeGuildIds.Count -eq 0) {
    $IncludeGuildIds = @(Split-EnvList -Value ([Environment]::GetEnvironmentVariable("DISCORD_INCLUDE_GUILD_IDS", "User")))
}
if ($null -eq $ExcludeGuildIds -or $ExcludeGuildIds.Count -eq 0) {
    $ExcludeGuildIds = @(Split-EnvList -Value ([Environment]::GetEnvironmentVariable("DISCORD_EXCLUDED_GUILD_IDS", "User")))
}
if ($null -eq $ExcludeGuildIds -or $ExcludeGuildIds.Count -eq 0) {
    $primaryGuildId = [Environment]::GetEnvironmentVariable("DISCORD_GUILD_ID", "User")
    if (-not [string]::IsNullOrWhiteSpace($primaryGuildId)) {
        $ExcludeGuildIds = @($primaryGuildId.Trim())
    }
}
if ($null -eq $ExcludeGuildNames -or $ExcludeGuildNames.Count -eq 0) {
    $ExcludeGuildNames = @(Split-EnvList -Value ([Environment]::GetEnvironmentVariable("DISCORD_EXCLUDED_GUILD_NAMES", "User")))
}

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

function Test-ContainsString {
    param(
        [string[]]$Values,
        [string]$Needle
    )
    if ($null -eq $Values) { return $false }
    foreach ($value in $Values) {
        if ([string]::Equals($value, $Needle, [System.StringComparison]::OrdinalIgnoreCase)) {
            return $true
        }
    }
    return $false
}

$start = [DateTimeOffset]::Parse("$StartDate`T00:00:00$TimeZoneOffset")
$end = ([DateTimeOffset]::Parse("$EndDate`T00:00:00$TimeZoneOffset")).AddDays(1)

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $fileName = if ($StartDate -eq $EndDate) { "$StartDate.jsonl" } else { "$StartDate-$EndDate.jsonl" }
    $OutPath = Join-Path $RepositoryRoot "records\inbox\discord-external\$fileName"
}
$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$guilds = @(Invoke-DiscordGetJson -Path "/users/@me/guilds" -Token $BotToken)
$targetGuilds = New-Object 'System.Collections.Generic.List[object]'
foreach ($guild in $guilds) {
    $guildId = [string]$guild.id
    $guildName = [string]$guild.name

    if ($IncludeGuildIds.Count -gt 0 -and -not (Test-ContainsString -Values $IncludeGuildIds -Needle $guildId)) {
        continue
    }
    if (Test-ContainsString -Values $ExcludeGuildIds -Needle $guildId) {
        continue
    }
    if (Test-ContainsString -Values $ExcludeGuildNames -Needle $guildName) {
        continue
    }
    $targetGuilds.Add($guild)
}

$records = New-Object 'System.Collections.Generic.List[object]'
$skippedChannels = 0

foreach ($guild in $targetGuilds) {
    try {
        $channels = @(Invoke-DiscordGetJson -Path "/guilds/$($guild.id)/channels" -Token $BotToken)
    } catch {
        Write-Warning "Skipping guild $($guild.id): $($_.Exception.Message)"
        continue
    }

    $textChannels = @($channels | Where-Object { $_.type -eq 0 } | Sort-Object position)
    foreach ($channel in $textChannels) {
        $before = $null

        for ($batch = 0; $batch -lt $MaxBatchesPerChannel; $batch++) {
            $path = "/channels/$($channel.id)/messages?limit=100"
            if (-not [string]::IsNullOrWhiteSpace($before)) {
                $path += "&before=$before"
            }

            try {
                $messages = @(Invoke-DiscordGetJson -Path $path -Token $BotToken)
            } catch {
                $skippedChannels += 1
                break
            }
            if ($messages.Count -eq 0) { break }

            foreach ($message in $messages) {
                $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
                if ($null -eq $timestamp) { continue }
                if ($timestamp -ge $start -and $timestamp -lt $end) {
                    $records.Add([ordered]@{
                        timestamp = $timestamp.ToString("o")
                        guild_id = $guild.id
                        guild = $guild.name
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
}

$records |
    Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
    ForEach-Object { ConvertTo-JsonLine -Value $_ } |
    Set-Content -LiteralPath $OutPath -Encoding UTF8

Write-Host "Exported $($records.Count) external Discord message(s) from $($targetGuilds.Count) target guild(s) to $OutPath."
if ($skippedChannels -gt 0) {
    Write-Host "Skipped $skippedChannels channel(s) because the bot could not read them."
}
