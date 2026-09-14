# ROADMAP.md

Last updated: 2026-09-14

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | GOVERNANCE/RAW STORAGE VERIFIED ON CANONICAL — REAL ACQUISITION BLOCKED | Source readiness, A01 acquisition contracts, raw persistence/privacy promoted and CI green |
| M3 Product Visibility — Operations Console | STREAMLIT CANDIDATE CI VERIFIED — REMOTE SMOKE PENDING | Run `34812099385` PASS on implementation SHA `f9042839`; Streamlit safety and startup smoke green |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- California SCO public bulk CSV identified only as a future bounded candidate; it is not approved for acquisition.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented and promoted to canonical.
- No real-source policy or real-source registry entry exists.

## Product visibility transition

The historical Next.js Operations Console remains in the repository as rollback/history. The owner explicitly ended Vercel as the active deployment path on 2026-09-14.

The Streamlit candidate:

1. reuses the existing typed M3 reviewer snapshot instead of duplicating payload data;
2. validates `SYNTHETIC_READ_ONLY`, source registry `0`, acquisition/matching `BLOCKED`, `NO_REAL_PII`, synthetic and immutable raw artifact before rendering;
3. fails closed on an unsafe snapshot;
4. uses Streamlit Community Cloud as the target host;
5. removes the separate backend-preview and `REVIEWER_API_BASE_URL` wiring from the critical path;
6. introduces no Supabase resource, real source, real acquisition or real PII.

## Candidate verification

Implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`
GitHub Actions run: `34812099385` — PASS.

- Ruff PASS.
- mypy PASS — 19 source files.
- 18 contract tests passed.
- 5 smoke tests passed.
- 55 full tests passed.
- Streamlit-specific safety tests: 2 passed.
- Streamlit startup smoke: PASS on `/_stcore/health`.
- Existing Next.js lint/type/build regression gates: PASS.

## Next gate

- Deploy branch `m3-streamlit-operations-console` to Streamlit Community Cloud with entrypoint `apps/reviewer-streamlit/streamlit_app.py` and Python 3.11.
- Perform a remote visual/content smoke confirming all M3 safety boundaries.
- Promote to canonical only after the normal explicit human promotion gate.
- Keep `main` unchanged until a separate stable-checkpoint decision.

## Still required before any real California acquisition

1. explicitly approve a versioned real-source governance policy and California SCO source entry through a separate human gate;
2. define production raw-storage/audit durability requirements;
3. implement bounded read-only retrieval with transport, redirect, size, timeout and content validation;
4. execute only a separately authorized bounded California spike with no unnecessary PII;
5. verify actual CSV layout from authorized evidence before A02 row normalization;
6. keep beneficiary matching blocked until later matching/privacy/legal gates are satisfied.

## Out of scope until later gates

- real California acquisition before explicit source/policy approval;
- real-data beneficiary matching;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.
