param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eleventh_attempt_transient_local_approval.v1.json"
$PiiApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eleventh_attempt_transient_pii_approval.v1.json"
$FreshPreflightReceipt = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eleventh_fresh_listing_preflight_receipt.v1.json"
$ExecutionAuthorization = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eleventh_execution_authorization.v1.json"
$PythonEntrypoint = Join-Path $RepoRoot "scripts\ny_osc_gate11_execute.py"

$ExpectedProposalRef = "sources/proposals/ny_osc_owner_name_file_eleventh_product_slice_auto_start_authorization.v1.json"
$ExpectedProposalCheckpoint = "270de2f6e79b7c654052519adc446fe76b811771"
$ExpectedAttemptNumber = 11
$ExpectedPreflightFreshnessSeconds = 900
$MinimumFreshnessRemainingSeconds = 180
$DownloadStartPollMilliseconds = 100
$ExpectedLocalAuthorization = "APPROVO NY OSC ELEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE ELEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
$ExpectedExecutionAuthorization = "AUTHORIZE_NY_OSC_ELEVENTH_BOUNDED_EXECUTION_ONCE"

$ProtectedGate11Paths = @(
    "scripts/ny_osc_gate11_transient_local.ps1"
    "scripts/ny_osc_gate11_execute.py"
    "sources/proposals/ny_osc_owner_name_file_eleventh_product_slice_auto_start_authorization.v1.json"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_attempt8_freshness.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_product_slice_v1.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_8.py"
    "src/unclaimed_platform/domain/mvp1_vertical_slice.py"
)

function Assert-Gate11ProtectedPackage {
    param([Parameter(Mandatory = $true)][string]$RunnerCheckpoint)
    if ($RunnerCheckpoint -notmatch '^[0-9a-f]{40}$') {
        throw "Attempt-11 runner checkpoint is invalid. Do not download."
    }
    $Inside = (& git -C $RepoRoot rev-parse --is-inside-work-tree 2>$null)
    if ($LASTEXITCODE -ne 0 -or $Inside.Trim() -ne "true") {
        throw "Gate 11 must run from the authorized Git worktree. Do not download."
    }
    & git -C $RepoRoot cat-file -e "${RunnerCheckpoint}^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Approved Gate 11 checkpoint is unavailable locally. Do not download."
    }
    foreach ($RelativePath in $ProtectedGate11Paths) {
        $ExpectedBlob = (& git -C $RepoRoot rev-parse "${RunnerCheckpoint}:$RelativePath" 2>$null)
        $ActualPath = Join-Path $RepoRoot $RelativePath
        if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $ActualPath -PathType Leaf)) {
            throw "Protected Gate 11 path is unavailable. Do not download."
        }
        $ActualBlob = (& git -C $RepoRoot hash-object -- $ActualPath 2>$null)
        if ($LASTEXITCODE -ne 0 -or $ActualBlob.Trim() -ne $ExpectedBlob.Trim()) {
            throw "Protected Gate 11 package differs from approved checkpoint. Do not download."
        }
    }
}

function Assert-CommonBinding {
    param([object]$Record, [string]$Label, [string]$RunnerCheckpoint)
    if (
        $Record.attempt_number -ne $ExpectedAttemptNumber -or
        $Record.proposal_ref -ne $ExpectedProposalRef -or
        $Record.proposal_checkpoint -ne $ExpectedProposalCheckpoint -or
        $Record.runner_checkpoint -ne $RunnerCheckpoint -or
        $Record.runner_ci_conclusion -ne "SUCCESS"
    ) {
        throw "$Label binding mismatch. Do not download."
    }
}

foreach ($RequiredArtifact in @($LocalApproval, $PiiApproval, $FreshPreflightReceipt, $ExecutionAuthorization)) {
    if (-not (Test-Path -LiteralPath $RequiredArtifact -PathType Leaf)) {
        throw "Required attempt-11 authorization artifact is missing. Do not download."
    }
}

