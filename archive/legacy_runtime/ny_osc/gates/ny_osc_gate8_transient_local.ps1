param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eighth_attempt_transient_local_approval.v1.json"
$PiiApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eighth_attempt_transient_pii_approval.v1.json"
$FreshPreflightReceipt = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eighth_fresh_listing_preflight_receipt.v1.json"
$ExecutionAuthorization = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_eighth_execution_authorization.v1.json"

$ExpectedProposalRef = "sources/proposals/ny_osc_owner_name_file_eighth_bounded_attempt_authorization.v1.json"
$ExpectedProposalCheckpoint = "0364207e12e70afe4ccaf80e981791871325110a"
$ExpectedProposalCiRunId = 35749555291
$ExpectedAttemptNumber = 8
$ExpectedPreflightFreshnessSeconds = 900
$ExpectedLocalAuthorization = "APPROVO NY OSC EIGHTH TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE EIGHTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
$ExpectedExecutionAuthorization = "AUTHORIZE_NY_OSC_EIGHTH_BOUNDED_EXECUTION_ONCE"

$ProtectedGate8Paths = @(
    "scripts/ny_osc_gate8_transient_local.ps1"
    "sources/proposals/ny_osc_owner_name_file_eighth_bounded_attempt_authorization.v1.json"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_attempt8_freshness.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_5.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_4.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_schema_discovery.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution.py"
)

function Assert-Gate8ProtectedPackage {
    param([Parameter(Mandatory = $true)][string]$RunnerCheckpoint)

    if ($RunnerCheckpoint -notmatch '^[0-9a-f]{40}$') {
        throw "Eighth-attempt runner checkpoint is not a 40-character Git SHA. Do not download."
    }

    $InsideWorkTree = (& git -C $RepoRoot rev-parse --is-inside-work-tree 2>$null)
    if ($LASTEXITCODE -ne 0 -or $InsideWorkTree.Trim() -ne "true") {
        throw "Gate 8 must run from the authorized Git working tree. Do not download."
    }

    & git -C $RepoRoot cat-file -e "${RunnerCheckpoint}^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Approved Gate 8 runner checkpoint is not available locally. Do not download."
    }

    foreach ($RelativePath in $ProtectedGate8Paths) {
        $ExpectedBlob = (& git -C $RepoRoot rev-parse "${RunnerCheckpoint}:$RelativePath" 2>$null)
        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($ExpectedBlob)) {
            throw "Protected Gate 8 path is absent from the approved runner checkpoint. Do not download."
        }
        $ActualPath = Join-Path $RepoRoot $RelativePath
        if (-not (Test-Path -LiteralPath $ActualPath -PathType Leaf)) {
            throw "Protected Gate 8 path is missing from the working tree. Do not download."
        }
        $ActualBlob = (& git -C $RepoRoot hash-object -- $ActualPath 2>$null)
        if ($LASTEXITCODE -ne 0 -or $ActualBlob.Trim() -ne $ExpectedBlob.Trim()) {
            throw "Protected Gate 8 package differs from the approved runner checkpoint. Do not download."
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
        $Record.proposal_ci_run_id -ne $ExpectedProposalCiRunId -or
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

    Assert-CommonBinding -Record $Receipt -Label "Eighth-attempt preflight" -RunnerCheckpoint $RunnerCheckpoint

    if ($Receipt.status -ne "EXACT_MATCH" -or $Receipt.remote_preflight_performed -ne $true) {
        throw "Eighth-attempt fresh listing preflight is not an exact match. Do not download."
    }
    if (
        [string]::IsNullOrWhiteSpace($Receipt.receipt_ref) -or
        [string]::IsNullOrWhiteSpace($Receipt.preflight_authorization_ref) -or
        [string]::IsNullOrWhiteSpace($Receipt.performed_at_utc)
    ) {
        throw "Eighth-attempt fresh listing preflight refs/timestamp are missing. Do not download."
    }
    if ($Receipt.freshness_window_seconds -ne $ExpectedPreflightFreshnessSeconds) {
        throw "Eighth-attempt fresh listing preflight freshness policy mismatch. Do not download."
    }
    if (
        $Receipt.expected_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.expected_listing.size_display -ne "390.51 MB" -or
        $Receipt.expected_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM" -or
        $Receipt.observed_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.observed_listing.size_display -ne "390.51 MB" -or
        $Receipt.observed_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM"
    ) {
        throw "Eighth-attempt listing metadata is not an exact match. Do not download."
    }
    if (
        $Receipt.download_performed -ne $false -or
        $Receipt.owner_file_opened -ne $false -or
        $Receipt.owner_pii_processed -ne $false -or
        $Receipt.contains_owner_pii -ne $false
    ) {
        throw "Eighth-attempt preflight privacy boundary mismatch. Do not download."
    }

    try {
        $PerformedAt = [DateTimeOffset]::Parse($Receipt.performed_at_utc)
    }
    catch {
        throw "Eighth-attempt preflight timestamp is invalid. Do not download."
    }
    $AgeSeconds = ([DateTimeOffset]::UtcNow - $PerformedAt.ToUniversalTime()).TotalSeconds
    if ($AgeSeconds -lt 0 -or $AgeSeconds -gt $ExpectedPreflightFreshnessSeconds) {
        throw "Eighth-attempt fresh listing preflight is stale or future-dated. Do not download."
    }
}

