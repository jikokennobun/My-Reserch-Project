param(
    [string]$WatchlistPath = (Join-Path (Resolve-Path (Join-Path $PSScriptRoot "..")).Path "references\chatgpt-share-watchlist.csv"),
    [string]$StatePath = (Join-Path (Resolve-Path (Join-Path $PSScriptRoot "..")).Path "logs\chatgpt-share-state.csv"),
    [string]$LogPath = (Join-Path (Resolve-Path (Join-Path $PSScriptRoot "..")).Path "logs\chatgpt-share-sync.md")
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

function Get-Sha256String {
    param([string]$Text)

    $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return (($sha.ComputeHash($bytes) | ForEach-Object { $_.ToString("x2") }) -join "")
    } finally {
        $sha.Dispose()
    }
}

function Get-ShareFingerprintText {
    param([string]$Html)

    $match = [regex]::Match($Html, 'streamController\.enqueue\("(?<payload>[\s\S]*?)"\);')
    if (-not $match.Success) {
        return $Html
    }

    $payload = $match.Groups["payload"].Value

    try {
        $decoded = ConvertFrom-Json ('"' + $payload + '"')
        $values = $decoded | ConvertFrom-Json
        $strings = @(
            $values | Where-Object {
                $_ -is [string] `
                    -and $_.Length -gt 40 `
                    -and $_ -notmatch '^https?://' `
                    -and $_ -notmatch '^/cdn/' `
                    -and $_ -notmatch '^/assets/' `
                    -and $_ -notmatch '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$' `
                    -and $_ -notmatch '^[0-9]+$'
            }
        )

        if ($strings.Count -gt 0) {
            return ($strings -join "`n---CHATGPT-SHARE-STRING---`n")
        }
    } catch {
        return $payload
    }

    return $payload
}

function Get-ShareTitle {
    param([string]$Html)

    $match = [regex]::Match($Html, '<title>(?<title>.*?)</title>')
    if (-not $match.Success) {
        return ""
    }

    $title = [System.Net.WebUtility]::HtmlDecode($match.Groups["title"].Value)
    return ($title -replace '^ChatGPT - ', '')
}

$watchlist = Import-Csv -Path $WatchlistPath

$stateByUrl = @{}
if (Test-Path $StatePath) {
    foreach ($row in (Import-Csv -Path $StatePath)) {
        $stateByUrl[$row.Url] = $row
    }
}

$now = (Get-Date).ToString("s")
$results = @()

foreach ($item in $watchlist) {
    try {
        $response = Invoke-WebRequest -Uri $item.Url -UseBasicParsing
        $html = $response.Content
        $fingerprintText = Get-ShareFingerprintText -Html $html
        $hash = Get-Sha256String -Text $fingerprintText
        $title = Get-ShareTitle -Html $html
        if ([string]::IsNullOrWhiteSpace($title)) {
            $title = $item.Title
        }

        $previous = $stateByUrl[$item.Url]
        $status = if ($null -eq $previous) {
            "new"
        } elseif ($previous.Hash -ne $hash) {
            "changed"
        } else {
            "unchanged"
        }

        $results += [pscustomobject]@{
            SourceKind = $item.SourceKind
            Title = $title
            Url = $item.Url
            NoteFile = $item.NoteFile
            Relay = $item.Relay
            Hash = $hash
            LastChecked = $now
            Status = $status
            Error = ""
        }
    } catch {
        $previous = $stateByUrl[$item.Url]
        $results += [pscustomobject]@{
            SourceKind = $item.SourceKind
            Title = $item.Title
            Url = $item.Url
            NoteFile = $item.NoteFile
            Relay = $item.Relay
            Hash = if ($null -ne $previous) { $previous.Hash } else { "" }
            LastChecked = $now
            Status = "error"
            Error = $_.Exception.Message
        }
    }
}

$stateDir = Split-Path -Parent $StatePath
if (-not (Test-Path $stateDir)) {
    New-Item -ItemType Directory -Path $stateDir | Out-Null
}

$results | Export-Csv -Path $StatePath -NoTypeInformation -Encoding UTF8

$logDir = Split-Path -Parent $LogPath
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir | Out-Null
}

$lines = @()
$lines += "## $now"
$lines += ""
$lines += "| Status | Title | Note | Url |"
$lines += "| --- | --- | --- | --- |"
foreach ($result in $results) {
    $safeTitle = $result.Title -replace '\|', '/'
    $lines += "| $($result.Status) | $safeTitle | $($result.NoteFile) | $($result.Url) |"
}
$lines += ""

if (Test-Path $LogPath) {
    $existing = Get-Content -Path $LogPath -Raw -Encoding UTF8
    ($lines -join "`n") + "`n" + $existing | Set-Content -Path $LogPath -Encoding UTF8
} else {
    "# ChatGPT Share Sync Log`n`n" + ($lines -join "`n") + "`n" | Set-Content -Path $LogPath -Encoding UTF8
}

$summary = $results | Group-Object Status | Sort-Object Name | ForEach-Object { "$($_.Name)=$($_.Count)" }
Write-Host "Checked $($results.Count) shared link(s): $($summary -join ', ')"
Write-Host "State: $StatePath"
Write-Host "Log: $LogPath"
