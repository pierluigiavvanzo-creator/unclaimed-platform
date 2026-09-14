# M3 Repository-Side Deployment Provider Decommission

Date: 2026-09-14

Status: **CANDIDATE — REPOSITORY RUNTIME CLEANUP**

## Objective

Remove every active repository-side configuration or executable instruction that can intentionally configure or invoke the historical Vercel deployment path, while preserving non-executable architectural history.

## Scope

This candidate:

- deletes `apps/reviewer-console/vercel.json`;
- removes provider-specific deployment instructions from `apps/reviewer-console/README.md`;
- keeps the legacy Next.js reviewer only as a provider-neutral local/regression artifact;
- adds `tests/contract/test_no_vercel_runtime_integration.py` to block reintroduction of Vercel-named files or textual Vercel references in active runtime surfaces;
- records D-007 in `DECISIONS.md`.

The test scans active runtime/configuration roots only:

- `.github/`;
- `apps/`;
- `scripts/`;
- `src/`;
- `.env.example`;
- `pyproject.toml`;
- `docker-compose.yml`.

Historical material under `docs/` and architectural decision history may still mention Vercel. Those files are not executable deployment configuration and are intentionally preserved.

## Why the legacy Next.js app is not deleted

The Next.js reviewer has no Vercel SDK dependency or Vercel CLI command in `package.json`; it remains useful for local regression/history. Deleting it would not disconnect an external Git integration and, if an external project still points to that directory, could cause additional provider-side build failures rather than stop notifications.

## External integration boundary

Repository contents cannot revoke an already-installed provider-side Git integration, project connection, webhook, or account-level notification policy. If Vercel remains connected to this GitHub repository outside the repository tree, it can continue receiving push events until that provider/GitHub integration is explicitly disconnected.

The repository cleanup therefore removes all intentional repo-side Vercel runtime configuration but does not claim that an external provider connection has been revoked.

## Acceptance criteria

1. `apps/reviewer-console/vercel.json` is absent.
2. No file/path under active runtime surfaces contains the string `vercel` (case-insensitive).
3. No Vercel CLI/deploy/config/token/project identifiers exist in active runtime surfaces.
4. Historical docs remain intact.
5. Ruff, mypy, contract tests, smoke tests, full pytest, legacy frontend regression build, and Streamlit smoke remain green.
6. `main` remains untouched.

## Rollback

Use a normal history-preserving revert. Do not force-push.
