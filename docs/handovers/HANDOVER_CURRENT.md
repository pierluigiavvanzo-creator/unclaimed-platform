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
- Provenance proposal SHA: `defed0c211230aad8f8cec6ff80b216223069844`
- Provenance proposal CI: `35002920469` — SUCCESS
- Code-shape provenance review branch: `m3-ca-sco-property-type-code-shape-provenance-offline-review`
- Provenance review result SHA: `b274e9db0a28dae1c9f6a1a25c657978dd27d7b4`
- Provenance review CI: `35003900554` — SUCCESS
- Never develop directly on `main`.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness complete.
- M3 acquisition/raw persistence/privacy controls verified.
- Streamlit reviewer canonical and verified.
- SCO `$500+` bounded structure inspection canonicalized.
- Canonical `PROPERTY_TYPE` runner uses execution schema v1.1.0.
- Historical v1.0 evidence remains frozen.
- v1.1 distinguishes UTF-8 encoding failure from decoded shape failure.
- Second bounded real execution was performed exactly once and stopped fail-closed.
- Second execution/privacy approvals are CONSUMED and non-reusable.
- One-shot network workflow was removed and remains ABSENT.
- Offline code-shape provenance proposal passed human review.
- Repository-only provenance classification has been completed and CI verified.
- No semantic/runtime change is justified by retained provenance.
- Repository-side Vercel integration remains decommissioned.
- Supabase remains untouched.

## Second Bounded Real Semantic Execution

Run: `34995672539`  
Execution commit: `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`  
Execution schema: `1.1.0`  
Semantic result: `STOPPED_FAIL_CLOSED`  
Stop reason: `PROPERTY_TYPE_FORMAT_UNEXPECTED`

Exact persisted counters:
- HEAD `1`
- Range GET `1`
- HTTP total `2`
- source response-body bytes `131072`
- accepted/examined rows `0`
- no retry
- no cap widening

Safe interpretation under v1.1.0:
- projected `PROPERTY_TYPE` decoded successfully as UTF-8;
- value was non-empty;
- row followed the path that failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

This does not reveal the offending value or explain why its shape differs. Do not infer it.

Consumed single-use approvals:
- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

They cannot authorize any retry or later execution.

Persisted execution evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json`

Execution audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION.md`

## Offline Code-Shape Provenance Review

Human review of proposal `defed0c211230aad8f8cec6ff80b216223069844`: **PASS**.

Review scope was repository-only. No California SCO request, SCO source-body access, external authority lookup/download, source-value reconstruction, parser change, regex change, normalization change, privacy expansion or workflow creation was performed.

Machine evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json`

Schema:
`schemas/common/property_type_code_shape_provenance_offline_review.schema.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_CODE_SHAPE_PROVENANCE_OFFLINE_REVIEW.md`

Contract test:
`tests/contract/test_ca_sco_property_type_code_shape_provenance_offline_review.py`

Review result SHA:
`b274e9db0a28dae1c9f6a1a25c657978dd27d7b4`

Review CI:
`35003900554` — SUCCESS

### Classification

1. `PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1`
   - `SUPPORTED_BY_REPOSITORY_EVIDENCE`
   - retained data-scope evidence has `PROPERTY_TYPE` as the second field in all four canonical 25-column headers; runner uses zero-based index `1`.

2. `GENERAL_CODE_SHAPE_AA99`
   - `PROVENANCE_INSUFFICIENT`
   - repository records/enforces the regex, but retained authority content does not prove that every non-`ZZZZ` source value must be exactly two uppercase ASCII letters plus two digits.

3. `SPECIAL_CODE_ZZZZ`
   - `PROVENANCE_INSUFFICIENT`
   - `ZZZZ` is permitted by current implementation, but no retained authority content proves it is a valid California SCO special token.

4. `CALIFORNIA_INSURANCE_CODE_SET`
   - `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`
   - repository records `IN01-IN08` and `IN99` and attributes them to an external SCO NAUPA document; that authority document is not archived in the approved offline evidence set.

5. `CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY`
   - `SUPPORTED_BY_REPOSITORY_EVIDENCE`
   - custom projector matches Python `csv.reader(..., strict=True)` on the committed deterministic synthetic matrix only; no universal CSV compatibility claim is allowed.

Aggregate:
- supported by repository evidence: `2`
- external-reference assertion not archived: `1`
- provenance insufficient: `2`

Decision:
`NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE`

## Governance / Safety State

Still fail-closed:

- source policy: `PROPOSED`
- source-level real acquisition authorization: `false`
- registry: disabled/unapproved
- approved real sources: `0`
- semantic compatibility: unresolved
- production classification: inactive
- one-shot workflow: ABSENT
- identity resolution: BLOCKED
- genealogy: BLOCKED
- beneficiary matching: BLOCKED
- outreach: BLOCKED
- claim submission: BLOCKED

Not authorized:
- SCO access or retry;
- external authority retrieval/download;
- reuse of consumed execution/privacy approvals;
- trimming, uppercasing or normalization;
- parser changes;
- regex modification or relaxation;
- logging/privacy expansion;
- source approval or registry activation;
- production classification;
- third real execution.

Any future real execution requires a new proposal plus fresh explicit semantic-execution and transient-row privacy approvals.

## SINGLE NEXT ACTION

A human decision is required before any further provenance acquisition:

**Decide whether to authorize preparation of a separate bounded authority archival / provenance acquisition proposal, or stop this M3 semantic line of work.**

No canonical authorization token for that proposal-preparation decision exists yet; do not invent one silently.

If proposal preparation is authorized, the proposal must remain separate from runtime changes and must define, before any authority access:

- exact authority documents/pages to retrieve;
- permitted network scope;
- archival/provenance format and hashes;
- legal/terms/privacy boundary;
- what claims each authority artifact is intended to prove;
- explicit prohibition on SCO data access and third semantic execution;
- a new human review gate before retrieval or runtime modification.

Do **not** access or download authority content merely to prepare the proposal.

## Context Health / Chat Rotation

The provenance review is complete and CI verified. This is a safe rotation point. If continuing with a new authority-provenance proposal, prefer a fresh chat using this handover as the restart source.

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
second interpretation: DECODED NON-EMPTY SHAPE MISMATCH
second execution/privacy approvals: CONSUMED + NON-REUSABLE
network workflow steady state: ABSENT
provenance proposal SHA: defed0c211230aad8f8cec6ff80b216223069844
provenance proposal CI: 35002920469 SUCCESS
provenance proposal human review: PASS
provenance review result SHA: b274e9db0a28dae1c9f6a1a25c657978dd27d7b4
provenance review CI: 35003900554 SUCCESS
provenance classifications: SUPPORTED=2 / EXTERNAL_REF_NOT_ARCHIVED=1 / INSUFFICIENT=2
semantic change justified: NO
semantic compatibility: UNRESOLVED
source policy: PROPOSED
registry: DISABLED + NOT APPROVED
approved real sources: 0
production classification: INACTIVE
identity/genealogy/matching/outreach/claim: BLOCKED
NEXT: HUMAN DECISION — PREPARE SEPARATE AUTHORITY ARCHIVAL/PROVENANCE ACQUISITION PROPOSAL OR STOP
NO AUTHORITY ACCESS/DOWNLOAD BEFORE SEPARATE PROPOSAL + HUMAN GATE
NO THIRD SCO EXECUTION WITHOUT NEW PROPOSAL + FRESH EXECUTION/PRIVACY APPROVALS
CONTEXT HEALTH: SAFE ROTATION POINT
```
