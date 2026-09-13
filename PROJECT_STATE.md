# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M3 — California Data Spike Readiness Gate

## Current Status

M0, M1 and M2 are VERIFIED.

M3 source/legal readiness, A01 acquisition contracts/adapters, immutable raw-storage/provenance persistence, and privacy/data-minimization gates are implemented and CI-verified on the canonical development branch `m2-state-governance-core`.

The raw-storage/privacy candidate `m3-raw-storage-privacy-gates` was promoted by fast-forward to the canonical development branch after explicit owner approval. The promoted implementation head is `1fbc74853385b6c6f92fb2c7d9b5b1df4ab0a10d`. Canonical CI run `34770452747` completed successfully after promotion.

`main` remains unchanged at the prior stable checkpoint. Promotion to `main` remains a separate human-gated action.

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
- Stable M0–M3 checkpoint aligned on `main` and `m2-state-governance-core` before the raw-storage/privacy block.
- M3 raw-storage/privacy REUSE FIRST review documented in `docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md`.
- Versioned A01 immutable raw/provenance record contract implemented.
- SHA-256 content-addressed raw persistence implemented behind `ImmutableRawStore`.
- Deterministic immutable provenance records permit append-only acquisition history for identical raw bytes.
- Existing M2 `AuditEventWriter` reused for `RAW_ARTIFACT_PERSISTED` hash-chain events; no parallel audit model introduced.
- Trusted `RawDataGovernancePolicy` separated from caller acquisition context so requests cannot self-authorize.
- Fail-closed gates implemented for privacy policy, provenance, real-source approval, processing purpose, retention policy, data categories, field minimization, PII authorization/necessity, and synthetic/real marker consistency.
- Candidate CI verified Ruff, mypy, contract tests, smoke tests and full pytest.
- Owner approved promotion of `m3-raw-storage-privacy-gates` to `m2-state-governance-core`.
- Promotion completed as a history-preserving fast-forward to `1fbc74853385b6c6f92fb2c7d9b5b1df4ab0a10d`.
- Canonical post-promotion CI run `34770452747`: PASS across Ruff, mypy, contract tests, smoke tests and full pytest.

## In Progress

- Product-facing reviewer/frontend visibility is the next cross-cutting development concern. It must remain downstream of deterministic backend contracts and must not bypass governance gates.

## Blocked

- Real M3 California acquisition remains blocked until a real source governance policy is explicitly approved and a later bounded retrieval implementation is separately authorized and verified.
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
- No Vercel team/project or Supabase project is currently connected; cloud-resource creation remains a separate explicit gate because it may create external state or cost.

## Assumptions

- No real claimant, beneficiary, insurer, decedent or family PII data is used in M3 tests.
- Public availability of a source does not automatically authorize downstream processing.
- A01 owns raw acquisition/provenance; California row parsing/normalization remains deferred to A02 until an official layout or bounded authorized sample is verified.
- The filesystem implementation is a replaceable adapter, not a production-backend decision.
- Outreach, legal determinations and claim submission remain disabled.
- Any frontend must consume governed backend contracts; it must not become an alternate authorization path.

## Test Status

Canonical post-promotion evidence:

- branch: `m2-state-governance-core`;
- promoted implementation head: `1fbc74853385b6c6f92fb2c7d9b5b1df4ab0a10d`;
- GitHub Actions run `34770452747`: PASS;
- Ruff: PASS;
- mypy: PASS — 16 source files;
- contract tests: PASS — 17 passed;
- smoke tests: PASS — 2 passed;
- full pytest: PASS — 51 passed with 2 known dependency warnings;
- no network acquisition was executed;
- no real source or real PII was introduced.

## Next Recommended Action

Create an isolated frontend/reviewer-console candidate from the verified canonical branch. Define the UI/backend contract first, record the material frontend hosting/data-platform choice in an ADR, implement a synthetic/read-only M3 Operations Console, and add frontend build/type/lint tests. Vercel and Supabase may be integrated only through explicit, bounded interfaces; no cloud project creation, real-source activation, or real PII ingestion is authorized by this step.