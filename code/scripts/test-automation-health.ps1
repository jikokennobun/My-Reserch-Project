param(
    [string]$Date,
    [string]$RepositoryRoot,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianDailySubdir,
    [switch]$WriteReport,
    [switch]$FailOnCritical
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($Date)) {
    $Date = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9)).ToString("yyyy-MM-dd")
}
if ([string]::IsNullOrWhiteSpace($ObsidianDailySubdir)) {
    $ObsidianDailySubdir = -join @([char]0x65E5, [char]0x5831)
}

Set-Location -LiteralPath $RepositoryRoot

$Results = New-Object 'System.Collections.Generic.List[object]'

function Add-HealthResult {
    param(
        [ValidateSet("OK", "WARN", "FAIL")]
        [string]$Level,
        [string]$Category,
        [string]$Name,
        [string]$Detail
    )

    $Results.Add([pscustomobject][ordered]@{
        level = $Level
        category = $Category
        name = $Name
        detail = $Detail
    }) | Out-Null
}

function Get-EnvPresence {
    param([string]$Name)

    $processValue = [Environment]::GetEnvironmentVariable($Name, "Process")
    if (-not [string]::IsNullOrWhiteSpace($processValue)) {
        return "set(process)"
    }

    $userValue = [Environment]::GetEnvironmentVariable($Name, "User")
    if (-not [string]::IsNullOrWhiteSpace($userValue)) {
        return "set(user)"
    }

    return "missing"
}

function Test-PathHealth {
    param(
        [string]$Category,
        [string]$Name,
        [string]$Path,
        [ValidateSet("WARN", "FAIL")]
        [string]$MissingLevel = "FAIL"
    )

    if (Test-Path -LiteralPath $Path) {
        Add-HealthResult -Level "OK" -Category $Category -Name $Name -Detail "Found."
    } else {
        Add-HealthResult -Level $MissingLevel -Category $Category -Name $Name -Detail "Missing: $Path"
    }
}

function Test-JsonFile {
    param(
        [string]$Path,
        [string]$Category,
        [string]$Name
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        Add-HealthResult -Level "WARN" -Category $Category -Name $Name -Detail "File not found: $Path"
        return
    }

    try {
        $null = Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
        Add-HealthResult -Level "OK" -Category $Category -Name $Name -Detail "Valid JSON."
    } catch {
        Add-HealthResult -Level "FAIL" -Category $Category -Name $Name -Detail "Invalid JSON: $($_.Exception.Message)"
    }
}

function Test-JsonLinesFile {
    param([System.IO.FileInfo]$File)

    $lineNumber = 0
    $badLines = New-Object 'System.Collections.Generic.List[string]'
    foreach ($line in (Get-Content -LiteralPath $File.FullName -Encoding UTF8 -ErrorAction Stop)) {
        $lineNumber++
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try {
            $null = $line | ConvertFrom-Json
        } catch {
            $badLines.Add("${lineNumber}: $($_.Exception.Message)") | Out-Null
        }
    }

    if ($badLines.Count -eq 0) {
        Add-HealthResult -Level "OK" -Category "inbox" -Name $File.Name -Detail "Valid JSONL."
    } else {
        $sample = ($badLines | Select-Object -First 3) -join " / "
        Add-HealthResult -Level "FAIL" -Category "inbox" -Name $File.Name -Detail "Invalid JSONL line(s): $sample"
    }
}

function Escape-MarkdownCell {
    param([string]$Value)

    if ($null -eq $Value) { return "" }
    return (($Value -replace "\r?\n", " ") -replace "\|", "\|")
}

Test-PathHealth -Category "paths" -Name "repository root" -Path $RepositoryRoot
Test-PathHealth -Category "paths" -Name "scripts directory" -Path (Join-Path $RepositoryRoot "code\scripts")
Test-PathHealth -Category "paths" -Name "records directory" -Path (Join-Path $RepositoryRoot "records")
Test-PathHealth -Category "paths" -Name "daily records directory" -Path (Join-Path $RepositoryRoot "records\daily")
Test-PathHealth -Category "paths" -Name "Obsidian vault" -Path $ObsidianVaultRoot -MissingLevel "WARN"
Test-PathHealth -Category "paths" -Name "Obsidian daily template" -Path (Join-Path (Join-Path $ObsidianVaultRoot $ObsidianDailySubdir) "nippo-template.md") -MissingLevel "WARN"

$todoPath = Join-Path $RepositoryRoot "records\tasks\todo.md"
Test-PathHealth -Category "paths" -Name "todo.md" -Path $todoPath -MissingLevel "WARN"

