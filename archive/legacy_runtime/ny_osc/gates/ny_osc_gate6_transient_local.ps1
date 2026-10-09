param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_sixth_attempt_transient_local_approval.v1.json"
$Gate2Approval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_sixth_attempt_transient_pii_approval.v1.json"
$FreshPreflightReceipt = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_sixth_fresh_listing_preflight_receipt.v1.json"

$ExpectedProposalRef = "sources/proposals/ny_osc_owner_name_file_sixth_bounded_attempt_authorization.v1.json"
$ExpectedProposalCheckpoint = "ac5a84a9523c5e99c79f41d0203f349e41be56c7"
$ExpectedProposalCiRunId = 35531762748
$ExpectedLocalAuthorization = "APPROVO NY OSC SIXTH TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE SIXTH BOUNDED TRANSIENT PII ATTEMPT ONCE"
$ExpectedPreflightFreshnessSeconds = 900

$ProtectedGate6Paths = @(
    "scripts/ny_osc_gate6_transient_local.ps1"
    "sources/proposals/ny_osc_owner_name_file_sixth_bounded_attempt_authorization.v1.json"
    "schemas/common/ny_osc_sixth_attempt_authorization_proposal.schema.json"
    "schemas/common/ny_osc_sixth_attempt_transient_local_approval.schema.json"
    "schemas/common/ny_osc_sixth_attempt_transient_pii_approval.schema.json"
    "schemas/common/ny_osc_sixth_fresh_listing_preflight_receipt.schema.json"
    "schemas/agents/ny_transient_local_execution_authorization_v1_1.schema.json"
    "schemas/agents/ny_transient_local_execution_result_v1_2.schema.json"
    "schemas/agents/ny_owner_name_structural_diagnostic_result.schema.json"
    "schemas/agents/ny_owner_name_quote_dialect_diagnostic_result.schema.json"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_schema_discovery.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution.py"
    "src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_2.py"
)

function Assert-Gate6ProtectedPackage {
    param(
        [Parameter(Mandatory = $true)]
        [string]$RunnerCheckpoint
    )

    if ($RunnerCheckpoint -notmatch '^[0-9a-f]{40}$') {
        throw "Sixth-attempt runner checkpoint is not a 40-character Git SHA. Do not download."
    }

    $InsideWorkTree = (& git -C $RepoRoot rev-parse --is-inside-work-tree 2>$null)
    if ($LASTEXITCODE -ne 0 -or $InsideWorkTree.Trim() -ne "true") {
        throw "Gate 6 must run from the authorized Git working tree. Do not download."
    }

    & git -C $RepoRoot cat-file -e "${RunnerCheckpoint}^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Approved Gate 6 runner checkpoint is not available locally. Do not download."
    }

    foreach ($RelativePath in $ProtectedGate6Paths) {
        $ExpectedBlob = (
            & git -C $RepoRoot rev-parse "${RunnerCheckpoint}:$RelativePath" 2>$null
        )
        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($ExpectedBlob)) {
            throw "Protected Gate 6 path is absent from the approved runner checkpoint. Do not download."
        }
        $ExpectedBlob = $ExpectedBlob.Trim()

        $ActualPath = Join-Path $RepoRoot $RelativePath
        if (-not (Test-Path -LiteralPath $ActualPath -PathType Leaf)) {
            throw "Protected Gate 6 path is missing from the working tree. Do not download."
        }

        $ActualBlob = (& git -C $RepoRoot hash-object -- $ActualPath 2>$null)
        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($ActualBlob)) {
            throw "Unable to hash protected Gate 6 path. Do not download."
        }
        $ActualBlob = $ActualBlob.Trim()

        if ($ActualBlob -ne $ExpectedBlob) {
            throw "Protected Gate 6 package differs from the approved runner checkpoint. Do not download."
        }
    }
}

