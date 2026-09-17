# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | AUTHORITY SEMANTICS RESOLVED; D-010 ROW-DEFER IMPLEMENTED OFFLINE; LIVE VALIDATION NEXT | exact CA insurance vocabulary + row-defer continuation tests |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — ONE LIVE ROW-DEFER VALIDATION FROM SOURCE DECISION | CA `IN03` is first high-precision target |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Critical-path state

Resolved:

- live transport/archive baseline;
- parser/projector field agreement;
- California authority provenance;
- exact California insurance vocabulary `IN01-IN08`, `IN99`;
- product rule that `IN03 = Proceeds Due Beneficiaries` is the first narrow MVP-1 target;
- deterministic metadata-only row defer for nonconforming/unknown insurance tokens;
- continuation after deferred rows in the product validator;
- no normalization, source-value persistence or silent omission.

D-010 supersedes D-008 whole-source continuation behavior only for this MVP-1 classification path. Transport/header/CSV-column/hard-cap failures remain fail-closed.

## Next Product Work

Execute exclusively:

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION`

Classification: `A — Product Critical`.

After fresh single-use execution + transient-row privacy authorization:

`one bounded live D-010 validation -> source decision -> bounded CA insurance activation -> candidate -> economics -> reviewer`

No additional generic PROPERTY_TYPE or transport diagnostics are on the critical path.
