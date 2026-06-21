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
    $OutPath = Join-Path $RepositoryRoot "records\tasks\candidates\$Date.md"
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

function Add-Candidate {
    param(
        [System.Collections.Generic.List[object]]$List,
        [string]$Source,
        [string]$Timestamp,
        [string]$Text
    )

    if ([string]::IsNullOrWhiteSpace($Text)) { return }
    $clean = ($Text -replace "\s+", " ").Trim()
    if ($clean -match "~~|まだ収集|自動収集分|リポジトリ内の変更状況|日報材料として収集|確認した。$") {
        return
    }
    $clean = ($clean -replace "^\s*#{1,6}\s*", "").Trim()
    if ($clean.Length -gt 240) { $clean = $clean.Substring(0, 240) + "..." }
    if ($clean -notmatch "TODO|todo|やる|する|読む|見る|調べ|確認|返信|書く|作る|直す|行く|申請|登録|決める|要検討|要確認|next|follow up") {
        return
    }

    $List.Add([ordered]@{
        Source = $Source
        Timestamp = $Timestamp
        Text = $clean
    })
}

$candidates = New-Object 'System.Collections.Generic.List[object]'
$inboxRoot = Join-Path $RepositoryRoot "records\inbox"
foreach ($file in @(Get-ChildItem -LiteralPath $inboxRoot -Recurse -Filter "$Date.jsonl" -File -ErrorAction SilentlyContinue)) {
    $source = $file.Directory.Name
    foreach ($item in @(Read-JsonLines -Path $file.FullName)) {
        $text = ""
        if ($item.PSObject.Properties.Name -contains "content") { $text = [string]$item.content }
        elseif ($item.PSObject.Properties.Name -contains "summary") { $text = [string]$item.summary }
        elseif ($item.PSObject.Properties.Name -contains "text") { $text = [string]$item.text }
        elseif ($item.PSObject.Properties.Name -contains "subject") {
            $hints = @($item.task_hints) -join " / "
            $text = (([string]$item.subject) + " " + $hints).Trim()
        }
        Add-Candidate -List $candidates -Source $source -Timestamp ([string]$item.timestamp) -Text $text
    }
}

$dailyPath = Join-Path $RepositoryRoot "records\daily\$Date.md"
if (Test-Path -LiteralPath $dailyPath) {
    foreach ($line in Get-Content -LiteralPath $dailyPath -Encoding UTF8) {
        Add-Candidate -List $candidates -Source "daily" -Timestamp "" -Text $line
    }
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# TODO Candidates - $Date")
$lines.Add("")
$lines.Add('These are candidates only. Review before moving them into `records/tasks/todo.md`.')
$lines.Add("")
if ($candidates.Count -eq 0) {
    $lines.Add("- No candidates found.")
} else {
    $seen = New-Object 'System.Collections.Generic.HashSet[string]'
    foreach ($item in $candidates) {
        $key = $item.Text.ToLowerInvariant()
        if (-not $seen.Add($key)) { continue }
        $stamp = if ([string]::IsNullOrWhiteSpace($item.Timestamp)) { "" } else { " [$($item.Timestamp)]" }
        $lines.Add("- [ ]$stamp ($($item.Source)) $($item.Text)")
    }
}

($lines -join "`n") | Set-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Wrote TODO candidates: $OutPath"



