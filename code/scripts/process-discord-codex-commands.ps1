param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$ChannelId = $env:DISCORD_COMMAND_CHANNEL_ID,
    [string]$BotToken = $env:DISCORD_BOT_TOKEN,
    [string]$SelfUserId = $env:DISCORD_SELF_USER_ID,
    [string]$TimeZoneOffset = "+09:00",
    [int]$MaxBatches = 10,
    [string]$RepositoryRoot,
    [string]$SourcePath,
    [string]$CommandOutPath,
    [string]$StatePath,
    [string]$TodoPath,
    [string]$ResearchInboxPath,
    [switch]$AllowAnyAuthor,
    [switch]$NaturalLanguage,
    [switch]$PostSummary,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($CommandOutPath)) {
    $CommandOutPath = Join-Path $RepositoryRoot "records\inbox\discord-commands\$Date.jsonl"
}
if ([string]::IsNullOrWhiteSpace($StatePath)) {
    $StatePath = Join-Path $RepositoryRoot "records\logs\discord-command-state.csv"
}
if ([string]::IsNullOrWhiteSpace($TodoPath)) {
    $TodoPath = Join-Path $RepositoryRoot "records\tasks\todo.md"
}
if ([string]::IsNullOrWhiteSpace($ResearchInboxPath)) {
    $ResearchInboxPath = Join-Path $RepositoryRoot "research\ideas\inbox.md"
}

if ([string]::IsNullOrWhiteSpace($ChannelId)) {
    $ChannelId = [Environment]::GetEnvironmentVariable("DISCORD_COMMAND_CHANNEL_ID", "User")
}
if ([string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = [Environment]::GetEnvironmentVariable("DISCORD_BOT_TOKEN", "User")
}
if ([string]::IsNullOrWhiteSpace($SelfUserId)) {
    $SelfUserId = [Environment]::GetEnvironmentVariable("DISCORD_SELF_USER_ID", "User")
}
if (-not [string]::IsNullOrWhiteSpace($BotToken)) {
    $BotToken = ([regex]::Replace($BotToken, "\p{C}", "")).Trim()
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 16 -Compress)
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

function ConvertTo-JsonBodyFile {
    param([object]$Body)

    $tmp = [IO.Path]::GetTempFileName()
    $json = $Body | ConvertTo-Json -Depth 16
    [IO.File]::WriteAllText($tmp, $json, [Text.UTF8Encoding]::new($false))
    return $tmp
}

function Invoke-DiscordJson {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null
    )

    $methodName = $Method.ToUpperInvariant()
    $uri = "https://discord.com/api/v10$Path"
    $args = @("-sS", "-X", $methodName, "-H", "Authorization: Bot $BotToken", "-H", "Content-Type: application/json; charset=utf-8")
    $bodyFile = $null
    if ($null -ne $Body) {
        $bodyFile = ConvertTo-JsonBodyFile -Body $Body
        $args += @("--data-binary", "@$bodyFile")
    }
    $args += $uri

    try {
        $raw = & curl.exe @args
    } finally {
        if (-not [string]::IsNullOrWhiteSpace($bodyFile) -and (Test-Path -LiteralPath $bodyFile)) {
            Remove-Item -LiteralPath $bodyFile -Force
        }
    }

    if ($LASTEXITCODE -ne 0) { throw "curl.exe failed for $methodName $Path." }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    $json = $raw | ConvertFrom-Json
    if ($json.PSObject.Properties.Name -contains "code" -and $json.PSObject.Properties.Name -contains "message" -and -not ($json.PSObject.Properties.Name -contains "id")) {
        throw "Discord API error for $methodName $Path`: $($json.message) ($($json.code))"
    }
    return $json
}

function Convert-DiscordTimestamp {
    param([object]$Value)

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    return [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
}

function Get-Urls {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return @() }
    return @([regex]::Matches($Text, "https?://\S+") | ForEach-Object { $_.Value.TrimEnd(")", "]", ">", ",", ".") })
}

