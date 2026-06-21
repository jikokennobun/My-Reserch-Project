param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [int]$MaxBatchesPerChannel = 2,
    [int]$MaxSeconds = 60,
    [string]$RepositoryRoot,
    [switch]$AllowAnyAuthor,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}

$selfUserId = [Environment]::GetEnvironmentVariable("DISCORD_SELF_USER_ID", "User")
if (-not $AllowAnyAuthor -and [string]::IsNullOrWhiteSpace($selfUserId)) {
    throw "Set DISCORD_SELF_USER_ID before scanning general channels, or pass -AllowAnyAuthor explicitly."
}

$recentPath = Join-Path $RepositoryRoot "records\inbox\discord\recent-$Date-$Date.jsonl"

& (Join-Path $ScriptRoot "export-discord-recent-activity.ps1") `
    -StartDate $Date `
    -EndDate $Date `
    -MaxBatchesPerChannel $MaxBatchesPerChannel `
    -MaxSeconds $MaxSeconds `
    -RepositoryRoot $RepositoryRoot `
    -OutPath $recentPath

$processArgs = @{
    Date = $Date
    RepositoryRoot = $RepositoryRoot
    SourcePath = $recentPath
    NaturalLanguage = $true
}
if ($AllowAnyAuthor) { $processArgs.AllowAnyAuthor = $true }
if ($DryRun) { $processArgs.DryRun = $true }

& (Join-Path $ScriptRoot "process-discord-codex-commands.ps1") @processArgs
