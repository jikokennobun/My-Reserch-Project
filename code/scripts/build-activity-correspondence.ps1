param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
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
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\links\$Date.md"
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

$watch = @(Read-JsonLines -Path (Join-Path $RepositoryRoot "records\inbox\watch\$Date.jsonl"))
$youtube = @(Read-JsonLines -Path (Join-Path $RepositoryRoot "records\inbox\youtube\$Date.jsonl"))
$ai = @(Read-JsonLines -Path (Join-Path $RepositoryRoot "records\inbox\ai\$Date.jsonl"))
$triagePath = Join-Path $RepositoryRoot "records\research-triage\$Date.md"

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# Activity Correspondence - $Date")
$lines.Add("")
$lines.Add("| Time | Source | Item | Possible follow-up |")
$lines.Add("| --- | --- | --- | --- |")

foreach ($item in $watch) {
    $text = ([string]$item.content -replace "\s+", " ").Trim()
    $safeText = $text -replace "\|", "/"
    $lines.Add(('| {0} | watch | {1} | connect to research note or daily impression |' -f $item.timestamp, $safeText))
}
foreach ($item in $youtube) {
    $title = if ([string]::IsNullOrWhiteSpace($item.title)) { $item.url } else { $item.title }
    $safeTitle = ([string]$title) -replace "\|", "/"
    $lines.Add(('| {0} | youtube | {1} | note what changed in understanding |' -f $item.timestamp, $safeTitle))
}
foreach ($item in $ai) {
    $summary = ([string]$item.summary -replace "\s+", " ").Trim()
    $safeSummary = $summary -replace "\|", "/"
    $lines.Add(('| {0} | ai | {1} | decide if it should become a durable note |' -f $item.timestamp, $safeSummary))
}
if (Test-Path -LiteralPath $triagePath) {
    $lines.Add("")
    $lines.Add("## Related Research Triage")
    $lines.Add("")
    $lines.Add("- See ``$triagePath``")
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
($lines -join "`n") | Set-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Wrote activity correspondence: $OutPath"

