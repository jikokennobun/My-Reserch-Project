param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}

$target = [datetime]::ParseExact($Date, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
$yesterday = $target.AddDays(-1).ToString("yyyy-MM-dd")
$todoPath = Join-Path $RepositoryRoot "records\tasks\todo.md"
$yesterdayDaily = Join-Path $RepositoryRoot "records\daily\$yesterday.md"
$calendarPath = Join-Path $RepositoryRoot "records\tasks\calendar\$Date.md"
$mailDeadlinePath = Join-Path $RepositoryRoot "records\tasks\deadlines\mail-deadlines.md"

$todo = if (Test-Path -LiteralPath $todoPath) {
    (Get-Content -LiteralPath $todoPath -Encoding UTF8 |
        Select-String -Pattern "^- \[ \]" |
        ForEach-Object { $_.Line } |
        Where-Object { $_ -notmatch "None\.|No candidates|自動収集|まだありません" } |
        Select-Object -First 8) -join "`n"
} else {
    ""
}
if ([string]::IsNullOrWhiteSpace($todo)) {
    $todo = "- [ ] 気分ログ・起床ログ・視聴ログのどれかを1つ残す"
}

$calendar = if (Test-Path -LiteralPath $calendarPath) {
    (Get-Content -LiteralPath $calendarPath -Encoding UTF8 |
        Select-String -Pattern "^- \[ \]" |
        ForEach-Object { $_.Line } |
        Where-Object { $_ -notmatch "No calendar events found" } |
        Select-Object -First 6) -join "`n"
} else {
    ""
}
if ([string]::IsNullOrWhiteSpace($calendar)) {
    $calendar = "- [ ] カレンダー予定は未取得/なし"
}

$mailDeadlines = if (Test-Path -LiteralPath $mailDeadlinePath) {
    (Get-Content -LiteralPath $mailDeadlinePath -Encoding UTF8 |
        Select-String -Pattern "^- \[ \]" |
        ForEach-Object { $_.Line } |
        Where-Object { $_ -notmatch "None\." } |
        Select-Object -First 6) -join "`n"
} else {
    ""
}
if ([string]::IsNullOrWhiteSpace($mailDeadlines)) {
    $mailDeadlines = "- [ ] メール締切は未取得/なし"
}
$digest = ""
if (Test-Path -LiteralPath $yesterdayDaily) {
    $text = Get-Content -LiteralPath $yesterdayDaily -Raw -Encoding UTF8
    $match = [regex]::Match($text, "(?ms)^## Discord Digest\s*\r?\n(.*?)(?=^##|\z)")
    if ($match.Success) { $digest = $match.Groups[1].Value.Trim() }
}

$message = @"
【$Date 朝の作戦会議】
昨日の要約:
$digest

今日の候補:
$todo

予定:
$calendar

締切:
$mailDeadlines

今日の3つ:
1. 一番軽いタスクから始める
2. 研究/学習を1ブロック進める
3. 夜に気分ログと振り返りを残す
"@.Trim()

if ($DryRun) {
    Write-Host $message
    exit 0
}

& (Join-Path $ScriptRoot "post-discord-webhook.ps1") -Content $message

