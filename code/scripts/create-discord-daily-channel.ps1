param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$ChannelName = "daily-report",
    [string]$Topic = "Daily reports generated from Obsidian, Discord, YouTube, and repository activity.",
    [switch]$CreateWebhook,
    [string]$WebhookName = "Codex Daily Report",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

function Invoke-DiscordApi {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null
    )

    $headers = @{
        Authorization = "Bot $BotToken"
    }
    $uri = "https://discord.com/api/v10$Path"

    if ($null -eq $Body) {
        return Invoke-RestMethod -Method $Method -Uri $uri -Headers $headers
    }

    $json = $Body | ConvertTo-Json -Depth 12
    return Invoke-RestMethod -Method $Method -Uri $uri -Headers $headers -ContentType "application/json; charset=utf-8" -Body $json
}

if ([string]::IsNullOrWhiteSpace($GuildId)) {
    throw "Set DISCORD_GUILD_ID or pass -GuildId."
}

if ($DryRun) {
    Write-Host "Would ensure Discord text channel '$ChannelName' exists in guild $GuildId."
    if ($CreateWebhook) {
        Write-Host "Would create webhook '$WebhookName' for that channel."
    }
    exit 0
}

if ([string]::IsNullOrWhiteSpace($BotToken)) {
    throw "Set DISCORD_BOT_TOKEN or pass -BotToken. Do not commit bot tokens."
}
$BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()

$channels = Invoke-DiscordApi -Method Get -Path "/guilds/$GuildId/channels"
$channel = $channels | Where-Object { $_.name -eq $ChannelName -and $_.type -eq 0 } | Select-Object -First 1

if ($null -eq $channel) {
    $body = @{
        name = $ChannelName
        type = 0
        topic = $Topic
    }
    $channel = Invoke-DiscordApi -Method Post -Path "/guilds/$GuildId/channels" -Body $body
    Write-Host "Created Discord channel '$($channel.name)' with id $($channel.id)."
} else {
    Write-Host "Found existing Discord channel '$($channel.name)' with id $($channel.id)."
}

if ($CreateWebhook) {
    $webhook = Invoke-DiscordApi -Method Post -Path "/channels/$($channel.id)/webhooks" -Body @{ name = $WebhookName }
    Write-Host "Webhook URL follows. Store it in DISCORD_DAILY_WEBHOOK_URL and do not commit it."
    Write-Host $webhook.url
}
