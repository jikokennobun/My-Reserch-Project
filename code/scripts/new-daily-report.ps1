param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$RepositoryRoot,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianDailySubdir,
    [string]$ObsidianDailyTemplatePath,
    [switch]$UseCodex,
    [switch]$SyncObsidian,
    [switch]$PostDiscordDigest,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($ObsidianDailySubdir)) {
    $ObsidianDailySubdir = -join @([char]0x65E5, [char]0x5831)
}

function Read-JsonLines {
    param([string]$Path)

    if (-not (Test-Path $Path)) {
        return @()
    }

    $items = @()
    foreach ($line in Get-Content -LiteralPath $Path -Encoding UTF8) {
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }
        $items += ($line | ConvertFrom-Json)
    }
    return $items
}

function Read-JsonIfExists {
    param([string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path) -or -not (Test-Path $Path)) {
        return $null
    }

    $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    if ([string]::IsNullOrWhiteSpace($text)) {
        return $null
    }

    return ($text | ConvertFrom-Json)
}

function Read-TextIfExists {
    param(
        [string]$Path,
        [int]$MaxChars = 12000
    )

    if ([string]::IsNullOrWhiteSpace($Path) -or -not (Test-Path $Path)) {
        return ""
    }

    $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    if ($text.Length -gt $MaxChars) {
        return $text.Substring(0, $MaxChars) + "`n...(truncated)"
    }
    return $text
}

function Add-Block {
    param(
        [System.Collections.Generic.List[string]]$Lines,
        [string]$Title
    )

    $Lines.Add("")
    $Lines.Add("## $Title")
    $Lines.Add("")
}

function Get-ShortLine {
    param(
        [string]$Text,
        [int]$MaxChars = 180
    )

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return ""
    }

    $value = ($Text -replace "\s+", " ").Trim()
    if ($value.Length -gt $MaxChars) {
        return $value.Substring(0, $MaxChars) + "..."
    }
    return $value
}

function ConvertTo-JapaneseClause {
    param([string]$Text)

    $value = Get-ShortLine -Text $Text -MaxChars 140
    if ([string]::IsNullOrWhiteSpace($value)) {
        return ""
    }
    return ($value -replace "[。.!！?？]+$", "").Trim()
}

function Join-JapaneseClauses {
    param(
        [object[]]$Items,
        [int]$MaxItems = 3
    )

    $clauses = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in @($Items | Select-Object -First $MaxItems)) {
        $clause = ConvertTo-JapaneseClause -Text ([string]$item)
        if (-not [string]::IsNullOrWhiteSpace($clause)) {
            $clauses.Add($clause)
        }
    }

    if ($clauses.Count -eq 0) {
        return ""
    }
    if ($clauses.Count -eq 1) {
        return $clauses[0]
    }

    $values = @($clauses.ToArray())
    $head = @($values | Select-Object -First ($values.Count - 1))
    $tail = $values[$values.Count - 1]
    return (($head -join "、") + "、また、" + $tail)
}

function ConvertTo-JapaneseNominalClause {
    param([string]$Text)

    $clause = ConvertTo-JapaneseClause -Text $Text
    if ([string]::IsNullOrWhiteSpace($clause)) {
        return ""
    }
    if ($clause -match "(こと|もの)$") {
        return $clause
    }
    if ($clause -match "(した|いた|った|んだ|だ)$") {
        return "$clause" + "こと"
    }
    return $clause
}

function Join-JapaneseNominalClauses {
    param(
        [object[]]$Items,
        [int]$MaxItems = 3
    )

    $clauses = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in @($Items | Select-Object -First $MaxItems)) {
        $clause = ConvertTo-JapaneseNominalClause -Text ([string]$item)
        if (-not [string]::IsNullOrWhiteSpace($clause)) {
            $clauses.Add($clause)
        }
    }

    if ($clauses.Count -eq 0) {
        return ""
    }
    if ($clauses.Count -eq 1) {
        return $clauses[0]
    }

    $values = @($clauses.ToArray())
    $head = @($values | Select-Object -First ($values.Count - 1))
    $tail = $values[$values.Count - 1]
    return (($head -join "、") + "、また、" + $tail)
}

function ConvertTo-JstDateTime {
    param([object]$Value)

    if ($null -eq $Value) {
        return $null
    }

    $text = [string]$Value
    if ([string]::IsNullOrWhiteSpace($text)) {
        return $null
    }

    try {
        $parsed = [DateTimeOffset]::Parse($text, [Globalization.CultureInfo]::InvariantCulture)
        return $parsed.ToOffset([TimeSpan]::FromHours(9))
    } catch {
        return $null
    }
}

function Format-JstTimestamp {
    param(
        [object]$Value,
        [string]$ReportDate
    )

    $timestamp = ConvertTo-JstDateTime -Value $Value
    if ($null -eq $timestamp) {
        return "時刻不明"
    }

    if ($timestamp.ToString("yyyy-MM-dd") -eq $ReportDate) {
        return $timestamp.ToString("HH:mm")
    }

    return $timestamp.ToString("M/d HH:mm")
}

function Get-ActivityTimestamp {
    param([object]$Item)

    if ($null -eq $Item) {
        return $null
    }

    foreach ($name in @("timestamp", "created_at", "start", "date", "LastModified")) {
        if ($Item.PSObject.Properties.Name -contains $name) {
            $value = $Item.$name
            $parsed = ConvertTo-JstDateTime -Value $value
            if ($null -ne $parsed) {
                return $parsed
            }
        }
    }

    return $null
}

function Get-TimestampedText {
    param(
        [object]$Item,
        [string]$Text,
        [string]$ReportDate
    )

    $stamp = Format-JstTimestamp -Value (Get-ActivityTimestamp -Item $Item) -ReportDate $ReportDate
    if ([string]::IsNullOrWhiteSpace($Text)) {
        return "[$stamp] "
    }

    return "[$stamp] $Text"
}

function Get-PropertyValue {
    param(
        [object]$Item,
        [string]$Name
    )

    if ($null -eq $Item) { return $null }
    foreach ($property in $Item.PSObject.Properties) {
        if ($property.Name -eq $Name) { return $property.Value }
    }
    return $null
}

function Get-NestedPropertyValue {
    param(
        [object]$Item,
        [string]$ObjectName,
        [string[]]$Names
    )

    $nested = Get-PropertyValue -Item $Item -Name $ObjectName
    if ($null -eq $nested) { return $null }

    foreach ($name in $Names) {
        $value = Get-PropertyValue -Item $nested -Name $name
        if (-not [string]::IsNullOrWhiteSpace([string]$value)) {
            return $value
        }
    }
    return $null
}

function Format-VideoDisplay {
    param(
        [string]$Title,
        [string]$Channel,
        [string]$Url
    )

    $cleanTitle = Get-ShortLine -Text $Title -MaxChars 160
    $cleanChannel = Get-ShortLine -Text $Channel -MaxChars 80
    $cleanUrl = Get-ShortLine -Text $Url -MaxChars 220

    $label = if ([string]::IsNullOrWhiteSpace($cleanTitle)) { $cleanUrl } else { $cleanTitle }
    if ([string]::IsNullOrWhiteSpace($label)) { $label = "動画" }
    if (-not [string]::IsNullOrWhiteSpace($cleanChannel)) {
        $label = "$label（$cleanChannel）"
    }
    if (-not [string]::IsNullOrWhiteSpace($cleanUrl) -and -not [string]::IsNullOrWhiteSpace($cleanTitle)) {
        $label = "$label - $cleanUrl"
    }
    return $label
}

