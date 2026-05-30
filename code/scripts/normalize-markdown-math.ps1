param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$rootPath = (Resolve-Path $Root).Path
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Get-RelativePathCompat {
    param(
        [string]$BasePath,
        [string]$TargetPath
    )

    $baseUri = [System.Uri]::new(($BasePath.TrimEnd('\') + '\'))
    $targetUri = [System.Uri]::new($TargetPath)
    $relativeUri = $baseUri.MakeRelativeUri($targetUri)
    return [System.Uri]::UnescapeDataString($relativeUri.ToString()).Replace('/', '\')
}

function Convert-MarkdownMathLine {
    param([string]$Line)

    $builder = [System.Text.StringBuilder]::new()
    $index = 0

    while ($index -lt $Line.Length) {
        if ($Line[$index] -eq [char]'`') {
            $tickEnd = $index
            while ($tickEnd -lt $Line.Length -and $Line[$tickEnd] -eq [char]'`') {
                $tickEnd++
            }

            $ticks = $Line.Substring($index, $tickEnd - $index)
            $close = $Line.IndexOf($ticks, $tickEnd, [System.StringComparison]::Ordinal)

            if ($close -ge 0) {
                [void]$builder.Append($Line.Substring($index, $close + $ticks.Length - $index))
                $index = $close + $ticks.Length
                continue
            }

            [void]$builder.Append($Line.Substring($index))
            break
        }

        $nextCode = $Line.IndexOf('`', $index)
        if ($nextCode -lt 0) {
            $nextCode = $Line.Length
        }

        $segment = $Line.Substring($index, $nextCode - $index)
        $segment = $segment.Replace('\[', '$$')
        $segment = $segment.Replace('\]', '$$')
        $segment = $segment.Replace('\(', '$')
        $segment = $segment.Replace('\)', '$')
        $segment = $segment.Replace('$|L|$', '$\lvert L\rvert$')
        $segment = $segment.Replace('$|G|$', '$\lvert G\rvert$')
        $segment = $segment.Replace('$|\mathrm{Fix}_{\boxtimes}(S)|$', '$\lvert\mathrm{Fix}_{\boxtimes}(S)\rvert$')
        [void]$builder.Append($segment)
        $index = $nextCode
    }

    return $builder.ToString()
}

$markdownFiles = Get-ChildItem -Path $rootPath -Recurse -File -Filter "*.md" |
    Where-Object { -not $_.FullName.StartsWith((Join-Path $rootPath ".git"), [System.StringComparison]::OrdinalIgnoreCase) }

$changed = @()

foreach ($file in $markdownFiles) {
    $text = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $out = [System.Text.StringBuilder]::new()
    $inFence = $false

    foreach ($match in [regex]::Matches($text, '(.*?)(\r\n|\n|\r|$)')) {
        if ($match.Value.Length -eq 0) {
            continue
        }

        $line = $match.Groups[1].Value
        $eol = $match.Groups[2].Value

        if ($line -match '^\s*(```|~~~)') {
            $inFence = -not $inFence
            [void]$out.Append($line)
        } elseif ($inFence) {
            [void]$out.Append($line)
        } else {
            [void]$out.Append((Convert-MarkdownMathLine -Line $line))
        }

        [void]$out.Append($eol)
    }

    $newText = $out.ToString()
    if ($newText -ne $text) {
        $changed += (Get-RelativePathCompat -BasePath $rootPath -TargetPath $file.FullName)
        if (-not $DryRun) {
            [System.IO.File]::WriteAllText($file.FullName, $newText, $utf8NoBom)
        }
    }
}

if ($changed.Count -eq 0) {
    Write-Host "No Markdown math delimiters needed normalization."
} else {
    Write-Host "Normalized Markdown math delimiters in $($changed.Count) file(s):"
    $changed | Sort-Object | ForEach-Object { Write-Host " - $_" }
}
