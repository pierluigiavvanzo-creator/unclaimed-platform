# PROJECT_STATE.md

Last updated: 2026-09-22

## Authoritative product state

The project is in **PRODUCT VALIDATION MODE**.

Primary objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

Governance and source diagnostics remain frozen unless a real execution proves a concrete blocker.

## Canonical integration branch

`main`

`main` remains the canonical integration branch. Product-critical milestone branches are temporary and must not be merged without the Product Owner's explicit authorization.

## Real-source evidence — NY OSC Attempt 9

Attempt 9 executed once against the authorized NY OSC Owner Name File and is now `CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO_RETRY`.

Authoritative non-PII evidence:

`sources/evidence/ny_osc_owner_name_file_ninth_attempt_execution_result.v1.json`

Real result:

- execution status: `BLOCKED`;
- reason: `TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED`;
- archive bytes: `409477526`;
- complete physical records: `14994489`;
- records with exactly 14 pipe bytes: `12`;
- records ending with `|`: `0`;
- records with non-empty bytes after the 14th pipe: `12`;
- records with a pipe count other than 14: `14994477`;
- raw archive logically deleted after execution;
- no raw records or owner values persisted or returned.

The result rejects the proposed empty terminal-field explanation. It does **not** establish that all `14994477` records in the aggregate `other pipe count` bucket have 13 pipes.

## Current product-critical path — NY OSC Attempt 10

Branch:

`mvp1-ny-tenth-product-slice-offline`

PR:

`#28`

Attempt 10 is not another pure source diagnostic. It is a bounded real product-slice package:

`physical record -> structural defer/accept -> Property Type Code -> insurance classification -> aggregate candidate or zero-candidate -> economic actionability state`

Implemented offline:

- treat exactly `13` pipe bytes as the documented `14`-field physical width;
- defer every other physical shape as `DEFER_STRUCTURAL_NONCONFORMING_METADATA_ONLY` without row persistence or repair;
- buffer/decode only field index `1` (`Property Type Code`) on conforming rows;
- reuse the existing exact authority-backed `NY_INSURANCE_CODES` vocabulary and `IN03` MVP-1 primary target from `mvp1_vertical_slice.py`;
- no trimming, casefolding, repair or semantic inference;
- emit only aggregate real product metrics;
- never materialize owner/candidate PII under this package;
- keep recoverable value `UNKNOWN_FROM_SOURCE` and refuse invented case economics;
- dedicated Gate 10 Python entrypoint and PowerShell runner;
- one download / one execution / zero retries design;
- immediate logical deletion of the local archive.

Package checkpoint before this canonical-document update:

`b34a2a283cf45a2e205af4d8944a0b35cb74e6b2`

CI:

`35777375233 — SUCCESS`

Passed: Ruff, mypy, contract tests, smoke tests, full pytest suite, Streamlit safety/startup, frontend lint/typecheck/build.

No NY OSC source access, preflight, download or PII processing occurred while preparing Attempt 10 offline.

## Current next action

Complete CI on the final documented Attempt-10 checkpoint. If green, request only the first two explicit Attempt-10 human gates:

1. `APPROVO NY OSC TENTH TRANSIENT LOCAL FILE BOUNDED ONCE`;
2. `APPROVO NY OSC OWNER NAME FILE TENTH BOUNDED TRANSIENT PII ATTEMPT ONCE`.

Fresh listing preflight and final execution authority remain separate later gates. No Attempt-9 grant may be reused.

## Product exit criteria

Current status:

- authorized real source: ACHIEVED FOR BOUNDED EXECUTIONS;
- bounded real acquisition: ACHIEVED;
- whole-file structural evidence: ACHIEVED VIA ATTEMPT 9;
- real row-defer + insurance classification: ATTEMPT 10 PACKAGE READY OFFLINE, REAL EXECUTION NOT YET AUTHORIZED;
- real candidate or documented zero-candidate aggregate: NOT YET EXECUTED;
- real provenance/evidence package: PARTIAL;
- reproducible real case economics: BLOCKED UNTIL VALUE EVIDENCE EXISTS;
- reviewer case with human GO / REVISE / STOP: NOT DONE;
- commercial baseline: NOT DONE.

If Attempt 10 completes, priority moves immediately to the resulting candidate/zero-candidate evidence and reviewer/economic decision path rather than another parser-diagnostic loop.
