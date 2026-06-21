param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}

function Read-JsonLines {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) { return @() }

    $items = @()
    foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $items += ($line | ConvertFrom-Json)
    }
    return $items
}

function ConvertTo-JsonLine {
    param([object]$Value)

    return ($Value | ConvertTo-Json -Depth 24 -Compress)
}

function Copy-ToOrderedMap {
    param([object]$Item)

    $map = [ordered]@{}
    if ($null -eq $Item) { return $map }

    foreach ($property in $Item.PSObject.Properties) {
        $map[$property.Name] = $property.Value
    }
    return $map
}

function Get-Urls {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return @() }
    return @([regex]::Matches($Text, "https?://\S+") | ForEach-Object {
        $_.Value.TrimEnd(")", "]", ">", "。", "、", ",", ".")
    })
}

function Get-NormalizedUrlKey {
    param([string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) { return "" }
    $clean = $Url.Trim().TrimEnd(")", "]", ">", "。", "、", ",", ".")
    if ($clean -match "youtu\.be/([^?&#/]+)") { return "youtube:$($Matches[1])" }
    if ($clean -match "youtube(?:-nocookie)?\.com/.*[?&]v=([^?&#/]+)") { return "youtube:$($Matches[1])" }
    if ($clean -match "youtube(?:-nocookie)?\.com/(?:shorts|live|embed)/([^?&#/]+)") { return "youtube:$($Matches[1])" }
    return (($clean -replace "([?&])si=[^&#]+", '$1') -replace "[?&]+$", "").ToLowerInvariant()
}

function Test-YouTubeUrl {
    param([string]$Url)

    return ($Url -match "https?://(?:www\.)?(youtube\.com|youtu\.be|youtube-nocookie\.com)/")
}

function Resolve-YouTubeOEmbed {
    param([string]$Url)

    if (-not (Test-YouTubeUrl -Url $Url)) { return $null }

    $encoded = [Uri]::EscapeDataString($Url)
    $endpoint = "https://www.youtube.com/oembed?url=$encoded&format=json"
    try {
        $json = Invoke-RestMethod -Uri $endpoint -UseBasicParsing -ErrorAction Stop
        return [ordered]@{
            provider = "youtube"
            url = $Url
            title = [string]$json.title
            channel = [string]$json.author_name
            author_url = [string]$json.author_url
            thumbnail_url = [string]$json.thumbnail_url
            fetched_at = (Get-Date).ToString("o")
        }
    } catch {
        Write-Warning "Could not fetch YouTube metadata for $Url`: $($_.Exception.Message)"
        return $null
    }
}

function Merge-Metadata {
    param(
        [object]$Existing,
        [object]$Resolved
    )

    $metadata = [ordered]@{}
    if ($null -ne $Existing) {
        $keys = $null
        $values = $null
        foreach ($property in $Existing.PSObject.Properties) {
            if ($property.Name -eq "Keys") { $keys = @($property.Value) }
            elseif ($property.Name -eq "Values") { $values = @($property.Value) }
        }
        if ($null -ne $keys -and $null -ne $values -and $keys.Count -eq $values.Count) {
            for ($i = 0; $i -lt $keys.Count; $i++) {
                $metadata[[string]$keys[$i]] = $values[$i]
            }
        } else {
            foreach ($property in $Existing.PSObject.Properties) {
                $metadata[$property.Name] = $property.Value
            }
        }
    }
    if ($null -eq $Resolved) { return [pscustomobject]$metadata }

    foreach ($property in $Resolved.PSObject.Properties) {
        $metadata[$property.Name] = $property.Value
    }
    if (-not $metadata.Contains("uploader") -or [string]::IsNullOrWhiteSpace([string]$metadata["uploader"])) {
        $metadata["uploader"] = $Resolved.channel
    }
    return [pscustomobject]$metadata
}

function Enrich-YouTubeFile {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Host "No YouTube inbox file: $Path"
        return
    }

    $records = New-Object 'System.Collections.Generic.List[object]'
    foreach ($item in @(Read-JsonLines -Path $Path)) {
        $record = Copy-ToOrderedMap -Item $item
        $url = [string]$item.url
        $resolved = $null
        if (-not [string]::IsNullOrWhiteSpace($url)) {
            $needsTitle = [string]::IsNullOrWhiteSpace([string]$record["title"])
            $needsChannel = (-not $record.Contains("channel")) -or [string]::IsNullOrWhiteSpace([string]$record["channel"])
            if ($needsTitle -or $needsChannel) {
                $resolved = Resolve-YouTubeOEmbed -Url $url
            }
        }

        if ($null -ne $resolved) {
            if ([string]::IsNullOrWhiteSpace([string]$record["title"])) { $record["title"] = $resolved.title }
            if (-not $record.Contains("channel") -or [string]::IsNullOrWhiteSpace([string]$record["channel"])) { $record["channel"] = $resolved.channel }
        } elseif (-not $record.Contains("channel")) {
            $record["channel"] = ""
        }
        $record["metadata"] = Merge-Metadata -Existing $item.metadata -Resolved $resolved

        $records.Add($record)
    }

    if (-not $DryRun) {
        $records | ForEach-Object { ConvertTo-JsonLine -Value $_ } | Set-Content -LiteralPath $Path -Encoding UTF8
    }
    Write-Host "Enriched $($records.Count) YouTube record(s): $Path"
}

function Enrich-WatchFile {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Host "No watch inbox file: $Path"
        return
    }

    $records = New-Object 'System.Collections.Generic.List[object]'
    foreach ($item in @(Read-JsonLines -Path $Path)) {
        $record = Copy-ToOrderedMap -Item $item
        $urls = @($item.urls) + @(Get-Urls -Text ([string]$item.content))
        $uniqueUrls = @($urls |
            Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) } |
            Group-Object { Get-NormalizedUrlKey -Url ([string]$_) } |
            ForEach-Object { $_.Group | Select-Object -First 1 })
        $videos = New-Object 'System.Collections.Generic.List[object]'

        foreach ($url in $uniqueUrls) {
            $resolved = Resolve-YouTubeOEmbed -Url ([string]$url)
            if ($null -ne $resolved) {
                $videos.Add($resolved)
            } else {
                $videos.Add([ordered]@{
                    provider = "url"
                    url = [string]$url
                    title = ""
                    channel = ""
                })
            }
        }

        $record["videos"] = [object[]]$videos.ToArray()
        $records.Add($record)
    }

    $records = @($records |
        Sort-Object {
            try { [DateTimeOffset]::Parse([string]$_.timestamp, [Globalization.CultureInfo]::InvariantCulture) } catch { [DateTimeOffset]::MinValue }
        } |
        Group-Object {
            $keys = @($_.urls | ForEach-Object { Get-NormalizedUrlKey -Url ([string]$_) } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -Unique)
            if ($keys.Count -gt 0) { ($keys -join "|") } else { "message:$($_.message_id)" }
        } |
        ForEach-Object { $_.Group | Select-Object -Last 1 } |
        Sort-Object {
            try { [DateTimeOffset]::Parse([string]$_.timestamp, [Globalization.CultureInfo]::InvariantCulture) } catch { [DateTimeOffset]::MinValue }
        })

    if (-not $DryRun) {
        $records | ForEach-Object { ConvertTo-JsonLine -Value $_ } | Set-Content -LiteralPath $Path -Encoding UTF8
    }
    Write-Host "Enriched $($records.Count) watch record(s): $Path"
}

$youtubePath = Join-Path $RepositoryRoot "records\inbox\youtube\$Date.jsonl"
$watchPath = Join-Path $RepositoryRoot "records\inbox\watch\$Date.jsonl"

Enrich-YouTubeFile -Path $youtubePath
Enrich-WatchFile -Path $watchPath




