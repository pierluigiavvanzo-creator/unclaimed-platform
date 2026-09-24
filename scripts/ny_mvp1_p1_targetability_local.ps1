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

python scripts/ny_mvp1_p1_targetability_execute.py `
    --archive $Archive `
    --local-file-gate $LocalFileGate `
    --l1-pii-gate $L1PiiGate `
    --preflight-gate $PreflightGate `
    --l1-execution-gate $L1ExecutionGate `
    --preflight-receipt $PreflightReceipt `
    --runner-checkpoint $RunnerCheckpoint `
    --authorized-download-started-at-utc $AuthorizedDownloadStartedAtUtc

exit $LASTEXITCODE