function Test-MathMusing {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return $false }
    $value = ($Text -replace "\s+", " ").Trim()
    if ($value.Length -lt 8) { return $false }

    $asciiPattern = "(?i)\b(aps|ams|g2|fg2|loeb|lob|fixed\s*point|provability|modal|logic|theorem|proof|model|algebra|topology|category|survey|paper|literature|conjecture|lemma|axiom|arithmetic|ordinal|sequent|cut\s*elimination|realizability|domain\s*theory)\b"
    if ($value -match $asciiPattern) { return $true }

    $jpPattern = [regex]::Unescape("\u6570\u5B66|\u5B9A\u7406|\u8A3C\u660E|\u8AD6\u6587|\u89E3\u8AAC|\u30B5\u30FC\u30D9\u30A4|\u7814\u7A76|\u516C\u7406|\u30E2\u30C7\u30EB|\u4E0D\u5B8C\u5168|\u56FA\u5B9A\u70B9|\u7B97\u8853|\u69D8\u76F8|\u8AD6\u7406|\u4F4D\u76F8|\u570F|\u4EE3\u6570|\u30DC\u30E4\u30AD")
    return ($value -match $jpPattern)
}

function New-CommandObject {
    param(
        [string]$Kind,
        [string]$RawName,
        [string]$Body,
        [string]$Inference = "explicit"
    )

    $cleanBody = ($Body -replace "\s+", " ").Trim()
    if ([string]::IsNullOrWhiteSpace($Kind) -or [string]::IsNullOrWhiteSpace($cleanBody)) { return $null }
    return [pscustomobject]@{
        Kind = $Kind
        RawName = $RawName
        Body = $cleanBody
        Inference = $Inference
    }
}

