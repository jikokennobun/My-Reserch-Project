param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$ChannelId = $env:DISCORD_FOOD_CHANNEL_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$TimeZoneOffset = "+09:00",
    [int]$MaxBatches = 20,
    [string]$RepositoryRoot,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianDailySubdir,
    [string]$OutPath
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($ObsidianDailySubdir)) {
    $ObsidianDailySubdir = -join @([char]0x65E5, [char]0x5831)
}
if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_FOOD_CHANNEL_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) { throw "Set DISCORD_FOOD_CHANNEL_ID or pass -ChannelId." }
if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }

function Invoke-DiscordGetJson {
    param(
        [string]$Path,
        [string]$Token
    )

    $raw = & curl.exe -sS -H "Authorization: Bot $Token" "https://discord.com/api/v10$Path"
    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $Path." }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Convert-DiscordTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 16 -Compress)
}

function Test-ImageAttachment {
    param([object]$Attachment)

    $contentType = [string]$Attachment.content_type
    $fileName = [string]$Attachment.filename
    $url = [string]$Attachment.url

    if ($contentType -like "image/*") { return $true }
    if ($fileName -match "\.(jpg|jpeg|png|webp|gif)$") { return $true }
    if ($url -match "\.(jpg|jpeg|png|webp|gif)(\?|$)") { return $true }
    return $false
}

function Get-Extension {
    param([object]$Attachment)

    $fileName = [string]$Attachment.filename
    if (-not [string]::IsNullOrWhiteSpace($fileName)) {
        $ext = [IO.Path]::GetExtension($fileName)
        if (-not [string]::IsNullOrWhiteSpace($ext)) { return $ext.ToLowerInvariant() }
    }

    $url = [string]$Attachment.url
    try {
        $path = ([Uri]$url).AbsolutePath
        $ext = [IO.Path]::GetExtension($path)
        if (-not [string]::IsNullOrWhiteSpace($ext)) { return $ext.ToLowerInvariant() }
    } catch {}

    return ".jpg"
}

$start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
$end = $start.AddDays(1)

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\discord-food\$Date.jsonl"
}
$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$obsidianDailyDir = Join-Path $ObsidianVaultRoot $ObsidianDailySubdir
$assetRelativeDir = "_attachments/food/$Date"
$assetDir = Join-Path $obsidianDailyDir ($assetRelativeDir -replace "/", "\")
if (-not (Test-Path $assetDir)) { New-Item -ItemType Directory -Path $assetDir | Out-Null }

$records = New-Object 'System.Collections.Generic.List[object]'
$before = $null

for ($batch = 0; $batch -lt $MaxBatches; $batch++) {
    $path = "/channels/$ChannelId/messages?limit=100"
    if (-not [string]::IsNullOrWhiteSpace($before)) { $path += "&before=$before" }

    $messages = @(Invoke-DiscordGetJson -Path $path -Token $BotToken)
    if ($messages.Count -eq 0) { break }

    foreach ($message in $messages) {
        $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
        if ($null -eq $timestamp) { continue }
        if ($timestamp -lt $start -or $timestamp -ge $end) { continue }

        $attachments = @($message.attachments | Where-Object { Test-ImageAttachment -Attachment $_ })
        for ($i = 0; $i -lt $attachments.Count; $i++) {
            $attachment = $attachments[$i]
            $ext = Get-Extension -Attachment $attachment
            $stamp = $timestamp.ToString("HHmmss")
            $fileName = "$stamp-$($message.id)-$i$ext"
            $targetPath = Join-Path $assetDir $fileName
            $relativePath = "$assetRelativeDir/$fileName"

            & curl.exe -L -sS -o $targetPath $attachment.url
            if ($LASTEXITCODE -ne 0) { throw "Failed to download Discord attachment $($attachment.id)." }

            $records.Add([ordered]@{
                date = $Date
                timestamp = $timestamp.ToString("o")
                channel_id = $ChannelId
                author = $message.author.username
                author_id = $message.author.id
                message_id = $message.id
                content = $message.content
                attachment_id = $attachment.id
                attachment_url = $attachment.url
                content_type = $attachment.content_type
                file_name = $fileName
                obsidian_relative_path = $relativePath
                local_path = $targetPath
            })
        }
    }

    $oldest = $messages |
        Where-Object { $null -ne (Convert-DiscordTimestamp -Value $_.timestamp) } |
        Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
        Select-Object -First 1

    if ($null -eq $oldest) { break }
    if ((Convert-DiscordTimestamp -Value $oldest.timestamp) -lt $start) { break }
    $before = $oldest.id
}

$records |
    Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
    ForEach-Object { ConvertTo-JsonLine -Value $_ } |
    Set-Content -LiteralPath $OutPath -Encoding UTF8

Write-Host "Collected $($records.Count) food image(s) from Discord channel $ChannelId."
Write-Host "Manifest: $OutPath"
Write-Host "Obsidian assets: $assetDir"
