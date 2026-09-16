# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

California SCO `PROPERTY_TYPE` handling remains governed by `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`, accepted policy `WHOLE_SOURCE_STOP`, implementation strategy `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`, and current runner output contract `1.2.0`.

The v1.2 implementation and its real-source execution proposal have both passed their human reviews.

The separate fresh authorization gate is now completed.

Authorization result:

`PASS_FRESH_SINGLE_USE_EXECUTION_PRIVACY_APPROVALS_GRANTED_ONE_SHOT_PATH_AUTHORIZED_EXECUTION_NOT_PERFORMED`

This authorizes exactly one future bounded v1.2 real-source execution under the reviewed proposal. No real-source execution was performed by the authorization gate.

## Authorization Checkpoint

Authorization branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-authorization`

Authorization base branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal-review`

Authorization base HEAD:

`7714966eb2190209ba2e4dfa52d525fce499009f`

Authorization base CI:

`35120306918` — **SUCCESS**

Reviewed proposal HEAD:

`a2139884d99bcd0bd1c06ea7374778347bbd64b1`

Reviewed proposal CI:

`35107229194` — **SUCCESS**

Authorization artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION.md`

## Fresh Single-Use Approvals

Execution approval ref:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval ref:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

State of both approvals:

`GRANTED_NOT_CONSUMED`

Both are fresh, single-use, non-reusable and bound to:

- proposal id `ca.sco.segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution`;
- proposal version `1.0.0`;
- reviewed proposal SHA `a2139884d99bcd0bd1c06ea7374778347bbd64b1`;
- runtime contract `1.2.0`;
- exact reviewed sample, transport, validation and privacy boundaries.

All historical execution/privacy approvals remain consumed and non-reusable.

The fresh approvals become consumed only when the later one-shot workflow actually begins the authorized real-source execution. No automatic retry is authorized.

## Authorized One-Shot Boundary

Workflow creation authorized: `true`.

Real-source execution authorized: `true`.

Real-source execution performed: `false`.

The later execution may create temporary path:

`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

It must be branch-pinned, use exactly the fresh approval refs above, perform exactly one bounded execution, remove the workflow immediately after the run, persist only permitted derived evidence and stop at evidence review.

Existing caps remain unchanged:

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

## Runtime / D-008 Boundary

Runner remains:

`scripts/ca_sco_property_type_semantic_verification.py`

Execution schema remains:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

If `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs, accepted result remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation = `false`;
- later members after trigger are not requested.

For unrelated stops and non-stopped outcomes, `control_disposition = null`.

No real-source outcome is predicted or precommitted.

## Privacy / Persistence Boundary

Fresh privacy authorization allows only transient in-memory row observation strictly required by the reviewed runner during the single execution.

Memory-only, immediate-disposal and zero-retention remain mandatory. No raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact-length persistence, record values in logs, real-row quarantine or row-specific human inspection is authorized.

`control_disposition` remains limited to non-value-bearing `status_code` and `reason_code`.

No privacy expansion is authorized.

## Source / Product Governance State

- D-008 accepted as design: `true`;
- v1.2 implementation completed and human-reviewed: `true`;
- real-source execution proposal prepared and human-reviewed: `true`;
- fresh execution approval granted: `true`;
- fresh privacy approval granted: `true`;
- fresh approvals consumed: `false`;
- workflow creation authorized: `true`;
- real-source execution authorized: `true`;
- real-source execution performed: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged: `true`;
- regex/normalization unchanged: `true`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Execute exclusively:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

That execution must remain within the exact authorization boundary, consume the two fresh approvals only when the real execution occurs, remove the temporary workflow after the run, and stop at:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.