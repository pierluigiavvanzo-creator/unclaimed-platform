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

## Current Working Checkpoint

Authorization work branch:

`m3-ca-sco-transport-archive-layout-revalidation-authorization`

Authorization base branch:

`m3-unified-mvp1`

Authorization base HEAD:

`3d4d8a76e47d88eca77ca6d899b85341ba8beaf2`

Authorization base CI:

`35195330933` — **SUCCESS**

Completed action:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

Authorization result:

`PASS_FRESH_SINGLE_USE_STRUCTURAL_REVALIDATION_EXECUTION_AND_STRUCTURAL_BYTE_PRIVACY_APPROVALS_GRANTED_EXECUTION_NOT_PERFORMED`

Authorization audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION.md`

Machine authorization:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation_approval.v1.json`

## Accepted Bounded Design

Accepted design remains:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

Reviewed proposal HEAD:

`359b1c1a86d34edabcd028e5e5fbb6fc3acba781`

Accepted review HEAD:

`b8f703db18207661cd799b0baf1f0dac1bfdc398`

The later separately authorized execution remains limited to:

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

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Fresh structural revalidation execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Fresh structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Both fresh approvals are:

- `GRANTED_NOT_CONSUMED`;
- single-use;
- reusable: `false`;
- consumed together on the first authorized California SCO network request of the later execution;
- invalid for automatic retry or any broader source/runtime scope.

Accepted privacy boundary remains:

- structural bytes memory-only;
- retention `0` days;
- raw Range bytes not persisted;
- compressed payload not decompressed or interpreted;
- CSV not parsed;
- no row or protected field observed;
- noncanonical member names not persisted;
- only the reviewed bounded derived transport/layout evidence may persist.

## Authorization Gate Actual Effects

This authorization task is repository-only.

Actual network/source usage by this gate:

- California SCO requests: `0`;
- HEAD requests: `0`;
- Range GET requests: `0`;
- source-body bytes read: `0`;
- CSV records read: `0`;
- structural revalidation performed: `false`;
- candidate baseline established: `false`;
- candidate baseline adopted: `false`.

No fresh approval has been consumed.

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

The fresh one-shot authorization removes the authorization blocker for structural revalidation but does not itself resolve transport/archive layout or approve a real source.

## Source / Product Governance State

- D-008 accepted as design: `true`;
- D-009 MVP-1 priority accepted: `true`;
- baseline-refresh proposal human-reviewed and accepted: `true`;
- bounded structural revalidation authorized for one future execution: `true`;
- fresh execution approval granted: `true`;
- fresh structural-byte privacy approval granted: `true`;
- workflow creation for the later one-shot execution authorized: `true`;
- approvals consumed: `false`;
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

`EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`

Classification:

`A/B — MVP-1 critical-path enabler`

This must be a separate action. It must use exactly the two fresh approval refs, stay inside the accepted classic-ZIP structural and privacy boundaries, consume both approvals on the first California SCO network request, perform no retry or widening, and stop at a separate human candidate-evidence review before any baseline adoption or runner mutation.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
