# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters, immutable raw-storage/provenance persistence, privacy/data-minimization gates, and the reviewer read contract are implemented and verified on canonical `m2-state-governance-core`.

The owner explicitly abandoned Vercel as the active reviewer deployment path on 2026-09-14 after repeated project/deployment visibility inconsistencies. Streamlit Community Cloud is now the approved M3 reviewer deployment target under D-006 / ADR-0005.

The Streamlit reviewer implementation was verified on commit `f9042839296cca256c1c886f4b1667caa3f2a532`; GitHub Actions run `34812099385` passed both `quality` and `streamlit-candidate`. Documentation closure commit `c75adff971da6132cbcc54fab185b2ff6470e047` also passed GitHub Actions run `34812289869`.

On 2026-09-14 the owner supplied a screenshot from the deployed Streamlit Community Cloud app at `https://unclaimed-platform-hlirhsqfxbfwjs7jhbsxn6.streamlit.app/`. Remote visual/content smoke is PASS: the page renders `M3 Operations Console`, `SYNTHETIC READ ONLY`, approved real sources `0`, real acquisition `BLOCKED`, beneficiary matching `BLOCKED`, privacy `PASS SYNTHETIC ONLY`, source approval `BLOCKED NO REAL SOURCE`, and `NO REAL PII`, with no visible runtime error.

After explicit owner approval, branch `m3-streamlit-operations-console` was promoted by fast-forward into canonical `m2-state-governance-core`.

A Vercel-style Streamlit visual restyle was then implemented on `m3-streamlit-vercel-style-restyle`. The restyle reuses the historical Next.js visual language: navy background, turquoise accents, dark cards, green/amber status pills, compact hero, and custom HTML/CSS rendering while preserving the existing typed reviewer snapshot and fail-closed safety adapter. A rendering regression where Governance HTML appeared as raw code was fixed by switching the page renderer to `st.html()` and adding a regression smoke test.

Final restyle candidate SHA `563128e3f37c14ec2715132ee14cf5813b057cba` passed GitHub Actions run `34817694129` with both `quality` and `streamlit-candidate` successful. The owner-provided final screenshot confirms the title is compact on one line, Governance renders correctly, Streamlit toolbar/status chrome is hidden, and the Vercel-style palette/layout is visible with no runtime error. Visual smoke: PASS.

After explicit owner approval, `m3-streamlit-vercel-style-restyle` was promoted by clean fast-forward into canonical `m2-state-governance-core`; immediately before promotion it was 6 commits ahead and 0 behind canonical with merge-base at `85bb7a71720c9cc3c3145762da8b6eb33e85283a`.

The deployed Streamlit app was manually pointed to `m3-streamlit-vercel-style-restyle` for visual validation. The same code is now canonical, but the Streamlit Community Cloud app should be repointed to `m2-state-governance-core` before treating the live deployment branch as canonical-aligned.

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
- Historical Next.js Operations Console retained as rollback/history; Vercel no longer on the critical path.
- Streamlit reviewer reuses the existing typed reviewer snapshot; no snapshot payload duplication.
- Streamlit fail-closed adapter rejects unsafe state before rendering.
- Streamlit 1.63.0 dependency installation verified on Python 3.11.16.
- Streamlit Community Cloud remote functional/content smoke: PASS.
- Vercel-style Streamlit restyle: CANONICAL + CI VERIFIED + VISUAL SMOKE PASS.
- Final restyle CI run `34817694129`: PASS.

## Verification Evidence

Base Streamlit implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`
Base documentation closure SHA: `c75adff971da6132cbcc54fab185b2ff6470e047`
Base CI runs: `34812099385`, `34812289869`
Final visual restyle SHA: `563128e3f37c14ec2715132ee14cf5813b057cba`
Final visual restyle CI run: `34817694129`
Remote URL: `https://unclaimed-platform-hlirhsqfxbfwjs7jhbsxn6.streamlit.app/`

Evidence:

- Ruff: PASS.
- mypy: PASS.
- contract tests: PASS.
- smoke tests: PASS, including Streamlit safety and visual regression checks.
- full pytest: PASS.
- historical Next.js frontend lint/typecheck/build regression gates: PASS.
- Streamlit startup smoke: PASS via `/_stcore/health`.
- remote Streamlit functional/content smoke: PASS.
- final owner screenshot confirms Vercel-style layout, correct Governance rendering and hidden Streamlit toolbar/status chrome.
- no real source, real acquisition, beneficiary matching or real PII introduced.

## Blocked / Not Authorized

- Real California acquisition.
- Approval of a real source through the reviewer UI.
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Unapproved scraping/restricted-source access.
- Promotion to `main` without a separate explicit human gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Known Issues

- Two known non-blocking FastAPI/Starlette/AnyIO dependency deprecation warnings remain.
- GitHub Actions reports upstream Node runtime deprecation warnings for current actions; workflows pass.
- Historical Next.js dependency install warns that ESLint 9.39.5 is no longer supported; that frontend is no longer on the critical path.
- The M3 reviewer read model is still synthetic rather than backed by live durable stores.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration are outstanding.
- Streamlit Community Cloud is currently pointed at the visual-restyle candidate branch used for remote validation; repoint it to canonical `m2-state-governance-core` to eliminate deploy-branch drift.

## Next Recommended Action

Repoint the existing Streamlit Community Cloud app from `m3-streamlit-vercel-style-restyle` to canonical `m2-state-governance-core`, verify one final remote smoke with the same visual state, then prepare the next bounded M3 source-governance proposal for the California SCO public bulk candidate without approving or acquiring real data. Keep real acquisition, beneficiary matching and real PII blocked. Keep `main` unchanged until a separate explicit stable-checkpoint gate.
