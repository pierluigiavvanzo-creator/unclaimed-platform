param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_seventh_attempt_transient_local_approval.v1.json"
$PiiApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_seventh_attempt_transient_pii_approval.v1.json"
$FreshPreflightReceipt = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_seventh_fresh_listing_preflight_receipt.v1.json"
$ExecutionAuthorization = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_seventh_execution_authorization.v1.json"

$ExpectedProposalRef = "sources/proposals/ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json"
$ExpectedProposalCheckpoint = "18c270bd89d7c4e0c37a5bc046a1f09e49dc672e"
$ExpectedProposalCiRunId = 35653220457
$ExpectedAttemptNumber = 7
$ExpectedPreflightFreshnessSeconds = 900
$ExpectedLocalAuthorization = "APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE SEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
$ExpectedExecutionAuthorization = "AUTHORIZE_NY_OSC_SEVENTH_BOUNDED_EXECUTION_ONCE"

$ProtectedGate7Paths = @(
    "scripts/ny_osc_gate7_transient_local.ps1"
    "sources/proposals/ny_osc_owner_name_file_seventh_bounded_attempt_authorization.v1.json"
    "schemas/common/ny_osc_seventh_attempt_authorization_proposal.schema.json"
    "schemas/common/ny_osc_seventh_attempt_transient_local_approval.schema.json"
    "schemas/common/ny_osc_seventh_attempt_transient_pii_approval.schema.json"
    "schemas/common/ny_osc_seventh_fresh_listing_preflight_receipt.schema.json"
    "schemas/common/ny_osc_seventh_execution_authorization.schema.json"
    "schemas/agents/ny_transient_local_execution_authorization_v1_3.schema.json"
    "schemas/agents/ny_transient_local_execution_result_v1_4.schema.json"
    "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_schema_discovery.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_4.py"
)

function Assert-Gate7ProtectedPackage {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RunnerCheckpoint
    )

    if ($RunnerCheckpoint -notmatch '^[0-9a-f]{40}$') {
        throw "Seventh-attempt runner checkpoint is not a 40-character Git SHA. Do not download."
    }

    $InsideWorkTree = (& git -C $RepoRoot rev-parse --is-inside-work-tree 2>$null)
    if ($LASTEXITCODE -ne 0 -or $InsideWorkTree.Trim() -ne "true") {
        throw "Gate 7 must run from the authorized Git working tree. Do not download."
    }

    & git -C $RepoRoot cat-file -e "${RunnerCheckpoint}^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Approved Gate 7 runner checkpoint is not available locally. Do not download."
    }

    foreach ($RelativePath in $ProtectedGate7Paths) {
        $ExpectedBlob = (
            & git -C $RepoRoot rev-parse "${RunnerCheckpoint}:$RelativePath" 2>$null
        )
        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($ExpectedBlob)) {
            throw "Protected Gate 7 path is absent from the approved runner checkpoint. Do not download."
        }
        $ExpectedBlob = $ExpectedBlob.Trim()

        $ActualPath = Join-Path $RepoRoot $RelativePath
        if (-not (Test-Path -LiteralPath $ActualPath -PathType Leaf)) {
            throw "Protected Gate 7 path is missing from the working tree. Do not download."
        }

        $ActualBlob = (& git -C $RepoRoot hash-object -- $ActualPath 2>$null)
        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($ActualBlob)) {
            throw "Unable to hash protected Gate 7 path. Do not download."
        }
        $ActualBlob = $ActualBlob.Trim()

        if ($ActualBlob -ne $ExpectedBlob) {
            throw "Protected Gate 7 package differs from the approved runner checkpoint. Do not download."
        }
    }
}

