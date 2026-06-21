param(
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$CategoryName,
    [switch]$CreateWebhooks,
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
if ([string]::IsNullOrWhiteSpace($CategoryName)) {
    $CategoryName = "📰 AI・数学ニュース"
}

$channelSpecs = @(
    [ordered]@{
        Name = "📰ai-news"
        Topic = "AI news, model releases, product updates, policy changes, and useful reading links."
        IdEnv = "DISCORD_AI_NEWS_CHANNEL_ID"
        NameEnv = "DISCORD_AI_NEWS_CHANNEL_NAME"
        WebhookEnv = "DISCORD_AI_NEWS_WEBHOOK_URL"
        WebhookName = "AI News Bot"
    },
    [ordered]@{
        Name = "📰math-news"
        Topic = "Mathematics news, papers, seminar links, surveys, and research trend notes."
        IdEnv = "DISCORD_MATH_NEWS_CHANNEL_ID"
        NameEnv = "DISCORD_MATH_NEWS_CHANNEL_NAME"
        WebhookEnv = "DISCORD_MATH_NEWS_WEBHOOK_URL"
        WebhookName = "Math News Bot"
    }
)

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
    $args = @(
        "-sS",
        "--connect-timeout", "8",
        "--max-time", "20",
        "-X", $methodName,
        "-H", "Authorization: Bot $BotToken",
        "-H", "Content-Type: application/json; charset=utf-8"
    )
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

function Ensure-Webhook {
    param(
        [object]$Channel,
        [object]$Spec
    )

    try {
        $webhooks = @(Invoke-DiscordJson -Method Get -Path "/channels/$($Channel.id)/webhooks")
        $webhook = $webhooks | Where-Object { $_.name -eq $Spec.WebhookName } | Select-Object -First 1
        if ($null -eq $webhook) {
            $webhook = Invoke-DiscordJson -Method Post -Path "/channels/$($Channel.id)/webhooks" -Body ([ordered]@{
                name = $Spec.WebhookName
            })
            Write-Host "Created webhook '$($Spec.WebhookName)' for channel '$($Channel.name)'."
        } else {
            Write-Host "Found webhook '$($Spec.WebhookName)' for channel '$($Channel.name)'."
        }

        if ($StoreInUserEnvironment -and -not [string]::IsNullOrWhiteSpace($webhook.url)) {
            [Environment]::SetEnvironmentVariable($Spec.WebhookEnv, [string]$webhook.url, "User")
        }
    } catch {
        Write-Warning "Could not ensure webhook '$($Spec.WebhookName)' for '$($Channel.name)': $($_.Exception.Message)"
    }
}

if ($DryRun) {
    Write-Host "Would ensure Discord category '$CategoryName' in guild $GuildId."
    foreach ($spec in $channelSpecs) {
        Write-Host "Would ensure Discord channel '$($spec.Name)' under '$CategoryName'."
        if ($CreateWebhooks) {
            Write-Host "Would ensure webhook '$($spec.WebhookName)' for '$($spec.Name)'."
        }
    }
    exit 0
}

$channels = @(Invoke-DiscordJson -Method Get -Path "/guilds/$GuildId/channels")
$storedCategoryId = [Environment]::GetEnvironmentVariable("DISCORD_NEWS_CATEGORY_ID", "User")
$category = $null
if (-not [string]::IsNullOrWhiteSpace($storedCategoryId)) {
    $category = $channels | Where-Object { [string]$_.id -eq $storedCategoryId } | Select-Object -First 1
}
if ($null -eq $category) {
    $category = $channels | Where-Object { $_.type -eq 4 -and $_.name -eq $CategoryName } | Select-Object -First 1
}
if ($null -eq $category) {
    $category = Invoke-DiscordJson -Method Post -Path "/guilds/$GuildId/channels" -Body ([ordered]@{
        name = $CategoryName
        type = 4
    })
    Write-Host "Created Discord category '$($category.name)' with id $($category.id)."
} else {
    Write-Host "Found Discord category '$($category.name)' with id $($category.id)."
}

if ($StoreInUserEnvironment) {
    [Environment]::SetEnvironmentVariable("DISCORD_NEWS_CATEGORY_ID", [string]$category.id, "User")
    [Environment]::SetEnvironmentVariable("DISCORD_NEWS_CATEGORY_NAME", [string]$category.name, "User")
}

$ensuredChannels = New-Object 'System.Collections.Generic.List[object]'
foreach ($spec in $channelSpecs) {
    $storedChannelId = [Environment]::GetEnvironmentVariable([string]$spec.IdEnv, "User")
    $channel = $null
    if (-not [string]::IsNullOrWhiteSpace($storedChannelId)) {
        $channel = $channels | Where-Object { [string]$_.id -eq $storedChannelId } | Select-Object -First 1
    }
    if ($null -eq $channel) {
        $channel = $channels | Where-Object { $_.type -eq 0 -and $_.name -eq $spec.Name } | Select-Object -First 1
    }
    if ($null -eq $channel) {
        $channel = Invoke-DiscordJson -Method Post -Path "/guilds/$GuildId/channels" -Body ([ordered]@{
            name = $spec.Name
            type = 0
            topic = $spec.Topic
            parent_id = $category.id
        })
        Write-Host "Created Discord channel '$($channel.name)' with id $($channel.id)."
    } else {
        if ([string]$channel.parent_id -ne [string]$category.id) {
            $channel = Invoke-DiscordJson -Method Patch -Path "/channels/$($channel.id)" -Body ([ordered]@{
                parent_id = $category.id
                topic = $spec.Topic
            })
            Write-Host "Moved Discord channel '$($channel.name)' under '$CategoryName'."
        } else {
            Write-Host "Found Discord channel '$($channel.name)' with id $($channel.id)."
        }
    }

    if ($StoreInUserEnvironment) {
        [Environment]::SetEnvironmentVariable($spec.IdEnv, [string]$channel.id, "User")
        [Environment]::SetEnvironmentVariable($spec.NameEnv, [string]$channel.name, "User")
    }

    if ($CreateWebhooks) {
        Ensure-Webhook -Channel $channel -Spec $spec
    }

    $ensuredChannels.Add($channel)
}

if ($PostUsageMessage) {
    $message = @(
        "News channels are ready.",
        "Use ai-news for AI model, tool, policy, and product updates.",
        "Use math-news for papers, seminars, surveys, and mathematical research news."
    ) -join "`n"
    foreach ($channel in @($ensuredChannels.ToArray())) {
        [void](Invoke-DiscordJson -Method Post -Path "/channels/$($channel.id)/messages" -Body ([ordered]@{ content = $message }))
    }
}

if ($StoreInUserEnvironment) {
    Write-Host "Updated Windows user environment for news channels."
}
