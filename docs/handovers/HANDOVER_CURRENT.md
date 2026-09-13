# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Active candidate: `m3-operations-console`
- Candidate base canonical SHA: `f518946c5e6fc4c816cfec54d4b5e1a7058c67d3`
- Never develop directly on `main`; promote verified checkpoints only after explicit owner approval.

At every restart, verify branch HEADs and CI directly from GitHub.

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
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- `sources/registry.yaml` has no approved real source.

## Current candidate

Branch: `m3-operations-console`

Implemented:

- `schemas/ui/m3_operations_console.schema.json` v1.0.0;
- `GET /api/reviewer/m3/operations` in FastAPI;
- `apps/reviewer-console` using Next.js App Router + TypeScript;
- synthetic/read-only dashboard with milestone, source-registry, provenance, privacy, audit and platform status;
- frontend lint/type/build CI gates;
- PowerShell frontend validation;
- ADR-0004 frontend/platform boundary;
- Vercel configuration and Supabase publishable-key placeholders only.

The UI cannot approve a source, enable acquisition, run matching or process real PII.

## Verification evidence

Implementation/fix head before documentation closure: `7c0ecc644363353250ed974816af2d0620a5998d`.
GitHub Actions run `34771881569`: PASS.

- Ruff PASS.
- mypy PASS — 17 source files.
- contract tests 18 passed.
- smoke tests 3 passed.
- full pytest 53 passed with 2 known dependency warnings.
- frontend dependency install PASS.
- frontend lint PASS.
- frontend TypeScript PASS.
- Next.js production build PASS; `/` generated as static route.

After this handover/documentation commit, verify CI again on the exact final candidate HEAD before calling the candidate ready for promotion.

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

Verify the final candidate HEAD and final GitHub Actions run after documentation closure. Then present the human gate with branch, HEAD, diff/stat, tests, risks, rollback and deployment readiness. Do not promote automatically.

If the owner explicitly approves promotion of `m3-operations-console` to `m2-state-governance-core`, first re-verify candidate/canonical/main refs and divergence, then perform only a history-preserving fast-forward if safe, verify canonical CI on the exact resulting HEAD, and leave `main` untouched unless separately authorized.

Vercel preview deployment is a separate gate after canonical promotion/CI. Supabase project creation/integration is a separate future organization/cost/architecture gate.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 governance/raw persistence: CANONICAL + VERIFIED
M3 Operations Console: CANDIDATE + VERIFIED IMPLEMENTATION, FINAL DOC CI PENDING
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Vercel project/team: NONE OBSERVED
Supabase project: NONE OBSERVED
NEXT: final candidate CI -> human promotion gate
CONTEXT HEALTH: coherent; repository is source of truth
```
