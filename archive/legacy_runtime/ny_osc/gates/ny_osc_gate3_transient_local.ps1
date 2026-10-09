param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_third_attempt_transient_local_approval.v1.json"
$Gate2Approval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_third_attempt_transient_pii_approval.v1.json"
$ExpectedLocalAuthorization = "APPROVO NY OSC THIRD TRANSIENT LOCAL FILE BOUNDED ONCE"
$ExpectedPiiAuthorization = "APPROVO NY OSC OWNER NAME FILE THIRD BOUNDED TRANSIENT PII ATTEMPT ONCE"

if (-not (Test-Path $LocalApproval)) {
    throw "Third-attempt transient-local approval is missing. Do not download."
}
if (-not (Test-Path $Gate2Approval)) {
    throw "Third-attempt transient-PII approval is missing. Do not download."
}

$LocalApprovalRecord = Get-Content -LiteralPath $LocalApproval -Raw | ConvertFrom-Json
$Gate2ApprovalRecord = Get-Content -LiteralPath $Gate2Approval -Raw | ConvertFrom-Json

if ($LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Third-attempt transient-local approval is not granted. Do not download."
}
if ($Gate2ApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Third-attempt transient-PII approval is not granted. Do not download."
}
if ($LocalApprovalRecord.attempt_number -ne 3 -or $Gate2ApprovalRecord.attempt_number -ne 3) {
    throw "Third-attempt approval number mismatch. Do not download."
}
if ($LocalApprovalRecord.owner_authorization -ne $ExpectedLocalAuthorization) {
    throw "Third-attempt transient-local authorization phrase mismatch. Do not download."
}
if ($Gate2ApprovalRecord.owner_authorization -ne $ExpectedPiiAuthorization) {
    throw "Third-attempt transient-PII authorization phrase mismatch. Do not download."
}
if ($LocalApprovalRecord.single_use -ne $true -or $LocalApprovalRecord.reusable -ne $false) {
    throw "Third-attempt transient-local reuse policy mismatch. Do not download."
}
if ($Gate2ApprovalRecord.single_use -ne $true -or $Gate2ApprovalRecord.reusable -ne $false) {
    throw "Third-attempt transient-PII reuse policy mismatch. Do not download."
}
if ($LocalApprovalRecord.retry_authorized -ne $false -or $Gate2ApprovalRecord.retry_authorized -ne $false) {
    throw "Third-attempt retry policy mismatch. Do not download."
}
if ($LocalApprovalRecord.runner_ci_conclusion -ne "SUCCESS") {
    throw "Third-attempt transient-local runner CI is not verified. Do not download."
}
if ($Gate2ApprovalRecord.runner_ci_conclusion -ne "SUCCESS") {
    throw "Third-attempt transient-PII runner CI is not verified. Do not download."
}

$TempDir = Join-Path $env:TEMP ("unclaimed-ny-osc-gate2-third-" + [guid]::NewGuid().ToString("N"))
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC third bounded attempt"
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
        throw "FINDERS.zip not found in the dedicated third-attempt temp directory."
    }

    Push-Location $RepoRoot
    try {
        python -m unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution --archive $Archive --local-approval $LocalApproval --gate2-approval $Gate2Approval --expected-attempt-number 3
        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC third bounded attempt stopped fail-closed."
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
