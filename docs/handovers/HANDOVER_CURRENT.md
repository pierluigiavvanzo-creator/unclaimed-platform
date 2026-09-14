# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Historical Vercel backend candidate: `m3-vercel-backend-preview`
- Historical Streamlit candidate branch: `m3-streamlit-operations-console`
- Streamlit candidate base canonical SHA: `a0ee1583187248c3deab52b7944a7c4f961bc8e8`
- Verified Streamlit implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`
- Documentation closure SHA: `c75adff971da6132cbcc54fab185b2ff6470e047`
- Never develop directly on `main`; promote verified checkpoints only after explicit owner approval.

The Streamlit candidate was promoted by fast-forward into `m2-state-governance-core` after explicit owner approval. The candidate was 2 commits ahead and 0 behind canonical before promotion.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Streamlit M3 Operations Console CANONICAL + CI VERIFIED + REMOTE SMOKE PASS.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- `sources/registry.yaml` has no approved real source.
- Supabase untouched.
- `main` unchanged.

## Deployment decision

On 2026-09-14 the owner explicitly directed the project to abandon Vercel and move to Streamlit. D-006 and ADR-0005 record the decision.

Reason: repeated Vercel connector/project/deployment visibility inconsistencies made the two-deployment preview path operationally expensive without improving product value.

The existing Next.js/Vercel implementation is retained as rollback/history. It is no longer on the critical path.

## Canonical Streamlit reviewer

Canonical branch: `m2-state-governance-core`.
Verified implementation SHA: `f9042839296cca256c1c886f4b1667caa3f2a532`.
Documentation closure SHA: `c75adff971da6132cbcc54fab185b2ff6470e047`.
GitHub Actions implementation run: `34812099385` — PASS.
GitHub Actions documentation run: `34812289869` — PASS.
Remote URL: `https://unclaimed-platform-hlirhsqfxbfwjs7jhbsxn6.streamlit.app/`.
Remote visual/content smoke: PASS based on owner-provided screenshot on 2026-09-14.

Canonical scope:

- `apps/reviewer-streamlit/streamlit_app.py` — Streamlit Community Cloud entrypoint;
- `apps/reviewer-streamlit/requirements.txt` — deployment dependencies with Streamlit 1.63.0 pinned;
- `src/unclaimed_platform/ui/streamlit_console.py` — typed fail-closed adapter over the existing M3 reviewer snapshot;
- smoke tests for safe state and unsafe real-source rejection;
- GitHub Actions Streamlit startup smoke;
- ADR-0005 and REUSE FIRST audit.

No snapshot payload is duplicated in Streamlit. The app loads the existing typed Python reviewer read model and refuses to render if safety invariants are violated.

## CI evidence

GitHub Actions run `34812099385` on exact implementation SHA `f9042839296cca256c1c886f4b1667caa3f2a532`:

- job `quality`: PASS;
- job `streamlit-candidate`: PASS;
- Ruff: PASS;
- mypy: PASS — 19 source files;
- contract tests: 18 passed;
- smoke tests: 5 passed;
- full pytest: 55 passed;
- known dependency warnings: 2 non-blocking FastAPI/Starlette/AnyIO deprecations;
- Streamlit 1.63.0 install: PASS on Python 3.11.16;
- Streamlit safety smoke: 2 passed;
- Streamlit startup smoke: PASS using `/_stcore/health`;
- existing Next.js lint/type/build regression gates: PASS.

GitHub Actions run `34812289869` on documentation closure SHA `c75adff971da6132cbcc54fab185b2ff6470e047`: PASS for both `quality` and `streamlit-candidate`.

## Remote smoke evidence

Owner screenshot from the deployed Streamlit page confirms:

- page renders `M3 Operations Console`;
- `SYNTHETIC READ ONLY`;
- source text `authoritative typed Python read model`;
- approved real sources `0`;
- real acquisition `BLOCKED`;
- beneficiary matching `BLOCKED`;
- privacy gate `PASS SYNTHETIC ONLY`;
- source approval `BLOCKED NO REAL SOURCE`;
- retention `REQUIRED`;
- PII mode `NO REAL PII`;
- no visible Streamlit/framework runtime error.

Remote smoke: PASS.

## Safety boundaries still in force

Do not enable without later explicit gates:

- real California acquisition;
- beneficiary matching on real data;
- real claimant/beneficiary/decedent/family PII;
- autonomous outreach;
- legal determinations;
- claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.

## SINGLE NEXT ACTION

Prepare the next bounded M3 source-governance proposal for the California SCO public bulk candidate. This is preparation only: do not approve a real source, do not acquire real data, and do not enable beneficiary matching or real PII.

Keep `main` untouched. A promotion to `main` remains a separate explicit stable-checkpoint gate.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 governance/raw persistence: CANONICAL + VERIFIED
Streamlit Operations Console: CANONICAL + CI VERIFIED + REMOTE SMOKE PASS
Vercel active path: ABANDONED BY OWNER
Streamlit implementation SHA: f9042839296cca256c1c886f4b1667caa3f2a532
Streamlit implementation CI: 34812099385 PASS
Streamlit documentation CI: 34812289869 PASS
Streamlit remote deploy: VERIFIED
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Supabase: UNTOUCHED
main: UNCHANGED
NEXT: prepare California SCO source-governance proposal only; no approval/acquisition
CONTEXT HEALTH: coherent; repository is source of truth
```
