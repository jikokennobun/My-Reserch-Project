param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

if ([string]::IsNullOrWhiteSpace($GuildId)) {
    $GuildId = [Environment]::GetEnvironmentVariable("DISCORD_GUILD_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($GuildId)) {
    throw "Set DISCORD_GUILD_ID or pass -GuildId."
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    throw "Set DISCORD_BOT_TOKEN or pass -BotToken. Do not commit bot tokens."
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

try {
    $channels = Invoke-DiscordGetJson -Path "/guilds/$GuildId/channels" -Token $BotToken
} catch {
    Write-Host "Failed to list channels for guild $GuildId."
    if ($_.ErrorDetails) { Write-Host $_.ErrorDetails.Message } else { Write-Host $_.Exception.Message }
    Write-Host "Check that the bot is installed in the server and has View Channels / Read Message History permissions."
    throw
}

$channels |
    Sort-Object position |
    Select-Object @{Name="Name";Expression={$_.name}}, @{Name="Id";Expression={$_.id}}, @{Name="Type";Expression={$_.type}}, @{Name="ParentId";Expression={$_.parent_id}} |
    Format-Table -AutoSize