$scriptDir = Join-Path $RepositoryRoot "code\scripts"
if (Test-Path -LiteralPath $scriptDir) {
    $syntaxFailures = New-Object 'System.Collections.Generic.List[string]'
    foreach ($file in @(Get-ChildItem -LiteralPath $scriptDir -Filter "*.ps1" -File -ErrorAction SilentlyContinue)) {
        try {
            $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
            $null = [scriptblock]::Create($text)
        } catch {
            $syntaxFailures.Add("$($file.Name): $($_.Exception.Message)") | Out-Null
        }
    }

    if ($syntaxFailures.Count -eq 0) {
        Add-HealthResult -Level "OK" -Category "scripts" -Name "PowerShell syntax" -Detail "All code/scripts/*.ps1 files parse."
    } else {
        $sample = ($syntaxFailures | Select-Object -First 8) -join " / "
        Add-HealthResult -Level "FAIL" -Category "scripts" -Name "PowerShell syntax" -Detail $sample
    }
}

$requiredEnv = @(
    "DISCORD_BOT_TOKEN",
    "DISCORD_GUILD_ID",
    "DISCORD_SELF_USER_ID"
)
foreach ($name in $requiredEnv) {
    $presence = Get-EnvPresence -Name $name
    if ($presence -eq "missing") {
        Add-HealthResult -Level "WARN" -Category "environment" -Name $name -Detail "Missing. Some Discord capture features will be skipped."
    } else {
        Add-HealthResult -Level "OK" -Category "environment" -Name $name -Detail $presence
    }
}

$dailyChannelSignals = @(
    "DISCORD_DAILY_CHANNEL_ID",
    "DISCORD_DAILY_WEBHOOK_URL",
    "DISCORD_MONTHLY_DAILY_WEBHOOK_URL"
)
$dailyConfigured = $false
foreach ($name in $dailyChannelSignals) {
    if ((Get-EnvPresence -Name $name) -ne "missing") {
        $dailyConfigured = $true
    }
}
if ($dailyConfigured) {
    Add-HealthResult -Level "OK" -Category "environment" -Name "daily Discord output" -Detail "At least one daily channel/webhook setting is present."
} else {
    Add-HealthResult -Level "WARN" -Category "environment" -Name "daily Discord output" -Detail "No daily channel/webhook setting is present."
}

$optionalEnv = @(
    "DISCORD_ACTIVITY_CHANNEL_ID",
    "DISCORD_FOOD_CHANNEL_ID",
    "DISCORD_WATCH_CHANNEL_ID",
    "DISCORD_WATCHLIST_CHANNEL_ID",
    "DISCORD_COMMAND_CHANNEL_ID",
    "DISCORD_AI_CHAT_CHANNEL_ID",
    "DISCORD_CALENDAR_WEBHOOK_URL",
    "DISCORD_UNIVERSITY_MAIL_WEBHOOK_URL",
    "DISCORD_TUTORING_MAIL_WEBHOOK_URL",
    "DISCORD_MAIL_TIMELINE_WEBHOOK_URL",
    "GOOGLE_CALENDAR_ICAL_URL",
    "X_BEARER_TOKEN"
)
foreach ($name in $optionalEnv) {
    $presence = Get-EnvPresence -Name $name
    if ($presence -eq "missing") {
        Add-HealthResult -Level "WARN" -Category "environment" -Name $name -Detail "Missing optional integration setting."
    } else {
        Add-HealthResult -Level "OK" -Category "environment" -Name $name -Detail $presence
    }
}

$aiReplyMode = [Environment]::GetEnvironmentVariable("DISCORD_AI_REPLY_MODE", "User")
if ([string]::IsNullOrWhiteSpace($aiReplyMode)) {
    $aiReplyMode = "QueueOnly"
}
Add-HealthResult -Level "OK" -Category "environment" -Name "DISCORD_AI_REPLY_MODE" -Detail "mode=$aiReplyMode"
if ($aiReplyMode -eq "OpenAI") {
    $openAiPresence = Get-EnvPresence -Name "OPENAI_API_KEY"
    if ($openAiPresence -eq "missing") {
        Add-HealthResult -Level "WARN" -Category "environment" -Name "OPENAI_API_KEY" -Detail "Missing, but DISCORD_AI_REPLY_MODE is OpenAI."
    } else {
        Add-HealthResult -Level "OK" -Category "environment" -Name "OPENAI_API_KEY" -Detail $openAiPresence
    }
} else {
    Add-HealthResult -Level "OK" -Category "environment" -Name "OPENAI_API_KEY" -Detail "Not required in QueueOnly/no-API mode."
}

