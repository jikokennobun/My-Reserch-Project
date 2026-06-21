param(
    [ValidateSet("QueueOnly", "OpenAI")]
    [string]$ReplyMode = "QueueOnly",
    [string]$AiChatChannelId,
    [string[]]$WatchChannelIds = @(),
    [string]$RepositoryRoot,
    [int]$MaxRestarts = 0,
    [int]$InitialRestartDelaySeconds = 5,
    [int]$MaxRestartDelaySeconds = 300,
    [int]$MaxMinutesPerRun = 0,
    [switch]$SaveResearchMusings,
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

function Get-UserEnv {
    param([string]$Name)
    $value = [Environment]::GetEnvironmentVariable($Name, "User")
    if (-not [string]::IsNullOrWhiteSpace($value)) { return $value }
    return [Environment]::GetEnvironmentVariable($Name, "Process")
}

if ([string]::IsNullOrWhiteSpace($AiChatChannelId)) {
    $AiChatChannelId = Get-UserEnv -Name "DISCORD_AI_CHAT_CHANNEL_ID"
}
if ([string]::IsNullOrWhiteSpace($AiChatChannelId) -and $WatchChannelIds.Count -eq 1) {
    $AiChatChannelId = [string]$WatchChannelIds[0]
}

if ($WatchChannelIds.Count -eq 0 -and -not [string]::IsNullOrWhiteSpace($AiChatChannelId)) {
    $WatchChannelIds = @($AiChatChannelId)
}

if ($WatchChannelIds.Count -eq 0) {
    throw "Set DISCORD_AI_CHAT_CHANNEL_ID or pass -WatchChannelIds."
}

$restartCount = 0
$delay = [Math]::Max(1, $InitialRestartDelaySeconds)

Write-Host "Self-Manzokubun event responder supervisor started. ReplyMode=$ReplyMode"
Write-Host "Watching channel id(s): $($WatchChannelIds -join ', ')"
if ($ReplyMode -eq "QueueOnly") {
    Write-Host "QueueOnly mode detects posts immediately and stores pending messages without API billing."
} else {
    Write-Host "OpenAI mode detects posts immediately and replies through the OpenAI API."
}

while ($true) {
    try {
        & (Join-Path $ScriptRoot "watch-discord-message-events.ps1") `
            -RepositoryRoot $RepositoryRoot `
            -WatchChannelIds $WatchChannelIds `
            -AiChatChannelId $AiChatChannelId `
            -AiReplyMode $ReplyMode `
            -MaxMinutes $MaxMinutesPerRun `
            -SaveResearchMusings:$SaveResearchMusings `
            -AllowAnyAuthor:$AllowAnyAuthor `
            -DryRun:$DryRun
    } catch {
        Write-Warning "Self-Manzokubun event responder stopped with an error: $($_.Exception.Message)"
    }

    $restartCount++
    if ($MaxRestarts -gt 0 -and $restartCount -gt $MaxRestarts) {
        Write-Warning "MaxRestarts reached. Supervisor is stopping."
        break
    }

    Write-Host "Restarting Discord event listener in $delay second(s). Restart count: $restartCount"
    Start-Sleep -Seconds $delay
    $delay = [Math]::Min($MaxRestartDelaySeconds, [Math]::Max($delay + 1, [int]($delay * 1.6)))
}

