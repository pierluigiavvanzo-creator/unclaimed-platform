# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Historical operations-console candidate: `m3-operations-console`
- Operations-console candidate base canonical SHA: `f518946c5e6fc4c816cfec54d4b5e1a7058c67d3`
- Promoted operations-console implementation SHA: `308a5f5f71d12378e190398b0e81fbabc28d6aa1`
- Canonical documentation-closure SHA before Vercel gate: `c6e8a9e25676853f8eb91652e27d0584c35ae3bb`
- Never develop directly on `main`; promote verified checkpoints only after explicit owner approval.

At every restart, verify branch HEADs and CI directly from GitHub. Documentation-only closure commits may make the latest canonical SHA newer than the promoted implementation SHA recorded above.

## Mandatory files to read first

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. this handover
6. `docs/architecture.md`
7. `docs/contracts.md`
8. `docs/decisions/ADR-0001-deterministic-core.md`
9. `docs/decisions/ADR-0002-versioned-machine-contracts.md`
10. `docs/decisions/ADR-0003-m2-governance-core.md`
11. `docs/decisions/ADR-0004-reviewer-frontend-platform.md`
12. `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`
13. `docs/audits/M3_ACQUISITION_CONTRACTS.md`
14. `docs/audits/MAIN_DIVERGENCE_RECONCILIATION.md`
15. `docs/audits/M3_RAW_STORAGE_PRIVACY_REUSE_FIRST.md`
16. `docs/audits/M3_RAW_STORAGE_PRIVACY_GATES.md`
17. `docs/audits/M3_OPERATIONS_CONSOLE_REUSE_FIRST.md`
18. `docs/audits/M3_OPERATIONS_CONSOLE.md`

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters IMPLEMENTED + CI VERIFIED + CANONICAL.
- M3 immutable raw storage/provenance + privacy/data-minimization IMPLEMENTED + CI VERIFIED + CANONICAL.
- M3 Operations Console IMPLEMENTED + CI VERIFIED + CANONICAL.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- `sources/registry.yaml` has no approved real source.
- `main` remains unchanged.
- Supabase project count remains zero.

## Operations Console promotion closure

Historical candidate branch: `m3-operations-console`

Owner approval: explicit on 2026-09-13.

Promotion target: `m2-state-governance-core`.

Pre-promotion state:

- candidate head: `308a5f5f71d12378e190398b0e81fbabc28d6aa1`;
- canonical head: `f518946c5e6fc4c816cfec54d4b5e1a7058c67d3`;
- candidate 4 commits ahead, 0 behind;
- candidate exact-head CI run `34772214241`: PASS.

Promotion method: history-preserving, non-forced fast-forward.

Canonical post-promotion run: `34774600910` — PASS on `308a5f5f71d12378e190398b0e81fbabc28d6aa1`.
Canonical documentation-closure run: `34774757492` — PASS on `c6e8a9e25676853f8eb91652e27d0584c35ae3bb`.

Verified:

- Ruff PASS;
- mypy PASS — 17 source files;
- contract tests 18 passed;
- smoke tests 3 passed;
- full pytest 53 passed with 2 known dependency warnings;
- frontend dependency install PASS;
- frontend lint PASS;
- frontend TypeScript PASS;
- Next.js 16.3.4 production build PASS; `/` generated as a static route.

`main` was not modified by this promotion.

## Current product-visible capability

Canonical includes:

- `schemas/ui/m3_operations_console.schema.json` v1.0.0;
- `GET /api/reviewer/m3/operations` in FastAPI;
- `apps/reviewer-console` using Next.js App Router + TypeScript;
- synthetic/read-only dashboard with milestone, source-registry, provenance, privacy, audit and platform status;
- frontend lint/type/build CI gates;
- PowerShell frontend validation;
- ADR-0004 frontend/platform boundary;
- Vercel configuration and Supabase publishable-key placeholders only.

The UI cannot approve a source, enable acquisition, run matching or process real PII.

## Vercel preview gate — current state

Owner authorization: explicit on 2026-09-13 to configure/deploy a preview, without touching `main` and without creating Supabase resources.

The Vercel connector initially returned no teams. A direct preview deployment using the canonical frontend bundle was nevertheless accepted by Vercel.

Deployment evidence:

- deployment ID: `dpl_8YLYX5gUtUu67feZd9mgemWNmFtL`;
- preview URL: `https://unclaimed-reviewer-console-5vf7znh1f-pierluigiavvanzo-8728.vercel.app`;
- inspector URL: `https://vercel.com/pierluigiavvanzo-8728/unclaimed-reviewer-console/8YLYX5gUtUu67feZd9mgemWNmFtL`;
- target: preview;
- Vercel create response: `INITIALIZING`;
- bundle contained only canonical `apps/reviewer-console` files; no backend secrets, real data or Supabase resources were included.

Post-create verification is BLOCKED by the current Vercel OAuth/scope state. Reading the deployment through the connector returns HTTP 403:

`Not authorized: Trying to access resource under scope "pierluigiavvanzo-8728".`

The error identifies team ID `team_l4XAWc1rSwVdJWzlv5ZIirsJ`. This identifier came from Vercel's own error response and was not invented.

Do not call the preview PASS or READY until the Vercel connection is re-authenticated/authorized for this scope and the following checks succeed:

1. deployment status is `READY`;
2. build logs show successful Next.js build;
3. preview URL renders meaningful Operations Console content;
4. no Next.js/framework error overlay is present;
5. UI still shows synthetic/read-only state, source registry 0, real acquisition BLOCKED, beneficiary matching BLOCKED and no real PII.

Do not create a second deployment unless the existing deployment failed or a code/config fix is required.

## Supabase state

Observed again after the Vercel deployment attempt:

- Supabase projects: `[]`;
- no project/database/Auth/Storage/Edge Function/resource was created;
- no Supabase SDK was added;
- no Supabase cost gate was entered.

## Known limitations / debt

- Vercel preview verification is blocked by scope authorization mismatch.
- `package-lock.json` not committed; transitive npm resolution is not fully reproducible yet.
- ESLint `9.39.5` is a temporary compatibility pin because current `eslint-plugin-react` used by Next config fails on ESLint 10; maintenance warning remains.
- reviewer endpoint is a synthetic read model rather than a live projection from durable source/audit stores.
- frontend synthetic fallback duplicates part of the contract shape; later generate TS bindings from JSON Schema/OpenAPI.
- filesystem raw storage is not provider WORM/object lock.
- audit writer is still in-memory.
- retention lifecycle enforcement and PostgreSQL/Alembic application migration remain outstanding.

## SINGLE NEXT ACTION

Re-authenticate or reconnect Vercel so the connected session has access to scope `pierluigiavvanzo-8728` / team `team_l4XAWc1rSwVdJWzlv5ZIirsJ`. Then inspect existing deployment `dpl_8YLYX5gUtUu67feZd9mgemWNmFtL` rather than redeploying by default. Verify READY/build/page/error-overlay/synthetic-boundary checks listed above.

Keep `main` untouched. Do not create Supabase resources. Real California acquisition and beneficiary matching remain blocked regardless of frontend deployment status.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 governance/raw persistence: CANONICAL + VERIFIED
M3 Operations Console: CANONICAL + CI VERIFIED
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Vercel preview: CREATED, NOT YET VERIFIED
Vercel blocker: HTTP 403 SCOPE AUTHORIZATION
Supabase project: NONE OBSERVED
main: UNCHANGED; separate human gate required
NEXT: re-authorize Vercel scope -> verify existing preview
CONTEXT HEALTH: coherent; repository is source of truth
```
