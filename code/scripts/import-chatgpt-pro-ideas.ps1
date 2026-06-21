param(
    [string]$Date = (Get-Date).ToString("yyyy-MM-dd"),
    [string]$SourcePath,
    [string]$Title = "ChatGPT Pro idea",
    [string]$Text,
    [string]$Url,
    [string]$RepositoryRoot,
    [string]$OutPath,
    [string]$IdeaReportPath,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ObsidianIdeaPath = "Research-memo\研究アイデアInbox.md",
    [int]$MaxConversations = 50,
    [switch]$SyncObsidian,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$ScriptRoot = if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path (Join-Path $ScriptRoot "..\..")).Path
}
if ([string]::IsNullOrWhiteSpace($OutPath)) {
    $OutPath = Join-Path $RepositoryRoot "records\inbox\chatgpt\$Date.jsonl"
}
if ([string]::IsNullOrWhiteSpace($IdeaReportPath)) {
    $IdeaReportPath = Join-Path $RepositoryRoot "records\research-triage\chatgpt-pro-ideas-$Date.md"
}

function ConvertTo-JsonLine {
    param([object]$Value)
    return ($Value | ConvertTo-Json -Depth 24 -Compress)
}

function Get-ShortLine {
    param(
        [string]$Value,
        [int]$MaxChars = 600
    )

    if ([string]::IsNullOrWhiteSpace($Value)) { return "" }
    $clean = ($Value -replace "\s+", " ").Trim()
    if ($clean.Length -gt $MaxChars) { return $clean.Substring(0, $MaxChars) + "..." }
    return $clean
}

function Test-ResearchLike {
    param([string]$Value)

    if ([string]::IsNullOrWhiteSpace($Value)) { return $false }
    return ($Value -match "研究|アイデア|定義|命題|定理|補題|証明|反例|予想|疑問|問題|方針|APS|G2|FG2|MND|AMS|Loeb|Löb|Rosser|fixed point|proof|theorem|lemma|conjecture|definition")
}

function Get-MessageText {
    param([object]$Message)

    if ($null -eq $Message -or $null -eq $Message.content) { return "" }
    $content = $Message.content
    $parts = @()
    if ($content.PSObject.Properties.Name -contains "parts") {
        foreach ($part in @($content.parts)) {
            if ($part -is [string]) {
                $parts += $part
            } else {
                $parts += ($part | ConvertTo-Json -Depth 12)
            }
        }
    } elseif ($content.PSObject.Properties.Name -contains "text") {
        $parts += [string]$content.text
    }
    return ($parts -join "`n").Trim()
}

function Expand-ZipToTemp {
    param([string]$ZipPath)

    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $tempDir = Join-Path ([IO.Path]::GetTempPath()) ("chatgpt-export-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $tempDir | Out-Null
    [System.IO.Compression.ZipFile]::ExtractToDirectory($ZipPath, $tempDir)
    return $tempDir
}

function Get-DefaultSourceDirectory {
    $configured = [Environment]::GetEnvironmentVariable("CHATGPT_PRO_IDEA_SOURCE", "User")
    if (-not [string]::IsNullOrWhiteSpace($configured)) { return $configured }

    $myDriveName = -join ([char[]](0x30de, 0x30a4, 0x30c9, 0x30e9, 0x30a4, 0x30d6))
    $candidates = @(
        (Join-Path $env:USERPROFILE "$myDriveName\ChatGPT Pro Inbox\My-Reserch-Project"),
        (Join-Path $env:USERPROFILE "$myDriveName\ChatGPT Project Inbox\My-Reserch-Project\ideas"),
        (Join-Path $env:USERPROFILE "My Drive\ChatGPT Pro Inbox\My-Reserch-Project")
    )
    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath $candidate) { return $candidate }
    }
    return $candidates[0]
}

function Resolve-SourcePath {
    param([string]$Path)

    if (-not [string]::IsNullOrWhiteSpace($Path)) { return $Path }

    $defaultDir = Get-DefaultSourceDirectory
    if (-not (Test-Path -LiteralPath $defaultDir)) { return "" }

    $file = Get-ChildItem -LiteralPath $defaultDir -File -Recurse |
        Where-Object { $_.Extension -in @(".zip", ".json", ".txt", ".md") } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
    if ($null -eq $file) { return "" }
    return $file.FullName
}