function Remove-UrlsFromText {
    param([string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) { return "" }
    return (($Text -replace "https?://\S+", "") -replace "\s+", " ").Trim()
}

function Get-YouTubeItemDisplay {
    param([object]$Item)

    $url = [string](Get-PropertyValue -Item $Item -Name "url")
    $title = [string](Get-PropertyValue -Item $Item -Name "title")
    if ([string]::IsNullOrWhiteSpace($title)) {
        $title = [string](Get-NestedPropertyValue -Item $Item -ObjectName "metadata" -Names @("title", "oembed_title"))
    }
    $channel = [string](Get-PropertyValue -Item $Item -Name "channel")
    if ([string]::IsNullOrWhiteSpace($channel)) {
        $channel = [string](Get-NestedPropertyValue -Item $Item -ObjectName "metadata" -Names @("channel", "uploader", "author_name"))
    }

    $display = Format-VideoDisplay -Title $title -Channel $channel -Url $url
    $notes = Get-ShortLine -Text ([string](Get-PropertyValue -Item $Item -Name "notes")) -MaxChars 120
    if (-not [string]::IsNullOrWhiteSpace($notes)) {
        $display = "$display / メモ: $notes"
    }
    return $display
}

function Get-GmailKindLabel {
    param([object]$Item)

    $kind = [string](Get-PropertyValue -Item $Item -Name "kind")
    switch ($kind) {
        "tutoring" { return "塾講師バイト" }
        "university" { return "大学" }
        default { return "メール" }
    }
}

function Get-WatchItemDisplay {
    param([object]$Item)

    $labels = New-Object 'System.Collections.Generic.List[string]'
    foreach ($video in @((Get-PropertyValue -Item $Item -Name "videos"))) {
        if ($null -eq $video) { continue }
        $labels.Add((Format-VideoDisplay `
            -Title ([string](Get-PropertyValue -Item $video -Name "title")) `
            -Channel ([string](Get-PropertyValue -Item $video -Name "channel")) `
            -Url ([string](Get-PropertyValue -Item $video -Name "url"))))
    }

    if ($labels.Count -eq 0) {
        foreach ($url in @((Get-PropertyValue -Item $Item -Name "urls"))) {
            if (-not [string]::IsNullOrWhiteSpace([string]$url)) {
                $labels.Add((Format-VideoDisplay -Title "" -Channel "" -Url ([string]$url)))
            }
        }
    }

    $content = Get-ShortLine -Text ([string](Get-PropertyValue -Item $Item -Name "content")) -MaxChars 180
    $note = Remove-UrlsFromText -Text $content
    $display = if ($labels.Count -gt 0) { @($labels) -join " / " } else { $content }
    if ([string]::IsNullOrWhiteSpace($display)) { $display = "視聴ログ" }
    $status = [string](Get-PropertyValue -Item $Item -Name "status")
    if (-not [string]::IsNullOrWhiteSpace($status)) {
        $display = "[$status] $display"
    }
    if (-not [string]::IsNullOrWhiteSpace($note) -and $display -notmatch [regex]::Escape($note)) {
        $display = "$display / メモ: $note"
    }
    return $display
}

function Get-CalendarItemDisplay {
    param([object]$Item)

    $title = Get-ShortLine -Text ([string](Get-PropertyValue -Item $Item -Name "title")) -MaxChars 160
    if ([string]::IsNullOrWhiteSpace($title)) { $title = "calendar event" }
    $source = [string](Get-PropertyValue -Item $Item -Name "source")
    $location = Get-ShortLine -Text ([string](Get-PropertyValue -Item $Item -Name "location")) -MaxChars 120
    $label = if ([string]::IsNullOrWhiteSpace($source)) { $title } else { "[$source] $title" }
    if (-not [string]::IsNullOrWhiteSpace($location)) {
        $label = "$label @ $location"
    }
    return $label
}

function Get-WeatherSummaryLine {
    param([object]$Weather)

    if ($null -eq $Weather) { return "" }
    if ($Weather.PSObject.Properties.Name -contains "available" -and -not [bool]$Weather.available) {
        return ""
    }
    if ($Weather.PSObject.Properties.Name -contains "summary") {
        return Get-ShortLine -Text ([string]$Weather.summary) -MaxChars 900
    }
    return ""
}

function Get-WeatherDetailLines {
    param([object]$Weather)

    $lines = New-Object 'System.Collections.Generic.List[string]'
    $summary = Get-WeatherSummaryLine -Weather $Weather
    if ([string]::IsNullOrWhiteSpace($summary)) {
        return @($lines)
    }

    $lines.Add("概要: $summary")
    if ($Weather.PSObject.Properties.Name -contains "segments" -and $null -ne $Weather.segments) {
        $flow = New-Object 'System.Collections.Generic.List[string]'
        foreach ($segment in @($Weather.segments)) {
            $weather = [string](Get-PropertyValue -Item $segment -Name "weather")
            if ([string]::IsNullOrWhiteSpace($weather)) { continue }
            if ($flow.Count -eq 0 -or $flow[$flow.Count - 1] -ne $weather) {
                $flow.Add($weather) | Out-Null
            }
        }
        if ($flow.Count -gt 0) {
            $labels = @($flow.ToArray())
            if ($labels.Count -gt 7) {
                $labels = @($labels | Select-Object -First 3) + @("...") + @($labels | Select-Object -Last 2)
            }
            $lines.Add("推移: " + ($labels -join "→"))
        }
    }
    if ($Weather.PSObject.Properties.Name -contains "source" -and -not [string]::IsNullOrWhiteSpace([string]$Weather.source)) {
        $lines.Add("出典: $($Weather.source)")
    }
    return @($lines)
}

function Get-DayPartLabel {
    param([object]$Item)

    $timestamp = Get-ActivityTimestamp -Item $Item
    if ($null -eq $timestamp) {
        return "時刻不明"
    }

    $hour = [int]$timestamp.Hour
    if ($hour -ge 4 -and $hour -lt 11) { return "朝" }
    if ($hour -ge 11 -and $hour -lt 16) { return "昼" }
    if ($hour -ge 16 -and $hour -lt 22) { return "夜" }
    return "深夜"
}

function Get-FoodLabel {
    param([object]$Item)

    $content = ""
    if ($null -ne $Item -and $Item.PSObject.Properties.Name -contains "content") {
        $content = [string]$Item.content
    }

    if ($content -match "朝|breakfast") { return "朝食" }
    if ($content -match "昼|lunch") { return "昼食" }
    if ($content -match "夜|夕|dinner") { return "夕食" }
    if ($content -match "間食|おやつ|snack") { return "間食" }

    switch (Get-DayPartLabel -Item $Item) {
        "朝" { return "朝食" }
        "昼" { return "昼食" }
        "夜" { return "夕食" }
        default { return "間食/深夜" }
    }
}

function Get-WakeValueFromItems {
    param(
        [object[]]$WakeItems,
        [string]$ReportDate
    )

    foreach ($item in ($WakeItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
        $content = ""
        if ($item.PSObject.Properties.Name -contains "content") {
            $content = [string]$item.content
        }

        $match = [regex]::Match($content, "([01]?\d|2[0-3])[:：時]([0-5]\d)?")
        if ($match.Success) {
            $hour = [int]$match.Groups[1].Value
            $minute = if ($match.Groups[2].Success -and -not [string]::IsNullOrWhiteSpace($match.Groups[2].Value)) { [int]$match.Groups[2].Value } else { 0 }
            return ("{0:00}:{1:00}（起床ログ）" -f $hour, $minute)
        }

        $timestamp = Get-ActivityTimestamp -Item $item
        if ($null -ne $timestamp) {
            return $timestamp.ToString("HH:mm") + "（起床ログ投稿時刻）"
        }
    }

    return ""
}

function Get-MoodValuesFromItems {
    param(
        [object[]]$MoodItems,
        [string]$ReportDate
    )

    $values = [ordered]@{ 朝 = $null; 昼 = $null; 夜 = $null }
    foreach ($item in ($MoodItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
        $content = ""
        if ($item.PSObject.Properties.Name -contains "content") {
            $content = Get-ShortLine -Text $item.content -MaxChars 160
        }
        if ([string]::IsNullOrWhiteSpace($content)) {
            continue
        }

        $label = $null
        if ($content -match "^\s*(朝|昼|夜)\s*[:：]?\s*(.+)$") {
            $label = $Matches[1]
            $content = $Matches[2].Trim()
        } else {
            $part = Get-DayPartLabel -Item $item
            if ($part -eq "朝" -or $part -eq "昼") {
                $label = $part
            } else {
                $label = "夜"
            }
        }

        if (-not [string]::IsNullOrWhiteSpace($label)) {
            $values[$label] = Get-TimestampedText -Item $item -ReportDate $ReportDate -Text $content
        }
    }

    return $values
}

function Get-ExistingLineValue {
    param(
        [string]$Text,
        [string]$Label
    )

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return ""
    }

    $escaped = [regex]::Escape($Label)
    $match = [regex]::Match($Text, "(?m)^-\s*$escaped\s*:\s*(.+?)\s*$")
    if (-not $match.Success) {
        return ""
    }

    return $match.Groups[1].Value.Trim()
}

function Set-TemplateLineValueIfBlank {
    param(
        [string]$Text,
        [string]$Label,
        [string]$Value
    )

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return $Text
    }

    $lines = New-Object 'System.Collections.Generic.List[string]'
    $found = $false

    foreach ($line in [regex]::Split($Text, "\r?\n")) {
        $match = [regex]::Match($line, "^\s*-\s*([^:：]+)\s*[:：]\s*(.*)$")
        if ($match.Success -and $match.Groups[1].Value.Trim() -eq $Label) {
            $found = $true
            $current = $match.Groups[2].Value.Trim()
            if ([string]::IsNullOrWhiteSpace($current)) {
                $lines.Add("- ${Label}: $Value")
            } else {
                $lines.Add($line)
            }
        } else {
            $lines.Add($line)
        }
    }

    if ($found) {
        return ($lines -join "`n")
    }

    return $Text.TrimEnd() + "`n- ${Label}: $Value`n"
}

function Get-EarliestActivityTimestamp {
    param(
        [object[]]$Items,
        [string]$DiscordSelfUserId
    )

    $timestamps = New-Object 'System.Collections.Generic.List[DateTimeOffset]'
    foreach ($item in $Items) {
        if ($null -eq $item) {
            continue
        }

        if ($item.PSObject.Properties.Name -contains "author") {
            $author = [string]$item.author
            if ($author -match "(?i)bot") {
                continue
            }
        }

        if (-not [string]::IsNullOrWhiteSpace($DiscordSelfUserId) -and $item.PSObject.Properties.Name -contains "author_id") {
            if ([string]$item.author_id -ne $DiscordSelfUserId) {
                continue
            }
        }

        $timestamp = Get-ActivityTimestamp -Item $item
        if ($null -ne $timestamp) {
            $timestamps.Add($timestamp)
        }
    }

    if ($timestamps.Count -eq 0) {
        return $null
    }

    return ($timestamps | Sort-Object | Select-Object -First 1)
}

function ConvertTo-BulletLines {
    param(
        [string[]]$Items,
        [string]$Fallback
    )

    $lines = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in $Items) {
        if ([string]::IsNullOrWhiteSpace($item)) {
            continue
        }
        $lines.Add("- $item")
    }

    if ($lines.Count -eq 0 -and -not [string]::IsNullOrWhiteSpace($Fallback)) {
        $lines.Add("- $Fallback")
    }

    return @($lines)
}

function Set-MarkdownSection {
    param(
        [string]$Text,
        [string]$Heading,
        [string[]]$ContentLines
    )

    $content = (($ContentLines | Where-Object { $null -ne $_ }) -join "`n").TrimEnd()
    if ([string]::IsNullOrWhiteSpace($content)) {
        $content = "- "
    }

    $escaped = [regex]::Escape($Heading)
    $pattern = "(?ms)(^#\s*$escaped\s*\r?\n)(.*?)(?=^#|\z)"
    $evaluator = [System.Text.RegularExpressions.MatchEvaluator]{
        param($match)
        return $match.Groups[1].Value + $content + "`n`n"
    }

    if ([regex]::IsMatch($Text, $pattern)) {
        return [regex]::Replace($Text, $pattern, $evaluator, 1)
    }

    return $Text.TrimEnd() + "`n`n#$Heading`n$content`n"
}

function Upsert-SectionBeforeHeading {
    param(
        [string]$Text,
        [string]$Heading,
        [string]$BeforeHeading,
        [string[]]$ContentLines
    )

    if ([regex]::IsMatch($Text, "(?m)^#\s*$([regex]::Escape($Heading))\s*$")) {
        return (Set-MarkdownSection -Text $Text -Heading $Heading -ContentLines $ContentLines)
    }

    $content = (($ContentLines | Where-Object { $null -ne $_ }) -join "`n").TrimEnd()
    if ([string]::IsNullOrWhiteSpace($content)) {
        $content = "- "
    }
    $block = "#$Heading`n$content`n`n"
    $beforePattern = "(?m)^#\s*$([regex]::Escape($BeforeHeading))\s*$"
    if ([regex]::IsMatch($Text, $beforePattern)) {
        return [regex]::Replace($Text, $beforePattern, { param($match) $block + $match.Value }, 1)
    }

    return $Text.TrimEnd() + "`n`n$block"
}

function Set-TemplateLineValue {
    param(
        [string]$Text,
        [string]$Label,
        [string]$Value
    )

    $escaped = [regex]::Escape($Label)
    $pattern = "(?m)^-\s*$escaped\s*:.*$"
    $replacement = "- ${Label}: $Value"
    if ([regex]::IsMatch($Text, $pattern)) {
        return [regex]::Replace($Text, $pattern, $replacement, 1)
    }
    return $Text.TrimEnd() + "`n$replacement`n"
}

function Set-AnyHeadingSection {
    param(
        [string]$Text,
        [string]$Heading,
        [string[]]$ContentLines
    )

    $content = (($ContentLines | Where-Object { $null -ne $_ }) -join "`n").TrimEnd()
    if ([string]::IsNullOrWhiteSpace($content)) {
        $content = "- "
    }

    $escaped = [regex]::Escape($Heading)
    $pattern = "(?ms)(^#{1,6}\s*$escaped\s*\r?\n)(.*?)(?=^#{1,6}\s+\S|\z)"
    $evaluator = [System.Text.RegularExpressions.MatchEvaluator]{
        param($match)
        return $match.Groups[1].Value + $content + "`n`n"
    }

    if ([regex]::IsMatch($Text, $pattern)) {
        return [regex]::Replace($Text, $pattern, $evaluator, 1)
    }

    return $Text.TrimEnd() + "`n`n###### $Heading`n$content`n"
}

function Test-DailyReportChannelName {
    param([string]$Channel)

    if ([string]::IsNullOrWhiteSpace($Channel)) { return $false }
    return ($Channel -match "^20\d{2}(-\d{1,2})?$")
}

function Test-ActivityLogChannelName {
    param([string]$Channel)

    return ($Channel -eq "活動ログ")
}

function Test-DiscordHumanActivity {
    param(
        [object]$Item,
        [switch]$AllowDailyReportChannel
    )

    if ($null -eq $Item) { return $false }
    if ($Item.PSObject.Properties.Name -contains "author_is_bot" -and [bool]$Item.author_is_bot) { return $false }

    $author = if ($Item.PSObject.Properties.Name -contains "author") { [string]$Item.author } else { "" }
    if ($author -match "(?i)bot|webhook|spidey|codex daily report|mail-timeline|大学メール通知|塾講師メール通知|自己満足文") {
        return $false
    }

    $content = if ($Item.PSObject.Properties.Name -contains "content") { [string]$Item.content } else { "" }
    if ($content -match "Codex command channel is ready|AI chat channel is ready|daily-report bridge is connected|Research channel bridge is connected") {
        return $false
    }

    $channel = if ($Item.PSObject.Properties.Name -contains "channel") { [string]$Item.channel } else { "" }
    if (-not $AllowDailyReportChannel -and (Test-DailyReportChannelName -Channel $channel)) {
        return $false
    }

    return $true
}

function Select-UniqueActivityItems {
    param([object[]]$Items)

    $seen = New-Object 'System.Collections.Generic.HashSet[string]'
    $unique = New-Object 'System.Collections.Generic.List[object]'
    foreach ($item in @($Items)) {
        if ($null -eq $item) { continue }
        $messageId = ""
        if ($item.PSObject.Properties.Name -contains "message_id") {
            $messageId = [string]$item.message_id
        }
        if ([string]::IsNullOrWhiteSpace($messageId) -and $item.PSObject.Properties.Name -contains "id") {
            $messageId = [string]$item.id
        }
        if ([string]::IsNullOrWhiteSpace($messageId)) {
            $timestamp = if ($item.PSObject.Properties.Name -contains "timestamp") { [string]$item.timestamp } else { "" }
            $channel = if ($item.PSObject.Properties.Name -contains "channel") { [string]$item.channel } else { "" }
            $content = if ($item.PSObject.Properties.Name -contains "content") { [string]$item.content } else { "" }
            $messageId = "$timestamp|$channel|$content"
        }
        if ($seen.Add($messageId)) {
            $unique.Add($item)
        }
    }
    return @($unique.ToArray())
}

function Add-CountPart {
    param(
        [System.Collections.Generic.List[string]]$Parts,
        [string]$Label,
        [int]$Count
    )

    if ($Count -gt 0) {
        $Parts.Add("$Label ${Count}件")
    }
}

function Get-CountSummaryText {
    param([System.Collections.Generic.List[string]]$Parts)

    if ($null -eq $Parts -or $Parts.Count -eq 0) {
        return "自動収集された記録は少なめ。必要なら手動で追記。"
    }
    return ($Parts.ToArray() -join " / ")
}

function Get-RelativePathCompat {
    param(
        [string]$BasePath,
        [string]$FullPath
    )

    $base = $BasePath.TrimEnd("\", "/")
    if ($FullPath.StartsWith($base, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $FullPath.Substring($base.Length).TrimStart("\", "/")
    }
    return $FullPath
}

function Test-ExcludedObsidianMemoPath {
    param(
        [string]$RelativePath,
        [string]$DailySubdir
    )

    if ([string]::IsNullOrWhiteSpace($RelativePath)) { return $true }
    $normalized = $RelativePath -replace "/", "\"
    $parts = @($normalized -split "\\")
    if ($parts.Count -gt 0 -and $parts[0] -in @(".obsidian", ".trash", "_attachments", "attachments", "assets")) {
        return $true
    }
    if (-not [string]::IsNullOrWhiteSpace($DailySubdir) -and ($normalized -eq $DailySubdir -or $normalized.StartsWith("$DailySubdir\", [System.StringComparison]::OrdinalIgnoreCase))) {
        return $true
    }
    $fileName = [IO.Path]::GetFileName($normalized)
    if ($fileName -match "(?i)template|テンプレ" -or $fileName -eq "nippo-template.md") {
        return $true
    }
    return $false
}

function Get-ObsidianMemoChanges {
    param(
        [string]$VaultRoot,
        [string]$ReportDate,
        [string]$DailySubdir
    )

    if ([string]::IsNullOrWhiteSpace($VaultRoot) -or -not (Test-Path -LiteralPath $VaultRoot)) {
        return @()
    }

    $target = [datetime]::ParseExact($ReportDate, "yyyy-MM-dd", [Globalization.CultureInfo]::InvariantCulture)
    $items = New-Object 'System.Collections.Generic.List[object]'

    $files = Get-ChildItem -LiteralPath $VaultRoot -Recurse -File -Filter "*.md" -ErrorAction SilentlyContinue
    foreach ($file in @($files)) {
        if ($file.LastWriteTime.Date -ne $target.Date) { continue }
        $relative = Get-RelativePathCompat -BasePath $VaultRoot -FullPath $file.FullName
        if (Test-ExcludedObsidianMemoPath -RelativePath $relative -DailySubdir $DailySubdir) { continue }

        $root = ($relative -split "[\\/]") | Select-Object -First 1
        $items.Add([pscustomobject]@{
            Title = [IO.Path]::GetFileNameWithoutExtension($file.Name)
            Root = [string]$root
            RelativePath = $relative
            LastModified = $file.LastWriteTime.ToString("s")
            SizeBytes = $file.Length
        })
    }

    return @($items.ToArray() | Sort-Object -Property @{ Expression = "LastModified"; Descending = $true }, RelativePath)
}

function Get-ObsidianMemoChangeDisplay {
    param(
        [object]$Item,
        [string]$ReportDate
    )

    $title = Get-ShortLine -Text ([string]$Item.Title) -MaxChars 120
    $root = Get-ShortLine -Text ([string]$Item.Root) -MaxChars 80
    $relative = Get-ShortLine -Text (([string]$Item.RelativePath) -replace "\\", "/") -MaxChars 180
    $label = if ([string]::IsNullOrWhiteSpace($title)) { $relative } else { $title }
    if (-not [string]::IsNullOrWhiteSpace($root)) {
        $label = "$label（$root）"
    }
    if (-not [string]::IsNullOrWhiteSpace($relative)) {
        $label = "$label :: $relative"
    }
    return (Get-TimestampedText -Item $Item -ReportDate $ReportDate -Text $label)
}

$dailyDir = Join-Path $RepositoryRoot "records\daily"
$packetDir = Join-Path $RepositoryRoot "records\inbox\daily-packets"
$discordPath = Join-Path $RepositoryRoot "records\inbox\discord\$Date.jsonl"
$recentDiscordPath = Join-Path $RepositoryRoot "records\inbox\discord\recent-$Date-$Date.jsonl"
$eventDiscordPath = Join-Path $RepositoryRoot "records\inbox\discord\events-$Date.jsonl"
$externalDiscordPath = Join-Path $RepositoryRoot "records\inbox\discord-external\$Date.jsonl"
$foodPath = Join-Path $RepositoryRoot "records\inbox\discord-food\$Date.jsonl"
$twitterPath = Join-Path $RepositoryRoot "records\inbox\twitter\$Date.jsonl"
$aiPath = Join-Path $RepositoryRoot "records\inbox\ai\$Date.jsonl"
$activityPath = Join-Path $RepositoryRoot "records\inbox\activity\$Date.jsonl"
$watchPath = Join-Path $RepositoryRoot "records\inbox\watch\$Date.jsonl"
$moodPath = Join-Path $RepositoryRoot "records\inbox\mood\$Date.jsonl"
$wakePath = Join-Path $RepositoryRoot "records\inbox\wake\$Date.jsonl"
$reflectionPath = Join-Path $RepositoryRoot "records\inbox\reflection\$Date.jsonl"
$youtubePath = Join-Path $RepositoryRoot "records\inbox\youtube\$Date.jsonl"
$gmailPath = Join-Path $RepositoryRoot "records\inbox\gmail\$Date.jsonl"
$chatgptPath = Join-Path $RepositoryRoot "records\inbox\chatgpt\$Date.jsonl"
$calendarPath = Join-Path $RepositoryRoot "records\inbox\calendar\$Date.jsonl"
$weatherPath = Join-Path $RepositoryRoot "records\inbox\weather\$Date.json"
$todoPath = Join-Path $RepositoryRoot "records\tasks\todo.md"
$researchLogPath = Join-Path $RepositoryRoot "records\logs\research-log.md"
$obsidianCsvPath = Join-Path $RepositoryRoot "research\references\obsidian-research-index.csv"
$reportPath = Join-Path $dailyDir "$Date.md"
$packetPath = Join-Path $packetDir "$Date.md"

$discordItemsRaw = @(Read-JsonLines -Path $discordPath)
$recentDiscordItemsRaw = @(Read-JsonLines -Path $recentDiscordPath)
$eventDiscordItemsRaw = @(Read-JsonLines -Path $eventDiscordPath)
$externalDiscordItemsRaw = @(Read-JsonLines -Path $externalDiscordPath)
$discordItems = @($discordItemsRaw | Where-Object { Test-DiscordHumanActivity -Item $_ -AllowDailyReportChannel })
$recentDiscordItems = @(Select-UniqueActivityItems -Items (@($recentDiscordItemsRaw) + @($eventDiscordItemsRaw)) | Where-Object { Test-DiscordHumanActivity -Item $_ })
$externalDiscordItems = @($externalDiscordItemsRaw | Where-Object { Test-DiscordHumanActivity -Item $_ -AllowDailyReportChannel })
$foodItems = @(Read-JsonLines -Path $foodPath)
$twitterItems = @(Read-JsonLines -Path $twitterPath)
$aiItems = @(Read-JsonLines -Path $aiPath)
$activityItems = @(Read-JsonLines -Path $activityPath)
$watchItems = @(Read-JsonLines -Path $watchPath)
$moodItems = @(Read-JsonLines -Path $moodPath)
$wakeItems = @(Read-JsonLines -Path $wakePath)
$reflectionItems = @(Read-JsonLines -Path $reflectionPath)
$youtubeItems = @(Read-JsonLines -Path $youtubePath)
$gmailItems = @(Read-JsonLines -Path $gmailPath)
$chatgptItems = @(Read-JsonLines -Path $chatgptPath)
$calendarItems = @(Read-JsonLines -Path $calendarPath)
$weatherItem = Read-JsonIfExists -Path $weatherPath
$weatherSummary = Get-WeatherSummaryLine -Weather $weatherItem
$weatherDetailLines = Get-WeatherDetailLines -Weather $weatherItem
$todoText = Read-TextIfExists -Path $todoPath -MaxChars 8000
$researchLogTail = if (Test-Path $researchLogPath) { (Get-Content -LiteralPath $researchLogPath -Tail 80 -Encoding UTF8) -join "`n" } else { "" }
if ([string]::IsNullOrWhiteSpace($ObsidianDailyTemplatePath)) {
    $ObsidianDailyTemplatePath = Join-Path (Join-Path $ObsidianVaultRoot $ObsidianDailySubdir) "nippo-template.md"
}
$templateText = Read-TextIfExists -Path $ObsidianDailyTemplatePath -MaxChars 30000
$obsidianDailyDir = Join-Path $ObsidianVaultRoot $ObsidianDailySubdir
$obsidianReportPath = Join-Path $obsidianDailyDir "$Date.md"
$existingDailyText = Read-TextIfExists -Path $obsidianReportPath -MaxChars 50000
if ([string]::IsNullOrWhiteSpace($existingDailyText)) {
    $existingDailyText = Read-TextIfExists -Path $reportPath -MaxChars 50000
}
$discordSelfUserId = [Environment]::GetEnvironmentVariable("DISCORD_SELF_USER_ID", "User")
if ([string]::IsNullOrWhiteSpace($discordSelfUserId)) {
    $discordSelfUserId = "1094849500033593415"
}

$obsidianChanged = @()
if (Test-Path $obsidianCsvPath) {
    $obsidianChanged = @(Import-Csv -LiteralPath $obsidianCsvPath | Where-Object { $_.LastModified -like "$Date*" } | Sort-Object LastModified -Descending)
}
$obsidianMemoChanged = @(Get-ObsidianMemoChanges -VaultRoot $ObsidianVaultRoot -ReportDate $Date -DailySubdir $ObsidianDailySubdir)

$gitStatus = ""
$git = Get-Command "git" -ErrorAction SilentlyContinue
if ($null -ne $git) {
    $gitStatus = (& $git.Source -C $RepositoryRoot status --short) -join "`n"
}

$packet = New-Object 'System.Collections.Generic.List[string]'
$packet.Add("# Daily Source Packet - $Date")
$packet.Add("")
$packet.Add("This local packet may contain raw source material. Do not commit this file.")

Add-Block -Lines $packet -Title "Discord"
if ($discordItems.Count -eq 0) {
    $packet.Add("No Discord capture found at `$discordPath`.")
} else {
    foreach ($item in $discordItems) {
        $content = Get-ShortLine -Text $item.content -MaxChars 500
        $attachments = @($item.attachments) -join ", "
        $packet.Add("- $($item.timestamp) [$($item.author)] $content")
        if (-not [string]::IsNullOrWhiteSpace($attachments)) {
            $packet.Add("  Attachments: $attachments")
        }
    }
}

Add-Block -Lines $packet -Title "Discord Recent Activity"
if ($recentDiscordItems.Count -eq 0) {
    $packet.Add("No recent Discord activity capture found at `$recentDiscordPath`.")
} else {
    foreach ($item in $recentDiscordItems) {
        $content = Get-ShortLine -Text $item.content -MaxChars 500
        $attachments = @($item.attachments) -join ", "
        $packet.Add("- $($item.timestamp) [$($item.channel) / $($item.author)] $content")
        if (-not [string]::IsNullOrWhiteSpace($attachments)) {
            $packet.Add("  Attachments: $attachments")
        }
    }
}

Add-Block -Lines $packet -Title "External Discord Activity"
if ($externalDiscordItems.Count -eq 0) {
    $packet.Add("No external Discord activity capture found at `$externalDiscordPath`.")
} else {
    foreach ($item in $externalDiscordItems) {
        $content = Get-ShortLine -Text $item.content -MaxChars 500
        $attachments = @($item.attachments) -join ", "
        $packet.Add("- $($item.timestamp) [$($item.guild) / $($item.channel) / $($item.author)] $content")
        if (-not [string]::IsNullOrWhiteSpace($attachments)) {
            $packet.Add("  Attachments: $attachments")
        }
    }
}

Add-Block -Lines $packet -Title "YouTube"
if ($youtubeItems.Count -eq 0) {
    $packet.Add("No YouTube activity found at `$youtubePath`.")
} else {
    foreach ($item in $youtubeItems) {
        $packet.Add("- $(Get-YouTubeItemDisplay -Item $item)")
        $packet.Add("  URL: $($item.url)")
        if (-not [string]::IsNullOrWhiteSpace($item.channel)) {
            $packet.Add("  Channel: $($item.channel)")
        }
        if (-not [string]::IsNullOrWhiteSpace($item.notes)) {
            $packet.Add("  Notes: $(Get-ShortLine -Text $item.notes -MaxChars 800)")
        }
        if ($null -ne $item.metadata) {
            $packet.Add("  Uploader: $($item.metadata.uploader)")
            $packet.Add("  Duration: $($item.metadata.duration)")
        }
        $transcriptText = Read-TextIfExists -Path $item.transcript_path -MaxChars 8000
        if (-not [string]::IsNullOrWhiteSpace($transcriptText)) {
            $packet.Add("")
            $packet.Add("  Transcript excerpt:")
            $packet.Add("")
            $packet.Add('  ```text')
            foreach ($line in ($transcriptText -split "`n")) {
                $packet.Add("  $line")
            }
            $packet.Add('  ```')
        }
    }
}

Add-Block -Lines $packet -Title "Twitter/X"
if ($twitterItems.Count -eq 0) {
    $packet.Add("No Twitter/X activity found at `$twitterPath`.")
} else {
    foreach ($item in $twitterItems) {
        $text = Get-ShortLine -Text $item.text -MaxChars 500
        $packet.Add("- $($item.timestamp) [@$($item.username) / $($item.kind)] $text")
        if (-not [string]::IsNullOrWhiteSpace($item.url)) {
            $packet.Add("  URL: $($item.url)")
        }
    }
}

Add-Block -Lines $packet -Title "Generated AI"
if ($aiItems.Count -eq 0) {
    $packet.Add("No generated-AI activity found at `$aiPath`.")
} else {
    foreach ($item in $aiItems) {
        $summary = Get-ShortLine -Text $item.summary -MaxChars 500
        $packet.Add("- $($item.timestamp) [$($item.tool)] $summary")
        if (-not [string]::IsNullOrWhiteSpace($item.details)) {
            $packet.Add("  Details: $(Get-ShortLine -Text $item.details -MaxChars 800)")
        }
        if (-not [string]::IsNullOrWhiteSpace($item.url)) {
            $packet.Add("  URL: $($item.url)")
        }
    }
}

Add-Block -Lines $packet -Title "Activity Log"
if ($activityItems.Count -eq 0) {
    $packet.Add("No activity-log capture found at `$activityPath`.")
} else {
    foreach ($item in ($activityItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
        $content = Get-ShortLine -Text $item.content -MaxChars 500
        $attachments = @($item.attachments) -join ", "
        $packet.Add("- $($item.timestamp) [$($item.author)] $content")
        if (-not [string]::IsNullOrWhiteSpace($attachments)) {
            $packet.Add("  Attachments: $attachments")
        }
    }
}

Add-Block -Lines $packet -Title "ChatGPT Pro Ideas"
if ($chatgptItems.Count -eq 0) {
    $packet.Add("No ChatGPT Pro idea capture found at `$chatgptPath`.")
} else {
    foreach ($item in ($chatgptItems | Select-Object -First 80)) {
        $text = Get-ShortLine -Text $item.text -MaxChars 700
        $packet.Add("- $($item.timestamp) [$($item.title) / $($item.role)] $text")
        if (-not [string]::IsNullOrWhiteSpace($item.url)) {
            $packet.Add("  URL: $($item.url)")
        }
    }
}

Add-Block -Lines $packet -Title "Watch Log"
if ($watchItems.Count -eq 0) {
    $packet.Add("No watch-log activity found at `$watchPath`.")
} else {
    foreach ($item in $watchItems) {
        $content = Get-WatchItemDisplay -Item $item
        $urls = @($item.urls) -join ", "
        $packet.Add("- $($item.timestamp) [$($item.author)] $content")
        if (-not [string]::IsNullOrWhiteSpace($urls)) {
            $packet.Add("  URL: $urls")
        }
    }
}

Add-Block -Lines $packet -Title "Mood Log"
if ($moodItems.Count -eq 0) {
    $packet.Add("No mood-log activity found at `$moodPath`.")
} else {
    foreach ($item in $moodItems) {
        $packet.Add("- $($item.timestamp) [$($item.author)] $(Get-ShortLine -Text $item.content -MaxChars 500)")
    }
}

Add-Block -Lines $packet -Title "Wake Log"
if ($wakeItems.Count -eq 0) {
    $packet.Add("No wake-log activity found at `$wakePath`.")
} else {
    foreach ($item in $wakeItems) {
        $packet.Add("- $($item.timestamp) [$($item.author)] $(Get-ShortLine -Text $item.content -MaxChars 500)")
    }
}

Add-Block -Lines $packet -Title "Reflection"
if ($reflectionItems.Count -eq 0) {
    $packet.Add("No reflection activity found at `$reflectionPath`.")
} else {
    foreach ($item in $reflectionItems) {
        $packet.Add("- $($item.timestamp) [$($item.author)] $(Get-ShortLine -Text $item.content -MaxChars 800)")
    }
}

Add-Block -Lines $packet -Title "Food"
if ($foodItems.Count -eq 0) {
    $packet.Add("No food images found at `$foodPath`.")
} else {
    foreach ($item in $foodItems) {
        $caption = Get-ShortLine -Text $item.content -MaxChars 300
        $packet.Add("- $($item.timestamp) [$($item.author)] $caption")
        $packet.Add("  Image: $($item.obsidian_relative_path)")
    }
}

Add-Block -Lines $packet -Title "Weather"
if ([string]::IsNullOrWhiteSpace($weatherSummary)) {
    $packet.Add("No weather capture found at `$weatherPath`.")
} else {
    $packet.Add("- $weatherSummary")
    foreach ($line in $weatherDetailLines) {
        $packet.Add("  $line")
    }
}

Add-Block -Lines $packet -Title "Calendar"
if ($calendarItems.Count -eq 0) {
    $packet.Add("No calendar capture found at `$calendarPath`.")
} else {
    foreach ($item in ($calendarItems | Select-Object -First 80)) {
        $packet.Add("- $($item.start) $(Get-CalendarItemDisplay -Item $item)")
    }
}

Add-Block -Lines $packet -Title "Gmail Tasks"
if ($gmailItems.Count -eq 0) {
    $packet.Add("No Gmail task capture found at `$gmailPath`.")
} else {
    foreach ($item in ($gmailItems | Select-Object -First 80)) {
        $subject = Get-ShortLine -Text $item.subject -MaxChars 180
        $hints = @($item.task_hints) -join " / "
        $packet.Add("- $($item.received_at) [$(Get-GmailKindLabel -Item $item) / $($item.from)] $subject")
        if (-not [string]::IsNullOrWhiteSpace($hints)) {
            $packet.Add("  Task hints: $hints")
        }
    }
}

Add-Block -Lines $packet -Title "Obsidian Research Notes Changed Today"
if ($obsidianChanged.Count -eq 0) {
    $packet.Add("No research-index entries changed on $Date.")
} else {
    foreach ($item in ($obsidianChanged | Select-Object -First 80)) {
        $packet.Add("- $($item.LastModified) [$($item.Category)] $($item.Title) :: $($item.RelativePath)")
    }
}

Add-Block -Lines $packet -Title "Obsidian Memo Changes"
if ($obsidianMemoChanged.Count -eq 0) {
    $packet.Add("No Obsidian memo files changed on $Date.")
} else {
    foreach ($item in ($obsidianMemoChanged | Select-Object -First 120)) {
        $packet.Add("- $($item.LastModified) [$($item.Root)] $($item.Title) :: $($item.RelativePath)")
    }
}

Add-Block -Lines $packet -Title "Todo"
if ([string]::IsNullOrWhiteSpace($todoText)) {
    $packet.Add("No todo file found.")
} else {
    $packet.Add($todoText)
}

Add-Block -Lines $packet -Title "Research Log Tail"
if ([string]::IsNullOrWhiteSpace($researchLogTail)) {
    $packet.Add("No research log tail found.")
} else {
    $packet.Add($researchLogTail)
}

Add-Block -Lines $packet -Title "Git Status"
if ([string]::IsNullOrWhiteSpace($gitStatus)) {
    $packet.Add("No Git status output.")
} else {
    $packet.Add('```text')
    $packet.Add($gitStatus)
    $packet.Add('```')
}

Add-Block -Lines $packet -Title "Obsidian Daily Template"
if ([string]::IsNullOrWhiteSpace($templateText)) {
    $packet.Add("No template found at `$ObsidianDailyTemplatePath`.")
} else {
    $packet.Add($templateText)
}

$packetText = $packet -join "`n"

if ($DryRun) {
    Write-Host $packetText
    exit 0
}

if (-not (Test-Path $dailyDir)) {
    New-Item -ItemType Directory -Path $dailyDir | Out-Null
}
if (-not (Test-Path $packetDir)) {
    New-Item -ItemType Directory -Path $packetDir | Out-Null
}

$packetText | Set-Content -LiteralPath $packetPath -Encoding UTF8

if ($UseCodex) {
    $codex = Get-Command "codex" -ErrorAction SilentlyContinue
    if ($null -eq $codex) {
        throw "codex CLI was not found. Run without -UseCodex to create a deterministic draft."
    }

    $instruction = @"
Generate a Japanese daily report from the source packet.

Output Markdown only. Use this structure:
# Daily Report - $Date

Then use the Obsidian Daily Template from the source packet as the body shape.
Preserve the user's existing template style and headings where possible.
Fill or add these sections in Japanese:
- #食事
- #天気の移り変わり
- #Obsidianメモ変更履歴
- #やった
- #思った
- #読んだ/見た/知った
- #SNSでの活動
- #生成AIでの活動
- #精神状態 with 朝, 昼, 夜
- 今日の感想

After the detailed Obsidian report, add:
## Discord Digest

Rules:
- Discord Digest must be a short plain-language summary for Discord, under 1800 characters.
- Write Discord Digest in Japanese prose, separated by bold section labels such as `**起床と天気**` and `**今日の活動**`.
- Do not use bullet lists, numbered lists, or Markdown heading lines inside Discord Digest.
- Do not mention zero-count categories in Discord Digest.
- Keep raw Discord conversations private in Discord Digest; summarize them instead of copying long quotes.
- Treat External Discord Activity as activity outside the primary server; summarize it separately from the daily-report channel.
- Include Twitter/X and generated-AI activities when provided.
- The detailed Obsidian report can include compact private notes, counts, and local image links.
- Include Watch Log entries as anime/video/watched-media items.
- Summarize YouTube videos only from provided notes, metadata, or transcripts.
- Include food images as Markdown image links when food image paths are provided.
- Fill the template weather line from Weather when available, and include a compact weather-transition section.
- Include Obsidian Memo Changes as a compact change-history section, excluding the daily report itself.
- If 起床 is blank, fill it from the earliest reliable activity timestamp and mark it as an automatic estimate. If 起床 already has a value, preserve it.
- Every food item, SNS activity, anime/video item, and generated-AI item must include a JST timestamp.
- Place SNS and generated-AI sections after #読んだ/見た/知った and before #精神状態.
- If mood is not available, keep 朝/昼/夜 as fill-in prompts rather than inventing emotions.
- Separate mathematical claims from todo management.
- Mark uncertain mathematical claims as conjectures or questions.
- Do not invent bibliographic facts.
"@

    $packetText | & $codex.Source exec --sandbox workspace-write --output-last-message $reportPath $instruction | Out-Null
} else {
    $snsSource = if ($recentDiscordItems.Count -gt 0) { $recentDiscordItems } else { $discordItems }

    $snsItems = New-Object 'System.Collections.Generic.List[string]'
    if ($snsSource.Count -gt 0) {
        foreach ($item in ($snsSource | Sort-Object { Get-ActivityTimestamp -Item $_ } | Select-Object -First 20)) {
            if ($item.PSObject.Properties.Name -contains "author_id" -and -not [string]::IsNullOrWhiteSpace($discordSelfUserId) -and [string]$item.author_id -ne $discordSelfUserId) {
                continue
            }
            if ($item.PSObject.Properties.Name -contains "author" -and [string]$item.author -match "(?i)bot") {
                continue
            }
            if ($item.PSObject.Properties.Name -contains "channel" -and (Test-ActivityLogChannelName -Channel ([string]$item.channel))) {
                continue
            }
            $content = Get-ShortLine -Text $item.content -MaxChars 120
            if (-not [string]::IsNullOrWhiteSpace($content)) {
                $prefix = if ($item.PSObject.Properties.Name -contains "channel" -and -not [string]::IsNullOrWhiteSpace([string]$item.channel)) { "#$($item.channel)" } else { "Discord" }
                $snsItems.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text ("Discord {0} / {1}: {2}" -f $prefix, $item.author, $content)))
            }
        }
    }
    if ($externalDiscordItems.Count -gt 0) {
        foreach ($item in ($externalDiscordItems | Sort-Object { Get-ActivityTimestamp -Item $_ } | Select-Object -First 20)) {
            if ($item.PSObject.Properties.Name -contains "author_id" -and -not [string]::IsNullOrWhiteSpace($discordSelfUserId) -and [string]$item.author_id -ne $discordSelfUserId) {
                continue
            }
            if ($item.PSObject.Properties.Name -contains "author" -and [string]$item.author -match "(?i)bot") {
                continue
            }
            $content = Get-ShortLine -Text $item.content -MaxChars 120
            if (-not [string]::IsNullOrWhiteSpace($content)) {
                $snsItems.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text ("外部Discord {0} #{1} / {2}: {3}" -f $item.guild, $item.channel, $item.author, $content)))
            }
        }
    }
    if ($twitterItems.Count -gt 0) {
        foreach ($item in ($twitterItems | Sort-Object { Get-ActivityTimestamp -Item $_ } | Select-Object -First 20)) {
            $text = Get-ShortLine -Text $item.text -MaxChars 140
            if ([string]::IsNullOrWhiteSpace($text)) {
                $text = $item.url
            }
            $snsItems.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text ("Twitter/X @{0}: {1}" -f $item.username, $text)))
        }
    }

    $aiLines = New-Object 'System.Collections.Generic.List[string]'
    if ($aiItems.Count -gt 0) {
        foreach ($item in ($aiItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
            $summary = Get-ShortLine -Text $item.summary -MaxChars 180
            if ([string]::IsNullOrWhiteSpace($summary)) {
                $summary = Get-ShortLine -Text $item.details -MaxChars 180
            }
            if ([string]::IsNullOrWhiteSpace($summary)) {
                $summary = $item.url
            }
            $aiLines.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text ("{0}: {1}" -f $item.tool, $summary)))
        }
    } else {
        $aiLines.Add("生成AI活動の自動収集はまだありません。Codex/ChatGPT等での作業要約を追加するとここに反映されます。")
    }

    $signalLines = New-Object 'System.Collections.Generic.List[string]'
    $personalDiscordCount = @($recentDiscordItems | Where-Object {
        ($_.PSObject.Properties.Name -contains "author_id") -and
        (-not [string]::IsNullOrWhiteSpace($discordSelfUserId)) -and
        ([string]$_.author_id -eq $discordSelfUserId) -and
        (-not ($_.PSObject.Properties.Name -contains "channel" -and (Test-ActivityLogChannelName -Channel ([string]$_.channel)))
        )
    }).Count
    $snsTotal = $personalDiscordCount + $twitterItems.Count
    if ($snsTotal -gt 0) {
        $snsParts = New-Object 'System.Collections.Generic.List[string]'
        Add-CountPart -Parts $snsParts -Label "Discord本人投稿" -Count $personalDiscordCount
        Add-CountPart -Parts $snsParts -Label "Twitter/X" -Count $twitterItems.Count
        $snsDetail = Get-CountSummaryText -Parts $snsParts
        if ($snsTotal -ge 50) {
            $signalLines.Add("SNS活動がかなり多めです: $snsDetail。")
        } elseif ($snsTotal -ge 20) {
            $signalLines.Add("SNS活動はやや多めです: $snsDetail。")
        } else {
            $signalLines.Add("SNS活動量は控えめ/通常範囲です: $snsDetail。")
        }
    }
    if ($aiItems.Count -ge 10) {
        $signalLines.Add("生成AI利用が多めです: $($aiItems.Count) 件。休憩や手書き整理も検討。")
    }
    if ($watchItems.Count -gt 0) {
        $signalLines.Add("視聴ログ: $($watchItems.Count) 件。")
    }
    if ($foodItems.Count -gt 0) {
        $signalLines.Add("食事記録: $($foodItems.Count) 件。")
    }
    if ($gmailItems.Count -gt 0) {
        $signalLines.Add("Gmail由来のタスク候補: $($gmailItems.Count) 件。")
    }
    if ($calendarItems.Count -gt 0) {
        $signalLines.Add("カレンダー予定: $($calendarItems.Count) 件。")
    }
    if (-not [string]::IsNullOrWhiteSpace($weatherSummary)) {
        $signalLines.Add("天気: $weatherSummary")
    }
    if ($chatgptItems.Count -gt 0) {
        $signalLines.Add("ChatGPT Pro由来の研究アイデア候補: $($chatgptItems.Count) 件。")
    }
    if ($obsidianMemoChanged.Count -gt 0) {
        $signalLines.Add("Obsidianメモ変更: $($obsidianMemoChanged.Count) 件。")
    }

    $foodLines = New-Object 'System.Collections.Generic.List[string]'
    if ($foodItems.Count -gt 0) {
        foreach ($item in $foodItems) {
            $caption = Get-ShortLine -Text $item.content -MaxChars 120
            if ([string]::IsNullOrWhiteSpace($caption)) {
                $caption = "食事画像"
            }
            $foodLines.Add("- $(Get-TimestampedText -Item $item -ReportDate $Date -Text ((Get-FoodLabel -Item $item) + ': ' + $caption))")
            $foodLines.Add("")
            $foodLines.Add("  ![]($($item.obsidian_relative_path))")
            $foodLines.Add("")
        }
    } else {
        $foodLines.Add("- 食事画像はまだ収集されていません。Discordの食事チャンネルに写真を投稿するとここに反映されます。")
    }

    $doneItems = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in ($activityItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
        $content = Get-ShortLine -Text $item.content -MaxChars 220
        if (-not [string]::IsNullOrWhiteSpace($content)) {
            $doneItems.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text ("活動ログ: {0}" -f $content)))
        }
    }
    if ($discordItems.Count -gt 0 -or $recentDiscordItems.Count -gt 0) {
        $doneItems.Add("Discordの活動ログを日報材料として収集した。")
    }
    if ($externalDiscordItems.Count -gt 0) {
        $doneItems.Add("自己嫌悪文以外のDiscordサーバー活動 $($externalDiscordItems.Count)件を収集した。")
    }
    if ($twitterItems.Count -gt 0) {
        $doneItems.Add("Twitter/X (@jikokennobun) の活動 $($twitterItems.Count)件を日報材料に追加した。")
    }
    if ($aiItems.Count -gt 0) {
        $doneItems.Add("生成AIを使った活動 $($aiItems.Count)件を記録した。")
    }
    if ($chatgptItems.Count -gt 0) {
        $doneItems.Add("ChatGPT Pro対話由来の研究アイデア候補 $($chatgptItems.Count)件を収集した。")
    }
    if ($gmailItems.Count -gt 0) {
        $doneItems.Add("Gmail由来のタスク候補 $($gmailItems.Count)件を収集した。")
    }
    if ($calendarItems.Count -gt 0) {
        $doneItems.Add("カレンダー予定 $($calendarItems.Count)件を確認した。")
    }
    if ($wakeItems.Count -gt 0) {
        $doneItems.Add("起床ログ $($wakeItems.Count)件を確認した。")
    }
    if ($moodItems.Count -gt 0) {
        $doneItems.Add("気分ログ $($moodItems.Count)件を確認した。")
    }
    if ($reflectionItems.Count -gt 0) {
        $doneItems.Add("夜の振り返り $($reflectionItems.Count)件を日報に反映した。")
    }
    if ($foodItems.Count -gt 0) {
        $doneItems.Add("食事画像をObsidian添付フォルダに保存して日報へ埋め込んだ。")
    }
    if ($watchItems.Count -gt 0) {
        $doneItems.Add("視聴ログ $($watchItems.Count)件を日報材料に追加した。")
    }
    if ($youtubeItems.Count -gt 0) {
        $doneItems.Add("YouTube視聴メモを日報材料に追加した。")
    }
    if ($obsidianChanged.Count -gt 0) {
        $doneItems.Add("Obsidian研究ノートの更新 $($obsidianChanged.Count)件を確認した。")
    }
    if ($obsidianMemoChanged.Count -gt 0) {
        $doneItems.Add("Obsidianメモ変更履歴 $($obsidianMemoChanged.Count)件を日報に追加した。")
    }
    if (-not [string]::IsNullOrWhiteSpace($gitStatus)) {
        $doneItems.Add("リポジトリ内の変更状況を確認した。")
    }

    $readItems = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in ($watchItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
        $content = Get-WatchItemDisplay -Item $item
        $readItems.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text ("視聴ログ: {0}" -f $content)))
    }
    foreach ($item in ($youtubeItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
        $readItems.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text ("YouTube/動画: {0}" -f (Get-YouTubeItemDisplay -Item $item))))
    }
    $mailTaskItems = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in ($gmailItems | Sort-Object received_at | Select-Object -First 20)) {
        $subject = Get-ShortLine -Text $item.subject -MaxChars 140
        $hints = @($item.task_hints) -join " / "
        $kindLabel = Get-GmailKindLabel -Item $item
        $text = if ([string]::IsNullOrWhiteSpace($hints)) { "[$kindLabel] $subject" } else { "[$kindLabel] $subject / $hints" }
        if (-not [string]::IsNullOrWhiteSpace($text)) {
            $mailTaskItems.Add("- [ ] $text")
        }
    }
    if ($mailTaskItems.Count -eq 0) {
        $mailTaskItems.Add("- [ ] Gmail由来のタスク候補はありません。")
    }

    $obsidianMemoChangeItems = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in ($obsidianMemoChanged | Sort-Object LastModified -Descending | Select-Object -First 40)) {
        $obsidianMemoChangeItems.Add((Get-ObsidianMemoChangeDisplay -Item $item -ReportDate $Date))
    }
    if ($obsidianMemoChangeItems.Count -eq 0) {
        $obsidianMemoChangeItems.Add("変更されたObsidianメモはありません。")
    }

    $calendarTaskItems = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in ($calendarItems | Sort-Object { Get-ActivityTimestamp -Item $_ } | Select-Object -First 20)) {
        $calendarTaskItems.Add("- [ ] $(Get-TimestampedText -Item $item -ReportDate $Date -Text (Get-CalendarItemDisplay -Item $item))")
    }
    if ($calendarTaskItems.Count -eq 0) {
        $calendarTaskItems.Add("- [ ] カレンダー予定はありません。")
    }

    $researchIdeaItems = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in ($chatgptItems | Select-Object -First 20)) {
        $idea = Get-ShortLine -Text $item.text -MaxChars 220
        if (-not [string]::IsNullOrWhiteSpace($idea)) {
            $researchIdeaItems.Add("ChatGPT Pro ($($item.title)): $idea")
        }
    }
    if ($researchIdeaItems.Count -eq 0) {
        $researchIdeaItems.Add("昇格先: [[Research-memo/研究アイデアInbox|研究アイデアInbox]]")
    }

    $existingWake = Get-ExistingLineValue -Text $existingDailyText -Label "起床"
    if ($existingWake -match "^\s*-") {
        $existingWake = ""
    }
    $wakeValue = $existingWake
    if ([string]::IsNullOrWhiteSpace($wakeValue)) {
        $wakeValue = Get-WakeValueFromItems -WakeItems $wakeItems -ReportDate $Date
        if ([string]::IsNullOrWhiteSpace($wakeValue)) {
            $wakeSources = @($discordItems) + @($activityItems) + @($recentDiscordItems) + @($externalDiscordItems) + @($twitterItems) + @($watchItems) + @($youtubeItems) + @($foodItems) + @($aiItems)
            $wakeTimestamp = Get-EarliestActivityTimestamp -Items $wakeSources -DiscordSelfUserId $discordSelfUserId
            if ($null -ne $wakeTimestamp) {
                $wakeValue = $wakeTimestamp.ToString("HH:mm") + "（最初の記録から自動推定）"
            }
        }
    }

    $thoughtItems = @(
        "自動収集だけでは主観までは分からない。Discordでの発言や手書きメモを見ながら、あとで自分の言葉で足す。"
    )

    $countParts = New-Object 'System.Collections.Generic.List[string]'
    Add-CountPart -Parts $countParts -Label "日報Discord" -Count $discordItems.Count
    Add-CountPart -Parts $countParts -Label "活動ログ" -Count $activityItems.Count
    Add-CountPart -Parts $countParts -Label "同サーバー全体" -Count $recentDiscordItems.Count
    Add-CountPart -Parts $countParts -Label "外部Discord" -Count $externalDiscordItems.Count
    Add-CountPart -Parts $countParts -Label "Twitter/X" -Count $twitterItems.Count
    Add-CountPart -Parts $countParts -Label "生成AI" -Count $aiItems.Count
    Add-CountPart -Parts $countParts -Label "ChatGPT Pro" -Count $chatgptItems.Count
    Add-CountPart -Parts $countParts -Label "Gmail" -Count $gmailItems.Count
    Add-CountPart -Parts $countParts -Label "カレンダー" -Count $calendarItems.Count
    Add-CountPart -Parts $countParts -Label "視聴ログ" -Count $watchItems.Count
    Add-CountPart -Parts $countParts -Label "YouTube" -Count $youtubeItems.Count
    Add-CountPart -Parts $countParts -Label "食事画像" -Count $foodItems.Count
    Add-CountPart -Parts $countParts -Label "気分ログ" -Count $moodItems.Count
    Add-CountPart -Parts $countParts -Label "起床ログ" -Count $wakeItems.Count
    Add-CountPart -Parts $countParts -Label "振り返り" -Count $reflectionItems.Count
    Add-CountPart -Parts $countParts -Label "Obsidianメモ変更" -Count $obsidianMemoChanged.Count
    Add-CountPart -Parts $countParts -Label "Obsidian研究更新" -Count $obsidianChanged.Count
    $countSummaryText = Get-CountSummaryText -Parts $countParts

    $activitySummaryItems = New-Object 'System.Collections.Generic.List[string]'
    foreach ($item in ($activityItems | Sort-Object { Get-ActivityTimestamp -Item $_ } | Select-Object -First 3)) {
        $content = Get-ShortLine -Text $item.content -MaxChars 80
        if (-not [string]::IsNullOrWhiteSpace($content)) {
            $activitySummaryItems.Add($content)
        }
    }
    foreach ($item in ($watchItems | Sort-Object { Get-ActivityTimestamp -Item $_ } | Select-Object -First 2)) {
        $activitySummaryItems.Add("視聴: " + (Get-ShortLine -Text (Get-WatchItemDisplay -Item $item) -MaxChars 90))
    }
    foreach ($item in ($calendarItems | Sort-Object { Get-ActivityTimestamp -Item $_ } | Select-Object -First 2)) {
        $activitySummaryItems.Add("予定: " + (Get-ShortLine -Text (Get-CalendarItemDisplay -Item $item) -MaxChars 90))
    }
    foreach ($item in ($gmailItems | Sort-Object received_at | Select-Object -First 2)) {
        $subject = Get-ShortLine -Text $item.subject -MaxChars 80
        if (-not [string]::IsNullOrWhiteSpace($subject)) {
            $activitySummaryItems.Add("メール: $subject")
        }
    }
    if ($chatgptItems.Count -gt 0) {
        $activitySummaryItems.Add("ChatGPT Pro由来の研究アイデアを整理")
    }
    if ($aiItems.Count -gt 0) {
        $activitySummaryItems.Add("生成AI作業を記録")
    }
    if ($obsidianMemoChanged.Count -gt 0) {
        $activitySummaryItems.Add("Obsidianメモを更新")
    }
    if ($obsidianChanged.Count -gt 0) {
        $activitySummaryItems.Add("Obsidian研究ノートを更新")
    }
    if ($foodItems.Count -gt 0) {
        $activitySummaryItems.Add("食事画像を保存")
    }
    if ($activitySummaryItems.Count -eq 0 -and $doneItems.Count -gt 0) {
        foreach ($item in ($doneItems | Select-Object -First 3)) {
            $activitySummaryItems.Add((Get-ShortLine -Text $item -MaxChars 90))
        }
    }
    $activitySummaryText = if ($activitySummaryItems.Count -gt 0) {
        Get-ShortLine -Text ("今日は" + (($activitySummaryItems.ToArray() | Select-Object -First 6) -join " / ") + "。") -MaxChars 650
    } else {
        "今日は自動収集できた活動ログが少なめ。必要なら、活動ログやObsidian側に手動で補足。"
    }

    $impressionItems = New-Object 'System.Collections.Generic.List[string]'
    $impressionItems.Add("活動まとめ: $activitySummaryText")
    foreach ($item in ($reflectionItems | Sort-Object { Get-ActivityTimestamp -Item $_ })) {
        $reflectionText = Get-ShortLine -Text $item.content -MaxChars 240
        if (-not [string]::IsNullOrWhiteSpace($reflectionText)) {
            $impressionItems.Add((Get-TimestampedText -Item $item -ReportDate $Date -Text $reflectionText))
        }
    }
    if ($countParts.Count -gt 0) {
        $impressionItems.Add("自動集計: $countSummaryText。")
    }

    $digestParts = New-Object 'System.Collections.Generic.List[string]'
    $digestParts.Add("【$Date 日報】")
    $digestParts.Add("")

    $wakeWeatherSentences = New-Object 'System.Collections.Generic.List[string]'
    if (-not [string]::IsNullOrWhiteSpace($wakeValue)) {
        $wakeWeatherSentences.Add("起床時刻は${wakeValue}です。")
    }
    if (-not [string]::IsNullOrWhiteSpace($weatherSummary)) {
        $wakeWeatherSentences.Add("天気は $weatherSummary でした。")
    }
    if ($wakeWeatherSentences.Count -gt 0) {
        $digestParts.Add("**起床と天気**")
        $digestParts.Add(($wakeWeatherSentences.ToArray() -join " "))
        $digestParts.Add("")
    }

    $digestParts.Add("**今日の活動**")
    $digestParts.Add($activitySummaryText)
    $digestParts.Add("")

    if ($countParts.Count -gt 0) {
        $digestParts.Add("**記録の内訳**")
        $digestParts.Add("自動収集では、$countSummaryText を確認しました。")
        $digestParts.Add("")
    }

    $digestParts.Add("**進捗**")
    if ($doneItems.Count -gt 0) {
        $progressText = Join-JapaneseNominalClauses -Items @($doneItems) -MaxItems 3
        if ([string]::IsNullOrWhiteSpace($progressText)) {
            $digestParts.Add("主な進捗はObsidian側の詳細日報にまとめています。")
        } else {
            $digestParts.Add("主な進捗は、${progressText}です。")
        }
    } else {
        $digestParts.Add("自動収集材料は少なめでした。必要ならObsidian側で詳細を追記してください。")
    }

    $body = if ([string]::IsNullOrWhiteSpace($templateText)) {
        @"
- 起床:
- 天気:

#やった
-

#思った
-

#読んだ/見た/知った
-

#精神状態
- 朝:
- 昼:
- 夜:

###### 今日の感想
"@
    } else {
        $templateText
    }
    $body = [regex]::Replace($body, "(?m)^(#{1,6})[ \t]*大学メールタスク[ \t]*$", '$1メールタスク')

    $body = Set-TemplateLineValueIfBlank -Text $body -Label "起床" -Value $wakeValue
    $body = Set-TemplateLineValueIfBlank -Text $body -Label "天気" -Value $weatherSummary
    if ($weatherDetailLines.Count -gt 0) {
        $body = Upsert-SectionBeforeHeading -Text $body -Heading "天気の移り変わり" -BeforeHeading "やった" -ContentLines (ConvertTo-BulletLines -Items @($weatherDetailLines) -Fallback "")
    }
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "活動まとめ" -BeforeHeading "やった" -ContentLines @("- $activitySummaryText")
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "食事" -BeforeHeading "やった" -ContentLines @($foodLines)
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "予定" -BeforeHeading "やった" -ContentLines @($calendarTaskItems)
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "メールタスク" -BeforeHeading "やった" -ContentLines @($mailTaskItems)
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "Obsidianメモ変更履歴" -BeforeHeading "やった" -ContentLines (ConvertTo-BulletLines -Items @($obsidianMemoChangeItems) -Fallback "変更されたObsidianメモはありません。")
    $body = Set-MarkdownSection -Text $body -Heading "やった" -ContentLines (ConvertTo-BulletLines -Items @($doneItems) -Fallback "今日やったことは手動で追記してください。")
    $body = Set-MarkdownSection -Text $body -Heading "思った" -ContentLines (ConvertTo-BulletLines -Items @($thoughtItems) -Fallback "今日思ったことをあとで足す。")
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "研究アイデア候補" -BeforeHeading "読んだ/見た/知った" -ContentLines (ConvertTo-BulletLines -Items @($researchIdeaItems) -Fallback "昇格先: [[Research-memo/研究アイデアInbox|研究アイデアInbox]]")
    $body = Set-MarkdownSection -Text $body -Heading "読んだ/見た/知った" -ContentLines (ConvertTo-BulletLines -Items @($readItems) -Fallback "今日読んだ/見た/知ったものを追記してください。")
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "SNSでの活動" -BeforeHeading "精神状態" -ContentLines (ConvertTo-BulletLines -Items @($snsItems) -Fallback "SNS活動の自動収集はありません。")
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "生成AIでの活動" -BeforeHeading "精神状態" -ContentLines (ConvertTo-BulletLines -Items @($aiLines) -Fallback "生成AI活動の自動収集はありません。")
    $body = Upsert-SectionBeforeHeading -Text $body -Heading "生活シグナル" -BeforeHeading "精神状態" -ContentLines (ConvertTo-BulletLines -Items @($signalLines) -Fallback "生活シグナルはありません。")
    $moodValues = Get-MoodValuesFromItems -MoodItems $moodItems -ReportDate $Date
    $body = Set-TemplateLineValue -Text $body -Label "朝" -Value $(if ([string]::IsNullOrWhiteSpace($moodValues["朝"])) { "未入力" } else { $moodValues["朝"] })
    $body = Set-TemplateLineValue -Text $body -Label "昼" -Value $(if ([string]::IsNullOrWhiteSpace($moodValues["昼"])) { "未入力" } else { $moodValues["昼"] })
    $body = Set-TemplateLineValue -Text $body -Label "夜" -Value $(if ([string]::IsNullOrWhiteSpace($moodValues["夜"])) { "未入力" } else { $moodValues["夜"] })
    $body = Set-AnyHeadingSection -Text $body -Heading "今日の感想" -ContentLines (ConvertTo-BulletLines -Items @($impressionItems) -Fallback "今日の感想を追記してください。")

    $report = New-Object 'System.Collections.Generic.List[string]'
    $report.Add("# Daily Report - $Date")
    $report.Add("")
    $report.Add($body.TrimEnd())
    $report.Add("")
    $report.Add("## Discord Digest")
    $report.Add("")
    foreach ($line in $digestParts) {
        $report.Add($line)
    }
    $report.Add("")

    ($report -join "`n") | Set-Content -LiteralPath $reportPath -Encoding UTF8
}

if ($SyncObsidian) {
    $obsidianDailyDir = Join-Path $ObsidianVaultRoot $ObsidianDailySubdir
    if (-not (Test-Path $obsidianDailyDir)) {
        New-Item -ItemType Directory -Path $obsidianDailyDir | Out-Null
    }
    Copy-Item -LiteralPath $reportPath -Destination (Join-Path $obsidianDailyDir "$Date.md") -Force
    Write-Host "Synced daily report to Obsidian: $(Join-Path $obsidianDailyDir "$Date.md")"
}

if ($PostDiscordDigest) {
    & (Join-Path $ScriptRoot "post-discord-webhook.ps1") -ContentPath $reportPath -SectionHeading "Discord Digest"
}

Write-Host "Source packet: $packetPath"
Write-Host "Daily report: $reportPath"














