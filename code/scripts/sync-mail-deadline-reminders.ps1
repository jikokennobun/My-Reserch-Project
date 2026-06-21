param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [string]$InboxRoot,
    [string]$OutPath,
    [string]$StatePath,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianDeadlinePath = "Tasks\メール締切リマインダー.md",
    [int[]]$ReminderDays = @(0, 1, 3),
    [int]$LookbackDays = 45,
    [int]$FutureDays = 240,
    [switch]$SyncObsidian,
    [switch]$PostDiscordReminders,
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
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\tasks\deadlines\mail-deadlines.md"
}
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\mail-deadline-reminder-state.csv"
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
        [int]$MaxChars = 220
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
        "tutoring" { return (-join @([char]0x587E, [char]0x8B1B, [char]0x5E2B, [char]0x30D0, [char]0x30A4, [char]0x30C8)) }
        "university" { return (-join @([char]0x5927, [char]0x5B66)) }
        default { return (-join @([char]0x30E1, [char]0x30FC, [char]0x30EB)) }
    }
}

function Get-WebhookEnvVar {
    param([object]$Item)
    $kind = Get-PropertyText -Item $Item -Name "kind"
    switch ($kind) {
        "tutoring" { return "DISCORD_TUTORING_MAIL_WEBHOOK_URL" }
        default { return "DISCORD_UNIVERSITY_MAIL_WEBHOOK_URL" }
    }
}

function Get-MessageId {
    param([object]$Item)
    $messageId = Get-PropertyText -Item $Item -Name "message_id"
    if (-not [string]::IsNullOrWhiteSpace($messageId)) { return $messageId }
    return ((Get-PropertyText -Item $Item -Name "subject"), (Get-PropertyText -Item $Item -Name "received_at"), (Get-PropertyText -Item $Item -Name "from")) -join "|"
}

function New-DateValue {
    param(
        [int]$Year,
        [int]$Month,
        [int]$Day,
        [datetime]$BaseDate
    )
    try {
        if ($Year -eq 0) { $Year = $BaseDate.Year }
        if ($Year -lt 100) { $Year = 2000 + $Year }
        $value = [datetime]::new($Year, $Month, $Day)
        if ($value.Date -lt $BaseDate.Date.AddDays(-7)) {
            $value = $value.AddYears(1)
        }
        return $value.Date
    } catch {
        return $null
    }
}

function Get-DateCandidates {
    param(
        [string]$Text,
        [datetime]$BaseDate
    )

    $values = New-Object 'System.Collections.Generic.List[datetime]'
    if ([string]::IsNullOrWhiteSpace($Text)) { return @() }

    foreach ($match in [regex]::Matches($Text, "(?<y>20\d{2})[\/\-\.](?<m>\d{1,2})[\/\-\.](?<d>\d{1,2})")) {
        $value = New-DateValue -Year ([int]$match.Groups["y"].Value) -Month ([int]$match.Groups["m"].Value) -Day ([int]$match.Groups["d"].Value) -BaseDate $BaseDate
        if ($null -ne $value) { $values.Add($value) }
    }

    foreach ($match in [regex]::Matches($Text, "(?<y>20\d{2})年\s*(?<m>\d{1,2})月\s*(?<d>\d{1,2})日?")) {
        $value = New-DateValue -Year ([int]$match.Groups["y"].Value) -Month ([int]$match.Groups["m"].Value) -Day ([int]$match.Groups["d"].Value) -BaseDate $BaseDate
        if ($null -ne $value) { $values.Add($value) }
    }

    foreach ($match in [regex]::Matches($Text, "(?<m>\d{1,2})月\s*(?<d>\d{1,2})日")) {
        $value = New-DateValue -Year 0 -Month ([int]$match.Groups["m"].Value) -Day ([int]$match.Groups["d"].Value) -BaseDate $BaseDate
        if ($null -ne $value) { $values.Add($value) }
    }

    if ($Text -match "(締切|期限|提出|回答|申請|登録|due|deadline)") {
        foreach ($match in [regex]::Matches($Text, "(?<!\d)(?<m>\d{1,2})\/(?<d>\d{1,2})(?!\d)")) {
            $value = New-DateValue -Year 0 -Month ([int]$match.Groups["m"].Value) -Day ([int]$match.Groups["d"].Value) -BaseDate $BaseDate
            if ($null -ne $value) { $values.Add($value) }
        }
    }

    if ($Text -match "本日|今日") { $values.Add($BaseDate.Date) }
    if ($Text -match "明日") { $values.Add($BaseDate.Date.AddDays(1)) }

    return @($values | Sort-Object -Unique)
}

