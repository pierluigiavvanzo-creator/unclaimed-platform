param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$LocalApproval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_transient_local_file_approval.v1.json"
$Gate2Approval = Join-Path $RepoRoot "sources\evidence\ny_osc_owner_name_file_first_download_transient_pii_approval.v1.json"

if (-not (Test-Path $LocalApproval)) {
    throw "Transient-local-file approval evidence is missing."
}
if (-not (Test-Path $Gate2Approval)) {
    throw "Gate 2 approval evidence is missing. Do not download the Owner Name File."
}

$TempDir = Join-Path $env:TEMP ("unclaimed-ny-osc-gate2-" + [guid]::NewGuid().ToString("N"))
$Archive = Join-Path $TempDir "FINDERS.zip"

New-Item -ItemType Directory -Path $TempDir | Out-Null

try {
    Write-Host ""
    Write-Host "NY OSC Gate 2 transient local-file runner"
    Write-Host "Save exactly FINDERS.zip into:"
    Write-Host $TempDir
    Write-Host ""
    Write-Host "Before downloading, verify the portal still shows:"
    Write-Host "  Name: FINDERS.zip"
    Write-Host "  Size: 390.51 MB"
    Write-Host "  Last modified: 9/16/2026, 1:33:31 PM"
    Write-Host ""
    Read-Host "Press Enter only AFTER Gate 2 is granted and the file is saved in that folder"

    if (-not (Test-Path $Archive)) {
        throw "FINDERS.zip was not found in the dedicated temp directory."
    }

    Push-Location $RepoRoot
    try {
        python -m unclaimed_platform.adapters.sources.ny_owner_name_transient_local_execution --archive $Archive --local-approval $LocalApproval --gate2-approval $Gate2Approval
        if ($LASTEXITCODE -ne 0) {
            throw "NY OSC bounded schema discovery stopped fail-closed."
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