function Assert-FreshPreflightReceipt {
    param(
        [Parameter(Mandatory = $true)]
        [object]$Receipt,
        [Parameter(Mandatory = $true)]
        [string]$RunnerCheckpoint
    )

    if ($Receipt.status -ne "EXACT_MATCH") {
        throw "Sixth-attempt fresh listing preflight is not an exact match. Do not download."
    }
    if ($Receipt.remote_preflight_performed -ne $true) {
        throw "Sixth-attempt fresh listing preflight was not performed. Do not download."
    }
    if (
        [string]::IsNullOrWhiteSpace($Receipt.preflight_authorization_ref) -or
        [string]::IsNullOrWhiteSpace($Receipt.performed_at_utc)
    ) {
        throw "Sixth-attempt fresh listing preflight authorization/timestamp is missing. Do not download."
    }
    if (
        $Receipt.attempt_number -ne 6 -or
        $Receipt.source_id -ne "ny.osc.unclaimed_funds.owner_name_file" -or
        $Receipt.proposal_ref -ne $ExpectedProposalRef -or
        $Receipt.proposal_checkpoint -ne $ExpectedProposalCheckpoint -or
        $Receipt.proposal_ci_run_id -ne $ExpectedProposalCiRunId -or
        $Receipt.runner_checkpoint -ne $RunnerCheckpoint
    ) {
        throw "Sixth-attempt fresh listing preflight binding mismatch. Do not download."
    }
    if ($Receipt.freshness_window_seconds -ne $ExpectedPreflightFreshnessSeconds) {
        throw "Sixth-attempt fresh listing preflight freshness policy mismatch. Do not download."
    }
    if (
        $Receipt.expected_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.expected_listing.size_display -ne "390.51 MB" -or
        $Receipt.expected_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM" -or
        $Receipt.observed_listing.remote_name -ne "FINDERS.zip" -or
        $Receipt.observed_listing.size_display -ne "390.51 MB" -or
        $Receipt.observed_listing.last_modified_display -ne "9/16/2026, 1:33:31 PM"
    ) {
        throw "Sixth-attempt fresh listing metadata is not an exact match. Do not download."
    }
    if (
        $Receipt.download_performed -ne $false -or
        $Receipt.owner_file_opened -ne $false -or
        $Receipt.owner_pii_processed -ne $false -or
        $Receipt.contains_owner_pii -ne $false
    ) {
        throw "Sixth-attempt fresh listing receipt scope mismatch. Do not download."
    }

    if ([string]$Receipt.performed_at_utc -notmatch 'Z$') {
        throw "Sixth-attempt fresh listing timestamp must be UTC. Do not download."
    }
    try {
        $PerformedAt = [DateTimeOffset]::Parse(
            [string]$Receipt.performed_at_utc,
            [System.Globalization.CultureInfo]::InvariantCulture,
            [System.Globalization.DateTimeStyles]::AssumeUniversal
        ).ToUniversalTime()
    }
    catch {
        throw "Sixth-attempt fresh listing timestamp is invalid. Do not download."
    }

    $AgeSeconds = ([DateTimeOffset]::UtcNow - $PerformedAt).TotalSeconds
    if ($AgeSeconds -lt 0 -or $AgeSeconds -gt $ExpectedPreflightFreshnessSeconds) {
        throw "Sixth-attempt fresh listing preflight is stale or future-dated. Do not download."
    }
}

if (-not (Test-Path $LocalApproval)) {
    throw "Sixth-attempt transient-local approval is missing. Do not download."
}
if (-not (Test-Path $Gate2Approval)) {
    throw "Sixth-attempt transient-PII approval is missing. Do not download."
}
if (-not (Test-Path $FreshPreflightReceipt)) {
    throw "Sixth-attempt fresh listing preflight receipt is missing. Do not download."
}

$LocalApprovalRecord = Get-Content -LiteralPath $LocalApproval -Raw | ConvertFrom-Json
$Gate2ApprovalRecord = Get-Content -LiteralPath $Gate2Approval -Raw | ConvertFrom-Json
$FreshPreflightRecord = Get-Content -LiteralPath $FreshPreflightReceipt -Raw | ConvertFrom-Json