function Get-NaturalLanguageCommand {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return $null }
    $text = ($Text -replace "\s+", " ").Trim()
    $morning = [regex]::Unescape("\u671D")
    $noon = [regex]::Unescape("\u663C")
    $night = [regex]::Unescape("\u591C")
    $laterWatch = [regex]::Unescape("\u3042\u3068\u3067\u898B\u308B")

    if ($text -match "^\s*(TODO|todo|\u30BF\u30B9\u30AF|\u3084\u308B\u3053\u3068)\s*[\uFF1A:]\s*(?<body>[\s\S]+)$") {
        return (New-CommandObject -Kind "todo" -RawName "natural-todo" -Body $Matches["body"] -Inference "natural-language")
    }
    if ($text -match "^(?<body>[\s\S]+?)\s*(\u3092)?\s*(TODO|todo|\u30BF\u30B9\u30AF|\u3084\u308B\u3053\u3068)\s*(\u306B)?\s*(\u8FFD\u52A0|\u5165\u308C|\u767B\u9332|\u8A18\u9332)\s*(\u3057\u3066|\u3057\u3068\u3044\u3066|\u304A\u9858\u3044\u3057\u307E\u3059|\u304A\u9858\u3044)?[\u3002.!\uFF01]*$") {
        return (New-CommandObject -Kind "todo" -RawName "natural-todo" -Body $Matches["body"] -Inference "natural-language")
    }

    if ($text -match "^\s*(TODO|todo|\u30BF\u30B9\u30AF|\u3084\u308B\u3053\u3068)\s*(\u5B8C\u4E86|done|\u6E08\u307F|\u7D42\u308F\u3063\u305F)\s*[\uFF1A:]\s*(?<body>[\s\S]+)$") {
        return (New-CommandObject -Kind "done" -RawName "natural-done" -Body $Matches["body"] -Inference "natural-language")
    }
    if ($text -match "^(?<body>[\s\S]+?)\s*(\u3092)?\s*(TODO|todo|\u30BF\u30B9\u30AF|\u3084\u308B\u3053\u3068)\s*(\u5B8C\u4E86|done|\u6E08\u307F|\u7D42\u308F\u3063\u305F)\s*(\u306B)?\s*(\u3057\u3066|\u767B\u9332|\u8A18\u9332)?[\u3002.!\uFF01]*$") {
        return (New-CommandObject -Kind "done" -RawName "natural-done" -Body $Matches["body"] -Inference "natural-language")
    }

    if ($text -match "^\s*(\u7814\u7A76\u30E1\u30E2|\u7814\u7A76\u30A2\u30A4\u30C7\u30A2|\u30A2\u30A4\u30C7\u30A2|idea|memo)\s*[\uFF1A:]\s*(?<body>[\s\S]+)$") {
        return (New-CommandObject -Kind "research" -RawName "natural-research" -Body $Matches["body"] -Inference "natural-language")
    }
    if ($text -match "^(?<body>[\s\S]+?)\s*(\u3092)?\s*(\u7814\u7A76\u30E1\u30E2|\u7814\u7A76\u30A2\u30A4\u30C7\u30A2|\u30A2\u30A4\u30C7\u30A2)\s*(\u3068\u3057\u3066)?\s*(\u8FFD\u52A0|\u8A18\u9332|\u4FDD\u5B58|\u30E1\u30E2)\s*(\u3057\u3066|\u3057\u3068\u3044\u3066|\u304A\u9858\u3044\u3057\u307E\u3059|\u304A\u9858\u3044)?[\u3002.!\uFF01]*$") {
        return (New-CommandObject -Kind "research" -RawName "natural-research" -Body $Matches["body"] -Inference "natural-language")
    }

    if ($text -match "^\s*(?<period>\u671D|\u663C|\u591C|\u4ECA|\u73FE\u5728|\u4ECA\u65E5)?\s*(\u306E)?\s*(\u6C17\u5206|mood)\s*[\uFF1A:]\s*(?<body>[\s\S]+)$") {
        $period = $Matches["period"]
        $body = $Matches["body"].Trim()
        if ($period -in @($morning, $noon, $night)) { $body = "$period`: $body" }
        return (New-CommandObject -Kind "mood" -RawName "natural-mood" -Body $body -Inference "natural-language")
    }

    if ($text -match "^\s*(\u898B\u305F|\u89B3\u305F|\u8996\u8074|\u52D5\u753B|\u30A2\u30CB\u30E1)\s*[\uFF1A:]\s*(?<body>[\s\S]+)$") {
        return (New-CommandObject -Kind "watch" -RawName "natural-watch" -Body $Matches["body"] -Inference "natural-language")
    }
    if ($text -match "^\s*(\u3042\u3068\u3067\u898B\u308B|\u5F8C\u3067\u898B\u308B|\u898B\u305F\u3044|\u89B3\u305F\u3044|watch later)\s*[\uFF1A:]\s*(?<body>[\s\S]+)$") {
        $body = "$laterWatch`: $($Matches["body"].Trim())"
        return (New-CommandObject -Kind "watch" -RawName "natural-later" -Body $body -Inference "natural-language")
    }

    $urls = @(Get-Urls -Text $text)
    if ($urls.Count -gt 0) {
        if ($text -match "\u3042\u3068\u3067\u898B\u308B|\u5F8C\u3067\u898B\u308B|\u898B\u305F\u3044|\u89B3\u305F\u3044|watch later|later") {
            return (New-CommandObject -Kind "watch" -RawName "natural-later" -Body $text -Inference "natural-language")
        }
        if ($text -match "\u9014\u4E2D|\u90E8\u5206|partial|\u898B\u305F|\u89B3\u305F|\u8996\u8074") {
            return (New-CommandObject -Kind "watch" -RawName "natural-watch" -Body $text -Inference "natural-language")
        }
    }

    if (Test-MathMusing -Text $text) {
        return (New-CommandObject -Kind "research" -RawName "natural-math-musing" -Body $text -Inference "math-musing")
    }

    return $null
}

