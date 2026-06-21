param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [string]$InboxPath,
    [string]$StatePath,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($InboxPath)) {
    $InboxPath = Join-Path $RepositoryRoot "records\inbox\gmail\$Date.jsonl"
}
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\gmail-announcement-state.csv"
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

function Get-KindLabel {
    param([object]$Item)
    $kind = if ($Item.PSObject.Properties.Name -contains "kind") { [string]$Item.kind } else { "" }
    switch ($kind) {
        "tutoring" { return (-join @([char]0x587E, [char]0x8B1B, [char]0x5E2B, [char]0x30D0, [char]0x30A4, [char]0x30C8)) }
        "university" { return (-join @([char]0x5927, [char]0x5B66)) }
        default { return (-join @([char]0x30E1, [char]0x30FC, [char]0x30EB)) }
    }
}

function Get-WebhookEnvVar {
    param([object]$Item)
    $kind = if ($Item.PSObject.Properties.Name -contains "kind") { [string]$Item.kind } else { "" }
    switch ($kind) {
        "tutoring" { return "DISCORD_TUTORING_MAIL_WEBHOOK_URL" }
        default { return "DISCORD_UNIVERSITY_MAIL_WEBHOOK_URL" }
    }
}

function Get-MessageId {
    param([object]$Item)
    if ($Item.PSObject.Properties.Name -contains "message_id" -and -not [string]::IsNullOrWhiteSpace([string]$Item.message_id)) {
        return [string]$Item.message_id
    }
    return (($Item.subject, $Item.received_at, $Item.from) -join "|")
}

function New-AnnouncementContent {
    param([object]$Item)

    $kind = Get-KindLabel -Item $Item
    $subject = Get-ShortLine -Text ([string]$Item.subject) -MaxChars 180
    $from = Get-ShortLine -Text ([string]$Item.from) -MaxChars 120
    $received = Get-ShortLine -Text ([string]$Item.received_at) -MaxChars 40
    $hints = @($Item.task_hints | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) } | Select-Object -First 4)
    $hintText = if ($hints.Count -gt 0) { "`n- " + ($hints -join "`n- ") } else { "`n- Please review the message." }

    $content = @(
        "[$kind Mail Task]"
        $subject
        ""
        "from: $from"
        "received: $received"
        "Candidates:$hintText"
    ) -join "`n"

    if ($content.Length -gt 1800) {
        return $content.Substring(0, 1790) + "...(truncated)"
    }
    return $content
}

$records = @(Read-JsonLines -Path $InboxPath)
if ($records.Count -eq 0) {
    Write-Host "No Gmail task records found: $InboxPath"
    exit 0
}

$announced = New-Object 'System.Collections.Generic.HashSet[string]'
if (Test-Path -LiteralPath $StatePath) {
    foreach ($row in @(Import-Csv -LiteralPath $StatePath)) {
        if (-not [string]::IsNullOrWhiteSpace($row.MessageId)) {
            [void]$announced.Add($row.MessageId)
        }
    }
}

$newRows = New-Object 'System.Collections.Generic.List[object]'
$postedCount = 0
foreach ($item in ($records | Sort-Object received_at, subject)) {
    $messageId = Get-MessageId -Item $item
    if ($announced.Contains($messageId)) { continue }

    $envVar = Get-WebhookEnvVar -Item $item
    $content = New-AnnouncementContent -Item $item
    if ($DryRun) {
        Write-Host "Would post to $envVar`:"
        Write-Host $content
    } else {
        & (Join-Path $ScriptRoot "post-discord-webhook.ps1") -WebhookEnvVar $envVar -Content $content
    }

    $postedCount += 1
    [void]$announced.Add($messageId)
    $newRows.Add([pscustomobject]@{
        MessageId = $messageId
        Kind = Get-KindLabel -Item $item
        WebhookEnvVar = $envVar
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

Write-Host "Posted $postedCount Gmail task announcement(s)."
