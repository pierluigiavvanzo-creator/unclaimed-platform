# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M2 — State & Governance Core

## Current Status

M2 IMPLEMENTED. LOCAL CANDIDATE TESTED. GITHUB CI AND WINDOWS VALIDATION PENDING.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 machine contracts and A00-A23 registry.
- M1 Windows validation on Python 3.11.9: Ruff PASS, mypy PASS, pytest 12 passed, smoke 2 passed.
- M1 GitHub Actions: PASS.

## Implemented but Not Yet Verified

- Versioned workflow state whitelist v1.
- A00 deterministic orchestrator skeleton.
- Fail-closed policy engine skeleton.
- Budget ledger with exhaustion behavior.
- Append-only audit hash-chain writer.

## In Progress

- GitHub CI validation for M2.
- Final Windows PowerShell validation for M2.

## Blocked

- M3 California Data Spike remains blocked until source/legal readiness is minimally established.

## Known Issues

- Two non-blocking deprecation warnings originate in FastAPI/Starlette test dependencies.
- PostgreSQL/Alembic initial application migration is not yet implemented.

## Assumptions

- No real claimant, beneficiary, insurer or PII data is used in M0-M2 tests.
- Outreach, legal determinations and claim submission remain disabled.
- M2 state names are workflow-control states, not legal or claimant-status determinations.

## Test Status

M2 candidate pre-publish:
- Python compileall: PASS
- M2 unit tests: 12 passed
- Full Ruff/mypy/pytest: pending GitHub CI
- Windows validation: pending

## Next Recommended Action

Complete GitHub CI, then validate the M2 branch on Windows using scripts/test.ps1 and scripts/smoke.ps1.
