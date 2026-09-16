# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal-review`

Created from reviewed proposal checkpoint:

`a2139884d99bcd0bd1c06ea7374778347bbd64b1`

Base proposal CI:

`35107229194` — **SUCCESS**

## Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

Review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW.md`

Meaning:

- the v1.2 real-source execution proposal is accepted as a bounded design;
- proposal/schema/test are coherent with D-008 and the human-reviewed v1.2 runtime;
- fresh single-use execution/privacy authorization is still required;
- workflow creation is not authorized;
- real-source execution is not authorized;
- this review performed no source access and no runtime change.

## Reviewed Proposal Evidence

Reviewed proposal HEAD:

`a2139884d99bcd0bd1c06ea7374778347bbd64b1`

Reviewed proposal CI:

`35107229194` — **SUCCESS**

Functional proposal checkpoint:

`19c395a6f89dbec1941566366274070db98cacd0`

Functional proposal CI:

`35106612846` — **SUCCESS**

Verified functional markers:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect, in this order as relevant:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW.md`
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL.md`
3. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`
4. `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`
5. `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py`
6. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_IMPLEMENTATION_REVIEW.md`
7. `scripts/ca_sco_property_type_semantic_verification.py`
8. `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`
9. historical v1.1 execution schema/evidence as needed.

## Governing Decision / Runtime State

Decision:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted policy:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

Current runner output contract remains `1.2.0`.

Exact accepted behavior if `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation after trigger = `false`;
- later members after trigger are not requested.

Other stops and non-stopped outcomes retain `control_disposition = null`.

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, parser/projector change or regex relaxation is accepted.

## Reviewed Proposal Boundary

Proposal status remains:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

The reviewed design preserves existing sample/transport caps:

- 4 canonical members;
- max 4 rows/member and 16 total;
- max 1 HEAD, 4 ranges, 5 HTTP requests;
- max 131072 bytes/range;
- max 524288 source response-body bytes total;
- max 262144 transient uncompressed bytes/member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes/logical record;
- no additional range;
- no full-body fallback;
- no automatic widening.

The proposal does not precommit, infer or predict any real-source result.

## Fresh Authorization State

All historical execution/privacy approvals remain consumed and non-reusable.

Current state:

- fresh execution approval: `REQUIRED_NOT_GRANTED`;
- fresh execution approval ref: `null`;
- fresh transient-row privacy approval: `REQUIRED_NOT_GRANTED`;
- fresh privacy approval ref: `null`;
- single-use approval required: `true`;
- workflow creation authorized: `false`;
- real-source execution authorized: `false`.

No fresh approval token has yet been created or granted.

## Privacy / Persistence Boundary

Future transient full-row observation still requires fresh privacy approval.

Memory-only, immediate-disposal and zero-retention remain mandatory. No raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact-length persistence, record values in logs, real-row quarantine or row-specific human inspection is authorized.

`control_disposition` remains limited to non-value-bearing `status_code` and `reason_code`.

No privacy expansion is authorized.

## Source / Downstream Governance

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain `0`; semantic compatibility remains unresolved; production classification is inactive; identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

`DECISIONS.md` is intentionally unchanged because this review accepts a proposal under existing D-008 and introduces no new architectural decision.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

This is an authorization gate only.

It may decide whether to grant fresh single-use execution/privacy approvals and authorize the bounded one-shot workflow/execution described by the reviewed proposal. It must not itself access the source or perform the execution.

## Do Not Do During the Next Authorization Gate

Do not:

- access the real CA SCO source or new authority sources;
- perform real-source execution;
- infer/reconstruct the hidden source value;
- change runtime, parser/projector, regex or normalization;
- reuse historical approvals;
- widen privacy or source continuation;
- activate source policy, registry or production classification;
- begin downstream identity, genealogy, beneficiary matching, outreach or claim work.

Any fresh approval refs created by the authorization gate must be explicit, single-use, proposal-bound and not treated as consumed until the later execution task actually uses them.

## Restart Instruction

1. verify remote HEAD of the current review branch;
2. verify latest CI for that exact HEAD;
3. read the five canonical files in order;
4. read review artifact + proposal audit/proposal/schema/test;
5. execute only the `SINGLE NEXT ACTION`;
6. keep authorization separate from real-source execution.