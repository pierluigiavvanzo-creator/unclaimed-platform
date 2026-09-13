# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M2 — State & Governance Core

## Current Status

M2 VERIFIED. READY FOR M3 READINESS GATE.

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
- M2 Windows PowerShell validation: Ruff PASS, mypy PASS on 13 source files, pytest 24 passed, smoke 2 passed.

## Implemented but Not Yet Verified

None for M2.

## In Progress

- M3 readiness gate: California source/legal readiness before any real acquisition.

## Blocked

- Real M3 California acquisition remains blocked until source authority, access method, provenance and terms/constraints are documented and approved.

## Known Issues

- Two non-blocking deprecation warnings originate in FastAPI/Starlette test dependencies.
- GitHub Actions reports upstream Node runtime deprecation warnings for actions/checkout@v4 and actions/setup-python@v5; current workflow still passes.
- PostgreSQL/Alembic initial application migration is not yet implemented.

## Assumptions

- No real claimant, beneficiary, insurer or PII data is used in M0-M2 tests.
- Outreach, legal determinations and claim submission remain disabled.
- M2 state names are workflow-control states, not legal or claimant-status determinations.

## Test Status

M2 verified branch: `m2-state-governance-core`

- Local M2 candidate: 12 unit tests PASS; compileall PASS.
- GitHub Actions: PASS.
- GitHub Ruff: PASS.
- GitHub mypy: PASS — 13 source files.
- GitHub pytest: 24 passed, 2 dependency warnings.
- Windows `scripts/test.ps1`: PASS — Ruff PASS, mypy PASS, pytest 24 passed, 2 known warnings.
- Windows `scripts/smoke.ps1`: PASS — 2 passed, 2 known warnings.

## Next Recommended Action

Begin the M3 readiness gate only: inventory candidate California sources, verify authority and permitted access, document provenance/terms, and decide what may be mocked versus accessed for real. Do not begin scraping or beneficiary matching yet.
