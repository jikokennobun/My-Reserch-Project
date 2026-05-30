param(
    [ValidateRange(1, 1000)]
    [int]$Depth = 3,

    [string]$OutputPath = ""
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$repositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $OutputPath = Join-Path $repositoryRoot "models\examples\nfg2-depth-$Depth.json"
}

$carrier = @("T")
for ($i = 1; $i -le ($Depth + 1); $i++) {
    $carrier += "a$i"
}
$carrier += "s"

$order = @()
foreach ($x in $carrier) {
    $order += ,@($x, $x)
}
$order += ,@("s", "a$($Depth + 1)")

$box = [ordered]@{}
foreach ($x in $carrier) {
    $box[$x] = $x
}

$refutability = [ordered]@{}
$refutability["T"] = "a1"
for ($i = 1; $i -le $Depth; $i++) {
    $refutability["a$i"] = "a$($i + 1)"
}
$refutability["a$($Depth + 1)"] = "s"
$refutability["s"] = "s"

$falseBlock = -join (1..$Depth | ForEach-Object { "F" })
$expectedPrefix = "$falseBlock" + "TTTT"

$model = [ordered]@{
    name = "nfg2-depth-$Depth"
    carrier = $carrier
    order = $order
    top = "T"
    bottom = "s"
    box = $box
    refutability = $refutability
    metadata = [ordered]@{
        purpose = "Arbitrary-depth nFG2 first-true witness: nFG2(k) fails for k <= $Depth and holds at k = $($Depth + 1)."
        construction = "Orbit T -> a1 -> ... -> a$($Depth + 1) -> s -> s, with the only non-reflexive order s <= a$($Depth + 1)."
        first_true_nFG2 = $Depth + 1
        expected_nFG2_prefix = $expectedPrefix
        collapse = $false
        G2_mode = "vacuous"
        note = "The model is intentionally sparse; antitonicity is forced only by s <= a$($Depth + 1), whose image condition is s <= s."
    }
}

$outputDir = Split-Path -Parent $OutputPath
if (-not [string]::IsNullOrWhiteSpace($outputDir) -and -not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

$model | ConvertTo-Json -Depth 8 | Set-Content -Path $OutputPath -Encoding UTF8
Write-Host "nFG2 depth witness written:"
Write-Host $OutputPath
