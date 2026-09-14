# PROJECT_STATE.md

Last updated: 2026-09-14

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED. M3 source/legal readiness, A01 acquisition contracts/adapters,
immutable raw-storage/provenance persistence, privacy/data-minimization gates, California SCO source
governance, approval-readiness evidence, and the transport-preflight proposal are canonical and CI
verified on `m2-state-governance-core`.

Streamlit Community Cloud is the only active reviewer deployment target represented by repository
runtime configuration. Repository-side Vercel deployment integration has been decommissioned under
D-007: `apps/reviewer-console/vercel.json` is removed, active application/runtime/configuration
surfaces contain no Vercel references, and a contract guardrail rejects reintroduction. The legacy
Next.js reviewer remains provider-neutral for local/regression use only.

The M3 reviewer read contract is now version `2.0.0`. The major-version bump explicitly removes the
historical provider-specific platform field while preserving the synthetic/read-only safety model.

The California SCO public bulk source remains `enabled: false` and `approved_for_use: false`.
The source-access policy remains `PROPOSED` and non-authorizing. The canonical transport proposal
enforces `network_execution_authorized: false`, `network_request_performed: false`,
`response_body_bytes_allowed: 0`, no response-body persistence/parsing, no dataset persistence,
no real PII processing, no beneficiary matching, and no outreach.

`main` remains unchanged at `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.
Supabase remains untouched.

## Completed and Verified

- M0 repository foundation and Windows development harness.
- M1 versioned machine contracts and A00-A23 registry.
- M2 deterministic state/governance core, budget ledger and SHA-256 audit chain.
- M3 California source/legal readiness and fail-closed A01 acquisition boundary.
- M3 immutable SHA-256 raw persistence and deterministic provenance records.
- M3 privacy/data-minimization gate with trusted policy separated from caller context.
- Streamlit reviewer canonical, CI verified and remotely validated.
- California SCO source registry canonical, disabled and not approved.
- `SourceAccessGovernance` v1, `SourceApprovalReadiness` v1 and
  `SourceTransportPreflightProposal` v1 canonical.
- California SCO policy remains `PROPOSED` / non-authorizing.
- Repository-side Vercel runtime/deploy configuration decommissioned.
- Reviewer contract upgraded to v2.0.0 to remove the provider-specific platform field.
- Guardrail `tests/contract/test_no_vercel_runtime_integration.py` scans `.github`, `apps`,
  `scripts`, `src`, `schemas/ui` and root runtime configuration for forbidden Vercel paths/references.

## Verification Evidence

- SCO governance SHA: `463c6d6c972fa955a8aa0d3c97208c3029e202a8`.
- SCO approval-readiness SHA: `73c6ffc130fdeffad7fb5cdaf86fa2185b8853a6`.
- SCO transport-preflight proposal SHA: `171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`.
- Transport-preflight proposal candidate CI `34832293876`: PASS.
- Transport-preflight proposal canonical CI `34835032368`: PASS.
- Vercel-decommission candidate exploratory run `34836335576`: FAIL as designed; guardrail found
  four residual active references, which were then removed rather than allowlisted.
- Vercel-decommission corrected candidate CI `34836721955`: PASS.
- Vercel-decommission canonical CI `34836845879`: PASS.
- Ruff, mypy, contract tests, smoke tests, full pytest: PASS.
- Legacy frontend lint/typecheck/build regression gates: PASS.
- Streamlit safety/startup smoke: PASS.
- Source registry approved real sources: `0`.
- No real dataset retrieval or row parsing performed.
- No transport-preflight request to a download endpoint has been executed.

## Blocked / Not Authorized

- Executing a California SCO transport preflight without a separate explicit owner gate.
- Real California acquisition.
- Moving the California SCO source-access policy from `PROPOSED` to `APPROVED` without a separate
  human gate.
- Enabling the SCO registry entry for real use.
- Persisting or parsing any response body during a transport preflight.
- California CSV row assumptions or parsing based on invented layout.
- Beneficiary matching on real data.
- Real claimant/beneficiary/decedent/family PII.
- Outreach, claimant verification, fee agreements and claim submission.
- Reintroducing a Vercel repository/runtime integration without a new explicit owner decision.
- Promotion to `main` without a separate explicit stable-checkpoint gate.
- Supabase resource creation without a separate organization/cost/architecture gate.

## Known Issues / Unresolved Readiness Items

- Exact SCO download endpoint remains unverified.
- Request method, timeout, redirect limit, approved host allowlist, execution approval reference,
  observed HTTP status, final host, content type and content length remain unresolved.
- No downloaded artifact hash/revision exists because no real artifact has been acquired.
- CSV row layout/field names remain unknown.
- Processing purpose, data categories, minimized fields, PII necessity and retention policy remain
  intentionally unresolved.
- Filesystem raw immutability is application-level, not provider WORM/object lock.
- M2 audit writer remains in-memory; durable production audit persistence is outstanding.
- Retention physical enforcement and PostgreSQL/Alembic initial application migration are outstanding.
- An external Vercel Git/project integration, if still connected outside repository contents, can
  continue receiving GitHub push events until disconnected provider-side; repository cleanup alone
  cannot revoke that external account connection.
- Known non-blocking dependency/runtime deprecation warnings remain in CI.

## Next Recommended Action

**Do not execute the SCO transport preflight yet.** First confirm that any external Vercel project/Git
integration associated with this repository is disconnected if failed-deployment notifications
continue. Repository-side Vercel integration is now removed and CI-guarded.

After the external-notification issue is resolved or confirmed absent, the next product gate returns
to the existing human decision: whether to authorize one bounded California SCO metadata-only
transport-preflight execution under the canonical proposal.
