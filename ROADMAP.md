# ROADMAP.md

Last updated: 2026-09-23

## Product validation critical path

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

No broad platform expansion is scheduled before this is complete.

## Stage 1 — Real-source evidence already established

Attempt 9 scanned the complete real archive under bounded authorization:

- `14994489` physical records;
- `12` records with exactly `14` pipes;
- `0` records ending with a terminal pipe;
- `12` records with non-empty bytes after the 14th pipe;
- `14994477` records with another pipe count;
- no owner/raw values returned;
- authorization consumed, zero retry.

The terminal-empty-field hypothesis is rejected.

Attempt 10 then attempted the first direct real product-slice execution. The manual download occurred, but the product slice did not start because the operator-captured download-start marker fell outside the 900-second fresh-preflight window. Attempt 10 is consumed/non-reusable/zero-retry.

## Stage 2 — Attempt 11: execute the same real product slice with automatic start detection

Active branch:

`mvp1-ny-eleventh-auto-start-detection-offline`

PR:

`#29`

Proposal checkpoint:

`270de2f6e79b7c654052519adc446fe76b811771`

Runner/code checkpoint:

`ce005f08a3bbd23eb8fac6088917109f7864e924`

CI:

`35834948309 — SUCCESS`

Attempt 11 changes only the freshness handoff. The Attempt-10 product slice remains unchanged.

Freshness handoff:

- require at least `180` seconds of preflight freshness before showing the download instruction;
- dedicated temp directory must be empty before arming;
- automatic start detector is armed before the operator is told to download;
- poll every `100 ms`;
- first non-empty file observed in the dedicated directory captures the UTC start marker;
- no first Enter;
- deadline overrun -> fail closed;
- no freshness extension and no retry.

Structural/classification rule:

- exactly `13` pipes -> documented `14` fields -> classify;
- any other pipe count -> metadata-only structural defer;
- buffer/decode only Property Type Code at zero-based index `1`;
- exact authority-backed code matching only;
- `IN03` remains the MVP-1 primary target;
- no owner/candidate PII materialization.

Required real output:

- total records;
- structurally conforming/deferred counts;
- authority-backed insurance count;
- aggregate `IN03` candidate count;
- other-insurance count;
- no-authority-match and unclassifiable counts;
- candidate-present or documented zero-candidate outcome;
- economic actionability state.

Economics remain fail-closed: no invented source value, fee basis, or commercial threshold.

## Stage 3 — Human gates for Attempt 11

Request in order and do not infer one gate from another:

1. `APPROVO NY OSC ELEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE`;
2. `APPROVO NY OSC OWNER NAME FILE ELEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE`;
3. `AUTHORIZE_NY_OSC_ELEVENTH_FRESH_LISTING_PREFLIGHT`;
4. fresh `EXACT_MATCH` receipt;
5. `AUTHORIZE_NY_OSC_ELEVENTH_BOUNDED_EXECUTION_ONCE`;
6. one manual download and one Gate 11 execution, zero retries.

No Attempt-10 grant is reusable.

## Stage 4 — Immediate result consumption

If Attempt 11 returns one or more aggregate `IN03` candidates, move directly to the minimum lawful evidence/value step needed for one reviewer-actionable case.

If it returns zero `IN03` candidates, record the real zero-candidate product result and evaluate source/product fit.

Do not return to parser or timing diagnostics unless the real output proves a new concrete blocker.

## Stage 5 — Economic baseline and Product Owner decision

Capture only evidence-supported measures: records examined, defer rate, insurance survivors, primary candidate count, supported processing/source cost, measured review burden, recoverable value/value band only where evidenced, lawful fee/revenue basis only where evidenced, and main drop-off reasons.

Then Product Owner decision:

`GO / REVISE / STOP`

## Frozen backlog before MVP-1

Unless a direct blocker is demonstrated: new broad diagnostics, governance layers, multi-state expansion, new agent frameworks, graph infrastructure, broad genealogy automation, outreach/contracts/claims automation, non-critical UI polish, and infrastructure refactors.

## Git health

`main` remains canonical. PR #29 isolates Attempt 11 from the consumed Attempt-10 branch. No merge is authorized by offline preparation.