$weatherLat = Get-EnvPresence -Name "WEATHER_LATITUDE"
$weatherLon = Get-EnvPresence -Name "WEATHER_LONGITUDE"
if ($weatherLat -eq "missing" -or $weatherLon -eq "missing") {
    Add-HealthResult -Level "WARN" -Category "environment" -Name "weather coordinates" -Detail "WEATHER_LATITUDE or WEATHER_LONGITUDE is missing."
} else {
    Add-HealthResult -Level "OK" -Category "environment" -Name "weather coordinates" -Detail "Weather coordinates are configured."
}
$weatherLabel = Get-EnvPresence -Name "WEATHER_LOCATION_LABEL"
if ($weatherLabel -eq "missing") {
    Add-HealthResult -Level "WARN" -Category "environment" -Name "weather label" -Detail "WEATHER_LOCATION_LABEL is missing."
} else {
    Add-HealthResult -Level "OK" -Category "environment" -Name "weather label" -Detail $weatherLabel
}

$inboxRoot = Join-Path $RepositoryRoot "records\inbox"
if (Test-Path -LiteralPath $inboxRoot) {
    $datedJsonlFiles = @(Get-ChildItem -LiteralPath $inboxRoot -Recurse -File -ErrorAction SilentlyContinue | Where-Object {
        $_.Extension -eq ".jsonl" -and $_.Name -like "*$Date*"
    })
    if ($datedJsonlFiles.Count -eq 0) {
        Add-HealthResult -Level "OK" -Category "inbox" -Name "dated JSONL files" -Detail "No dated JSONL files to validate."
    } else {
        foreach ($file in $datedJsonlFiles) {
            Test-JsonLinesFile -File $file
        }
    }
}

$aiPendingPath = Join-Path $RepositoryRoot "records\inbox\ai-chat\$Date-pending.jsonl"
$aiStatePath = Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv"
$repliedIds = New-Object 'System.Collections.Generic.HashSet[string]'
if (Test-Path -LiteralPath $aiStatePath) {
    foreach ($row in @(Import-Csv -LiteralPath $aiStatePath)) {
        $status = ""
        if ($row.PSObject.Properties.Name -contains "Status") {
            $status = ([string]$row.Status).ToLowerInvariant()
        }
        if ($status -eq "replied" -or ([string]::IsNullOrWhiteSpace($status) -and $row.PSObject.Properties.Name -contains "RepliedAt" -and -not [string]::IsNullOrWhiteSpace([string]$row.RepliedAt))) {
            if (-not [string]::IsNullOrWhiteSpace([string]$row.MessageId)) {
                [void]$repliedIds.Add([string]$row.MessageId)
            }
        }
    }
}
$pendingUnreplied = 0
$seenPendingIds = New-Object 'System.Collections.Generic.HashSet[string]'
if (Test-Path -LiteralPath $aiPendingPath) {
    foreach ($line in Get-Content -LiteralPath $aiPendingPath -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try {
            $item = $line | ConvertFrom-Json
            $messageId = [string]$item.message_id
            $content = [string]$item.content
            if ([string]::IsNullOrWhiteSpace($messageId) -or [string]::IsNullOrWhiteSpace($content)) {
                continue
            }
            if ($seenPendingIds.Contains($messageId)) {
                continue
            }
            [void]$seenPendingIds.Add($messageId)
            if (-not $repliedIds.Contains($messageId)) {
                $pendingUnreplied++
            }
        } catch {}
    }
}
if ($pendingUnreplied -gt 0) {
    Add-HealthResult -Level "WARN" -Category "ai-chat" -Name "pending self-manzokubun replies" -Detail "$pendingUnreplied pending message(s) are not marked replied."
} else {
    Add-HealthResult -Level "OK" -Category "ai-chat" -Name "pending self-manzokubun replies" -Detail "No unreplied pending messages."
}