function Get-PropertyText {
    param(
        [object]$Item,
        [string]$Name
    )
    if ($null -eq $Item) { return "" }
    if ($Item.PSObject.Properties.Name -contains $Name) { return [string]$Item.$Name }
    return ""
}

function Get-Command {
    param([string]$Content)

    if ([string]::IsNullOrWhiteSpace($Content)) { return $null }
    $text = $Content.Trim()
    $match = [regex]::Match($text, "^[!/](?<cmd>[A-Za-z][A-Za-z0-9_-]*)\s*:?\s*(?<body>[\s\S]*)$")
    if (-not $match.Success) {
        $match = [regex]::Match($text, "^(?<cmd>todo|task|done|finish|complete|watch|video|anime|later|want|watchlater|mood|research|idea|memo|t|d|x|w|m|r)\s*:\s*(?<body>[\s\S]*)$", [Text.RegularExpressions.RegexOptions]::IgnoreCase)
    }
    if (-not $match.Success) {
        if ($NaturalLanguage) { return (Get-NaturalLanguageCommand -Text $text) }
        return $null
    }

    $name = $match.Groups["cmd"].Value.ToLowerInvariant()
    $kind = switch ($name) {
        { $_ -in @("todo", "task", "t") } { "todo"; break }
        { $_ -in @("done", "finish", "complete", "x", "d") } { "done"; break }
        { $_ -in @("watch", "video", "anime", "w", "later", "want", "watchlater") } { "watch"; break }
        { $_ -in @("mood", "m") } { "mood"; break }
        { $_ -in @("research", "idea", "memo", "r") } { "research"; break }
        default { "" }
    }
    if ([string]::IsNullOrWhiteSpace($kind)) { return $null }

    $body = $match.Groups["body"].Value.Trim()
    return (New-CommandObject -Kind $kind -RawName $name -Body $body)
}

function Test-JsonlMessageExists {
    param(
        [string]$Path,
        [string]$MessageId
    )
    foreach ($item in @(Read-JsonLines -Path $Path)) {
        if ((Get-PropertyText -Item $item -Name "message_id") -eq $MessageId) { return $true }
    }
    return $false
}

function Add-JsonLineIfMissing {
    param(
        [string]$Path,
        [object]$Record
    )

    $messageId = Get-PropertyText -Item $Record -Name "message_id"
    if (-not [string]::IsNullOrWhiteSpace($messageId) -and (Test-JsonlMessageExists -Path $Path -MessageId $messageId)) {
        return $false
    }

    if (-not $DryRun) {
        $dir = Split-Path -Parent $Path
        if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
        Add-Content -LiteralPath $Path -Encoding UTF8 -Value (ConvertTo-JsonLine -Value $Record)
    }
    return $true
}

function Get-StateKeys {
    param([string]$Path)

    $keys = New-Object 'System.Collections.Generic.HashSet[string]'
    if (Test-Path -LiteralPath $Path) {
        foreach ($row in @(Import-Csv -LiteralPath $Path)) {
            if (-not [string]::IsNullOrWhiteSpace($row.StateKey)) {
                [void]$keys.Add($row.StateKey)
            }
        }
    }
    return ,$keys
}

function Save-StateRows {
    param(
        [string]$Path,
        [object[]]$Rows
    )

    if ($DryRun -or $Rows.Count -eq 0) { return }
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }
    if (Test-Path -LiteralPath $Path) {
        $Rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Append -Encoding UTF8
    } else {
        $Rows | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding UTF8
    }
}

