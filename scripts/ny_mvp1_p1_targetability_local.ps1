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

# Compatibility wrapper. The canonical active gate entrypoint is scripts/ny_osc_gate.ps1.
$CanonicalGate = Join-Path $PSScriptRoot "ny_osc_gate.ps1"

& $CanonicalGate \
    -Archive $Archive \
    -LocalFileGate $LocalFileGate \
    -L1PiiGate $L1PiiGate \
    -PreflightGate $PreflightGate \
    -L1ExecutionGate $L1ExecutionGate \
    -PreflightReceipt $PreflightReceipt \
    -RunnerCheckpoint $RunnerCheckpoint \
    -AuthorizedDownloadStartedAtUtc $AuthorizedDownloadStartedAtUtc

exit $LASTEXITCODE
