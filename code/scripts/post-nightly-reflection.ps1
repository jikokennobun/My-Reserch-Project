param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$message = @"
【$Date 夜の振り返り】
よければこのまま返信してください。

1. 今日よかったこと:
2. 今日しんどかったこと:
3. 明日に回すこと:
4. 朝/昼/夜の気分:
5. ひとこと感想:
"@.Trim()

if ($DryRun) {
    Write-Host $message
    exit 0
}

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
& (Join-Path $ScriptRoot "post-discord-webhook.ps1") -Content $message

