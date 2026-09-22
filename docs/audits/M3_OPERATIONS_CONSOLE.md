# M3 Operations Console — implementation and verification audit

Date: 2026-09-13
Candidate branch: `m3-operations-console`
Base canonical SHA: `f518946c5e6fc4c816cfec54d4b5e1a7058c67d3`

## Scope

Implemented the first product-visible reviewer surface without expanding the real-data permission boundary.

### Backend/read contract

- Added `GET /api/reviewer/m3/operations`.
- Added JSON Schema `schemas/ui/m3_operations_console.schema.json` version `1.0.0`.
- Snapshot mode is fixed to `SYNTHETIC_READ_ONLY`.
- Approved real sources remain `0`.
- Real acquisition and beneficiary matching remain `BLOCKED`.
- Raw/provenance display data is synthetic only.

### Frontend

- Added Next.js App Router + TypeScript app under `apps/reviewer-console`.
- Shows milestone cards, source-registry state, synthetic raw/provenance metadata, privacy/governance state, audit-chain state and Vercel/Supabase connection state.
- Server-side reader prefers the authoritative FastAPI endpoint and fails safely to a typed synthetic fallback when no backend URL is configured.
- No write action, source approval control, matching action, claimant workflow or real PII path exists.

### Platform boundary

- Vercel is the preferred preview/hosting target after an account/team/project is connected.
- Supabase is deferred to a later persistence/auth slice behind existing backend/repository boundaries.
- The current connected Vercel account returned no teams/projects; the current Supabase connection returned no projects.
- No cloud resource, database, deployment, key or paid service was created.

## Candidate verification

Implementation/fix head `7c0ecc644363353250ed974816af2d0620a5998d` was verified by GitHub Actions run `34771881569`:

- Ruff: PASS.
- mypy: PASS — 17 source files.
- contract tests: PASS — 18 passed.
- smoke tests: PASS — 3 passed.
- full pytest: PASS — 53 passed, 2 known dependency warnings.
- frontend dependency install: PASS.
- frontend lint: PASS.
- frontend TypeScript check: PASS.
- Next.js production build: PASS; static `/` route generated successfully.

The first CI attempt failed only because ESLint 10 removed an API still used by `eslint-plugin-react` bundled through the current Next.js config. The candidate was corrected to ESLint `9.39.5`, after which the full pipeline passed. This compatibility pin is temporary technical debt: ESLint 9 now emits an upstream support warning and should be removed when the Next.js React-plugin chain is verified compatible with ESLint 10.

## Promotion closure

The owner explicitly approved promotion of `m3-operations-console` to `m2-state-governance-core` on 2026-09-13.

Pre-promotion verification confirmed:

- candidate head `308a5f5f71d12378e190398b0e81fbabc28d6aa1`;
- canonical head `f518946c5e6fc4c816cfec54d4b5e1a7058c67d3`;
- compare status: candidate 4 commits ahead, 0 behind;
- candidate exact-head CI run `34772214241`: PASS;
- `main` remained unchanged.

Promotion used a history-preserving, non-forced fast-forward of `m2-state-governance-core` to `308a5f5f71d12378e190398b0e81fbabc28d6aa1`.

Canonical post-promotion GitHub Actions run `34774600910` completed successfully on the exact promoted implementation head:

- Ruff: PASS;
- mypy: PASS — 17 source files;
- contract tests: PASS — 18 passed;
- smoke tests: PASS — 3 passed;
- full pytest: PASS — 53 passed, 2 known dependency warnings;
- frontend dependency install: PASS;
- frontend lint: PASS;
- frontend TypeScript check: PASS;
- Next.js 16.3.4 production build: PASS; static `/` route generated successfully.

No real source, acquisition, California row interpretation or real PII was introduced by the promotion. `main` was not modified.

## Known limitations

- No Vercel preview is deployed yet because no Vercel team/project is available through the current connection.
- No Supabase project exists; Auth/RLS/PostgreSQL/Storage integration is not implemented.
- The reviewer snapshot is currently a synthetic read model rather than a live projection from the durable audit/source stores.
- The frontend duplicates the safe synthetic fallback shape; later work should generate TypeScript types or client bindings from the versioned schema/OpenAPI to reduce drift.
- `package-lock.json` is not yet committed; direct dependency versions are exact-pinned but transitive npm resolution is not fully reproducible. Add a lockfile before production deployment.
- Existing backend durability limitations remain: filesystem adapter is not provider-level WORM, audit writer is in-memory, physical retention lifecycle is not implemented.

## Rollback

The candidate is now promoted. Any rollback on canonical must use history-preserving revert commits; never force-push shared branches. `main` remains an independent stable checkpoint and was not changed by this promotion.
