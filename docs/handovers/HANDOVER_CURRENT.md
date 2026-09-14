# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Current canonical HEAD before this candidate:
  `5b23d63faceb94112a907bff4af1a287141756d0`
- Current candidate branch:
  `m3-ca-sco-source-approval-package`
- Candidate functional commit:
  `4250291d24286be2e0d4cb1a12de0960cc3faa90`
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
- Repository-side Vercel runtime/deployment integration DECOMMISSIONED + CI VERIFIED.
- Reviewer read contract v2.0.0 and provider-neutral.
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
- method used by the bounded preflight: `HEAD`;
- final host: `claimit.ca.gov`;
- HTTP status: `200`;
- redirects: `0`;
- TLS: `https`;
- content type: `application/zip`;
- content length: `3,203,972,130` bytes;
- response-body bytes read: `0`.

The ZIP body has never been downloaded or opened. Do not claim internal files, CSV row layout, columns
or PII contents are known.

Canonical transport post-promotion CI:
`34840001821` — PASS.

Canonical documentation closure CI:
`34840291103` — PASS.

## Current candidate — SCO source-approval readiness package

Branch:
`m3-ca-sco-source-approval-package`

Functional commit:
`4250291d24286be2e0d4cb1a12de0960cc3faa90`

Candidate CI:
`34843714665` — PASS for both `quality` and `streamlit-candidate`.

Pre-closure compare against canonical:
- 1 commit ahead;
- 0 behind;
- exact merge-base `5b23d63faceb94112a907bff4af1a287141756d0`;
- exactly 5 new files;
- no existing policy, registry or runtime files modified.

New files:

1. `schemas/common/source_approval_package.schema.json`
2. `schemas/examples/ca_sco_source_approval_package.examples.json`
3. `sources/proposals/ca_sco_unclaimed_property_bulk.source_approval_package.v1.json`
4. `tests/contract/test_ca_sco_source_approval_package.py`
5. `docs/audits/M3_CA_SCO_SOURCE_APPROVAL_PACKAGE.md`

## Why this is a separate contract

`SourceAccessGovernance` v1 intentionally forces processing purpose, categories, fields and production
transport controls to remain empty while policy status is `PROPOSED`.

Therefore the candidate does not mutate the authorization policy. `SourceApprovalPackage` v1 carries
proposed readiness values while remaining machine-enforced as non-authorizing.

## Candidate package invariants

The schema fixes:

- `package_status = READINESS_PROPOSAL_NOT_AUTHORIZED`;
- `source_approved = false`;
- `source_enabled = false`;
- `real_acquisition_authorized = false`;
- `network_request_performed = false`;
- `body_access_performed = false`.

The package cannot be mutated under v1 to claim approval or real acquisition authorization.

## Proposed processing scope

Narrow purpose:
`SOURCE_STRUCTURE_VERIFICATION_ONLY`

Meaning: validate archive integrity and establish internal CSV schema before any record-level use,
identity resolution, matching, outreach or claim activity.

High-level proposed category:
`PUBLIC_UNCLAIMED_PROPERTY_BULK_ARCHIVE`

Record-level field scope:
`BLOCK_UNTIL_ROW_SCHEMA_VERIFIED`

`proposed_allowed_fields` remains empty. No field names were invented.

PII necessity:
`UNDETERMINED_BLOCKING`

`allow_pii = false` because the archive body and row schema have not been inspected.

## Proposed privacy / retention prerequisites

The package proposes these prerequisites for any later real-data path:

- quarantine required;
- encryption at rest required;
- least-privilege access required;
- access logging required;
- no record-level processing;
- no export;
- no beneficiary matching;
- no outreach;
- delete on validation failure.

Still unresolved and explicitly null:

- production retention policy reference;
- retention duration;
- trusted project privacy policy reference.

Those are intentional blockers.

## Proposed transport bounds

Derived only from canonical transport evidence:

- HTTPS only;
- allowed host: `claimit.ca.gov`;
- redirect policy: same-host only;
- timeout: 10 seconds, proposal semantics = per-request network inactivity;
- expected media type: `application/zip`;
- content length required;
- max bytes: `3,203,972,130`;
- max-byte basis: exact observed content length, no growth tolerance;
- endpoint change → new preflight required;
- media-type change → block/review;
- content-length growth → block/review;
- future real client must stream;
- partial artifact persistence after failure is disallowed.

No network request was made while creating this package.

## Readiness decision

The package is explicitly:

`BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION`

Reason code:

`ROW_SCHEMA_AND_PII_SCOPE_UNVERIFIED`

Still required before source approval:

- verified row layout;
- minimized field whitelist;
- PII necessity determination;
- production retention policy;
- trusted project privacy policy;
- reviewed real-acquisition client;
- explicit human approval reference.

## Canonical authorization state remains unchanged

`policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json` remains:

- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `approval_ref: null`;
- no authorized processing purposes/categories/fields;
- `allow_pii: false`;
- production transport controls unset.

`sources/registry.yaml` remains:

- `enabled: false`;
- `approved_for_use: false`.

## Verification

Candidate CI `34843714665` passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- legacy frontend lint/typecheck/build;
- Streamlit safety/startup smoke.

No network request, real data acquisition, PII processing, beneficiary matching or outreach occurred.

## SINGLE NEXT ACTION

**HUMAN PROMOTION GATE ONLY:** decide whether to promote verified candidate branch
`m3-ca-sco-source-approval-package` into canonical `m2-state-governance-core`.

If the owner explicitly approves promotion:

1. verify canonical HEAD has not diverged from candidate base;
2. compare candidate vs canonical and require clean ancestry;
3. fast-forward canonical without force;
4. verify canonical CI on the promoted SHA;
5. update persistent project state/handover after canonical CI passes;
6. stop again before any source approval or network/data action.

Promotion records a non-authorizing readiness proposal only. It does **not** permit policy `APPROVED`,
registry activation, network access, ZIP/CSV download, record-level processing, PII, matching or
outreach.

Because the package still has row-schema/PII/privacy/retention blockers, even after promotion the
next product action must be a separately authorized bounded prerequisite for data-scope evidence,
not a silent source approval.

## Handover status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 source/legal readiness: COMPLETE
M3 acquisition/raw persistence/privacy: CANONICAL + VERIFIED
M3 SCO source governance: CANONICAL + CI VERIFIED
M3 SCO approval readiness: CANONICAL + CI VERIFIED
M3 SCO transport-preflight execution/evidence: CANONICAL + CI VERIFIED
M3 SCO source-approval readiness package: CANDIDATE + CI VERIFIED
Candidate branch: m3-ca-sco-source-approval-package
Candidate functional SHA: 4250291d24286be2e0d4cb1a12de0960cc3faa90
Candidate CI: 34843714665 PASS
SCO policy: PROPOSED + NON-AUTHORIZING
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
Row schema: UNVERIFIED
Field whitelist: BLOCKED
PII necessity: UNDETERMINED_BLOCKING
Retention policy: REQUIRED / UNSELECTED
Trusted project privacy policy: REQUIRED / UNSELECTED
Network actions in package task: 0
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Vercel repository integration: DECOMMISSIONED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: owner decision on candidate -> canonical promotion
CONTEXT HEALTH: coherent; repository is source of truth
```
