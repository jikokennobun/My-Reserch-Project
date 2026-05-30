param(
    [string]$Root = "",
    [string]$Destination = "",
    [string]$BackupDestination = "",
    [switch]$SkipBackup
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

function Get-DefaultBackupDestination {
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

if ([string]::IsNullOrWhiteSpace($Root)) {
    $Root = (Resolve-Path -LiteralPath (Join-Path $scriptRoot "..\..")).Path
}

$rootPath = (Resolve-Path $Root).Path

if ([string]::IsNullOrWhiteSpace($Destination)) {
    $Destination = Join-Path $rootPath "artifacts\pdf"
}

$destinationPath = Resolve-OrCreateDirectory -Path $Destination

$excludedPrefixes = @(
    (Join-Path $rootPath ".git"),
    $destinationPath
)

$pdfs = Get-ChildItem -Path $rootPath -Recurse -File -Filter "*.pdf" |
    Where-Object {
        $path = $_.FullName
        -not ($excludedPrefixes | Where-Object { $path.StartsWith($_, [System.StringComparison]::OrdinalIgnoreCase) })
    }
$collectedPdfCount = @($pdfs).Count

$manifestPath = Join-Path $destinationPath "manifest.csv"
$existingRowsByFile = @{}
if (Test-Path -LiteralPath $manifestPath) {
    foreach ($row in @(Import-Csv -Path $manifestPath)) {
        if ($row.File) {
            $existingRowsByFile[$row.File] = $row
        }
    }
}

$sourceByTargetName = @{}

foreach ($pdf in $pdfs) {
    $hash = (Get-FileHash -Path $pdf.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $shortHash = $hash.Substring(0, 8)
    $safeBaseName = [System.IO.Path]::GetFileNameWithoutExtension($pdf.Name) -replace '[^\w\-.]+', "_"
    $targetName = "$safeBaseName-$shortHash.pdf"
    $targetPath = Join-Path $destinationPath $targetName

    if (-not (Test-Path $targetPath)) {
        Copy-Item -LiteralPath $pdf.FullName -Destination $targetPath
    }

    $relativeSource = Get-RelativePathCompat -BasePath $rootPath -TargetPath $pdf.FullName
    $sourceByTargetName[$targetName] = $relativeSource
}

Write-Host "Collected $collectedPdfCount PDF(s) into $destinationPath"

$backupByTargetName = @{}

if (-not $SkipBackup) {
    if ([string]::IsNullOrWhiteSpace($BackupDestination)) {
        $BackupDestination = Get-DefaultBackupDestination
    }

    if ([string]::IsNullOrWhiteSpace($BackupDestination)) {
        Write-Warning "Google Drive backup directory was not found. PDFs remain in $destinationPath"
    } else {
        $backupPath = Resolve-OrCreateDirectory -Path $BackupDestination
        $publishedPdfs = Get-ChildItem -Path $destinationPath -File -Filter "*.pdf"

        foreach ($pdf in $publishedPdfs) {
            $targetPath = Join-Path $backupPath $pdf.Name
            Copy-Item -LiteralPath $pdf.FullName -Destination $targetPath -Force

            $sourceHash = (Get-FileHash -Path $pdf.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
            $targetHash = (Get-FileHash -Path $targetPath -Algorithm SHA256).Hash.ToLowerInvariant()
            if ($sourceHash -ne $targetHash) {
                throw "Backup hash mismatch: $targetPath"
            }

            $backupByTargetName[$pdf.Name] = $targetPath
        }

        Write-Host "Backed up $($publishedPdfs.Count) PDF(s) to $backupPath"
    }
}

$collectedAt = (Get-Date).ToString("s")
$manifestRows = @()
$centralPdfs = Get-ChildItem -Path $destinationPath -File -Filter "*.pdf" | Sort-Object Name

foreach ($pdf in $centralPdfs) {
    $relativeFile = Get-RelativePathCompat -BasePath $rootPath -TargetPath $pdf.FullName
    $existingRow = $null
    if ($existingRowsByFile.ContainsKey($relativeFile)) {
        $existingRow = $existingRowsByFile[$relativeFile]
    } elseif ($existingRowsByFile.ContainsKey($pdf.Name)) {
        $existingRow = $existingRowsByFile[$pdf.Name]
    }

    $hash = (Get-FileHash -Path $pdf.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $source = if ($sourceByTargetName.ContainsKey($pdf.Name)) {
        $sourceByTargetName[$pdf.Name]
    } elseif ($existingRow -and $existingRow.Source) {
        $existingRow.Source
    } else {
        $relativeFile
    }

    $generatedAt = if ($existingRow -and $existingRow.GeneratedAt) {
        $existingRow.GeneratedAt
    } else {
        ""
    }

    $backedUpTo = if ($backupByTargetName.ContainsKey($pdf.Name)) {
        $backupByTargetName[$pdf.Name]
    } elseif ($existingRow -and $existingRow.BackedUpTo) {
        $existingRow.BackedUpTo
    } else {
        ""
    }

    $manifestRows += [pscustomobject]@{
        File = $relativeFile
        Source = $source
        Sha256 = $hash
        Bytes = $pdf.Length
        GeneratedAt = $generatedAt
        CollectedAt = $collectedAt
        BackedUpTo = $backedUpTo
    }
}

$manifestRows | Export-Csv -Path $manifestPath -NoTypeInformation -Encoding UTF8

Write-Host "Manifest: $manifestPath"