function New-DeadlineItem {
    param(
        [object]$Record,
        [datetime]$DueDate,
        [datetime]$BaseDate
    )

    $messageId = Get-MessageId -Item $Record
    $kindLabel = Get-KindLabel -Item $Record
    $subject = Get-ShortLine -Text (Get-PropertyText -Item $Record -Name "subject") -MaxChars 180
    $from = Get-ShortLine -Text (Get-PropertyText -Item $Record -Name "from") -MaxChars 140
    $hints = @($Record.task_hints | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) } | Select-Object -First 5)
    $snippet = Get-ShortLine -Text (Get-PropertyText -Item $Record -Name "snippet") -MaxChars 240

    return [pscustomobject]@{
        Key = "$messageId|$($DueDate.ToString('yyyy-MM-dd'))"
        MessageId = $messageId
        Kind = Get-PropertyText -Item $Record -Name "kind"
        KindLabel = $kindLabel
        Subject = $subject
        From = $from
        ReceivedAt = Get-PropertyText -Item $Record -Name "received_at"
        DueDate = $DueDate.ToString("yyyy-MM-dd")
        DaysUntil = [int]($DueDate.Date - $BaseDate.Date).TotalDays
        Hints = @($hints)
        Snippet = $snippet
        WebhookEnvVar = Get-WebhookEnvVar -Item $Record
    }
}

function Add-DeadlineLine {
    param(
        [System.Collections.Generic.List[string]]$Lines,
        [object]$Item
    )

    $line = "- [ ] [$($Item.KindLabel)] $($Item.Subject) 📅 $($Item.DueDate)"
    $Lines.Add($line)
    $Lines.Add("  - due:: $($Item.DueDate)")
    $Lines.Add("  - from:: $($Item.From)")
    $Lines.Add("  - received:: $($Item.ReceivedAt)")
    if ($Item.Hints.Count -gt 0) {
        $Lines.Add("  - hints:: " + ($Item.Hints -join " / "))
    }
    if (-not [string]::IsNullOrWhiteSpace($Item.Snippet)) {
        $Lines.Add("  - snippet:: $($Item.Snippet)")
    }
}

function New-ReminderMessage {
    param([object]$Item)

    $timing = switch ($Item.DaysUntil) {
        0 { "today" }
        1 { "tomorrow" }
        default { "$($Item.DaysUntil) days left" }
    }
    $hints = if ($Item.Hints.Count -gt 0) { "`n- " + ($Item.Hints -join "`n- ") } else { "`n- Please review the message." }
    $message = @(
        "[$($Item.KindLabel) Deadline Reminder]"
        "$($Item.Subject)"
        ""
        "due: $($Item.DueDate) ($timing)"
        "from: $($Item.From)"
        "Candidates:$hints"
    ) -join "`n"
    if ($message.Length -gt 1800) { return $message.Substring(0, 1790) + "...(truncated)" }
    return $message
}

