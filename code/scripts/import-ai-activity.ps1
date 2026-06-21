param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$Tool = "Codex",
    [string]$Summary,
    [string]$Details,
    [string]$Url,
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
    $OutPath = Join-Path $RepositoryRoot "records\inbox\ai\$Date.jsonl"
}

if ([string]::IsNullOrWhiteSpace($Summary) -and [string]::IsNullOrWhiteSpace($Details) -and [string]::IsNullOrWhiteSpace($Url)) {
    throw "Provide -Summary, -Details, or -Url."
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$record = [ordered]@{
    date = $Date
    timestamp = (Get-Date).ToString("o")
    tool = $Tool
    summary = $Summary
    details = $Details
    url = $Url
}

($record | ConvertTo-Json -Depth 8 -Compress) | Add-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Queued AI activity: $OutPath"
