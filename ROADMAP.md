# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | V1.2 REAL-SOURCE EXECUTION PROPOSAL PREPARED + CI GREEN; HUMAN PROPOSAL REVIEW NEXT | D-008 WHOLE_SOURCE_STOP; v1.2 implementation accepted; real execution still unauthorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- bounded diagnostic run `35019840276`: `ASCII_STRUCTURAL_MISMATCH`;
- source-format one-shot run `35090057224`: SUCCESS;
- source-format class: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- semantic compatibility with the hidden source value remains unresolved;
- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- v1.2 implementation completed and human-reviewed;
- implementation review result: `PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- current runner output contract: `1.2.0`;
- historical v1.1 schema preserved at blob `33c829116eea0b568cfe16c664ffbeee9d00e013`;
- source continuation remains `false`;
- all historical execution/privacy approvals remain consumed and non-reusable.

## v1.2 Real-Source Execution Proposal

Proposal branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-proposal`

Functional proposal checkpoint:

`19c395a6f89dbec1941566366274070db98cacd0`

Functional CI:

`35106612846` — **SUCCESS**

Prepared artifacts:

- `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.schema.json`;
- `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`;
- `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.py`;
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL.md`.

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

Functional CI evidence:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `242 passed`;
- smoke tests: `6 passed`;
- full pytest: `299 passed`;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

## Fresh Authorization Path — Defined, Not Granted

The proposal requires a later separate review and fresh single-use authorization path.

Current authorization state remains:

- execution approval: `REQUIRED_NOT_GRANTED`;
- execution approval ref: `null`;
- transient-row privacy approval: `REQUIRED_NOT_GRANTED`;
- privacy approval ref: `null`;
- network workflow creation authorized: `false`;
- real-source execution authorized: `false`.

No approval token was created or granted during proposal preparation.

If the proposal is later accepted, a separate authorization gate remains required before any workflow creation or real-source execution.

## Frozen Execution Boundary

The proposal preserves the human-reviewed v1.2 runner and its caps without runtime modification:

- 4 canonical members;
- 4 rows/member, 16 total;
- 1 HEAD + max 4 ranges, max 5 HTTP requests total;
- max 524288 source response-body bytes total;
- no full-body fallback, additional range or automatic widening.

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, casing, Unicode normalization, parser/projector change or regex relaxation is proposed.

D-008 remains exact: if `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs in a later authorized execution, legacy fail-closed status/reason remain and the non-value-bearing control disposition is `PROPERTY_TYPE_NONCONFORMING_STOPPED / PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`; source continuation remains false.

The proposal does not predict or precommit that this outcome will occur on the real source.

## Privacy / Source Governance

No privacy expansion is proposed. A future transient-row observation requires fresh privacy approval and remains memory-only, immediate-disposal, zero-retention, with no row/value persistence, row quarantine or row-specific human inspection.

Source policy remains `PROPOSED`. Registry remains disabled/unapproved. Approved real sources remain `0`. Production classification and all downstream identity/genealogy/matching/outreach/claim gates remain inactive.

Proposal preparation performed no request to `claimit.ca.gov`, no source-body access and no real-source execution.

## Next Product Work

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

That review may accept or reject only the proposal design. It must not grant fresh approvals, create the network workflow, authorize or perform real-source execution, widen privacy or continuation, modify validation/runtime, activate source/registry/production classification or enter downstream work.

## Still Out of Scope

- real-source access or execution before separate authorization;
- reuse of consumed execution/privacy approvals;
- invention or granting of approvals during proposal review;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or Unicode normalization changes;
- automatic source-value remediation;
- source continuation after the nonconforming row;
- real-row quarantine persistence;
- row-specific human inspection;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
