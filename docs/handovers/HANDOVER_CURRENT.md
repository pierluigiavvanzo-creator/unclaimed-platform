# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before current candidate: `50887231d39eff793b1968b4a062292533205602`
- Current candidate branch: `m3-ca-sco-transport-preflight-execution`
- Current evidence commit before this documentation closure:
  `2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`
- Stable `main` HEAD: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Never develop directly on `main`; promote verified checkpoints only after the applicable owner gate.

## Verified baseline

Canonical before the current candidate:

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
- Reviewer read contract v2.0.0 and provider-neutral.
- SCO registry `enabled: false` and `approved_for_use: false`.
- SCO source-access policy `PROPOSED`; real acquisition authorization `false`.
- Approved real source count `0`.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

Current candidate adds a separately owner-authorized, metadata-only California SCO transport
observation. It is CI verified but is **not yet canonical**.

## Vercel closure

Repository-side Vercel runtime/deploy support remains decommissioned under D-007. The owner reported
the Vercel account deleted before authorizing the transport task.

Evidence commit `2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e` showed no external commit-status
contexts, so no Vercel status reappeared during the candidate evidence push.

Do not reintroduce Vercel paths, commands or runtime references without a new explicit owner decision.

## California SCO transport execution authorization

The prior canonical handover required a separate explicit owner gate before any transport request.
That gate was satisfied when the owner confirmed the Vercel account had been deleted and instructed
`procedi pure`.

Internal execution approval reference:

`OWNER_CHAT_APPROVAL_2026-09-14T13:26+02:00`

The approval covered exactly one bounded metadata-only preflight. It did **not** approve source use,
registry activation, dataset acquisition, ZIP/CSV download, response-body access, PII processing,
beneficiary matching, outreach, or downstream legal/commercial action.

## Candidate branch and commits

Candidate branch:
`m3-ca-sco-transport-preflight-execution`

Created from canonical:
`50887231d39eff793b1968b4a062292533205602`

Initial authorization commit:
`3c3dfe3fd15a65b96b9e4e55e6c518932bbba80d`

The first one-shot workflow attempt (`34838663274`) failed before creating any job. Therefore **no SCO
download-endpoint request occurred** on that attempt. The regular CI for that commit (`34838664055`)
also stopped at Ruff due formatting/style defects.

Corrected execution commit:
`7d89ec664992a30b5270be8da4c2616254747e59`

One-shot execution workflow:
`34838890387`

- targeted validation job: PASS;
- preflight job: PASS;
- network execution occurred only after validation passed.

Evidence commit:
`2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e`

Evidence candidate CI:
`34839100497` — PASS for both `quality` and `streamlit-candidate`.

The temporary workflow `.github/workflows/ca-sco-transport-preflight-once.yml` was deleted in the
evidence commit. Contract tests require it to remain absent, so later pushes cannot repeat the
preflight automatically.

## Execution controls fixed before the request

- official source page: `https://www.sco.ca.gov/upd_download_property_records.html`;
- target anchor label: `All properties`;
- endpoint discovery: parse exactly one matching anchor from the official SCO HTML page;
- allowlisted download host: `claimit.ca.gov` only;
- method against the discovered download endpoint: `HEAD` only;
- HTTPS only;
- timeout: 10 seconds per request;
- maximum redirects: 3;
- redirects must remain HTTPS on `claimit.ca.gov` or stop fail-closed;
- response-body bytes allowed/read: `0`;
- no response-body persistence/parsing;
- no dataset artifact persistence;
- selected safe headers only;
- no real PII;
- no beneficiary matching;
- no outreach.

## Observed transport evidence

Observation timestamp:
`2026-09-14T11:34:58.210154Z`

The runner extracted the current `All properties` href from the official SCO source page and issued
one `HEAD` request.

Observed endpoint:

`https://claimit.ca.gov/upd-property-records/00_All_Records.zip`

Observed metadata:

- final host: `claimit.ca.gov`;
- HTTP status: `200`;
- redirect count: `0`;
- TLS scheme: `https`;
- content type: `application/zip`;
- content length: `3,203,972,130` bytes;
- `Accept-Ranges: bytes`;
- ETag: `"0ce16eb75bbbe7018639c7a71e802008"`;
- Last-Modified: `Wed, 09 Sep 2026 16:32:37 GMT`;
- response-body bytes read: `0`.

The public SCO page describes public records as downloadable CSV data, while the current
`All properties` transport endpoint is a ZIP resource advertising `application/zip`. The ZIP body was
not downloaded or opened, so do not claim its contents, internal CSV files, row layout, columns or
schema are known.

Machine-readable candidate evidence:

`sources/evidence/ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json`

Execution schema:

`schemas/common/source_transport_preflight_execution.schema.json`

Execution runner:

`scripts/ca_sco_transport_preflight.py`

Contract tests:

- `tests/contract/test_ca_sco_transport_preflight_execution.py`
- `tests/contract/test_ca_sco_transport_preflight_observation.py`

Audit:

`docs/audits/M3_CA_SCO_TRANSPORT_PREFLIGHT_EXECUTION.md`

## Safety state after the observation

The recorded evidence requires:

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

The observed allowlist/method/timeout were task-bounded execution controls. They do not silently mutate
the canonical source-access policy into an approved policy.

## What the preflight resolves

Resolved as candidate transport evidence:

- exact current `All properties` endpoint;
- direct HTTPS host;
- one bounded request method (`HEAD`);
- one bounded timeout (10 seconds);
- one bounded redirect limit (3);
- preflight host allowlist (`claimit.ca.gov`);
- explicit execution approval reference;
- observed status/final host/content type/content length;
- selected transport metadata.

Still unresolved / not authorized:

- safe maximum bytes for any future real acquisition;
- production retention/privacy/data-minimization policy;
- authorized processing purpose;
- authorized data categories and minimized fields;
- PII necessity;
- source policy approval;
- registry activation;
- ZIP contents;
- actual CSV row/field layout;
- real artifact hash/revision from an authorized download;
- real California acquisition;
- beneficiary matching;
- real PII;
- outreach and claim activity.

## SINGLE NEXT ACTION

**HUMAN PROMOTION GATE ONLY:** decide whether to promote verified candidate branch
`m3-ca-sco-transport-preflight-execution` into canonical `m2-state-governance-core`.

If the owner explicitly approves promotion:

1. compare candidate to canonical and require clean ancestry / no unexpected files;
2. fast-forward canonical without force;
3. verify canonical GitHub CI on the promoted SHA;
4. update persistent project state/handover after canonical CI passes;
5. stop again before source approval, registry activation or real retrieval.

Promotion records the already-observed metadata only. It does **not** authorize any additional network
request or data download.

If promotion is not explicitly approved, do not move canonical.

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
M3 SCO transport-preflight execution/evidence: CANDIDATE + CI VERIFIED
SCO execution branch: m3-ca-sco-transport-preflight-execution
SCO execution commit: 7d89ec664992a30b5270be8da4c2616254747e59
SCO evidence commit: 2f762aa2673a52bfa211fb216a4cf06ccc3fbb1e
SCO one-shot run: 34838890387 PASS
SCO evidence candidate CI: 34839100497 PASS
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
Vercel external status on evidence commit: NONE OBSERVED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: owner decision on candidate -> canonical promotion
CONTEXT HEALTH: coherent; repository is source of truth
```
