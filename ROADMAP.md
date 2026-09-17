# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | STRUCTURAL REVALIDATION ONE-SHOT SUCCESS; CANDIDATE EVIDENCE REVIEW NEXT | candidate transport/archive layout established from bounded classic-ZIP metadata; no adoption yet |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source:

`PRODUCT_STRATEGY_MVP1.md`

Governing decision:

`D-009 — MVP-1 commercial validation becomes the product-priority objective`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler required to reach one lawful approved real source.

## Verified M3 State

- D-008 `WHOLE_SOURCE_STOP` remains unchanged;
- semantic runner contract remains `1.2.0`;
- prior v1.2 one-shot stopped fail-closed on `TRANSPORT_METADATA_DRIFT` before Range/CSV access;
- bounded transport/archive-layout refresh design was human-reviewed and accepted;
- fresh single-use structural execution/privacy approvals were granted;
- implementation preflight was CI-green with source execution skipped;
- bounded structural revalidation was then executed exactly once;
- live run `35198720002` attempt `1` completed **SUCCESS**;
- both fresh approvals are now consumed and non-reusable;
- candidate transport/archive-layout evidence is established;
- no candidate value has been adopted;
- semantic compatibility remains unresolved.

## Candidate Transport / Archive-Layout Evidence

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`

Result:

`CANDIDATE_BASELINE_ESTABLISHED`

Candidate transport:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- media type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Canonical members:

- all four present exactly once;
- additional member count `0`.

Candidate local-header offsets:

1. `0`;
2. `59745428`;
3. `96861315`;
4. `134172553`.

These values are candidate evidence only.

## Baseline / Adoption Boundary

Current semantic-runner constants remain historical and unchanged:

- length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- offsets `0`, `59747797`, `96862896`, `134174190`.

Candidate replacement baseline established: `true`.

Candidate baseline adopted: `false`.

A separate human evidence review is required before any later implementation gate may update runtime pins.

## Request / Privacy Boundary Preserved

The one-shot verifier enforced:

- HEAD max `1`;
- Range max `4`;
- HTTP total max `5`;
- response bytes/range max `131072`;
- source response-body max total `524288`;
- full-body fallback `false`;
- widening `false`;
- retry `false`.

Structural bytes remained memory-only with zero retention. No raw Range bytes, decompressed payload, CSV rows, protected fields or noncanonical member names were persisted.

## Approval State

The two structural revalidation approvals are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No rerun is authorized.

## MVP-1 Commercial Baseline To Establish

Once one lawful approved real source exists, immediately capture where available:

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

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`

Classification:

`A/B — MVP-1 critical-path enabler`

The review must remain repository-only, perform no source retry, and determine whether the candidate evidence supports a later separate baseline-adoption implementation gate. It must not modify semantic-runner constants in the review itself.

After one approved real source exists, priority shifts immediately to the MVP-1 vertical slice rather than further infrastructure expansion.
