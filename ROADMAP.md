# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | D-010 READY; FIRST AUTHORIZED ATTEMPT ABORTED PRE-NETWORK; MODULE-LAUNCH REMEDIATED; FRESH REAUTHORIZATION NEXT | run `35237721059` + consumed refs + module-mode regression test |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — ONE FRESH AUTHORIZED D-010 LIVE VALIDATION FROM SOURCE DECISION | CA `IN03` remains first high-precision target |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Critical-path state

Resolved:

- live transport/archive baseline from prior bounded executions;
- parser/projector field agreement;
- California authority provenance;
- exact California insurance vocabulary `IN01-IN08`, `IN99`;
- product rule that `IN03 = Proceeds Due Beneficiaries` is the first narrow MVP-1 target;
- deterministic metadata-only row defer for nonconforming/unknown insurance tokens;
- continuation after deferred rows in the product validator;
- no normalization, source-value persistence or silent omission;
- operational CLI packaging defect from first D-010 attempt: future execution uses module-mode invocation.

D-010 supersedes D-008 whole-source continuation behavior only for this MVP-1 classification path. Transport/header/CSV-column/hard-cap failures remain fail-closed.

## First D-010 Authorization Attempt

Owner authorization:

`APPROVO D010 LIVE VALIDATION + TRANSIENT-ROW PRIVACY`

One-shot run:

`35237721059`, attempt `1`.

The workflow preflight passed and fresh execution/privacy refs were consumed before source access. The process then failed at Python import because the workflow invoked the package-owned runner by file path rather than module path.

Observed source use for this failed attempt:

- SCO HEAD: `0`;
- SCO Range GET: `0`;
- SCO source bytes: `0`;
- live rows: `0`.

Therefore this attempt creates no positive or negative semantic evidence about the live source.

Consumed refs:

- `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_BOUNDED_B2AF7877`;
- `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_TRANSIENT_ROW_PRIVACY_BOUNDED_B2AF7877`.

They are non-reusable and no rerun is permitted.

## Remediation

The D-010 runner remains unchanged at blob:

`8e952a80105d56a8e84e6fb9feb5524dd01625d0`

Future one-shot workflows must invoke:

`python -m scripts.ca_sco_mvp1_property_type_validation ...`

A subprocess regression test covers this exact startup mode offline. The failed attempt's temporary workflow and trigger have been removed.

## Next Product Work

Execute exclusively:

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_REAUTHORIZATION_AFTER_PRENETWORK_CLI_REMEDIATION`

Classification: `A — Product Critical`.

After fresh explicit execution + transient-row privacy authorization:

`fresh single-use refs -> one module-mode bounded live D-010 validation -> source decision -> bounded CA insurance activation if supported -> candidate -> economics -> reviewer`

No generic PROPERTY_TYPE or transport diagnostic is on the critical path.
