# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ca-property-type-row-defer-live-validation-once`

Latest product-critical lifecycle:

`AUTHORIZE_D010_LIVE_VALIDATION -> CONSUME_SINGLE_USE_APPROVALS -> PRE_NETWORK_CLI_FAILURE -> OFFLINE_LAUNCH_REMEDIATION`

Classification: `A — Product Critical`.

Authorization/execution audit:

`docs/audits/M3_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_AUTHORIZATION.md`

## D-010 State

D-010 remains the selected California SCO MVP-1 classification policy:

`ROW_DEFER_CONTINUE_METADATA_ONLY`

Nonconforming or unknown insurance-like `PROPERTY_TYPE` values are not normalized, repaired, persisted or inferred. They are represented by an aggregate deferred-row count while later rows may continue.

Exact authority-backed insurance vocabulary remains:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN08, IN99`

Primary high-precision MVP-1 target remains:

`IN03 — Proceeds Due Beneficiaries`

Transport/header/CSV-column/hard-cap failures remain whole-source fail-closed.

## Authorized Attempt Result

Product Owner authorization:

`APPROVO D010 LIVE VALIDATION + TRANSIENT-ROW PRIVACY`

Fresh single-use refs minted for that authorization:

- execution: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_BOUNDED_B2AF7877`;
- privacy: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_TRANSIENT_ROW_PRIVACY_BOUNDED_B2AF7877`.

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

One-shot run:

`35237721059` — attempt `1` — FAILED before SCO network access.

The authorization preflight passed and the approvals were deliberately consumed before network. The execution process then failed during top-level Python import with:

`ModuleNotFoundError: No module named 'scripts'`

Because the import failed before `main()` and before `legacy.HttpTransport()` construction:

- SCO requests issued: `0`;
- SCO response-body bytes read: `0`;
- live rows examined: `0`;
- live semantic evidence produced: `none`;
- source approval/rejection decision from this attempt: `none`.

No rerun under the consumed refs is authorized.

## CLI Launch Remediation

Root cause was invocation mode, not D-010 runtime semantics.

The D-010 runner is restored byte-for-byte to the previously reviewed/authorized blob:

`8e952a80105d56a8e84e6fb9feb5524dd01625d0`

Future one-shot execution must invoke it from repository root as:

`python -m scripts.ca_sco_mvp1_property_type_validation ...`

A subprocess unit test now validates module-mode startup offline with `--help`, closing the exact packaging gap that caused run `35237721059` to fail.

The temporary live workflow and trigger from the consumed attempt have been removed together. No live workflow remains armed.

## Product / Commercial State

- live transport/archive baseline: **CONFIRMED** from prior executions;
- California authority vocabulary: **RESOLVED**;
- D-010 row-defer semantics: **IMPLEMENTED OFFLINE**;
- D-010 runner semantic blob: **UNCHANGED**;
- D-010 module-mode launch remediation: **IMPLEMENTED OFFLINE**;
- latest D-010 authorized attempt: **ABORTED PRE-NETWORK**;
- approved real sources: `0`;
- real MVP-1 candidate cases: `0`.

This pre-network packaging failure is not evidence against the California source and does not reopen transport or generic `PROPERTY_TYPE` diagnostics.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_CA_SCO_MVP1_PROPERTY_TYPE_ROW_DEFER_REAL_SOURCE_VALIDATION_REAUTHORIZATION_AFTER_PRENETWORK_CLI_REMEDIATION`

Classification: `A — Product Critical`.

A new explicit Product Owner authorization is required because the previous execution/privacy refs are consumed and non-reusable even though no SCO request occurred.

After fresh authorization:

`fresh single-use refs -> one module-mode bounded live D-010 validation -> source decision -> if PASS, bounded CA insurance activation -> MVP-1 candidate/economics/reviewer`

Do not retry or reuse `B2AF7877`, widen transport/sample caps, or reopen generic diagnostics absent new contradictory evidence.
