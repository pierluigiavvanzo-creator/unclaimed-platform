# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

California SCO `PROPERTY_TYPE` handling remains governed by `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`, accepted policy `WHOLE_SOURCE_STOP`, implementation strategy `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`, and runner output contract `1.2.0`.

The v1.2 one-shot real-source execution stopped fail-closed on transport metadata drift before body access. Its evidence was human-reviewed and accepted. The subsequent repository-only transport + archive-layout baseline refresh proposal has now also been human-reviewed and accepted as a bounded design.

## Current Review Checkpoint

Review branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal-review`

Reviewed proposal branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`

Reviewed proposal HEAD:

`359b1c1a86d34edabcd028e5e5fbb6fc3acba781`

Reviewed proposal CI:

`35139290645` — **SUCCESS**

Completed action:

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

1. `From_500_To_Beyond_1_of_4.csv` → `0`;
2. `From_500_To_Beyond_2_of_4.csv` → `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` → `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` → `134174190`.

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

`DECISIONS.md` remains unchanged because this review accepts a bounded operational verification design under existing deterministic/fail-closed governance and introduces no new architecture or runtime semantics.

## Source / Product Governance State

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

This next gate is repository-only. It may decide whether to grant fresh single-use execution and structural-byte privacy approvals for the accepted bounded revalidation design.

It must perform no source/network request and must remain separate from execution itself.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
