# M3 Repository-Side Deployment Provider Decommission

Date: 2026-09-14

Status: **CANONICAL + CI VERIFIED**

## Objective

Remove every active repository-side configuration or executable instruction that can intentionally
configure or invoke the historical Vercel deployment path, while preserving non-executable
architectural history.

## Canonical changes

The decommission:

- deletes `apps/reviewer-console/vercel.json`;
- removes provider-specific deployment instructions from active application documentation;
- removes the provider-specific platform field from the FastAPI reviewer model, JSON Schema and
  legacy Next.js read model/UI;
- upgrades the reviewer read contract from v1.0.0 to v2.0.0 because removing a required field is a
  breaking contract change under the repository compatibility policy;
- keeps the legacy Next.js reviewer only as provider-neutral local/regression code;
- adds `tests/contract/test_no_vercel_runtime_integration.py` to block reintroduction of Vercel-named
  paths or textual references in active runtime/configuration surfaces;
- records D-007 in `DECISIONS.md`.

The guardrail scans:

- `.github/`;
- `apps/`;
- `scripts/`;
- `src/`;
- `schemas/ui/`;
- `.env.example`;
- `pyproject.toml`;
- `docker-compose.yml`.

Historical material under `docs/` and decision history may still mention Vercel. Those files are
non-executable records and are intentionally preserved.

## Discovery from the first guardrail run

Candidate run `34836335576` failed at the new contract test, correctly identifying four residual
active references:

1. `apps/reviewer-console/src/app/page.tsx`;
2. `apps/reviewer-console/src/lib/operations.ts`;
3. `apps/reviewer-streamlit/README.md`;
4. `src/unclaimed_platform/api/reviewer.py`.

The failure was treated as evidence, not bypassed. All four references were removed. The UI schema was
also brought inside the guardrail scan and the Streamlit adapter/tests were updated for reviewer
contract v2.0.0.

## Verification

Candidate branch: `maintenance-decommission-vercel-runtime`.

Final promoted SHA:
`fe8c27e536b2bf86a7bfe8c4f9af0bf31052f54d`

Evidence:

- exploratory guardrail CI `34836335576`: FAIL as designed on residual active references;
- corrected candidate CI `34836721955`: PASS;
- canonical post-promotion CI `34836845879`: PASS;
- Ruff PASS;
- mypy PASS;
- contract tests PASS, including active-surface provider guardrail;
- smoke tests PASS;
- full pytest PASS;
- legacy Next.js lint/typecheck/build regression gates PASS;
- Streamlit safety/startup smoke PASS.

## External integration boundary

Repository contents cannot revoke an already-installed provider-side Git integration, project
connection, webhook, or account-level notification policy. If Vercel remains connected to this GitHub
repository outside the repository tree, it can continue receiving push events until that provider-side
connection is explicitly disconnected.

Therefore the repository decommission is complete, but it does not claim that an external Vercel
account/project connection has been revoked.

## Acceptance criteria result

1. `apps/reviewer-console/vercel.json` absent — PASS.
2. No Vercel reference in guarded active runtime/configuration surfaces — PASS.
3. No Vercel CLI/deploy/config/token/project identifier in guarded active surfaces — PASS.
4. Historical documentation preserved — PASS.
5. All repository CI/regression gates green — PASS.
6. `main` untouched — PASS.

## Rollback

Use a normal history-preserving revert. Do not force-push. Reintroducing Vercel repository/runtime
deployment support requires a new explicit owner decision and corresponding governance/test update.
