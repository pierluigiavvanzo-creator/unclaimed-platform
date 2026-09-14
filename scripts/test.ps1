[CmdletBinding()]
param()
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$Repo = Split-Path -Parent $PSScriptRoot
Set-Location $Repo
$Python = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $Python)) { throw "Missing .venv. Run scripts/bootstrap.ps1 first." }
& $Python -m ruff check .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $Python -m mypy src/unclaimed_platform/core src/unclaimed_platform/api src/unclaimed_platform/adapters/storage src/unclaimed_platform/ui
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $Python -m pytest -q tests/contract
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $Python -m pytest -q tests/smoke
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $Python -m pytest -q
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$Frontend = Join-Path $Repo "apps\reviewer-console"
if (Test-Path $Frontend) {
    $Npm = Get-Command npm -ErrorAction SilentlyContinue
    if (-not $Npm) { throw "Missing npm/Node.js required by apps/reviewer-console." }
    Push-Location $Frontend
    try {
        & npm install --no-audit --no-fund
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
        & npm run lint
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
        & npm run typecheck
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
        & npm run build
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }
    finally {
        Pop-Location
    }
}
exit 0
