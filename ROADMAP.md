# ROADMAP.md

Last updated: 2026-09-22

## Product validation critical path

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

No broad platform expansion is scheduled before this is complete.

## Stage 1 — Real-source execution evidence

Attempts 8 and 9 established real-source transport and structure under bounded single-use authorization.

Attempt 9 whole-file result:

- `14994489` physical records scanned;
- `12` records with exactly `14` pipes;
- `0` records ending in a terminal pipe;
- `12` records with non-empty bytes after the 14th pipe;
- `14994477` records with a pipe count different from 14;
- no raw/owner values returned;
- archive logically deleted;
- authorization consumed, zero retry.

The empty-terminal-field hypothesis is rejected. The aggregate `other pipe count` bucket must not be interpreted as all having 13 pipes without another observation.

## Stage 2 — Attempt 10: execute a real product slice

Active branch:

`mvp1-ny-tenth-product-slice-offline`

PR:

`#28`

Attempt 10 directly advances the product slice instead of opening another pure diagnostic phase.

Structural rule:

- exactly `13` pipe bytes -> documented `14` fields -> eligible for classification;
- any other pipe count -> `DEFER_STRUCTURAL_NONCONFORMING_METADATA_ONLY`;
- no repair, trimming or structural inference.

Classification rule:

- buffer/decode only `Property Type Code` at documented zero-based index `1`;
- reuse existing authority-backed `NY_INSURANCE_CODES`;
- exact code match only;
- `IN03` is the existing MVP-1 primary target;
- no owner/candidate PII materialization in this execution package.

Required real output:

- total records;
- structurally conforming records;
- structurally deferred records;
- authority-backed insurance records;
- `IN03` aggregate candidate records;
- other insurance records;
- records with no authority-backed insurance match;
- unclassifiable Property Type Code records;
- aggregate candidate or documented zero-candidate outcome;
- economic actionability state.

Economics remain fail-closed:

- source value: `UNKNOWN_FROM_SOURCE`;
- no invented dollar value;
- no invented fee basis;
- candidate-present result -> `VALUE_EVIDENCE_REQUIRED`;
- zero-candidate result -> `ZERO_CANDIDATE_NO_CASE_ECONOMICS`.

Offline package checkpoint before canonical-document updates:

`b34a2a283cf45a2e205af4d8944a0b35cb74e6b2`

CI:

`35777375233 — SUCCESS`

All Python quality/tests, Streamlit checks and frontend lint/typecheck/build passed.

No source access or real PII processing occurred during offline package preparation.

## Stage 3 — Human gates for Attempt 10

Only after the final documented checkpoint is CI green, request in order:

1. `APPROVO NY OSC TENTH TRANSIENT LOCAL FILE BOUNDED ONCE`;
2. `APPROVO NY OSC OWNER NAME FILE TENTH BOUNDED TRANSIENT PII ATTEMPT ONCE`;
3. `AUTHORIZE_NY_OSC_TENTH_FRESH_LISTING_PREFLIGHT`;
4. fresh `EXACT_MATCH` receipt;
5. `AUTHORIZE_NY_OSC_TENTH_BOUNDED_EXECUTION_ONCE`;
6. one manual download and one Gate 10 execution, zero retries.

No earlier grant is reusable.

## Stage 4 — Immediate result consumption

If Attempt 10 produces one or more aggregate `IN03` candidates, move directly to the minimum lawful evidence/value step needed to make one candidate reviewer-actionable. Do not perform identity resolution, beneficiary matching, outreach, representation or claim activity without their separate later gates.

If Attempt 10 produces zero `IN03` candidates, record the real zero-candidate outcome and evaluate source/product fit rather than returning to parser experimentation by default.

Exit criterion: a real reviewer-facing candidate/economic evidence path or a documented real zero-candidate product result.

## Stage 5 — Economic baseline and Product Owner decision

Capture only evidence-supported measures:

- records examined;
- structurally deferred rate;
- records surviving insurance classification;
- primary candidate count;
- processing/source cost where supportable;
- human review burden where measured;
- recoverable value/value band only where evidence exists;
- lawful fee/revenue basis only where evidence exists;
- main failure/drop-off reasons.

Then Product Owner decision:

`GO / REVISE / STOP`

## Frozen backlog before MVP-1

Unless a direct blocker is demonstrated:

- new source-diagnostic programs;
- broad parser research;
- new governance layers;
- multi-state expansion;
- new agent frameworks;
- graph infrastructure;
- broad genealogy automation;
- outreach/contracts/claims automation;
- non-critical UI polish;
- infrastructure refactors without direct MVP-1 value.

## Git health

`main` remains canonical. PR #28 isolates the Attempt-10 delta from Attempt 9. No merge is authorized by offline preparation.