$gatewayStatePath = Join-Path $RepositoryRoot "records\logs\discord-gateway-listener-state.csv"
if (Test-Path -LiteralPath $gatewayStatePath) {
    $latestSeen = @(Import-Csv -LiteralPath $gatewayStatePath | Where-Object { -not [string]::IsNullOrWhiteSpace($_.SeenAt) } | Sort-Object SeenAt | Select-Object -Last 1)
    if ($latestSeen.Count -gt 0) {
        try {
            $seenAt = [DateTimeOffset]::Parse([string]$latestSeen[0].SeenAt, [Globalization.CultureInfo]::InvariantCulture)
            $ageMinutes = ([DateTimeOffset]::Now - $seenAt).TotalMinutes
            $latestKind = ""
            if ($latestSeen[0].PSObject.Properties.Name -contains "Kind") {
                $latestKind = [string]$latestSeen[0].Kind
            }
            if ($latestKind -eq "listener-error") {
                Add-HealthResult -Level "WARN" -Category "ai-chat" -Name "gateway listener state" -Detail ("Listener errored {0:N0} minute(s) ago." -f $ageMinutes)
            } elseif ($latestKind -eq "listener-stop") {
                Add-HealthResult -Level "WARN" -Category "ai-chat" -Name "gateway listener state" -Detail ("Listener stopped {0:N0} minute(s) ago." -f $ageMinutes)
            } elseif ($ageMinutes -le 180) {
                Add-HealthResult -Level "OK" -Category "ai-chat" -Name "gateway listener state" -Detail ("Last listener state was {0} {1:N0} minute(s) ago." -f $latestKind, $ageMinutes)
            } else {
                Add-HealthResult -Level "WARN" -Category "ai-chat" -Name "gateway listener state" -Detail ("No listener state recorded in the last {0:N0} minute(s). Last state: {1}." -f $ageMinutes, $latestKind)
            }
        } catch {
            Add-HealthResult -Level "WARN" -Category "ai-chat" -Name "gateway listener state" -Detail "Could not parse listener SeenAt timestamp."
        }
    } else {
        Add-HealthResult -Level "WARN" -Category "ai-chat" -Name "gateway listener state" -Detail "Listener state file exists but has no SeenAt rows."
    }
} else {
    Add-HealthResult -Level "WARN" -Category "ai-chat" -Name "gateway listener state" -Detail "No listener state file yet. Start start-self-manzokubun-event-responder.ps1 for event-driven detection."
}

$weatherPath = Join-Path $RepositoryRoot "records\inbox\weather\$Date.json"
if (Test-Path -LiteralPath $weatherPath) {
    Test-JsonFile -Path $weatherPath -Category "inbox" -Name "weather JSON"
} elseif ($weatherLat -eq "missing" -or $weatherLon -eq "missing") {
    Add-HealthResult -Level "OK" -Category "inbox" -Name "weather JSON" -Detail "Weather capture is not configured, so no weather JSON is expected."
} else {
    Add-HealthResult -Level "WARN" -Category "inbox" -Name "weather JSON" -Detail "Weather is configured, but $weatherPath does not exist yet."
}

$dailyReportPath = Join-Path $RepositoryRoot "records\daily\$Date.md"
if (Test-Path -LiteralPath $dailyReportPath) {
    $dailyText = Get-Content -LiteralPath $dailyReportPath -Raw -Encoding UTF8
    if ($dailyText -match "(?m)^## Discord Digest\s*$") {
        Add-HealthResult -Level "OK" -Category "reports" -Name "Discord Digest section" -Detail "Present in records daily report."
    } else {
        Add-HealthResult -Level "WARN" -Category "reports" -Name "Discord Digest section" -Detail "Missing in records daily report."
    }
    $weatherTransitionHeading = -join @([char]0x5929, [char]0x6C17, [char]0x306E, [char]0x79FB, [char]0x308A, [char]0x5909, [char]0x308F, [char]0x308A)
    $weatherHeadingPattern = "(?m)^#\s*$([regex]::Escape($weatherTransitionHeading))\s*$"
    if ((Test-Path -LiteralPath $weatherPath) -and $dailyText -notmatch $weatherHeadingPattern) {
        Add-HealthResult -Level "WARN" -Category "reports" -Name "weather transition section" -Detail "Weather JSON exists, but the report has no weather transition section."
    } else {
        Add-HealthResult -Level "OK" -Category "reports" -Name "weather transition section" -Detail "Present or not required yet."
    }
} else {
    Add-HealthResult -Level "WARN" -Category "reports" -Name "daily report" -Detail "Not generated yet: $dailyReportPath"
}

