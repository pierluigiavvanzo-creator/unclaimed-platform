param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_fifth_attempt_transient_local_approval.v1.json"
$Gate2Approval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_fifth_attempt_transient_pii_approval.v1.json"
$ExpectedProposalRef = "sources/proposals/ny_osc_owner_name_file_fifth_bounded_attempt_authorization.v1.json"
$ExpectedProposalCheckpoint = "8ce856ddbeac5d2300f808729a887803e212b240"
$ExpectedProposalCiRunId = 35460348569
$ExpectedLocalAuthorization = "APPROVO NY OSC FIFTH TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE FIFTH BOUNDED TRANSIENT PII ATTEMPT ONCE"

if (-not (Test-Path $LocalApproval)) {
    throw "Fifth-attempt transient-local approval is missing. Do not download."
}
if (-not (Test-Path $Gate2Approval)) {
    throw "Fifth-attempt transient-PII approval is missing. Do not download."
}

$LocalApprovalRecord = Get-Content -LiteralPath $LocalApproval -Raw | ConvertFrom-Json
$Gate2ApprovalRecord = Get-Content -LiteralPath $Gate2Approval -Raw | ConvertFrom-Json

if ($LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Fifth-attempt transient-local approval is not granted. Do not download."
}
if ($Gate2ApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Fifth-attempt transient-PII approval is not granted. Do not download."
}
if ($LocalApprovalRecord.attempt_number -ne 5 -or $Gate2ApprovalRecord.attempt_number -ne 5) {
    throw "Fifth-attempt approval number mismatch. Do not download."
}
if ($LocalApprovalRecord.proposal_ref -ne $ExpectedProposalRef -or $Gate2ApprovalRecord.proposal_ref -ne $ExpectedProposalRef) {
    throw "Fifth-attempt proposal binding mismatch. Do not download."
}
if ($LocalApprovalRecord.proposal_checkpoint -ne $ExpectedProposalCheckpoint -or $Gate2ApprovalRecord.proposal_checkpoint -ne $ExpectedProposalCheckpoint) {
    throw "Fifth-attempt proposal checkpoint mismatch. Do not download."
}
if ($LocalApprovalRecord.proposal_ci_run_id -ne $ExpectedProposalCiRunId -or $Gate2ApprovalRecord.proposal_ci_run_id -ne $ExpectedProposalCiRunId) {
    throw "Fifth-attempt proposal CI binding mismatch. Do not download."
}
if ($LocalApprovalRecord.owner_authorization -ne $ExpectedLocalAuthorization) {
    throw "Fifth-attempt transient-local authorization phrase mismatch. Do not download."
}
if ($Gate2ApprovalRecord.owner_authorization -ne $ExpectedPiiAuthorization) {
    throw "Fifth-attempt transient-PII authorization phrase mismatch. Do not download."
}
if ($LocalApprovalRecord.single_use -ne $true -or $LocalApprovalRecord.reusable -ne $false) {
    throw "Fifth-attempt transient-local reuse policy mismatch. Do not download."
}
if ($Gate2ApprovalRecord.single_use -ne $true -or $Gate2ApprovalRecord.reusable -ne $false) {
    throw "Fifth-attempt transient-PII reuse policy mismatch. Do not download."
}
if ($LocalApprovalRecord.retry_authorized -ne $false -or $Gate2ApprovalRecord.retry_authorized -ne $false) {
    throw "Fifth-attempt retry policy mismatch. Do not download."
}
if ([string]::IsNullOrWhiteSpace($LocalApprovalRecord.execution_approval_ref) -or [string]::IsNullOrWhiteSpace($Gate2ApprovalRecord.execution_approval_ref)) {
    throw "Fifth-attempt approval reference is missing. Do not download."
}
if ($LocalApprovalRecord.execution_approval_ref -eq $Gate2ApprovalRecord.execution_approval_ref) {
    throw "Fifth-attempt approval references must be distinct. Do not download."
}
if ([string]::IsNullOrWhiteSpace($LocalApprovalRecord.runner_checkpoint) -or $LocalApprovalRecord.runner_checkpoint -ne $Gate2ApprovalRecord.runner_checkpoint) {
    throw "Fifth-attempt runner checkpoint mismatch. Do not download."
}
if ($LocalApprovalRecord.runner_ci_run_id -le 0 -or $LocalApprovalRecord.runner_ci_run_id -ne $Gate2ApprovalRecord.runner_ci_run_id) {
    throw "Fifth-attempt runner CI binding mismatch. Do not download."
}
if ($LocalApprovalRecord.runner_ci_conclusion -ne "SUCCESS" -or $Gate2ApprovalRecord.runner_ci_conclusion -ne "SUCCESS") {
    throw "Fifth-attempt runner CI is not verified. Do not download."
}
if ($LocalApprovalRecord.scope.expected_local_filename -ne "FINDERS.zip") {
    throw "Fifth-attempt local filename mismatch. Do not download."
}
if (
    $LocalApprovalRecord.scope.max_download_bytes -ne 450000000 -or
    $LocalApprovalRecord.scope.dedicated_os_temp_directory_required -ne $true -or
    $LocalApprovalRecord.scope.immediate_logical_deletion_required -ne $true -or
    $LocalApprovalRecord.scope.durable_raw_persistence_allowed -ne $false -or
    $LocalApprovalRecord.scope.repository_persistence_allowed -ne $false -or
    $LocalApprovalRecord.scope.cloud_sync_allowed -ne $false -or
    $LocalApprovalRecord.scope.chat_upload_allowed -ne $false -or
    $LocalApprovalRecord.scope.physical_secure_erasure_guaranteed -ne $false
) {
    throw "Fifth-attempt local retention scope mismatch. Do not download."
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
    $Gate2ApprovalRecord.execution_bounds.required_execution_result_contract_version -ne "1.1.0" -or
    $Gate2ApprovalRecord.execution_bounds.required_structural_diagnostic_contract_version -ne "1.0.0" -or
    $Gate2ApprovalRecord.execution_bounds.automatic_widening_allowed -ne $false -or
    $Gate2ApprovalRecord.execution_bounds.automatic_retry_allowed -ne $false
) {
    throw "Fifth-attempt execution bounds mismatch. Do not download."
}

