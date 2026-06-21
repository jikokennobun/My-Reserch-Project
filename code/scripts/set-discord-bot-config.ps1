param(
    [string]$ChannelId,
    [string]$GuildId,
    [switch]$IncludeResearchChannel
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

function Read-SecretText {
    param([string]$Prompt)

    $secure = Read-Host -Prompt $Prompt -AsSecureString
    $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
    try {
        return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
    } finally {
        if ($bstr -ne [IntPtr]::Zero) {
            [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
        }
    }
}

$token = Read-SecretText -Prompt "Paste Discord bot token"
$token = ([regex]::Replace($token, "\p{C}", "")).Trim()
if ([string]::IsNullOrWhiteSpace($token)) {
    throw "Bot token was empty."
}

[Environment]::SetEnvironmentVariable("DISCORD_BOT_TOKEN", $token, "User")

if (-not [string]::IsNullOrWhiteSpace($GuildId)) {
    [Environment]::SetEnvironmentVariable("DISCORD_GUILD_ID", $GuildId, "User")
}

if (-not [string]::IsNullOrWhiteSpace($ChannelId)) {
    [Environment]::SetEnvironmentVariable("DISCORD_DAILY_CHANNEL_ID", $ChannelId, "User")
}

if ($IncludeResearchChannel) {
    $researchChannelId = Read-Host -Prompt "Paste research Discord channel ID"
    if (-not [string]::IsNullOrWhiteSpace($researchChannelId)) {
        [Environment]::SetEnvironmentVariable("DISCORD_RESEARCH_CHANNEL_ID", $researchChannelId, "User")
    }
}

Write-Host "Saved Discord bot config to Windows user environment."
Write-Host "DISCORD_BOT_TOKEN: ***"
if (-not [string]::IsNullOrWhiteSpace($GuildId)) { Write-Host "DISCORD_GUILD_ID: $GuildId" }
if (-not [string]::IsNullOrWhiteSpace($ChannelId)) { Write-Host "DISCORD_DAILY_CHANNEL_ID: $ChannelId" }
if ($IncludeResearchChannel) { Write-Host "DISCORD_RESEARCH_CHANNEL_ID: $([Environment]::GetEnvironmentVariable('DISCORD_RESEARCH_CHANNEL_ID', 'User'))" }
