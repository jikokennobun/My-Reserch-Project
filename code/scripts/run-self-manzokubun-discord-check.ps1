param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [int]$MaxBatchesPerChannel = 2,
    [int]$MaxSeconds = 60,
    [string]$RepositoryRoot
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}

& (Join-Path $ScriptRoot "collect-discord-math-musings.ps1") `
    -Date $Date `
    -MaxBatchesPerChannel $MaxBatchesPerChannel `
    -MaxSeconds $MaxSeconds `
    -RepositoryRoot $RepositoryRoot

& (Join-Path $ScriptRoot "export-discord-ai-chat-requests.ps1") `
    -Date $Date `
    -RepositoryRoot $RepositoryRoot
