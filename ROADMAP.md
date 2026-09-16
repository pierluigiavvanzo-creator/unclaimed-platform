# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | IMPLEMENTATION DESIGN REVIEW PASSED; IMPLEMENTATION AUTHORIZATION NEXT | D-008 WHOLE_SOURCE_STOP design accepted; implementation proposal reviewed PASS; runtime unchanged |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- bounded diagnostic run `35019840276`: `ASCII_STRUCTURAL_MISMATCH`;
- source-format one-shot run `35090057224`: SUCCESS;
- source-format class: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- all historical execution/privacy approvals consumed and non-reusable;
- nonconforming-row handling design review completed;
- policy-decision review accepted `WHOLE_SOURCE_STOP` as design;
- decision recorded as `D-008`;
- implementation proposal branch reviewed at `e9af9d61b2f216de58cd8f3ad6a6925c38aef172`;
- reviewed proposal CI `35098004540`: SUCCESS;
- implementation proposal human review result: `PASS_IMPLEMENTATION_PROPOSAL_ACCEPTED_AS_DESIGN_RUNTIME_IMPLEMENTATION_NOT_AUTHORIZED`;
- implementation design accepted: `true`;
- runtime remains schema `1.1.0` and unchanged;
- future schema `1.2.0` remains proposed only and does not exist yet;
- runtime implementation authorized: `false`;
- real-source execution authorized: `false`;
- no remediation or real-source execution performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Accepted Implementation Design — Still Gated

The reviewed minimum implementation remains additive and versioned:

- reuse the existing runner and existing `RunnerStop` fail-closed behavior;
- keep historical execution schema v1.1 immutable;
- future runner output schema becomes `1.2.0` only after a later explicit implementation authorization;
- future v1.2 adds nullable `control_disposition`;
- only legacy `PROPERTY_TYPE_FORMAT_UNEXPECTED` maps to:
  - `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
  - `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- legacy `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED` remain present;
- other stops and success keep `control_disposition = null`;
- source continuation remains `false`;
- no value-bearing source data enters the new control vocabulary.

## Regression / Rollback

A later authorized implementation must preserve synthetic/offline regression coverage for legacy compatibility, exact D-008 mapping, no later-member request after trigger, null disposition for other outcomes, privacy constraints and unchanged validation behavior.

No real-source execution is required to validate the code implementation itself. Any real-source execution remains a later separate gate.

Rollback remains revert of implementation commit(s) only; no database, source-state or historical evidence migration is required.

## Next Product Work

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION`

This gate may authorize only the reviewed runtime/schema/test implementation plus synthetic/offline validation. It must not itself perform the implementation, authorize a real-source execution, widen privacy, enable continuation, change validation semantics, activate source/registry/production classification or enter downstream work.

## Still Out of Scope

- runtime implementation before explicit implementation authorization;
- creation of execution schema v1.2 before explicit implementation authorization;
- another real source execution without a new separately reviewed authorization path;
- reuse of consumed approvals;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- source continuation after the nonconforming row;
- real-row quarantine persistence;
- row-specific human inspection;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
