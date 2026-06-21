param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$ChannelName,
    [string]$ChannelNameFormat = "yyyy-M",
    [string]$Topic,
    [string]$WebhookName = "Codex Daily Report",
    [switch]$CreateWebhook,
    [switch]$StoreInUserEnvironment,
    [switch]$DryRun
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
    throw "Set DISCORD_BOT_TOKEN or pass -BotToken."
}

$targetDate = [datetime]::ParseExact($Date, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
if ([string]::IsNullOrWhiteSpace($ChannelName)) {
    $ChannelName = $targetDate.ToString($ChannelNameFormat, [Globalization.CultureInfo]::InvariantCulture).ToLowerInvariant()
}
if ([string]::IsNullOrWhiteSpace($Topic)) {
    $Topic = "Daily reports and activity logs for " + $targetDate.ToString("yyyy-MM", [Globalization.CultureInfo]::InvariantCulture) + "."
}

function ConvertTo-JsonBodyFile {
    param([object]$Body)

    $tmp = [IO.Path]::GetTempFileName()
    $json = $Body | ConvertTo-Json -Depth 16
    [IO.File]::WriteAllText($tmp, $json, [Text.UTF8Encoding]::new($false))
    return $tmp
}

function Invoke-DiscordJson {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null
    )

    $Method = $Method.ToUpperInvariant()
    $uri = "https://discord.com/api/v10$Path"
    $args = @("-sS", "-X", $Method, "-H", "Authorization: Bot $BotToken", "-H", "Content-Type: application/json; charset=utf-8")
    $bodyFile = $null
    if ($null -ne $Body) {
        $bodyFile = ConvertTo-JsonBodyFile -Body $Body
        $args += @("--data-binary", "@$bodyFile")
    }
    $args += $uri

    try {
        $raw = & curl.exe @args
    } finally {
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path $bodyFile)) {
            Remove-Item -LiteralPath $bodyFile -Force
        }
    }

    if ($LASTEXITCODE -ne 0) {
        throw "curl.exe failed for $Method $Path."
    }
    if ([string]::IsNullOrWhiteSpace($raw)) {
        return $null
    }

    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $Method $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

if ($DryRun) {
    Write-Host "Would ensure monthly Discord channel '$ChannelName' in guild $GuildId."
    if ($CreateWebhook) {
        Write-Host "Would ensure webhook '$WebhookName'."
    }
    if ($StoreInUserEnvironment) {
        Write-Host "Would update DISCORD_DAILY_CHANNEL_ID and DISCORD_DAILY_WEBHOOK_URL in the Windows user environment."
    }
    exit 0
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$channel = $channels | Where-Object { $_.type -eq 0 -and $_.name -eq $ChannelName } | Select-Object -First 1

$parentId = $null
$currentChannelId = [Environment]::GetEnvironmentVariable("DISCORD_DAILY_CHANNEL_ID", "User")
if (-not [string]::IsNullOrWhiteSpace($currentChannelId)) {
    $currentChannel = $channels | Where-Object { $_.id -eq $currentChannelId } | Select-Object -First 1
    if ($null -ne $currentChannel -and -not [string]::IsNullOrWhiteSpace([string]$currentChannel.parent_id)) {
        $parentId = $currentChannel.parent_id
    }
}

if ($null -eq $channel) {
    $body = [ordered]@{
        name = $ChannelName
        type = 0
        topic = $Topic
    }
    if (-not [string]::IsNullOrWhiteSpace($parentId)) {
        $body.parent_id = $parentId
    }
    $channel = Invoke-DiscordJson -Method Post -Path "/guilds/$GuildId/channels" -Body $body
    Write-Host "Created monthly Discord channel '$($channel.name)' with id $($channel.id)."
} else {
    Write-Host "Found monthly Discord channel '$($channel.name)' with id $($channel.id)."
}

$webhookUrl = $null
if ($CreateWebhook) {
    $webhooks = @()
    try {
        $webhooks = @(Invoke-DiscordJson -Method Get -Path "/channels/$($channel.id)/webhooks")
    } catch {
        $webhooks = @()
    }

    $webhook = $webhooks | Where-Object { $_.name -eq $WebhookName } | Select-Object -First 1
    if ($null -eq $webhook) {
        $webhook = Invoke-DiscordJson -Method Post -Path "/channels/$($channel.id)/webhooks" -Body @{ name = $WebhookName }
        Write-Host "Created webhook '$WebhookName' for '$($channel.name)'."
    } else {
        Write-Host "Found webhook '$WebhookName' for '$($channel.name)'."
    }

    if ($webhook.PSObject.Properties.Name -contains "url") {
        $webhookUrl = $webhook.url
    }
}

if ($StoreInUserEnvironment) {
    [Environment]::SetEnvironmentVariable("DISCORD_DAILY_CHANNEL_ID", [string]$channel.id, "User")
    [Environment]::SetEnvironmentVariable("DISCORD_DAILY_CHANNEL_NAME", [string]$channel.name, "User")
    if (-not [string]::IsNullOrWhiteSpace($webhookUrl)) {
        [Environment]::SetEnvironmentVariable("DISCORD_DAILY_WEBHOOK_URL", [string]$webhookUrl, "User")
    }
    Write-Host "Updated Windows user environment for monthly daily channel."
}

Write-Host "Monthly daily channel: $($channel.name) ($($channel.id))"
if ($CreateWebhook -and [string]::IsNullOrWhiteSpace($webhookUrl)) {
    Write-Host "Webhook URL was not available. The bot may need Manage Webhooks permission."
}
