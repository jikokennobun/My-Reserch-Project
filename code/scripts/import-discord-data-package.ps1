param(
    [Parameter(Mandatory = $true)]
    [string]$SourcePath,
    [string]$GuildId,
    [string]$GuildName,
    [string]$ChannelName,
    [string]$StartDate,
    [string]$EndDate,
    [string]$RepositoryRoot,
    [string]$OutPath
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}

function Get-PropertyValue {
    param(
        [object]$Object,
        [string[]]$Names
    )

    if ($null -eq $Object) { return $null }
    foreach ($name in $Names) {
        $prop = $Object.PSObject.Properties | Where-Object { $_.Name -eq $name } | Select-Object -First 1
        if ($null -ne $prop) { return $prop.Value }
    }
    return $null
}

function Read-Json {
    param([string]$Path)
    return (Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json)
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 16 -Compress)
}

function Test-MatchFilter {
    param(
        [string]$Value,
        [string]$Filter
    )

    if ([string]::IsNullOrWhiteSpace($Filter)) { return $true }
    if ([string]::IsNullOrWhiteSpace($Value)) { return $false }
    return $Value -like "*$Filter*"
}

function Convert-Attachments {
    param([object]$Value)

    if ($null -eq $Value) { return @() }
    if ($Value -is [array]) { return @($Value | ForEach-Object { [string]$_ } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) }
    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return @() }
    return @($text -split "[,\s]+" | Where-Object { $_ -match "^https?://" })
}

function Convert-MessageTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    try {
        return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
    } catch {
        return $null
    }
}

$resolvedSource = Resolve-Path -LiteralPath $SourcePath
$workingRoot = $resolvedSource.Path
$cleanupRoot = $null

if ((Test-Path -LiteralPath $workingRoot -PathType Leaf) -and ([IO.Path]::GetExtension($workingRoot) -ieq ".zip")) {
    $cleanupRoot = Join-Path ([IO.Path]::GetTempPath()) ("discord-data-package-" + [guid]::NewGuid().ToString("n"))
    New-Item -ItemType Directory -Path $cleanupRoot | Out-Null
    Expand-Archive -LiteralPath $workingRoot -DestinationPath $cleanupRoot -Force
    $workingRoot = $cleanupRoot
}

