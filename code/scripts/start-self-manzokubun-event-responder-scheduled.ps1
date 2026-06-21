param(
    [ValidateSet("QueueOnly", "OpenAI")]
    [string]$ReplyMode = "QueueOnly",
    [string]$ChannelId
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path

$resolvedChannelId = $ChannelId
if ([string]::IsNullOrWhiteSpace($resolvedChannelId)) {
    $resolvedChannelId = [Environment]::GetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($resolvedChannelId)) {
    $resolvedChannelId = [Environment]::GetEnvironmentVariable("DISCORD_AI_CHAT_CHANNEL_ID", "Process")
}
if ([string]::IsNullOrWhiteSpace($resolvedChannelId)) {
    throw "Set DISCORD_AI_CHAT_CHANNEL_ID before starting the scheduled event responder."
}

Write-Host "Resolved DISCORD_AI_CHAT_CHANNEL_ID=$resolvedChannelId"

& (Join-Path $ScriptRoot "start-self-manzokubun-event-responder.ps1") `
    -ReplyMode $ReplyMode `
    -AiChatChannelId $resolvedChannelId `
    -WatchChannelIds @($resolvedChannelId) `
    -RepositoryRoot $RepositoryRoot
