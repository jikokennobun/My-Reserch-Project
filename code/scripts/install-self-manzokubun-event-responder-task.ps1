param(
    [string]$TaskName = "Self-Manzokubun Discord Event Responder",
    [ValidateSet("QueueOnly", "OpenAI")]
    [string]$ReplyMode = "QueueOnly",
    [string]$ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", "User"),
    [switch]$StartNow
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
$Launcher = Join-Path $ScriptRoot "start-self-manzokubun-event-responder-scheduled.cmd"

if (-not (Test-Path -LiteralPath $Launcher)) {
    throw "Launcher not found: $Launcher"
}

$resolvedChannelId = $ChannelId
if ([string]::IsNullOrWhiteSpace($resolvedChannelId)) {
    $resolvedChannelId = [Environment]::GetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", "Process")
}
if ([string]::IsNullOrWhiteSpace($resolvedChannelId)) {
    throw "Set DISCORD_AI_CHAT_CHANNEL_ID or pass -ChannelId."
}

$cmd = Join-Path $env:SystemRoot "System32\cmd.exe"
$action = New-ScheduledTaskAction `
    -Execute $cmd `
    -Argument "/c `"$Launcher`" $ReplyMode $resolvedChannelId" `
    -WorkingDirectory $RepositoryRoot

$trigger = New-ScheduledTaskTrigger -AtLogOn
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -RestartCount 999 `
    -RestartInterval (New-TimeSpan -Minutes 1) `
    -ExecutionTimeLimit (New-TimeSpan -Days 7)

$currentUser = [Security.Principal.WindowsIdentity]::GetCurrent().Name
$principal = New-ScheduledTaskPrincipal `
    -UserId $currentUser `
    -LogonType Interactive `
    -RunLevel Limited

$description = "Runs the local Discord Gateway listener for 自己満足文. QueueOnly has no OpenAI API billing; OpenAI replies immediately through the API."
$task = New-ScheduledTask `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description $description

Register-ScheduledTask -TaskName $TaskName -InputObject $task -Force | Out-Null

if ($StartNow) {
    Start-ScheduledTask -TaskName $TaskName
}

Write-Host "Registered scheduled task: $TaskName"
Write-Host "ReplyMode: $ReplyMode"
Write-Host "ChannelId: $resolvedChannelId"
Write-Host "Launcher: $Launcher"
Write-Host "Logs: $(Join-Path $RepositoryRoot "records\logs\self-manzokubun-event-responder.out.log")"
