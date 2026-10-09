# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution Authorization

Date: 2026-09-16

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — PASS — FRESH SINGLE-USE EXECUTION + PRIVACY APPROVALS GRANTED — ONE-SHOT PATH AUTHORIZED — EXECUTION NOT PERFORMED**

## Authorization gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

## Authoritative checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- authorization base branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal-review`
- authorization base HEAD: `7714966eb2190209ba2e4dfa52d525fce499009f`
- authorization base CI: `35120306918` — **SUCCESS**
- reviewed proposal HEAD: `a2139884d99bcd0bd1c06ea7374778347bbd64b1`
- reviewed proposal CI: `35107229194` — **SUCCESS**
- proposal review result: `PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`
- proposal id: `ca.sco.segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution`
- proposal version: `1.0.0`
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`
- governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- runtime contract: `1.2.0`

The owner instructed the system to continue the canonical `SINGLE NEXT ACTION`. This authorization interprets that instruction only as approval to complete this authorization gate. It does not perform the separately gated real-source execution.

## Decision

`PASS_FRESH_SINGLE_USE_EXECUTION_PRIVACY_APPROVALS_GRANTED_ONE_SHOT_PATH_AUTHORIZED_EXECUTION_NOT_PERFORMED`

The reviewed bounded one-shot v1.2 real-source verification path is authorized for exactly one future execution under the frozen proposal boundary.

## Fresh approval references

The authorization gate creates the following explicit non-secret governance identifiers:

Execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both approvals are:

- status: `GRANTED_NOT_CONSUMED`;
- fresh: `true`;
- single-use: `true`;
- reusable: `false`;
- bound to proposal version `1.0.0`;
- bound to reviewed proposal SHA `a2139884d99bcd0bd1c06ea7374778347bbd64b1`;
- bound to runtime contract `1.2.0`;
- valid only for the exact sample, transport, validation and privacy boundaries below;
- not substitutes for, and not derived from, any historical approval.

All historical execution/privacy approvals remain consumed and non-reusable.

The fresh approvals become consumed when the later authorized one-shot workflow actually invokes the real-source execution. They are not consumed by this authorization record, repository-local CI, workflow-file creation, or a failure that occurs before any real-source execution begins. No automatic retry is authorized.

## Authorized execution scope

A later dedicated execution task may:

1. create the temporary workflow `.github/workflows/ca-sco-property-type-semantic-verification-once.yml`;
2. pin that workflow to the reviewed/authorized path and exact fresh approval refs above;
3. CI-validate the workflow and authorization evidence before any source request;
4. perform exactly one bounded real-source execution of `scripts/ca_sco_property_type_semantic_verification.py` using execution schema `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
5. persist only the derived evidence permitted by the reviewed v1.2 contract/privacy boundary;
6. remove the temporary workflow immediately after the single run;
7. mark both fresh approvals consumed once the real execution occurs;
8. stop at a separate evidence-review gate.

Workflow creation is authorized: `true`.

Real-source execution is authorized: `true`.

Real-source execution performed by this gate: `false`.

## Fixed sample / transport caps

Authorization is limited exactly to:

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
- no automatic widening;
- no automatic retry.

## Validation / D-008 boundary

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Authorization permits no trim, case conversion, Unicode normalization, alternate-token acceptance, regex relaxation, parser change or projector change.

If the later execution encounters `PROPERTY_TYPE_FORMAT_UNEXPECTED`, the accepted v1.2 result remains exactly:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation after trigger = `false`;
- later members after trigger are not requested;
- silent row skip is not allowed.

For unrelated stops and non-stopped outcomes, `control_disposition = null`.

This authorization does not infer, predict or precommit any real-source outcome and does not treat one bounded run as proof of global source semantics, frequency or future compatibility.

## Privacy / persistence authorization

The fresh privacy approval authorizes only the transient in-memory full-row observation strictly required by the reviewed runner to project `PROPERTY_TYPE` during the single bounded execution.

The authorized privacy boundary remains:

- memory-only;
- zero retention days;
- immediate disposal;
- no raw-body persistence;
- no full-row persistence;
- no `PROPERTY_ID` persistence;
- no owner/holder persistence;
- no per-row `PROPERTY_TYPE` persistence;
- no offending bytes persistence;
- no offending-value hash persistence;
- no offending-value exact-length persistence;
- no record values in logs;
- no real-row quarantine persistence;
- no row-specific human inspection.

Persisted `control_disposition` remains limited to non-value-bearing `status_code` and `reason_code`, alongside only the derived execution summary fields already allowed by the reviewed proposal/runtime contract.

No privacy expansion is authorized.

## Source / production separation

This execution-specific authorization does not activate the source for production use.

The following remain unchanged:

- source policy: `PROPOSED`;
- registry enabled: `false`;
- registry approved for use: `false`;
- approved real sources: `0`;
- semantic compatibility resolved: `false`;
- production classification active: `false`;
- source continuation authorized: `false`;
- identity resolution: blocked;
- genealogy: blocked;
- beneficiary matching: blocked;
- outreach: blocked;
- claim submission: blocked.

## Explicitly not performed by this gate

This authorization task did not:

- request the CA SCO source;
- request any new authority source;
- access source-body bytes;
- inspect a real row/field;
- infer or reconstruct the hidden source value;
- create the temporary network workflow;
- perform real-source execution;
- modify runtime, execution schema, parser/projector, regex or normalization;
- modify source policy or registry;
- consume the fresh approvals;
- widen privacy or continuation;
- activate production/downstream gates.

`DECISIONS.md` remains unchanged because this gate grants a bounded execution authorization under the already accepted D-008 design; it does not introduce a new architectural decision.

## Next single action

Execute exclusively:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

The execution task must create and CI-validate the temporary one-shot workflow, use exactly the two fresh approval refs above, perform no more than one authorized real-source execution, persist only permitted derived evidence, remove the workflow immediately after the run, mark the approvals consumed, and stop at:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

No downstream product gate opens automatically from the execution outcome.