if ($LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Sixth-attempt transient-local approval is not granted. Do not download."
}
if ($Gate2ApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Sixth-attempt transient-PII approval is not granted. Do not download."
}
if (
    $LocalApprovalRecord.attempt_number -ne 6 -or
    $Gate2ApprovalRecord.attempt_number -ne 6
) {
    throw "Sixth-attempt approval number mismatch. Do not download."
}
if (
    $LocalApprovalRecord.proposal_ref -ne $ExpectedProposalRef -or
    $Gate2ApprovalRecord.proposal_ref -ne $ExpectedProposalRef
) {
    throw "Sixth-attempt proposal reference mismatch. Do not download."
}
if (
    $LocalApprovalRecord.proposal_checkpoint -ne $ExpectedProposalCheckpoint -or
    $Gate2ApprovalRecord.proposal_checkpoint -ne $ExpectedProposalCheckpoint
) {
    throw "Sixth-attempt proposal checkpoint mismatch. Do not download."
}
if (
    $LocalApprovalRecord.proposal_ci_run_id -ne $ExpectedProposalCiRunId -or
    $Gate2ApprovalRecord.proposal_ci_run_id -ne $ExpectedProposalCiRunId
) {
    throw "Sixth-attempt proposal CI binding mismatch. Do not download."
}
if ($LocalApprovalRecord.owner_authorization -ne $ExpectedLocalAuthorization) {
    throw "Sixth-attempt transient-local authorization phrase mismatch. Do not download."
}
if ($Gate2ApprovalRecord.owner_authorization -ne $ExpectedPiiAuthorization) {
    throw "Sixth-attempt transient-PII authorization phrase mismatch. Do not download."
}
if (
    $LocalApprovalRecord.single_use -ne $true -or
    $LocalApprovalRecord.reusable -ne $false -or
    $Gate2ApprovalRecord.single_use -ne $true -or
    $Gate2ApprovalRecord.reusable -ne $false
) {
    throw "Sixth-attempt reuse policy mismatch. Do not download."
}
if (
    $LocalApprovalRecord.retry_authorized -ne $false -or
    $Gate2ApprovalRecord.retry_authorized -ne $false
) {
    throw "Sixth-attempt retry policy mismatch. Do not download."
}
if (
    [string]::IsNullOrWhiteSpace($LocalApprovalRecord.execution_approval_ref) -or
    [string]::IsNullOrWhiteSpace($Gate2ApprovalRecord.execution_approval_ref)
) {
    throw "Sixth-attempt approval reference is missing. Do not download."
}
if (
    $LocalApprovalRecord.execution_approval_ref -eq
    $Gate2ApprovalRecord.execution_approval_ref
) {
    throw "Sixth-attempt approval references must be distinct. Do not download."
}
if (
    [string]::IsNullOrWhiteSpace($LocalApprovalRecord.runner_checkpoint) -or
    $LocalApprovalRecord.runner_checkpoint -ne $Gate2ApprovalRecord.runner_checkpoint
) {
    throw "Sixth-attempt runner checkpoint mismatch. Do not download."
}
if ($LocalApprovalRecord.runner_checkpoint -notmatch '^[0-9a-f]{40}$') {
    throw "Sixth-attempt runner checkpoint format mismatch. Do not download."
}
if (
    $LocalApprovalRecord.runner_ci_run_id -le 0 -or
    $LocalApprovalRecord.runner_ci_run_id -ne $Gate2ApprovalRecord.runner_ci_run_id
) {
    throw "Sixth-attempt runner CI binding mismatch. Do not download."
}
if (
    $LocalApprovalRecord.runner_ci_conclusion -ne "SUCCESS" -or
    $Gate2ApprovalRecord.runner_ci_conclusion -ne "SUCCESS"
) {
    throw "Sixth-attempt runner CI is not verified. Do not download."
}

$RunnerCheckpoint = [string]$LocalApprovalRecord.runner_checkpoint

Assert-Gate6ProtectedPackage -RunnerCheckpoint $RunnerCheckpoint
Assert-FreshPreflightReceipt `
    -Receipt $FreshPreflightRecord `
    -RunnerCheckpoint $RunnerCheckpoint

