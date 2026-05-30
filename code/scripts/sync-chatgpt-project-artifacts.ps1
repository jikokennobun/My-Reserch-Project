param(
    [string]$SourceDirectory = "",
    [string]$RepositoryRoot = "",
    [string]$SlideDestination = "",
    [string]$PdfDestination = "",
    [string]$ManifestPath = "",
    [string[]]$Extensions = @(".pdf", ".ppt", ".pptx", ".odp"),
    [switch]$SkipPdfCollection,
    [switch]$SkipPdfBackup,
    [switch]$NoCreateSourceDirectory,
    [switch]$WhatIf
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
    param(
        [string]$Path,
        [switch]$NoCreate
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        if ($NoCreate) {
            throw "Directory does not exist: $Path"
        }

        if (-not $WhatIf) {
            New-Item -ItemType Directory -Path $Path | Out-Null
        }
    }

    if ($WhatIf -and -not (Test-Path -LiteralPath $Path)) {
        return [System.IO.Path]::GetFullPath($Path)
    }

    return (Resolve-Path -LiteralPath $Path).Path
}

function Get-DefaultProjectInbox {
    $myDriveName = -join ([char[]](0x30de, 0x30a4, 0x30c9, 0x30e9, 0x30a4, 0x30d6))
    $driveRoot = Join-Path $env:USERPROFILE $myDriveName
    return Join-Path $driveRoot "ChatGPT Project Inbox\My-Reserch-Project"
}

function Get-SafeFileName {
    param([string]$FileName)

    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($FileName)
    $extension = [System.IO.Path]::GetExtension($FileName).ToLowerInvariant()
    $safeBaseName = $baseName -replace '[^\w\-.]+', "_"
    $safeBaseName = $safeBaseName.Trim("._-")
    if ([string]::IsNullOrWhiteSpace($safeBaseName)) {
        $safeBaseName = "chatgpt-project-artifact"
    }

    return "$safeBaseName$extension"
}