try {
    $messagesRoot = Join-Path $workingRoot "messages"
    if (-not (Test-Path -LiteralPath $messagesRoot -PathType Container)) {
        throw "Could not find a 'messages' folder under $workingRoot."
    }

    $channelIndex = @{}
    $indexPath = Join-Path $messagesRoot "index.json"
    if (Test-Path -LiteralPath $indexPath) {
        $index = Read-Json -Path $indexPath
        foreach ($prop in $index.PSObject.Properties) {
            $channelIndex[$prop.Name] = $prop.Value
            $channelIndex[($prop.Name -replace "^c", "")] = $prop.Value
        }
    }

    $start = $null
    $end = $null
    if (-not [string]::IsNullOrWhiteSpace($StartDate)) {
        $start = [DateTimeOffset]::Parse("$StartDate`T00:00:00+09:00")
    }
    if (-not [string]::IsNullOrWhiteSpace($EndDate)) {
        $end = ([DateTimeOffset]::Parse("$EndDate`T00:00:00+09:00")).AddDays(1)
    }

    $records = New-Object 'System.Collections.Generic.List[object]'
    $folders = @(Get-ChildItem -LiteralPath $messagesRoot -Directory)

    foreach ($folder in $folders) {
        $folderChannelId = ($folder.Name -replace "^c", "")
        $metadata = $null
        $metadataPath = Join-Path $folder.FullName "channel.json"
        if (Test-Path -LiteralPath $metadataPath) {
            $metadata = Read-Json -Path $metadataPath
        }

        $indexValue = if ($channelIndex.ContainsKey($folder.Name)) { $channelIndex[$folder.Name] } elseif ($channelIndex.ContainsKey($folderChannelId)) { $channelIndex[$folderChannelId] } else { $null }

        $metaGuildId = [string](Get-PropertyValue -Object $metadata -Names @("guild_id", "guildId", "Guild ID", "guild.id"))
        $metaGuildName = [string](Get-PropertyValue -Object $metadata -Names @("guild_name", "guildName", "Guild Name", "guild.name"))
        $metaChannelId = [string](Get-PropertyValue -Object $metadata -Names @("id", "channel_id", "channelId", "Channel ID"))
        $metaChannelName = [string](Get-PropertyValue -Object $metadata -Names @("name", "channel_name", "channelName", "Channel Name"))

        if ([string]::IsNullOrWhiteSpace($metaChannelId)) { $metaChannelId = $folderChannelId }
        if ([string]::IsNullOrWhiteSpace($metaChannelName) -and $null -ne $indexValue) { $metaChannelName = [string]$indexValue }

        if (-not (Test-MatchFilter -Value $metaGuildId -Filter $GuildId)) { continue }
        if (-not (Test-MatchFilter -Value $metaGuildName -Filter $GuildName)) { continue }
        if (-not (Test-MatchFilter -Value $metaChannelName -Filter $ChannelName)) { continue }

        $messageFiles = @(
            Join-Path $folder.FullName "messages.json"
            Join-Path $folder.FullName "messages.csv"
        ) | Where-Object { Test-Path -LiteralPath $_ }

        foreach ($messageFile in $messageFiles) {
            $messages = @()
            if ([IO.Path]::GetExtension($messageFile) -ieq ".csv") {
                $messages = @(Import-Csv -LiteralPath $messageFile -Encoding UTF8)
            } else {
                $messages = @(Read-Json -Path $messageFile)
            }

            foreach ($message in $messages) {
                $timestamp = Convert-MessageTimestamp -Value (Get-PropertyValue -Object $message -Names @("Timestamp", "timestamp", "created_at", "Created At"))
                if ($null -eq $timestamp) { continue }
                if ($null -ne $start -and $timestamp -lt $start) { continue }
                if ($null -ne $end -and $timestamp -ge $end) { continue }

                $records.Add([ordered]@{
                    timestamp = $timestamp.ToString("o")
                    source = "discord-data-package"
                    guild_id = $metaGuildId
                    guild = $metaGuildName
                    channel_id = $metaChannelId
                    channel = $metaChannelName
                    message_id = [string](Get-PropertyValue -Object $message -Names @("ID", "id", "message_id"))
                    content = [string](Get-PropertyValue -Object $message -Names @("Contents", "contents", "content"))
                    attachments = @(Convert-Attachments -Value (Get-PropertyValue -Object $message -Names @("Attachments", "attachments")))
                })
            }
        }
    }

    if ([string]::IsNullOrWhiteSpace($OutPath)) {
        $suffix = if (-not [string]::IsNullOrWhiteSpace($StartDate) -and -not [string]::IsNullOrWhiteSpace($EndDate)) { "$StartDate-$EndDate" } elseif (-not [string]::IsNullOrWhiteSpace($StartDate)) { $StartDate } else { (Get-Date).ToString("yyyy-MM-dd") }
        $OutPath = Join-Path $RepositoryRoot "records\inbox\discord-data-package\$suffix.jsonl"
    }
    $outDir = Split-Path -Parent $OutPath
    if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

    $records |
        Sort-Object { Convert-MessageTimestamp -Value $_.timestamp } |
        ForEach-Object { ConvertTo-JsonLine -Value $_ } |
        Set-Content -LiteralPath $OutPath -Encoding UTF8

    Write-Host "Imported $($records.Count) Discord data-package message(s) to $OutPath."
} finally {
    if (-not [string]::IsNullOrWhiteSpace($cleanupRoot) -and (Test-Path -LiteralPath $cleanupRoot)) {
        Remove-Item -LiteralPath $cleanupRoot -Recurse -Force
    }
}
