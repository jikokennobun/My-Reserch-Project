param(
    [string]$Date,
    [string]$RepositoryRoot,
    [switch]$RunHealthCheck
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

Set-Location -LiteralPath $RepositoryRoot

$directories = @(
    "records\daily",
    "records\discussions\daily",
    "records\health",
    "records\inbox\activity",
    "records\inbox\ai",
    "records\inbox\ai-chat",
    "records\inbox\calendar",
    "records\inbox\chatgpt",
    "records\inbox\daily-packets",
    "records\inbox\discord",
    "records\inbox\discord-commands",
    "records\inbox\discord-data-package",
    "records\inbox\discord-external",
    "records\inbox\discord-food",
    "records\inbox\gmail",
    "records\inbox\gmail-export-source",
    "records\inbox\mood",
    "records\inbox\reflection",
    "records\inbox\twitter",
    "records\inbox\wake",
    "records\inbox\watch",
    "records\inbox\weather",
    "records\inbox\youtube",
    "records\links",
    "records\logs",
    "records\periodic",
    "records\research-triage",
    "records\tasks\candidates",
    "records\tasks\deadlines",
    "records\tasks\mail",
    "research\ideas",
    "tmp\self-manzokubun-replies"
)

$created = New-Object 'System.Collections.Generic.List[string]'
foreach ($relative in $directories) {
    $path = Join-Path $RepositoryRoot $relative
    if (-not (Test-Path -LiteralPath $path)) {
        New-Item -ItemType Directory -Path $path | Out-Null
        $created.Add($relative) | Out-Null
    }
}

$todoPath = Join-Path $RepositoryRoot "records\tasks\todo.md"
if (-not (Test-Path -LiteralPath $todoPath)) {
    $todo = @(
        "# Todo",
        "",
        "## Now",
        "",
        "## Next",
        "",
        "## Waiting",
        "",
        "## Someday",
        "",
        "## Done Archive",
        ""
    )
    Set-Content -LiteralPath $todoPath -Value ($todo -join "`r`n") -Encoding UTF8
    $created.Add("records\tasks\todo.md") | Out-Null
}

$researchInboxPath = Join-Path $RepositoryRoot "research\ideas\inbox.md"
if (-not (Test-Path -LiteralPath $researchInboxPath)) {
    $researchInbox = @(
        "# Research Ideas Inbox",
        "",
        "Raw research ideas land here before classification.",
        ""
    )
    Set-Content -LiteralPath $researchInboxPath -Value ($researchInbox -join "`r`n") -Encoding UTF8
    $created.Add("research\ideas\inbox.md") | Out-Null
}

if ($created.Count -eq 0) {
    Write-Host "Automation local state already has the expected directories and seed files."
} else {
    Write-Host "Created or repaired $($created.Count) local automation path(s):"
    foreach ($item in $created) {
        Write-Host "- $item"
    }
}

if ($RunHealthCheck) {
    & (Join-Path $ScriptRoot "test-automation-health.ps1") -Date $Date -RepositoryRoot $RepositoryRoot -WriteReport
}
