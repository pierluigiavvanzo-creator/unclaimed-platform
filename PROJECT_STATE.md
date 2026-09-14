# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters, immutable raw-storage/provenance persistence, privacy/data-minimization gates, and the first reviewer operations console are implemented and CI-verified on canonical `m2-state-governance-core`.

The owner explicitly abandoned Vercel as the active reviewer deployment path on 2026-09-14 after repeated project/deployment visibility inconsistencies. Streamlit Community Cloud is now the approved M3 reviewer deployment target under D-006 / ADR-0005.

Candidate branch `m3-streamlit-operations-console` adds a Streamlit reviewer surface that reuses the existing typed synthetic M3 read model and fails closed if real sources, real acquisition, beneficiary matching or real PII appear. Candidate CI and remote Streamlit smoke are pending.

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

## In Progress

- Streamlit reviewer candidate implementation on `m3-streamlit-operations-console`.
- Streamlit-specific CI safety/startup smoke.
- Remote Streamlit Community Cloud deployment after CI passes.

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

- Streamlit candidate has not yet completed GitHub Actions validation or remote Community Cloud smoke.
- The M3 reviewer read model is still synthetic rather than backed by live durable stores.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration are outstanding.

## Next Recommended Action

Run CI on `m3-streamlit-operations-console`. If quality, Streamlit safety smoke and Streamlit startup smoke pass, deploy the candidate branch to Streamlit Community Cloud using `apps/reviewer-streamlit/streamlit_app.py` with Python 3.11. Verify the rendered page remains `SYNTHETIC_READ_ONLY`, approved real sources `0`, real acquisition `BLOCKED`, beneficiary matching `BLOCKED` and `NO_REAL_PII`. Keep `main` untouched.
