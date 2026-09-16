# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

The California SCO `PROPERTY_TYPE` handling path is governed by `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE` with accepted policy `WHOLE_SOURCE_STOP` and implementation strategy `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`.

The v1.2 runtime implementation is complete, CI-green and human-reviewed as conforming. Current runner output contract remains `1.2.0`.

A bounded non-executing proposal for a future v1.2 real-source verification has now also passed human proposal review.

Proposal review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Real-source execution remains unauthorized. Fresh single-use execution/privacy authorization is the next separate gate.

## Proposal Review Checkpoint

Review branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal-review`

Reviewed proposal HEAD:

`a2139884d99bcd0bd1c06ea7374778347bbd64b1`

Reviewed proposal CI:

`35107229194` — **SUCCESS**

Functional proposal checkpoint:

`19c395a6f89dbec1941566366274070db98cacd0`

Functional proposal CI:

`35106612846` — **SUCCESS**

Proposal review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW.md`

Proposal artifact:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Proposal remains:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

## Accepted v1.2 Runtime Boundary

Runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Execution schema:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

Historical v1.1 schema remains immutable.

For `PROPERTY_TYPE_FORMAT_UNEXPECTED`, accepted behavior remains exactly:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation = `false`.

Other stops and non-stopped outcomes retain `control_disposition = null`.

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

## Reviewed Future Execution Boundary

The accepted proposal preserves the existing bounded sample/transport plan:

- 4 canonical members;
- max 4 rows/member and 16 rows total;
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

The proposal does not precommit or infer a real-source outcome and does not prove global source semantics, frequency or future compatibility.

## Fresh Authorization State

All historical execution/privacy approvals remain consumed and non-reusable.

Current state remains:

- fresh execution approval: `REQUIRED_NOT_GRANTED`;
- fresh execution approval ref: `null`;
- fresh transient-row privacy approval: `REQUIRED_NOT_GRANTED`;
- fresh privacy approval ref: `null`;
- single-use approval required: `true`;
- workflow creation authorized: `false`;
- real-source execution authorized: `false`.

No approval token was created or granted by proposal review.

## Privacy / Persistence Boundary

Future transient full-row observation still requires fresh privacy approval.

The accepted proposal remains memory-only, immediate-disposal and zero-retention. It does not permit raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact-length persistence, record values in logs, real-row quarantine or row-specific human inspection.

`control_disposition` remains limited to non-value-bearing `status_code` and `reason_code`.

No privacy expansion is authorized.

## CI / Scope Evidence

Reviewed final proposal CI `35107229194` is SUCCESS on exact reviewed HEAD `a2139884d99bcd0bd1c06ea7374778347bbd64b1`.

Functional proposal CI `35106612846` recorded:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

Diff from the prior human-reviewed v1.2 checkpoint contains only proposal/schema/test/audit and durable state/handover documentation. Runtime, execution schema, policy, registry and network workflow were not modified.

## Governance State

- D-008 accepted as design: `true`;
- v1.2 implementation completed: `true`;
- v1.2 implementation human-reviewed: `true`;
- real-source execution proposal prepared: `true`;
- real-source execution proposal human-reviewed: `true`;
- proposal review result: `PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- fresh execution approval granted: `false`;
- fresh privacy approval granted: `false`;
- workflow creation authorized: `false`;
- real-source execution authorized: `false`;
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

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

That gate may decide whether to grant fresh single-use execution/privacy approvals and authorize the reviewed one-shot execution path. It must not itself access the source or perform the execution.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.