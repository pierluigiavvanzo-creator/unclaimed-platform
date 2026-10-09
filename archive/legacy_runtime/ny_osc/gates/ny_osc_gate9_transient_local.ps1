param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_ninth_attempt_transient_local_approval.v1.json"
$PiiApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_ninth_attempt_transient_pii_approval.v1.json"
$FreshPreflightReceipt = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_ninth_fresh_listing_preflight_receipt.v1.json"
$ExecutionAuthorization = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_ninth_execution_authorization.v1.json"
$PythonEntrypoint = Join-Path $RepoRoot "scripts\ny_osc_gate9_execute.py"

$ExpectedProposalRef = "sources/proposals/ny_osc_owner_name_file_ninth_bounded_attempt_authorization.v1.json"
$ExpectedProposalCheckpoint = "9170f27480ccd49eafd040346fa80e0fe9ab078f"
$ExpectedAttemptNumber = 9
$ExpectedPreflightFreshnessSeconds = 900
$ExpectedLocalAuthorization = "APPROVO NY OSC NINTH TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE NINTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
$ExpectedExecutionAuthorization = "AUTHORIZE_NY_OSC_NINTH_BOUNDED_EXECUTION_ONCE"

$ProtectedGate9Paths = @(
    "scripts/ny_osc_gate9_transient_local.ps1"
    "scripts/ny_osc_gate9_execute.py"
    "sources/proposals/ny_osc_owner_name_file_ninth_bounded_attempt_authorization.v1.json"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_attempt8_freshness.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_trailing_delimiter_diagnostic.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_6.py"
)

function Assert-Gate9ProtectedPackage {
    param([Parameter(Mandatory = $true)][string]$RunnerCheckpoint)

    if ($RunnerCheckpoint -notmatch '^[0-9a-f]{40}$') {
        throw "Ninth-attempt runner checkpoint is not a 40-character Git SHA. Do not download."
    }
    $InsideWorkTree = (& git -C $RepoRoot rev-parse --is-inside-work-tree 2>$null)
    if ($LASTEXITCODE -ne 0 -or $InsideWorkTree.Trim() -ne "true") {
        throw "Gate 9 must run from the authorized Git working tree. Do not download."
    }
    & git -C $RepoRoot cat-file -e "${RunnerCheckpoint}^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Approved Gate 9 runner checkpoint is not available locally. Do not download."
    }
    foreach ($RelativePath in $ProtectedGate9Paths) {
        $ExpectedBlob = (& git -C $RepoRoot rev-parse "${RunnerCheckpoint}:$RelativePath" 2>$null)
        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($ExpectedBlob)) {
            throw "Protected Gate 9 path is absent from the approved runner checkpoint. Do not download."
        }
        $ActualPath = Join-Path $RepoRoot $RelativePath
        if (-not (Test-Path -LiteralPath $ActualPath -PathType Leaf)) {
            throw "Protected Gate 9 path is missing from the working tree. Do not download."
        }
        $ActualBlob = (& git -C $RepoRoot hash-object -- $ActualPath 2>$null)
        if ($LASTEXITCODE -ne 0 -or $ActualBlob.Trim() -ne $ExpectedBlob.Trim()) {
            throw "Protected Gate 9 package differs from the approved runner checkpoint. Do not download."
        }
    }
}

