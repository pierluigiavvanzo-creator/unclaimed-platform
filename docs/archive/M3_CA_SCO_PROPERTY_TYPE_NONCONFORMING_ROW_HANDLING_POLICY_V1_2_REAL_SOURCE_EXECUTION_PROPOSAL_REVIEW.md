# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy v1.2 Real-Source Execution Proposal Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS — PROPOSAL ACCEPTED AS DESIGN — FRESH AUTHORIZATION REQUIRED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- proposal branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal`
- reviewed proposal HEAD: `a2139884d99bcd0bd1c06ea7374778347bbd64b1`
- reviewed proposal CI: `35107229194` — **SUCCESS**
- functional proposal checkpoint: `19c395a6f89dbec1941566366274070db98cacd0`
- functional proposal CI: `35106612846` — **SUCCESS**
- governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- accepted design policy: `WHOLE_SOURCE_STOP`
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`
- proposal schema: `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL.md`

This review is repository-only. It performs no request to the CA SCO source, no source-body or real-row access, no approval granting, no workflow creation and no real-source execution.

## Decision

`PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

The proposal is accepted as a bounded, non-authorizing design for a future separately authorized v1.2 real-source verification.

This PASS does **not** grant execution or privacy approval, authorize workflow creation, authorize source access, perform execution, widen privacy, enable continuation, activate source policy/registry/production classification or open downstream work.

## Proposal contract / non-authorizing state

PASS.

The proposal remains explicitly:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

The versioned proposal schema fixes that state and rejects authorization widening. Contract tests verify:

- fresh execution approval status is `REQUIRED_NOT_GRANTED`;
- fresh execution approval ref is `null`;
- fresh transient-row privacy approval status is `REQUIRED_NOT_GRANTED`;
- fresh privacy approval ref is `null`;
- workflow creation authorization is `false`;
- real execution authorization is `false`;
- approvals must be single-use;
- the one-shot workflow is absent during proposal review.

## Historical approval separation

PASS.

All historical execution/privacy approvals remain consumed and non-reusable. The proposal does not reuse, reinterpret or silently reactivate any prior approval reference.

A fresh authorization gate remains mandatory after this review.

## Base checkpoint / runtime immutability

PASS.

The proposal is pinned to the CI-green human-reviewed v1.2 checkpoint and references the accepted `1.2.0` execution contract.

Comparison from base `7b6397f0e89d8ee1640be2eea4f8651f6b74478c` to reviewed proposal HEAD `a2139884d99bcd0bd1c06ea7374778347bbd64b1` contains only:

- proposal JSON;
- proposal schema;
- proposal contract test;
- proposal audit;
- `PROJECT_STATE.md`;
- `ROADMAP.md`;
- `docs/handovers/HANDOVER_CURRENT.md`.

No runner, v1.2 execution schema, parser/projector module, source policy, registry or network workflow changed.

## Sample / transport boundary

PASS and unchanged.

The proposal preserves the existing reviewed caps:

- 4 canonical members;
- max 4 data rows/member;
- max 16 data rows total;
- max 1 HEAD request;
- max 4 range requests;
- max 5 HTTP requests total;
- max 131072 response bytes/range;
- max 524288 source response-body bytes total;
- max 262144 transient uncompressed bytes/member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes/logical record;
- no additional range;
- no full-body fallback;
- no automatic widening.

The contract test binds these values to the current runner constants.

## Validation semantics

PASS and unchanged.

Regex remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The proposal permits no trim, case conversion, Unicode normalization, alternate-token acceptance, regex relaxation, parser change or projector change.

## D-008 outcome boundary

PASS.

The proposal preserves the accepted fail-closed contract **if** a later separately authorized execution encounters `PROPERTY_TYPE_FORMAT_UNEXPECTED`:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation after trigger = `false`;
- later members after trigger are not requested;
- silent row skip is not allowed.

For unrelated stops and non-stopped outcomes, `control_disposition = null`.

The proposal does not assert that the real source will produce this stop and makes no semantic claim about the hidden source value.

## Privacy / persistence boundary

PASS; no expansion.

A future execution still requires fresh transient-row privacy approval before transient full-row observation.

The proposed boundary remains memory-only, immediate-disposal and zero-retention, with no persistence of raw bodies, full rows, `PROPERTY_ID`, owner/holder values, per-row `PROPERTY_TYPE`, offending bytes, hashes or exact lengths, and no record values in logs.

No real-row quarantine and no row-specific human inspection are proposed.

The v1.2 `control_disposition` remains limited to non-value-bearing `status_code` and `reason_code`.

## Outcome neutrality / proof boundary

PASS.

The proposal explicitly does not precommit, infer or predict a real-source result. One bounded execution is scoped only to checking conformance of the reviewed v1.2 execution path and cannot prove global source semantics, frequency or future compatibility.

## Workflow boundary

PASS.

The proposal does not create `.github/workflows/ca-sco-property-type-semantic-verification-once.yml`.

A later workflow is only contemplated after fresh authorization and must be one-shot, branch-pinned, require fresh execution/privacy refs and be removed after execution.

## Source / downstream governance

PASS and closed.

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain `0`; semantic compatibility remains unresolved; production classification remains inactive; identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

## CI evidence

PASS.

Reviewed final proposal CI `35107229194` is SUCCESS for both `quality` and `streamlit-candidate` on reviewed HEAD `a2139884d99bcd0bd1c06ea7374778347bbd64b1`.

Functional proposal CI `35106612846` recorded:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

## Governance state after review

- D-008 accepted as design: `true`;
- v1.2 implementation completed and human-reviewed: `true`;
- real-source execution proposal prepared: `true`;
- proposal human-reviewed: `true`;
- proposal review result: `PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- fresh execution approval granted: `false`;
- fresh privacy approval granted: `false`;
- workflow creation authorized: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- runtime/schema/parser/projector changed by review: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- downstream gates remain closed.

## Next explicit action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

That gate may decide whether to grant fresh single-use execution/privacy approvals and authorize the separately bounded one-shot workflow/execution defined by the reviewed proposal. It must remain separate from the execution itself and must perform no source access.