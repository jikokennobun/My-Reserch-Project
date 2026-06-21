param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$ChannelName,
    [string]$Topic = "Want-to-watch backlog. Post URLs, anime titles, streams, lectures, and short notes.",
    [switch]$StoreInUserEnvironment,
    [switch]$PostUsageMessage,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

if ([string]::IsNullOrWhiteSpace($ChannelName)) {
    $ChannelName = -join @([char]0x898B, [char]0x305F, [char]0x3044, [char]0x3082, [char]0x306E)
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

    $methodName = $Method.ToUpperInvariant()
    $uri = "https://discord.com/api/v10$Path"
    $args = @("-sS", "-X", $methodName, "-H", "Authorization: Bot $BotToken", "-H", "Content-Type: application/json; charset=utf-8")
    $bodyFile = $null
    if ($null -ne $Body) {
        $bodyFile = ConvertTo-JsonBodyFile -Body $Body
        $args += @("--data-binary", "@$bodyFile")
    }
    $args += $uri

    try {
        $raw = & curl.exe @args
    } finally {
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path -LiteralPath $bodyFile)) {
            Remove-Item -LiteralPath $bodyFile -Force
        }
    }

    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $methodName $Path." }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $methodName $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

if ($DryRun) {
    Write-Host "Would ensure Discord watchlist channel '$ChannelName' in guild $GuildId."
    exit 0
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$storedChannelId = [Environment]::GetEnvironmentVariable("DISCORD_WATCHLIST_CHANNEL_ID", "User")
$channel = $null
if (-not [string]::IsNullOrWhiteSpace($storedChannelId)) {
    $channel = $channels | Where-Object { [string]$_.id -eq $storedChannelId } | Select-Object -First 1
}
if ($null -eq $channel) {
    $channel = $channels | Where-Object { $_.type -eq 0 -and $_.name -eq $ChannelName } | Select-Object -First 1
}

$parentId = $null
$watchChannelId = [Environment]::GetEnvironmentVariable("DISCORD_WATCH_CHANNEL_ID", "User")
if (-not [string]::IsNullOrWhiteSpace($watchChannelId)) {
    $watchChannel = $channels | Where-Object { $_.id -eq $watchChannelId } | Select-Object -First 1
    if ($null -ne $watchChannel -and -not [string]::IsNullOrWhiteSpace([string]$watchChannel.parent_id)) {
        $parentId = $watchChannel.parent_id
    }
}
if ([string]::IsNullOrWhiteSpace($parentId)) {
    $dailyCategory = $channels | Where-Object { $_.type -eq 4 -and $_.name -eq "daily-report" } | Select-Object -First 1
    if ($null -ne $dailyCategory) { $parentId = $dailyCategory.id }
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
    Write-Host "Created Discord watchlist channel '$($channel.name)' with id $($channel.id)."
} else {
    Write-Host "Found Discord watchlist channel '$($channel.name)' with id $($channel.id)."
}

if ($StoreInUserEnvironment) {
    [Environment]::SetEnvironmentVariable("DISCORD_WATCHLIST_CHANNEL_ID", [string]$channel.id, "User")
    [Environment]::SetEnvironmentVariable("DISCORD_WATCHLIST_CHANNEL_NAME", [string]$channel.name, "User")
    Write-Host "Updated Windows user environment for watchlist channel."
}

if ($PostUsageMessage) {
    $usage = @(
        "Want-to-watch channel is ready."
        "Post URLs or titles here when you have not watched them yet."
        "Move/post to the watch-log channel after watching, or use !watch in codex-command."
    ) -join "`n"
    [void](Invoke-DiscordJson -Method Post -Path "/channels/$($channel.id)/messages" -Body ([ordered]@{ content = $usage }))
}

Write-Host "Watchlist channel: $($channel.name) ($($channel.id))"
