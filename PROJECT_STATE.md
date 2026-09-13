# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M3 — California Data Spike Readiness Gate

## Current Status

M0, M1 and M2 are VERIFIED.

M3 source/legal readiness inventory is complete. A01 raw-acquisition contracts, a fail-closed California SCO adapter boundary, and deferred-source mock adapters are implemented and CI-verified.

The first stable M0–M3 checkpoint has been reconciled into `main`. The previous `main` divergence was resolved with a history-preserving two-parent merge. The canonical development branch remains `m2-state-governance-core`; stable milestone checkpoints are promoted to `main` only after verification and owner approval.

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
- M3 candidate CI: Ruff PASS; mypy PASS on 13 source files; pytest 30 passed, 2 known dependency warnings.
- M3 acquisition-contract candidate promoted to `m2-state-governance-core` at commit `757202bb079cfeb01d0e1c5648ab26c9095be89e`.
- `main` divergence audit completed and documented in `docs/audits/MAIN_DIVERGENCE_RECONCILIATION.md`.
- Branch/integration policy recorded as D-005 in `DECISIONS.md`.
- History-preserving reconciliation merge committed as `b65e02f455c5a4c9bef6c77237ec5fefc6c315d3`.
- GitHub Actions on `main`, run `34764546636`: PASS — Ruff PASS, mypy PASS, pytest 30 passed.

## In Progress

- Define immutable raw-storage handling and provenance persistence before any real network retrieval.
- Define privacy/data-minimization controls for the bounded California spike.
- Define the explicit source-approval gate for the California SCO bulk source.

## Blocked

- Real M3 California acquisition remains blocked until immutable raw storage, provenance persistence, privacy/data-minimization controls and explicit source approval are complete.
- `sources/registry.yaml` remains intentionally without approved real sources.
- Beneficiary matching remains blocked.
- Automated outreach, claimant verification, fee agreements and claim submission remain blocked.

## Known Issues

- Two non-blocking FastAPI/Starlette/AnyIO test deprecation warnings remain.
- GitHub Actions reports upstream Node runtime deprecation warnings for `actions/checkout@v4` and `actions/setup-python@v5`; current workflow passes.
- PostgreSQL/Alembic initial application migration is not yet implemented.
- Branch protection is not currently enabled on `main`; governance relies on the explicit human gate recorded in `AGENTS.md` and D-005.

## Assumptions

- No real claimant, beneficiary, insurer, decedent or other PII data is used in the M3 tests.
- Public availability of a source does not automatically authorize every downstream processing purpose.
- A01 owns raw acquisition/provenance; California row parsing/normalization is deferred to A02 after an official layout or bounded sample is verified.
- Outreach, legal determinations and claim submission remain disabled.

## Test Status

Stable checkpoint evidence:

- `main` reconciliation commit: `b65e02f455c5a4c9bef6c77237ec5fefc6c315d3`.
- GitHub Actions on `main`, run `34764546636`: PASS.
- Ruff: PASS.
- mypy: PASS — 13 source files.
- pytest: 30 passed, 2 known dependency warnings.
- No network acquisition was executed.

## Next Recommended Action

Define and test immutable raw-storage/provenance persistence plus privacy/data-minimization gates for M3. Do not implement a real California SCO download until those controls and explicit source approval are complete.
