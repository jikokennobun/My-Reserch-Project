param(
    [string]$Date,
    [switch]$ScheduledRun,
    [string]$RepositoryRoot
)

$ErrorActionPreference = "Continue"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
Set-Location -LiteralPath $RepositoryRoot

if ([string]::IsNullOrWhiteSpace($Date)) {
    $jst = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9))
    if ($ScheduledRun) {
        $jst = $jst.AddMinutes(-5)
    }
    $Date = $jst.ToString("yyyy-MM-dd")
}

$envNames = @(
    "DISCORD_BOT_TOKEN",
    "DISCORD_GUILD_ID",
    "DISCORD_DAILY_CHANNEL_ID",
    "DISCORD_DAILY_WEBHOOK_URL",
    "DISCORD_MONTHLY_DAILY_WEBHOOK_URL",
    "DISCORD_FOOD_CHANNEL_ID",
    "DISCORD_WATCH_CHANNEL_ID",
    "DISCORD_WATCHLIST_CHANNEL_ID",
    "DISCORD_ACTIVITY_CHANNEL_ID",
    "DISCORD_MOOD_CHANNEL_ID",
    "DISCORD_WAKE_CHANNEL_ID",
    "DISCORD_REFLECTION_CHANNEL_ID",
    "DISCORD_COMMAND_CHANNEL_ID",
    "DISCORD_SELF_USER_ID",
    "DISCORD_CALENDAR_WEBHOOK_URL",
    "DISCORD_UNIVERSITY_MAIL_WEBHOOK_URL",
    "DISCORD_TUTORING_MAIL_WEBHOOK_URL",
    "DISCORD_MAIL_TIMELINE_WEBHOOK_URL",
    "GOOGLE_CALENDAR_ICAL_URL",
    "WEATHER_LATITUDE",
    "WEATHER_LONGITUDE",
    "WEATHER_LOCATION_LABEL",
    "X_BEARER_TOKEN"
)

foreach ($name in $envNames) {
    $value = [Environment]::GetEnvironmentVariable($name, "User")
    if (-not [string]::IsNullOrWhiteSpace($value)) {
        Set-Item -Path "Env:$name" -Value $value
    }
}

$RunStartedAt = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9))
$RunId = "daily-research-report-$($RunStartedAt.ToString("yyyyMMdd-HHmmss"))"
$StepResults = New-Object 'System.Collections.Generic.List[object]'
$LockAcquired = $false
$LockPath = Join-Path $RepositoryRoot "records\logs\automation-runs\daily-research-report.lock"

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

function Acquire-AutomationLock {
    param(
        [string]$Path,
        [int]$StaleHours = 6
    )

    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
    }

    if (Test-Path -LiteralPath $Path) {
        $existing = Get-Item -LiteralPath $Path
        $ageHours = ([DateTime]::Now - $existing.LastWriteTime).TotalHours
        if ($ageHours -lt $StaleHours) {
            throw "Another daily automation run appears active. Lock: $Path"
        }
        Remove-Item -LiteralPath $Path -Force
        Write-Warning "Removed stale daily automation lock: $Path"
    }

    $lockPayload = [ordered]@{
        run_id = $RunId
        job = "daily-research-report"
        date = $Date
        started_at_jst = $RunStartedAt.ToString("yyyy-MM-dd HH:mm:ss zzz")
    } | ConvertTo-Json -Compress

    New-Item -ItemType File -Path $Path -Value $lockPayload -ErrorAction Stop | Out-Null
    $script:LockAcquired = $true
}

function Release-AutomationLock {
    param([string]$Path)

    if ($script:LockAcquired -and (Test-Path -LiteralPath $Path)) {
        Remove-Item -LiteralPath $Path -Force
        $script:LockAcquired = $false
    }
}

function Invoke-Step {
    param(
        [string]$Name,
        [scriptblock]$Block,
        [ValidateSet("critical", "degraded", "optional")]
        [string]$Severity = "optional"
    )

    Write-Host "--- $Name"
    $stepStartedAt = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9))
    $status = "ok"
    $detail = ""
    try {
        $global:LASTEXITCODE = 0
        & $Block
        if ($LASTEXITCODE -ne 0) {
            $status = "failed"
            $detail = "exit code $LASTEXITCODE"
            Write-Warning "$Name exited with $LASTEXITCODE"
            $global:LASTEXITCODE = 0
        }
    } catch {
        $status = "failed"
        $detail = $_.Exception.Message
        Write-Warning "$Name failed: $detail"
    } finally {
        $stepEndedAt = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9))
        $StepResults.Add([pscustomobject][ordered]@{
            name = $Name
            severity = $Severity
            status = $status
            detail = $detail
            started_at_jst = $stepStartedAt.ToString("yyyy-MM-dd HH:mm:ss zzz")
            ended_at_jst = $stepEndedAt.ToString("yyyy-MM-dd HH:mm:ss zzz")
            duration_seconds = [Math]::Round(($stepEndedAt - $stepStartedAt).TotalSeconds, 3)
        }) | Out-Null
    }
}

