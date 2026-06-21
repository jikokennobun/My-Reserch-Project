$ErrorActionPreference = "Stop"

$repositoryRoot = "C:\Users\20010215fjii\Documents\GitHub\My-Reserch-Project"
$scriptPath = Join-Path $repositoryRoot "code\scripts\start-self-manzokubun-event-responder-scheduled.ps1"
$pidPath = Join-Path $repositoryRoot "records\logs\self-manzokubun-event-responder.pid"

$process = Start-Process `
    -FilePath "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" `
    -ArgumentList @(
        "-NoProfile",
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        $scriptPath,
        "-ReplyMode",
        "QueueOnly",
        "-ChannelId",
        "1516830527687098388"
    ) `
    -WorkingDirectory $repositoryRoot `
    -WindowStyle Hidden `
    -PassThru

$process.Id | Set-Content -LiteralPath $pidPath -Encoding ascii
Write-Output $process.Id
