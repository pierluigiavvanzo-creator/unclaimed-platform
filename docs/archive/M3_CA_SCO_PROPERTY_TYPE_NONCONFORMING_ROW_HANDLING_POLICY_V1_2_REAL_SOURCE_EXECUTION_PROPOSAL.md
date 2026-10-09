# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy v1.2 Real-Source Execution Proposal

Date: 2026-09-16

Status: **PROPOSAL PREPARED — CI GREEN — HUMAN PROPOSAL REVIEW REQUIRED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Task

`PREPARE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL`

## Authoritative base

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- base branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-implementation-review`
- base HEAD: `7b6397f0e89d8ee1640be2eea4f8651f6b74478c`
- base CI: `35105522139` — **SUCCESS**
- implementation review result: `PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`
- governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- accepted policy: `WHOLE_SOURCE_STOP`
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

## Proposal checkpoint

Proposal branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal`

Functional proposal checkpoint:

`19c395a6f89dbec1941566366274070db98cacd0`

GitHub Actions CI:

`35106612846` — **SUCCESS**

Verified markers:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- reviewer frontend lint: PASS;
- reviewer frontend typecheck: PASS;
- reviewer frontend build: PASS;
- Streamlit safety smoke: PASS;
- Streamlit startup smoke: PASS.

## Prepared artifacts

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Proposal schema:

`schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py`

The proposal is explicitly `PROPOSAL_ONLY_NOT_AUTHORIZED`.

## Proposed bounded execution question

A later, separately authorized execution would ask only whether the already human-reviewed `1.2.0` runner, when applied under the unchanged deterministic bounded prefix sample, produces an output conforming to the v1.2 execution contract, including the exact D-008 `control_disposition` mapping **if** `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs.

The proposal does not precommit, infer or predict any real-source outcome. One bounded execution would not prove global source semantics, frequency or future compatibility.

## Fresh authorization boundary

All historical execution/privacy approvals remain consumed and non-reusable.

The proposal requires, but does not grant:

- fresh execution approval;
- fresh transient-row privacy approval;
- single-use authorization;
- later explicit authorization for creation of the one-shot network workflow;
- later explicit authorization for the real execution itself.

Current proposal values remain:

- `execution_approval_status = REQUIRED_NOT_GRANTED`;
- `execution_approval_ref = null`;
- `transient_row_privacy_approval_status = REQUIRED_NOT_GRANTED`;
- `transient_row_privacy_approval_ref = null`;
- `network_workflow_creation_authorized = false`;
- `real_execution_authorized = false`.

No approval token was invented, created or granted during proposal preparation.

## Bounded sample / transport caps

The proposal preserves the existing runner limits without widening:

- 4 canonical members;
- max 4 data rows per member;
- max 16 data rows total;
- max 1 HEAD request;
- max 4 range requests;
- max 5 HTTP requests total;
- max 131072 response bytes per range;
- max 524288 source response body bytes total;
- max 262144 transient uncompressed bytes per member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes per logical record;
- no additional range;
- no full-body fallback;
- no automatic widening.

## Validation / runtime boundary

The reviewed v1.2 runtime remains unchanged by this proposal.

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The proposal permits no:

- trim;
- case conversion;
- Unicode normalization;
- alternate-token acceptance;
- regex relaxation;
- parser change;
- projector change.

Current execution schema remains:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

Current runner remains:

`scripts/ca_sco_property_type_semantic_verification.py`

## D-008 outcome boundary

If a later authorized execution encounters `PROPERTY_TYPE_FORMAT_UNEXPECTED`, the accepted contract remains exactly:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation after trigger = `false`;
- later members after trigger = not requested.

For unrelated stops and non-stopped outcomes, `control_disposition = null`.

This proposal does not claim that the hidden real source value is semantically invalid in the source system.

## Privacy / persistence boundary

A future execution would require fresh transient-row privacy approval before observing transient full-row bytes.

The proposal retains:

- memory-only transient handling;
- zero retention days;
- immediate disposal;
- no raw-body persistence;
- no full-row persistence;
- no `PROPERTY_ID` persistence;
- no owner/holder persistence;
- no per-row `PROPERTY_TYPE` persistence;
- no offending bytes, hash or exact-length persistence;
- no record values in logs;
- no real-row quarantine;
- no row-specific human inspection.

The non-value-bearing `control_disposition` remains limited to:

- `status_code`;
- `reason_code`.

No privacy expansion is proposed.

## Workflow boundary

The historical one-shot path remains only a planned future path:

`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

This proposal does not create it.

A later authorized workflow, if separately approved, must be single-use, branch-pinned, require fresh execution/privacy refs and be removed after execution.

## Explicitly not performed

This proposal preparation did **not**:

- access `claimit.ca.gov`;
- access a new authority source;
- perform a network request;
- access source-body bytes;
- inspect any real row or field;
- infer or reconstruct the hidden real `PROPERTY_TYPE` value;
- modify the reviewed v1.2 runtime;
- modify the v1.2 execution schema;
- modify source policy;
- modify the source registry;
- create a one-shot network workflow;
- reuse consumed approvals;
- create or grant new execution/privacy approvals;
- widen privacy;
- enable source continuation;
- activate source policy, registry or production classification;
- enter identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Governance state after proposal preparation

- v1.2 implementation human-reviewed: `true`;
- proposal prepared: `true`;
- proposal contract validation: `PASS`;
- proposal human-reviewed: `false`;
- fresh execution approval granted: `false`;
- fresh privacy approval granted: `false`;
- network workflow creation authorized: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- downstream gates remain closed.

## Next gate

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

That review may accept or reject only this proposal design. A PASS must not itself create approval tokens, create the network workflow, authorize execution or perform real-source access. A later separate authorization gate remains required before any real-source execution.
