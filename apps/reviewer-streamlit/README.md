# Streamlit M3 Operations Console

Active Streamlit reviewer surface for the M3 governance/provenance slice.

## Safety scope

This app is read-only and synthetic-only. It must not enable real acquisition, beneficiary matching, source approval, outreach or real PII.

The app reuses `unclaimed_platform.ui.streamlit_console`, which in turn loads the existing typed M3 reviewer snapshot and fails closed if safety invariants are violated.

## Local run

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r apps/reviewer-streamlit/requirements.txt
streamlit run apps/reviewer-streamlit/streamlit_app.py
```

## Streamlit Community Cloud deploy

Use:

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m2-state-governance-core`
- entrypoint: `apps/reviewer-streamlit/streamlit_app.py`
- Python: `3.11`

Do not add secrets for this synthetic-only reviewer.

Community Cloud supports entrypoints in subdirectories and requirements files beside the entrypoint. Official documentation:

- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization
