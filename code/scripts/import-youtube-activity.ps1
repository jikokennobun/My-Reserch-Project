param(
    [Parameter(Mandatory = $true)]
    [string[]]$Url,
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$Title,
    [string]$Channel,
    [string]$Notes,
    [string]$TranscriptPath,
    [switch]$FetchMetadata,
    [switch]$FetchTranscript,
    [switch]$SkipOEmbed,
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

function ConvertTo-JsonLine {
    param([object]$Value)

    return ($Value | ConvertTo-Json -Depth 16 -Compress)
}

function Test-YouTubeUrl {
    param([string]$Value)

    return ($Value -match "https?://(?:www\.)?(youtube\.com|youtu\.be|youtube-nocookie\.com)/")
}

function Resolve-YouTubeOEmbed {
    param([string]$Value)

    if (-not (Test-YouTubeUrl -Value $Value)) { return $null }

    $encoded = [Uri]::EscapeDataString($Value)
    $endpoint = "https://www.youtube.com/oembed?url=$encoded&format=json"
    try {
        $json = Invoke-RestMethod -Uri $endpoint -UseBasicParsing -ErrorAction Stop
        return [ordered]@{
            provider = "youtube"
            title = [string]$json.title
            channel = [string]$json.author_name
            author_url = [string]$json.author_url
            thumbnail_url = [string]$json.thumbnail_url
            fetched_at = (Get-Date).ToString("o")
        }
    } catch {
        Write-Warning "Could not fetch YouTube metadata for $Value`: $($_.Exception.Message)"
        return $null
    }
}

function Convert-VttToText {
    param(
        [string]$VttPath,
        [string]$TextPath
    )

    $seen = New-Object 'System.Collections.Generic.HashSet[string]'
    $lines = Get-Content -LiteralPath $VttPath -Encoding UTF8
    $clean = foreach ($line in $lines) {
        $value = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($value)) { continue }
        if ($value -eq "WEBVTT") { continue }
        if ($value -match "^Kind:") { continue }
        if ($value -match "^Language:") { continue }
        if ($value -match "^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->") { continue }
        if ($value -match "^\d+$") { continue }

        $value = $value -replace "<[^>]+>", ""
        $value = $value -replace "&amp;", "&"
        $value = $value -replace "&lt;", "<"
        $value = $value -replace "&gt;", ">"
        $value = $value.Trim()

        if (-not [string]::IsNullOrWhiteSpace($value) -and $seen.Add($value)) {
            $value
        }
    }

    $clean -join "`n" | Set-Content -LiteralPath $TextPath -Encoding UTF8
}

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\youtube\$Date.jsonl"
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

$ytDlp = Get-Command "yt-dlp" -ErrorAction SilentlyContinue
if (($FetchMetadata -or $FetchTranscript) -and $null -eq $ytDlp) {
    throw "yt-dlp is required for -FetchMetadata or -FetchTranscript. Install yt-dlp or run without those switches."
}

foreach ($videoUrl in $Url) {
    $metadata = $null
    $resolvedTitle = $Title
    $resolvedChannel = $Channel
    $resolvedTranscriptPath = $TranscriptPath

    if ($FetchMetadata) {
        $raw = & $ytDlp.Source --dump-json --skip-download --no-warnings $videoUrl
        $json = $raw | ConvertFrom-Json
        $resolvedTitle = if ([string]::IsNullOrWhiteSpace($resolvedTitle)) { $json.title } else { $resolvedTitle }
        $resolvedChannel = if ([string]::IsNullOrWhiteSpace($resolvedChannel)) { $json.uploader } else { $resolvedChannel }
        $description = [string]$json.description
        if ($description.Length -gt 2000) {
            $description = $description.Substring(0, 2000) + "...(truncated)"
        }
        $metadata = [pscustomobject][ordered]@{
            id = $json.id
            title = $json.title
            uploader = $json.uploader
            channel = $json.uploader
            duration = $json.duration
            webpage_url = $json.webpage_url
            description = $description
        }
    }

    if (-not $SkipOEmbed -and ([string]::IsNullOrWhiteSpace($resolvedTitle) -or [string]::IsNullOrWhiteSpace($resolvedChannel))) {
        $oembed = Resolve-YouTubeOEmbed -Value $videoUrl
        if ($null -ne $oembed) {
            $resolvedTitle = if ([string]::IsNullOrWhiteSpace($resolvedTitle)) { $oembed.title } else { $resolvedTitle }
            $resolvedChannel = if ([string]::IsNullOrWhiteSpace($resolvedChannel)) { $oembed.channel } else { $resolvedChannel }
            if ($null -eq $metadata) {
                $metadata = [pscustomobject]$oembed
            }
        }
    }

    if ($FetchTranscript) {
        $transcriptDir = Join-Path $RepositoryRoot "records\inbox\youtube\$Date"
        if (-not (Test-Path $transcriptDir)) {
            New-Item -ItemType Directory -Path $transcriptDir | Out-Null
        }

        $before = @(Get-ChildItem -LiteralPath $transcriptDir -Filter "*.vtt" -File -ErrorAction SilentlyContinue)
        & $ytDlp.Source --write-auto-subs --write-subs --sub-langs "ja,en.*" --sub-format "vtt" --skip-download -o (Join-Path $transcriptDir "%(id)s.%(ext)s") $videoUrl | Out-Null
        $after = @(Get-ChildItem -LiteralPath $transcriptDir -Filter "*.vtt" -File -ErrorAction SilentlyContinue)
        $newVtt = $after |
            Where-Object { $before.FullName -notcontains $_.FullName } |
            Sort-Object LastWriteTime -Descending |
            Select-Object -First 1

        if ($null -eq $newVtt) {
            $newVtt = $after | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        }

        if ($null -ne $newVtt) {
            $textPath = [System.IO.Path]::ChangeExtension($newVtt.FullName, ".txt")
            Convert-VttToText -VttPath $newVtt.FullName -TextPath $textPath
            $resolvedTranscriptPath = $textPath
        }
    }

    $record = [ordered]@{
        timestamp = (Get-Date).ToString("o")
        date = $Date
        url = $videoUrl
        title = $resolvedTitle
        channel = $resolvedChannel
        notes = $Notes
        transcript_path = $resolvedTranscriptPath
        metadata = $metadata
    }

    Add-Content -LiteralPath $OutPath -Encoding UTF8 -Value (ConvertTo-JsonLine -Value $record)
}

Write-Host "Queued $($Url.Count) YouTube item(s) in $OutPath."


