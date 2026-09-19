param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_fourth_attempt_transient_local_approval.v1.json"
$Gate2Approval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_fourth_attempt_transient_pii_approval.v1.json"
$ExpectedProposalRef = "sources/proposals/ny_osc_owner_name_file_fourth_bounded_attempt_authorization.v1.json"
$ExpectedLocalAuthorization = "APPROVO NY OSC FOURTH TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE FOURTH BOUNDED TRANSIENT PII ATTEMPT ONCE"

if (-not (Test-Path $LocalApproval)) {
    throw "Fourth-attempt transient-local approval is missing. Do not download."
}
if (-not (Test-Path $Gate2Approval)) {
    throw "Fourth-attempt transient-PII approval is missing. Do not download."
}

$LocalApprovalRecord = Get-Content -LiteralPath $LocalApproval -Raw | ConvertFrom-Json
$Gate2ApprovalRecord = Get-Content -LiteralPath $Gate2Approval -Raw | ConvertFrom-Json

if ($LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Fourth-attempt transient-local approval is not granted. Do not download."
}
if ($Gate2ApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Fourth-attempt transient-PII approval is not granted. Do not download."
}
if ($LocalApprovalRecord.attempt_number -ne 4 -or $Gate2ApprovalRecord.attempt_number -ne 4) {
    throw "Fourth-attempt approval number mismatch. Do not download."
}
if ($LocalApprovalRecord.proposal_ref -ne $ExpectedProposalRef -or $Gate2ApprovalRecord.proposal_ref -ne $ExpectedProposalRef) {
    throw "Fourth-attempt proposal binding mismatch. Do not download."
}
if ($LocalApprovalRecord.owner_authorization -ne $ExpectedLocalAuthorization) {
    throw "Fourth-attempt transient-local authorization phrase mismatch. Do not download."
}
if ($Gate2ApprovalRecord.owner_authorization -ne $ExpectedPiiAuthorization) {
    throw "Fourth-attempt transient-PII authorization phrase mismatch. Do not download."
}
if ($LocalApprovalRecord.single_use -ne $true -or $LocalApprovalRecord.reusable -ne $false) {
    throw "Fourth-attempt transient-local reuse policy mismatch. Do not download."
}
if ($Gate2ApprovalRecord.single_use -ne $true -or $Gate2ApprovalRecord.reusable -ne $false) {
    throw "Fourth-attempt transient-PII reuse policy mismatch. Do not download."
}
if ($LocalApprovalRecord.retry_authorized -ne $false -or $Gate2ApprovalRecord.retry_authorized -ne $false) {
    throw "Fourth-attempt retry policy mismatch. Do not download."
}
if ([string]::IsNullOrWhiteSpace($LocalApprovalRecord.execution_approval_ref) -or [string]::IsNullOrWhiteSpace($Gate2ApprovalRecord.execution_approval_ref)) {
    throw "Fourth-attempt approval reference is missing. Do not download."
}
if ($LocalApprovalRecord.execution_approval_ref -eq $Gate2ApprovalRecord.execution_approval_ref) {
    throw "Fourth-attempt approval references must be distinct. Do not download."
}
if ([string]::IsNullOrWhiteSpace($LocalApprovalRecord.runner_checkpoint) -or $LocalApprovalRecord.runner_checkpoint -ne $Gate2ApprovalRecord.runner_checkpoint) {
    throw "Fourth-attempt runner checkpoint mismatch. Do not download."
}
if ($LocalApprovalRecord.runner_ci_run_id -le 0 -or $LocalApprovalRecord.runner_ci_run_id -ne $Gate2ApprovalRecord.runner_ci_run_id) {
    throw "Fourth-attempt runner CI binding mismatch. Do not download."
}
if ($LocalApprovalRecord.runner_ci_conclusion -ne "SUCCESS" -or $Gate2ApprovalRecord.runner_ci_conclusion -ne "SUCCESS") {
    throw "Fourth-attempt runner CI is not verified. Do not download."
}
if ($LocalApprovalRecord.scope.max_download_bytes -ne 450000000) {
    throw "Fourth-attempt local byte bound mismatch. Do not download."
}
if (
    $Gate2ApprovalRecord.execution_bounds.downloads_max -ne 1 -or
    $Gate2ApprovalRecord.execution_bounds.retries_max -ne 0 -or
    $Gate2ApprovalRecord.execution_bounds.max_download_bytes -ne 450000000 -or
    $Gate2ApprovalRecord.execution_bounds.max_uncompressed_bytes -ne 2000000000 -or
    $Gate2ApprovalRecord.execution_bounds.max_archive_members -ne 1 -or
    $Gate2ApprovalRecord.execution_bounds.text_members_required_exactly -ne 1 -or
    $Gate2ApprovalRecord.execution_bounds.expected_documented_field_count -ne 14 -or
    $Gate2ApprovalRecord.execution_bounds.parser_chunk_bytes -ne 65536 -or
    $Gate2ApprovalRecord.execution_bounds.automatic_widening_allowed -ne $false -or
    $Gate2ApprovalRecord.execution_bounds.automatic_retry_allowed -ne $false
) {
    throw "Fourth-attempt execution bounds mismatch. Do not download."
}

$TempDir = Join-Path $env:TEMP ("unclaimed-ny-osc-gate2-fourth-" + [guid]::NewGuid().ToString("N"))
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC fourth bounded attempt"
    Write-Host "Before downloading, perform the separately authorized fresh listing preflight."
    Write-Host "Historical comparison values only:"
    Write-Host "  Name: FINDERS.zip"
    Write-Host "  Size: 390.51 MB"
    Write-Host "  Last modified: 9/16/2026, 1:33:31 PM"
    Write-Host ""
    Write-Host "If any value differs, STOP and report the new values. Do not download."
    Write-Host "If all values match, save FINDERS.zip directly into:"
    Write-Host $TempDir
    Write-Host ""
    Read-Host "Press Enter only after the separately authorized single download finishes"

    if (-not (Test-Path $Archive)) {
        throw "FINDERS.zip not found in the dedicated fourth-attempt temp directory."
    }

    Push-Location $RepoRoot
    try {
        python -m unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution --archive $Archive --local-approval $LocalApproval --gate2-approval $Gate2Approval --expected-attempt-number 4
        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC fourth bounded attempt stopped fail-closed."
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
