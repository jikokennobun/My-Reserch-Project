param(
    [Parameter(Mandatory = $true)]
    [string]$SourcePath,
    [string]$VaultRelativePath,
    [string]$ObsidianVaultRoot = (Join-Path ([Environment]::GetFolderPath("MyDocuments")) "Mr.Jikokennobun"),
    [string]$ApiBaseUrl = $env:OBSIDIAN_LOCAL_REST_API_URL,
    [string]$ApiKey = $env:OBSIDIAN_LOCAL_REST_API_KEY,
    [switch]$PreferRestApi
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

if ([string]::IsNullOrWhiteSpace($ApiBaseUrl)) {
    $ApiBaseUrl = [Environment]::GetEnvironmentVariable("OBSIDIAN_LOCAL_REST_API_URL", "User")
}
if ([string]::IsNullOrWhiteSpace($ApiKey)) {
    $ApiKey = [Environment]::GetEnvironmentVariable("OBSIDIAN_LOCAL_REST_API_KEY", "User")
}

$source = Resolve-Path -LiteralPath $SourcePath
$content = Get-Content -LiteralPath $source.Path -Raw -Encoding UTF8

if ($PreferRestApi -and -not [string]::IsNullOrWhiteSpace($ApiBaseUrl) -and -not [string]::IsNullOrWhiteSpace($ApiKey) -and -not [string]::IsNullOrWhiteSpace($VaultRelativePath)) {
    $uri = $ApiBaseUrl.TrimEnd("/") + "/vault/" + [Uri]::EscapeDataString($VaultRelativePath)
    $headers = @{ Authorization = "Bearer $ApiKey" }
    try {
        Invoke-RestMethod -Method Put -Uri $uri -Headers $headers -Body $content -ContentType "text/markdown; charset=utf-8" | Out-Null
        Write-Host "Synced via Obsidian Local REST API: $VaultRelativePath"
        exit 0
    } catch {
        Write-Warning "Obsidian Local REST API sync failed, falling back to file copy: $($_.Exception.Message)"
    }
}

if ([string]::IsNullOrWhiteSpace($VaultRelativePath)) {
    throw "VaultRelativePath is required for file-copy fallback."
}

$target = Join-Path $ObsidianVaultRoot ($VaultRelativePath -replace "/", "\")
$targetDir = Split-Path -Parent $target
if (-not (Test-Path -LiteralPath $targetDir)) { New-Item -ItemType Directory -Path $targetDir | Out-Null }
Copy-Item -LiteralPath $source.Path -Destination $target -Force
Write-Host "Synced by file copy: $target"

