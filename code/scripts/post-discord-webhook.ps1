param(
    [string]$Content,
    [string]$ContentPath,
    [string]$SectionHeading,
    [string]$WebhookEnvVar = "DISCORD_DAILY_WEBHOOK_URL",
    [string]$WebhookUrl = $env:DISCORD_DAILY_WEBHOOK_URL,
    [int]$MaxLength = 1800,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

if ([string]::IsNullOrWhiteSpace($Content) -and [string]::IsNullOrWhiteSpace($ContentPath)) {
    throw "Provide -Content or -ContentPath."
}

if (-not [string]::IsNullOrWhiteSpace($ContentPath)) {
    $resolved = Resolve-Path -LiteralPath $ContentPath
    $Content = Get-Content -LiteralPath $resolved.Path -Raw -Encoding UTF8
}

if (-not [string]::IsNullOrWhiteSpace($SectionHeading)) {
    $lines = @($Content -split "\r?\n")
    $start = -1
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match "^\s{0,3}#{1,6}\s+$([regex]::Escape($SectionHeading))\s*$") {
            $start = $i + 1
            break
        }
    }

    if ($start -lt 0) {
        throw "Section '$SectionHeading' was not found."
    }

    $section = New-Object 'System.Collections.Generic.List[string]'
    for ($i = $start; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match "^\s{0,3}#{1,6}\s+\S") {
            break
        }
        $section.Add($lines[$i])
    }
    $Content = ($section -join "`n").Trim()
}

$message = $Content.Trim()
if ([string]::IsNullOrWhiteSpace($message)) {
    throw "Discord message is empty."
}

if ($MaxLength -lt 200) {
    throw "-MaxLength must be at least 200."
}

if ($message.Length -gt $MaxLength) {
    $suffix = "`n...(truncated)"
    $message = $message.Substring(0, $MaxLength - $suffix.Length).TrimEnd() + $suffix
}

if ($DryRun) {
    Write-Host $message
    exit 0
}

if ([string]::IsNullOrWhiteSpace($WebhookUrl)) {
    $WebhookUrl = [Environment]::GetEnvironmentVariable($WebhookEnvVar, "Process")
}

if ([string]::IsNullOrWhiteSpace($WebhookUrl)) {
    $WebhookUrl = [Environment]::GetEnvironmentVariable($WebhookEnvVar, "User")
}

if ([string]::IsNullOrWhiteSpace($WebhookUrl)) {
    throw "Set $WebhookEnvVar or pass -WebhookUrl. Do not commit webhook URLs."
}

$payload = @{
    content = $message
} | ConvertTo-Json -Depth 4

Invoke-RestMethod -Method Post -Uri $WebhookUrl -ContentType "application/json; charset=utf-8" -Body $payload | Out-Null
Write-Host "Posted Discord webhook message ($($message.Length) character(s))."