$Local = Get-Content -LiteralPath $LocalApproval -Raw | ConvertFrom-Json
$Pii = Get-Content -LiteralPath $PiiApproval -Raw | ConvertFrom-Json
$Preflight = Get-Content -LiteralPath $FreshPreflightReceipt -Raw | ConvertFrom-Json
$Execution = Get-Content -LiteralPath $ExecutionAuthorization -Raw | ConvertFrom-Json

if ($Local.status -ne "GRANTED_NOT_CONSUMED" -or $Pii.status -ne "GRANTED_NOT_CONSUMED" -or $Execution.status -ne "GRANTED_NOT_CONSUMED") {
    throw "All attempt-11 single-use approvals must be granted and unconsumed. Do not download."
}

$RunnerCheckpoint = [string]$Local.runner_checkpoint
Assert-CommonBinding -Record $Local -Label "Transient-local approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $Pii -Label "Transient-PII approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $Preflight -Label "Fresh preflight" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $Execution -Label "Execution authorization" -RunnerCheckpoint $RunnerCheckpoint
Assert-Gate11ProtectedPackage -RunnerCheckpoint $RunnerCheckpoint

if ($Local.owner_authorization -ne $ExpectedLocalAuthorization -or $Pii.owner_authorization -ne $ExpectedPiiAuthorization -or $Execution.owner_authorization -ne $ExpectedExecutionAuthorization) {
    throw "Attempt-11 human authorization phrase mismatch. Do not download."
}

if ($Preflight.status -ne "EXACT_MATCH" -or $Preflight.remote_preflight_performed -ne $true -or $Preflight.freshness_window_seconds -ne $ExpectedPreflightFreshnessSeconds) {
    throw "Attempt-11 fresh preflight is invalid. Do not download."
}

if (
    $Preflight.expected_listing.remote_name -ne "FINDERS.zip" -or
    $Preflight.expected_listing.size_display -ne "390.51 MB" -or
    $Preflight.expected_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM" -or
    $Preflight.observed_listing.remote_name -ne "FINDERS.zip" -or
    $Preflight.observed_listing.size_display -ne "390.51 MB" -or
    $Preflight.observed_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM"
) {
    throw "Attempt-11 listing metadata is not an exact match. Do not download."
}

if ($Preflight.download_performed -ne $false -or $Preflight.owner_file_opened -ne $false -or $Preflight.owner_pii_processed -ne $false -or $Preflight.contains_owner_pii -ne $false) {
    throw "Attempt-11 preflight privacy boundary mismatch. Do not download."
}

try {
    $PerformedAt = [DateTimeOffset]::Parse($Preflight.performed_at_utc)
}
catch {
    throw "Attempt-11 preflight timestamp is invalid. Do not download."
}

$FreshDeadline = $PerformedAt.ToUniversalTime().AddSeconds($ExpectedPreflightFreshnessSeconds)
$NowBeforePrompt = [DateTimeOffset]::UtcNow
$AgeSeconds = ($NowBeforePrompt - $PerformedAt.ToUniversalTime()).TotalSeconds
if ($AgeSeconds -lt 0 -or $AgeSeconds -gt $ExpectedPreflightFreshnessSeconds) {
    throw "Attempt-11 fresh preflight is stale or future-dated. Do not download."
}
$RemainingSeconds = ($FreshDeadline - $NowBeforePrompt).TotalSeconds
if ($RemainingSeconds -lt $MinimumFreshnessRemainingSeconds) {
    throw "Attempt-11 freshness margin is too small to begin a download. Do not download."
}

if ($Execution.fresh_preflight_receipt_ref -ne $Preflight.receipt_ref -or $Execution.fresh_preflight_status -ne "EXACT_MATCH" -or $Execution.download_authority -ne "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP" -or $Execution.execution_authority -ne "ONE_BOUND_GATE11_EXECUTION") {
    throw "Attempt-11 explicit execution authorization mismatch. Do not download."
}

if ($Local.scope.expected_local_filename -ne "FINDERS.zip" -or $Local.scope.max_download_bytes -ne 450000000 -or $Local.scope.immediate_logical_deletion_required -ne $true -or $Local.scope.durable_raw_persistence_allowed -ne $false -or $Local.scope.repository_persistence_allowed -ne $false -or $Local.scope.cloud_sync_allowed -ne $false -or $Local.scope.chat_upload_allowed -ne $false) {
    throw "Attempt-11 local retention scope mismatch. Do not download."
}

