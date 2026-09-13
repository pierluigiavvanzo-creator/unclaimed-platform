[CmdletBinding()]
param([string]$Output = "docs/handovers/HANDOVER_CURRENT.md")
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
$Repo = Split-Path -Parent $PSScriptRoot
Set-Location $Repo
$branch = git branch --show-current
$head = git log -1 --oneline 2>$null
if (-not $head) { $head = "NO_COMMIT" }
$status = git status --short | Out-String
$content = @"
# HANDOVER — unclaimed-platform — $(Get-Date -Format yyyy-MM-dd)

## Obiettivo attuale
M0 — Repository & Development Harness

## Baseline approvata
AGENTS.md v1.0

## Repo / branch / HEAD
- Branch: $branch
- HEAD: $head

## Stato test
Eseguire scripts/test.ps1 e registrare l'esito.

## Prossima singola azione
M1 — Machine Contracts.

## Working tree
```text
$status
```
"@
$dir = Split-Path -Parent $Output
if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
Set-Content -Path $Output -Value $content -Encoding utf8
Write-Host "Handover written to $Output"