function Write-AutomationRunLedger {
    param([string]$FinalMessage)

    $runEndedAt = [DateTimeOffset]::UtcNow.ToOffset([TimeSpan]::FromHours(9))
    $criticalFailures = @($StepResults | Where-Object { $_.status -ne "ok" -and $_.severity -eq "critical" })
    $degradedFailures = @($StepResults | Where-Object { $_.status -ne "ok" -and $_.severity -eq "degraded" })
    $optionalFailures = @($StepResults | Where-Object { $_.status -ne "ok" -and $_.severity -eq "optional" })
    $overallStatus = if ($criticalFailures.Count -gt 0) {
        "failed"
    } elseif (($degradedFailures.Count + $optionalFailures.Count) -gt 0) {
        "completed_with_warnings"
    } else {
        "completed"
    }

    $envReadiness = [ordered]@{}
    foreach ($name in $envNames) {
        $envReadiness[$name] = Get-EnvPresence -Name $name
    }

    $outputs = [ordered]@{
        daily_report = Test-Path -LiteralPath (Join-Path $RepositoryRoot "records\daily\$Date.md")
        health_report = Test-Path -LiteralPath (Join-Path $RepositoryRoot "records\health\$Date.md")
        weekly_report_dir = Test-Path -LiteralPath (Join-Path $RepositoryRoot "records\periodic")
        monthly_report_dir = Test-Path -LiteralPath (Join-Path $RepositoryRoot "records\periodic")
    }

    $payload = [ordered]@{
        run_id = $RunId
        job = "daily-research-report"
        date = $Date
        status = $overallStatus
        message = $FinalMessage
        started_at_jst = $RunStartedAt.ToString("yyyy-MM-dd HH:mm:ss zzz")
        ended_at_jst = $runEndedAt.ToString("yyyy-MM-dd HH:mm:ss zzz")
        duration_seconds = [Math]::Round(($runEndedAt - $RunStartedAt).TotalSeconds, 3)
        counts = [ordered]@{
            steps = $StepResults.Count
            critical_failures = $criticalFailures.Count
            degraded_failures = $degradedFailures.Count
            optional_failures = $optionalFailures.Count
        }
        env_readiness = $envReadiness
        outputs = $outputs
        steps = @($StepResults.ToArray())
    }

    $runLogDir = Join-Path $RepositoryRoot "records\logs\automation-runs"
    if (-not (Test-Path -LiteralPath $runLogDir)) {
        New-Item -ItemType Directory -Path $runLogDir | Out-Null
    }
    $runLogPath = Join-Path $runLogDir "$Date.jsonl"
    Add-Content -LiteralPath $runLogPath -Value ($payload | ConvertTo-Json -Depth 10 -Compress) -Encoding UTF8
    Write-Host "Automation run ledger: $runLogPath"
    return $overallStatus
}

Write-Host "Daily research report run date: $Date"
Acquire-AutomationLock -Path $LockPath

Invoke-Step -Name "repair local automation state" -Severity "critical" -Block {
    .\code\scripts\repair-automation-state.ps1 -Date $Date
}
Invoke-Step -Name "preflight automation health" -Severity "degraded" -Block {
    .\code\scripts\test-automation-health.ps1 -Date $Date -WriteReport
}

Invoke-Step -Name "ensure monthly daily channel" -Severity "degraded" -Block {
    .\code\scripts\ensure-discord-monthly-daily-channel.ps1 -Date $Date -CreateWebhook -StoreInUserEnvironment
}
Invoke-Step "ensure life-log channels" {
    .\code\scripts\ensure-discord-life-log-channels.ps1 -StoreInUserEnvironment
}
Invoke-Step "ensure command channel" {
    .\code\scripts\ensure-discord-command-channel.ps1 -StoreInUserEnvironment
}
Invoke-Step "ensure watchlist channel" {
    .\code\scripts\ensure-discord-watchlist-channel.ps1 -StoreInUserEnvironment
}
Invoke-Step "ensure calendar channel" {
    .\code\scripts\ensure-discord-calendar-channel.ps1 -CreateWebhook -StoreInUserEnvironment
}
Invoke-Step "ensure mail announcement channels" {
    .\code\scripts\ensure-discord-mail-announcement-channels.ps1 -CreateWebhooks -StoreInUserEnvironment
}
Invoke-Step "ensure AI chat channel" {
    .\code\scripts\ensure-discord-ai-chat-channel.ps1 -StoreInUserEnvironment
}

foreach ($name in $envNames) {
    $value = [Environment]::GetEnvironmentVariable($name, "User")
    if (-not [string]::IsNullOrWhiteSpace($value)) {
        Set-Item -Path "Env:$name" -Value $value
    }
}

