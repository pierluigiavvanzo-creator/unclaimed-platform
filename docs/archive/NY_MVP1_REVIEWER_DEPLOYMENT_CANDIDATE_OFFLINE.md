# NY MVP-1 Reviewer Deployment Candidate — Offline Readiness

Date: 2026-09-18

Classification: `A — Product Critical`

## Objective

Prepare the verified integrated MVP-1 Streamlit reviewer as an explicit deployment candidate without performing or claiming a remote deployment.

## Current official Streamlit deployment assumptions verified

Current Streamlit Community Cloud documentation confirms:

- an entrypoint may live in a repository subdirectory;
- a `requirements.txt` may live beside the entrypoint;
- Community Cloud executes from the repository root;
- Python version is selected in deployment advanced settings;
- the project should use the same Python version in deployment as development;
- pinning Streamlit is recommended to avoid unexpected upgrades.

The project therefore keeps:

- entrypoint: `apps/reviewer-streamlit/streamlit_app.py`;
- colocated requirements: `apps/reviewer-streamlit/requirements.txt`;
- deployment Python: `3.11`.

No external Linux package dependency is required, so no `packages.txt` is added.

## Dependency reproducibility

The candidate pins the exact versions exercised by the verified CI environment:

- Streamlit 1.63.0;
- FastAPI 0.141.1;
- Pydantic 2.13.5.

This is intentionally narrower than the root development dependency ranges because the deployment candidate should not silently resolve a new reviewer runtime during remote deployment.

## Product-facing wording

Legacy page wording `M3 Operations Console` was replaced on the active Streamlit page with:

`MVP-1 Reviewer Console`

M3 milestone/governance data remains visible where it is part of the underlying historical/readiness snapshot; only the product-facing surface title was aligned.

## Synthetic/test-only disclosure

The page now has an above-content banner:

`Synthetic/test-only deployment candidate.`

It explicitly states that there is:

- no real acquisition;
- no Owner Name File download;
- no beneficiary matching;
- no real PII.

Ready monetary fields are labeled synthetic. The blocked direct machine/data cost is also labeled synthetic and remains marked `NOT FULLY LOADED`.

## Startup contract

The existing CI runs the app from repository root using:

`python -m streamlit run apps/reviewer-streamlit/streamlit_app.py --server.headless true --server.port 8501`

and checks:

`http://127.0.0.1:8501/_stcore/health`

This matches Community Cloud's repository-root execution model.

## Rollback

Rollback baseline:

`6b14edfa39aab0c9bfe7be840820859075c7a708`

No safety or authorization change is required to rollback.

## Remote boundary

This work does not perform remote deployment.

A remote deployment may be declared only after a real `streamlit.app` URL exists and the rendered candidate is remotely verified.

Gate 2 remains ungranted. No Owner Name File, real owner PII, outreach, fee agreement, representation or claim activity is enabled.
