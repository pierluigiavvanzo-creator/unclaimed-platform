# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical Vercel-decommission SHA before this documentation closure:
  `fe8c27e536b2bf86a7bfe8c4f9af0bf31052f54d`
- Stable `main` HEAD: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Promoted SCO governance candidate: `m3-ca-sco-source-governance`
- Promoted SCO approval-readiness candidate: `m3-ca-sco-approval-readiness`
- Promoted SCO transport-preflight proposal candidate: `m3-ca-sco-transport-preflight-proposal`
- Promoted repository cleanup candidate: `maintenance-decommission-vercel-runtime`
- Never develop directly on `main`; promote verified checkpoints only after the applicable owner gate.

## Verified baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Streamlit M3 reviewer CANONICAL + CI VERIFIED + prior REMOTE FUNCTIONAL/VISUAL SMOKE PASS.
- California SCO source governance CANONICAL + CI VERIFIED.
- California SCO approval-readiness evidence CANONICAL + CI VERIFIED.
- California SCO transport-preflight proposal CANONICAL + CI VERIFIED.
- Repository-side Vercel runtime/deployment integration DECOMMISSIONED + CI VERIFIED.
- Reviewer read contract is v2.0.0 and provider-neutral.
- SCO registry remains `enabled: false` and `approved_for_use: false`.
- SCO source-access policy remains `PROPOSED`; real acquisition authorization remains `false`.
- Approved real source count remains `0`.
- No California dataset has been downloaded or parsed.
- No transport-preflight request has been executed against a SCO download endpoint.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

## Repository-side Vercel decommission

Owner requested removal of every repository-side direct or indirect Vercel connection/command after
continued failed-deployment notifications.

Candidate branch:
`maintenance-decommission-vercel-runtime`

Final promoted SHA:
`fe8c27e536b2bf86a7bfe8c4f9af0bf31052f54d`

Canonical changes include:

- removed `apps/reviewer-console/vercel.json`;
- removed provider-specific deployment instructions from active app docs;
- removed the provider-specific platform field from FastAPI, JSON Schema, Next.js types/fallback/UI;
- bumped the reviewer read contract from v1.0.0 to v2.0.0 because removal of a required field is a
  breaking shape change;
- kept the old Next.js reviewer provider-neutral for local/regression use only;
- updated Streamlit docs to canonical branch and active-host wording;
- added `tests/contract/test_no_vercel_runtime_integration.py`.

The guardrail scans active runtime/configuration surfaces:

- `.github/`;
- `apps/`;
- `scripts/`;
- `src/`;
- `schemas/ui/`;
- root `.env.example`, `pyproject.toml`, `docker-compose.yml`.

It rejects Vercel-named runtime paths and any textual Vercel reference in those active surfaces.
Historical `docs/`/ADR/audit records may retain the name because they are inert project history.

## Decommission verification

Initial candidate run `34836335576` failed as designed. The new guardrail found residual active
references in:

- `apps/reviewer-console/src/app/page.tsx`;
- `apps/reviewer-console/src/lib/operations.ts`;
- `apps/reviewer-streamlit/README.md`;
- `src/unclaimed_platform/api/reviewer.py`.

Those references were removed rather than exempted.

Corrected candidate CI run `34836721955`: PASS.
Canonical post-promotion CI run `34836845879`: PASS.

Verified gates:

- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- Vercel active-surface guardrail PASS;
- smoke tests PASS;
- full pytest PASS;
- legacy Next.js lint/typecheck/build regression gates PASS;
- Streamlit safety smoke PASS;
- Streamlit startup smoke PASS.

## External Vercel connection boundary

Repository cleanup cannot revoke an already-existing Vercel account/project Git integration, GitHub
App installation, webhook, or notification rule managed outside repository contents. If failed Vercel
deployment messages continue after this canonical cleanup, that is evidence that a provider-side
connection still exists and it must be disconnected separately.

Do not claim the external connection has been removed unless it is actually verified through Vercel
or the relevant GitHub integration settings.

## California SCO transport-preflight state

Canonical proposal SHA:
`171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3`

Candidate CI `34832293876`: PASS.
Canonical post-promotion CI `34835032368`: PASS.

The proposal remains deliberately non-executable and requires:

- `network_execution_authorized = false`;
- `network_request_performed = false`;
- `acquisition_performed = false`;
- `source_approved = false`;
- `source_enabled = false`;
- `response_body_bytes_allowed = 0`;
- no response-body persistence/parsing;
- no dataset persistence;
- no real PII;
- no beneficiary matching;
- no outreach.

## Unresolved transport controls

Do not invent or silently fill:

- exact SCO download endpoint;
- request method;
- timeout;
- redirect limit;
- approved host allowlist;
- execution approval reference;
- observed HTTP status/final host/content type/content length.

The advertised host `claimit.ca.gov` remains evidence only and is not automatically an approved
allowlist entry.

## SINGLE NEXT ACTION

**Operational cleanup gate first:** verify whether failed Vercel deployment notifications continue
after repository-side decommission. If they continue, disconnect the external Vercel project/Git
integration associated with `pierluigiavvanzo-creator/unclaimed-platform` before making further
project pushes.

This external connection is not stored in repository files and cannot be proven removed by the
repository guardrail alone.

Only after that notification/integration issue is resolved, return to the product human gate:
owner decision on whether to authorize one bounded California SCO metadata-only transport preflight.
Do not execute that preflight without a new explicit approval.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
M3 SCO approval readiness: CANONICAL + CI VERIFIED
M3 SCO transport-preflight proposal: CANONICAL + CI VERIFIED
Repository-side Vercel integration: DECOMMISSIONED + CI VERIFIED
Reviewer read contract: 2.0.0 PROVIDER-NEUTRAL
Vercel decommission SHA: fe8c27e536b2bf86a7bfe8c4f9af0bf31052f54d
Vercel corrected candidate CI: 34836721955 PASS
Vercel canonical CI: 34836845879 PASS
SCO transport proposal SHA: 171dc2e55f85b89f1bba81b1cc676d0ed2b7f3d3
SCO registry: DISABLED + NOT APPROVED
SCO policy: PROPOSED + NON-AUTHORIZING
Approved real sources: 0
Transport preflight execution: BLOCKED PENDING EXPLICIT OWNER APPROVAL
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: verify/disconnect external Vercel Git/project integration if notifications continue
AFTER THAT: owner decision on one bounded metadata-only SCO transport preflight
CONTEXT HEALTH: coherent; repository is source of truth
```
