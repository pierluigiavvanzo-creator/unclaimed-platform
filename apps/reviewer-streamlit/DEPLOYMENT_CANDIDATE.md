# MVP-1 Reviewer Deployment Candidate Checklist

Date: 2026-09-18

Status: `READY_OFFLINE_NOT_REMOTELY_DEPLOYED`

Classification: `A — Product Critical`

## Candidate coordinates

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Branch: `mvp1-ny-reviewer-deployment-candidate-offline`
- Entrypoint: `apps/reviewer-streamlit/streamlit_app.py`
- Dependency file: `apps/reviewer-streamlit/requirements.txt`
- Python: `3.11`
- Secrets: none required
- Rollback baseline: `6b14edfa39aab0c9bfe7be840820859075c7a708`

## Offline exit checks

- [x] Streamlit entrypoint exists in repository.
- [x] Requirements file is colocated with the entrypoint.
- [x] Streamlit dependency is pinned.
- [x] FastAPI dependency used by the in-process reviewer read model is pinned.
- [x] Pydantic dependency used by typed contracts is pinned.
- [x] Python deployment version is explicitly specified as 3.11 in deployment instructions.
- [x] No `packages.txt` is needed for the current pure-Python reviewer surface.
- [x] No secrets are required for the synthetic-only candidate.
- [x] CI startup smoke launches the exact Streamlit entrypoint from repository root.
- [x] CI health check uses `/_stcore/health`.
- [x] Product-facing title uses MVP-1 reviewer language.
- [x] Synthetic/test-only scope is visible above the reviewer content.
- [x] Ready economics monetary values are labeled synthetic.
- [x] Blocked machine/data cost is labeled synthetic and `NOT FULLY LOADED`.
- [x] Automatic commercial recommendation remains absent.
- [x] Real acquisition remains blocked.
- [x] Owner Name File download remains unauthorized.
- [x] Real owner PII remains disabled.
- [x] Gate 2 remains ungranted.

## Remote deployment coordinates to enter

In Streamlit Community Cloud:

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `mvp1-ny-reviewer-deployment-candidate-offline`
- main file path: `apps/reviewer-streamlit/streamlit_app.py`
- Python version: `3.11`

Do not enter secrets for this candidate.

## Remote verification required after deployment

A remote deployment is not considered verified until:

- the final `streamlit.app` URL is recorded;
- remote page title and safety banner are visible;
- READY synthetic economics card renders;
- FAIL-CLOSED synthetic economics card renders;
- no runtime exception appears;
- no real-source or PII state is enabled;
- screenshot or equivalent remote evidence is recorded;
- canonical `PROJECT_STATE.md`, `ROADMAP.md` and handover are updated.

## Rollback

If the remote candidate fails before any real-data authorization changes, deploy the previous verified Streamlit state from:

`6b14edfa39aab0c9bfe7be840820859075c7a708`

Do not fix remote deployment by weakening safety validators, removing synthetic labels, broadening privacy scope, or enabling Gate 2.
