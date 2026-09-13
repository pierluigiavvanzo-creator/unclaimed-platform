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

Canonical now includes:

- `schemas/ui/m3_operations_console.schema.json` v1.0.0;
- `GET /api/reviewer/m3/operations` in FastAPI;
- `apps/reviewer-console` using Next.js App Router + TypeScript;
- synthetic/read-only dashboard with milestone, source-registry, provenance, privacy, audit and platform status;
- frontend lint/type/build CI gates;
- PowerShell frontend validation;
- ADR-0004 frontend/platform boundary;
- Vercel configuration and Supabase publishable-key placeholders only.

The UI cannot approve a source, enable acquisition, run matching or process real PII.

## Vercel / Supabase state

Observed 2026-09-13 through connected platform tools:

- Vercel: no teams/projects returned; no preview deployed.
- Supabase: no projects returned; no project/database/Auth/Storage created.

Do not invent IDs, URLs or keys. Supabase project/branch creation may incur cost and requires explicit organization/cost confirmation. Vercel deployment requires an available/connected team/project and a separate deployment gate.

## Known limitations / debt

- `package-lock.json` not committed; transitive npm resolution is not fully reproducible yet.
- ESLint `9.39.5` is a temporary compatibility pin because current `eslint-plugin-react` used by Next config fails on ESLint 10; maintenance warning remains.
- reviewer endpoint is a synthetic read model rather than a live projection from durable source/audit stores.
- frontend synthetic fallback duplicates part of the contract shape; later generate TS bindings from JSON Schema/OpenAPI.
- filesystem raw storage is not provider WORM/object lock.
- audit writer is still in-memory.
- retention lifecycle enforcement and PostgreSQL/Alembic application migration remain outstanding.

## SINGLE NEXT ACTION

Keep `main` untouched. Present and satisfy the separate Vercel preview/deployment gate: connect or expose an authorized Vercel team/project, verify that `apps/reviewer-console` is the project root or configured root directory, and deploy a preview only after explicit owner authorization. If no Vercel team/project is available, stop and request connection rather than inventing identifiers.

Supabase project creation/integration remains a separate future organization/cost/architecture gate. Real California acquisition and beneficiary matching remain blocked regardless of frontend deployment status.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 governance/raw persistence: CANONICAL + VERIFIED
M3 Operations Console: CANONICAL + CI VERIFIED
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Vercel project/team: NONE OBSERVED
Supabase project: NONE OBSERVED
main: UNCHANGED; separate human gate required
NEXT: Vercel connection/deployment gate
CONTEXT HEALTH: coherent; repository is source of truth
```
