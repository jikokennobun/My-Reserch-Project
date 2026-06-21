param(
    [string]$Date,
    [string]$RepositoryRoot,
    [string]$PendingPath,
    [string]$StatePath,
    [string]$TriggerPath,
    [int]$MaxMessages = 3,
    [int]$ClaimStaleMinutes = 10
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
if ([string]::IsNullOrWhiteSpace($PendingPath)) {
    $PendingPath = Join-Path $RepositoryRoot "records\inbox\ai-chat\$Date-pending.jsonl"
}
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv"
}
if ([string]::IsNullOrWhiteSpace($TriggerPath)) {
    $TriggerPath = Join-Path $RepositoryRoot "records\inbox\ai-chat\pending-trigger.json"
}

function Convert-DiscordTimestamp {
    param([object]$Value)
    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return [DateTimeOffset]::MinValue }
    try { return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture) } catch { return [DateTimeOffset]::MinValue }
}

function Get-StateRows {
    $paths = @(
        $StatePath,
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-codex-state.csv"),
        (Join-Path $RepositoryRoot "records\logs\discord-ai-chat-state.csv")
    ) | Select-Object -Unique

    $rows = New-Object 'System.Collections.Generic.List[object]'
    foreach ($path in $paths) {
        if (-not (Test-Path -LiteralPath $path)) { continue }
        foreach ($row in @(Import-Csv -LiteralPath $path)) {
            $rows.Add($row) | Out-Null
        }
    }
    return @($rows.ToArray())
}

function Get-RowStatus {
    param([object]$Row)
    if ($null -eq $Row) { return "" }
    if ($Row.PSObject.Properties.Name -contains "Status" -and -not [string]::IsNullOrWhiteSpace([string]$Row.Status)) {
        return ([string]$Row.Status).ToLowerInvariant()
    }
    if ($Row.PSObject.Properties.Name -contains "RepliedAt" -and -not [string]::IsNullOrWhiteSpace([string]$Row.RepliedAt)) {
        return "replied"
    }
    return ""
}

function Get-RowUpdatedAt {
    param([object]$Row)
    foreach ($name in @("UpdatedAt", "RepliedAt", "SeenAt", "CreatedAt")) {
        if ($Row.PSObject.Properties.Name -contains $name -and -not [string]::IsNullOrWhiteSpace([string]$Row.$name)) {
            try { return [DateTimeOffset]::Parse([string]$Row.$name, [Globalization.CultureInfo]::InvariantCulture) } catch {}
        }
    }
    return [DateTimeOffset]::MinValue
}

function Get-LatestState {
    param([object[]]$Rows, [string]$MessageId)
    $matched = @($Rows | Where-Object { [string]$_.MessageId -eq [string]$MessageId })
    if ($matched.Count -eq 0) { return $null }
    return ($matched | Sort-Object { Get-RowUpdatedAt -Row $_ } | Select-Object -Last 1)
}

function Read-PendingRecords {
    if (-not (Test-Path -LiteralPath $PendingPath)) { return @() }
    $records = New-Object 'System.Collections.Generic.List[object]'
    foreach ($line in Get-Content -LiteralPath $PendingPath -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try {
            $records.Add(($line | ConvertFrom-Json)) | Out-Null
        } catch {
            Write-Warning "Ignoring invalid pending JSONL line in $PendingPath`: $($_.Exception.Message)"
        }
    }
    return @($records.ToArray())
}

function Write-Trigger {
    param([object[]]$Pending)
    $dir = Split-Path -Parent $TriggerPath
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    $latest = @($Pending | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } | Select-Object -Last 1)
    $payload = [ordered]@{
        needs_response = ($Pending.Count -gt 0)
        date = $Date
        pending_path = $PendingPath
        pending_count = $Pending.Count
        message_id = if ($latest.Count -gt 0) { [string]$latest[0].message_id } else { "" }
        channel_id = if ($latest.Count -gt 0) { [string]$latest[0].channel_id } else { "" }
        channel = if ($latest.Count -gt 0) { [string]$latest[0].channel } else { "" }
        timestamp = if ($latest.Count -gt 0) { [string]$latest[0].timestamp } else { "" }
        updated_at = (Get-Date).ToString("o")
        source = "codex-heartbeat-summary"
    }
    $payload | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $TriggerPath -Encoding UTF8
}

$triggerExists = Test-Path -LiteralPath $TriggerPath
$pendingFileExists = Test-Path -LiteralPath $PendingPath
$stateRows = @(Get-StateRows)
$records = @(Read-PendingRecords)
$targets = New-Object 'System.Collections.Generic.List[object]'

foreach ($record in ($records | Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp })) {
    $messageId = [string]$record.message_id
    if ([string]::IsNullOrWhiteSpace($messageId)) { continue }
    if ([string]::IsNullOrWhiteSpace([string]$record.content) -and @($record.attachments).Count -eq 0) { continue }

    $latest = Get-LatestState -Rows $stateRows -MessageId $messageId
    $status = Get-RowStatus -Row $latest
    if ($status -eq "replied") { continue }
    if ($status -eq "claimed") {
        $updatedAt = Get-RowUpdatedAt -Row $latest
        if (([DateTimeOffset]::Now - $updatedAt).TotalMinutes -lt $ClaimStaleMinutes) { continue }
    }

    $targets.Add($record) | Out-Null
}

$selected = @($targets.ToArray() | Select-Object -First $MaxMessages)
if ($targets.Count -gt 0) {
    Write-Trigger -Pending @($targets.ToArray())
} elseif ($triggerExists) {
    Remove-Item -LiteralPath $TriggerPath -Force
}

$result = [ordered]@{
    date = $Date
    needs_response = ($targets.Count -gt 0)
    pending_count = $targets.Count
    selected_count = $selected.Count
    trigger_exists = $triggerExists
    pending_file_exists = $pendingFileExists
    pending_path = $PendingPath
    state_path = $StatePath
    trigger_path = $TriggerPath
    records = @($selected)
}

$result | ConvertTo-Json -Depth 24
