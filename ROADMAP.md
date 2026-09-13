# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | GOVERNANCE/RAW STORAGE VERIFIED ON CANONICAL — REAL ACQUISITION BLOCKED | Source readiness, A01 acquisition contracts, raw persistence/privacy promoted and CI green |
| M3 Product Visibility — Operations Console | CANONICAL + CI VERIFIED + FRONTEND VISUAL SMOKE PASS — BACKEND PREVIEW DEPLOY PENDING | Vercel frontend renders safe synthetic UI; authoritative FastAPI Vercel entrypoint candidate passes Python 3.11/3.12 CI; remote backend deploy blocked by unavailable connector |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources.
- California SCO public bulk CSV identified only as a future bounded candidate; it is not approved for acquisition.
- A01 acquisition request/result contracts and fail-closed adapter boundary implemented.
- Immutable content-addressed raw storage/provenance and privacy/data-minimization gate implemented and promoted to canonical.
- No real-source policy or real-source registry entry exists.

## M3 product visibility — canonical frontend

The canonical Operations Console provides:

1. versioned read-only operations-console JSON Schema v1.0.0;
2. FastAPI reviewer endpoint as authoritative backend boundary;
3. Next.js App Router + TypeScript console;
4. visible M0-M3 status, source registry `0`, synthetic provenance metadata, privacy gates and audit health;
5. explicit real-acquisition and beneficiary-matching blocked states;
6. frontend lint/type/build in GitHub CI and PowerShell test harness;
7. ADR-0004 for Next.js/Vercel/Supabase boundary;
8. Vercel preview configuration without Supabase integration.

The owner supplied a screenshot of the Vercel frontend preview on 2026-09-13. Visual smoke is PASS: meaningful UI renders with `SYNTHETIC READ ONLY`, source registry `0`, acquisition/matching blocked and no real PII. It currently reports `Source: typed synthetic fallback`.

## Backend preview candidate

Branch `m3-vercel-backend-preview` was created from canonical `d2ffb0ae161a7fc300c4688bf1880b2f44806c5d`.

Candidate head: `973e01c62d0722e8c8e4eaffd0b985919a0a8f1f`.
GitHub Actions run `34777855668`: PASS.

Candidate scope:

- root `app.py` deployment adapter that re-exports the existing authoritative FastAPI application;
- smoke coverage for `/health` and `/api/reviewer/m3/operations` safety invariants;
- dedicated Python 3.12 CI compatibility job for Vercel, while normal project CI remains Python 3.11;
- no contract-version change;
- no real source/data/PII;
- no Supabase resource or SDK;
- no `main` change.

## Next gate

- Keep `main` unchanged unless separately approved under the stable-checkpoint policy.
- Restore/use the Vercel connector, which became unavailable during this task.
- Deploy `m3-vercel-backend-preview` from repository root as a PREVIEW backend only.
- Verify backend `/health` and `/api/reviewer/m3/operations` return the expected synthetic governed payload.
- Configure reviewer-console PREVIEW `REVIEWER_API_BASE_URL=<backend-preview-url>` and redeploy the frontend preview.
- Verify the UI changes from `typed synthetic fallback` to `FastAPI contract` while all safety boundaries remain unchanged.
- Promote the backend candidate to canonical only through the normal explicit human promotion gate after remote verification.
- Supabase project/database/Auth/Storage remains a separate future organization/cost/architecture gate.

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
