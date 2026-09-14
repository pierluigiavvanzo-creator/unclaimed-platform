# M3 Streamlit Reviewer — REUSE FIRST

Date: 2026-09-14
Task class: A — Product Critical

## Goal

Replace the blocked Vercel preview path with the smallest hosted reviewer surface that preserves the existing M3 read contract and safety boundaries.

## Candidates

### Streamlit Community Cloud

- License/runtime: Streamlit is Apache-2.0 open source; Community Cloud provides managed hosting.
- Maintenance: active; latest PyPI release verified as 1.63.0 on 2026-09-01.
- Python compatibility: Streamlit 1.63.0 requires Python >=3.10; project baseline Python 3.11 is compatible.
- Repository fit: direct GitHub deployment; entrypoint may live in a subdirectory; requirements file may live beside the entrypoint.
- Security/privacy fit: suitable for the current synthetic-only reviewer candidate. No secrets are required.
- Integration cost: low because the current read model is already Python/Pydantic.
- Decision: REUSE.

### Existing Next.js + Vercel surface

- Fit: UI already exists and visual smoke passed.
- Current blocker: unreliable Vercel project/deployment visibility and backend wiring through the available connector.
- Integration cost to continue: unbounded relative to current M3 product value.
- Decision: retain as rollback/history, DEFER as active deployment path.

### FastAPI server-rendered templates

- Fit: would preserve one Python service boundary.
- Cost: requires new template/UI implementation and a separate hosting choice.
- Decision: DEFER.

### Gradio

- Fit: mature Python UI framework, strongest for interactive model/demo workflows.
- Current console fit: weaker than Streamlit for a status/dashboard-style internal reviewer surface.
- Decision: REJECT for this slice.

## Reuse decision

Use Streamlit Community Cloud and reuse the existing typed `synthetic_operations_snapshot()` read model. Do not duplicate the M3 snapshot payload in Streamlit. Add a fail-closed adapter that validates the existing safety invariants before rendering.

## Sources

- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
- https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization
- https://pypi.org/project/streamlit/
