# PROJECT_STATE.md

Last updated: 2026-09-23

## Authoritative product state

The project is in **PRODUCT VALIDATION MODE**.

Primary objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

Governance and source diagnostics remain frozen unless a real execution proves a concrete blocker.

## Canonical integration branch

`main`

`main` remains the canonical integration branch. Product-critical milestone branches are temporary and must not be merged without the Product Owner's explicit authorization.

## Real-source evidence — NY OSC Attempt 9

Attempt 9 executed once and is `CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO_RETRY`.

Authoritative non-PII evidence:

`sources/evidence/ny_osc_owner_name_file_ninth_attempt_execution_result.v1.json`

Observed aggregate result:

- status `BLOCKED`;
- reason `TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED`;
- archive bytes `409477526`;
- physical records `14994489`;
- exactly-14-pipe records `12`;
- records ending with `|`: `0`;
- non-empty data after the 14th pipe: `12`;
- records with any other pipe count: `14994477`;
- no owner/raw values returned.

The empty-terminal-field hypothesis is rejected. The `14994477` aggregate bucket must not be interpreted as all 13-pipe records.

## Real-source evidence — NY OSC Attempt 10

Attempt 10 received fresh exact-match metadata and one bounded execution authorization. One manual download occurred, but the product slice did not start.

Authoritative non-PII evidence:

`sources/evidence/ny_osc_owner_name_file_tenth_attempt_execution_result.v1.json`

Result:

- status `BLOCKED`;
- reason `AUTHORIZED_DOWNLOAD_START_OUTSIDE_FRESH_PREFLIGHT_WINDOW`;
- failure stage `BUILD_REAL_EXECUTION_AUTHORIZATION_V1_6`;
- the runner had already confirmed `FINDERS.zip` existed before invoking Python;
- classification did not start;
- no candidate/zero-candidate result was produced;
- no owner values or raw path were returned;
- authorization is treated as `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- zero retry;
- runner cleanup was attempted, but physical secure erasure is not guaranteed.

Root cause: Gate 10 depended on the operator pressing Enter to capture the download-start marker. That marker was recorded after the 900-second preflight deadline.

## Current product-critical path — NY OSC Attempt 11

Branch:

`mvp1-ny-eleventh-auto-start-detection-offline`

PR:

`#29`

Attempt 11 reuses the Attempt-10 product slice unchanged and modifies only the freshness handoff.

Proposal checkpoint:

`270de2f6e79b7c654052519adc446fe76b811771`

Runner/code checkpoint:

`ce005f08a3bbd23eb8fac6088917109f7864e924`

CI:

`35834948309 — SUCCESS`

Passed: Ruff, mypy, contract tests, smoke tests, full pytest suite, Streamlit safety/startup, frontend lint/typecheck/build.

Gate 11 behavior:

- requires at least `180` freshness seconds remaining before exposing the download instruction;
- creates a new dedicated empty OS temp directory;
- arms automatic detection before instructing the operator to start the manual download;
- polls the dedicated directory every `100 ms`;
- captures the authorized download-start marker at the first observation of any non-empty file in that previously empty directory;
- no operator Enter is used for the start marker;
- if no start is observed before the preflight deadline, execution stops fail-closed;
- completion confirmation remains one manual Enter after the same single download finishes;
- one download / one execution / zero retry;
- no direct network client in the runner;
- product slice remains: 13 pipes -> documented 14-field width -> Property Type Code index 1 -> exact authority-backed insurance classification -> aggregate IN03 candidate or zero-candidate result;
- all other physical shapes are deferred metadata-only;
- owner/candidate PII is not materialized by this package;
- recoverable value remains `UNKNOWN_FROM_SOURCE`.

No NY OSC access, fresh preflight, download, or PII processing occurred while preparing Attempt 11 offline.

## Current next action

Request only the first two new Attempt-11 grants:

1. `APPROVO NY OSC ELEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE`;
2. `APPROVO NY OSC OWNER NAME FILE ELEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE`.

Fresh preflight and final execution authorization remain separate later gates. No Attempt-10 authorization may be reused.

## Product exit criteria

Current status:

- authorized real source: ACHIEVED FOR BOUNDED EXECUTIONS;
- bounded real acquisition: ACHIEVED;
- whole-file structural evidence: ACHIEVED VIA ATTEMPT 9;
- real row-defer + insurance classification: ATTEMPT 11 PACKAGE READY OFFLINE;
- real candidate or documented zero-candidate aggregate: NOT YET PRODUCED;
- real provenance/evidence package: PARTIAL;
- reproducible real case economics: BLOCKED UNTIL VALUE EVIDENCE EXISTS;
- reviewer case with human GO / REVISE / STOP: NOT DONE;
- commercial baseline: NOT DONE.

If Attempt 11 completes, priority moves immediately downstream to candidate/zero-candidate evidence, value/economics, and reviewer actionability rather than another parser/timing loop.
