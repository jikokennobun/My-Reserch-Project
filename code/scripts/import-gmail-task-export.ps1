param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$SourcePath,
    [string]$RepositoryRoot,
    [string]$OutPath,
    [string]$TaskReportPath,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianTaskSubdir = "Tasks\メール",
    [switch]$IncludeAllDates,
    [switch]$SyncObsidian,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\gmail\$Date.jsonl"
}
if ([string]::IsNullOrWhiteSpace($TaskReportPath)) {
    $TaskReportPath = Join-Path $RepositoryRoot "records\tasks\mail\$Date.md"
}

function Get-DefaultExportDirectory {
    $myDriveName = -join ([char[]](0x30de, 0x30a4, 0x30c9, 0x30e9, 0x30a4, 0x30d6))
    $candidates = @(
        (Join-Path $env:USERPROFILE "$myDriveName\Codex Gmail Task Export"),
        (Join-Path $env:USERPROFILE "My Drive\Codex Gmail Task Export"),
        (Join-Path $env:USERPROFILE "Google Drive\My Drive\Codex Gmail Task Export")
    )
    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath $candidate) { return $candidate }
    }
    return $candidates[0]
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 24 -Compress)
}

function Read-ExportFile {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) { return @() }
    $json = Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "records") {
        return @($json.records)
    }
    return @($json)
}

function Get-SourceFiles {
    param([string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) {
        $Path = Get-DefaultExportDirectory
    }
    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Host "No Gmail export source found: $Path"
        return @()
    }

    $item = Get-Item -LiteralPath $Path
    if (-not $item.PSIsContainer) {
        return @($item)
    }

    $exact = Join-Path $item.FullName "mail-tasks-$Date.json"
    if (Test-Path -LiteralPath $exact) {
        return @(Get-Item -LiteralPath $exact)
    }
    $legacyExact = Join-Path $item.FullName "university-mail-tasks-$Date.json"
    if (Test-Path -LiteralPath $legacyExact) {
        return @(Get-Item -LiteralPath $legacyExact)
    }

    $latest = @(Get-ChildItem -LiteralPath $item.FullName -Filter "mail-tasks-*.json" -File |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1)
    if ($latest.Count -gt 0) { return $latest }

    return @(Get-ChildItem -LiteralPath $item.FullName -Filter "university-mail-tasks-*.json" -File |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1)
}

function Get-ShortLine {
    param(
        [string]$Text,
        [int]$MaxChars = 220
    )
    if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
    $value = ($Text -replace "\s+", " ").Trim()
    if ($value.Length -gt $MaxChars) { return $value.Substring(0, $MaxChars) + "..." }
    return $value
}

