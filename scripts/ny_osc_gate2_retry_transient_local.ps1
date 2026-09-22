param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_second_attempt_transient_local_approval.v1.json"
$Gate2Approval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_second_attempt_transient_pii_approval.v1.json"

if (-not (Test-Path $LocalApproval)) {
    throw "Second-attempt transient-local approval is missing. Do not download."
}
if (-not (Test-Path $Gate2Approval)) {
    throw "Second-attempt transient-PII approval is missing. Do not download."
}

$LocalApprovalRecord = Get-Content -LiteralPath $LocalApproval -Raw | ConvertFrom-Json
$Gate2ApprovalRecord = Get-Content -LiteralPath $Gate2Approval -Raw | ConvertFrom-Json

if ($LocalApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Second-attempt transient-local approval is consumed or unavailable. Do not download."
}
if ($Gate2ApprovalRecord.status -ne "GRANTED_NOT_CONSUMED") {
    throw "Second-attempt transient-PII approval is consumed or unavailable. Do not download."
}

$TempDir = Join-Path $env:TEMP ("unclaimed-ny-osc-gate2-retry-" + [guid]::NewGuid().ToString("N"))
$Archive = Join-Path $TempDir "FINDERS.zip"
New-Item -ItemType Directory -Path $TempDir | Out-Null
Set-Clipboard -Value $TempDir
Start-Process explorer.exe $TempDir

try {
    Write-Host ""
    Write-Host "NY OSC second bounded attempt"
    Write-Host "Before downloading, verify the secure-transfer listing."
    Write-Host "If unchanged, it should still show:"
    Write-Host "  Name: FINDERS.zip"
    Write-Host "  Size: 390.51 MB"
    Write-Host "  Last modified: 9/16/2026, 1:33:31 PM"
    Write-Host ""
    Write-Host "If any value differs, STOP and report the new values. Do not download."
    Write-Host "If all values match, save FINDERS.zip directly into:"
    Write-Host $TempDir
    Write-Host ""
    Read-Host "Press Enter only after the authorized single download finishes"

    if (-not (Test-Path $Archive)) {
        throw "FINDERS.zip not found in the dedicated retry temp directory."
    }

    Push-Location $RepoRoot
    try {
        python -m unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution --archive $Archive --local-approval $LocalApproval --gate2-approval $Gate2Approval --expected-attempt-number 2
        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC second bounded attempt stopped fail-closed."
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
