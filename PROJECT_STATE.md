# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source:

`PRODUCT_STRATEGY_MVP1.md`

Governing decision:

`D-009 — MVP-1 commercial validation becomes the product-priority objective`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California source work remains active only as the minimum critical-path enabler required to reach one lawful approved real source.

## MVP-1 Target Vertical Slice

`APPROVED REAL SOURCE`

`-> bounded acquisition`

`-> normalization`

`-> insurance classification`

`-> candidate case creation`

`-> provenance / evidence package`

`-> case economics`

`-> reviewer console`

`-> human continue / stop decision`

No commercial success threshold is invented in advance. Real execution must establish the commercial baseline.

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Unified Checkpoint

Current unified branch:

`m3-unified-mvp1`

Technical base branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal-review`

Technical base HEAD:

`b8f703db18207661cd799b0baf1f0dac1bfdc398`

Technical base CI:

`35187432747` — **SUCCESS**

Completed technical action:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

Review result:

`PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW.md`

## Accepted Bounded Design

Accepted for a later separately authorized gate:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

The accepted future design is limited to:

1. one exact-endpoint HEAD observation for transport identity;
2. bounded classic-ZIP tail/EOCD/central-directory Range reads;
3. candidate extraction of the four canonical member local-header offsets from central-directory metadata;
4. persistence only of bounded derived transport/layout evidence;
5. human candidate-evidence review before any baseline adoption.

Rejected paths remain:

- HEAD-only baseline refresh;
- arithmetic offset rebasing;
- full archive download and inspection.

## Preserved Caps

- HEAD max: `1`;
- Range max: `4`;
- HTTP total max: `5`;
- Range response max each: `131072` bytes;
- source response-body bytes max total: `524288`;
- full-body fallback: `false`;
- automatic widening: `false`;
- automatic retry: `false`.

ZIP64, multi-disk ZIP, ambiguous/missing EOCD, missing/duplicate canonical members, identity drift or inability to resolve the layout within these caps must stop fail-closed.

## Baseline State

Historical transport pins remain stale for future execution planning but not proven invalid:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`.

Historical canonical local-header offsets remain:

1. `From_500_To_Beyond_1_of_4.csv` -> `0`;
2. `From_500_To_Beyond_2_of_4.csv` -> `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` -> `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` -> `134174190`.

One-shot observed drift evidence remains evidence only:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- HTTP `200`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

No observed value has been adopted as a replacement baseline.

Candidate replacement baseline remains unresolved:

- candidate content length: `null`;
- candidate ETag: `null`;
- all four candidate member offsets: `null`.

## Authorization / Privacy State

Consumed v1.2 execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain `CONSUMED_SINGLE_USE_NON_REUSABLE`.

The accepted bounded structural design requires fresh single-use:

- execution approval;
- structural-byte privacy approval.

Neither is currently granted.

Accepted privacy boundary remains:

- structural bytes memory-only;
- retention `0` days;
- raw Range bytes not persisted;
- compressed payload not decompressed or interpreted;
- CSV not parsed;
- no row or protected field observed;
- noncanonical member names not persisted.

## Runtime / D-008 State

Unchanged:

- runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- trimming/casing/normalization;
- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- canonical member offsets;
- D-008 `WHOLE_SOURCE_STOP` handling.

## Product / Commercial Interpretation

Current facts:

- approved real sources: `0`;
- semantic compatibility resolved: `false`;
- production classification active: `false`;
- real candidate cases through MVP-1: `0`;
- commercial baseline from real cases: not yet established.

Therefore additional M3 diagnostic or governance work is justified only when it materially shortens the safe path to one approved real source. Once one approved real source exists, priority shifts immediately to the MVP-1 vertical slice and commercial measurements.

## Source / Product Governance State

- D-008 accepted as design: `true`;
- D-009 MVP-1 priority accepted: `true`;
- baseline-refresh proposal prepared: `true`;
- proposal human-reviewed: `true`;
- proposal accepted as design: `true`;
- network revalidation authorized: `false`;
- fresh execution approval granted: `false`;
- fresh structural-byte privacy approval granted: `false`;
- workflow creation authorized: `false`;
- retry authorized: `false`;
- current historical baseline suitable for blind reuse: `false`;
- candidate replacement baseline established: `false`;
- candidate baseline adopted: `false`;
- source continuation authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

Classification:

`A/B — MVP-1 critical-path enabler`

This next gate is repository-only. It may decide whether to grant fresh single-use execution and structural-byte privacy approvals for the accepted bounded revalidation design.

It must perform no source/network request and must remain separate from execution itself.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