$automationRoot = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex\automations"
$expectedAutomations = @(
    "daily-research-report",
    "discord-command-poller",
    "morning-daily-brief",
    "nightly-reflection-prompt",
    "self-manzokubun-discord-responder"
)
if (Test-Path -LiteralPath $automationRoot) {
    foreach ($name in $expectedAutomations) {
        $tomlPath = Join-Path (Join-Path $automationRoot $name) "automation.toml"
        if (Test-Path -LiteralPath $tomlPath) {
            $toml = Get-Content -LiteralPath $tomlPath -Raw -Encoding UTF8
            $status = "unknown"
            if ($toml -match '(?m)^\s*status\s*=\s*"([^"]+)"') {
                $status = $Matches[1]
            } elseif ($toml -match "(?m)^\s*paused\s*=\s*true\s*$") {
                $status = "PAUSED"
            } else {
                $status = "not explicitly paused"
            }
            $schedule = ""
            if ($toml -match "(?m)^\s*rrule\s*=\s*`"([^`"]+)`"") {
                $schedule = " schedule=$($Matches[1])"
            }
            Add-HealthResult -Level "OK" -Category "automations" -Name $name -Detail "status=$status.$schedule"
        } else {
            Add-HealthResult -Level "WARN" -Category "automations" -Name $name -Detail "automation.toml not found."
        }
    }
} else {
    Add-HealthResult -Level "WARN" -Category "automations" -Name "automation root" -Detail "No Codex automation directory found."
}

$healthDir = Join-Path $RepositoryRoot "records\health"
if ($WriteReport -and -not (Test-Path -LiteralPath $healthDir)) {
    New-Item -ItemType Directory -Path $healthDir | Out-Null
}
if (Test-Path -LiteralPath (Split-Path -Parent $healthDir)) {
    try {
        if (-not (Test-Path -LiteralPath $healthDir)) {
            New-Item -ItemType Directory -Path $healthDir | Out-Null
        }
        $writeTestPath = Join-Path $healthDir ".write-test"
        Set-Content -LiteralPath $writeTestPath -Value "ok" -Encoding UTF8
        Remove-Item -LiteralPath $writeTestPath -Force
        Add-HealthResult -Level "OK" -Category "paths" -Name "health report directory" -Detail "Writable."
    } catch {
        Add-HealthResult -Level "FAIL" -Category "paths" -Name "health report directory" -Detail "Not writable: $($_.Exception.Message)"
    }
}

$failCount = @($Results | Where-Object { $_.level -eq "FAIL" }).Count
$warnCount = @($Results | Where-Object { $_.level -eq "WARN" }).Count
$okCount = @($Results | Where-Object { $_.level -eq "OK" }).Count
$overall = if ($failCount -gt 0) { "FAIL" } elseif ($warnCount -gt 0) { "WARN" } else { "OK" }
$generatedAt = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9)).ToString("yyyy-MM-dd HH:mm:ss zzz")

if ($WriteReport) {
    $markdownPath = Join-Path $healthDir "$Date.md"
    $jsonPath = Join-Path $healthDir "$Date.json"
    $lines = New-Object 'System.Collections.Generic.List[string]'
    $lines.Add("# Automation Health - $Date") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("- Generated: $generatedAt") | Out-Null
    $lines.Add("- Overall: $overall") | Out-Null
    $lines.Add("- OK: $okCount / WARN: $warnCount / FAIL: $failCount") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("## Findings") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("| Level | Category | Check | Detail |") | Out-Null
    $lines.Add("| --- | --- | --- | --- |") | Out-Null
    foreach ($result in $Results) {
        $lines.Add("| $(Escape-MarkdownCell $result.level) | $(Escape-MarkdownCell $result.category) | $(Escape-MarkdownCell $result.name) | $(Escape-MarkdownCell $result.detail) |") | Out-Null
    }
    $lines.Add("") | Out-Null
    $lines.Add("## Next Actions") | Out-Null
    $lines.Add("") | Out-Null
    $actionItems = @($Results | Where-Object { $_.level -in @("FAIL", "WARN") } | Select-Object -First 12)
    if ($actionItems.Count -eq 0) {
        $lines.Add("- No action needed.") | Out-Null
    } else {
        foreach ($item in $actionItems) {
            $lines.Add("- [$($item.level)] $($item.name): $($item.detail)") | Out-Null
        }
    }
    Set-Content -LiteralPath $markdownPath -Value ($lines -join "`r`n") -Encoding UTF8

    $payload = [ordered]@{
        date = $Date
        generated_at_jst = $generatedAt
        overall = $overall
        counts = [ordered]@{
            ok = $okCount
            warn = $warnCount
            fail = $failCount
        }
        results = @($Results.ToArray())
    }
    $payload | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $jsonPath -Encoding UTF8
}

Write-Host "Automation health ($Date): $overall (OK=$okCount WARN=$warnCount FAIL=$failCount)"
if ($WriteReport) {
    Write-Host "Health report: $(Join-Path $healthDir "$Date.md")"
}

if ($FailOnCritical -and $failCount -gt 0) {
    exit 1
}

