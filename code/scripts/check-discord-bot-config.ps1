param(
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$ChannelId = $env:DISCORD_DAILY_CHANNEL_ID
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_DAILY_CHANNEL_ID", "User")
}

if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

$result = [ordered]@{
    BotTokenConfigured = -not [string]::IsNullOrWhiteSpace($BotToken)
    DailyChannelId = $ChannelId
    BotUsername = $null
    BotId = $null
    ChannelReadable = $false
    ChannelName = $null
}

function Invoke-DiscordGetJson {
    param(
        [string]$Path,
        [string]$Token
    )

    $raw = & curl.exe -sS -H "Authorization: Bot $Token" "https://discord.com/api/v10$Path"
    if ($LASTEXITCODE -ne 0) {
        throw "curl.exe failed for $Path."
    }
    return $raw | ConvertFrom-Json
}

if (-not $result.BotTokenConfigured) {
    [pscustomobject]$result | Format-List
    throw "DISCORD_BOT_TOKEN is not configured."
}

$me = Invoke-DiscordGetJson -Path "/users/@me" -Token $BotToken
$result.BotUsername = $me.username
$result.BotId = $me.id

if (-not [string]::IsNullOrWhiteSpace($ChannelId)) {
    try {
        $channel = Invoke-DiscordGetJson -Path "/channels/$ChannelId" -Token $BotToken
        $result.ChannelReadable = $true
        $result.ChannelName = $channel.name
    } catch {
        $result.ChannelReadable = $false
        $result.ChannelName = "ERROR: $($_.ErrorDetails.Message)"
    }
}

[pscustomobject]$result | Format-List