Invoke-Step "export daily Discord channel" {
    .\code\scripts\export-discord-channel-messages.ps1 -Date $Date
}
Invoke-Step "export recent primary guild activity" {
    .\code\scripts\export-discord-recent-activity.ps1 -StartDate $Date -EndDate $Date
}
Invoke-Step "process recent Discord math musings" {
    $recentPath = Join-Path $RepositoryRoot "records\inbox\discord\recent-$Date-$Date.jsonl"
    if (Test-Path -LiteralPath $recentPath) {
        .\code\scripts\process-discord-codex-commands.ps1 -Date $Date -SourcePath $recentPath -NaturalLanguage
    } else {
        Write-Host "Recent Discord activity export not found. Skipping general-channel musing scan."
    }
}
Invoke-Step "build Discord discussion summary" {
    .\code\scripts\new-discord-discussion-summary.ps1 -Date $Date
}
Invoke-Step "export external Discord activity" {
    .\code\scripts\export-discord-external-activity.ps1 -Date $Date
}
Invoke-Step "collect Discord food images" {
    .\code\scripts\collect-discord-food-images.ps1 -Date $Date
}
Invoke-Step "export Discord watch-log activity" {
    .\code\scripts\export-discord-watch-activity.ps1 -Date $Date
}
Invoke-Step "export Discord watchlist activity" {
    .\code\scripts\export-discord-watchlist-activity.ps1 -Date $Date
}
foreach ($kind in @("activity", "mood", "wake")) {
    Invoke-Step "export $kind log" {
        .\code\scripts\export-discord-log-channel.ps1 -LogKind $kind -Date $Date
    }
}
Invoke-Step "process Discord Codex commands" {
    .\code\scripts\process-discord-codex-commands.ps1 -Date $Date -NaturalLanguage
}
Invoke-Step "enrich video metadata" {
    .\code\scripts\enrich-video-metadata.ps1 -Date $Date
}
Invoke-Step "sync calendar notifications" {
    .\code\scripts\sync-calendar-notifications.ps1 -Date $Date -IncludeDiscordEvents -SyncObsidian -PostDiscordDigest
}
Invoke-Step "import Gmail task export" {
    .\code\scripts\import-gmail-task-export.ps1 -Date $Date -SyncObsidian
}
Invoke-Step "post Gmail task announcements" {
    .\code\scripts\post-gmail-task-announcements.ps1 -Date $Date
}
Invoke-Step "sync mail deadline reminders" {
    .\code\scripts\sync-mail-deadline-reminders.ps1 -Date $Date -SyncObsidian -PostDiscordReminders
}
Invoke-Step "new mail action timeline" {
    .\code\scripts\new-mail-action-timeline.ps1 -Date $Date -SyncObsidian -PostDiscord
}
Invoke-Step "import ChatGPT Pro ideas" {
    .\code\scripts\import-chatgpt-pro-ideas.ps1 -Date $Date -SyncObsidian
}
Invoke-Step "collect weather activity" {
    .\code\scripts\collect-weather-activity.ps1 -Date $Date
}
if (-not [string]::IsNullOrWhiteSpace($env:X_BEARER_TOKEN)) {
    Invoke-Step "import Twitter/X activity" {
        .\code\scripts\import-twitter-activity.ps1 -Date $Date -FetchApi
    }
} else {
    Write-Host "--- import Twitter/X activity"
    Write-Host "X_BEARER_TOKEN is not configured. Skipping Twitter/X import."
}
Invoke-Step "index Obsidian research notes" {
    .\code\scripts\index-obsidian-research.ps1
}
Invoke-Step -Name "new daily report" -Severity "critical" -Block {
    .\code\scripts\new-daily-report.ps1 -Date $Date -SyncObsidian -PostDiscordDigest
}
Invoke-Step "extract todo candidates" {
    .\code\scripts\extract-todo-candidates.ps1 -Date $Date
}
Invoke-Step "classify research activity" {
    .\code\scripts\classify-research-activity.ps1 -Date $Date
}
Invoke-Step "extract proof obligations" {
    .\code\scripts\extract-proof-obligations.ps1 -Date $Date
}
Invoke-Step "build activity correspondence" {
    .\code\scripts\build-activity-correspondence.ps1 -Date $Date
}
Invoke-Step "new weekly report" {
    .\code\scripts\new-periodic-report.ps1 -Date $Date -Period week
}
Invoke-Step "new monthly report" {
    .\code\scripts\new-periodic-report.ps1 -Date $Date -Period month
}
Invoke-Step -Name "postflight automation health" -Severity "degraded" -Block {
    .\code\scripts\test-automation-health.ps1 -Date $Date -WriteReport
}

$finalStatus = Write-AutomationRunLedger -FinalMessage "Daily research report automation completed for $Date."
Release-AutomationLock -Path $LockPath
if ($finalStatus -eq "failed") {
    Write-Warning "Daily research report automation finished with critical failures for $Date."
    exit 1
}

Write-Host "Daily research report automation completed for $Date ($finalStatus)."
