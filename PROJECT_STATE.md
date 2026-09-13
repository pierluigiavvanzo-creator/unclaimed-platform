# PROJECT_STATE.md

Last updated: 2026-09-13

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters, immutable raw-storage/provenance persistence, privacy/data-minimization gates, and the first reviewer operations console are implemented and CI-verified on canonical `m2-state-governance-core`.

The Operations Console is canonical. The owner supplied a screenshot of the Vercel preview on 2026-09-13 showing a successful visual smoke: the page renders `M3 Operations Console`, `SYNTHETIC READ ONLY`, source registry `0`, real acquisition `BLOCKED`, beneficiary matching `BLOCKED`, `PASS SYNTHETIC ONLY`, and `NO REAL PII`. This closes the frontend visual smoke as PASS. Vercel platform metadata/build-log verification is still pending because the Vercel connector became unavailable in the active session.

A new candidate branch `m3-vercel-backend-preview` was created from canonical `d2ffb0ae161a7fc300c4688bf1880b2f44806c5d` to connect the frontend to the authoritative FastAPI read contract without duplicating backend logic. Candidate head `973e01c62d0722e8c8e4eaffd0b985919a0a8f1f` adds a root `app.py` Vercel entrypoint, a deployment smoke test, and a Python 3.12 Vercel compatibility CI job. GitHub Actions run `34777855668` passed both `quality` and `vercel-backend-preview` jobs. The candidate has NOT been promoted to canonical and has NOT been deployed remotely yet.

`main` remains unchanged at the prior stable checkpoint. Real California acquisition and beneficiary matching remain BLOCKED. `sources/registry.yaml` has no approved real source. Supabase remains untouched.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 versioned machine contracts and A00-A23 registry.
- M2 deterministic state/governance core, budget ledger and SHA-256 audit chain.
- M3 California source/legal readiness and fail-closed A01 acquisition boundary.
- M3 immutable SHA-256 raw persistence and deterministic provenance records.
- M3 privacy/data-minimization gate with trusted policy separated from caller context.
- Reviewer read contract `schemas/ui/m3_operations_console.schema.json` v1.0.0.
- FastAPI `GET /api/reviewer/m3/operations` synthetic/read-only endpoint.
- Next.js App Router + TypeScript reviewer console under `apps/reviewer-console`.
- Frontend lint/type/build gates in GitHub CI.
- ADR-0004 keeps FastAPI/versioned contracts authoritative and the browser read-only.
- Operations Console promoted to canonical after explicit owner approval.
- Vercel frontend preview created; owner-provided screenshot confirms visual smoke PASS.
- Candidate `m3-vercel-backend-preview` reuses the authoritative FastAPI app through a root deployment adapter rather than copying reviewer logic.
- Candidate CI run `34777855668` PASS: Python 3.11 quality suite, Python 3.12 Vercel entrypoint smoke, 18 contract tests, 4 smoke tests, 54 full tests, frontend lint/type/build.

## Vercel Frontend Preview

Deployment ID: `dpl_8YLYX5gUtUu67feZd9mgemWNmFtL`.
Preview URL: `https://unclaimed-reviewer-console-5vf7znh1f-pierluigiavvanzo-8728.vercel.app`.
Visual smoke: PASS based on owner screenshot supplied 2026-09-13.
Current rendered source: `typed synthetic fallback`.
Platform metadata/build-log verification: PENDING because the Vercel connector is unavailable in the active session.

## Backend Preview Candidate

Branch: `m3-vercel-backend-preview`.
Base canonical SHA: `d2ffb0ae161a7fc300c4688bf1880b2f44806c5d`.
Candidate head: `973e01c62d0722e8c8e4eaffd0b985919a0a8f1f`.
CI run: `34777855668` — PASS.

Candidate changes:

- root `app.py` exports the existing `unclaimed_platform.api.app.app` for Vercel; no domain/reviewer logic is duplicated;
- `tests/smoke/test_vercel_backend_entrypoint.py` verifies `/health`, contract v1.0.0, `SYNTHETIC_READ_ONLY`, source registry `0`, acquisition/matching `BLOCKED`, and `NO_REAL_PII`;
- CI adds a Python 3.12 deployment-compatibility smoke job while preserving Python 3.11 as the normal development baseline.

Remote backend deployment: NOT YET EXECUTED because the Vercel connector became unavailable during the task.

## Blocked / Not Authorized

- Real California acquisition.
- Approval of a real source through the reviewer UI.
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Unapproved scraping/restricted-source access.
- Promotion to `main` without a separate explicit human gate.
- Supabase resource creation without the separate organization/cost/architecture gate.
- Promotion of `m3-vercel-backend-preview` to canonical without the normal candidate promotion gate.

## Known Issues

- Vercel connector/tool is currently unavailable in the active session, so backend project creation/deployment, environment-variable mutation and platform-log verification cannot be completed from ChatGPT right now.
- The frontend still shows `typed synthetic fallback` until `REVIEWER_API_BASE_URL` is configured to a reachable FastAPI preview.
- The read contract still reports `platform.vercel = NOT_CONNECTED`; changing platform-status semantics should be a separate versioned contract decision, not silently changed in this deployment slice.
- `package-lock.json` is not committed yet; exact direct npm pins are present but transitive resolution is not fully locked.
- ESLint `9.39.5` remains a compatibility pin with an upstream maintenance warning.
- Reviewer read model is synthetic rather than backed by live durable stores.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration remain outstanding.

## Next Recommended Action

Keep `main` untouched. When the Vercel connector is available, deploy branch `m3-vercel-backend-preview` from repository root as a PREVIEW backend, verify `/health` and `/api/reviewer/m3/operations`, then set the reviewer-console PREVIEW environment variable `REVIEWER_API_BASE_URL` to that backend preview URL and redeploy the frontend preview. Acceptance requires the UI to render `Source: FastAPI contract` while retaining `SYNTHETIC READ ONLY`, source registry `0`, real acquisition `BLOCKED`, beneficiary matching `BLOCKED`, and no real PII. Do not create Supabase resources.
