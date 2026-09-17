# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California work remains active only as the minimum critical-path enabler required to reach one lawful approved real source.

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Working Checkpoint

Current branch:

`m3-ca-sco-transport-archive-layout-revalidation-once`

Reviewed base HEAD:

`ac7ced81299d5a563e4c4beeb74858ba28e2b50a`

Reviewed base CI:

`35199132893` — **SUCCESS**

Completed action:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`

Review result:

`PASS_CANDIDATE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_EVIDENCE_ACCEPTED_FOR_SEPARATE_ADOPTION_IMPLEMENTATION`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW.md`

## Accepted Candidate Baseline Evidence

The successful one-shot structural revalidation remains the evidence source:

- workflow run `35198720002` — **SUCCESS**, attempt `1`;
- evidence status `CANDIDATE_BASELINE_ESTABLISHED`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`;
- canonical member status `ALL_CANONICAL_MEMBERS_UNIQUE`;
- additional member count `0`;
- candidate offsets `0`, `59745428`, `96861315`, `134172553`.

The evidence is accepted as sufficient for a separate repository-only baseline-adoption implementation.

## Adoption State

Candidate replacement baseline established: `true`.

Human evidence review accepted: `true`.

Candidate baseline adopted: `false`.

The semantic runner still contains the historical values:

- `EXPECTED_LENGTH = 162416884`;
- `EXPECTED_ETAG = "b25b315b6cd8007624387c3a00d4b1fe"`;
- offsets `0`, `59747797`, `96862896`, `134174190`.

No candidate value was changed by the evidence review.

## Authorization / Privacy State

Structural revalidation execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Current state of both:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

The historical authorization artifact retains its pre-execution `GRANTED_NOT_CONSUMED` snapshot for provenance only and is not reusable authority.

No replacement network/privacy approval was granted by the evidence review.

## Runtime / D-008 State

Unchanged:

- semantic runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- parser/projector;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP` behavior;
- source policy and registry state.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout evidence accepted for adoption implementation: `true`;
- candidate baseline adopted: `false`;
- semantic compatibility resolved: `false`;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`.

The next useful product move is to adopt the reviewed transport/layout pins in the runner, verify repository integrity, and then return to the shortest safe path toward one approved real source.

## Next Recommended Action

Execute exclusively:

`IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`

Classification:

`A/B — MVP-1 critical-path enabler`

This action is repository-only. It may update only the reviewed content length, ETag and four canonical offsets, with regression tests and full CI. It must perform no California SCO request and must not change parser/projector/regex/normalization, D-008, source policy, registry or downstream gates.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
