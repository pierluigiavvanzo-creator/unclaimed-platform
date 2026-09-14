# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before current candidate:
  `c832b447cbe37482fdc4273eb1b163ce9299edf3`
- Current candidate branch:
  `m3-ca-sco-data-scope-inspection-proposal`
- Candidate functional commit:
  `2df97f9dbab16ba0e30ec07a590657b381eb8c8b`
- Stable `main` HEAD:
  `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Never develop directly on `main`; promote verified checkpoints only after the applicable owner gate.

## Verified canonical baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition contracts/adapters CANONICAL + CI VERIFIED.
- M3 immutable raw storage/provenance + privacy/data-minimization CANONICAL + CI VERIFIED.
- Streamlit M3 reviewer CANONICAL + CI VERIFIED.
- California SCO source governance CANONICAL + CI VERIFIED.
- California SCO approval-readiness evidence CANONICAL + CI VERIFIED.
- California SCO transport-preflight proposal CANONICAL + CI VERIFIED.
- California SCO bounded transport-preflight execution/evidence CANONICAL + CI VERIFIED.
- California SCO source-approval readiness package CANONICAL + CI VERIFIED.
- Repository-side Vercel runtime/deployment integration DECOMMISSIONED + CI VERIFIED.
- SCO registry `enabled: false` and `approved_for_use: false`.
- SCO source-access policy `PROPOSED` and non-authorizing.
- Approved real source count `0`.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

## Canonical transport evidence

Canonical observation:

- endpoint: `https://claimit.ca.gov/upd-property-records/00_All_Records.zip`;
- method used by bounded preflight: `HEAD`;
- final host: `claimit.ca.gov`;
- HTTP status: `200`;
- redirects: `0`;
- TLS: `https`;
- content type: `application/zip`;
- content length: `3,203,972,130` bytes;
- `Accept-Ranges: bytes` observed;
- response-body bytes read: `0`.

The ZIP body has never been downloaded or opened. Do not claim internal files, CSV row layout,
columns or PII contents are known.

## Canonical source-approval package remains blocking

Canonical package baseline:
`41dfc61cd96d7573cdd67c37631567ef5343fcdd`

Canonical package CI:
`34853561664` — PASS.

Package decision remains:
`BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION`.

PII necessity remains:
`UNDETERMINED_BLOCKING`.

`proposed_allowed_fields` remains empty. Production retention policy and trusted project privacy
policy remain unselected.

## Current candidate — data-scope inspection proposal

Branch:
`m3-ca-sco-data-scope-inspection-proposal`

Functional commit:
`2df97f9dbab16ba0e30ec07a590657b381eb8c8b`

Candidate CI:
`34855459255` — PASS for both `quality` and `streamlit-candidate`.

Pre-closure compare against canonical:

- 1 commit ahead;
- 0 behind;
- exact merge-base `c832b447cbe37482fdc4273eb1b163ce9299edf3`;
- exactly five new files;
- no policy, registry, runtime adapter, script or network workflow change.

New files:

1. `schemas/common/source_data_scope_inspection_proposal.schema.json`
2. `schemas/examples/ca_sco_data_scope_inspection_proposal.examples.json`
3. `sources/proposals/ca_sco_unclaimed_property_bulk.data_scope_inspection.v1.json`
4. `tests/contract/test_ca_sco_data_scope_inspection_proposal.py`
5. `docs/audits/M3_CA_SCO_DATA_SCOPE_INSPECTION_PROPOSAL.md`

## Proposal invariants

The schema fixes:

- `proposal_status = PROPOSAL_ONLY_NOT_AUTHORIZED`;
- `source_approved = false`;
- `source_enabled = false`;
- `real_acquisition_authorized = false`;
- `network_execution_authorized = false`;
- `network_request_performed = false`;
- `body_access_performed = false`;
- `body_bytes_read = 0`;
- `execution_approval_ref = null`;
- `execution_authorized = false`;
- `next_gate = HUMAN_DATA_SCOPE_INSPECTION_EXECUTION`.

The current task executed no SCO request and accessed no source body.

## Inspection scope proposed for a later separate execution gate

Purpose:
`SOURCE_STRUCTURE_VERIFICATION_ONLY`

Allowed derived structure evidence:

- archive member names;
- member metadata limited to name, size, compression, encryption indicator and offset;
- one logical CSV record per candidate member only as a header candidate;
- delimiter, encoding, column count and header-confidence metadata;
- potential PII indicators derived from header labels only.

Not allowed:

- CSV data rows (`0` allowed);
- record values;
- identity resolution;
- beneficiary matching;
- outreach;
- downstream record use;
- full-body download.

