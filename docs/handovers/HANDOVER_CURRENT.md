# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory. Verify current remote branch heads before acting.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Canonical development branch: `m2-state-governance-core`
- Canonical development HEAD: `e97c1f62959f603bdd3df79538d4b70255594c70`
- Second-execution closure branch: `m3-ca-sco-property-type-second-semantic-execution`
- Second-execution closure HEAD: `9d0243987c843172fe46c971ead0bf3947098336`
- Code-shape provenance proposal branch: `m3-ca-sco-property-type-code-shape-provenance-offline-proposal`
- Code-shape provenance proposal SHA: `defed0c211230aad8f8cec6ff80b216223069844`
- Code-shape provenance proposal CI: `35002920469` — SUCCESS
- Code-shape provenance review branch: `m3-ca-sco-property-type-code-shape-provenance-offline-review`
- Provenance review result SHA: `b274e9db0a28dae1c9f6a1a25c657978dd27d7b4`
- Provenance review CI: `35003900554` — SUCCESS
- Provenance review documentation closure HEAD: `dba496d254e94a68f7f74e0b53090cfef972a969`
- Authority provenance acquisition proposal branch: `m3-ca-sco-property-type-authority-provenance-acquisition-proposal`
- Authority proposal package SHA: `963c205b662cf56260ca7af14d71c65a6916c30f`
- Authority proposal CI: `35005451605` — SUCCESS
- Never develop directly on `main`.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness complete.
- M3 acquisition/raw persistence/privacy controls verified.
- Streamlit reviewer canonical and verified.
- Canonical `PROPERTY_TYPE` runner uses execution schema v1.1.0.
- Second bounded real semantic execution was performed exactly once and stopped fail-closed.
- Second execution/privacy approvals are CONSUMED and non-reusable.
- One-shot semantic network workflow is ABSENT.
- Offline code-shape provenance proposal passed human review.
- Repository-only provenance review completed and CI verified.
- Retained provenance does not justify a semantic/runtime change.
- Separate bounded authority archival/provenance acquisition proposal prepared and CI verified.
- Authority retrieval remains NOT AUTHORIZED.
- Repository-side Vercel integration remains decommissioned.
- Supabase remains untouched.

## Second Bounded Real Semantic Execution

Run: `34995672539`  
Execution commit: `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`  
Execution schema: `1.1.0`  
Semantic result: `STOPPED_FAIL_CLOSED`  
Stop reason: `PROPERTY_TYPE_FORMAT_UNEXPECTED`

Safe interpretation under v1.1.0: the projected `PROPERTY_TYPE` decoded successfully, was non-empty, and failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The offending value/bytes were not retained and must not be inferred.

Consumed single-use approvals:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

They cannot authorize any retry, authority acquisition, or later execution.

## Offline Code-Shape Provenance Review

Machine evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json`

Review result:
`NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE`

Classification:

1. `PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1` -> `SUPPORTED_BY_REPOSITORY_EVIDENCE`
2. `GENERAL_CODE_SHAPE_AA99` -> `PROVENANCE_INSUFFICIENT`
3. `SPECIAL_CODE_ZZZZ` -> `PROVENANCE_INSUFFICIENT`
4. `CALIFORNIA_INSURANCE_CODE_SET` -> `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`
5. `CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY` -> `SUPPORTED_BY_REPOSITORY_EVIDENCE`

Aggregate: supported `2`; external-reference assertion not archived `1`; provenance insufficient `2`.

## Bounded Authority Provenance Acquisition Proposal

Human preparation of the proposal was authorized. No authority content was accessed or downloaded during proposal preparation.

Proposal branch:
`m3-ca-sco-property-type-authority-provenance-acquisition-proposal`

Verified proposal package SHA:
`963c205b662cf56260ca7af14d71c65a6916c30f`

Verified CI:
`35005451605` — SUCCESS

Package artifacts:

- schema: `schemas/common/property_type_authority_provenance_acquisition_proposal.schema.json`
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_authority_provenance_acquisition.v1.json`
- contract test: `tests/contract/test_ca_sco_property_type_authority_provenance_acquisition_proposal.py`

Proposal status:
`PROPOSAL_ONLY_NOT_AUTHORIZED`

### Exact authority target

The proposal contains exactly one authority target already referenced by repository evidence:

`https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`

No additional authority discovery is included.

### Future network boundary if separately authorized

