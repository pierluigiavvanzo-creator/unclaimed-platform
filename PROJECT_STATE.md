# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters, immutable raw-storage/provenance persistence, privacy/data-minimization gates, and the first reviewer operations console are implemented and CI-verified on canonical `m2-state-governance-core`.

The `m3-operations-console` candidate was promoted to canonical by a history-preserving, non-forced fast-forward after explicit owner approval. The promoted implementation head is `308a5f5f71d12378e190398b0e81fbabc28d6aa1`; canonical post-promotion GitHub Actions run `34774600910` completed successfully.

`main` remains unchanged at the prior stable checkpoint. Real California acquisition and beneficiary matching remain BLOCKED. `sources/registry.yaml` has no approved real source.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 versioned machine contracts and A00-A23 registry.
- M2 deterministic state/governance core, budget ledger and SHA-256 audit chain.
- M3 California source/legal readiness and fail-closed A01 acquisition boundary.
- M3 immutable SHA-256 raw persistence and deterministic provenance records.
- M3 privacy/data-minimization gate with trusted policy separated from caller context.
- M3 raw-storage/privacy block promoted to canonical after explicit owner approval; canonical promotion CI run `34770452747` PASS.
- Reviewer read contract `schemas/ui/m3_operations_console.schema.json` v1.0.0.
- FastAPI `GET /api/reviewer/m3/operations` synthetic/read-only endpoint.
- Next.js App Router + TypeScript reviewer console under `apps/reviewer-console`.
- Frontend CI gates for lint, TypeScript and production build.
- PowerShell `scripts/test.ps1` extended to run frontend validation when the app exists.
- ADR-0004 records frontend/Vercel/Supabase architecture boundary.
- `m3-operations-console` promoted to `m2-state-governance-core` after explicit owner approval.
- Canonical post-promotion CI run `34774600910` PASS on the exact promoted implementation head.

## Canonical Promotion Verification

Candidate: `m3-operations-console`
Promotion target: `m2-state-governance-core`
Pre-promotion canonical head: `f518946c5e6fc4c816cfec54d4b5e1a7058c67d3`
Promoted implementation head: `308a5f5f71d12378e190398b0e81fbabc28d6aa1`
Promotion method: non-forced fast-forward
GitHub Actions run: `34774600910` — PASS.

Evidence:

- Ruff PASS.
- mypy PASS — 17 source files.
- contract tests 18 passed.
- smoke tests 3 passed.
- full pytest 53 passed, 2 known dependency warnings.
- frontend dependency install PASS.
- frontend lint PASS.
- frontend typecheck PASS.
- Next.js 16.3.4 production build PASS; `/` generated as a static route.
- no real source, real acquisition or real PII introduced.

## Blocked / Not Authorized

- Real California acquisition.
- Approval of a real source through the reviewer UI.
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Unapproved scraping/restricted-source access.
- Promotion to `main` without a separate explicit human gate.
- Vercel deployment or Supabase resource creation without the separate account/cost/deployment gate.

## Known Issues

- Vercel connection currently exposes no team/project; no preview exists.
- Supabase connection currently exposes no project; no active Supabase integration exists.
- `package-lock.json` is not committed yet; exact direct npm pins are present but transitive resolution is not fully locked.
- ESLint `9.39.5` is a compatibility pin because the current Next.js config's React plugin fails on ESLint 10; upstream maintenance warning remains.
- Reviewer read model is synthetic rather than backed by live durable stores.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention policy is recorded but physical lifecycle enforcement is outstanding.
- PostgreSQL/Alembic initial application migration is outstanding.
- Two known non-blocking FastAPI/Starlette/AnyIO test deprecation warnings remain.

## Next Recommended Action

Keep `main` untouched. The next bounded product action is a separate Vercel preview/deployment gate: connect or expose an authorized Vercel team/project, verify the project/root configuration for `apps/reviewer-console`, and deploy only after explicit owner authorization. Supabase project/database/Auth/Storage creation remains a later explicit organization/cost and architecture gate. Real acquisition remains blocked independently of frontend deployment.
