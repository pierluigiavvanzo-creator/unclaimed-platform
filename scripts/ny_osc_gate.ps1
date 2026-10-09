param(
    [Parameter(Mandatory = $true)][string]$Archive,
    [Parameter(Mandatory = $true)][string]$LocalFileGate,
    [Parameter(Mandatory = $true)][string]$L1PiiGate,
    [Parameter(Mandatory = $true)][string]$PreflightGate,
    [Parameter(Mandatory = $true)][string]$L1ExecutionGate,
    [Parameter(Mandatory = $true)][string]$PreflightReceipt,
    [Parameter(Mandatory = $true)][string]$RunnerCheckpoint,
    [Parameter(Mandatory = $true)][string]$AuthorizedDownloadStartedAtUtc
)

$ErrorActionPreference = "Stop"

# Canonical active NY OSC gate entrypoint.
# Historical ny_osc_gate2..11 scripts are retained only as immutable lineage evidence.
# Their consumed approvals are not reusable.

$RepoRoot = Split-Path -Parent $PSScriptRoot
$PythonEntrypoint = Join-Path $RepoRoot "scripts\ny_mvp1_p1_targetability_execute.py"

if (-not (Test-Path -LiteralPath $PythonEntrypoint -PathType Leaf)) {
    throw "Canonical P1 Python entrypoint is missing."
}

$Arguments = @(
    $PythonEntrypoint,
    "--archive", $Archive,
    "--local-file-gate", $LocalFileGate,
    "--l1-pii-gate", $L1PiiGate,
    "--preflight-gate", $PreflightGate,
    "--l1-execution-gate", $L1ExecutionGate,
    "--preflight-receipt", $PreflightReceipt,
    "--runner-checkpoint", $RunnerCheckpoint,
    "--authorized-download-started-at-utc", $AuthorizedDownloadStartedAtUtc
)

Push-Location $RepoRoot
try {
    $env:PYTHONPATH = Join-Path $RepoRoot "src"
    & python @Arguments
    $ExitCode = $LASTEXITCODE
}
finally {
    Pop-Location
}

exit $ExitCode
