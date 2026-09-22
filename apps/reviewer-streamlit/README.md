# MVP-1 Streamlit Reviewer Console

Deployment-candidate Streamlit surface for the Unclaimed Insurance Platform MVP-1 reviewer.

## Candidate state

`READY_OFFLINE_NOT_REMOTELY_DEPLOYED`

This surface is synthetic/test-only. It must not enable or imply:

- real source acquisition;
- NY OSC Owner Name File download;
- beneficiary matching;
- real owner PII processing;
- outreach;
- fee agreement execution;
- representation;
- claim activity.

The UI consumes the existing typed Python read models in-process and fails closed if reviewer safety invariants are violated.

## Deployment coordinates

Use these coordinates for Streamlit Community Cloud:

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `mvp1-ny-reviewer-deployment-candidate-offline`
- entrypoint: `apps/reviewer-streamlit/streamlit_app.py`
- Python: `3.11`
- dependency file: `apps/reviewer-streamlit/requirements.txt`
- secrets: none required for this synthetic-only candidate

Do not deploy from the historical `m2-state-governance-core` branch for this MVP-1 candidate.

## Dependency policy

The deployment-candidate requirements are pinned to the versions exercised by the verified GitHub CI environment:

- `streamlit==1.63.0`
- `fastapi==0.141.1`
- `pydantic==2.13.5`

This avoids an unreviewed dependency re-resolution at deployment time.

## Local startup contract

Run from the repository root so Community Cloud path behavior is reproduced locally:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r apps/reviewer-streamlit/requirements.txt
python -m streamlit run apps/reviewer-streamlit/streamlit_app.py --server.headless true --server.port 8501
```

Health check:

```text
http://127.0.0.1:8501/_stcore/health
```

The GitHub CI already executes the same entrypoint and health endpoint as a startup smoke.

## Required visible labels

A deployment candidate is acceptable only when the rendered page visibly includes:

- `MVP-1 Reviewer Console`;
- `Synthetic/test-only deployment candidate`;
- `MVP-1 SYNTHETIC CASE`;
- `NY PRE-CONTACT ECONOMICS`;
- `MVP-1 INTEGRATED ECONOMICS — SYNTHETIC TEST`;
- `MVP-1 INTEGRATED ECONOMICS — SYNTHETIC TEST / FAIL CLOSED`;
- `NONE — HUMAN DECISION REQUIRED`.

Any monetary values in the ready/blocked demonstration remain synthetic test fixtures.

## Rollback

Rollback baseline before deployment-candidate preparation:

`6b14edfa39aab0c9bfe7be840820859075c7a708`

Branch:

`mvp1-ny-integrated-economics-reviewer-offline`

If deployment-candidate preparation regresses safety or startup behavior, return to that verified checkpoint rather than weakening guards.

## Remote deployment gate

Remote deployment is a separate action. Do not mark deployment complete until all of the following are observed:

1. a real `streamlit.app` URL exists for this candidate branch;
2. the remote page loads without runtime error;
3. synthetic/test-only labeling is visible;
4. both READY and FAIL-CLOSED integrated economics cards render;
5. real sources remain zero / blocked;
6. no secret or real owner PII is required or displayed;
7. a remote smoke record is written back to the repository.

Current official Streamlit Community Cloud guidance permits an entrypoint in a subdirectory and a requirements file beside that entrypoint. Python version is selected in the deployment dialog; select Python 3.11 for this project.
