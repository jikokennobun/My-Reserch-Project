param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
    [string]$Destination = (Join-Path (Resolve-Path (Join-Path $PSScriptRoot "..")).Path "outputs\pdf")
)

$ErrorActionPreference = "Stop"

$rootPath = (Resolve-Path $Root).Path
$destinationPath = if (Test-Path $Destination) {
    (Resolve-Path $Destination).Path
} else {
    New-Item -ItemType Directory -Path $Destination | Out-Null
    (Resolve-Path $Destination).Path
}

$excludedPrefixes = @(
    (Join-Path $rootPath ".git"),
    $destinationPath
)

$pdfs = Get-ChildItem -Path $rootPath -Recurse -File -Filter "*.pdf" |
    Where-Object {
        $path = $_.FullName
        -not ($excludedPrefixes | Where-Object { $path.StartsWith($_, [System.StringComparison]::OrdinalIgnoreCase) })
    }

$manifestRows = @()

foreach ($pdf in $pdfs) {
    $hash = (Get-FileHash -Path $pdf.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $shortHash = $hash.Substring(0, 8)
    $safeBaseName = [System.IO.Path]::GetFileNameWithoutExtension($pdf.Name) -replace '[^\w\-.]+', "_"
    $targetName = "$safeBaseName-$shortHash.pdf"
    $targetPath = Join-Path $destinationPath $targetName

    if (-not (Test-Path $targetPath)) {
        Copy-Item -LiteralPath $pdf.FullName -Destination $targetPath
    }

    $relativeSource = [System.IO.Path]::GetRelativePath($rootPath, $pdf.FullName)
    $manifestRows += [pscustomobject]@{
        File = $targetName
        Source = $relativeSource
        Sha256 = $hash
        CollectedAt = (Get-Date).ToString("s")
    }
}

$manifestPath = Join-Path $destinationPath "manifest.csv"
$manifestRows | Export-Csv -Path $manifestPath -NoTypeInformation -Encoding UTF8

Write-Host "Collected $($manifestRows.Count) PDF(s) into $destinationPath"
Write-Host "Manifest: $manifestPath"
