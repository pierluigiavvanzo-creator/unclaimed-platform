# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | WHOLE_SOURCE_STOP DESIGN ACCEPTED; IMPLEMENTATION PROPOSAL NEXT | policy-decision review PASS; D-008 accepted as design; runtime implementation not authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- first bounded diagnostic run `35019840276`: `ASCII_STRUCTURAL_MISMATCH`;
- source-format one-shot execution run `35090057224`: SUCCESS;
- source-format class: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- all historical execution/privacy approvals consumed and non-reusable;
- nonconforming-row handling proposal and its human review completed;
- policy-decision proposal package `33abf635dc2b3f3893300b5e6adf3e35abeefcb8` CI `35095481531`: SUCCESS;
- proposal final HEAD `5e6f538a03f0b5e61c4559a27431e9718b29e265` CI `35095734936`: SUCCESS;
- human policy-decision proposal review: `PASS_POLICY_DECISION_ACCEPTED_AS_DESIGN_IMPLEMENTATION_NOT_AUTHORIZED`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- decision recorded as `D-008`;
- runtime implementation remains unauthorized and unchanged;
- no remediation performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Accepted Design — Runtime Still Gated

The accepted `WHOLE_SOURCE_STOP` design separates control disposition from source continuation.

Control disposition for a future separately authorized implementation:

- status `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- metadata-only;
- no real row/field retention.

Source continuation:

- continuation after trigger: `false`;
- later rows after trigger: `false`;
- silent skip/continuation: `false`.

The accepted design preserves the current fail-closed behavior and does not resolve or reinterpret the hidden source value.

## Next Product Work

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL`

The implementation proposal must describe the smallest deterministic code/contract/test changes required to implement D-008, including rollback and regression coverage. Preparation does not authorize those code changes or any real-source execution.

## Still Out of Scope

- runtime policy implementation before a later explicit review/authorization gate;
- another real source execution without a new reviewed authorization path;
- reuse of consumed approvals;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- source continuation after the nonconforming row;
- real-row quarantine persistence;
- row-specific human inspection without separate privacy authorization;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
