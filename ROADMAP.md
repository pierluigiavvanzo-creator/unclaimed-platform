# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | LIVE TRANSPORT CONFIRMED; SEMANTIC EXECUTION STOPPED FAIL-CLOSED; EVIDENCE REVIEW NEXT | one authorized bounded run reached `PROPERTY_TYPE_FORMAT_UNEXPECTED`; D-008 applied correctly |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler to one approved real source. No further transport diagnostics are justified by the latest execution.

## Verified M3 State

- D-008 `WHOLE_SOURCE_STOP` unchanged and now exercised on live source data;
- runtime contract `1.2.0` unchanged;
- proposal `1.1.0` remains the frozen reviewed boundary;
- adopted transport baseline was confirmed live: length `162560390`, ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- one-shot real execution run `35227857742` completed **SUCCESS**, attempt `1`;
- actual request use: 1 HEAD + 1 Range, 2 HTTP total, 131072 body bytes;
- result: `STOPPED_FAIL_CLOSED / PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- control disposition: `PROPERTY_TYPE_NONCONFORMING_STOPPED / PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- temporary workflow and trigger removed;
- fresh execution/privacy refs consumed and non-reusable;
- privacy/safety boundary preserved;
- semantic compatibility remains unresolved positively;
- approved real sources remain `0`.

## Active Product Blocker

The current blocker is no longer transport/archive layout.

It is compatibility between live `PROPERTY_TYPE` source content and the unchanged strict validation boundary:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The execution intentionally persisted no source value, row, hash or exact value length. Therefore no source semantics should be invented from the stop alone.

## Next Product Work

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

Classification:

`A — Product Critical`

The evidence review should choose the shortest safe commercial path:

- if authoritative source semantics can resolve compatibility without unsupported inference, define the smallest separately reviewed remediation;
- otherwise reject/defer this source for MVP-1 and move to another lawful source.

Do not retry the consumed execution, widen regex/parser/normalization, or reopen transport work without new evidence.

After the first real source is approved, immediately switch priority to the MVP-1 vertical slice and commercial measurements.