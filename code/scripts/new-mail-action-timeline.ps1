param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [string]$InboxRoot,
    [string]$DeadlinePath,
    [string]$OutPath,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianTaskSubdir,
    [string]$WebhookEnvVar = "DISCORD_MAIL_TIMELINE_WEBHOOK_URL",
    [int]$UpcomingDays = 7,
    [switch]$SyncObsidian,
    [switch]$PostDiscord,
    [switch]$PostEmpty,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($InboxRoot)) {
    $InboxRoot = Join-Path $RepositoryRoot "records\inbox\gmail"
}
if ([string]::IsNullOrWhiteSpace($DeadlinePath)) {
    $DeadlinePath = Join-Path $RepositoryRoot "records\tasks\deadlines\mail-deadlines.md"
}
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\tasks\mail\timeline-$Date.md"
}
if ([string]::IsNullOrWhiteSpace($ObsidianTaskSubdir)) {
    $mailDirName = -join @([char]0x30E1, [char]0x30FC, [char]0x30EB)
    $ObsidianTaskSubdir = Join-Path "Tasks" $mailDirName
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

function Get-ShortLine {
    param(
        [string]$Text,
        [int]$MaxChars = 160
    )
    if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
    $value = ($Text -replace "\s+", " ").Trim()
    if ($value.Length -gt $MaxChars) { return $value.Substring(0, $MaxChars) + "..." }
    return $value
}

function Get-PropertyText {
    param(
        [object]$Item,
        [string]$Name
    )
    if ($null -eq $Item) { return "" }
    if ($Item.PSObject.Properties.Name -contains $Name) { return [string]$Item.$Name }
    return ""
}

function Get-KindLabel {
    param([object]$Item)
    $kind = Get-PropertyText -Item $Item -Name "kind"
    switch ($kind) {
        "tutoring" { return "tutoring" }
        "university" { return "university" }
        default { return "mail" }
    }
}

function Convert-ToDateTime {
    param([string]$Value)
    if ([string]::IsNullOrWhiteSpace($Value)) { return $null }
    try { return [DateTimeOffset]::Parse($Value, [Globalization.CultureInfo]::InvariantCulture) } catch { return $null }
}

function Get-ActionHint {
    param([object]$Item)
    $hints = @($Item.task_hints | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) } | Select-Object -First 2)
    if ($hints.Count -gt 0) { return (($hints | ForEach-Object { Get-ShortLine -Text ([string]$_) -MaxChars 100 }) -join " / ") }
    $snippet = Get-ShortLine -Text (Get-PropertyText -Item $Item -Name "snippet") -MaxChars 110
    if (-not [string]::IsNullOrWhiteSpace($snippet)) { return $snippet }
    return "Review the message."
}

