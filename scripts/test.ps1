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
& $Python -m mypy src/unclaimed_platform/core src/unclaimed_platform/api src/unclaimed_platform/adapters/storage
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $Python -m pytest -q tests/contract
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $Python -m pytest -q tests/smoke
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $Python -m pytest -q
exit $LASTEXITCODE
