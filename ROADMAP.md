# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | CANDIDATE BASELINE EVIDENCE HUMAN-REVIEWED PASS; ADOPTION IMPLEMENTATION NEXT | bounded classic-ZIP revalidation succeeded; evidence accepted; runtime pins not yet changed |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — BLOCKED ON FIRST APPROVED REAL SOURCE | real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 remains only the minimum critical-path enabler required to reach one lawful approved real source. Additional diagnostics, governance or infrastructure that do not shorten that path are deprioritized.

## Verified M3 State

- D-008 `WHOLE_SOURCE_STOP` remains unchanged;
- semantic runner contract remains `1.2.0`;
- one-shot structural revalidation run `35198720002` completed **SUCCESS** on attempt `1`;
- candidate transport/archive-layout baseline was established from bounded classic-ZIP metadata;
- both structural execution/privacy approvals are consumed and non-reusable;
- persisted candidate evidence passed schema/contract validation;
- human evidence review accepted the candidate evidence as sufficient for a later separate repository-only adoption implementation;
- no candidate value is yet adopted;
- semantic compatibility remains unresolved.

## Reviewed Candidate Baseline

Candidate transport:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- media type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Canonical members:

- all four present exactly once;
- additional member count `0`;
- offsets `0`, `59745428`, `96861315`, `134172553`.

Human review result:

`PASS_CANDIDATE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_EVIDENCE_ACCEPTED_FOR_SEPARATE_ADOPTION_IMPLEMENTATION`

## Adoption Boundary

Current semantic-runner pins remain historical:

- length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- offsets `0`, `59747797`, `96862896`, `134174190`.

Candidate baseline adopted: `false`.

The next repository-only implementation may update only those reviewed transport/layout pins. Parser/projector/regex/normalization and D-008 remain unchanged.

## Approval State

The two structural revalidation approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

The pre-execution authorization artifact is historical provenance only and must not be treated as fresh authority. No network retry is authorized.

## MVP-1 Commercial Baseline To Establish

Once one lawful approved real source exists, immediately measure where available:

- records examined;
- records surviving insurance classification;
- candidate cases produced;
- candidate-to-review conversion;
- human review time per candidate;
- automated/source cost per candidate;
- supportable recoverable-value/revenue evidence;
- principal failure/drop-off reasons;
- false-positive or unresolved-case signals;
- additional manual research burden.

No commercial threshold is invented in advance.

## Next Product Work

Execute exclusively:

`IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`

Classification:

`A/B — MVP-1 critical-path enabler`

This action is repository-only. Update the reviewed content length, ETag and four canonical member offsets, add/update regression coverage as needed, run full CI/smoke, and perform no California SCO network request. Do not alter parser/projector/regex/normalization, D-008, source policy, registry or downstream gates.

After the baseline adoption is CI-green, return immediately to the shortest safe path to one approved real source and then the MVP-1 vertical slice.