function Assert-CommonBinding {
    param(
        [Parameter(Mandatory = $true)]
        [object]$Record,
        [Parameter(Mandatory = $true)]
        [string]$Label,
        [Parameter(Mandatory = $true)]
        [string]$RunnerCheckpoint
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
        [Parameter(Mandatory = $true)]
        [object]$Receipt,
        [Parameter(Mandatory = $true)]
        [string]$RunnerCheckpoint
    )

    Assert-CommonBinding -Record $Receipt -Label "Seventh-attempt preflight" -RunnerCheckpoint $RunnerCheckpoint

    if ($Receipt.status -ne "EXACT_MATCH") {
        throw "Seventh-attempt fresh listing preflight is not an exact match. Do not download."
    }
    if ($Receipt.remote_preflight_performed -ne $true) {
        throw "Seventh-attempt fresh listing preflight was not performed. Do not download."
    }
    if (
        [string]::IsNullOrWhiteSpace($Receipt.receipt_ref) -or
        [string]::IsNullOrWhiteSpace($Receipt.preflight_authorization_ref) -or
        [string]::IsNullOrWhiteSpace($Receipt.performed_at_utc)
    ) {
        throw "Seventh-attempt fresh listing preflight refs/timestamp are missing. Do not download."
    }
    if ($Receipt.freshness_window_seconds -ne $ExpectedPreflightFreshnessSeconds) {
        throw "Seventh-attempt fresh listing preflight freshness policy mismatch. Do not download."
    }
    if (
        $Receipt.expected_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.expected_listing.size_display -ne "390.51 MB" -or
        $Receipt.expected_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM" -or
        $Receipt.observed_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.observed_listing.size_display -ne "390.51 MB" -or
        $Receipt.observed_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM"
    ) {
        throw "Seventh-attempt listing metadata is not an exact match. Do not download."
    }
    if (
        $Receipt.download_performed -ne $false -or
        $Receipt.owner_file_opened -ne $false -or
        $Receipt.owner_pii_processed -ne $false -or
        $Receipt.contains_owner_pii -ne $false
    ) {
        throw "Seventh-attempt preflight privacy boundary mismatch. Do not download."
    }

    try {
        $PerformedAt = [DateTimeOffset]::Parse($Receipt.performed_at_utc)
    }
    catch {
        throw "Seventh-attempt preflight timestamp is invalid. Do not download."
    }
    $AgeSeconds = ([DateTimeOffset]::UtcNow - $PerformedAt.ToUniversalTime()).TotalSeconds
    if ($AgeSeconds -lt 0 -or $AgeSeconds -gt $ExpectedPreflightFreshnessSeconds) {
        throw "Seventh-attempt fresh listing preflight is stale or future-dated. Do not download."
    }
}

