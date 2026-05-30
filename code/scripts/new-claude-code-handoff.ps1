param(
    [string]$Focus = "Run an independent review of the next useful research step.",
    [string]$OutputPath = "",
    [string[]]$ContextFiles = @(
        "docs\claude-code-research-bridge.md",
        "docs\claude-code-autonomous-review-prompt.md",
        "docs\codex-research-automation.md",
        "logs\autonomous-discussion.md",
        "logs\claude-code-review.md",
        "ideas\research-questions.md",
        "open_problems.md",
        "definitions.md",
        "models\README.md",
        "models\macneille-reflection-search.md",
        "models\macneille-checker-interface.md",
        "scripts\check-macneille-reflection.ps1"
    )
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$repositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

function Get-RepositoryText {
    param([string]$RelativePath)

    $path = Join-Path $repositoryRoot $RelativePath
    if (-not (Test-Path $path)) {
        return ""
    }

    return Get-Content -Path $path -Raw -Encoding UTF8
}

function Get-Section {
    param(
        [string]$Text,
        [string]$StartHeading,
        [string]$NextHeadingPattern = "^## "
    )

    $escapedHeading = [regex]::Escape($StartHeading)
    $pattern = "(?ms)^$escapedHeading\s*`r?`n(?<body>.*?)(?=$NextHeadingPattern|\z)"
    $match = [regex]::Match($Text, $pattern)
    if ($match.Success) {
        return $match.Groups["body"].Value.Trim()
    }

    return ""
}

function Get-LastAutonomousPass {
    param([string]$Text)

    $matches = [regex]::Matches($Text, "(?ms)^### Pass \d+ - .*?(?=^### Pass \d+ - |\z)")
    if ($matches.Count -eq 0) {
        return ""
    }

    return $matches[$matches.Count - 1].Value.Trim()
}

function Get-LastClaudeReview {
    param([string]$Text)

    $matches = [regex]::Matches($Text, "(?ms)^### Review \d+ - .*?(?=^### Review \d+ - |\z)")
    if ($matches.Count -eq 0) {
        return "No Claude Code review has been recorded yet."
    }

    return $matches[$matches.Count - 1].Value.Trim()
}

function Get-GitStatusText {
    try {
        Push-Location $repositoryRoot
        return ((git status --short --branch) -join "`n")
    } catch {
        return "Git status unavailable: $($_.Exception.Message)"
    } finally {
        Pop-Location
    }
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $outputDir = Join-Path $repositoryRoot "outputs\claude-code"
    if (-not (Test-Path $outputDir)) {
        New-Item -ItemType Directory -Path $outputDir | Out-Null
    }
    $OutputPath = Join-Path $outputDir "handoff-$timestamp.md"
}

$researchQuestions = Get-RepositoryText "ideas\research-questions.md"
$openProblems = Get-RepositoryText "open_problems.md"
$autonomousLog = Get-RepositoryText "logs\autonomous-discussion.md"
$claudeLog = Get-RepositoryText "logs\claude-code-review.md"

$activeQuestions = Get-Section -Text $researchQuestions -StartHeading "## Active"
$coreProblems = Get-Section -Text $openProblems -StartHeading "## Core Separations"
$completionProblems = Get-Section -Text $openProblems -StartHeading "## Completion and Fixed Points"
$lastPass = Get-LastAutonomousPass -Text $autonomousLog
$lastReview = Get-LastClaudeReview -Text $claudeLog
$gitStatus = Get-GitStatusText
$generatedAt = Get-Date -Format "yyyy-MM-dd HH:mm:ss K"

$lines = @()
$lines += "# Claude Code Research Handoff"
$lines += ""
$lines += "- Generated: $generatedAt"
$lines += "- Repository: ``$repositoryRoot``"
$lines += "- Focus: $Focus"
$lines += ""
$lines += "## Claude Code Task"
$lines += ""
$lines += "Run one independent review pass for this repository. Complement the Codex autonomous loop by looking for hidden assumptions, counterexample directions, implementation gaps, and concrete next steps."
$lines += ""
$lines += 'Append your result to `logs/claude-code-review.md` using the format in `docs/claude-code-autonomous-review-prompt.md`. Do not commit or push unless the user explicitly asks.'
$lines += ""
$lines += "## Git Status"
$lines += ""
$lines += '```text'
$lines += $gitStatus
$lines += '```'
$lines += ""
$lines += "## Active Research Questions"
$lines += ""
$lines += $activeQuestions
$lines += ""
$lines += "## Core Open Problems"
$lines += ""
$lines += $coreProblems
$lines += ""
$lines += "## Completion/Fixed-Point Problems"
$lines += ""
$lines += $completionProblems
$lines += ""
$lines += "## Last Codex Autonomous Pass"
$lines += ""
$lines += $lastPass
$lines += ""
$lines += "## Last Claude Code Review"
$lines += ""
$lines += $lastReview
$lines += ""
$lines += "## Context Files to Read"
$lines += ""
foreach ($file in $ContextFiles) {
    $path = Join-Path $repositoryRoot $file
    if (Test-Path $path) {
        $lines += "- ``$file``"
    }
}
$lines += ""
$lines += "## Suggested Review Angles"
$lines += ""
$lines += '- Is the current completion-extension convention for antitone `boxtimes` mathematically justified, or merely a smoke-test rule?'
$lines += "- What is the smallest finite model/search target that could expose a non-principal completion fixed point?"
$lines += '- Does `scripts/check-macneille-reflection.ps1` report enough data to separate implementation artifacts from theorem-level evidence?'
$lines += "- Which note or open problem should be sharpened before the next autonomous Codex pass?"
$lines += ""

$outputDir = Split-Path -Parent $OutputPath
if (-not [string]::IsNullOrWhiteSpace($outputDir) -and -not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

$lines -join "`n" | Set-Content -Path $OutputPath -Encoding UTF8

Write-Host "Claude Code handoff written:"
Write-Host $OutputPath
Write-Host ""
Write-Host "Next:"
Write-Host "1. Open Claude Code in the repository root."
Write-Host "2. Paste this handoff or the prompt in docs\claude-code-autonomous-review-prompt.md."
