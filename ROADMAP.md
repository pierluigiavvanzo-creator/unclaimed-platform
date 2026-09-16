# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | V1.2 REAL-SOURCE EXECUTION FRESH SINGLE-USE AUTHORIZED; ONE-SHOT EXECUTION NEXT | D-008 WHOLE_SOURCE_STOP; proposal/review PASS; fresh approvals granted, not consumed |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- v1.2 implementation completed and human-reviewed;
- current runner output contract: `1.2.0`;
- real-source execution proposal prepared and human-reviewed PASS;
- proposal review result: `PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- authorization gate completed;
- authorization result: `PASS_FRESH_SINGLE_USE_EXECUTION_PRIVACY_APPROVALS_GRANTED_ONE_SHOT_PATH_AUTHORIZED_EXECUTION_NOT_PERFORMED`;
- source continuation remains `false`;
- all historical execution/privacy approvals remain consumed and non-reusable.

## Fresh Single-Use Authorization

Execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both are:

- `GRANTED_NOT_CONSUMED`;
- fresh;
- single-use;
- non-reusable;
- bound to proposal version `1.0.0`;
- bound to reviewed proposal SHA `a2139884d99bcd0bd1c06ea7374778347bbd64b1`;
- bound to runtime contract `1.2.0`.

Workflow creation authorized: `true`.

Real-source execution authorized: `true`.

Real-source execution performed: `false`.

Fresh approvals consumed: `false`.

The fresh approvals become consumed only when the later one-shot workflow actually invokes the authorized real-source execution. No automatic retry is authorized.

## Authorized One-Shot Boundary

The future execution is limited to the reviewed plan:

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

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, parser/projector change or regex relaxation is authorized.

If `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs, D-008 remains exact:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation = `false`;
- later members after the trigger are not requested.

No real-source outcome is predicted or precommitted.

## Privacy / Source Governance

The fresh privacy approval permits only transient in-memory row observation strictly necessary for the reviewed runner. Memory-only, immediate-disposal and zero-retention remain mandatory.

No raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact-length persistence, record values in logs, real-row quarantine or row-specific human inspection is authorized.

`control_disposition` remains limited to non-value-bearing `status_code` and `reason_code`.

Source policy remains `PROPOSED`. Registry remains disabled/unapproved. Approved real sources remain `0`. Semantic compatibility remains unresolved. Production classification and all downstream identity/genealogy/matching/outreach/claim gates remain inactive.

## Next Product Work

Execute exclusively:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

The execution task must:

1. create the temporary one-shot workflow on a dedicated execution branch;
2. use exactly the two fresh approval refs above;
3. CI-validate the workflow and authorization evidence before source access;
4. perform exactly one bounded real-source execution;
5. persist only permitted derived evidence;
6. remove the temporary workflow immediately after the run;
7. mark both fresh approvals consumed once the execution occurs;
8. stop at `HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`.

## Still Out of Scope

- any widening of sample or transport caps;
- any automatic retry;
- reuse of consumed historical approvals;
- source-value reconstruction or inference;
- parser/projector/regex/normalization changes;
- privacy widening or real-row persistence;
- source continuation;
- source/registry/production-classification activation;
- downstream identity resolution, genealogy, beneficiary matching, outreach or claim submission.