function Add-Todo {
    param(
        [string]$Path,
        [string]$Text
    )

    $clean = ($Text -replace "\s+", " ").Trim()
    $clean = [regex]::Replace($clean, "^\s*-\s*\[[ xX]\]\s*", "")
    if ([string]::IsNullOrWhiteSpace($clean)) { return $false }

    if ($DryRun) {
        Write-Host "Would add TODO: $clean"
        return $true
    }

    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

    if (Test-Path -LiteralPath $Path) {
        $lines = New-Object 'System.Collections.Generic.List[string]'
        foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) { $lines.Add($line) }
    } else {
        $lines = New-Object 'System.Collections.Generic.List[string]'
        $lines.Add("# Todo")
        $lines.Add("")
        $lines.Add("## Now")
        $lines.Add("")
        $lines.Add("## Next")
        $lines.Add("")
        $lines.Add("## Waiting")
        $lines.Add("")
        $lines.Add("## Someday")
    }

    $needle = "- [ ] $clean"
    if ($lines | Where-Object { $_.Trim() -eq $needle }) { return $false }

    $nowIndex = -1
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq "## Now") { $nowIndex = $i; break }
    }
    if ($nowIndex -lt 0) {
        $lines.Insert(0, "")
        $lines.Insert(0, "## Now")
        $nowIndex = 0
    }

    $insertIndex = $nowIndex + 1
    while ($insertIndex -lt $lines.Count -and [string]::IsNullOrWhiteSpace($lines[$insertIndex])) {
        $insertIndex += 1
    }
    $lines.Insert($insertIndex, $needle)
    if (($insertIndex + 1) -lt $lines.Count -and $lines[$insertIndex + 1].Trim().StartsWith("## ")) {
        $lines.Insert($insertIndex + 1, "")
    }
    Set-Content -LiteralPath $Path -Encoding UTF8 -Value $lines
    return $true
}

function Complete-Todo {
    param(
        [string]$Path,
        [string]$Text
    )

    $needle = ($Text -replace "\s+", " ").Trim()
    $needle = [regex]::Replace($needle, "^\s*-\s*\[[ xX]\]\s*", "")
    if ([string]::IsNullOrWhiteSpace($needle)) { return $false }

    if (-not (Test-Path -LiteralPath $Path)) {
        if ($DryRun) { Write-Host "Would complete TODO matching: $needle" }
        return $false
    }

    $lines = New-Object 'System.Collections.Generic.List[string]'
    foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) { $lines.Add($line) }

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        if ($line -notmatch "^\s*-\s*\[ \]\s*(?<task>.+)$") { continue }
        $task = ($Matches["task"] -replace "\s+", " ").Trim()
        if ($task.IndexOf($needle, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) { continue }

        if ($DryRun) {
            Write-Host "Would complete TODO: $task"
            return $true
        }

        $lines[$i] = $line -replace "\[ \]", "[x]"
        Set-Content -LiteralPath $Path -Encoding UTF8 -Value $lines
        return $true
    }

    if ($DryRun) { Write-Host "No TODO matched: $needle" }
    return $false
}

function Get-WatchStatus {
    param(
        [string]$Text,
        [string]$DefaultStatus = "watched"
    )

    if ([string]::IsNullOrWhiteSpace($Text)) { return $DefaultStatus }
    if ($Text -match "\u307F\u305F\u3044|\u898B\u305F\u3044|\u898B\u3066\u306A\u3044|\u672A\u8996\u8074|\u898B\u3088\u3046|\u307E\u3060|want[- ]?to[- ]?watch|watch later|later") {
        return "want_to_watch"
    }
    if ($Text -match "\u90E8\u5206|\u9014\u4E2D|partial") {
        return "partial"
    }
    return $DefaultStatus
}

function Get-ResearchTitle {
    param([string]$Text)

    $first = (($Text -split "\r?\n") | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($first)) { return "Discord memo" }
    if ($first -match "^\s*(?<title>[^|]{2,80})\|\s*(?<rest>.+)$") {
        $first = $Matches["title"].Trim()
    }
    $first = ($first -replace "\s+", " ").Trim()
    if ($first.Length -gt 70) { $first = $first.Substring(0, 70) + "..." }
    return $first
}

