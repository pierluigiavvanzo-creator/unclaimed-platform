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

## Real-source result — NY OSC attempt 8

Attempt 8 executed once against the authorized real NY OSC Owner Name File and is now consumed/non-reusable/zero-retry.

Non-PII execution evidence:

`sources/evidence/ny_osc_owner_name_file_eighth_attempt_execution_result.v1.json`

Real result:

- execution status: `BLOCKED`;
- reason: `UNEXPECTED_DATA_FIELD_COUNT`;
- archive bytes: `409477526`;
- complete records: `2490891`;
- documented field count: `14`;
- observed structural field count: `15`;
- raw/structural pipe count: `14`;
- quote bytes: `0`;
- header: `NO_HEADER_OBSERVED`;
- Property Type Code column index: `1` zero-based;
- Property Type Code ASCII records: `2490891`;
- raw archive logically deleted after execution;
- owner rows/values were not persisted or returned.

Freshness binding to the download-start marker worked as designed.

The runner then emitted a post-result `NameError` caused by the inline `python -c` status comparison losing quoting under PowerShell. The structured execution result had already been emitted and is authoritative; the wrapper error did not change the real structural result.

## Current concrete blocker

Attempt 8 demonstrated one narrow structural hypothesis worth testing:

`14 documented fields + a terminal pipe -> empty 15th structural field`

This is not assumed. It requires one bounded aggregate-only confirmation.

## NY OSC attempt 9 offline package

Branch:

`mvp1-ny-ninth-trailing-delimiter-bounded-offline`

PR:

`#27` targeting the attempt-8 branch so the attempt-9 delta is isolated.

Implemented:

- attempt-8 non-PII execution-result evidence;
- bounded trailing-delimiter diagnostic;
- runtime/result contract v1.6;
- structural normalization allowed only when every complete record has exactly 14 pipes, every record ends with `|`, and the 15th field contains zero bytes;
- fail-closed result when any record violates that condition;
- dedicated Python entrypoint replacing the fragile PowerShell `python -c` wrapper;
- raw archive deletion after runtime;
- no owner/raw values in serializable results;
- zero retry / one execution design.

Package CI before canonical-document updates:

`35771193204 — SUCCESS`

No NY OSC source access, preflight, download or PII processing occurred while preparing attempt 9 offline.

## Current next action

Finish CI on the final documented attempt-9 checkpoint, then — and only then — request the separate attempt-9 human gates in order:

1. transient-local retention authorization;
2. transient-PII authorization;
3. fresh listing preflight authorization and `EXACT_MATCH` receipt;
4. final single-use bounded execution authorization;
5. one manual download and one Gate 9 execution, zero retries.

No attempt-8 authorization may be reused.

## Product exit criteria

Current status:

- one authorized real source: ACHIEVED FOR BOUNDED EXECUTION;
- one bounded real acquisition: ACHIEVED BUT STRUCTURALLY BLOCKED;
- structural blocker diagnosis: ATTEMPT 9 PACKAGE IMPLEMENTED, REAL CONFIRMATION NOT YET AUTHORIZED;
- real normalization/classification: NOT DONE;
- real candidate or documented zero-candidate full-pipeline result: NOT DONE;
- real provenance/evidence package: PARTIAL;
- reproducible real case economics: NOT DONE;
- reviewer case with human GO / REVISE / STOP: NOT DONE;
- commercial baseline: NOT DONE.

If attempt 9 confirms the terminal-empty-field hypothesis, do not open another parser-research loop: treat the documented 14 fields as structurally confirmed after removal of the terminal empty transport field and move downstream as directly as the privacy/source gates allow.
