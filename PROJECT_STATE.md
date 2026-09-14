# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters, immutable raw-storage/provenance persistence, privacy/data-minimization gates, and the reviewer read contract are implemented and verified on canonical `m2-state-governance-core`.

The owner explicitly abandoned Vercel as the active reviewer deployment path on 2026-09-14 after repeated project/deployment visibility inconsistencies. Streamlit Community Cloud is now the approved M3 reviewer deployment target under D-006 / ADR-0005.

Candidate branch `m3-streamlit-operations-console` has a CI-verified implementation at commit `f9042839296cca256c1c886f4b1667caa3f2a532`. GitHub Actions run `34812099385` passed both `quality` and `streamlit-candidate` jobs. Remote Streamlit Community Cloud deployment/visual smoke is still pending.

`main` remains unchanged. Real California acquisition and beneficiary matching remain BLOCKED. `sources/registry.yaml` has no approved real source. Supabase remains untouched.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 versioned machine contracts and A00-A23 registry.
- M2 deterministic state/governance core, budget ledger and SHA-256 audit chain.
- M3 California source/legal readiness and fail-closed A01 acquisition boundary.
- M3 immutable SHA-256 raw persistence and deterministic provenance records.
- M3 privacy/data-minimization gate with trusted policy separated from caller context.
- Reviewer read contract `schemas/ui/m3_operations_console.schema.json` v1.0.0.
- FastAPI `GET /api/reviewer/m3/operations` synthetic/read-only endpoint.
- Historical Next.js Operations Console canonical + CI verified; prior Vercel visual smoke passed.
- Streamlit candidate reuses the existing typed reviewer snapshot; no snapshot payload duplication.
- Streamlit fail-closed adapter rejects unsafe state before rendering.
- Streamlit 1.63.0 dependency installation verified on Python 3.11.16.
- GitHub Actions run `34812099385` on implementation SHA `f9042839296cca256c1c886f4b1667caa3f2a532`: PASS.

## Streamlit Candidate Verification

Branch: `m3-streamlit-operations-console`
Verified implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`
GitHub Actions run: `34812099385`

Evidence:

- Ruff: PASS (`All checks passed!`).
- mypy: PASS — 19 source files.
- contract tests: 18 passed, 2 known dependency warnings.
- smoke tests: 5 passed, 2 known dependency warnings.
- full pytest: 55 passed, 2 known dependency warnings.
- historical Next.js frontend lint: PASS.
- historical Next.js frontend typecheck: PASS.
- historical Next.js production build: PASS.
- Streamlit safety smoke: 2 passed.
- Streamlit startup smoke: PASS via `/_stcore/health` on port 8501.
- no real source, real acquisition, beneficiary matching or real PII introduced.

## In Progress

- Remote Streamlit Community Cloud deployment from the verified candidate.
- Remote visual/content smoke after deployment.

## Blocked / Not Authorized

- Real California acquisition.
- Approval of a real source through the reviewer UI.
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Unapproved scraping/restricted-source access.
- Promotion to canonical or `main` without the applicable human gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Known Issues

- Streamlit candidate has not yet been deployed to Community Cloud, so remote visual/content smoke remains unverified.
- Two known non-blocking FastAPI/Starlette/AnyIO dependency deprecation warnings remain.
- GitHub Actions reports upstream Node runtime deprecation warnings for current actions; workflows pass.
- Historical Next.js dependency install warns that ESLint 9.39.5 is no longer supported; historical build still passes and that frontend is no longer on the critical path.
- The M3 reviewer read model is still synthetic rather than backed by live durable stores.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration are outstanding.

## Next Recommended Action

Deploy verified implementation `f9042839296cca256c1c886f4b1667caa3f2a532` from branch `m3-streamlit-operations-console` to Streamlit Community Cloud using `apps/reviewer-streamlit/streamlit_app.py` with Python 3.11. Verify the rendered page remains `SYNTHETIC_READ_ONLY`, approved real sources `0`, real acquisition `BLOCKED`, beneficiary matching `BLOCKED` and `NO_REAL_PII`. Keep `main` untouched and stop at the explicit promotion gate after remote verification.
