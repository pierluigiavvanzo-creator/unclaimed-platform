# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | D-010 CONTINUATION VALIDATED LIVE; SAME-BYTE DEEPER DISCOVERY VALIDATOR READY OFFLINE; FRESH LIVE AUTHORIZATION NEXT | run `35243232091` + offline CI `35244998206` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — ONE SAME-BYTE DEEPER LIVE VALIDATION FROM SOURCE DECISION | CA `IN03` remains first high-precision target |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Latest Live Evidence

D-010 module-mode live validation:

`35243232091` — attempt `1` — SUCCESS.

Observed live envelope:

- HEAD `1`;
- Range GET `4`;
- source bytes `524288`;
- rows examined `16` (`4/member`);
- deferred unclassifiable rows `16`;
- recognized insurance rows `0`;
- `IN03` `0`.

D-010 continuation is proven live, but insurance discovery was not observed in that deliberately tiny deterministic sample. California source activation therefore remains held, not rejected.

## Same-Bytes Deeper Discovery

Implemented offline:

`scripts/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

The new validator keeps the future source-response envelope unchanged:

- `1` HEAD max;
- `4` Range GET max;
- `131072` bytes per Range;
- `524288` source body bytes total;
- no additional Range;
- no full-body fallback.

It increases only complete logical-row depth:

- max `256 rows/member`;
- max `1024 rows total`;
- up to `64x` the previous logical depth.

Existing transient caps remain unchanged:

- `262144` uncompressed bytes/member;
- `1048576` uncompressed bytes total;
- `32768` bytes/logical record.

D-010 privacy/semantic boundaries remain unchanged: metadata-only defer, no normalization/repair/regex relaxation, no source-value or row/PII persistence.

Offline CI:

`35244998206` — SUCCESS.

Synthetic tests verify discovery of `IN03` after the historical four-row boundary, recognition of `IN01`/`IN99`, hard exclusion of row `257`, unchanged source-byte budget, and fail-closed transport drift.

No California source request occurred during implementation/testing.

## Source State

- transport/archive baseline: CONFIRMED LIVE;
- authority semantics: RESOLVED;
- D-010 continuation: VALIDATED LIVE;
- same-byte deeper discovery validator: OFFLINE READY;
- California source approval: HELD;
- approved real sources: `0`;
- real candidates: `0`.

## Next Product Work

Execute exclusively:

`HUMAN_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_LIVE_VALIDATION_AUTHORIZATION`

Classification: `A — Product Critical`.

Fresh approval must cover exactly one deeper live execution plus transient-row privacy up to `256/member`, `1024 total`, while preserving the existing `524288` source-byte envelope.

After approval:

`one same-byte deeper live validation -> evidence/source decision -> if insurance observed, bounded CA source activation -> candidate -> economics -> reviewer`

Do not repeat the same 16-row run and do not reopen generic transport/CSV/PROPERTY_TYPE diagnostics.