$baseDate = [datetime]::ParseExact($Date, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
$records = New-Object 'System.Collections.Generic.List[object]'
if (Test-Path -LiteralPath $InboxRoot) {
    foreach ($file in @(Get-ChildItem -LiteralPath $InboxRoot -Filter "*.jsonl" -File | Sort-Object Name)) {
        foreach ($record in @(Read-JsonLines -Path $file.FullName)) {
            $records.Add($record)
        }
    }
}

$deadlineByKey = @{}
foreach ($record in $records) {
    $textParts = @(
        (Get-PropertyText -Item $record -Name "subject"),
        (@($record.task_hints) -join "`n"),
        (Get-PropertyText -Item $record -Name "snippet"),
        (Get-PropertyText -Item $record -Name "body_excerpt")
    )
    $text = $textParts -join "`n"
    foreach ($due in @(Get-DateCandidates -Text $text -BaseDate $baseDate)) {
        if ($due.Date -lt $baseDate.Date.AddDays(-$LookbackDays)) { continue }
        if ($due.Date -gt $baseDate.Date.AddDays($FutureDays)) { continue }
        $item = New-DeadlineItem -Record $record -DueDate $due -BaseDate $baseDate
        $deadlineByKey[$item.Key] = $item
    }
}

$deadlines = @($deadlineByKey.Values | Sort-Object DueDate, KindLabel, Subject)

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# メール締切リマインダー")
$lines.Add("")
$lines.Add("Generated: $(Get-Date -Format o)")
$lines.Add("Base date: $Date")
$lines.Add("")
$groups = @(
    @{ Heading = "Today"; Items = @($deadlines | Where-Object { $_.DaysUntil -eq 0 }) },
    @{ Heading = "Next 3 Days"; Items = @($deadlines | Where-Object { $_.DaysUntil -gt 0 -and $_.DaysUntil -le 3 }) },
    @{ Heading = "Upcoming"; Items = @($deadlines | Where-Object { $_.DaysUntil -gt 3 }) },
    @{ Heading = "Past"; Items = @($deadlines | Where-Object { $_.DaysUntil -lt 0 }) }
)
foreach ($group in $groups) {
    $lines.Add("## $($group.Heading)")
    $lines.Add("")
    if ($group.Items.Count -eq 0) {
        $lines.Add("- None.")
    } else {
        foreach ($item in $group.Items) { Add-DeadlineLine -Lines $lines -Item $item }
    }
    $lines.Add("")
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir) -and -not $DryRun) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}
if (-not $DryRun) {
    ($lines -join "`n") | Set-Content -LiteralPath $OutPath -Encoding UTF8
}

if ($SyncObsidian) {
    $obsidianPath = Join-Path $ObsidianVaultRoot $ObsidianDeadlinePath
    $obsidianDir = Split-Path -Parent $obsidianPath
    if (-not (Test-Path -LiteralPath $obsidianDir) -and -not $DryRun) {
        New-Item -ItemType Directory -Path $obsidianDir | Out-Null
    }
    if (-not $DryRun) {
        Copy-Item -LiteralPath $OutPath -Destination $obsidianPath -Force
    }
    Write-Host "Synced mail deadline reminders to Obsidian: $obsidianPath"
}

if ($PostDiscordReminders) {
    $announced = New-Object 'System.Collections.Generic.HashSet[string]'
    if (Test-Path -LiteralPath $StatePath) {
        foreach ($row in @(Import-Csv -LiteralPath $StatePath)) {
            if (-not [string]::IsNullOrWhiteSpace($row.ReminderKey)) {
                [void]$announced.Add($row.ReminderKey)
            }
        }
    }

    $newRows = New-Object 'System.Collections.Generic.List[object]'
    $postCount = 0
    foreach ($item in $deadlines) {
        if ($ReminderDays -notcontains [int]$item.DaysUntil) { continue }
        $reminderKey = "$($item.Key)|$($item.DaysUntil)"
        if ($announced.Contains($reminderKey)) { continue }
        $message = New-ReminderMessage -Item $item
        if ($DryRun) {
            Write-Host "Would post reminder to $($item.WebhookEnvVar):"
            Write-Host $message
        } else {
            & (Join-Path $ScriptRoot "post-discord-webhook.ps1") -WebhookEnvVar $item.WebhookEnvVar -Content $message
        }
        $postCount += 1
        [void]$announced.Add($reminderKey)
        $newRows.Add([pscustomobject]@{
            ReminderKey = $reminderKey
            MessageId = $item.MessageId
            Kind = $item.KindLabel
            DueDate = $item.DueDate
            DaysUntil = $item.DaysUntil
            WebhookEnvVar = $item.WebhookEnvVar
            AnnouncedAt = (Get-Date).ToString("o")
        })
    }

    if (-not $DryRun -and $newRows.Count -gt 0) {
        $stateDir = Split-Path -Parent $StatePath
        if (-not (Test-Path -LiteralPath $stateDir)) {
            New-Item -ItemType Directory -Path $stateDir | Out-Null
        }
        if (Test-Path -LiteralPath $StatePath) {
            $newRows | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Append -Encoding UTF8
        } else {
            $newRows | Export-Csv -LiteralPath $StatePath -NoTypeInformation -Encoding UTF8
        }
    }
    Write-Host "Posted $postCount deadline reminder(s)."
}

Write-Host "Mail deadline(s): $($deadlines.Count)"
Write-Host "Deadline report: $OutPath"
