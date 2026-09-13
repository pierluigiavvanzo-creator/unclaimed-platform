# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M3 — California Data Spike Readiness Gate

## Current Status

M0, M1 and M2 VERIFIED. M3 source/legal readiness inventory completed; real acquisition remains BLOCKED pending acquisition contracts, privacy constraints and explicit source approval.

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
- M3 California source/legal readiness inventory documented in `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md` using authoritative California government sources.
- Preferred future real-data candidate identified as the California State Controller Unclaimed Property public bulk CSV, with approval still pending.
- Deferred/mock treatment documented for Estates of Deceased Persons, CDI/NAIC locator, CDPH death records and California court records as applicable.

## Implemented but Not Yet Verified

None.

## In Progress

- M3 readiness gate: define acquisition contracts and adapter boundaries before any real California acquisition.
- Define privacy/data-minimization constraints and explicit source approval for any future real-data spike.

## Blocked

- Real M3 California acquisition remains blocked until acquisition contracts, provenance handling, privacy constraints and explicit source approval are complete.
- Beneficiary matching remains blocked.
- Automated outreach, claimant verification, fee agreements and claim submission remain blocked.

## Known Issues

- Two non-blocking deprecation warnings originate in FastAPI/Starlette test dependencies.
- GitHub Actions reports upstream Node runtime deprecation warnings for actions/checkout@v4 and actions/setup-python@v5; current workflow still passes.
- PostgreSQL/Alembic initial application migration is not yet implemented.
- `sources/registry.yaml` remains intentionally empty pending source approval; readiness candidates are documented in the M3 audit rather than marked `approved_for_use` prematurely.

## Assumptions

- No real claimant, beneficiary, insurer or PII data was acquired during the M3 source-readiness inventory.
- Public availability of a source does not automatically authorize every downstream processing purpose.
- Outreach, legal determinations and claim submission remain disabled.
- M2 state names are workflow-control states, not legal or claimant-status determinations.

## Test Status

No application code or machine contract was changed by the M3 source-readiness inventory, so no new runtime test result is claimed for this documentation-only task.

Last verified software baseline remains branch `m2-state-governance-core` before this documentation update:

- GitHub Actions: PASS.
- GitHub Ruff: PASS.
- GitHub mypy: PASS — 13 source files.
- GitHub pytest: 24 passed, 2 dependency warnings.
- Windows `scripts/test.ps1`: PASS — Ruff PASS, mypy PASS, pytest 24 passed, 2 known warnings.
- Windows `scripts/smoke.ps1`: PASS — 2 passed, 2 known warnings.

## Next Recommended Action

Define the M3 acquisition contract and adapter boundary for the California State Controller public bulk CSV source, plus mock contracts for deferred sources. Do not download real data or begin beneficiary matching until contracts, privacy constraints, provenance handling and explicit source approval are complete.
