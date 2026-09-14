# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-14

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository and branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Promoted SCO source-approval package baseline:
  `41dfc61cd96d7573cdd67c37631567ef5343fcdd`
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
- Reviewer read contract v2.0.0 and provider-neutral.
- SCO registry `enabled: false` and `approved_for_use: false`.
- SCO source-access policy `PROPOSED` and non-authorizing.
- Approved real source count `0`.
- Real acquisition BLOCKED.
- Beneficiary matching BLOCKED.
- Real PII BLOCKED.
- Supabase untouched.
- `main` unchanged.

## Promotion just completed

Owner explicitly approved:

`m3-ca-sco-source-approval-package` → `m2-state-governance-core`

Pre-promotion compare:

- candidate 2 commits ahead;
- 0 behind;
- merge-base exactly `5b23d63faceb94112a907bff4af1a287141756d0`;
- clean fast-forward available.

Canonical was advanced without force to:
`41dfc61cd96d7573cdd67c37631567ef5343fcdd`.

Canonical post-promotion CI:
`34853561664` — PASS for both `quality` and `streamlit-candidate`.

Verified in that run:

- Ruff PASS;
- mypy PASS;
- contract tests PASS;
- smoke tests PASS;
- full pytest PASS;
- legacy frontend lint/typecheck/build PASS;
- Streamlit safety/startup smoke PASS.

No SCO network request occurred during promotion.

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

## Canonical source-approval readiness package

Canonical artifacts:

1. `schemas/common/source_approval_package.schema.json`
2. `schemas/examples/ca_sco_source_approval_package.examples.json`
3. `sources/proposals/ca_sco_unclaimed_property_bulk.source_approval_package.v1.json`
4. `tests/contract/test_ca_sco_source_approval_package.py`
5. `docs/audits/M3_CA_SCO_SOURCE_APPROVAL_PACKAGE.md`

The separate contract exists because `SourceAccessGovernance` v1 intentionally forces proposed
purpose/categories/fields/transport to stay empty while policy status is `PROPOSED`. The readiness
package can therefore carry proposed values without silently authorizing them.

## Canonical package invariants

The schema fixes:

- `package_status = READINESS_PROPOSAL_NOT_AUTHORIZED`;
- `source_approved = false`;
- `source_enabled = false`;
- `real_acquisition_authorized = false`;
- `network_request_performed = false`;
- `body_access_performed = false`.

Readiness decision:
`BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION`.

Reason code:
`ROW_SCHEMA_AND_PII_SCOPE_UNVERIFIED`.

## Proposed processing scope

Narrow purpose:
`SOURCE_STRUCTURE_VERIFICATION_ONLY`

High-level proposed category:
`PUBLIC_UNCLAIMED_PROPERTY_BULK_ARCHIVE`

Record-level field scope:
`BLOCK_UNTIL_ROW_SCHEMA_VERIFIED`

`proposed_allowed_fields` remains empty. No field names were invented.

PII necessity:
`UNDETERMINED_BLOCKING`

`allow_pii = false` because the archive body and row schema have not been inspected.

## Proposed privacy / retention prerequisites

The canonical package proposes these prerequisites for any later real-data path:

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

Those remain approval blockers.

## Proposed transport bounds

Derived only from canonical transport evidence:

- HTTPS only;
- allowed host: `claimit.ca.gov`;
- redirect policy: same-host only;
- timeout: 10 seconds per-request network inactivity;
- expected media type: `application/zip`;
- content length required;
- max bytes: `3,203,972,130`;
- exact observed content-length basis; no invented growth tolerance;
- endpoint change → new preflight/review;
- media-type change → block/review;
- content-length growth → block/review;
- future real client must stream;
- no partial artifact persistence after failure.

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

## Remaining blockers before source approval

- verified archive contents and CSV row layout;
- minimized record-level field whitelist;
- PII presence/necessity determination;
- production retention policy;
- trusted project privacy policy;
- reviewed real-acquisition client;
- explicit human source-approval reference.

## SINGLE NEXT ACTION

Create a new isolated candidate for a **California SCO data-scope inspection proposal only**.

The proposal must:

1. perform no network request and no archive/body access;
2. define the minimum evidence required to verify archive member names and CSV header/row layout;
3. define byte/range/read limits and stop conditions before execution;
4. require streaming and prohibit partial artifact persistence;
5. require quarantine, encryption, least privilege and access logging;
6. define machine-readable outputs for structure evidence and PII-presence indicators only;
7. prohibit identity resolution, beneficiary matching, outreach and downstream record use;
8. require a separate explicit owner execution approval reference before any body access;
9. add schema/examples/tests/audit and run CI;
10. stop at a human execution gate.

Do not approve the source, enable the registry or retrieve any ZIP/CSV data as part of that proposal
task.

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
M3 SCO source-approval readiness package: CANONICAL + CI VERIFIED
Promoted package baseline: 41dfc61cd96d7573cdd67c37631567ef5343fcdd
Canonical package CI: 34853561664 PASS
SCO policy: PROPOSED + NON-AUTHORIZING
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
Row schema: UNVERIFIED
Field whitelist: BLOCKED
PII necessity: UNDETERMINED_BLOCKING
Retention policy: REQUIRED / UNSELECTED
Trusted project privacy policy: REQUIRED / UNSELECTED
Real acquisition: BLOCKED
Beneficiary matching: BLOCKED
Real PII: BLOCKED
Vercel repository integration: DECOMMISSIONED
Supabase: UNTOUCHED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: isolated non-authorizing CA SCO data-scope inspection proposal only
CONTEXT HEALTH: coherent; repository is source of truth
```
