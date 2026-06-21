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
    $OutPath = Join-Path $RepositoryRoot "records\research-triage\$Date.md"
}

$categories = [ordered]@{
    "Definitions" = @()
    "Propositions" = @()
    "Proof Plans" = @()
    "Questions" = @()
    "Literature" = @()
    "Ideas" = @()
}

function Add-Line {
    param([string]$Text)
    $clean = ($Text -replace "\s+", " ").Trim()
    if ([string]::IsNullOrWhiteSpace($clean)) { return }
    if ($clean.Length -gt 260) { $clean = $clean.Substring(0, 260) + "..." }
    if ($clean -match "定義|definition") { $categories["Definitions"] += $clean }
    elseif ($clean -match "命題|定理|補題|proposition|theorem|lemma") { $categories["Propositions"] += $clean }
    elseif ($clean -match "証明|示す|方針|proof|derive|導出") { $categories["Proof Plans"] += $clean }
    elseif ($clean -match "疑問|問題|なぜ|どう|\\?|？|question") { $categories["Questions"] += $clean }
    elseif ($clean -match "論文|文献|読む|arXiv|paper|ref\\.|@") { $categories["Literature"] += $clean }
    elseif ($clean -match "アイデア|思いつ|仮説|conjecture|idea") { $categories["Ideas"] += $clean }
}

foreach ($path in @(
    (Join-Path $RepositoryRoot "records\inbox\daily-packets\$Date.md"),
    (Join-Path $RepositoryRoot "records\daily\$Date.md"),
    (Join-Path $RepositoryRoot "records\logs\research-log.md")
)) {
    if (-not (Test-Path -LiteralPath $path)) { continue }
    foreach ($line in Get-Content -LiteralPath $path -Encoding UTF8) {
        Add-Line -Text $line
    }
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# Research Triage - $Date")
$lines.Add("")
foreach ($category in $categories.Keys) {
    $lines.Add("## $category")
    $lines.Add("")
    $items = @($categories[$category] | Select-Object -Unique | Select-Object -First 30)
    if ($items.Count -eq 0) {
        $lines.Add("- None.")
    } else {
        foreach ($item in $items) { $lines.Add("- $item") }
    }
    $lines.Add("")
}

($lines -join "`n") | Set-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Wrote research triage: $OutPath"