function Find-ConversationsJson {
    param([string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) { return "" }
    if (-not (Test-Path -LiteralPath $Path)) { return "" }
    $item = Get-Item -LiteralPath $Path
    if (-not $item.PSIsContainer) {
        if ($item.Extension -eq ".zip") {
            $temp = Expand-ZipToTemp -ZipPath $item.FullName
            $found = Get-ChildItem -LiteralPath $temp -Recurse -Filter "conversations.json" -File | Select-Object -First 1
            if ($null -ne $found) { return $found.FullName }
        }
        return $item.FullName
    }
    $json = Get-ChildItem -LiteralPath $item.FullName -Recurse -Filter "conversations.json" -File | Select-Object -First 1
    if ($null -ne $json) { return $json.FullName }
    return ""
}

function Import-ChatGptConversations {
    param([string]$JsonPath)

    $items = New-Object 'System.Collections.Generic.List[object]'
    if ([string]::IsNullOrWhiteSpace($JsonPath) -or -not (Test-Path -LiteralPath $JsonPath)) {
        return $items
    }

    $conversations = @(Get-Content -LiteralPath $JsonPath -Raw -Encoding UTF8 | ConvertFrom-Json)
    $selected = $conversations |
        Sort-Object update_time -Descending |
        Select-Object -First $MaxConversations

    foreach ($conversation in $selected) {
        $conversationTitle = if ([string]::IsNullOrWhiteSpace($conversation.title)) { "Untitled ChatGPT conversation" } else { [string]$conversation.title }
        foreach ($node in @($conversation.mapping.PSObject.Properties.Value)) {
            if ($null -eq $node.message) { continue }
            $message = $node.message
            $role = if ($null -ne $message.author -and $message.author.PSObject.Properties.Name -contains "role") { [string]$message.author.role } else { "" }
            $messageText = Get-MessageText -Message $message
            if (-not (Test-ResearchLike -Value $messageText)) { continue }

            $timestamp = ""
            if ($message.create_time -is [double] -or $message.create_time -is [int]) {
                $timestamp = ([DateTimeOffset]::FromUnixTimeSeconds([int64]$message.create_time)).ToString("o")
            }

            $items.Add([ordered]@{
                timestamp = $timestamp
                date = $Date
                source = "chatgpt-pro-export"
                title = $conversationTitle
                role = $role
                text = Get-ShortLine -Value $messageText -MaxChars 1200
                conversation_id = [string]$conversation.id
            })
        }
    }
    return $items
}

$records = New-Object 'System.Collections.Generic.List[object]'

if (-not [string]::IsNullOrWhiteSpace($Text)) {
    $records.Add([ordered]@{
        timestamp = (Get-Date).ToString("o")
        date = $Date
        source = "chatgpt-pro-manual"
        title = $Title
        role = "manual"
        text = Get-ShortLine -Value $Text -MaxChars 2000
        url = $Url
    })
}

$SourcePath = Resolve-SourcePath -Path $SourcePath
if (-not [string]::IsNullOrWhiteSpace($SourcePath)) {
    $sourceItem = Get-Item -LiteralPath $SourcePath -ErrorAction SilentlyContinue
    if ($null -ne $sourceItem -and -not $sourceItem.PSIsContainer -and $sourceItem.Extension -in @(".txt", ".md")) {
        $body = Get-Content -LiteralPath $sourceItem.FullName -Raw -Encoding UTF8
        if (-not [string]::IsNullOrWhiteSpace($body)) {
            $records.Add([ordered]@{
                timestamp = (Get-Date).ToString("o")
                date = $Date
                source = "chatgpt-pro-file"
                title = if ([string]::IsNullOrWhiteSpace($Title)) { [IO.Path]::GetFileNameWithoutExtension($sourceItem.Name) } else { $Title }
                role = "file"
                text = Get-ShortLine -Value $body -MaxChars 2000
                url = $Url
            })
        }
    } else {
        $conversationJson = Find-ConversationsJson -Path $SourcePath
        foreach ($item in @(Import-ChatGptConversations -JsonPath $conversationJson)) {
            $records.Add($item)
        }
    }
}

if ($records.Count -eq 0) {
    Write-Host "No ChatGPT Pro idea records found."
    exit 0
}

$outDir = Split-Path -Parent $OutPath
if (-not (Test-Path -LiteralPath $outDir) -and -not $DryRun) {
    New-Item -ItemType Directory -Path $outDir | Out-Null
}
if (-not $DryRun) {
    $records | ForEach-Object { ConvertTo-JsonLine -Value $_ } | Set-Content -LiteralPath $OutPath -Encoding UTF8
}

$reportDir = Split-Path -Parent $IdeaReportPath
if (-not (Test-Path -LiteralPath $reportDir) -and -not $DryRun) {
    New-Item -ItemType Directory -Path $reportDir | Out-Null
}

$lines = New-Object 'System.Collections.Generic.List[string]'
$lines.Add("# ChatGPT Pro Ideas - $Date")
$lines.Add("")
$lines.Add("These are idea candidates from ChatGPT Pro conversations. Review before promoting them into stable research notes.")
$lines.Add("")
foreach ($group in ($records | Group-Object title | Sort-Object Name)) {
    $lines.Add("## $($group.Name)")
    $lines.Add("")
    foreach ($item in @($group.Group | Select-Object -First 12)) {
        $role = if ([string]::IsNullOrWhiteSpace($item.role)) { "unknown" } else { $item.role }
        $stamp = if ([string]::IsNullOrWhiteSpace($item.timestamp)) { "" } else { "[$($item.timestamp)] " }
        $lines.Add("- ${stamp}${role}: $($item.text)")
    }
    $lines.Add("")
}

if (-not $DryRun) {
    ($lines -join "`n") | Set-Content -LiteralPath $IdeaReportPath -Encoding UTF8
}

if ($SyncObsidian) {
    $obsidianPath = Join-Path $ObsidianVaultRoot $ObsidianIdeaPath
    $obsidianDir = Split-Path -Parent $obsidianPath
    if (-not (Test-Path -LiteralPath $obsidianDir) -and -not $DryRun) {
        New-Item -ItemType Directory -Path $obsidianDir | Out-Null
    }

    $block = New-Object 'System.Collections.Generic.List[string]'
    $block.Add("")
    $block.Add("## ChatGPT Pro ideas - $Date")
    $block.Add("")
    foreach ($item in @($records | Select-Object -First 40)) {
        $block.Add("- ($($item.title)) $($item.text)")
    }
    $block.Add("")

    if (-not $DryRun) {
        if (Test-Path -LiteralPath $obsidianPath) {
            Add-Content -LiteralPath $obsidianPath -Encoding UTF8 -Value (($block -join "`n"))
        } else {
            "# 研究アイデアInbox`n" + ($block -join "`n") | Set-Content -LiteralPath $obsidianPath -Encoding UTF8
        }
    }
    Write-Host "Synced ChatGPT Pro ideas to Obsidian: $obsidianPath"
}

Write-Host "Imported $($records.Count) ChatGPT Pro idea record(s)."
Write-Host "Inbox: $OutPath"
Write-Host "Idea report: $IdeaReportPath"



