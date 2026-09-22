# ROADMAP.md

Last updated: 2026-09-22

## Product validation critical path

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

No broad platform expansion is scheduled before this is complete.

## Stage 1 — Real-source authorization and first execution

NY OSC attempt 8 completed the first bounded real download/execution under single-use authorization.

Result:

- authorization consumed;
- freshness correctly bound to download start;
- real archive processed transiently and deleted;
- execution blocked on `UNEXPECTED_DATA_FIELD_COUNT`;
- documented fields: `14`;
- observed fields: `15`;
- raw/structural pipes: `14`;
- complete records: `2490891`;
- quote bytes: `0`;
- no owner values returned or persisted.

Exit criterion for this stage: ACHIEVED AS A BOUNDED REAL EXECUTION WITH A SPECIFIC STRUCTURAL BLOCKER.

## Stage 2 — Attempt 9: resolve the proven blocker once

Attempt 9 is the only active source-diagnostic exception because attempt 8 produced a concrete blocker.

Offline package branch:

`mvp1-ny-ninth-trailing-delimiter-bounded-offline`

PR:

`#27`

Pre-documentation package CI:

`35771193204 — SUCCESS`

Attempt-9 execution hypothesis:

`14 documented fields + terminal | -> empty 15th structural field`

Bounded real execution must emit aggregate counters only:

- complete records;
- records with exactly 14 pipes;
- records ending with `|`;
- records with a non-empty 15th field;
- records with any other pipe count;
- classification.

Continuation rule:

If and only if every complete record has exactly 14 pipes, every record ends with `|`, the 15th field contains zero bytes, and no record has another pipe count, classify:

`DOCUMENTED_14_FIELDS_WITH_TERMINAL_DELIMITER`

and allow structural normalization to documented width `14` in that same execution result.

Any exception returns `BLOCKED` / `TRAILING_DELIMITER_HYPOTHESIS_NOT_CONFIRMED`.

Runner fix:

- no inline `python -c` status wrapper;
- dedicated Python entrypoint;
- one download maximum;
- one execution maximum;
- zero retries;
- no direct network client;
- dedicated OS temp;
- immediate logical deletion;
- no raw/owner values returned.

Next gates, only after final package CI is green:

1. `APPROVO NY OSC NINTH TRANSIENT LOCAL FILE BOUNDED ONCE`;
2. `APPROVO NY OSC OWNER NAME FILE NINTH BOUNDED TRANSIENT PII ATTEMPT ONCE`;
3. `AUTHORIZE_NY_OSC_NINTH_FRESH_LISTING_PREFLIGHT`;
4. fresh `EXACT_MATCH` receipt;
5. `AUTHORIZE_NY_OSC_NINTH_BOUNDED_EXECUTION_ONCE`;
6. one Gate 9 execution.

No attempt-8 grant is reusable.

## Stage 3 — Immediate downstream product slice

If attempt 9 confirms the terminal-empty-field hypothesis, stop parser/source-diagnostic work and move directly toward:

`normalized real mapping -> insurance classification -> candidate or documented zero-candidate -> provenance/evidence -> economics -> reviewer`

Reuse the existing synthetic MVP-1 path/contracts rather than building a parallel framework.

Exit criterion: at least one real reviewer case or one documented zero-candidate full-pipeline result.

## Stage 4 — Economic baseline

Capture:

- records examined;
- records surviving insurance classification;
- candidates produced;
- candidate-to-review conversion;
- automated cost/candidate;
- source cost/candidate where applicable;
- human review time/candidate;
- recoverable value/value band where evidentially supportable;
- fee/revenue basis where legally supportable;
- unresolved/manual research burden;
- main drop-off reasons.

Exit criterion: one reproducible economic result visible to the Product Owner.

## Stage 5 — Product decision

Product Owner decision:

`GO / REVISE / STOP`

Only after this decision should the project consider multi-state expansion, graph infrastructure, broader agent automation, genealogy automation, additional source programs or major UI/infrastructure work.

## Frozen backlog before MVP-1

Unless a direct blocker is demonstrated:

- new governance layers;
- new source diagnostics beyond attempt 9;
- parser research unrelated to the real blocker;
- new agent frameworks;
- graph databases/evidence-graph infrastructure;
- multi-state expansion;
- broad genealogy automation;
- outreach/contracts/claims automation;
- non-critical UI polish;
- infrastructure refactors.

## Git health

`main` remains the canonical integration branch. PR #27 isolates the attempt-9 delta from the attempt-8 package. No merge is authorized by the offline preparation itself.