if ($Pii.execution_bounds.downloads_max -ne 1 -or $Pii.execution_bounds.retries_max -ne 0 -or $Pii.execution_bounds.max_download_bytes -ne 450000000 -or $Pii.execution_bounds.max_uncompressed_bytes -ne 2000000000 -or $Pii.execution_bounds.max_archive_members -ne 1 -or $Pii.execution_bounds.required_execution_result_contract_version -ne "1.8.0") {
    throw "Attempt-11 execution bounds mismatch. Do not download."
}

if ($Pii.processing_scope.owner_rows_persistence_allowed -ne $false -or $Pii.processing_scope.owner_field_logging_allowed -ne $false -or $Pii.processing_scope.row_specific_human_inspection_allowed -ne $false -or $Pii.processing_scope.property_type_code_only_buffering_allowed -ne $true) {
    throw "Attempt-11 processing scope mismatch. Do not download."
}

if ($Execution.authorization_scope.downloads_max -ne 1 -or $Execution.authorization_scope.gate11_executions_max -ne 1 -or $Execution.authorization_scope.retries_max -ne 0 -or $Execution.authorization_scope.direct_network_client_allowed -ne $false) {
    throw "Attempt-11 execution scope mismatch. Do not download."
}

$TempDir = Join-Path $env:TEMP ("unclaimed-ny-osc-gate2-eleventh-" + [guid]::NewGuid().ToString("N"))
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null

$PreExistingFiles = @(Get-ChildItem -LiteralPath $TempDir -File -Force -ErrorAction SilentlyContinue)
if ($PreExistingFiles.Count -ne 0) {
    throw "Attempt-11 dedicated temp directory is not empty. Do not download."
}

Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC eleventh bounded product-slice attempt"
    Write-Host "All four machine-bound grants are verified."
    Write-Host "Fresh listing receipt: EXACT_MATCH."
    Write-Host ("Gate 11 has at least " + [math]::Floor($RemainingSeconds) + " freshness seconds remaining before arming.")
    Write-Host "Save FINDERS.zip directly into:"
    Write-Host $TempDir
    Write-Host ""
    Write-Host "Gate 11 automatic download-start detector is ARMED."
    Write-Host "Start the separately authorized single manual download now."
    Write-Host "Do not press Enter when the transfer starts; detection is automatic."

    $AuthorizedDownloadStartedAtUtc = $null
    while ($null -eq $AuthorizedDownloadStartedAtUtc) {
        $Now = [DateTimeOffset]::UtcNow
        if ($Now -gt $FreshDeadline) {
            throw "Attempt-11 did not detect download start inside the fresh preflight window."
        }

        $ObservedNonEmptyFile = Get-ChildItem -LiteralPath $TempDir -File -Force -ErrorAction SilentlyContinue | Where-Object { $_.Length -gt 0 } | Select-Object -First 1
        if ($null -ne $ObservedNonEmptyFile) {
            $AuthorizedDownloadStartedAtUtc = $Now.ToUniversalTime().ToString("o")
            break
        }

        Start-Sleep -Milliseconds $DownloadStartPollMilliseconds
    }

    Write-Host "Attempt-11 download-start automatically detected inside freshness window."
    Read-Host "Press Enter only after that same single download finishes"

    if (-not (Test-Path -LiteralPath $Archive -PathType Leaf)) {
        throw "FINDERS.zip not found in the dedicated attempt-11 temp directory."
    }

    $env:PYTHONPATH = Join-Path $RepoRoot "src"
    & python $PythonEntrypoint $Archive $LocalApproval $PiiApproval $FreshPreflightReceipt $ExecutionAuthorization $RunnerCheckpoint $AuthorizedDownloadStartedAtUtc

    if ($LASTEXITCODE -ne 0) {
        throw "NY OSC eleventh bounded product-slice attempt stopped fail-closed."
    }
}
finally {
    if (Test-Path $TempDir) {
        Remove-Item -LiteralPath $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