foreach ($RequiredArtifact in @(
    $LocalApproval,
    $PiiApproval,
    $FreshPreflightReceipt,
    $ExecutionAuthorization
)) {
    if (-not (Test-Path -LiteralPath $RequiredArtifact -PathType Leaf)) {
        throw "Required seventh-attempt authorization artifact is missing. Do not download."
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
    throw "All seventh-attempt single-use approvals must be granted and unconsumed. Do not download."
}

$RunnerCheckpoint = [string]$LocalApprovalRecord.runner_checkpoint
if ([string]::IsNullOrWhiteSpace($RunnerCheckpoint)) {
    throw "Seventh-attempt runner checkpoint is missing. Do not download."
}

Assert-CommonBinding -Record $LocalApprovalRecord -Label "Transient-local approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $PiiApprovalRecord -Label "Transient-PII approval" -RunnerCheckpoint $RunnerCheckpoint
Assert-CommonBinding -Record $ExecutionAuthorizationRecord -Label "Execution authorization" -RunnerCheckpoint $RunnerCheckpoint
Assert-FreshPreflightReceipt -Receipt $FreshPreflightRecord -RunnerCheckpoint $RunnerCheckpoint
Assert-Gate7ProtectedPackage -RunnerCheckpoint $RunnerCheckpoint

if (
    $LocalApprovalRecord.owner_authorization -ne $ExpectedLocalAuthorization -or
    $PiiApprovalRecord.owner_authorization -ne $ExpectedPiiAuthorization -or
    $ExecutionAuthorizationRecord.owner_authorization -ne $ExpectedExecutionAuthorization
) {
    throw "Seventh-attempt human authorization phrase mismatch. Do not download."
}

$Refs = @(
    [string]$LocalApprovalRecord.execution_approval_ref,
    [string]$PiiApprovalRecord.execution_approval_ref,
    [string]$FreshPreflightRecord.receipt_ref,
    [string]$ExecutionAuthorizationRecord.execution_approval_ref
)
if ($Refs | Where-Object { [string]::IsNullOrWhiteSpace($_) }) {
    throw "Seventh-attempt binding ref is missing. Do not download."
}
if (($Refs | Select-Object -Unique).Count -ne 4) {
    throw "Seventh-attempt binding refs must be distinct. Do not download."
}

if (
    $ExecutionAuthorizationRecord.fresh_preflight_receipt_ref -ne $FreshPreflightRecord.receipt_ref -or
    $ExecutionAuthorizationRecord.fresh_preflight_status -ne "EXACT_MATCH" -or
    $ExecutionAuthorizationRecord.download_authority -ne "ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP" -or
    $ExecutionAuthorizationRecord.execution_authority -ne "ONE_BOUND_GATE7_EXECUTION"
) {
    throw "Seventh-attempt explicit execution authorization mismatch. Do not download."
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
    throw "Seventh-attempt local retention scope mismatch. Do not download."
}

if (
    $PiiApprovalRecord.execution_bounds.downloads_max -ne 1 -or
    $PiiApprovalRecord.execution_bounds.retries_max -ne 0 -or
    $PiiApprovalRecord.execution_bounds.max_download_bytes -ne 450000000 -or
    $PiiApprovalRecord.execution_bounds.max_uncompressed_bytes -ne 2000000000 -or
    $PiiApprovalRecord.execution_bounds.max_archive_members -ne 1 -or
    $PiiApprovalRecord.execution_bounds.required_transient_execution_authorization_contract_version -ne "1.3.0" -or
    $PiiApprovalRecord.execution_bounds.required_execution_result_contract_version -ne "1.4.0" -or
    $PiiApprovalRecord.execution_bounds.required_quote_dialect_mode -ne "DOCUMENTED_WIDTH_RAW_LITERAL_POLICY" -or
    $PiiApprovalRecord.execution_bounds.quote_dialect_diagnostic_required_null -ne $true -or
    $PiiApprovalRecord.execution_bounds.automatic_retry_allowed -ne $false
) {
    throw "Seventh-attempt execution bounds mismatch. Do not download."
}

if (
    $PiiApprovalRecord.processing_scope.transient_owner_pii_in_memory_allowed -ne $true -or
    $PiiApprovalRecord.processing_scope.owner_rows_persistence_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.owner_field_decoding_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.owner_field_buffering_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.owner_field_logging_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.row_specific_human_inspection_allowed -ne $false -or
    $PiiApprovalRecord.processing_scope.derived_non_pii_schema_metadata_persistence_allowed -ne $true -or
    $PiiApprovalRecord.processing_scope.structural_diagnostic_persistence_allowed -ne $true -or
    $PiiApprovalRecord.processing_scope.quote_dialect_diagnostic_persistence_allowed -ne $false
) {
    throw "Seventh-attempt processing scope mismatch. Do not download."
}

if (
    $ExecutionAuthorizationRecord.authorization_scope.manual_download_allowed -ne $true -or
    $ExecutionAuthorizationRecord.authorization_scope.direct_network_client_allowed -ne $false -or
    $ExecutionAuthorizationRecord.authorization_scope.downloads_max -ne 1 -or
    $ExecutionAuthorizationRecord.authorization_scope.gate7_executions_max -ne 1 -or
    $ExecutionAuthorizationRecord.authorization_scope.retries_max -ne 0
) {
    throw "Seventh-attempt execution authorization scope mismatch. Do not download."
}

$TempDir = Join-Path $env:TEMP (
    "unclaimed-ny-osc-gate2-seventh-" + [guid]::NewGuid().ToString("N")
)
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC seventh bounded attempt"
    Write-Host "All four machine-bound grants are verified."
    Write-Host "Fresh listing receipt: EXACT_MATCH and within 900 seconds."
    Write-Host "The execution authorization permits exactly one manual download."
    Write-Host "Save FINDERS.zip directly into:"
    Write-Host $TempDir
    Write-Host ""
    Read-Host "Press Enter only after the separately authorized single manual download finishes"

    if (-not (Test-Path -LiteralPath $Archive -PathType Leaf)) {
        throw "FINDERS.zip not found in the dedicated seventh-attempt temp directory."
    }

    Push-Location $RepoRoot
    try {
        $PythonCode = @'
from pathlib import Path
import sys
from unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_4 import (
    build_real_execution_authorization_v1_3,
    execute_transient_local_file_discovery_v1_4,
)
authorization = build_real_execution_authorization_v1_3(
    Path(sys.argv[2]),
    Path(sys.argv[3]),
    Path(sys.argv[4]),
    Path(sys.argv[5]),
    expected_runner_checkpoint=sys.argv[6],
)
result = execute_transient_local_file_discovery_v1_4(
    authorization,
    Path(sys.argv[1]),
)
print(result.model_dump_json())
raise SystemExit(0 if result.status == "DISCOVERED" else 2)
'@
        python -c $PythonCode $Archive $LocalApproval $PiiApproval $FreshPreflightReceipt $ExecutionAuthorization $RunnerCheckpoint

        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC seventh bounded attempt stopped fail-closed."
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
