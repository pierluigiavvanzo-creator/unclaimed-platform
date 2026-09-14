# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Historical Vercel backend candidate: `m3-vercel-backend-preview`
- Current Streamlit candidate: `m3-streamlit-operations-console`
- Streamlit candidate base canonical SHA: `a0ee1583187248c3deab52b7944a7c4f961bc8e8`
- Never develop directly on `main`; promote verified checkpoints only after explicit owner approval.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Historical M3 Operations Console CANONICAL + CI VERIFIED.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- `sources/registry.yaml` has no approved real source.
- Supabase untouched.
- `main` unchanged.

## Deployment decision change

On 2026-09-14 the owner explicitly directed the project to abandon Vercel and move to Streamlit. D-006 and ADR-0005 record the decision.

Reason: repeated Vercel connector/project/deployment visibility inconsistencies made the two-deployment preview path operationally expensive without improving product value.

The existing Next.js/Vercel implementation is retained as rollback/history until the Streamlit candidate passes CI and remote smoke. It is no longer on the critical path.

## Streamlit candidate

Branch: `m3-streamlit-operations-console`.
Base: canonical `a0ee1583187248c3deab52b7944a7c4f961bc8e8`.

Candidate scope:

- `apps/reviewer-streamlit/streamlit_app.py` — Streamlit Community Cloud entrypoint;
- `apps/reviewer-streamlit/requirements.txt` — deployment dependencies with Streamlit 1.63.0 pinned;
- `src/unclaimed_platform/ui/streamlit_console.py` — typed fail-closed adapter over the existing M3 reviewer snapshot;
- smoke tests for safe state and unsafe real-source rejection;
- GitHub Actions Streamlit startup smoke;
- ADR-0005 and REUSE FIRST audit.

No snapshot payload is duplicated in Streamlit. The app loads the existing typed Python reviewer read model and refuses to render if safety invariants are violated.

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

Wait for GitHub Actions on `m3-streamlit-operations-console`. If quality, Streamlit safety smoke and startup smoke pass, deploy that branch to Streamlit Community Cloud using:

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-streamlit-operations-console`
- entrypoint: `apps/reviewer-streamlit/streamlit_app.py`
- Python: `3.11`

Then perform remote smoke and verify `SYNTHETIC_READ_ONLY`, approved real sources `0`, acquisition/matching `BLOCKED`, `NO_REAL_PII`, and no framework/runtime error.

Keep `main` untouched. Promotion to canonical requires the normal explicit owner gate after verification.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 governance/raw persistence: CANONICAL + VERIFIED
Historical Next.js Operations Console: CANONICAL + CI VERIFIED
Vercel active path: ABANDONED BY OWNER
Streamlit candidate: IMPLEMENTED, CI PENDING
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Supabase: UNTOUCHED
main: UNCHANGED
NEXT: CI -> Streamlit Community Cloud deploy -> remote smoke -> promotion gate
CONTEXT HEALTH: coherent; repository is source of truth
```