function Assert-CommonBinding {
    param(
        [Parameter(Mandatory = $true)][object]$Record,
        [Parameter(Mandatory = $true)][string]$Label,
        [Parameter(Mandatory = $true)][string]$RunnerCheckpoint
    )

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

function Assert-FreshPreflightReceipt {
    param(
        [Parameter(Mandatory = $true)][object]$Receipt,
        [Parameter(Mandatory = $true)][string]$RunnerCheckpoint
    )

    Assert-CommonBinding -Record $Receipt -Label "Ninth-attempt preflight" -RunnerCheckpoint $RunnerCheckpoint
    if ($Receipt.status -ne "EXACT_MATCH" -or $Receipt.remote_preflight_performed -ne $true) {
        throw "Ninth-attempt fresh listing preflight is not an exact match. Do not download."
    }
    if ($Receipt.freshness_window_seconds -ne $ExpectedPreflightFreshnessSeconds) {
        throw "Ninth-attempt fresh listing preflight freshness policy mismatch. Do not download."
    }
    if (
        $Receipt.expected_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.expected_listing.size_display -ne "390.51 MB" -or
        $Receipt.expected_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM" -or
        $Receipt.observed_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.observed_listing.size_display -ne "390.51 MB" -or
        $Receipt.observed_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM"
    ) {
        throw "Ninth-attempt listing metadata is not an exact match. Do not download."
    }
    if (
        $Receipt.download_performed -ne $false -or
        $Receipt.owner_file_opened -ne $false -or
        $Receipt.owner_pii_processed -ne $false -or
        $Receipt.contains_owner_pii -ne $false
    ) {
        throw "Ninth-attempt preflight privacy boundary mismatch. Do not download."
    }
    try {
        $PerformedAt = [DateTimeOffset]::Parse($Receipt.performed_at_utc)
    }
    catch {
        throw "Ninth-attempt preflight timestamp is invalid. Do not download."
    }
    $AgeSeconds = ([DateTimeOffset]::UtcNow - $PerformedAt.ToUniversalTime()).TotalSeconds
    if ($AgeSeconds -lt 0 -or $AgeSeconds -gt $ExpectedPreflightFreshnessSeconds) {
        throw "Ninth-attempt fresh listing preflight is stale or future-dated. Do not download."
    }
}

foreach ($RequiredArtifact in @(
    $LocalApproval,
    $PiiApproval,
    $FreshPreflightReceipt,
    $ExecutionAuthorization
)) {
    if (-not (Test-Path -LiteralPath $RequiredArtifact -PathType Leaf)) {
        throw "Required ninth-attempt authorization artifact is missing. Do not download."
    }
}

$LocalApprovalRecord = Get-Content -LiteralPath $LocalApproval -Raw | ConvertFrom-Json
$PiiApprovalRecord = Get-Content -LiteralPath $PiiApproval -Raw | ConvertFrom-Json
$FreshPreflightRecord = Get-Content -LiteralPath $FreshPreflightReceipt -Raw | ConvertFrom-Json
$ExecutionAuthorizationRecord = Get-Content -LiteralPath $ExecutionAuthorization -Raw | ConvertFrom-Json

if (
    $LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED" -or
    $PiiApprovalRecord.status -ne "GRANTED_NOT_CONSUMED" -or
    $ExecutionAuthorizationRecord.status -ne "GRANTED_NOT_CONSUMED"
) {
    throw "All ninth-attempt single-use approvals must be granted and unconsumed. Do not download."
}

$RunnerCheckpoint = [string]$LocalApprovalRecord.runner_checkpoint
if ([string]::IsNullOrWhiteSpace($RunnerCheckpoint)) {
    throw "Ninth-attempt runner checkpoint is missing. Do not download."
}

Assert-CommonBinding -Record $LocalApprovalRecord -Label "Transient-local approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $PiiApprovalRecord -Label "Transient-PII approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $ExecutionAuthorizationRecord -Label "Execution authorization" -RunnerCheckpoint $RunnerCheckpoint
Assert-FreshPreflightReceipt -Receipt $FreshPreflightRecord -RunnerCheckpoint $RunnerCheckpoint
Assert-Gate9ProtectedPackage -RunnerCheckpoint $RunnerCheckpoint

if (
    $LocalApprovalRecord.owner_authorization -ne $ExpectedLocalAuthorization -or
    $PiiApprovalRecord.owner_authorization -ne $ExpectedPiiAuthorization -or
    $ExecutionAuthorizationRecord.owner_authorization -ne $ExpectedExecutionAuthorization
) {
    throw "Ninth-attempt human authorization phrase mismatch. Do not download."
}

if (
    $ExecutionAuthorizationRecord.fresh_preflight_receipt_ref -ne $FreshPreflightRecord.receipt_ref -or
    $ExecutionAuthorizationRecord.fresh_preflight_status -ne "EXACT_MATCH" -or
    $ExecutionAuthorizationRecord.download_authority -ne "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP" -or
    $ExecutionAuthorizationRecord.execution_authority -ne "ONE_BOUND_GATE9_EXECUTION"
) {
    throw "Ninth-attempt explicit execution authorization mismatch. Do not download."
}

if (
    $LocalApprovalRecord.scope.expected_local_filename -ne "FINDERS.zip" -or
    $LocalApprovalRecord.scope.max_download_bytes -ne 450000000 -or
    $LocalApprovalRecord.scope.dedicated_os_temp_directory_required -ne $true -or
    $LocalApprovalRecord.scope.immediate_logical_deletion_required -ne $true -or
    $LocalApprovalRecord.scope.durable_raw_persistence_allowed -ne $false -or
    $LocalApprovalRecord.scope.repository_persistence_allowed -ne $false -or
    $LocalApprovalRecord.scope.cloud_sync_allowed -ne $false -or
    $LocalApprovalRecord.scope.chat_upload_allowed -ne $false
) {
    throw "Ninth-attempt local retention scope mismatch. Do not download."
}

if (
    $PiiApprovalRecord.execution_bounds.downloads_max -ne 1 -or
    $PiiApprovalRecord.execution_bounds.retries_max -ne 0 -or
    $PiiApprovalRecord.execution_bounds.max_download_bytes -ne 450000000 -or
    $PiiApprovalRecord.execution_bounds.max_uncompressed_bytes -ne 2000000000 -or
    $PiiApprovalRecord.execution_bounds.max_archive_members -ne 1 -or
    $PiiApprovalRecord.execution_bounds.required_transient_execution_authorization_contract_version -ne "1.5.0" -or
    $PiiApprovalRecord.execution_bounds.required_execution_result_contract_version -ne "1.6.0" -or
    $PiiApprovalRecord.execution_bounds.required_trailing_delimiter_diagnostic_contract_version -ne "1.0.0" -or
    $PiiApprovalRecord.execution_bounds.automatic_retry_allowed -ne $false
) {
    throw "Ninth-attempt execution bounds mismatch. Do not download."
}

if (
    $PiiApprovalRecord.processing_scope.transient_owner_pii_in_memory_allowed -ne $true -or
    $PiiApprovalRecord.processing_scope.owner_rows_persistence_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.owner_field_logging_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.row_specific_human_inspection_allowed -ne $false
) {
    throw "Ninth-attempt processing scope mismatch. Do not download."
}

if (
    $ExecutionAuthorizationRecord.authorization_scope.manual_download_allowed -ne $true -or
    $ExecutionAuthorizationRecord.authorization_scope.direct_network_client_allowed -ne $false -or
    $ExecutionAuthorizationRecord.authorization_scope.downloads_max -ne 1 -or
    $ExecutionAuthorizationRecord.authorization_scope.gate9_executions_max -ne 1 -or
    $ExecutionAuthorizationRecord.authorization_scope.retries_max -ne 0
) {
    throw "Ninth-attempt execution authorization scope mismatch. Do not download."
}

$TempDir = Join-Path $env:TEMP (
    "unclaimed-ny-osc-gate2-ninth-" + [guid]::NewGuid().ToString("N")
)
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC ninth bounded attempt"
    Write-Host "All four machine-bound grants are verified."
    Write-Host "Fresh listing receipt: EXACT_MATCH and currently within 900 seconds."
    Write-Host "The execution authorization permits exactly one manual download."
    Write-Host "Save FINDERS.zip directly into:"
    Write-Host $TempDir
    Write-Host ""
    Write-Host "Start the separately authorized manual download now."
    Read-Host "As soon as the browser shows that the transfer HAS STARTED, press Enter"
    $AuthorizedDownloadStartedAtUtc = [DateTimeOffset]::UtcNow.ToUniversalTime().ToString("o")
    Write-Host "Attempt-9 download-start marker captured."
    Read-Host "Press Enter only after that same single download finishes"

    if (-not (Test-Path -LiteralPath $Archive -PathType Leaf)) {
        throw "FINDERS.zip not found in the dedicated ninth-attempt temp directory."
    }

    $env:PYTHONPATH = Join-Path $RepoRoot "src"
    & python $PythonEntrypoint $Archive $LocalApproval $PiiApproval $FreshPreflightReceipt $ExecutionAuthorization $RunnerCheckpoint $AuthorizedDownloadStartedAtUtc
    if ($LASTEXITCODE -ne 0) {
        throw "NY OSC ninth bounded attempt stopped fail-closed."
    }
}
finally {
    if (Test-Path $TempDir) {
        Remove-Item -LiteralPath $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