function Add-ResearchMemo {
    param(
        [string]$Path,
        [string]$Text,
        [string]$DateValue,
        [string]$Timestamp,
        [string]$MessageId,
        [string]$ChannelName
    )

    $title = Get-ResearchTitle -Text $Text
    $ideaText = $Text.Trim()
    if ($ideaText -match "^\s*[^|]{2,80}\|\s*(?<rest>[\s\S]+)$") {
        $ideaText = $Matches["rest"].Trim()
    }
    if ($DryRun) {
        Write-Host "Would add research memo: $title"
        return $true
    }

    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir | Out-Null }

    if (Test-Path -LiteralPath $Path) {
        $lines = New-Object 'System.Collections.Generic.List[string]'
        foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) { $lines.Add($line) }
    } else {
        $lines = New-Object 'System.Collections.Generic.List[string]'
        $lines.Add("# Idea Inbox")
        $lines.Add("")
        $lines.Add("## Unsorted")
    }

    if ($lines | Where-Object { $_ -match [regex]::Escape($MessageId) }) { return $false }

    $block = @(
        "",
        "### $DateValue - $title",
        "",
        ("Source: Discord command " + $MessageId + " in " + $ChannelName + " at " + $Timestamp),
        "",
        "Idea:",
        $ideaText,
        "",
        "Related references:",
        "",
        "Next action:",
        "Triage this into a research note or discard it.",
        ""
    )

    $unsortedIndex = -1
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i].Trim() -eq "## Unsorted") { $unsortedIndex = $i; break }
    }
    if ($unsortedIndex -lt 0) {
        $lines.Add("")
        $lines.Add("## Unsorted")
        $unsortedIndex = $lines.Count - 1
    }

    $insertIndex = $unsortedIndex + 1
    for ($i = $block.Count - 1; $i -ge 0; $i--) {
        $lines.Insert($insertIndex, $block[$i])
    }
    Set-Content -LiteralPath $Path -Encoding UTF8 -Value $lines
    return $true
}

function Normalize-MoodText {
    param([string]$Text)

    $value = $Text.Trim()
    $morning = -join @([char]0x671D)
    $noon = -join @([char]0x663C)
    $night = -join @([char]0x591C)

    if ($value -match "^\s*(morning|am|asa)\s*[: ]\s*(?<rest>[\s\S]+)$") {
        return "$morning`: $($Matches["rest"].Trim())"
    }
    if ($value -match "^\s*(noon|afternoon|pm|hiru)\s*[: ]\s*(?<rest>[\s\S]+)$") {
        return "$noon`: $($Matches["rest"].Trim())"
    }
    if ($value -match "^\s*(night|evening|yoru)\s*[: ]\s*(?<rest>[\s\S]+)$") {
        return "$night`: $($Matches["rest"].Trim())"
    }
    return $value
}

function Get-MessagesFromSource {
    param([string]$Path)

    $items = @(Read-JsonLines -Path $Path)
    foreach ($item in $items) {
        if (-not ($item.PSObject.Properties.Name -contains "timestamp") -and ($item.PSObject.Properties.Name -contains "created_at")) {
            $item | Add-Member -NotePropertyName timestamp -NotePropertyValue $item.created_at -Force
        }
    }
    return $items
}

