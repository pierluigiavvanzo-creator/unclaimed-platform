# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Promoted SCO transport-evidence baseline:
  `60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a`
- Stable `main` HEAD:
  `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
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
- California SCO bounded transport-preflight execution/evidence CANONICAL + CI VERIFIED.
- Repository-side Vercel runtime/deployment integration DECOMMISSIONED + CI VERIFIED.
- Reviewer read contract v2.0.0 and provider-neutral.
- SCO registry remains `enabled: false` and `approved_for_use: false`.
- SCO source-access policy remains `PROPOSED` and non-authorizing.
- Approved real source count remains `0`.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

## Vercel closure

Repository-side Vercel runtime/deploy support remains decommissioned under D-007. The owner reported
the external Vercel account deleted before authorizing the SCO transport task. No Vercel runtime
integration was reintroduced during transport-evidence promotion.

## California SCO transport execution authorization

The owner explicitly authorized exactly one bounded metadata-only transport preflight after confirming
Vercel account deletion.

Execution approval reference:
`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

The approval did not authorize source use, registry activation, dataset acquisition, response-body
access, PII processing, beneficiary matching, outreach, or downstream legal/commercial action.

## Executed transport preflight

Candidate branch:
`m3-ca-sco-transport-preflight-execution`

Canonical parent before candidate:
`50887231d39eff793b1968b4a062292533205602`

Execution commit:
`7d89ec664992a30b5270be8da4c2616254747e59`

One-shot workflow run:
`34838890387`

- targeted validation: PASS;
- preflight: PASS;
- network execution started only after validation passed.

Evidence commit:
`2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`

Candidate evidence CI:
`34839100497` — PASS.

Candidate closure CI:
`34839373665` — PASS.

Promoted baseline:
`60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a`

Canonical post-promotion CI:
`34840001821` — PASS for both `quality` and `streamlit-candidate`.

The temporary workflow `.github/workflows/ca-sco-transport-preflight-once.yml` was removed before
promotion. Contract tests require it to remain absent, so later pushes cannot repeat the preflight
automatically.

## Observed transport evidence

Observation timestamp:
`2026-09-14T11:34:58.210154Z`

Observed endpoint:
`https://claimit.ca.gov/upd-property-records/00_All_Records.zip`

Observed metadata:

- method: `HEAD`;
- final host: `claimit.ca.gov`;
- HTTP status: `200`;
- redirects: `0`;
- TLS: `https`;
- content type: `application/zip`;
- content length: `3,203,972,130` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"0ce16eb75bbbe7018639c7a71e802008"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:37 GMT`;
- response-body bytes read: `0`.

The public SCO page describes downloadable records as CSV data, but the observed `All properties`
transport object is currently a ZIP resource advertising `application/zip`. The ZIP body was not
downloaded or opened. Do not claim archive contents, internal CSV files, fields, row layout or schema
are known.

Machine-readable evidence:
`sources/evidence/ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json`

Execution schema:
`schemas/common/source_transport_preflight_execution.schema.json`

Runner:
`scripts/ca_sco_transport_preflight.py`

Contract tests:

- `tests/contract/test_ca_sco_transport_preflight_execution.py`
- `tests/contract/test_ca_sco_transport_preflight_observation.py`

Audit:
`docs/audits/M3_CA_SCO_TRANSPORT_PREFLIGHT_EXECUTION.md`

## Safety state after promotion

The canonical evidence requires:

- `acquisition_performed = false`;
- `source_approved = false`;
- `source_enabled = false`;
- `response_body_bytes_read = 0`;
- no response-body persistence/parsing;
- no dataset artifact persistence;
- no real PII processed;
- no beneficiary matching;
- no outreach.

`sources/registry.yaml` remains:

- `enabled: false`;
- `approved_for_use: false`.

`policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json` remains:

- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `beneficiary_matching_authorized: false`;
- `outreach_authorized: false`;
- `approval_ref: null`;
- `allow_pii: false`.

The task-bounded preflight method/timeout/allowlist do not silently mutate that policy into an approved
production policy.

## Remaining readiness gaps

- safe maximum bytes for future real acquisition;
- production retention/privacy/data-minimization policy;
- explicit permitted processing purpose;
- permitted data categories and minimized fields;
- PII necessity determination;
- source-policy approval;
- registry activation;
- ZIP contents;
- actual CSV row/field layout;
- real artifact hash/revision from an authorized download;
- real acquisition, matching, PII and outreach remain unauthorized.

## SINGLE NEXT ACTION

Create a new isolated candidate from current canonical for a **California SCO source-approval
readiness package only**.

Suggested branch:
`m3-ca-sco-source-approval-package`

The task must:

1. reuse the canonical transport evidence; do not re-run the preflight;
2. propose explicit processing purpose, data categories, minimized fields and PII-necessity evidence;
3. propose privacy and retention controls;
4. propose a safe maximum acquisition size and production transport constraints;
5. define evidence required for an eventual approval reference;
6. keep source policy `PROPOSED`;
7. keep registry disabled and not approved;
8. perform no network request and no ZIP/CSV download;
9. perform no PII processing, matching or outreach;
10. add machine-readable contracts/tests and run CI.

After tests and CI pass, stop at a human source-approval gate. Do not move policy to `APPROVED`, enable
the registry, or retrieve real data without separate explicit owner approval.

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
M3 SCO transport-preflight execution/evidence: CANONICAL + CI VERIFIED
SCO promoted transport-evidence SHA: 60ec305d4f2fd7ec00ca0cfa3f53da9d7c9b595a
SCO canonical post-promotion CI: 34840001821 PASS
Observed endpoint: https://claimit.ca.gov/upd-property-records/00_All_Records.zip
Observed status: HTTP 200
Observed media type: application/zip
Observed content length: 3,203,972,130 bytes
Response body bytes read: 0
One-shot workflow: REMOVED
SCO registry: DISABLED + NOT APPROVED
SCO policy: PROPOSED + NON-AUTHORIZING
Approved real sources: 0
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Vercel repository integration: DECOMMISSIONED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: isolated non-authorizing SCO source-approval readiness package
CONTEXT HEALTH: coherent; repository is source of truth
```
