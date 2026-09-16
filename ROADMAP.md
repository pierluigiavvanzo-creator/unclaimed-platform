# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | V1.2 REAL-SOURCE EXECUTION PROPOSAL HUMAN-REVIEWED PASS; FRESH AUTHORIZATION NEXT | D-008 WHOLE_SOURCE_STOP; proposal accepted as design; execution still unauthorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- historical second semantic execution stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- diagnostic chain remains bounded by `ASCII_STRUCTURAL_MISMATCH` and `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- semantic compatibility with the hidden source value remains unresolved;
- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- v1.2 implementation completed and human-reviewed;
- current runner output contract: `1.2.0`;
- source continuation remains `false`;
- all historical execution/privacy approvals remain consumed and non-reusable.

## v1.2 Real-Source Execution Proposal Review

Reviewed proposal branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal`

Reviewed proposal HEAD:

`a2139884d99bcd0bd1c06ea7374778347bbd64b1`

Reviewed proposal CI:

`35107229194` — **SUCCESS**

Review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW.md`

The proposal remains `PROPOSAL_ONLY_NOT_AUTHORIZED`.

Functional proposal evidence remains:

- checkpoint `19c395a6f89dbec1941566366274070db98cacd0`;
- CI `35106612846` SUCCESS;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- ruff/mypy/frontend/Streamlit checks: PASS.

## Accepted Proposal Boundary

The reviewed design preserves:

- the human-reviewed v1.2 runner and execution schema unchanged;
- 4 canonical members;
- max 4 rows/member and 16 total;
- max 1 HEAD + 4 range requests + 5 HTTP requests;
- max 524288 source response-body bytes total;
- no full-body fallback, additional range or automatic widening;
- exact regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no trim/case/Unicode normalization;
- no parser/projector change;
- D-008 fail-closed mapping if `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs;
- source continuation `false`;
- no precommitted or inferred real-source outcome.

## Fresh Authorization Path

Proposal review does not grant authorization.

Current state remains:

- fresh execution approval: `REQUIRED_NOT_GRANTED`;
- fresh execution approval ref: `null`;
- fresh transient-row privacy approval: `REQUIRED_NOT_GRANTED`;
- fresh privacy approval ref: `null`;
- single-use approval required: `true`;
- workflow creation authorized: `false`;
- real-source execution authorized: `false`.

A separate owner authorization gate is required before the one-shot workflow or real-source execution can be authorized.

## Privacy / Source Governance

No privacy expansion is accepted. Future transient-row handling remains memory-only, immediate-disposal and zero-retention, with no real row/value persistence, quarantine or row-specific human inspection.

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain `0`; production classification and all downstream identity/genealogy/matching/outreach/claim gates remain inactive.

## Next Product Work

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

This gate may decide whether to grant fresh single-use execution/privacy approvals and authorize the bounded one-shot path already reviewed. It must not itself perform source access or execution.

## Still Out of Scope

- real-source access/execution before fresh authorization;
- reuse of consumed approvals;
- source-value reconstruction or inference;
- parser/projector/regex/normalization changes;
- privacy widening;
- source continuation;
- real-row quarantine or row-specific human inspection;
- source/registry/production-classification activation;
- downstream identity resolution, genealogy, beneficiary matching, outreach or claim submission.