# M3 Vercel Backend Preview — Deployment Readiness Audit

Date: 2026-09-13
Status: CANDIDATE CI VERIFIED — REMOTE DEPLOY PENDING

## Goal

Replace the reviewer frontend's safe local fallback with the authoritative FastAPI read contract in a Vercel PREVIEW environment, without changing governance authority, enabling real acquisition, processing real PII, touching `main`, or creating Supabase resources.

## Architecture decision

ADR-0004 remains authoritative. This slice does not introduce a new application architecture.

- FastAPI and versioned backend contracts remain authoritative.
- Next.js remains a read-only consumer.
- The deployment adapter must not duplicate domain or reviewer logic.
- `REVIEWER_API_BASE_URL` remains the frontend server-side connection point.

## Reuse-first findings

Vercel's current Python/FastAPI guidance supports zero-configuration FastAPI deployment and recognizes an ASGI `app` entrypoint while installing Python dependencies from `pyproject.toml`. The current Vercel Python runtime supports Python 3.12+, and this repository's `requires-python = ">=3.11,<3.13"` includes Python 3.12.

Decision: WRAP the existing FastAPI application with a minimal root `app.py`; do not copy reviewer models/routes into the frontend or create a second backend implementation.

## Candidate

Branch: `m3-vercel-backend-preview`
Base canonical SHA: `d2ffb0ae161a7fc300c4688bf1880b2f44806c5d`
Verified candidate head: `973e01c62d0722e8c8e4eaffd0b985919a0a8f1f`

Changed implementation files:

- `app.py` — adds the repository `src` directory to the import path and re-exports `unclaimed_platform.api.app.app`;
- `tests/smoke/test_vercel_backend_entrypoint.py` — validates the deployment entrypoint and safety boundary;
- `.github/workflows/ci.yml` — adds a Python 3.12 Vercel-backend compatibility job.

No reviewer/domain payload implementation is duplicated in the adapter.

## Verification

GitHub Actions run: `34777855668` — PASS.

`quality` job:

- Ruff PASS;
- mypy PASS — 17 source files;
- contract tests: 18 passed;
- smoke tests: 4 passed;
- full pytest: 54 passed;
- known FastAPI/Starlette/AnyIO dependency warnings remain non-blocking;
- frontend dependency install PASS;
- frontend lint PASS;
- frontend typecheck PASS;
- Next.js 16.3.4 build PASS.

`vercel-backend-preview` job:

- Python 3.12 setup PASS;
- project install PASS;
- `tests/smoke/test_vercel_backend_entrypoint.py` PASS.

Safety assertions include:

- contract version `1.0.0`;
- mode `SYNTHETIC_READ_ONLY`;
- approved real sources `0`;
- real acquisition `BLOCKED`;
- beneficiary matching `BLOCKED`;
- PII mode `NO_REAL_PII`.

## Frontend preview evidence

Existing frontend preview deployment:

- ID: `dpl_8YLYX5gUtUu67feZd9mgemWNmFtL`;
- URL: `https://unclaimed-reviewer-console-5vf7znh1f-pierluigiavvanzo-8728.vercel.app`.

The owner supplied a screenshot showing the deployed UI renders successfully and preserves all synthetic/read-only safety boundaries. Visual smoke is therefore PASS. The screenshot also confirms the current source is still `typed synthetic fallback`.

## Remote deployment blocker

The Vercel connector became unavailable in the active ChatGPT session during this task. Therefore the following actions have NOT been executed:

- create/deploy the backend Vercel preview project;
- obtain a backend preview URL;
- inspect backend Vercel build/runtime logs;
- set reviewer-console PREVIEW `REVIEWER_API_BASE_URL`;
- redeploy and verify the frontend against the FastAPI service.

No workaround that invents project/team IDs or exposes credentials was used.

## Deployment acceptance criteria

When Vercel access is available:

1. deploy branch `m3-vercel-backend-preview` from repository root, PREVIEW only;
2. verify `GET /health` returns the expected service health payload;
3. verify `GET /api/reviewer/m3/operations` returns contract v1.0.0 with all safety invariants;
4. set frontend PREVIEW `REVIEWER_API_BASE_URL` to the backend preview origin;
5. redeploy frontend preview;
6. verify UI source changes to `FastAPI contract`;
7. verify `SYNTHETIC READ ONLY`, source registry `0`, acquisition/matching `BLOCKED`, and `NO REAL PII` remain visible;
8. if cross-project Vercel preview protection blocks server-to-server fetch, stop and design the smallest server-only protection-bypass mechanism rather than weakening governance or silently disabling protection.

## Rollback

The candidate is not promoted. Rollback is simply to leave canonical unchanged and discard the candidate branch. After a future promotion, rollback must use history-preserving revert commits; never force-push.
