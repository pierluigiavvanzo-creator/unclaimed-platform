# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M3 — California Data Spike Readiness Gate

## Current Status

M0, M1 and M2 VERIFIED.

M3 source/legal readiness inventory is complete. A01 raw-acquisition contracts, a fail-closed California SCO adapter boundary, and deferred-source mock adapters are IMPLEMENTED and GitHub-CI VERIFIED on isolated branch `m3-acquisition-contracts`.

Real California acquisition remains BLOCKED. No real data has been downloaded and beneficiary matching remains disabled.

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
- M3 California source/legal readiness inventory documented in `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`.
- M3 acquisition contracts documented in `docs/audits/M3_ACQUISITION_CONTRACTS.md`.
- A01 request/result JSON Schema contracts implemented at version `1.0.0`.
- California SCO bulk adapter boundary implemented fail-closed with no network retrieval.
- Deferred California sources represented by deterministic synthetic mocks only.
- Candidate branch `m3-acquisition-contracts` GitHub CI: Ruff PASS; mypy PASS on 13 source files; pytest 30 passed, 2 known dependency warnings.

## Implemented but Not Yet Promoted

- Commit `b6030f2f1a5f9c7bdbe656e9eacba0a2e5107885` on branch `m3-acquisition-contracts` contains the M3 acquisition contracts/adapters implementation.
- The candidate has not yet been promoted to the canonical development branch `m2-state-governance-core`.

## In Progress

- Owner review/approval for promotion of the M3 acquisition-contract candidate.
- Define immutable raw-storage handling and privacy/data-minimization controls before any real network retrieval.

## Blocked

- Real M3 California acquisition remains blocked until immutable raw storage, provenance persistence, privacy/data-minimization controls and explicit source approval are complete.
- `sources/registry.yaml` remains intentionally without approved real sources.
- Beneficiary matching remains blocked.
- Automated outreach, claimant verification, fee agreements and claim submission remain blocked.

## Known Issues

- Two non-blocking FastAPI/Starlette/AnyIO test deprecation warnings remain.
- GitHub Actions reports upstream Node runtime deprecation warnings for actions/checkout@v4 and actions/setup-python@v5; current workflow passes.
- PostgreSQL/Alembic initial application migration is not yet implemented.

## Assumptions

- No real claimant, beneficiary, insurer, decedent or other PII data is used in the M3 candidate tests.
- Public availability of a source does not automatically authorize every downstream processing purpose.
- A01 owns raw acquisition/provenance; California row parsing/normalization is deferred to A02 after an official layout or bounded sample is verified.
- Outreach, legal determinations and claim submission remain disabled.

## Test Status

Candidate branch: `m3-acquisition-contracts`

- Local candidate-only tests: 6 passed; `compileall` PASS.
- GitHub Actions run 34763952641: PASS.
- Ruff: PASS.
- mypy: PASS — 13 source files.
- pytest: 30 passed, 2 known dependency warnings.
- No network acquisition was executed.

## Next Recommended Action

Review and approve promotion of the verified `m3-acquisition-contracts` candidate into the canonical development branch. After promotion, define immutable raw-storage/provenance persistence and privacy/data-minimization gates before implementing any real SCO download.
