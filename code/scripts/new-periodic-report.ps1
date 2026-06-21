param(
    [ValidateSet("week", "month")]
    [string]$Period = "week",
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

$target = [datetime]::ParseExact($Date, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
if ($Period -eq "week") {
    $daysFromMonday = (([int]$target.DayOfWeek + 6) % 7)
    $start = $target.Date.AddDays(-$daysFromMonday)
    $end = $start.AddDays(6)
    $label = "$($start.ToString('yyyy-MM-dd'))-$($end.ToString('yyyy-MM-dd'))"
} else {
    $start = [datetime]::new($target.Year, $target.Month, 1)
    $end = $start.AddMonths(1).AddDays(-1)
    $label = $target.ToString("yyyy-MM")
}

if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\periodic\$Period-$label.md"
}

function Get-Section {
    param(
        [string]$Text,
        [string]$Heading
    )

    $match = [regex]::Match($Text, "(?ms)^#{1,6}[ \t]*$([regex]::Escape($Heading))[^\r\n]*\r?\n(.*?)(?=^#{1,6}[ \t]*\S|\z)")
    if ($match.Success) { return $match.Groups[1].Value.Trim() }
    return ""
}

$dailyDir = Join-Path $RepositoryRoot "records\daily"
$dailyFiles = @()
for ($d = $start; $d -le $end; $d = $d.AddDays(1)) {
    $p = Join-Path $dailyDir ($d.ToString("yyyy-MM-dd") + ".md")
    if (Test-Path -LiteralPath $p) { $dailyFiles += Get-Item -LiteralPath $p }
}

$lines = New-Object 'System.Collections.Generic.List[string]'
$title = if ($Period -eq "week") { "Weekly Report" } else { "Monthly Report" }
$lines.Add("# $title - $label")
$lines.Add("")
$lines.Add("Range: $($start.ToString('yyyy-MM-dd')) to $($end.ToString('yyyy-MM-dd'))")
$lines.Add("")
$lines.Add("## Overview")
$lines.Add("")
$lines.Add("- Daily reports included: $($dailyFiles.Count)")
$lines.Add("")
$lines.Add("## Done")
$lines.Add("")
$lines.Add("## Watched / Read")
$lines.Add("")
$lines.Add("## SNS / AI")
$lines.Add("")
$lines.Add("## Mood / Life")
$lines.Add("")
$lines.Add("## Next")
$lines.Add("")

foreach ($file in $dailyFiles) {
    $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    $day = [IO.Path]::GetFileNameWithoutExtension($file.Name)
    foreach ($pair in @(
        @{Heading="やった"; Target="Done"},
        @{Heading="読んだ/見た/知った"; Target="Watched / Read"},
        @{Heading="SNSでの活動"; Target="SNS / AI"},
        @{Heading="生成AIでの活動"; Target="SNS / AI"},
        @{Heading="精神状態"; Target="Mood / Life"},
        @{Heading="今日の感想"; Target="Mood / Life"}
    )) {
        $section = Get-Section -Text $text -Heading $pair.Heading
        if ([string]::IsNullOrWhiteSpace($section)) { continue }
        $idx = $lines.IndexOf("## $($pair.Target)")
        if ($idx -ge 0) {
            $insertAt = $idx + 2
            while ($insertAt -lt $lines.Count -and $lines[$insertAt] -notmatch "^## ") { $insertAt++ }
            $lines.Insert($insertAt, "")
            $lines.Insert($insertAt, ($section -split "\r?\n" | ForEach-Object { if ($_ -match "^\s*-") { "  $_" } else { "  - $_" } }) -join "`n")
            $lines.Insert($insertAt, "- $day")
        }
    }
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
($lines -join "`n") | Set-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Wrote $Period report: $OutPath"