If a data row would be required to proceed, execution must stop.

## Proposed range/request safety caps

These are project safety caps, not observed source facts:

- archive tail suffix: `131,072` bytes;
- central directory max: `4,194,304` bytes;
- maximum archive members: `10,000`;
- maximum CSV candidates: `10`;
- member response prefix max: `1,048,576` bytes each;
- decompressed prefix max: `65,536` bytes each;
- maximum logical CSV records parsed: `1` per member;
- maximum data rows parsed: `0`;
- maximum range requests: `12`;
- maximum total source response-body bytes: `14,811,136`.

Budget identity:
`131,072 + 4,194,304 + (10 × 1,048,576) = 14,811,136`.

## Proposed transport controls

A future authorized execution must require:

- HTTPS only;
- host `claimit.ca.gov` only;
- same-host redirects only;
- HTTP range GET only;
- no full-body GET;
- 10-second per-request network-inactivity timeout;
- media type `application/zip`;
- exact current content length `3,203,972,130` before inspection;
- `Accept-Ranges: bytes`;
- unexpected non-partial/full-body response => STOP;
- endpoint/media type/content-length drift => STOP/REVIEW.

## Proposed privacy controls

A later authorized execution must:

- use quarantine;
- process source body bytes in memory only;
- create no temporary source files;
- persist no raw ZIP/member/header bytes;
- keep body bytes and record values out of logs;
- enforce least privilege and access logging;
- encrypt any persisted derived structure evidence at rest;
- delete transient buffers after inspection;
- permit no export, matching or outreach.

Header labels may be persisted only if a deterministic structure-only check can classify the first
logical record as header-like without reading a following data row. Otherwise stop without persisting
candidate values.

## Stop conditions

The proposal fails closed on:

- transport metadata drift;
- byte ranges unsupported;
- unexpected full-body/non-partial behavior;
- ZIP tail structure not found inside cap;
- central directory too large;
- archive member limit exceeded;
- unsafe member path;
- encrypted member;
- unsupported compression;
- no `.csv` member;
- too many CSV members;
- member prefix cap exhausted;
- header incomplete inside cap;
- header ambiguity;
- any need to access a data row;
- byte budget exhausted;
- request budget exhausted;
- unexpected response-body behavior.

## Canonical authorization state unchanged

`policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json` remains:

- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `approval_ref: null`;
- `allow_pii: false`;
- production transport authorization unset.

`sources/registry.yaml` remains:

- `enabled: false`;
- `approved_for_use: false`.

## Verification

Candidate CI `34855459255` passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- legacy frontend lint/typecheck/build;
- Streamlit safety/startup smoke.

No network request, archive access, real-data acquisition, PII processing, identity resolution,
beneficiary matching or outreach occurred.

## SINGLE NEXT ACTION

**HUMAN PROMOTION GATE ONLY:** decide whether to promote verified candidate branch
`m3-ca-sco-data-scope-inspection-proposal` into canonical `m2-state-governance-core`.

If the owner explicitly approves promotion:

1. verify canonical HEAD has not diverged from candidate base;
2. compare candidate vs canonical and require clean ancestry;
3. fast-forward canonical without force;
4. verify canonical CI on the promoted SHA;
5. update persistent state/handover after canonical CI passes;
6. stop again before any network/body action.

Promotion records a non-authorizing proposal only. It does **not** permit a range GET, ZIP/CSV body
access, archive/header inspection, source approval, registry activation, PII processing, matching or
outreach.

After promotion, the next gate is a separate explicit owner decision on bounded data-scope inspection
execution. That later gate must assign an execution approval reference before any body byte can be
read.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
M3 SCO transport-preflight evidence: CANONICAL + CI VERIFIED
M3 SCO source-approval readiness package: CANONICAL + CI VERIFIED
M3 SCO data-scope inspection proposal: CANDIDATE + CI VERIFIED
Candidate branch: m3-ca-sco-data-scope-inspection-proposal
Candidate functional SHA: 2df97f9dbab16ba0e30ec07a590657b381eb8c8b
Candidate CI: 34855459255 PASS
SCO policy: PROPOSED + NON-AUTHORIZING
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
Data-scope execution: NOT AUTHORIZED
Execution approval ref: null
Source body bytes read in proposal task: 0
CSV data rows allowed: 0
PII necessity: UNDETERMINED_BLOCKING
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Vercel repository integration: DECOMMISSIONED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: owner decision on proposal candidate -> canonical promotion
CONTEXT HEALTH: coherent; repository is source of truth
```
