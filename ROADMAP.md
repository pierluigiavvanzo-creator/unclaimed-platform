# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | TRANSPORT + ARCHIVE-LAYOUT REFRESH PROPOSAL REVIEW PASS; FRESH AUTHORIZATION NEXT | bounded classic-ZIP structural design accepted; network revalidation still not authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source:

`PRODUCT_STRATEGY_MVP1.md`

Governing decision:

`D-009 — MVP-1 commercial validation becomes the product-priority objective`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 is retained only as the minimum critical-path enabler required to reach one lawful approved real source. Additional diagnostics, infrastructure or governance work that does not materially shorten this path is not the current priority.

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- runner output contract remains `1.2.0`;
- v1.2 one-shot execution performed exactly once;
- one-shot result: `STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`;
- one-shot evidence human-reviewed and accepted;
- consumed execution/privacy approvals remain non-reusable;
- no retry authorized;
- no source body or row was read during the stopped one-shot;
- semantic compatibility remains unresolved.

## Transport + Archive-Layout Proposal Review

Completed:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

Technical review branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal-review`

Technical review HEAD:

`b8f703db18207661cd799b0baf1f0dac1bfdc398`

Technical review CI:

`35187432747` — **SUCCESS**

Review result:

`PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`

Accepted design:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

The design permits only:

1. one exact-endpoint HEAD observation;
2. bounded classic-ZIP tail/EOCD/central-directory metadata Range reads;
3. candidate derivation of canonical local-header offsets from central-directory metadata;
4. privacy-safe derived evidence persistence;
5. human evidence review before any baseline adoption.

Rejected:

- HEAD-only transport refresh;
- arithmetic member-offset rebasing;
- full archive download and inspection.

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

## Authorization / Privacy Boundary

Any later bounded structural revalidation requires fresh single-use:

- execution approval;
- structural-byte privacy approval.

Structural Range bytes must be memory-only with zero retention. No raw byte persistence, decompression, CSV parsing, row inspection or protected-field observation is allowed.

## MVP-1 Commercial Baseline To Establish

Once one lawful approved real source is available, immediately capture from the vertical slice where available:

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

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

Classification:

`A/B — MVP-1 critical-path enabler`

That gate is repository-only and may decide whether to grant fresh single-use execution and structural-byte privacy approvals. It must remain separate from the network execution itself.

After one approved real source exists, priority shifts immediately to the MVP-1 vertical slice rather than further infrastructure expansion.
