param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
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
if ([string]::IsNullOrWhiteSpace($GuildId)) { throw "Set DISCORD_GUILD_ID or pass -GuildId." }
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }

$channelSpecs = @(
    [ordered]@{
        Name = "活動ログ"
        Topic = "日報素材になる日中の活動メモ。雑でOK。例: 鹿島先生にSlackで連絡した / 図書館で院試勉強した"
        IdEnv = "DISCORD_ACTIVITY_CHANNEL_ID"
        NameEnv = "DISCORD_ACTIVITY_CHANNEL_NAME"
    },
    [ordered]@{
        Name = "気分ログ"
        Topic = "朝昼晩の気分、点数、短い理由を投げる。例: 朝: 60 眠い"
        IdEnv = "DISCORD_MOOD_CHANNEL_ID"
        NameEnv = "DISCORD_MOOD_CHANNEL_NAME"
    },
    [ordered]@{
        Name = "起床ログ"
        Topic = "起床・睡眠・活動開始の記録。例: 起床 08:15 / 睡眠 6h"
        IdEnv = "DISCORD_WAKE_CHANNEL_ID"
        NameEnv = "DISCORD_WAKE_CHANNEL_NAME"
    },
    [ordered]@{
        Name = "振り返り"
        Topic = "夜の振り返り質問への回答や、今日のよかったこと、明日に回すこと。"
        IdEnv = "DISCORD_REFLECTION_CHANNEL_ID"
        NameEnv = "DISCORD_REFLECTION_CHANNEL_NAME"
    }
)

function Find-DiscordChannel {
    param(
        [object[]]$Channels,
        [object]$Spec
    )

    $storedId = [Environment]::GetEnvironmentVariable([string]$Spec.IdEnv, "User")
    if (-not [string]::IsNullOrWhiteSpace($storedId)) {
        $byId = $Channels | Where-Object { [string]$_.id -eq $storedId } | Select-Object -First 1
        if ($null -ne $byId) { return $byId }
    }

    return ($Channels | Where-Object { $_.type -eq 0 -and $_.name -eq $Spec.Name } | Select-Object -First 1)
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
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path $bodyFile)) {
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
    foreach ($spec in $channelSpecs) {
        Write-Host "Would ensure Discord channel '$($spec.Name)' in guild $GuildId."
    }
    exit 0
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$parentId = [Environment]::GetEnvironmentVariable("DISCORD_LIFE_LOG_CATEGORY_ID", "User")
$dailyCategory = $channels | Where-Object { $_.type -eq 4 -and $_.name -eq "daily-report" } | Select-Object -First 1
if ([string]::IsNullOrWhiteSpace($parentId) -and $null -ne $dailyCategory) {
    $parentId = $dailyCategory.id
}

foreach ($spec in $channelSpecs) {
    $channel = Find-DiscordChannel -Channels $channels -Spec $spec
    if ($null -eq $channel) {
        $body = [ordered]@{
            name = $spec.Name
            type = 0
            topic = $spec.Topic
        }
        if (-not [string]::IsNullOrWhiteSpace($parentId)) {
            $body.parent_id = $parentId
        }
        $channel = Invoke-DiscordJson -Method Post -Path "/guilds/$GuildId/channels" -Body $body
        Write-Host "Created Discord channel '$($channel.name)' with id $($channel.id)."
    } else {
        Write-Host "Found Discord channel '$($channel.name)' with id $($channel.id)."
    }

    if ($StoreInUserEnvironment) {
        [Environment]::SetEnvironmentVariable($spec.IdEnv, [string]$channel.id, "User")
        [Environment]::SetEnvironmentVariable($spec.NameEnv, [string]$channel.name, "User")
    }
}

if ($StoreInUserEnvironment) {
    Write-Host "Updated Windows user environment for life-log channels."
}

