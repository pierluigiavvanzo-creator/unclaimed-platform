# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M2 — State & Governance Core

## Current Status

M2 IMPLEMENTED AND CI-TESTED. WINDOWS VALIDATION PENDING.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 machine contracts and A00-A23 registry.
- M1 Windows validation on Python 3.11.9: Ruff PASS, mypy PASS, pytest 12 passed, smoke 2 passed.
- M1 GitHub Actions: PASS.
- M2 versioned workflow state whitelist v1.
- M2 A00 deterministic orchestrator skeleton.
- M2 fail-closed policy engine skeleton.
- M2 budget ledger with explicit exhaustion behavior.
- M2 append-only audit SHA-256 hash-chain writer.
- M2 GitHub Actions: Ruff PASS, mypy PASS on 13 source files, pytest 24 passed.

## Implemented but Not Yet Verified

- Final M2 validation on the Product Owner Windows environment.

## In Progress

- Windows PowerShell test and smoke validation for M2.

## Blocked

- M3 California Data Spike remains blocked until source/legal readiness is minimally established.

## Known Issues

- Two non-blocking deprecation warnings originate in FastAPI/Starlette test dependencies.
- GitHub Actions reports upstream Node runtime deprecation warnings for actions/checkout@v4 and actions/setup-python@v5; current workflow still passes.
- PostgreSQL/Alembic initial application migration is not yet implemented.

## Assumptions

- No real claimant, beneficiary, insurer or PII data is used in M0-M2 tests.
- Outreach, legal determinations and claim submission remain disabled.
- M2 state names are workflow-control states, not legal or claimant-status determinations.

## Test Status

M2 latest code commit: ab5e1fff5ae5103b895ed0dc4a13c4aa398936ac

- Local M2 candidate: 12 unit tests PASS; compileall PASS.
- GitHub Actions: PASS.
- Ruff: PASS.
- mypy: PASS — 13 source files.
- pytest: 24 passed, 2 dependency warnings.
- Windows validation: pending.

## Next Recommended Action

Validate branch `m2-state-governance-core` on Windows with `scripts/test.ps1` and `scripts/smoke.ps1`. If green, mark M2 VERIFIED before any M3 work.
