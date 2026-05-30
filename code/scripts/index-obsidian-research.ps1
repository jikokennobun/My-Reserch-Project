param(
    [string]$VaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$RepositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$includedRoots = @(
    "Research",
    "Research-memo",
    "References",
    "Logic & Logic",
    "Proof_memo",
    "Tex",
    "研究紹介"
)

$excludedNamePatterns = @(
    "自己省察",
    "妄想",
    "Song",
    "書きたい本"
)

function Get-Category {
    param(
        [string]$Root,
        [string]$Title
    )

    $text = "$Root $Title"

    if ($Root -eq "References") { return "Literature" }
    if ($Root -eq "Proof_memo") { return "Proof memo" }
    if ($Root -eq "研究紹介") { return "Research presentation" }
    if ($text -match "APS|AbProv|抽象的証明可能|G2|FG2|MND|MN4|GL|K4|証明可能|可証性|無矛盾|Gödel|Löb|Rosser") {
        return "APS/G2/provability"
    }
    if ($text -match "自己言及|相互言及|不動点|固定点|Lawvere|Smullyan|対角") {
        return "Self-reference/fixed point"
    }
    if ($text -match "圏|AAL|代数|普遍代数|Substructural|構造|強制") {
        return "Algebra/categorical logic"
    }
    if ($text -match "Domain|Scott|位相|topolog|連続") {
        return "Domain/topology"
    }
    if ($text -match "論理|Logic|計算可能性|記述集合論|真理") {
        return "Logic"
    }

    return "Research note"
}

function Test-ExcludedName {
    param([string]$Name)

    foreach ($pattern in $excludedNamePatterns) {
        if ($Name -match [regex]::Escape($pattern)) {
            return $true
        }
    }
    return $false
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

$vault = Resolve-Path $VaultRoot
$items = @()

foreach ($rootName in $includedRoots) {
    $rootPath = Join-Path $vault.Path $rootName
    if (-not (Test-Path $rootPath)) {
        continue
    }

    $files = Get-ChildItem -LiteralPath $rootPath -Recurse -File |
        Where-Object {
            $_.Extension -in @(".md", ".tex", ".pdf") -and -not (Test-ExcludedName -Name $_.Name)
        }

    foreach ($file in $files) {
        $relativeToVault = Get-RelativePathCompat -BasePath $vault.Path -FullPath $file.FullName
        $title = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)

        $items += [pscustomobject]@{
            Title = $title
            Category = Get-Category -Root $rootName -Title $title
            Root = $rootName
            Extension = $file.Extension.TrimStart(".")
            RelativePath = $relativeToVault
            SizeBytes = $file.Length
            LastModified = $file.LastWriteTime.ToString("s")
        }
    }
}

$referencesDir = Join-Path $RepositoryRoot "references"
$notesDir = Join-Path $RepositoryRoot "notes"
if (-not (Test-Path $referencesDir)) { New-Item -ItemType Directory -Path $referencesDir | Out-Null }
if (-not (Test-Path $notesDir)) { New-Item -ItemType Directory -Path $notesDir | Out-Null }

$csvPath = Join-Path $referencesDir "obsidian-research-index.csv"
$mdPath = Join-Path $notesDir "obsidian-research-index.md"

$items |
    Sort-Object Root, Category, Title |
    Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8

$byRoot = $items | Group-Object Root | Sort-Object Name
$byCategory = $items | Group-Object Category | Sort-Object Name
$recent = $items | Sort-Object LastModified -Descending | Select-Object -First 30
$large = $items | Sort-Object SizeBytes -Descending | Select-Object -First 30

$lines = @()
$lines += "# Obsidian Research Index"
$lines += ""
$lines += "Source vault:"
$lines += ""
$lines += "`$HOME\Documents\Mr.Jikokennobun"
$lines += ""
$lines += "Generated: $(Get-Date -Format s)"
$lines += ""
$lines += "This index intentionally includes only research-related folders from the Obsidian vault. It does not index daily logs, personal notes, life planning, images, or non-research folders."
$lines += ""
$lines += "## Included Roots"
$lines += ""
foreach ($root in $includedRoots) {
    $lines += "- $root"
}
$lines += ""
$lines += "## Excluded Title Patterns"
$lines += ""
foreach ($pattern in $excludedNamePatterns) {
    $lines += "- $pattern"
}
$lines += ""
$lines += "## Counts by Root"
$lines += ""
$lines += "| Root | Count |"
$lines += "| --- | ---: |"
foreach ($group in $byRoot) {
    $lines += "| $($group.Name) | $($group.Count) |"
}
$lines += ""
$lines += "## Counts by Category"
$lines += ""
$lines += "| Category | Count |"
$lines += "| --- | ---: |"
foreach ($group in $byCategory) {
    $lines += "| $($group.Name) | $($group.Count) |"
}
$lines += ""
$lines += "## Recently Modified"
$lines += ""
$lines += "| Title | Category | Root | Last modified | Path |"
$lines += "| --- | --- | --- | --- | --- |"
foreach ($item in $recent) {
    $path = $item.RelativePath -replace "\|", "/"
    $lines += "| $($item.Title) | $($item.Category) | $($item.Root) | $($item.LastModified) | $path |"
}
$lines += ""
$lines += "## Largest Research Notes"
$lines += ""
$lines += "| Title | Category | Root | Size | Path |"
$lines += "| --- | --- | --- | ---: | --- |"
foreach ($item in $large) {
    $path = $item.RelativePath -replace "\|", "/"
    $lines += "| $($item.Title) | $($item.Category) | $($item.Root) | $($item.SizeBytes) | $path |"
}
$lines += ""
$lines += "## Full CSV"
$lines += ""
$lines += "See [../references/obsidian-research-index.csv](../references/obsidian-research-index.csv)."
$lines += ""
$lines += "## Update Command"
$lines += ""
$lines += '```powershell'
$lines += 'powershell -ExecutionPolicy Bypass -File .\scripts\index-obsidian-research.ps1'
$lines += '```'

$lines -join "`n" | Set-Content -Path $mdPath -Encoding UTF8

Write-Host "Indexed $($items.Count) research file(s)."
Write-Host "CSV: $csvPath"
Write-Host "Markdown: $mdPath"



