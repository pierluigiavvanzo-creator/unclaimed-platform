# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Windows Ruff/mypy green, 12 tests passed, smoke green, GitHub CI green |
| M2 — State & Governance Core | VERIFIED | GitHub CI green; Windows Ruff/mypy green; 24 tests passed; smoke 2 passed |
| M3 — California Data Spike | RAW STORAGE / PRIVACY GATES VERIFIED ON CANONICAL — REAL ACQUISITION BLOCKED | Source readiness, A01 acquisition contracts and raw persistence/governance boundary promoted to `m2-state-governance-core`; canonical CI green |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources;
- California SCO public bulk CSV identified as the preferred future real-data candidate;
- deferred sources classified as mock/reference/deferred;
- A01 raw-acquisition request/result contracts defined at version `1.0.0`;
- `REAL` requests require an explicit approval identifier;
- acquisition scope constrained to `RAW_INGEST_ONLY`;
- immutable raw artifact metadata includes SHA-256, byte count, content type and storage reference;
- provenance includes source URI, authority, acquisition method, terms-review reference and retrieval time;
- California SCO adapter boundary implemented fail-closed with no network retrieval;
- deferred-source deterministic mock adapter and fixtures implemented;
- acquisition-contract candidate promoted to the canonical development branch and stable M0–M3 checkpoint reconciled to `main`;
- M3 raw-storage/privacy REUSE FIRST evaluation completed;
- content-addressed raw-byte persistence implemented behind `ImmutableRawStore`;
- immutable provenance records use separate deterministic SHA-256 record hashes and support append-only acquisition history for identical raw bytes;
- successful new persistence reuses the existing M2 audit SHA-256 hash-chain writer;
- trusted privacy/data-minimization policy is separated from acquisition context;
- fail-closed gates cover source approval, required provenance, processing purpose, retention, data scope, field minimization, PII and synthetic/real scope;
- no real-source policy or real-source registry entry was added;
- raw-storage/privacy candidate promoted by fast-forward to canonical commit `1fbc74853385b6c6f92fb2c7d9b5b1df4ab0a10d` after owner approval;
- post-promotion canonical CI run `34770452747` passed Ruff, mypy, contract tests, smoke tests and full pytest.

## Product visibility / reviewer console — next bounded slice

The platform now needs a visible reviewer surface in parallel with backend development.

Next bounded frontend work should:

1. define the reviewer-console/backend read contract before UI implementation;
2. record the material frontend/platform decision in an ADR;
3. add a Next.js App Router frontend in an isolated candidate branch;
4. expose a read-only M3 Operations Console using synthetic/governed data only;
5. show milestone state, source-registry state, raw-artifact/provenance metadata, privacy-gate status and audit-chain status without exposing real PII;
6. add frontend lint/type/build tests to CI;
7. keep FastAPI and deterministic backend contracts authoritative;
8. evaluate Vercel as the frontend hosting/preview platform;
9. evaluate Supabase as a managed PostgreSQL/Auth/Storage provider behind existing boundaries rather than creating a parallel data plane;
10. do not create paid/external cloud resources without the required owner/cost gate.

## M3 still required before any real California acquisition

1. explicitly approve a versioned real-source governance policy and California SCO source entry through a separate human gate;
2. define production raw-storage/audit durability requirements as needed for the bounded real-data spike, without silently treating the local filesystem adapter as production WORM storage;
3. implement bounded read-only retrieval with transport, redirect, size, timeout and content validation;
4. only then execute a separately authorized bounded California spike with no unnecessary PII;
5. verify the actual CSV layout from authorized evidence before implementing A02 row normalization;
6. keep beneficiary matching blocked until the later matching/privacy/legal gates are satisfied.

## Still out of scope until later gates

- real California acquisition before explicit source/policy approval and retrieval verification;
- beneficiary matching on real data before M3 readiness approval;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.