function Get-MailTaskLine {
    param([object]$Item)

    $subject = Get-ShortLine -Text ([string]$Item.subject) -MaxChars 120
    $from = Get-ShortLine -Text ([string]$Item.from) -MaxChars 80
    $kind = Get-MailKindLabel -Item $Item
    $hints = @($Item.task_hints | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
    $hintText = if ($hints.Count -gt 0) { " / " + (($hints | Select-Object -First 2) -join " / ") } else { "" }
    return "- [ ] [$kind] $subject$hintText `n  - from: $from / received: $($Item.received_at)"
}

function Get-MailKindLabel {
    param([object]$Item)

    $kind = ""
    if ($null -ne $Item -and $Item.PSObject.Properties.Name -contains "kind") {
        $kind = [string]$Item.kind
    }
    switch ($kind) {
        "tutoring" { return "塾講師バイト" }
        "university" { return "大学" }
        default { return "メール" }
    }
}

function Test-MailTaskRecord {
    param(
        [object]$Item,
        [string]$TargetDate
    )

    if ($null -eq $Item) { return $false }
    if (-not $IncludeAllDates -and $Item.PSObject.Properties.Name -contains "date") {
        $recordDate = [string]$Item.date
        if (-not [string]::IsNullOrWhiteSpace($recordDate) -and $recordDate -ne $TargetDate) {
            return $false
        }
    }

    $from = ([string]$Item.from).ToLowerInvariant()
    $subject = [string]$Item.subject
    $snippet = [string]$Item.snippet
    $text = "$subject`n$snippet"

    if ($subject -match "^\s*\[TEST\]" -or $text -match "Codex/Obsidian automation test mail|実際の課題・締切・提出依頼ではありません") {
        return $false
    }
    if ($from -match "no-reply@accounts\.google\.com" -and $text -match "セキュリティ通知|security|ログイン|アカウント") {
        return $false
    }
    if ($from -match "mail@tnews\.jp" -and $text -match "メールマガジン|新着|おすすめ|求人|Pick Up") {
        return $false
    }
    if ($from -match "donotreply@indeed\.com|noreply@.*indeed|townwork|baitoru|mynavi|rikunabi" -and $text -match "求人|採用|応募|スカウト|おすすめ|新着|job|Indeed|勤務形態|福利厚生|公式オンラインストア|放課後学習サポート") {
        return $false
    }

    $hints = @($Item.task_hints | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
    if ($hints.Count -gt 0) { return $true }
    if ($text -match "締切|期限|提出|申請|登録|回答|返信|予約|面談|授業|休講|補講|シフト|勤務|deadline|submit|application|register|reply|shift") {
        return $true
    }
    return $false
}

$sourceFiles = @(Get-SourceFiles -Path $SourcePath)
if ($sourceFiles.Count -eq 0) {
    exit 0
}

$sourceFreshnessWarnings = @(
    foreach ($sourceFile in $sourceFiles) {
        if ($sourceFile.Name -match "mail-tasks-(\d{4}-\d{2}-\d{2})") {
            $sourceDate = $Matches[1]
            if ($sourceDate -ne $Date) {
                "Gmail export source is '$($sourceFile.Name)', not mail-tasks-$Date.json. Run the Apps Script export/trigger if today's mail should be imported."
            }
        }
    }
)
foreach ($warning in $sourceFreshnessWarnings) {
    Write-Warning $warning
}

$records = New-Object 'System.Collections.Generic.List[object]'
foreach ($file in $sourceFiles) {
    foreach ($record in @(Read-ExportFile -Path $file.FullName)) {
        if (Test-MailTaskRecord -Item $record -TargetDate $Date) {
            $records.Add($record)
        }
    }
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir) -and -not $DryRun) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}

if (-not $DryRun) {
    $jsonLines = @(
        $records |
            Sort-Object received_at, subject |
            ForEach-Object { ConvertTo-JsonLine -Value $_ }
    )
    if ($jsonLines.Count -eq 0) {
        Set-Content -LiteralPath $OutPath -Value "" -Encoding UTF8
    } else {
        $jsonLines | Set-Content -LiteralPath $OutPath -Encoding UTF8
    }
}

$taskDir = Split-Path -Parent $TaskReportPath
if (-not (Test-Path -LiteralPath $taskDir) -and -not $DryRun) {
    New-Item -ItemType Directory -Path $taskDir | Out-Null
}

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# メールタスク - $Date")
$lines.Add("")
$lines.Add('Source: Gmail labels `Codex/大学タスク` and `Codex/塾講師タスク`')
$lines.Add("")
$lines.Add("## Review")
$lines.Add("")
if ($records.Count -eq 0) {
    $lines.Add("- [ ] Gmail由来のタスク候補はありません。")
    foreach ($warning in $sourceFreshnessWarnings) {
        $lines.Add("  - warning: $warning")
    }
} else {
    foreach ($record in ($records | Sort-Object received_at, subject)) {
        foreach ($line in ((Get-MailTaskLine -Item $record) -split "`n")) {
            $lines.Add($line)
        }
        $snippet = Get-ShortLine -Text ([string]$record.snippet) -MaxChars 260
        if (-not [string]::IsNullOrWhiteSpace($snippet)) {
            $lines.Add("  - snippet: $snippet")
        }
        $lines.Add("")
    }
}

if (-not $DryRun) {
    ($lines -join "`n") | Set-Content -LiteralPath $TaskReportPath -Encoding UTF8
}

if ($SyncObsidian) {
    $obsidianDir = Join-Path $ObsidianVaultRoot $ObsidianTaskSubdir
    if (-not (Test-Path -LiteralPath $obsidianDir) -and -not $DryRun) {
        New-Item -ItemType Directory -Path $obsidianDir | Out-Null
    }
    $obsidianPath = Join-Path $obsidianDir "$Date.md"
    if (-not $DryRun) {
        Copy-Item -LiteralPath $TaskReportPath -Destination $obsidianPath -Force
    }
    Write-Host "Synced mail tasks to Obsidian: $obsidianPath"
}

Write-Host "Imported $($records.Count) mail task record(s)."
Write-Host "Inbox: $OutPath"
Write-Host "Task report: $TaskReportPath"





