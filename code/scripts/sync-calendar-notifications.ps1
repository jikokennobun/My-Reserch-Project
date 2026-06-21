param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [string]$CalendarIcsUrl = $env:GOOGLE_CALENDAR_ICAL_URL,
    [string]$CalendarIcsPath,
    [string]$GuildId = $env:DISCORD_GUILD_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$OutPath,
    [string]$TaskReportPath,
    [string]$StatePath,
    [int]$LookAheadDays = 7,
    [switch]$IncludeDiscordEvents,
    [switch]$SyncObsidian,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianCalendarPath,
    [int[]]$ReminderDays = @(0, 1, 2, 3),
    [switch]$PostDiscordDigest,
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
    $OutPath = Join-Path $RepositoryRoot "records\inbox\calendar\$Date.jsonl"
}
if ([string]::IsNullOrWhiteSpace($TaskReportPath)) {
    $TaskReportPath = Join-Path $RepositoryRoot "records\tasks\calendar\$Date.md"
}
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\calendar-notification-state.csv"
}
if ([string]::IsNullOrWhiteSpace($CalendarIcsUrl)) {
    $CalendarIcsUrl = [Environment]::GetEnvironmentVariable("GOOGLE_CALENDAR_ICAL_URL", "User")
}
if ([string]::IsNullOrWhiteSpace($GuildId)) {
    $GuildId = [Environment]::GetEnvironmentVariable("DISCORD_GUILD_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}
if ([string]::IsNullOrWhiteSpace($ObsidianCalendarPath)) {
    $calendarDir = -join @([char]0x30AB, [char]0x30EC, [char]0x30F3, [char]0x30C0, [char]0x30FC)
    $ObsidianCalendarPath = "Tasks\$calendarDir\YYYY-MM-DD.md"
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 16 -Compress)
}

function Unfold-IcsLines {
    param([string[]]$Lines)

    $result = New-Object 'System.Collections.Generic.List[string]'
    foreach ($line in $Lines) {
        if (($line.StartsWith(" ") -or $line.StartsWith("`t")) -and $result.Count -gt 0) {
            $result[$result.Count - 1] = $result[$result.Count - 1] + $line.Substring(1)
        } else {
            $result.Add($line)
        }
    }
    return @($result.ToArray())
}

function Split-IcsProperty {
    param([string]$Line)

    $idx = $Line.IndexOf(":")
    if ($idx -lt 0) { return $null }
    $left = $Line.Substring(0, $idx)
    $value = $Line.Substring($idx + 1)
    $parts = $left -split ";"
    $name = $parts[0].ToUpperInvariant()
    $params = @{}
    foreach ($part in ($parts | Select-Object -Skip 1)) {
        $pidx = $part.IndexOf("=")
        if ($pidx -gt 0) {
            $params[$part.Substring(0, $pidx).ToUpperInvariant()] = $part.Substring($pidx + 1).Trim('"')
        }
    }
    return [pscustomobject]@{ Name = $name; Params = $params; Value = $value }
}

function Convert-IcsText {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
    return ($Text -replace "\\n", "`n" -replace "\\,", "," -replace "\\;", ";" -replace "\\\\", "\").Trim()
}

function Convert-IcsDate {
    param(
        [string]$Value,
        [hashtable]$Params
    )

    if ([string]::IsNullOrWhiteSpace($Value)) { return $null }
    try {
        if ($Params.ContainsKey("VALUE") -and $Params["VALUE"] -eq "DATE") {
            $date = [datetime]::ParseExact($Value, "yyyyMMdd", [Globalization.CultureInfo]::InvariantCulture)
            return [pscustomobject]@{ Value = [DateTimeOffset]::new($date.Year, $date.Month, $date.Day, 0, 0, 0, [TimeSpan]::FromHours(9)); AllDay = $true }
        }
        if ($Value.EndsWith("Z")) {
            $utcFormats = [string[]]@("yyyyMMdd'T'HHmmss'Z'", "yyyyMMdd'T'HHmm'Z'")
            $utc = [datetime]::ParseExact($Value, $utcFormats, [Globalization.CultureInfo]::InvariantCulture, [Globalization.DateTimeStyles]::AssumeUniversal)
            return [pscustomobject]@{ Value = [DateTimeOffset]$utc.ToUniversalTime(); AllDay = $false }
        }
        $localFormats = [string[]]@("yyyyMMdd'T'HHmmss", "yyyyMMdd'T'HHmm")
        $local = [datetime]::ParseExact($Value, $localFormats, [Globalization.CultureInfo]::InvariantCulture, [Globalization.DateTimeStyles]::None)
        return [pscustomobject]@{ Value = [DateTimeOffset]::new($local, [TimeSpan]::FromHours(9)); AllDay = $false }
    } catch {
        return $null
    }
}

function Convert-IcsEvents {
    param([string]$IcsText)

    if ([string]::IsNullOrWhiteSpace($IcsText)) { return @() }
    $lines = Unfold-IcsLines -Lines ($IcsText -split "\r?\n")
    $events = New-Object 'System.Collections.Generic.List[object]'
    $props = @{}
    $inEvent = $false

    foreach ($line in $lines) {
        if ($line.Trim() -eq "BEGIN:VEVENT") {
            $props = @{}
            $inEvent = $true
            continue
        }
        if ($line.Trim() -eq "END:VEVENT") {
            if ($inEvent) {
                $start = $null
                $end = $null
                if ($props.ContainsKey("DTSTART")) { $start = Convert-IcsDate -Value $props["DTSTART"].Value -Params $props["DTSTART"].Params }
                if ($props.ContainsKey("DTEND")) { $end = Convert-IcsDate -Value $props["DTEND"].Value -Params $props["DTEND"].Params }
                if ($null -ne $start) {
                    $uid = if ($props.ContainsKey("UID")) { $props["UID"].Value } else { [guid]::NewGuid().ToString("N") }
                    $summary = if ($props.ContainsKey("SUMMARY")) { Convert-IcsText -Text $props["SUMMARY"].Value } else { "(untitled)" }
                    $location = if ($props.ContainsKey("LOCATION")) { Convert-IcsText -Text $props["LOCATION"].Value } else { "" }
                    $description = if ($props.ContainsKey("DESCRIPTION")) { Convert-IcsText -Text $props["DESCRIPTION"].Value } else { "" }
                    $url = if ($props.ContainsKey("URL")) { $props["URL"].Value } else { "" }
                    $events.Add([pscustomobject][ordered]@{
                        source = "google_calendar"
                        uid = $uid
                        title = $summary
                        start = $start.Value.ToString("o")
                        end = if ($null -ne $end) { $end.Value.ToString("o") } else { "" }
                        all_day = [bool]$start.AllDay
                        location = $location
                        description = $description
                        url = $url
                    })
                }
            }
            $inEvent = $false
            continue
        }
        if ($inEvent) {
            $prop = Split-IcsProperty -Line $line
            if ($null -ne $prop) { $props[$prop.Name] = $prop }
        }
    }
    return @($events.ToArray())
}

function Invoke-DiscordGetJson {
    param([string]$Path)

    $raw = & curl.exe -sS -H "Authorization: Bot $BotToken" "https://discord.com/api/v10$Path"
    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $Path." }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Get-DiscordScheduledEvents {
    if ([string]::IsNullOrWhiteSpace($GuildId) -or [string]::IsNullOrWhiteSpace($BotToken)) { return @() }
    $items = @(Invoke-DiscordGetJson -Path "/guilds/$GuildId/scheduled-events?with_user_count=false")
    return @($items | ForEach-Object {
        [pscustomobject][ordered]@{
            source = "discord_event"
            uid = [string]$_.id
            title = [string]$_.name
            start = [string]$_.scheduled_start_time
            end = [string]$_.scheduled_end_time
            all_day = $false
            location = if ($_.entity_metadata -and $_.entity_metadata.location) { [string]$_.entity_metadata.location } else { "" }
            description = [string]$_.description
            url = ""
        }
    })
}

function Get-EventStart {
    param([object]$Event)
    try {
        return [DateTimeOffset]::Parse([string]$Event.start, [Globalization.CultureInfo]::InvariantCulture)
    } catch {
        return $null
    }
}

function Format-EventLine {
    param([object]$Event)

    $start = Get-EventStart -Event $Event
    $time = if ($null -eq $start) { "time unknown" } elseif ($Event.all_day) { $start.ToOffset([TimeSpan]::FromHours(9)).ToString("yyyy-MM-dd") + " all-day" } else { $start.ToOffset([TimeSpan]::FromHours(9)).ToString("yyyy-MM-dd HH:mm") }
    $source = [string]$Event.source
    $line = "- [ ] $time [$source] $($Event.title)"
    if (-not [string]::IsNullOrWhiteSpace([string]$Event.location)) { $line += " @ $($Event.location)" }
    return $line
}

function Get-EventReminderKey {
    param(
        [object]$Event,
        [int]$DaysUntil
    )

    $uid = [string]$Event.uid
    if ([string]::IsNullOrWhiteSpace($uid)) {
        $uid = ([string]$Event.title) + "|" + ([string]$Event.start)
    }
    return "$($Event.source)|$uid|$($Event.start)|$DaysUntil"
}

function Get-DaysUntilEvent {
    param(
        [object]$Event,
        [datetime]$BaseDate
    )

    $start = Get-EventStart -Event $Event
    if ($null -eq $start) { return $null }
    $jstStart = $start.ToOffset([TimeSpan]::FromHours(9)).Date
    return [int]($jstStart - $BaseDate.Date).TotalDays
}

function Get-ReminderTimingText {
    param([int]$DaysUntil)

    switch ($DaysUntil) {
        0 { return "today" }
        1 { return "tomorrow" }
        default { return "$DaysUntil days left" }
    }
}

function Read-ReminderState {
    param([string]$Path)

    $keys = New-Object 'System.Collections.Generic.HashSet[string]'
    if (Test-Path -LiteralPath $Path) {
        foreach ($row in @(Import-Csv -LiteralPath $Path)) {
            if (-not [string]::IsNullOrWhiteSpace($row.ReminderKey)) {
                [void]$keys.Add($row.ReminderKey)
            }
        }
    }
    return ,$keys
}

function Save-ReminderStateRows {
    param(
        [string]$Path,
        [object[]]$Rows
    )

    if ($DryRun -or $Rows.Count -eq 0) { return }
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    if (Test-Path -LiteralPath $Path) {
        $Rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Append -Encoding UTF8
    } else {
        $Rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding UTF8
    }
}

function Normalize-CalendarIcsUrl {
    param([string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) { return "" }

    $trimmed = $Url.Trim()
    $quoteChars = @([char]34, [char]39, [char]60)
    $endQuoteChars = @([char]34, [char]39, [char]62)
    while ($trimmed.Length -gt 0 -and $quoteChars.Contains($trimmed[0])) {
        $trimmed = $trimmed.Substring(1).TrimStart()
    }
    while ($trimmed.Length -gt 0 -and $endQuoteChars.Contains($trimmed[$trimmed.Length - 1])) {
        $trimmed = $trimmed.Substring(0, $trimmed.Length - 1).TrimEnd()
    }

    if ($trimmed -match '(?i)(webcal|https?)://\S+') {
        $trimmed = $Matches[0]
        while ($trimmed.Length -gt 0 -and $endQuoteChars.Contains($trimmed[$trimmed.Length - 1])) {
            $trimmed = $trimmed.Substring(0, $trimmed.Length - 1).TrimEnd()
        }
    }
    if ($trimmed.StartsWith("calendar.google.com/", [StringComparison]::OrdinalIgnoreCase)) {
        $trimmed = "https://" + $trimmed
    }
    $trimmed = $trimmed -replace '^(https?):/([^/])', '$1://$2'

    if ($trimmed.StartsWith("webcal://", [StringComparison]::OrdinalIgnoreCase)) {
        $trimmed = "https://" + $trimmed.Substring(9)
    }

    return $trimmed
}

$baseDate = [datetime]::ParseExact($Date, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
$windowStart = [DateTimeOffset]::new($baseDate.Year, $baseDate.Month, $baseDate.Day, 0, 0, 0, [TimeSpan]::FromHours(9))
$windowEnd = $windowStart.AddDays($LookAheadDays)

$events = New-Object 'System.Collections.Generic.List[object]'
if (-not [string]::IsNullOrWhiteSpace($CalendarIcsPath) -and (Test-Path -LiteralPath $CalendarIcsPath)) {
    $icsText = Get-Content -LiteralPath $CalendarIcsPath -Raw -Encoding UTF8
    foreach ($event in @(Convert-IcsEvents -IcsText $icsText)) { $events.Add($event) }
} elseif (-not [string]::IsNullOrWhiteSpace($CalendarIcsUrl)) {
    $CalendarIcsUrl = Normalize-CalendarIcsUrl -Url $CalendarIcsUrl
    $calendarUri = $null
    $isValidCalendarUri = [Uri]::TryCreate($CalendarIcsUrl, [UriKind]::Absolute, [ref]$calendarUri)
    if (-not $isValidCalendarUri -or ($calendarUri.Scheme -ne "http" -and $calendarUri.Scheme -ne "https")) {
        throw "GOOGLE_CALENDAR_ICAL_URL is not a valid Google Calendar iCal URL. Re-copy 'Secret address in iCal format' from Google Calendar settings and save it again."
    }
    $icsText = (Invoke-WebRequest -Uri $calendarUri.AbsoluteUri -UseBasicParsing).Content
    foreach ($event in @(Convert-IcsEvents -IcsText $icsText)) { $events.Add($event) }
} else {
    Write-Host "GOOGLE_CALENDAR_ICAL_URL is not configured. Skipping Google Calendar import."
}

if ($IncludeDiscordEvents) {
    foreach ($event in @(Get-DiscordScheduledEvents)) { $events.Add($event) }
}

$filtered = @($events | Where-Object {
    $start = Get-EventStart -Event $_
    $null -ne $start -and $start -ge $windowStart -and $start -lt $windowEnd
} | Sort-Object { Get-EventStart -Event $_ })

if (-not $DryRun) {
    $outDir = Split-Path -Parent $OutPath
    if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
    $filtered | ForEach-Object { ConvertTo-JsonLine -Value $_ } | Set-Content -LiteralPath $OutPath -Encoding UTF8

    $taskDir = Split-Path -Parent $TaskReportPath
    if (-not (Test-Path -LiteralPath $taskDir)) { New-Item -ItemType Directory -Path $taskDir | Out-Null }
}

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# Calendar Tasks - $Date")
$lines.Add("")
$lines.Add("Window: $Date + $LookAheadDays day(s)")
$lines.Add("")
if ($filtered.Count -eq 0) {
    $lines.Add("- [ ] No calendar events found.")
} else {
    foreach ($event in $filtered) { $lines.Add((Format-EventLine -Event $event)) }
}
if (-not $DryRun) {
    Set-Content -LiteralPath $TaskReportPath -Encoding UTF8 -Value $lines
}

if ($SyncObsidian -and -not $DryRun) {
    $relative = $ObsidianCalendarPath.Replace("YYYY-MM-DD", $Date)
    $obsidianPath = Join-Path $ObsidianVaultRoot $relative
    $obsidianDir = Split-Path -Parent $obsidianPath
    if (-not (Test-Path -LiteralPath $obsidianDir)) { New-Item -ItemType Directory -Path $obsidianDir | Out-Null }
    Copy-Item -LiteralPath $TaskReportPath -Destination $obsidianPath -Force
    Write-Host "Synced calendar tasks to Obsidian: $obsidianPath"
}

if ($PostDiscordDigest -and $filtered.Count -gt 0) {
    $webhook = $env:DISCORD_CALENDAR_WEBHOOK_URL
    if ([string]::IsNullOrWhiteSpace($webhook)) {
        $webhook = [Environment]::GetEnvironmentVariable("DISCORD_CALENDAR_WEBHOOK_URL", "User")
    }
    if ([string]::IsNullOrWhiteSpace($webhook)) {
        Write-Host "DISCORD_CALENDAR_WEBHOOK_URL is not configured. Skipping Discord calendar digest."
    } else {
        $posted = Read-ReminderState -Path $StatePath
        $newRows = New-Object 'System.Collections.Generic.List[object]'
        $reminderEvents = New-Object 'System.Collections.Generic.List[object]'
        foreach ($event in $filtered) {
            $daysUntil = Get-DaysUntilEvent -Event $event -BaseDate $baseDate
            if ($null -eq $daysUntil) { continue }
            if ($ReminderDays -notcontains [int]$daysUntil) { continue }
            $reminderKey = Get-EventReminderKey -Event $event -DaysUntil $daysUntil
            if ($posted.Contains($reminderKey)) { continue }
            $event | Add-Member -NotePropertyName days_until -NotePropertyValue $daysUntil -Force
            $event | Add-Member -NotePropertyName reminder_key -NotePropertyValue $reminderKey -Force
            $reminderEvents.Add($event)
        }

        if ($reminderEvents.Count -eq 0) {
            Write-Host "Posted 0 new calendar reminder(s)."
        } else {
        $digestLines = New-Object 'System.Collections.Generic.List[string]'
            $digestLines.Add("[Calendar Reminders] $Date")
            foreach ($event in ($reminderEvents | Select-Object -First 10)) {
                $timing = Get-ReminderTimingText -DaysUntil ([int]$event.days_until)
                $digestLines.Add(((Format-EventLine -Event $event).TrimStart("-", " ", "[", "]")) + " ($timing)")
                $newRows.Add([pscustomobject]@{
                    ReminderKey = [string]$event.reminder_key
                    Source = [string]$event.source
                    Uid = [string]$event.uid
                    Title = [string]$event.title
                    Start = [string]$event.start
                    DaysUntil = [int]$event.days_until
                    AnnouncedAt = (Get-Date).ToString("o")
                })
        }
        $content = ($digestLines -join "`n")
        if ($content.Length -gt 1800) { $content = $content.Substring(0, 1790) + "...(truncated)" }
        if ($DryRun) {
            Write-Host "Would post calendar digest:"
            Write-Host $content
        } else {
            & (Join-Path $ScriptRoot "post-discord-webhook.ps1") -WebhookEnvVar "DISCORD_CALENDAR_WEBHOOK_URL" -Content $content
                Save-ReminderStateRows -Path $StatePath -Rows @($newRows.ToArray())
            }
            Write-Host "Posted $($reminderEvents.Count) new calendar reminder(s)."
        }
    }
}

Write-Host "Calendar event(s): $($filtered.Count)"
Write-Host "Calendar report: $TaskReportPath"
