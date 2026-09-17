# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | STRUCTURAL REVALIDATION AUTHORIZATION PASS; ONE-SHOT EXECUTION NEXT | fresh bounded execution + structural-byte privacy approvals granted; no network execution yet |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source:

`PRODUCT_STRATEGY_MVP1.md`

Governing decision:

`D-009 — MVP-1 commercial validation becomes the product-priority objective`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler required to reach one lawful approved real source. Additional diagnostics, infrastructure or governance work that does not materially shorten this path is not the current priority.

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- runner output contract remains `1.2.0`;
- v1.2 one-shot execution performed exactly once;
- one-shot result: `STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`;
- no source body or CSV row was read in that stopped execution;
- prior v1.2 execution/privacy approvals are consumed and non-reusable;
- transport + archive-layout baseline-refresh proposal was human-reviewed and accepted as design;
- accepted structural strategy: `BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`;
- fresh single-use structural revalidation execution and structural-byte privacy approvals are now granted;
- structural revalidation itself has not been performed;
- candidate replacement baseline remains unresolved;
- semantic compatibility remains unresolved.

## Structural Revalidation Authorization

Completed:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

Authorization base:

- branch: `m3-unified-mvp1`;
- HEAD: `3d4d8a76e47d88eca77ca6d899b85341ba8beaf2`;
- CI: `35195330933` — **SUCCESS**.

Accepted technical review:

- HEAD: `b8f703db18207661cd799b0baf1f0dac1bfdc398`;
- CI: `35187432747` — **SUCCESS**.

Reviewed proposal:

- HEAD: `359b1c1a86d34edabcd028e5e5fbb6fc3acba781`;
- CI: `35139290645` — **SUCCESS**.

Authorization result:

`PASS_FRESH_SINGLE_USE_STRUCTURAL_REVALIDATION_EXECUTION_AND_STRUCTURAL_BYTE_PRIVACY_APPROVALS_GRANTED_EXECUTION_NOT_PERFORMED`

Fresh execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Fresh structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Both are `GRANTED_NOT_CONSUMED`, single-use and non-reusable. They are consumed together on the first authorized California SCO network request of the later execution. No automatic retry is authorized.

## Preserved Request / Byte Caps

- HEAD requests max: `1`;
- Range requests max: `4`;
- HTTP requests max total: `5`;
- Range response max each: `131072` bytes;
- source response-body max total: `524288` bytes;
- full-body fallback: `false`;
- automatic widening: `false`;
- automatic retry: `false`.

Classic ZIP only. ZIP64, multi-disk, missing/ambiguous EOCD, identity drift, missing/duplicate canonical members or inability to complete inside these caps must stop fail-closed.

## Privacy / Persistence Boundary

Structural Range bytes are authorized only for the later one-shot execution and must remain:

- memory-only;
- retention `0` days;
- immediately disposed;
- not persisted raw;
- not decompressed as payload;
- not parsed as CSV;
- not inspected as rows or protected fields.

Only bounded derived transport/archive-layout candidate evidence may persist. Noncanonical member names may not persist.

## Baseline / Adoption Boundary

No content length, ETag or member offset has been adopted by the authorization gate.

A successful later structural execution may create only candidate evidence and must stop at a separate human evidence-review gate before any runner constant update.

## MVP-1 Commercial Baseline To Establish

Once one lawful approved real source is available, immediately capture where available:

- records examined;
- records surviving insurance classification;
- candidate cases produced;
- candidate-to-review conversion;
- human review time per candidate;
- automated processing cost per candidate;
- data/source cost per candidate;
- supportable recoverable-value or value-band evidence;
- legally supportable fee/revenue basis;
- principal failure/drop-off reasons;
- false-positive or unresolved-case signals;
- additional manual research burden before commercial action.

These are measurement requirements, not invented success thresholds.

## Next Product Work

Execute exclusively:

`EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`

Classification:

`A/B — MVP-1 critical-path enabler`

That action must be separate from authorization, use exactly the two fresh approval refs, remain bounded to the accepted classic-ZIP structural design, consume the approvals on the first source request, perform no retry/widening, persist only approved derived candidate evidence, and stop at a separate human candidate-evidence review.

After one approved real source exists, priority shifts immediately to the MVP-1 vertical slice rather than further infrastructure expansion.
