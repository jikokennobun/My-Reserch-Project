param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$ChannelName = "aicodex-command",
    [string]$Topic = "Post Codex commands here: !todo, !watch, !mood, !research.",
    [switch]$StoreInUserEnvironment,
    [switch]$PostUsageMessage,
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
    Write-Host "Would ensure Discord command channel '$ChannelName' in guild $GuildId."
    if ($StoreInUserEnvironment) {
        Write-Host "Would update DISCORD_COMMAND_CHANNEL_ID and DISCORD_COMMAND_CHANNEL_NAME."
    }
    if ($PostUsageMessage) {
        Write-Host "Would post command usage message."
    }
    exit 0
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$storedChannelId = [Environment]::GetEnvironmentVariable("DISCORD_COMMAND_CHANNEL_ID", "User")
$channel = $null
if (-not [string]::IsNullOrWhiteSpace($storedChannelId)) {
    $channel = $channels | Where-Object { [string]$_.id -eq $storedChannelId } | Select-Object -First 1
}
if ($null -eq $channel) {
    $channel = $channels | Where-Object { $_.type -eq 0 -and $_.name -eq $ChannelName } | Select-Object -First 1
}

$parentId = [Environment]::GetEnvironmentVariable("DISCORD_AI_AUTOMATION_CATEGORY_ID", "User")
$dailyChannelId = [Environment]::GetEnvironmentVariable("DISCORD_DAILY_CHANNEL_ID", "User")
if ([string]::IsNullOrWhiteSpace($parentId) -and -not [string]::IsNullOrWhiteSpace($dailyChannelId)) {
    $dailyChannel = $channels | Where-Object { $_.id -eq $dailyChannelId } | Select-Object -First 1
    if ($null -ne $dailyChannel -and -not [string]::IsNullOrWhiteSpace([string]$dailyChannel.parent_id)) {
        $parentId = $dailyChannel.parent_id
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
    Write-Host "Created Discord command channel '$($channel.name)' with id $($channel.id)."
} else {
    Write-Host "Found Discord command channel '$($channel.name)' with id $($channel.id)."
}

if ($StoreInUserEnvironment) {
    [Environment]::SetEnvironmentVariable("DISCORD_COMMAND_CHANNEL_ID", [string]$channel.id, "User")
    [Environment]::SetEnvironmentVariable("DISCORD_COMMAND_CHANNEL_NAME", [string]$channel.name, "User")
    Write-Host "Updated Windows user environment for command channel."
}

if ($PostUsageMessage) {
    $usage = @(
        "Codex command channel is ready."
        ""
        "Use:"
        "!todo submit report by Friday"
        "!done submit report"
        "!watch https://youtu.be/... | memo"
        "!later https://youtu.be/... | want to watch"
        "!mood morning: 70 focused"
        "!mood noon: 55 tired"
        "!mood night: 60 calm"
        "!research title | idea memo"
        ""
        "Japanese text is OK in the command body."
    ) -join "`n"
    [void](Invoke-DiscordJson -Method Post -Path "/channels/$($channel.id)/messages" -Body ([ordered]@{ content = $usage }))
    Write-Host "Posted command usage message."
}

Write-Host "Command channel: $($channel.name) ($($channel.id))"