function Get-MessagesFromDiscord {
    if ([string]::IsNullOrWhiteSpace($ChannelId)) {
        Write-Host "DISCORD_COMMAND_CHANNEL_ID is not configured. Skipping command processing."
        return @()
    }
    if ([string]::IsNullOrWhiteSpace($BotToken)) { throw "Set DISCORD_BOT_TOKEN or pass -BotToken." }

    $start = [DateTimeOffset]::Parse("$Date`T00:00:00$TimeZoneOffset")
    $end = $start.AddDays(1)
    $channel = Invoke-DiscordJson -Method Get -Path "/channels/$ChannelId"
    $records = New-Object 'System.Collections.Generic.List[object]'
    $before = $null

    for ($batch = 0; $batch -lt $MaxBatches; $batch++) {
        $path = "/channels/$ChannelId/messages?limit=100"
        if (-not [string]::IsNullOrWhiteSpace($before)) { $path += "&before=$before" }

        $messages = @(Invoke-DiscordJson -Method Get -Path $path)
        if ($messages.Count -eq 0) { break }

        foreach ($message in $messages) {
            $timestamp = Convert-DiscordTimestamp -Value $message.timestamp
            if ($null -eq $timestamp) { continue }
            if ($timestamp -lt $start -or $timestamp -ge $end) { continue }

            $records.Add([pscustomobject][ordered]@{
                timestamp = $timestamp.ToString("o")
                channel_id = $ChannelId
                channel = $channel.name
                author = $message.author.username
                author_id = $message.author.id
                message_id = $message.id
                content = [string]$message.content
                attachments = @($message.attachments | ForEach-Object { $_.url })
            })
        }

        $oldest = $messages |
            Where-Object { $null -ne (Convert-DiscordTimestamp -Value $_.timestamp) } |
            Sort-Object { Convert-DiscordTimestamp -Value $_.timestamp } |
            Select-Object -First 1
        if ($null -eq $oldest) { break }
        if ((Convert-DiscordTimestamp -Value $oldest.timestamp) -lt $start) { break }
        $before = $oldest.id
    }
    return @($records.ToArray())
}

$messages = if ([string]::IsNullOrWhiteSpace($SourcePath)) {
    @(Get-MessagesFromDiscord)
} else {
    @(Get-MessagesFromSource -Path $SourcePath)
}

$stateKeys = Get-StateKeys -Path $StatePath
$newStateRows = New-Object 'System.Collections.Generic.List[object]'
$counts = [ordered]@{ todo = 0; done = 0; watch = 0; mood = 0; research = 0; skipped = 0 }