- HTTPS only;
- exact host `www.sco.ca.gov`;
- exact URL/path only;
- exactly one `GET`;
- single PDF, all pages;
- redirects forbidden;
- retries `0`;
- query parameters forbidden;
- authentication/cookies forbidden;
- response-body maximum `16777216` bytes, a project safety cap rather than a source fact;
- source-data and `claimit.ca.gov` access forbidden.

### Archive/provenance contract

If later separately authorized, the raw authority PDF must be stored immutably and content-addressed with SHA-256.

Archive template:
`sources/authority/ca/sco/upd_naupa_ii_codes_dormancy_periods/{sha256}.pdf`

Metadata target:
`sources/evidence/ca_sco_property_type_authority_archive.v1.json`

Required metadata includes authority ID, requested/final URL, UTC retrieval time, HTTP status, content type, response byte count, SHA-256, archive path, method, and redirect count. PDF magic must be verified.

Retrieval cannot perform semantic extraction or runtime contract changes. The archive itself does not prove the unresolved claims; a separate post-archive human provenance review is mandatory.

### Intended provenance questions

Only these unresolved items are in scope:

- whether official authority establishes the general `AA99` code grammar;
- whether `ZZZZ` is an official special PROPERTY_TYPE token;
- whether `IN01-IN08` and `IN99` are official California insurance PROPERTY_TYPE codes with the meanings already attributed by the repository.

The proposal does not assume the authority will prove any of them.

## Governance / Safety State

Still fail-closed:

- authority network access authorized by this proposal: `false`
- source policy: `PROPOSED`
- source-level real acquisition authorization: `false`
- registry: disabled/unapproved
- approved real sources: `0`
- semantic compatibility: unresolved
- production classification: inactive
- semantic one-shot workflow: ABSENT
- identity resolution: BLOCKED
- genealogy: BLOCKED
- beneficiary matching: BLOCKED
- outreach: BLOCKED
- claim submission: BLOCKED

Not authorized by the proposal:

- authority retrieval/download before a separate authorization;
- additional authority discovery/crawling;
- SCO dataset or `claimit.ca.gov` access;
- reuse of consumed execution/privacy approvals;
- source-value reconstruction;
- trimming, uppercasing or normalization;
- parser or regex modification/relaxation;
- logging/privacy expansion;
- source approval or registry activation;
- production classification;
- third real semantic execution;
- identity, genealogy, matching, outreach, or claim submission.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_AUTHORITY_PROVENANCE_ACQUISITION_PROPOSAL_REVIEW`

Review the proposal, schema and contract test package at the verified proposal package SHA.

The review must decide only whether the bounded proposal is acceptable. **Do not retrieve or download the authority document during this review.**

If the proposal review passes and authority archival is desired, prepare a separate explicit one-shot authority archival execution/authorization artifact before any network request. No authority execution approval token has been created by this proposal.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e
canonical dev: e97c1f62959f603bdd3df79538d4b70255594c70
second execution run: 34995672539
second schema: 1.1.0
second result: STOPPED_FAIL_CLOSED
second stop: PROPERTY_TYPE_FORMAT_UNEXPECTED
second execution/privacy approvals: CONSUMED + NON-REUSABLE
semantic network workflow: ABSENT
offline provenance review: VERIFIED
offline provenance decision: NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE
provenance classifications: SUPPORTED=2 / EXTERNAL_REF_NOT_ARCHIVED=1 / INSUFFICIENT=2
authority proposal branch: m3-ca-sco-property-type-authority-provenance-acquisition-proposal
authority proposal package SHA: 963c205b662cf56260ca7af14d71c65a6916c30f
authority proposal CI: 35005451605 SUCCESS
authority proposal status: PROPOSAL_ONLY_NOT_AUTHORIZED
authority targets: 1 EXACT PRE-EXISTING SCO PDF REFERENCE
authority retrieval authorized: NO
semantic compatibility: UNRESOLVED
source policy: PROPOSED
registry: DISABLED + NOT APPROVED
approved real sources: 0
production classification: INACTIVE
identity/genealogy/matching/outreach/claim: BLOCKED
NEXT: HUMAN_PROPERTY_TYPE_AUTHORITY_PROVENANCE_ACQUISITION_PROPOSAL_REVIEW
NO AUTHORITY RETRIEVAL DURING REVIEW
NO THIRD SCO EXECUTION WITHOUT NEW PROPOSAL + FRESH EXECUTION/PRIVACY APPROVALS
```