function Get-TargetPath {
    param(
        [string]$Destination,
        [System.IO.FileInfo]$SourceFile,
        [string]$Hash
    )

    $safeName = Get-SafeFileName -FileName $SourceFile.Name
    $candidate = Join-Path $Destination $safeName
    if (-not (Test-Path -LiteralPath $candidate)) {
        return $candidate
    }

    $existingHash = (Get-FileHash -Path $candidate -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($existingHash -eq $Hash) {
        return $candidate
    }

    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($safeName)
    $extension = [System.IO.Path]::GetExtension($safeName)
    $shortHash = $Hash.Substring(0, 8)
    return Join-Path $Destination "$baseName-$shortHash$extension"
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

if ([string]::IsNullOrWhiteSpace($SourceDirectory)) {
    $SourceDirectory = Get-DefaultProjectInbox
}
$sourcePath = Resolve-OrCreateDirectory -Path $SourceDirectory -NoCreate:$NoCreateSourceDirectory

if ([string]::IsNullOrWhiteSpace($SlideDestination)) {
    $SlideDestination = Join-Path $repoPath "artifacts\slides\chatgpt-project"
}
$slideDestinationPath = Resolve-OrCreateDirectory -Path $SlideDestination

if ([string]::IsNullOrWhiteSpace($PdfDestination)) {
    $PdfDestination = Join-Path $repoPath "artifacts\pdf"
}
$pdfDestinationPath = Resolve-OrCreateDirectory -Path $PdfDestination

if ([string]::IsNullOrWhiteSpace($ManifestPath)) {
    $ManifestPath = Join-Path $repoPath "artifacts\reports\chatgpt-project-artifact-sync.csv"
}
$manifestDirectory = Resolve-OrCreateDirectory -Path (Split-Path -Parent $ManifestPath)
$manifestFullPath = Join-Path $manifestDirectory ([System.IO.Path]::GetFileName($ManifestPath))

$normalizedExtensions = @{}
foreach ($extension in $Extensions) {
    $normalized = $extension.ToLowerInvariant()
    if (-not $normalized.StartsWith(".")) {
        $normalized = ".$normalized"
    }
    $normalizedExtensions[$normalized] = $true
}

$existingRowsByKey = @{}
if (Test-Path -LiteralPath $manifestFullPath) {
    foreach ($row in @(Import-Csv -Path $manifestFullPath)) {
        if ($row.SourcePath -and $row.Sha256) {
            $existingRowsByKey["$($row.SourcePath)|$($row.Sha256)"] = $row
        }
    }
}

$importedRows = @{}
$sourceFiles = Get-ChildItem -Path $sourcePath -Recurse -File |
    Where-Object {
        $extension = $_.Extension.ToLowerInvariant()
        $normalizedExtensions.ContainsKey($extension) -and
            -not $_.Name.StartsWith("~") -and
            -not $_.Name.EndsWith(".tmp", [System.StringComparison]::OrdinalIgnoreCase)
    } |
    Sort-Object FullName

$importedCount = 0
$pdfCount = 0

foreach ($sourceFile in $sourceFiles) {
    $hash = (Get-FileHash -Path $sourceFile.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $targetPath = Get-TargetPath -Destination $slideDestinationPath -SourceFile $sourceFile -Hash $hash

    $shouldCopy = $true
    if (Test-Path -LiteralPath $targetPath) {
        $targetHash = (Get-FileHash -Path $targetPath -Algorithm SHA256).Hash.ToLowerInvariant()
        $shouldCopy = ($targetHash -ne $hash)
    }

    if ($shouldCopy -and -not $WhatIf) {
        Copy-Item -LiteralPath $sourceFile.FullName -Destination $targetPath -Force
    }

    if (-not $WhatIf) {
        $copiedHash = (Get-FileHash -Path $targetPath -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($copiedHash -ne $hash) {
            throw "Imported artifact hash mismatch: $targetPath"
        }
    }

    $relativeTarget = if ($WhatIf -and -not (Test-Path -LiteralPath $targetPath)) {
        Get-RelativePathCompat -BasePath $repoPath -TargetPath ([System.IO.Path]::GetFullPath($targetPath))
    } else {
        Get-RelativePathCompat -BasePath $repoPath -TargetPath (Resolve-Path -LiteralPath $targetPath).Path
    }

    $centralPdf = ""
    if ($sourceFile.Extension.Equals(".pdf", [System.StringComparison]::OrdinalIgnoreCase)) {
        $pdfCount += 1
        $safeTargetName = Get-SafeFileName -FileName (Split-Path -Leaf $targetPath)
        $safeBase = [System.IO.Path]::GetFileNameWithoutExtension($safeTargetName)
        $centralPdfName = "$safeBase-$($hash.Substring(0, 8)).pdf"
        $centralPdf = Get-RelativePathCompat -BasePath $repoPath -TargetPath (Join-Path $pdfDestinationPath $centralPdfName)
    }

    $sourceAbsolutePath = $sourceFile.FullName
    $key = "$sourceAbsolutePath|$hash"
    $importedAt = (Get-Date).ToString("s")
    if ($existingRowsByKey.ContainsKey($key) -and $existingRowsByKey[$key].ImportedAt) {
        $importedAt = $existingRowsByKey[$key].ImportedAt
    }

    $importedRows[$key] = [pscustomobject]@{
        SourcePath = $sourceAbsolutePath
        RepositoryFile = $relativeTarget
        CentralPdfFile = $centralPdf
        Extension = $sourceFile.Extension.ToLowerInvariant()
        Sha256 = $hash
        Bytes = $sourceFile.Length
        SourceLastWriteTime = $sourceFile.LastWriteTime.ToString("s")
        ImportedAt = $importedAt
    }

    if ($shouldCopy) {
        $importedCount += 1
    }
}

foreach ($key in $existingRowsByKey.Keys) {
    if (-not $importedRows.ContainsKey($key)) {
        $importedRows[$key] = $existingRowsByKey[$key]
    }
}

if (-not $WhatIf) {
    $rowsToWrite = @($importedRows.Values | Sort-Object SourcePath, Sha256)
    if ($rowsToWrite.Count -eq 0) {
        '"SourcePath","RepositoryFile","CentralPdfFile","Extension","Sha256","Bytes","SourceLastWriteTime","ImportedAt"' |
            Set-Content -Path $manifestFullPath -Encoding UTF8
    } else {
        $rowsToWrite | Export-Csv -Path $manifestFullPath -NoTypeInformation -Encoding UTF8
    }
}

if ($pdfCount -gt 0 -and -not $SkipPdfCollection -and -not $WhatIf) {
    $collectScript = Join-Path $scriptRoot "collect-pdfs.ps1"
    $collectArgs = @("-Root", $repoPath, "-Destination", $pdfDestinationPath)
    if ($SkipPdfBackup) {
        $collectArgs += "-SkipBackup"
    }

    & $collectScript @collectArgs
}

Write-Host "Source inbox: $sourcePath"
Write-Host "Slide destination: $slideDestinationPath"
Write-Host "Manifest: $manifestFullPath"
Write-Host "Scanned artifact(s): $(@($sourceFiles).Count)"
Write-Host "Copied or refreshed artifact(s): $importedCount"
Write-Host "PDF artifact(s): $pdfCount"