foreach ($RequiredArtifact in @(
    $LocalApproval,
    $PiiApproval,
    $FreshPreflightReceipt,
    $ExecutionAuthorization
)) {
    if (-not (Test-Path -LiteralPath $RequiredArtifact -PathType Leaf)) {
        throw "Required eighth-attempt authorization artifact is missing. Do not download."
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
    throw "All eighth-attempt single-use approvals must be granted and unconsumed. Do not download."
}

$RunnerCheckpoint = [string]$LocalApprovalRecord.runner_checkpoint
if ([string]::IsNullOrWhiteSpace($RunnerCheckpoint)) {
    throw "Eighth-attempt runner checkpoint is missing. Do not download."
}

Assert-CommonBinding -Record $LocalApprovalRecord -Label "Transient-local approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $PiiApprovalRecord -Label "Transient-PII approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $ExecutionAuthorizationRecord -Label "Execution authorization" -RunnerCheckpoint $RunnerCheckpoint
Assert-FreshPreflightReceipt -Receipt $FreshPreflightRecord -RunnerCheckpoint $RunnerCheckpoint
Assert-Gate8ProtectedPackage -RunnerCheckpoint $RunnerCheckpoint

if (
    $LocalApprovalRecord.owner_authorization -ne $ExpectedLocalAuthorization -or
    $PiiApprovalRecord.owner_authorization -ne $ExpectedPiiAuthorization -or
    $ExecutionAuthorizationRecord.owner_authorization -ne $ExpectedExecutionAuthorization
) {
    throw "Eighth-attempt human authorization phrase mismatch. Do not download."
}

$Refs = @(
    [string]$LocalApprovalRecord.execution_approval_ref,
    [string]$PiiApprovalRecord.execution_approval_ref,
    [string]$FreshPreflightRecord.receipt_ref,
    [string]$ExecutionAuthorizationRecord.execution_approval_ref
)
if ($Refs | Where-Object { [string]::IsNullOrWhiteSpace($_) }) {
    throw "Eighth-attempt binding ref is missing. Do not download."
}
if (($Refs | Select-Object -Unique).Count -ne 4) {
    throw "Eighth-attempt binding refs must be distinct. Do not download."
}

if (
    $ExecutionAuthorizationRecord.fresh_preflight_receipt_ref -ne $FreshPreflightRecord.receipt_ref -or
    $ExecutionAuthorizationRecord.fresh_preflight_status -ne "EXACT_MATCH" -or
    $ExecutionAuthorizationRecord.download_authority -ne "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP" -or
    $ExecutionAuthorizationRecord.execution_authority -ne "ONE_BOUND_GATE8_EXECUTION"
) {
    throw "Eighth-attempt explicit execution authorization mismatch. Do not download."
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
    throw "Eighth-attempt local retention scope mismatch. Do not download."
}

if (
    $PiiApprovalRecord.execution_bounds.downloads_max -ne 1 -or
    $PiiApprovalRecord.execution_bounds.retries_max -ne 0 -or
    $PiiApprovalRecord.execution_bounds.max_download_bytes -ne 450000000 -or
    $PiiApprovalRecord.execution_bounds.max_uncompressed_bytes -ne 2000000000 -or
    $PiiApprovalRecord.execution_bounds.max_archive_members -ne 1 -or
    $PiiApprovalRecord.execution_bounds.required_transient_execution_authorization_contract_version -ne "1.4.0" -or
    $PiiApprovalRecord.execution_bounds.required_execution_result_contract_version -ne "1.5.0" -or
    $PiiApprovalRecord.execution_bounds.required_quote_dialect_mode -ne "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY" -or
    $PiiApprovalRecord.execution_bounds.automatic_retry_allowed -ne $false
) {
    throw "Eighth-attempt execution bounds mismatch. Do not download."
}

if (
    $PiiApprovalRecord.processing_scope.transient_owner_pii_in_memory_allowed -ne $true -or
    $PiiApprovalRecord.processing_scope.owner_rows_persistence_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.owner_field_decoding_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.owner_field_buffering_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.owner_field_logging_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.row_specific_human_inspection_allowed -ne $false
) {
    throw "Eighth-attempt processing scope mismatch. Do not download."
}

if (
    $ExecutionAuthorizationRecord.authorization_scope.manual_download_allowed -ne $true -or
    $ExecutionAuthorizationRecord.authorization_scope.direct_network_client_allowed -ne $false -or
    $ExecutionAuthorizationRecord.authorization_scope.downloads_max -ne 1 -or
    $ExecutionAuthorizationRecord.authorization_scope.gate8_executions_max -ne 1 -or
    $ExecutionAuthorizationRecord.authorization_scope.retries_max -ne 0
) {
    throw "Eighth-attempt execution authorization scope mismatch. Do not download."
}

$TempDir = Join-Path $env:TEMP (
    "unclaimed-ny-osc-gate2-eighth-" + [guid]::NewGuid().ToString("N")
)
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC eighth bounded attempt"
    Write-Host "All four machine-bound grants are verified."
    Write-Host "Fresh listing receipt: EXACT_MATCH and currently within 900 seconds."
    Write-Host "The execution authorization permits exactly one manual download."
    Write-Host "Save FINDERS.zip directly into:"
    Write-Host $TempDir
    Write-Host ""
    Write-Host "Start the separately authorized manual download now."
    Read-Host "As soon as the browser shows that the transfer HAS STARTED, press Enter"
    $AuthorizedDownloadStartedAtUtc = [DateTimeOffset]::UtcNow.ToUniversalTime().ToString("o")
    Write-Host "Attempt-8 download-start marker captured."
    Read-Host "Press Enter only after that same single download finishes"

    if (-not (Test-Path -LiteralPath $Archive -PathType Leaf)) {
        throw "FINDERS.zip not found in the dedicated eighth-attempt temp directory."
    }

    Push-Location $RepoRoot
    try {
        $PythonCode = @'
from pathlib import Path
import sys
from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_5 import (
    build_real_execution_authorization_v1_4,
    execute_transient_local_file_discovery_v1_5,
)
authorization = build_real_execution_authorization_v1_4(
    Path(sys.argv[2]),
    Path(sys.argv[3]),
    Path(sys.argv[4]),
    Path(sys.argv[5]),
    expected_runner_checkpoint=sys.argv[6],
    authorized_download_started_at_utc=sys.argv[7],
)
result = execute_transient_local_file_discovery_v1_5(
    authorization,
    Path(sys.argv[1]),
)
print(result.model_dump_json())
raise SystemExit(0 if result.status == "DISCOVERED" else 2)
'@
        python -c $PythonCode $Archive $LocalApproval $PiiApproval $FreshPreflightReceipt $ExecutionAuthorization $RunnerCheckpoint $AuthorizedDownloadStartedAtUtc

        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC eighth bounded attempt stopped fail-closed."
        }
    }
    finally {
        Pop-Location
    }
}
finally {
    if (Test-Path $TempDir) {
        Remove-Item -LiteralPath $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
