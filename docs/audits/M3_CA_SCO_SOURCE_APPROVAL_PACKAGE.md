# M3 California SCO Source-Approval Readiness Package

Date: 2026-09-14

Class: **A — Product Critical**

Status: **CANDIDATE READINESS PROPOSAL — NON-AUTHORIZING — SOURCE APPROVAL BLOCKED**

## Objective

Prepare a machine-readable California SCO source-approval readiness package from canonical repository
evidence without changing the authorization state.

This candidate performs no network request, downloads no ZIP/CSV body, processes no real PII, performs
no beneficiary matching, and performs no outreach.

## REUSE FIRST result

The repository already contains the relevant authority boundaries:

- `SourceAccessGovernance` v1;
- canonical SCO approval-readiness evidence;
- canonical SCO transport-preflight execution/evidence;
- the deterministic `RawDataGovernanceGate`;
- the disabled/not-approved SCO source registry entry;
- the canonical `PROPOSED` SCO source-access policy.

`SourceAccessGovernance` deliberately forces purpose, categories, fields and production transport
controls to remain empty while status is `PROPOSED`. Mutating that policy to carry proposed values
would blur evidence/proposal from authorization and violate fail-closed separation.

Therefore this task adds a separate `SourceApprovalPackage` v1 proposal contract. It does not alter
the canonical source-access policy or registry.

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

The candidate proposes only the narrow purpose:

`SOURCE_STRUCTURE_VERIFICATION_ONLY`

Meaning: validate archive integrity and establish the internal CSV schema before any record-level use,
identity resolution, beneficiary matching, outreach or claim activity.

The proposed high-level data category is:

`PUBLIC_UNCLAIMED_PROPERTY_BULK_ARCHIVE`

No record-level field names are proposed. The archive body has not been inspected and the CSV row
schema is unknown, so inventing a field whitelist would violate the repository no-fabrication rule.

The field-scope mode is therefore:

`BLOCK_UNTIL_ROW_SCHEMA_VERIFIED`

and `proposed_allowed_fields` remains empty.

## PII necessity decision

PII necessity remains a blocking unknown:

- status: `UNDETERMINED_BLOCKING`;
- `allow_pii = false`;
- actual record contents and row schema are unverified.

The package explicitly refuses to infer PII presence or necessity from source naming or general
knowledge.

## Proposed privacy and retention controls

The package proposes these prerequisites for any later real-data gate:

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

These nulls are intentional blockers, not omissions.

## Proposed production transport bounds

The package derives transport values only from canonical observation:

- HTTPS only;
- allowed host: `claimit.ca.gov`;
- redirect policy: same host only;
- timeout: `10` seconds, explicitly described by the proposal as per-request network inactivity;
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

with reason code:

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

This candidate does not change:

- `policies/states/CA/ca_sco_unclaimed_property_bulk.source_access.v1.json`;
- `sources/registry.yaml`.

Those remain:

- source policy `PROPOSED`;
- `real_acquisition_authorized = false`;
- `approval_ref = null`;
- production transport policy unset;
- registry `enabled = false`;
- registry `approved_for_use = false`.

## Acceptance criteria

Candidate acceptance requires:

1. JSON Schema draft 2020-12 validation succeeds;
2. valid proposal example and real package validate;
3. authorization claims are schema-invalid;
4. invented/unverified record-level fields are schema-invalid;
5. proposed transport values cross-check canonical transport evidence;
6. current source policy and registry remain fail-closed;
7. data-scope, PII, privacy and retention blockers remain explicit;
8. repository CI passes;
9. no network request or real data acquisition occurs.

## Rollback

The candidate is additive. Rollback is deletion of the four machine-readable/test artifacts and this
audit before promotion. No runtime migration, database change, source policy change or registry change
is required.

## Stop condition

After candidate tests and CI pass, stop at a human review gate.

Because the package still has row-schema, PII, retention and trusted-project-privacy blockers, this
candidate must not be interpreted as evidence that the source is ready for `APPROVED` status. A later
human decision must choose the next bounded prerequisite; source approval, registry activation and
real retrieval remain prohibited until all required controls are actually resolved.
