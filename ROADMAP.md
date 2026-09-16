# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | V1.2 IMPLEMENTATION HUMAN-REVIEWED PASS; REAL-SOURCE EXECUTION STILL SEPARATELY GATED | D-008 WHOLE_SOURCE_STOP; v1.2 additive control disposition accepted as conforming |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- bounded diagnostic run `35019840276`: `ASCII_STRUCTURAL_MISMATCH`;
- source-format one-shot run `35090057224`: SUCCESS;
- source-format class: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- all historical execution/privacy approvals consumed and non-reusable;
- policy-decision review accepted `WHOLE_SOURCE_STOP` as design and recorded `D-008`;
- implementation proposal review: `PASS_IMPLEMENTATION_PROPOSAL_ACCEPTED_AS_DESIGN_RUNTIME_IMPLEMENTATION_NOT_AUTHORIZED`;
- owner authorization: `PASS_BOUNDED_IMPLEMENTATION_AUTHORIZED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- offline implementation completed on branch `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-offline`;
- reviewed implementation HEAD: `7d40f410752cdaef96faeae4aaafc1ca86b13e18`;
- reviewed implementation CI `35101304555`: SUCCESS;
- implementation review: `PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- current runner output contract: `1.2.0`;
- v1.2 execution schema created: `true`;
- historical v1.1 schema preserved unchanged at blob `33c829116eea0b568cfe16c664ffbeee9d00e013`;
- synthetic/offline regression validation: PASS;
- completed implementation human-reviewed: `true`;
- real-source execution authorized: `false`;
- no real-source execution performed by implementation or review;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Accepted v1.2 Control Contract

The reviewed implementation is additive and versioned:

- existing runner and existing `RunnerStop` fail-closed behavior are reused;
- historical execution schema v1.1 remains immutable;
- current runner output contract is `1.2.0`;
- v1.2 adds nullable `control_disposition`;
- only legacy `PROPERTY_TYPE_FORMAT_UNEXPECTED` maps to:
  - `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
  - `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- legacy `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED` remain present;
- other stops and successful/inconclusive outcomes keep `control_disposition = null`;
- source continuation remains `false`;
- no source-value-bearing data enters the new control vocabulary.

## Regression / Rollback

Synthetic/offline regression coverage verifies legacy compatibility, exact D-008 mapping, no later-member request after the trigger, null disposition for unrelated outcomes, privacy constraints, historical v1.1 evidence validity and unchanged validation behavior.

Functional checkpoint evidence:

- contract: `235 passed`;
- smoke: `6 passed`;
- full pytest: `292 passed`;
- ruff/mypy/frontend/Streamlit checks: PASS.

Final reviewed HEAD CI `35101304555` is SUCCESS.

Rollback remains revert of implementation commits only; no database, source-state or historical-evidence migration is required.

## Next Product Work

Prepare exclusively:

`PREPARE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL`

This next action is proposal-only. It may define a fresh, separately reviewable execution/privacy authorization path for a bounded v1.2 real-source verification, but it must not itself access the source, authorize or perform execution, reuse consumed approvals, widen privacy, enable continuation, change validation semantics, activate source/registry/production classification or enter downstream work.

## Still Out of Scope

- any real-source execution without a fresh separately reviewed authorization path;
- reuse or invention of execution/privacy approvals during proposal preparation;
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
