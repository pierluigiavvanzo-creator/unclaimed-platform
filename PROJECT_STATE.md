# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M3 — California Data Spike Readiness Gate

## Current Status

M0, M1 and M2 are VERIFIED.

M3 source/legal readiness and A01 acquisition contracts/adapters are complete and verified on the canonical baseline.

The isolated candidate branch `m3-raw-storage-privacy-gates` now implements and CI-verifies immutable raw-byte persistence, append-only immutable provenance records, integration with the existing audit SHA-256 hash chain, and fail-closed privacy/data-minimization gates. This work is **pending the explicit human promotion gate** and has not been promoted to `m2-state-governance-core` or `main`.

Real California acquisition remains BLOCKED. No real source is approved in `sources/registry.yaml`, no real data was downloaded, and beneficiary matching remains disabled.

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
- M3 acquisition-contract candidate promoted to `m2-state-governance-core` at commit `757202bb079cfeb01d0e1c5648ab26c9095be89e`.
- `main` divergence reconciled and branch/integration policy recorded as D-005.
- Stable M0–M3 checkpoint aligned on `main` and `m2-state-governance-core` before the current candidate work.
- M3 raw-storage/privacy REUSE FIRST review documented in `docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md`.
- Versioned A01 immutable raw/provenance record contract implemented.
- SHA-256 content-addressed raw persistence implemented behind `ImmutableRawStore`.
- Deterministic immutable provenance records permit append-only acquisition history for identical raw bytes.
- Existing M2 `AuditEventWriter` reused for `RAW_ARTIFACT_PERSISTED` hash-chain events; no parallel audit model introduced.
- Trusted `RawDataGovernancePolicy` separated from caller acquisition context so requests cannot self-authorize.
- Fail-closed gates implemented for privacy policy, provenance, real-source approval, processing purpose, retention policy, data categories, field minimization, PII authorization/necessity, and synthetic/real marker consistency.
- M3 raw-storage/privacy candidate CI run `34766966136`: Ruff PASS; mypy PASS on 16 source files; contract tests 17 passed; smoke 2 passed; full pytest 51 passed with 2 known dependency warnings.

## In Progress

- Human review/promotion gate for `m3-raw-storage-privacy-gates`.

## Blocked

- Real M3 California acquisition remains blocked until this candidate is promoted, a real source governance policy is explicitly approved, and a later bounded retrieval implementation is separately authorized and verified.
- `sources/registry.yaml` remains intentionally without approved real sources.
- Beneficiary matching remains blocked.
- Automated outreach, claimant verification, fee agreements and claim submission remain blocked.

## Known Issues

- Two non-blocking FastAPI/Starlette/AnyIO test deprecation warnings remain.
- GitHub Actions reports upstream Node runtime deprecation warnings for `actions/checkout@v4` and `actions/setup-python@v5`; current workflow passes.
- PostgreSQL/Alembic initial application migration is not yet implemented.
- The bounded filesystem store provides application-level immutability through content addressing, exclusive create and verification; production WORM/object-lock storage is not yet selected.
- The existing verified M2 audit writer remains in-memory; durable production audit-event persistence is still outstanding.
- Retention policy is required/recorded but physical lifecycle enforcement is not implemented in this block.
- Branch protection is not currently enabled on `main`; governance relies on the explicit human gate recorded in `AGENTS.md` and D-005.

## Assumptions

- No real claimant, beneficiary, insurer, decedent or family PII data is used in M3 tests.
- Public availability of a source does not automatically authorize downstream processing.
- A01 owns raw acquisition/provenance; California row parsing/normalization remains deferred to A02 until an official layout or bounded authorized sample is verified.
- The filesystem implementation is a replaceable adapter, not a production-backend decision.
- Outreach, legal determinations and claim submission remain disabled.

## Test Status

Current candidate evidence:

- branch: `m3-raw-storage-privacy-gates`;
- base: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`;
- verified implementation/test head: `f42d8aa2daadcc83ff799150c039117755d8717a`;
- GitHub Actions run `34766966136`: PASS;
- Ruff: PASS;
- mypy: PASS — 16 source files;
- contract tests: 17 passed;
- smoke tests: 2 passed;
- full pytest: 51 passed, 2 known dependency warnings;
- no network acquisition was executed;
- no real source or real PII was introduced.

Documentation-only commits after the verified implementation head must also pass CI before promotion.

## Next Recommended Action

Complete the human promotion gate for `m3-raw-storage-privacy-gates`: verify final candidate HEAD/diff and final CI, then obtain owner approval before promoting to the canonical development branch. Do not implement or execute any real California SCO retrieval as part of this gate.