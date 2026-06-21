param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$ChannelName = "ir自己満足文",
    [string]$Topic = "数学的ぼやき、研究相談、短いAI会話。OpenAI modeならここで自動返信。",
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
    Write-Host "Would ensure Discord AI chat channel '$ChannelName' in guild $GuildId."
    if ($StoreInUserEnvironment) {
        Write-Host "Would update DISCORD_AI_CHAT_CHANNEL_ID and DISCORD_AI_CHAT_CHANNEL_NAME."
    }
    exit 0
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$storedChannelId = [Environment]::GetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", "User")
$channel = $null
if (-not [string]::IsNullOrWhiteSpace($storedChannelId)) {
    $channel = $channels | Where-Object { [string]$_.id -eq $storedChannelId } | Select-Object -First 1
}
if ($null -eq $channel) {
    $channel = $channels | Where-Object { $_.type -eq 0 -and $_.name -eq $ChannelName } | Select-Object -First 1
}

$parentId = [Environment]::GetEnvironmentVariable("DISCORD_AI_AUTOMATION_CATEGORY_ID", "User")
if ([string]::IsNullOrWhiteSpace($parentId)) {
    $parentId = [Environment]::GetEnvironmentVariable("DISCORD_MAIL_ANNOUNCEMENT_CATEGORY_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($parentId)) {
    $dailyChannelId = [Environment]::GetEnvironmentVariable("DISCORD_DAILY_CHANNEL_ID", "User")
    if (-not [string]::IsNullOrWhiteSpace($dailyChannelId)) {
        $dailyChannel = $channels | Where-Object { $_.id -eq $dailyChannelId } | Select-Object -First 1
        if ($null -ne $dailyChannel -and -not [string]::IsNullOrWhiteSpace([string]$dailyChannel.parent_id)) {
            $parentId = $dailyChannel.parent_id
        }
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
    Write-Host "Created Discord AI chat channel '$($channel.name)' with id $($channel.id)."
} else {
    Write-Host "Found Discord AI chat channel '$($channel.name)' with id $($channel.id)."
}

if ($StoreInUserEnvironment) {
    [Environment]::SetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", [string]$channel.id, "User")
    [Environment]::SetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_NAME", [string]$channel.name, "User")
    Write-Host "Updated Windows user environment for AI chat channel."
}

if ($PostUsageMessage) {
    $usage = @(
        "AI chat channel is ready."
        ""
        "No-API mode: the Codex discord-command-poller automation can check this channel periodically and reply without separate OpenAI API billing."
        ""
        "Live local mode is optional and uses the paid OpenAI API. To enable live replies, set OPENAI_API_KEY in the Windows user environment and run:"
        "powershell -NoProfile -ExecutionPolicy Bypass -File .\code\scripts\respond-discord-ai-chat.ps1 -Loop"
        ""
        "Both modes only read this channel and write replies here."
    ) -join "`n"
    [void](Invoke-DiscordJson -Method Post -Path "/channels/$($channel.id)/messages" -Body ([ordered]@{ content = $usage }))
    Write-Host "Posted AI chat usage message."
}

Write-Host "AI chat channel: $($channel.name) ($($channel.id))"