if (
    $Gate2ApprovalRecord.processing_scope.transient_owner_pii_in_memory_allowed -ne $true -or
    $Gate2ApprovalRecord.processing_scope.owner_rows_persistence_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.owner_field_decoding_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.owner_field_buffering_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.owner_field_logging_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.row_specific_human_inspection_allowed -ne $false -or
    $Gate2ApprovalRecord.processing_scope.derived_non_pii_schema_metadata_persistence_allowed -ne $true -or
    $Gate2ApprovalRecord.processing_scope.structural_diagnostic_persistence_allowed -ne $true
) {
    throw "Fifth-attempt processing scope mismatch. Do not download."
}

$TempDir = Join-Path $env:TEMP ("unclaimed-ny-osc-gate2-fifth-" + [guid]::NewGuid().ToString("N"))
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC fifth bounded attempt"
    Write-Host "Before downloading, perform the separately authorized fresh listing preflight."
    Write-Host "Historical comparison values only:"
    Write-Host "  Name: FINDERS.zip"
    Write-Host "  Size: 390.51 MB"
    Write-Host "  Last modified: 9/16/2026, 1:33:31 PM"
    Write-Host ""
    Write-Host "If any value differs, STOP and refresh the proposal. Do not download."
    Write-Host "If all values match, save FINDERS.zip directly into:"
    Write-Host $TempDir
    Write-Host ""
    Read-Host "Press Enter only after the separately authorized single download finishes"

    if (-not (Test-Path $Archive)) {
        throw "FINDERS.zip not found in the dedicated fifth-attempt temp directory."
    }

    Push-Location $RepoRoot
    try {
        python -m unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution --archive $Archive --local-approval $LocalApproval --gate2-approval $Gate2Approval --expected-attempt-number 5
        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC fifth bounded attempt stopped fail-closed."
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