foreach ($message in ($messages | Sort-Object { Convert-DiscordTimestamp -Value (Get-PropertyText -Item $_ -Name "timestamp") })) {
    $authorId = Get-PropertyText -Item $message -Name "author_id"
    if (-not $AllowAnyAuthor -and -not [string]::IsNullOrWhiteSpace($SelfUserId) -and $authorId -ne $SelfUserId) {
        continue
    }

    $content = Get-PropertyText -Item $message -Name "content"
    $command = Get-Command -Content $content
    if ($null -eq $command) { continue }

    $messageId = Get-PropertyText -Item $message -Name "message_id"
    if ([string]::IsNullOrWhiteSpace($messageId)) {
        $messageId = [guid]::NewGuid().ToString("N")
    }
    $timestampText = Get-PropertyText -Item $message -Name "timestamp"
    $channelName = Get-PropertyText -Item $message -Name "channel"
    if ([string]::IsNullOrWhiteSpace($channelName)) { $channelName = "discord-command" }
    $attachments = @()
    if ($message.PSObject.Properties.Name -contains "attachments") { $attachments = @($message.attachments) }
    $urls = @(Get-Urls -Text $command.Body) + @($attachments | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })

    $commandRecord = [ordered]@{
        date = $Date
        timestamp = $timestampText
        source = $(if ([string]::IsNullOrWhiteSpace($SourcePath)) { "discord-command" } else { "discord-activity-command" })
        command = $command.Kind
        raw_command = $command.RawName
        inference = $command.Inference
        body = $command.Body
        channel_id = Get-PropertyText -Item $message -Name "channel_id"
        channel = $channelName
        author = Get-PropertyText -Item $message -Name "author"
        author_id = $authorId
        message_id = $messageId
        content = $content
        urls = @($urls | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
        attachments = $attachments
    }
    [void](Add-JsonLineIfMissing -Path $CommandOutPath -Record $commandRecord)

    switch ($command.Kind) {
        "todo" {
            $stateKey = "$messageId|todo"
            if ($stateKeys.Contains($stateKey)) { $counts.skipped += 1; break }
            if (Add-Todo -Path $TodoPath -Text $command.Body) {
                $counts.todo += 1
                [void]$stateKeys.Add($stateKey)
                $newStateRows.Add([pscustomobject]@{ StateKey = $stateKey; Command = "todo"; MessageId = $messageId; AppliedAt = (Get-Date).ToString("o") })
            }
        }
        "done" {
            $stateKey = "$messageId|done"
            if ($stateKeys.Contains($stateKey)) { $counts.skipped += 1; break }
            if (Complete-Todo -Path $TodoPath -Text $command.Body) {
                $counts.done += 1
                [void]$stateKeys.Add($stateKey)
                $newStateRows.Add([pscustomobject]@{ StateKey = $stateKey; Command = "done"; MessageId = $messageId; AppliedAt = (Get-Date).ToString("o") })
            }
        }
        "watch" {
            $watchPath = Join-Path $RepositoryRoot "records\inbox\watch\$Date.jsonl"
            $status = if ($command.RawName -in @("later", "want", "watchlater")) { "want_to_watch" } else { Get-WatchStatus -Text $command.Body -DefaultStatus "watched" }
            $record = [ordered]@{
                date = $Date
                timestamp = $timestampText
                source = $(if ([string]::IsNullOrWhiteSpace($SourcePath)) { "discord-command" } else { "discord-activity-command" })
                inference = $command.Inference
                channel_id = Get-PropertyText -Item $message -Name "channel_id"
                channel = $channelName
                author = Get-PropertyText -Item $message -Name "author"
                author_id = $authorId
                message_id = $messageId
                content = $command.Body
                status = $status
                urls = @($urls | Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
                attachments = $attachments
            }
            if (Add-JsonLineIfMissing -Path $watchPath -Record $record) { $counts.watch += 1 }
        }
        "mood" {
            $moodContent = Normalize-MoodText -Text $command.Body
            $moodPath = Join-Path $RepositoryRoot "records\inbox\mood\$Date.jsonl"
            $record = [ordered]@{
                date = $Date
                kind = "mood"
                timestamp = $timestampText
                source = $(if ([string]::IsNullOrWhiteSpace($SourcePath)) { "discord-command" } else { "discord-activity-command" })
                inference = $command.Inference
                channel_id = Get-PropertyText -Item $message -Name "channel_id"
                channel = $channelName
                author = Get-PropertyText -Item $message -Name "author"
                author_id = $authorId
                message_id = $messageId
                content = $moodContent
                attachments = $attachments
            }
            if (Add-JsonLineIfMissing -Path $moodPath -Record $record) { $counts.mood += 1 }
        }
        "research" {
            $stateKey = "$messageId|research"
            if ($stateKeys.Contains($stateKey)) { $counts.skipped += 1; break }
            if (Add-ResearchMemo -Path $ResearchInboxPath -Text $command.Body -DateValue $Date -Timestamp $timestampText -MessageId $messageId -ChannelName $channelName) {
                $counts.research += 1
                [void]$stateKeys.Add($stateKey)
                $newStateRows.Add([pscustomobject]@{ StateKey = $stateKey; Command = "research"; MessageId = $messageId; AppliedAt = (Get-Date).ToString("o") })
            }
        }
    }
}

Save-StateRows -Path $StatePath -Rows @($newStateRows.ToArray())

$summary = "Processed Discord Codex commands: todo=$($counts.todo), done=$($counts.done), watch=$($counts.watch), mood=$($counts.mood), research=$($counts.research), skipped=$($counts.skipped)."
Write-Host $summary

if ($PostSummary -and -not $DryRun -and [string]::IsNullOrWhiteSpace($SourcePath) -and -not [string]::IsNullOrWhiteSpace($ChannelId)) {
    [void](Invoke-DiscordJson -Method Post -Path "/channels/$ChannelId/messages" -Body ([ordered]@{ content = $summary }))
}
