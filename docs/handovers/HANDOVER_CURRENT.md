# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-13

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Historical operations-console candidate: `m3-operations-console`
- Current backend-preview candidate: `m3-vercel-backend-preview`
- Backend-preview candidate base canonical SHA: `d2ffb0ae161a7fc300c4688bf1880b2f44806c5d`
- Backend-preview candidate verified head: `973e01c62d0722e8c8e4eaffd0b985919a0a8f1f`
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
8. relevant ADRs, especially `docs/decisions/ADR-0004-reviewer-frontend-platform.md`
9. relevant audits, especially `docs/audits/M3_OPERATIONS_CONSOLE.md` and `docs/audits/M3_VERCEL_BACKEND_PREVIEW.md`

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- M3 Operations Console CANONICAL + CI VERIFIED.
- Frontend Vercel preview VISUAL SMOKE PASS based on owner-provided screenshot.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- `sources/registry.yaml` has no approved real source.
- Supabase untouched.
- `main` unchanged.

## Frontend Vercel preview

Deployment ID: `dpl_8YLYX5gUtUu67feZd9mgemWNmFtL`.
Preview URL: `https://unclaimed-reviewer-console-5vf7znh1f-pierluigiavvanzo-8728.vercel.app`.

Owner screenshot on 2026-09-13 confirms:

- page renders `M3 Operations Console`;
- `SYNTHETIC READ ONLY`;
- `Source: typed synthetic fallback`;
- source registry `0`;
- real acquisition `BLOCKED`;
- beneficiary matching `BLOCKED`;
- privacy `PASS SYNTHETIC ONLY`;
- `NO REAL PII`;
- no visible Next.js error overlay.

Visual smoke: PASS.
Vercel deployment metadata/build-log inspection: still pending because the connector/tool is unavailable in the current session.

## Backend preview candidate

Branch: `m3-vercel-backend-preview`.
Base: canonical `d2ffb0ae161a7fc300c4688bf1880b2f44806c5d`.
Verified head: `973e01c62d0722e8c8e4eaffd0b985919a0a8f1f`.
GitHub Actions run: `34777855668` — PASS.

Candidate changes:

- root `app.py` is a deployment adapter that imports/re-exports the existing authoritative FastAPI app;
- no reviewer/domain logic duplicated;
- smoke test verifies `/health` and `/api/reviewer/m3/operations` safety invariants;
- CI now has a Python 3.12 Vercel compatibility job in addition to the normal Python 3.11 quality job.

Run `34777855668` verified:

- Ruff PASS;
- mypy PASS — 17 files;
- 18 contract tests passed;
- 4 smoke tests passed;
- 54 full tests passed;
- frontend lint/type/build PASS;
- Python 3.12 Vercel entrypoint smoke PASS.

The candidate is NOT promoted and the backend is NOT remotely deployed yet.

## Vercel blocker

The Vercel plugin is installed/enabled, but the Vercel tool became unavailable during the task. Do not invent identifiers or credentials and do not substitute a production deployment.

## SINGLE NEXT ACTION

When Vercel access is available, deploy `m3-vercel-backend-preview` from repository root as a PREVIEW backend. Verify `/health` and `/api/reviewer/m3/operations`. Then configure the existing reviewer-console PREVIEW environment variable `REVIEWER_API_BASE_URL` with the backend preview origin and redeploy the frontend preview. Acceptance requires the UI source to become `FastAPI contract` while remaining `SYNTHETIC READ ONLY` with source registry `0`, real acquisition `BLOCKED`, beneficiary matching `BLOCKED`, and `NO REAL PII`.

If Vercel preview protection blocks the frontend's server-side request to the backend preview, stop and add only the minimum server-only bypass mechanism after reviewing the protection model; do not disable safety/governance controls.

After successful remote verification, present a separate human gate before promoting `m3-vercel-backend-preview` to canonical. Keep `main` untouched. Do not create Supabase resources.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 governance/raw persistence: CANONICAL + VERIFIED
M3 Operations Console: CANONICAL + CI VERIFIED
Frontend Vercel preview: VISUAL SMOKE PASS
Frontend data source: TYPED SYNTHETIC FALLBACK
Backend Vercel candidate: CI VERIFIED, NOT DEPLOYED
Backend candidate head: 973e01c62d0722e8c8e4eaffd0b985919a0a8f1f
Backend candidate CI: 34777855668 PASS
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Supabase: UNTOUCHED
main: UNCHANGED
NEXT: backend PREVIEW deploy -> verify -> set REVIEWER_API_BASE_URL -> frontend redeploy
CONTEXT HEALTH: coherent; repository is source of truth
```
