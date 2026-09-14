# M3 California SCO Source-Approval Readiness Package

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANONICAL + CI VERIFIED — NON-AUTHORIZING — SOURCE APPROVAL BLOCKED**

## Objective

Prepare a machine-readable California SCO source-approval readiness package from canonical repository
evidence without changing the authorization state.

The package performs no network request, downloads no ZIP/CSV body, processes no real PII, performs
no beneficiary matching, and performs no outreach.

## REUSE FIRST result

The repository already contained the required authority boundaries:

- `SourceAccessGovernance` v1;
- canonical SCO approval-readiness evidence;
- canonical SCO transport-preflight execution/evidence;
- deterministic `RawDataGovernanceGate`;
- disabled/not-approved SCO source registry entry;
- canonical `PROPOSED` SCO source-access policy.

`SourceAccessGovernance` intentionally forces purpose, categories, fields and production transport
controls to remain empty while status is `PROPOSED`. A separate `SourceApprovalPackage` v1 contract
therefore carries proposed readiness values without blurring proposal/evidence with authorization.

## Canonical evidence reused

Transport evidence:
`sources/evidence/ca_sco_unclaimed_property_bulk.transport_preflight.execution.v1.json`

Observed facts reused without another network request:

- endpoint: `https://claimit.ca.gov/upd-property-records/00_All_Records.zip`;
- host: `claimit.ca.gov`;
- HTTPS;
- HTTP `200`;
- media type `application/zip`;
- content length `3,203,972,130` bytes;
- preflight timeout `10` seconds;
- response-body bytes read `0`.

The package also references the existing approval-readiness evidence, source-access policy and source
registry.

## Proposed processing scope

Narrow purpose:
`SOURCE_STRUCTURE_VERIFICATION_ONLY`

Meaning: validate archive integrity and establish the internal CSV schema before any record-level use,
identity resolution, beneficiary matching, outreach or claim activity.

High-level proposed data category:
`PUBLIC_UNCLAIMED_PROPERTY_BULK_ARCHIVE`

No record-level field names are proposed. The archive body has not been inspected and the CSV row
schema is unknown, so inventing a field whitelist would violate the repository no-fabrication rule.

Field-scope mode:
`BLOCK_UNTIL_ROW_SCHEMA_VERIFIED`

`proposed_allowed_fields` remains empty.

## PII necessity decision

PII necessity remains a blocking unknown:

- status: `UNDETERMINED_BLOCKING`;
- `allow_pii = false`;
- actual record contents and row schema are unverified.

The package explicitly refuses to infer PII presence or necessity from source naming or general
knowledge.

## Proposed privacy and retention controls

Prerequisites proposed for any later real-data gate:

- quarantine required;
- encryption at rest required;
- least-privilege access required;
- access logging required;
- no record-level processing before a later gate;
- no export;
- no beneficiary matching;
- no outreach;
- delete on validation failure.

A production retention policy is still required before approval. No retention duration is invented:

- `retention_policy_ref = null`;
- `retention_duration_days = null`.

A trusted project privacy policy is also still required:

- `trusted_project_privacy_policy_ref = null`.

These nulls are intentional blockers.

## Proposed production transport bounds

The package derives transport values only from canonical observation:

- HTTPS only;
- allowed host: `claimit.ca.gov`;
- redirect policy: same host only;
- timeout: `10` seconds per-request network inactivity;
- expected media type: `application/zip`;
- content length required;
- maximum bytes: `3,203,972,130`.

The maximum byte value equals the exact observed content length. No growth headroom is invented.
Any increase, endpoint change or media-type change requires a new preflight/review before real
acquisition.

A future real client is proposed to stream the artifact and persist no partial artifact after failure,
but the real acquisition client is not implemented or authorized by this package.

## Approval blockers

The package is intentionally marked:

`BLOCKED_PENDING_DATA_SCOPE_PRIVACY_RETENTION`

Reason code:
`ROW_SCHEMA_AND_PII_SCOPE_UNVERIFIED`

Before source approval, all of the following remain required:

1. verified row layout;
2. selected minimized field whitelist;
3. PII necessity determination;
4. selected production retention policy;
5. selected trusted project privacy policy;
6. reviewed real-acquisition client implementation;
7. explicit human approval reference.

## Machine-readable artifacts

- `schemas/common/source_approval_package.schema.json`;
- `schemas/examples/ca_sco_source_approval_package.examples.json`;
- `sources/proposals/ca_sco_unclaimed_property_bulk.source_approval_package.v1.json`;
- `tests/contract/test_ca_sco_source_approval_package.py`.

The schema fixes the package in a non-authorizing state and rejects attempts to claim source approval,
real acquisition authorization, network execution, body access or unverified record-level fields.

## Canonical state preserved

This package does not change:

- `policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json`;
- `sources/registry.yaml`.

Those remain:

- source policy `PROPOSED`;
- `real_acquisition_authorized = false`;
- `approval_ref = null`;
- production transport policy unset;
- registry `enabled = false`;
- registry `approved_for_use = false`.

## Candidate verification

Candidate branch:
`m3-ca-sco-source-approval-package`

Functional commit:
`4250291d24286be2e0d4cb1a12de0960cc3faa90`

Candidate closure commit:
`41dfc61cd96d7573cdd67c37631567ef5343fcdd`

Candidate CI:
`34843714665` — SUCCESS.

Candidate closure CI:
`34843990986` — SUCCESS.

Verified gates included Ruff, mypy, contract tests, smoke tests, full pytest, legacy frontend
lint/typecheck/build, and Streamlit safety/startup smoke.

## Promotion evidence

The owner explicitly approved promotion of:

`m3-ca-sco-source-approval-package` → `m2-state-governance-core`.

Immediately before promotion:

- candidate was 2 commits ahead;
- candidate was 0 commits behind;
- merge-base was exactly `5b23d63faceb94112a907bff4af1a287141756d0`.

Canonical was advanced by non-force fast-forward to:
`41dfc61cd96d7573cdd67c37631567ef5343fcdd`.

Canonical post-promotion CI:
`34853561664` — SUCCESS.

Both `quality` and `streamlit-candidate` passed. No SCO request or body access occurred during
promotion.

## Acceptance criteria

Verified:

1. JSON Schema draft 2020-12 validation succeeds;
2. valid proposal example and real package validate;
3. authorization claims are schema-invalid;
4. invented/unverified record-level fields are schema-invalid;
5. proposed transport values cross-check canonical transport evidence;
6. current source policy and registry remain fail-closed;
7. data-scope, PII, privacy and retention blockers remain explicit;
8. candidate and canonical CI pass;
9. no network request or real data acquisition occurs.

## Next bounded prerequisite

The next product step is a separate **data-scope inspection proposal only**. It must define the
minimum body-access evidence required to verify archive member names, CSV headers/row layout and
PII-presence indicators, together with strict byte/range limits, streaming/no-partial-persistence,
quarantine, stop conditions and machine-readable outputs.

That proposal itself must perform no network request or archive access. Any later structure inspection
requires another explicit owner execution gate.

## Stop condition

The promoted package must not be interpreted as evidence that the source is ready for `APPROVED`
status. Source approval, registry activation, archive/body access, real acquisition, PII processing,
matching and outreach remain blocked until the documented prerequisites and later human gates are
satisfied.
