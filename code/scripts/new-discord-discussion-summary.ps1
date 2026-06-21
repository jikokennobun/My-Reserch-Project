param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [string]$SourcePath,
    [string]$OutPath,
    [int]$MaxItems = 24,
    [switch]$IncludeBotMessages
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    $SourcePath = Join-Path $RepositoryRoot "records\inbox\discord\recent-$Date-$Date.jsonl"
}
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\discussions\daily\$Date.md"
}

function Read-JsonLines {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) { return @() }
    $items = @()
    foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $items += ($line | ConvertFrom-Json)
    }
    return $items
}

function Convert-DiscordTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture).ToOffset([TimeSpan]::FromHours(9))
}

function Get-ShortLine {
    param(
        [string]$Text,
        [int]$MaxChars = 220
    )

    if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
    $value = ($Text -replace "\s+", " ").Trim()
    if ($value.Length -le $MaxChars) { return $value }
    return $value.Substring(0, [Math]::Max(0, $MaxChars - 1)) + "..."
}

function Get-TopicTags {
    param([string]$Text)

    $tags = New-Object 'System.Collections.Generic.List[string]'
    $patterns = [ordered]@{
        "formalization" = "(Lean|Mathlib|\u5F62\u5F0F\u5316|\u8A3C\u660E\u652F\u63F4|\u691C\u8A3C)"
        "logic" = "(\u4E0D\u5B8C\u5168\u6027|\u56FA\u5B9A\u70B9|\u30ED\u30FC\u30D6|\u8A3C\u660E\u53EF\u80FD|\u5BFE\u89D2\u5316|Lob|provability|GLP)"
        "math-philosophy" = "(\u6570\u5B66\u3068\u306F|\u54F2\u5B66|\u76F4\u611F|\u610F\u7FA9|\u771F\u7406|strong programme|SSK)"
        "ai-math" = "(AI|LLM|Codex|ChatGPT|Cursor|\u751F\u6210AI)"
        "media" = "(youtu\.be|youtube\.com|\u52D5\u753B|\u8996\u8074|\u30A2\u30CB\u30E1)"
        "todo" = "(TODO|\u30BF\u30B9\u30AF|\u3084\u308B\u3053\u3068|\u7DE0\u5207)"
    }
    foreach ($key in $patterns.Keys) {
        if ($Text -match $patterns[$key]) { [void]$tags.Add($key) }
    }
    if ($tags.Count -eq 0) { [void]$tags.Add("discussion") }
    return @($tags.ToArray())
}

$messages = @(Read-JsonLines -Path $SourcePath)
$filtered = @(
    $messages |
        Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_.content) } |
        Where-Object { $IncludeBotMessages -or -not [bool]$_.author_is_bot } |
        Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
        Select-Object -First $MaxItems
)

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# Daily Discord Discussion Summary - $Date")
$lines.Add("")
$lines.Add('Source: `' + $SourcePath + '`')
$lines.Add("")

if ($filtered.Count -eq 0) {
    $lines.Add("No target Discord discussion logs were found today.")
} else {
    $lines.Add("## Discussion Cards")
    $lines.Add("")
    foreach ($message in $filtered) {
        $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
        $timeText = if ($null -eq $timestamp) { "" } else { $timestamp.ToString("HH:mm") }
        $content = Get-ShortLine -Text ([string]$message.content)
        $tags = @(Get-TopicTags -Text $content)
        $channel = [string]$message.channel
        $author = [string]$message.author

        $lines.Add("### $timeText #$channel")
        $lines.Add("")
        $lines.Add("- Tags: " + (($tags | ForEach-Object { "#" + $_ }) -join " "))
        $lines.Add("- Speaker: $author")
        $lines.Add("- Claim / musing: $content")
        $lines.Add("- Mathematical handle: Untriaged. Split into definitions, propositions, counterexamples, and sources when useful.")
        $lines.Add("- Next action: Decide whether to promote this to a Codex/Obsidian research memo.")
        $lines.Add("")
    }

    $lines.Add("## Suggested Deepening Shape")
    $lines.Add("")
    $lines.Add('- Split discussion into `definition -> proposition -> proof idea -> counterexample candidate -> sources`.')
    $lines.Add("- For formalization topics, check what Lean/Mathlib already defines.")
    $lines.Add("- For philosophy or STS topics, separate mathematical claims from sociological claims.")
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
$lines | Set-Content -LiteralPath $OutPath -Encoding UTF8
Write-Host "Wrote Discord discussion summary to $OutPath."
