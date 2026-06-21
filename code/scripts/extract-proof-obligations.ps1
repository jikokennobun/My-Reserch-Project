param(
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
    $OutPath = Join-Path $RepositoryRoot "records\research-triage\proof-obligations.md"
}

$patterns = "TODO|未証明|要証明|要確認|証明が必要|未解決|conjecture|Conjecture|TODO proof|proof obligation|疑問"
$matches = @()
$researchFiles = Get-ChildItem -LiteralPath (Join-Path $RepositoryRoot "research") -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object { $_.Extension -in @(".md", ".tex") }
foreach ($file in @($researchFiles)) {
    $lineNo = 0
    foreach ($line in Get-Content -LiteralPath $file.FullName -Encoding UTF8) {
        $lineNo++
        if ($line -match $patterns) {
            $rel = Resolve-Path -LiteralPath $file.FullName -Relative
            $matches += [ordered]@{ File = $rel; Line = $lineNo; Text = ($line -replace "\s+", " ").Trim() }
        }
    }
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# Proof Obligations")
$lines.Add("")
$lines.Add("Generated: $(Get-Date -Format o)")
$lines.Add("")
if ($matches.Count -eq 0) {
    $lines.Add("- No proof obligations found by keyword scan.")
} else {
    foreach ($m in ($matches | Select-Object -First 200)) {
        $lines.Add("- `$($m.File):$($m.Line)` $($m.Text)")
    }
}

($lines -join "`n") | Set-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Wrote proof obligations: $OutPath"

