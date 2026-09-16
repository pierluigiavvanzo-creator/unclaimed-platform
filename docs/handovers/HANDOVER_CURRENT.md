# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-authorization`

Created from proposal-review checkpoint:

`7714966eb2190209ba2e4dfa52d525fce499009f`

Base CI:

`35120306918` — **SUCCESS**

## Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

Authorization result:

`PASS_FRESH_SINGLE_USE_EXECUTION_PRIVACY_APPROVALS_GRANTED_ONE_SHOT_PATH_AUTHORIZED_EXECUTION_NOT_PERFORMED`

Authorization artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION.md`

Meaning:

- the reviewed bounded v1.2 one-shot real-source path is authorized;
- fresh execution/privacy approvals are granted but not consumed;
- creation of the temporary one-shot workflow is authorized for the later execution task;
- exactly one real-source execution is authorized;
- this authorization task performed no source access, created no network workflow and performed no real-source execution.

## Reviewed Proposal Evidence

Reviewed proposal HEAD:

`a2139884d99bcd0bd1c06ea7374778347bbd64b1`

Reviewed proposal CI:

`35107229194` — **SUCCESS**

Proposal review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Proposal id:

`ca.sco.segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution`

Proposal version:

`1.0.0`

## Fresh Approval References

Execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

State of each approval:

`GRANTED_NOT_CONSUMED`

Both are fresh, single-use, non-reusable, proposal-bound to version `1.0.0` / SHA `a2139884d99bcd0bd1c06ea7374778347bbd64b1`, and runtime-bound to `1.2.0`.

All historical execution/privacy approvals remain consumed and non-reusable.

The fresh approvals become consumed only once the later one-shot workflow actually invokes the authorized real-source execution. They are not consumed by authorization documentation, repository-local CI, workflow-file creation or a pre-execution failure.

No automatic retry is authorized.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect, in this order as relevant:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION.md`
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW.md`
3. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL.md`
4. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`
5. `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`
6. `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py`
7. `scripts/ca_sco_property_type_semantic_verification.py`
8. `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`
9. historical v1.1 execution evidence as needed.

## Governing Runtime / D-008 State

Decision:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

Current runner output contract:

`1.2.0`

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

If `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs, exact accepted behavior remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation after trigger = `false`;
- later members after trigger are not requested;
- silent row skip is not allowed.

Other stops and non-stopped outcomes retain `control_disposition = null`.

The authorization does not predict or precommit any real-source outcome.

## Authorized One-Shot Caps

The execution boundary remains:

- 4 canonical members;
- max 4 data rows/member and 16 total;
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

## Privacy / Persistence Boundary

Fresh privacy authorization permits only the transient in-memory full-row observation strictly required by the reviewed runner for the single bounded execution.

Memory-only, immediate-disposal and zero-retention remain mandatory. No raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact-length persistence, record values in logs, real-row quarantine or row-specific human inspection is authorized.

`control_disposition` remains limited to non-value-bearing `status_code` and `reason_code`.

No privacy expansion is authorized.

## Source / Downstream Governance

Current state:

- fresh execution approval granted: `true`;
- fresh privacy approval granted: `true`;
- fresh approvals consumed: `false`;
- workflow creation authorized: `true`;
- real-source execution authorized: `true`;
- real-source execution performed: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

`DECISIONS.md` is intentionally unchanged because this authorization is bounded under existing D-008 and introduces no new architectural design decision.

## SINGLE NEXT ACTION

Execute exclusively:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

This next task must remain separate from the authorization gate.

Required sequence:

1. verify the remote HEAD and latest CI of this authorization branch;
2. read the five canonical files in order plus the authorization/proposal artifacts;
3. create a dedicated execution branch from the verified authorization checkpoint;
4. create the temporary `.github/workflows/ca-sco-property-type-semantic-verification-once.yml` only on that execution branch;
5. bind the workflow to exactly the two fresh approval refs above and the reviewed `1.2.0` runner/path;
6. CI-validate the workflow and authorization evidence before any source request;
7. perform exactly one bounded real-source execution using the frozen caps and validation/privacy boundaries;
8. do not automatically retry;
9. persist only permitted derived evidence;
10. mark both fresh approvals consumed once real execution occurs, regardless of semantic result;
11. remove the temporary workflow immediately after the run;
12. stop at `HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`.

## Do Not Do During the Next Execution

Do not widen sample or transport caps; do not add fallback/ranges/retries; do not infer or reconstruct hidden source values; do not persist real rows/values; do not modify runner/parser/projector/regex/normalization; do not reuse historical approvals; do not enable source continuation; do not activate source policy, registry or production classification; do not begin identity resolution, genealogy, beneficiary matching, outreach or claim work.

## Restart Instruction

1. verify remote HEAD of the current authorization branch;
2. verify latest CI for that exact HEAD;
3. read canonical five files in order;
4. read authorization artifact and proposal review/proposal/schema/test;
5. execute only the `SINGLE NEXT ACTION`;
6. stop after workflow removal/evidence persistence at the separate human evidence-review gate.