function Read-Deadlines {
    param([datetime]$BaseDate)

    if (-not (Test-Path -LiteralPath $DeadlinePath)) { return @() }
    $items = New-Object 'System.Collections.Generic.List[object]'
    foreach ($line in Get-Content -LiteralPath $DeadlinePath -Encoding UTF8) {
        if ($line -notmatch "^\s*-\s+\[[ xX]\]\s+\[(?<kind>[^\]]+)\]\s+(?<subject>.+?)\s+.*?(?<due>20\d{2}-\d{2}-\d{2})") { continue }
        try {
            $due = [datetime]::ParseExact($Matches["due"], "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
        } catch {
            continue
        }
        $daysUntil = [int]($due.Date - $BaseDate.Date).TotalDays
        if ($daysUntil -lt 0 -or $daysUntil -gt $UpcomingDays) { continue }
        $items.Add([pscustomobject]@{
            Kind = $Matches["kind"]
            Subject = Get-ShortLine -Text $Matches["subject"] -MaxChars 150
            DueDate = $due.ToString("yyyy-MM-dd")
            DaysUntil = $daysUntil
        })
    }
    return @($items.ToArray() | Sort-Object DaysUntil, Kind, Subject)
}

$baseDate = [datetime]::ParseExact($Date, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
$todayPath = Join-Path $InboxRoot "$Date.jsonl"
$records = @(Read-JsonLines -Path $todayPath)
$deadlines = @(Read-Deadlines -BaseDate $baseDate)

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# Mail Action Timeline - $Date")
$lines.Add("")
$lines.Add("Generated: $(Get-Date -Format o)")
$lines.Add("")

$lines.Add("## Now")
$lines.Add("")
$todayDeadlines = @($deadlines | Where-Object { $_.DaysUntil -eq 0 })
if ($todayDeadlines.Count -eq 0) {
    $lines.Add("- [ ] No mail-derived task is detected as due today.")
} else {
    foreach ($item in $todayDeadlines) {
        $lines.Add("- [ ] [$($item.Kind)] $($item.Subject) due::$($item.DueDate)")
    }
}
$lines.Add("")

$lines.Add("## Next")
$lines.Add("")
$nextDeadlines = @($deadlines | Where-Object { $_.DaysUntil -gt 0 })
if ($nextDeadlines.Count -eq 0) {
    $lines.Add("- [ ] No mail-derived deadline is detected in the next $UpcomingDays days.")
} else {
    foreach ($item in $nextDeadlines) {
        $lines.Add("- [ ] [$($item.Kind)] $($item.Subject) due::$($item.DueDate) ($($item.DaysUntil) days)")
    }
}
$lines.Add("")

$lines.Add("## New Mail Candidates")
$lines.Add("")
if ($records.Count -eq 0) {
    $lines.Add("- [ ] No Gmail task candidates for today.")
} else {
    foreach ($record in ($records | Sort-Object received_at, subject)) {
        $received = Convert-ToDateTime -Value (Get-PropertyText -Item $record -Name "received_at")
        $time = if ($null -ne $received) { $received.ToOffset([TimeSpan]::FromHours(9)).ToString("HH:mm") } else { "--:--" }
        $kind = Get-KindLabel -Item $record
        $subject = Get-ShortLine -Text (Get-PropertyText -Item $record -Name "subject") -MaxChars 150
        $from = Get-ShortLine -Text (Get-PropertyText -Item $record -Name "from") -MaxChars 120
        $hint = Get-ActionHint -Item $record
        $lines.Add("- [ ] [$time][$kind] $subject")
        $lines.Add("  - action:: $hint")
        $lines.Add("  - from:: $from")
        $lines.Add("")
    }
}

if (-not $DryRun) {
    $outDir = Split-Path -Parent $OutPath
    if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
    ($lines -join "`n") | Set-Content -LiteralPath $OutPath -Encoding UTF8
}

if ($SyncObsidian) {
    $obsidianDir = Join-Path $ObsidianVaultRoot $ObsidianTaskSubdir
    if (-not (Test-Path -LiteralPath $obsidianDir) -and -not $DryRun) {
        New-Item -ItemType Directory -Path $obsidianDir | Out-Null
    }
    $obsidianPath = Join-Path $obsidianDir "timeline-$Date.md"
    if (-not $DryRun) {
        Copy-Item -LiteralPath $OutPath -Destination $obsidianPath -Force
    }
    Write-Host "Synced mail action timeline to Obsidian: $obsidianPath"
}

$discordLines = New-Object 'System.Collections.Generic.List[string]'
$discordLines.Add("[Mail TODO Timeline $Date]")
$discordLines.Add("due today: $($todayDeadlines.Count) / within $UpcomingDays days: $($nextDeadlines.Count) / new candidates: $($records.Count)")
$discordLines.Add("")

$top = New-Object 'System.Collections.Generic.List[string]'
foreach ($item in $todayDeadlines | Select-Object -First 5) {
    $top.Add("- today: [$($item.Kind)] $($item.Subject)")
}
foreach ($item in $nextDeadlines | Select-Object -First 5) {
    $top.Add("- in $($item.DaysUntil)d: [$($item.Kind)] $($item.Subject)")
}
foreach ($record in ($records | Sort-Object received_at, subject | Select-Object -First 5)) {
    $received = Convert-ToDateTime -Value (Get-PropertyText -Item $record -Name "received_at")
    $time = if ($null -ne $received) { $received.ToOffset([TimeSpan]::FromHours(9)).ToString("HH:mm") } else { "--:--" }
    $top.Add("- new ${time}: [$(Get-KindLabel -Item $record)] $(Get-ShortLine -Text (Get-PropertyText -Item $record -Name "subject") -MaxChars 90)")
}

if ($top.Count -eq 0) {
    $discordLines.Add("- No mail TODO is detected right now.")
} else {
    foreach ($line in $top | Select-Object -First 12) { $discordLines.Add($line) }
}

$discordMessage = ($discordLines -join "`n").Trim()

if ($PostDiscord) {
    if ($top.Count -eq 0 -and -not $PostEmpty) {
        Write-Host "No mail TODO timeline items. Skipping Discord post. Use -PostEmpty to post an empty timeline."
    } elseif ($DryRun) {
        Write-Host $discordMessage
    } else {
        & (Join-Path $ScriptRoot "post-discord-webhook.ps1") -WebhookEnvVar $WebhookEnvVar -Content $discordMessage
    }
}

Write-Host "Mail action timeline created: $OutPath"
Write-Host "Today deadlines: $($todayDeadlines.Count); upcoming deadlines: $($nextDeadlines.Count); new mail candidates: $($records.Count)."
