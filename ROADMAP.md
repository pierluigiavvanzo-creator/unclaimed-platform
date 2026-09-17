# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | D-010 CONTINUATION VALIDATED LIVE; INSURANCE DISCOVERY NOT OBSERVED; SOURCE ACTIVATION HELD | run `35243232091` + derived evidence v2 |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — SAME-BYTE DEEPER INSURANCE DISCOVERY NEXT | CA `IN03` remains first high-precision target |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Latest Product-Critical Evidence

Authorized one-shot D-010 module-mode validation:

`35243232091` — attempt `1` — SUCCESS.

Observed live envelope:

- HEAD `1`;
- Range GET `4`;
- HTTP total `5`;
- source bytes `524288`;
- rows examined `16` (`4/member`).

Classification result:

- deferred unclassifiable rows: `16`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- distinct insurance codes: `[]`;
- stop reason: none.

D-010 therefore removed the old whole-source continuation blocker in live execution: all authorized rows were examined. However, the tiny deterministic prefix sample did not demonstrate authority-backed insurance discovery, so California is not activated yet.

Fresh refs used for the run are consumed and non-reusable. The one-shot workflow and trigger were removed after execution.

## Source State

- transport/archive baseline: CONFIRMED LIVE;
- authority semantics: RESOLVED;
- D-010 continuation: VALIDATED LIVE;
- insurance discovery in current sample: NOT OBSERVED;
- California source approval: HELD;
- approved real sources: `0`;
- real candidates: `0`.

This is neither source approval nor source rejection. The current bounded prefix is not statistically representative.

## Next Product Work

Execute exclusively:

`IMPLEMENT_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE`

Classification: `A — Product Critical`.

Purpose:

Increase logical row depth from the already-established compressed Range prefixes while preserving the same future network envelope:

- `1` HEAD;
- `4` Range GETs;
- `131072` bytes per Range;
- `524288` source bytes total;
- no extra Range/full-body fallback;
- no normalization/regex relaxation;
- metadata-only D-010 defer;
- no source-value/row/PII persistence.

The implementation/test step is offline and requires no California source access. After it is green, request fresh single-use execution/privacy approval for one deeper live validation.

Do not repeat the same 16-row run and do not reopen generic transport/CSV diagnostics.
