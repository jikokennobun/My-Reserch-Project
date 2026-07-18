param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ResearchArguments
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [Console]::OutputEncoding

$bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$pythonExecutable = if (Test-Path -LiteralPath $bundledPython) { $bundledPython } else { $null }
$pythonArgs = @()
if (-not $pythonExecutable) {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCommand) {
        $pythonExecutable = $pythonCommand.Source
    }
}

if (-not $pythonExecutable) {
    $pythonCommand = Get-Command py -ErrorAction SilentlyContinue
    if ($pythonCommand) {
        $pythonExecutable = $pythonCommand.Source
        $pythonArgs = @("-3")
    }
}

if (-not $pythonExecutable) {
    throw "Python 3 was not found. Install Python, enable the 'py' launcher, or run this command inside Codex Desktop."
}

$scriptPath = Join-Path $PSScriptRoot "research_system.py"
& $pythonExecutable @pythonArgs $scriptPath @ResearchArguments
exit $LASTEXITCODE