if (
    $LocalApprovalRecord.scope.expected_local_filename -ne "FINDERS.zip" -or
    $LocalApprovalRecord.scope.max_download_bytes -ne 450000000 -or
    $LocalApprovalRecord.scope.dedicated_os_temp_directory_required -ne $true -or
    $LocalApprovalRecord.scope.immediate_logical_deletion_required -ne $true -or
    $LocalApprovalRecord.scope.durable_raw_persistence_allowed -ne $false -or
    $LocalApprovalRecord.scope.repository_persistence_allowed -ne $false -or
    $LocalApprovalRecord.scope.cloud_sync_allowed -ne $false -or
    $LocalApprovalRecord.scope.chat_upload_allowed -ne $false -or
    $LocalApprovalRecord.scope.physical_secure_erasure_guaranteed -ne $false
) {
    throw "Sixth-attempt local retention scope mismatch. Do not download."
}

if (
    $Gate2ApprovalRecord.execution_bounds.downloads_max -ne 1 -or
    $Gate2ApprovalRecord.execution_bounds.retries_max -ne 0 -or
    $Gate2ApprovalRecord.execution_bounds.max_download_bytes -ne 450000000 -or
    $Gate2ApprovalRecord.execution_bounds.max_uncompressed_bytes -ne 2000000000 -or
    $Gate2ApprovalRecord.execution_bounds.max_archive_members -ne 1 -or
    $Gate2ApprovalRecord.execution_bounds.text_members_required_exactly -ne 1 -or
    $Gate2ApprovalRecord.execution_bounds.expected_delimiter -ne "|" -or
    $Gate2ApprovalRecord.execution_bounds.expected_documented_field_count -ne 14 -or
    $Gate2ApprovalRecord.execution_bounds.parser_chunk_bytes -ne 65536 -or
    $Gate2ApprovalRecord.execution_bounds.required_transient_execution_authorization_contract_version -ne "1.1.0" -or
    $Gate2ApprovalRecord.execution_bounds.required_execution_result_contract_version -ne "1.2.0" -or
    $Gate2ApprovalRecord.execution_bounds.required_quote_dialect_mode -ne "LINE_LOCAL_ARBITRATION" -or
    $Gate2ApprovalRecord.execution_bounds.required_structural_diagnostic_contract_version -ne "1.0.0" -or
    $Gate2ApprovalRecord.execution_bounds.required_quote_dialect_diagnostic_contract_version -ne "1.0.0" -or
    $Gate2ApprovalRecord.execution_bounds.automatic_widening_allowed -ne $false -or
    $Gate2ApprovalRecord.execution_bounds.automatic_retry_allowed -ne $false
) {
    throw "Sixth-attempt execution bounds mismatch. Do not download."
}

if (
    $Gate2ApprovalRecord.processing_scope.transient_owner_pii_in_memory_allowed -ne $true -or
    $Gate2ApprovalRecord.processing_scope.owner_rows_persistence_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.owner_field_decoding_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.owner_field_buffering_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.owner_field_logging_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.row_specific_human_inspection_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.derived_non_pii_schema_metadata_persistence_allowed -ne $true -or
    $Gate2ApprovalRecord.processing_scope.structural_diagnostic_persistence_allowed -ne $true -or
    $Gate2ApprovalRecord.processing_scope.quote_dialect_diagnostic_persistence_allowed -ne $true
) {
    throw "Sixth-attempt processing scope mismatch. Do not download."
}

$TempDir = Join-Path $env:TEMP (
    "unclaimed-ny-osc-gate2-sixth-" + [guid]::NewGuid().ToString("N")
)
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC sixth bounded attempt"
    Write-Host "Fresh listing receipt: EXACT_MATCH and machine-verified."
    Write-Host "Save the separately authorized single FINDERS.zip download directly into:"
    Write-Host $TempDir
    Write-Host ""
    Read-Host "Press Enter only after the separately authorized single download finishes"

    if (-not (Test-Path $Archive)) {
        throw "FINDERS.zip not found in the dedicated sixth-attempt temp directory."
    }

    Push-Location $RepoRoot
    try {
        python -m unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution_v1_2 `
            --archive $Archive `
            --local-approval $LocalApproval `
            --gate2-approval $Gate2Approval `
            --expected-attempt-number 6
        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC sixth bounded attempt stopped fail-closed."
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
