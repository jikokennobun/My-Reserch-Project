param(
    [Parameter(Mandatory = $true)]
    [string]$MarkdownPath,

    [string]$OutputPdf = "",
    [string]$RepositoryRoot = "",
    [string]$PdfDirectory = "",
    [string]$DriveBackupDirectory = "",
    [switch]$SkipDriveBackup
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

function Get-RelativePathCompat {
    param(
        [string]$BasePath,
        [string]$TargetPath
    )

    $baseUri = [System.Uri]::new(($BasePath.TrimEnd('\') + '\'))
    $targetUri = [System.Uri]::new($TargetPath)
    return [System.Uri]::UnescapeDataString($baseUri.MakeRelativeUri($targetUri).ToString()).Replace('/', '\')
}

function Resolve-OrCreateDirectory {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path | Out-Null
    }

    return (Resolve-Path -LiteralPath $Path).Path
}

function Get-DefaultDriveBackupDirectory {
    $myDriveName = -join ([char[]](0x30de, 0x30a4, 0x30c9, 0x30e9, 0x30a4, 0x30d6))
    $driveRoot = Join-Path $env:USERPROFILE $myDriveName
    if (Test-Path -LiteralPath $driveRoot) {
        return Join-Path $driveRoot "GitHub PDF Backup\My-Reserch-Project\artifacts\pdf"
    }

    return ""
}

$scriptRoot = if ([string]::IsNullOrWhiteSpace($PSScriptRoot)) {
    Split-Path -Parent $MyInvocation.MyCommand.Path
} else {
    $PSScriptRoot
}

if ([string]::IsNullOrWhiteSpace($RepositoryRoot)) {
    $RepositoryRoot = (Resolve-Path -LiteralPath (Join-Path $scriptRoot "..\..")).Path
}

$repoPath = (Resolve-Path -LiteralPath $RepositoryRoot).Path
$markdownFullPath = (Resolve-Path -LiteralPath $MarkdownPath).Path

if ([System.IO.Path]::GetExtension($markdownFullPath) -ne ".md") {
    throw "MarkdownPath must point to a .md file: $markdownFullPath"
}

if (-not $markdownFullPath.StartsWith($repoPath, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "MarkdownPath must be inside the repository: $markdownFullPath"
}

if ([string]::IsNullOrWhiteSpace($PdfDirectory)) {
    $PdfDirectory = Join-Path $repoPath "artifacts\pdf"
}
$pdfDirectoryPath = Resolve-OrCreateDirectory -Path $PdfDirectory

if ([string]::IsNullOrWhiteSpace($OutputPdf)) {
    $pdfName = [System.IO.Path]::GetFileNameWithoutExtension($markdownFullPath) + ".pdf"
    $OutputPdf = Join-Path $pdfDirectoryPath $pdfName
} elseif (-not [System.IO.Path]::IsPathRooted($OutputPdf)) {
    $OutputPdf = Join-Path $repoPath $OutputPdf
}

$outputDirectory = Resolve-OrCreateDirectory -Path (Split-Path -Parent $OutputPdf)
$outputPdfPath = Join-Path $outputDirectory ([System.IO.Path]::GetFileName($OutputPdf))

if (-not $outputPdfPath.StartsWith($pdfDirectoryPath, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "OutputPdf must be inside the PDF directory: $outputPdfPath"
}

$pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
if (-not $pandoc) {
    throw "pandoc is required to publish research output as PDF."
}

$xelatex = Get-Command xelatex -ErrorAction SilentlyContinue
if (-not $xelatex) {
    throw "xelatex is required as the pandoc PDF engine."
}

& $pandoc.Source `
    $markdownFullPath `
    "--from=gfm+tex_math_dollars+yaml_metadata_block" `
    "--pdf-engine=xelatex" `
    "--standalone" `
    "-V" "mainfont=Yu Mincho" `
    "-V" "sansfont=Yu Gothic" `
    "-V" "monofont=Consolas" `
    "-V" "geometry=margin=24mm" `
    "-o" $outputPdfPath

if ($LASTEXITCODE -ne 0) {
    throw "pandoc failed with exit code $LASTEXITCODE"
}

$pdfHash = (Get-FileHash -Path $outputPdfPath -Algorithm SHA256).Hash.ToLowerInvariant()
$pdfInfo = Get-Item -LiteralPath $outputPdfPath
$backupPath = ""

if (-not $SkipDriveBackup) {
    if ([string]::IsNullOrWhiteSpace($DriveBackupDirectory)) {
        $DriveBackupDirectory = Get-DefaultDriveBackupDirectory
    }

    if ([string]::IsNullOrWhiteSpace($DriveBackupDirectory)) {
        Write-Warning "Google Drive backup directory was not found. PDF remains in $pdfDirectoryPath"
    } else {
        $driveBackupPath = Resolve-OrCreateDirectory -Path $DriveBackupDirectory
        $backupPath = Join-Path $driveBackupPath $pdfInfo.Name
        Copy-Item -LiteralPath $outputPdfPath -Destination $backupPath -Force

        $backupHash = (Get-FileHash -Path $backupPath -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($backupHash -ne $pdfHash) {
            throw "Drive backup hash mismatch: $backupPath"
        }
    }
}

$manifestPath = Join-Path $pdfDirectoryPath "manifest.csv"
$relativePdf = Get-RelativePathCompat -BasePath $repoPath -TargetPath $outputPdfPath
$relativeSource = Get-RelativePathCompat -BasePath $repoPath -TargetPath $markdownFullPath
$row = [pscustomobject]@{
    File = $relativePdf
    Source = $relativeSource
    Sha256 = $pdfHash
    Bytes = $pdfInfo.Length
    GeneratedAt = (Get-Date).ToString("s")
    CollectedAt = ""
    BackedUpTo = $backupPath
}

$existingRows = @()
if (Test-Path -LiteralPath $manifestPath) {
    $existingRows = @(Import-Csv -Path $manifestPath | Where-Object {
        $_.File -ne $row.File -or $_.Source -ne $row.Source
    })
}

@($existingRows + $row) | Export-Csv -Path $manifestPath -NoTypeInformation -Encoding UTF8

Write-Host "Published PDF: $outputPdfPath"
Write-Host "Source Markdown: $markdownFullPath"
Write-Host "SHA256: $pdfHash"
if ($backupPath) {
    Write-Host "Drive backup: $backupPath"
}
Write-Host "Manifest: $manifestPath"
