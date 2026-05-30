param(
    [Parameter(Mandatory = $true)]
    [string]$ModelPath,

    [ValidateSet("antitone-dual-lower-cut-v0", "antitone-dual-lower-cut-v1")]
    [string]$ExtensionRule = "antitone-dual-lower-cut-v1",

    [string]$OutputPath = ""
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

function Assert-Condition {
    param(
        [bool]$Condition,
        [string]$Message
    )

    if (-not $Condition) {
        throw $Message
    }
}

function Get-JsonProperty {
    param(
        [object]$Object,
        [string]$Name
    )

    $property = $Object.PSObject.Properties[$Name]
    if ($null -eq $property) {
        throw "Missing property '$Name'."
    }

    return [string]$property.Value
}

function Get-SubsetKey {
    param(
        [string[]]$Subset,
        [hashtable]$Rank
    )

    return (($Subset | Sort-Object { $Rank[$_] }) -join "`u{1f}")
}

function Get-PowerSet {
    param([string[]]$Carrier)

    $count = [int][math]::Pow(2, $Carrier.Count)
    $sets = @()
    for ($mask = 0; $mask -lt $count; $mask++) {
        $subset = @()
        for ($index = 0; $index -lt $Carrier.Count; $index++) {
            if (($mask -band (1 -shl $index)) -ne 0) {
                $subset += $Carrier[$index]
            }
        }
        $sets += ,([string[]]$subset)
    }
    return $sets
}

function Format-Set {
    param(
        [string[]]$Subset,
        [hashtable]$Rank
    )

    $ordered = @($Subset | Sort-Object { $Rank[$_] })
    return "{ " + ($ordered -join ", ") + " }"
}

$resolvedModelPath = (Resolve-Path -Path $ModelPath).Path
$model = Get-Content -Path $resolvedModelPath -Raw -Encoding UTF8 | ConvertFrom-Json

$carrier = @($model.carrier | ForEach-Object { [string]$_ })
Assert-Condition ($carrier.Count -gt 0) "Model carrier must not be empty."

$carrierSet = @{}
$rank = @{}
for ($i = 0; $i -lt $carrier.Count; $i++) {
    Assert-Condition (-not $carrierSet.ContainsKey($carrier[$i])) "Duplicate carrier element '$($carrier[$i])'."
    $carrierSet[$carrier[$i]] = $true
    $rank[$carrier[$i]] = $i
}

function Assert-CarrierElement {
    param(
        [string]$Element,
        [string]$Context
    )

    Assert-Condition $carrierSet.ContainsKey($Element) "$Context '$Element' is not in carrier."
}

$top = [string]$model.top
$bottom = [string]$model.bottom
Assert-CarrierElement -Element $top -Context "top"
Assert-CarrierElement -Element $bottom -Context "bottom"

$order = @{}
foreach ($pair in @($model.order)) {
    Assert-Condition ($pair.Count -eq 2) "Each order entry must have exactly two elements."
    $left = [string]$pair[0]
    $right = [string]$pair[1]
    Assert-CarrierElement -Element $left -Context "order left"
    Assert-CarrierElement -Element $right -Context "order right"
    $order["$left`t$right"] = $true
}

function Test-Leq {
    param(
        [string]$Left,
        [string]$Right
    )

    return $order.ContainsKey("$Left`t$Right")
}

function Test-Equivalent {
    param(
        [string]$Left,
        [string]$Right
    )

    return ((Test-Leq -Left $Left -Right $Right) -and (Test-Leq -Left $Right -Right $Left))
}

foreach ($x in $carrier) {
    Assert-Condition (Test-Leq -Left $x -Right $x) "Order is not reflexive at '$x'."
}

foreach ($x in $carrier) {
    foreach ($y in $carrier) {
        foreach ($z in $carrier) {
            if ((Test-Leq -Left $x -Right $y) -and (Test-Leq -Left $y -Right $z)) {
                Assert-Condition (Test-Leq -Left $x -Right $z) "Order is not transitive: $x <= $y <= $z but $x <= $z is missing."
            }
        }
    }
}

$box = @{}
$refutability = @{}
foreach ($x in $carrier) {
    $boxValue = Get-JsonProperty -Object $model.box -Name $x
    $refutabilityValue = Get-JsonProperty -Object $model.refutability -Name $x
    Assert-CarrierElement -Element $boxValue -Context "box($x)"
    Assert-CarrierElement -Element $refutabilityValue -Context "refutability($x)"
    $box[$x] = $boxValue
    $refutability[$x] = $refutabilityValue
}

foreach ($x in $carrier) {
    foreach ($y in $carrier) {
        if (Test-Leq -Left $x -Right $y) {
            Assert-Condition (Test-Leq -Left $refutability[$y] -Right $refutability[$x]) "Refutability is not antitone: $x <= $y but refutability($y) <= refutability($x) is missing."
        }
    }
}

function Get-Uppers {
    param([string[]]$Subset)

    return @($carrier | Where-Object {
        $candidate = $_
        foreach ($x in $Subset) {
            if (-not (Test-Leq -Left $x -Right $candidate)) {
                return $false
            }
        }
        return $true
    })
}

function Get-Lowers {
    param([string[]]$Subset)

    return @($carrier | Where-Object {
        $candidate = $_
        foreach ($x in $Subset) {
            if (-not (Test-Leq -Left $candidate -Right $x)) {
                return $false
            }
        }
        return $true
    })
}

function Get-MacNeilleClosure {
    param([string[]]$Subset)

    return [string[]](Get-Lowers -Subset (Get-Uppers -Subset $Subset))
}

function Get-MacNeilleDualClosure {
    param([string[]]$Subset)

    return [string[]](Get-Uppers -Subset (Get-Lowers -Subset $Subset))
}

function Invoke-CompletedRefutability {
    param([string[]]$Cut)

    $image = @()
    foreach ($x in $Cut) {
        $image += $refutability[$x]
    }

    switch ($ExtensionRule) {
        "antitone-dual-lower-cut-v0" {
            return [string[]](Get-MacNeilleClosure -Subset $image)
        }
        "antitone-dual-lower-cut-v1" {
            return [string[]](Get-MacNeilleDualClosure -Subset $image)
        }
    }
}

$closedCuts = @()
$closedByKey = @{}
foreach ($subset in (Get-PowerSet -Carrier $carrier)) {
    $closure = Get-MacNeilleClosure -Subset $subset
    $subsetKey = Get-SubsetKey -Subset $subset -Rank $rank
    $closureKey = Get-SubsetKey -Subset $closure -Rank $rank
    if ($subsetKey -eq $closureKey -and -not $closedByKey.ContainsKey($subsetKey)) {
        $closedByKey[$subsetKey] = $true
        $closedCuts += ,([string[]]$subset)
    }
}

$principalByKey = @{}
$principalCutByElement = @{}
$dualPrincipalCutByElement = @{}
$principalCuts = @()
foreach ($x in $carrier) {
    $cut = Get-MacNeilleClosure -Subset @($x)
    $dualCut = Get-MacNeilleDualClosure -Subset @($x)
    $key = Get-SubsetKey -Subset $cut -Rank $rank
    $principalByKey[$key] = $x
    $principalCutByElement[$x] = [string[]]$cut
    $dualPrincipalCutByElement[$x] = [string[]]$dualCut
    $principalCuts += [pscustomobject]@{
        element = $x
        cut = @($cut | Sort-Object { $rank[$_] })
        display = Format-Set -Subset $cut -Rank $rank
        dualCut = @($dualCut | Sort-Object { $rank[$_] })
        dualDisplay = Format-Set -Subset $dualCut -Rank $rank
    }
}

$syntacticFixedPoints = @()
foreach ($x in $carrier) {
    if (Test-Equivalent -Left $x -Right $refutability[$x]) {
        $syntacticFixedPoints += $x
    }
}

$completedFixedPoints = @()
foreach ($cut in $closedCuts) {
    $extended = Invoke-CompletedRefutability -Cut $cut
    $cutKey = Get-SubsetKey -Subset $cut -Rank $rank
    $extendedKey = Get-SubsetKey -Subset $extended -Rank $rank
    if ($cutKey -eq $extendedKey) {
        $isPrincipal = $principalByKey.ContainsKey($cutKey)
        $principalElement = if ($isPrincipal) { $principalByKey[$cutKey] } else { $null }
        $isReflected = if ($isPrincipal) {
            Test-Equivalent -Left $principalElement -Right $refutability[$principalElement]
        } else {
            $false
        }
        $completedFixedPoints += [pscustomobject]@{
            cut = @($cut | Sort-Object { $rank[$_] })
            display = Format-Set -Subset $cut -Rank $rank
            principal = $isPrincipal
            principalElement = $principalElement
            reflected = $isReflected
        }
    }
}

$extensionConditionFailures = @()
foreach ($x in $carrier) {
    $sourceCut = [string[]]($principalCutByElement[$x])
    $actualCut = Invoke-CompletedRefutability -Cut $sourceCut
    $expectedCut = if ($ExtensionRule -eq "antitone-dual-lower-cut-v1") {
        [string[]]($dualPrincipalCutByElement[$refutability[$x]])
    } else {
        [string[]]($principalCutByElement[$refutability[$x]])
    }
    $expectedEmbedding = if ($ExtensionRule -eq "antitone-dual-lower-cut-v1") {
        "dual-principal"
    } else {
        "lower-principal"
    }
    $actualKey = Get-SubsetKey -Subset $actualCut -Rank $rank
    $expectedKey = Get-SubsetKey -Subset $expectedCut -Rank $rank

    if ($actualKey -ne $expectedKey) {
        $extensionConditionFailures += [pscustomobject]@{
            element = $x
            refutability = $refutability[$x]
            expectedEmbedding = $expectedEmbedding
            actual = @($actualCut | Sort-Object { $rank[$_] })
            actualDisplay = Format-Set -Subset $actualCut -Rank $rank
            expected = @($expectedCut | Sort-Object { $rank[$_] })
            expectedDisplay = Format-Set -Subset $expectedCut -Rank $rank
        }
    }
}

$nonPrincipalCount = @($completedFixedPoints | Where-Object { -not $_.principal }).Count
$principalUnreflectedCount = @($completedFixedPoints | Where-Object { $_.principal -and -not $_.reflected }).Count
$reflectedCount = @($completedFixedPoints | Where-Object { $_.reflected }).Count
$classification = if ($completedFixedPoints.Count -eq 0) {
    "no-completion-fixed-point"
} elseif ($nonPrincipalCount -gt 0 -and $syntacticFixedPoints.Count -eq 0) {
    "nonprincipal-without-syntactic"
} elseif ($nonPrincipalCount -gt 0) {
    "nonprincipal-with-rounding-candidate"
} elseif ($principalUnreflectedCount -gt 0) {
    "principal-unreflected"
} elseif ($reflectedCount -gt 0) {
    "reflected-only"
} else {
    "principal-only"
}

$g2Antecedent = Test-Leq -Left $refutability[$top] -Right $bottom
$g2 = if ($g2Antecedent) { Test-Leq -Left $top -Right $bottom } else { $true }
$fg2 = Test-Leq -Left $refutability[$refutability[$top]] -Right $refutability[$top]

$extensionDescription = if ($ExtensionRule -eq "antitone-dual-lower-cut-v1") {
    "v1: treat antitone refutability as a monotone map L -> L^op and close the pointwise image by the L^op MacNeille closure ((image)^l_L)^u_L."
} else {
    "Legacy v0: close the pointwise refutability image by the L MacNeille lower-cut closure ((image)^u_L)^l_L. This is retained to reproduce earlier smoke-test output and has the wrong polarity for antitone L -> L^op."
}

$warnings = @(
    "APS axioms A1-A4 are not checked by this finite checker."
)
if ($ExtensionRule -eq "antitone-dual-lower-cut-v0") {
    $warnings = @(
        "The selected v0 rule has the wrong polarity for antitone L -> L^op; use v1 for current research passes."
    ) + $warnings
}
if ($extensionConditionFailures.Count -gt 0) {
    $warnings += "The selected extension rule does not preserve all principal cuts for this model."
}

$report = [pscustomobject]@{
    model = $model.name
    modelPath = $resolvedModelPath
    extensionRule = $ExtensionRule
    extensionDescription = $extensionDescription
    classification = $classification
    carrierSize = $carrier.Count
    closedCutCount = $closedCuts.Count
    closedCuts = @($closedCuts | ForEach-Object {
        [pscustomobject]@{
            cut = @($_ | Sort-Object { $rank[$_] })
            display = Format-Set -Subset $_ -Rank $rank
            principalElement = if ($principalByKey.ContainsKey((Get-SubsetKey -Subset $_ -Rank $rank))) { $principalByKey[(Get-SubsetKey -Subset $_ -Rank $rank)] } else { $null }
        }
    })
    principalCuts = $principalCuts
    syntacticFixedPoints = $syntacticFixedPoints
    completedFixedPoints = $completedFixedPoints
    extensionConditionFailures = $extensionConditionFailures
    g2 = $g2
    fg2 = $fg2
    warnings = $warnings
}

if (-not [string]::IsNullOrWhiteSpace($OutputPath)) {
    $outputDir = Split-Path -Parent $OutputPath
    if (-not [string]::IsNullOrWhiteSpace($outputDir) -and -not (Test-Path $outputDir)) {
        New-Item -ItemType Directory -Path $outputDir | Out-Null
    }
    $report | ConvertTo-Json -Depth 8 | Set-Content -Path $OutputPath -Encoding UTF8
}

Write-Host "Model: $($report.model)"
Write-Host "Extension rule: $ExtensionRule"
Write-Host "Closed cuts: $($report.closedCutCount)"
Write-Host "Syntactic fixed point(s): $($syntacticFixedPoints -join ', ')"
Write-Host "Completed fixed point classification: $classification"
foreach ($fixedPoint in $completedFixedPoints) {
    $principalText = if ($fixedPoint.principal) { "principal: $($fixedPoint.principalElement)" } else { "non-principal" }
    $reflectionText = if ($fixedPoint.principal) {
        if ($fixedPoint.reflected) { "reflected" } else { "unreflected" }
    } else {
        "not reflected"
    }
    Write-Host "  $($fixedPoint.display) [$principalText; $reflectionText]"
}
if ($extensionConditionFailures.Count -gt 0) {
    Write-Host "Principal extension condition failures: $($extensionConditionFailures.Count)"
}
