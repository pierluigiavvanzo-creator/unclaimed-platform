# ADR-0005 — Streamlit reviewer deployment target

Date: 2026-09-14
Status: Accepted by owner; implementation candidate CI verified, remote smoke pending

## Context

ADR-0004 selected Next.js + Vercel as the preferred reviewer preview stack while keeping FastAPI and versioned contracts authoritative. The frontend itself rendered successfully, but repeated Vercel connector/deployment inconsistencies prevented reliable project/deployment visibility and backend wiring. The owner explicitly directed the project to abandon Vercel and move the reviewer surface to Streamlit.

## Decision

1. Use Streamlit Community Cloud as the current deployment target for the M3 reviewer Operations Console.
2. Keep deterministic governance, versioned contracts and the existing typed Python reviewer snapshot authoritative. Streamlit is a server-side presentation adapter only.
3. The Streamlit candidate may consume the typed Python read model in-process, avoiding a second preview backend and eliminating `REVIEWER_API_BASE_URL` from the deployment path.
4. Preserve the existing Next.js/Vercel implementation as rollback/history until the Streamlit candidate passes remote smoke; do not delete it in this task.
5. Keep the Streamlit candidate synthetic/read-only and fail closed if real sources, real acquisition, beneficiary matching or real PII appear.
6. Do not introduce Supabase or any new data plane as part of this migration.

## Verification

Implementation SHA `f9042839296cca256c1c886f4b1667caa3f2a532` passed GitHub Actions run `34812099385`:

- Ruff PASS;
- mypy PASS on 19 source files;
- 18 contract tests passed;
- 5 smoke tests passed;
- 55 full tests passed;
- Streamlit safety smoke 2 passed;
- Streamlit server startup and `/_stcore/health` PASS;
- existing Next.js regression lint/type/build PASS.

Remote Streamlit Community Cloud deployment is not yet verified.

## Reason

This reduces deployment complexity and user operating time while preserving the existing governance boundaries. Community Cloud can deploy directly from the GitHub repository and supports an entrypoint in a subdirectory plus a local requirements file.

## Alternatives considered

- Continue diagnosing Vercel: rejected for the current milestone because repeated create/read inconsistencies consumed time without increasing usable product value.
- Keep Next.js locally only: preserves UI code but does not solve the hosted product-visibility requirement.
- FastAPI server-rendered templates: viable but requires custom presentation work and hosting configuration that Streamlit already provides.
- Gradio: mature Python UI option, but the current reviewer surface is dashboard/status oriented rather than model-demo oriented.

## Consequences

- `apps/reviewer-streamlit` becomes the active M3 reviewer deployment candidate.
- Vercel-specific backend-preview work is no longer on the critical path.
- FastAPI remains available for API consumers and later service separation; Streamlit does not become governance authority.
- A later production-grade UI decision may supersede Streamlit if product requirements outgrow the internal reviewer use case.
- `main` remains unchanged until a separate milestone promotion gate.

## External evidence

- Streamlit Community Cloud deploy: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
- Dependency handling: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
- Repository/file organization: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization
- Streamlit 1.63.0 release: https://pypi.org/project/streamlit/
