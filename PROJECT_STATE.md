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

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Working Checkpoint

Execution branch:

`m3-ca-sco-transport-archive-layout-revalidation-once`

Authorization checkpoint:

`4079fb44b36699e9b05821761c222d063a89648d`

Implementation preflight checkpoint:

`e87e7d20d766ad06ca0feb8805ac00c4a6ed547c`

Execution trigger checkpoint:

`de4c20e0a4158da0497d2ca9c2090589636b40e0`

Completed action:

`EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`

Execution workflow run:

`35198720002` — **SUCCESS** — attempt `1`

Execution job:

`105128028851` — **SUCCESS**

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EXECUTION.md`

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`

## Structural Revalidation Result

`REVALIDATION_RESULT_STATUS = CANDIDATE_BASELINE_ESTABLISHED`

`STOP_REASON = null`

Observed candidate transport:

- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`;
- observed at: `2026-09-17T08:15:58.436797Z`.

Canonical member status:

`ALL_CANONICAL_MEMBERS_UNIQUE`

Additional member count:

`0`

Candidate canonical local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` -> `0`;
2. `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
3. `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
4. `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

These candidate values were derived from current classic-ZIP Central Directory metadata. They are evidence only and are **not adopted** as runtime/source baseline values.

## Historical Baseline / Adoption State

Historical semantic-runner pins remain unchanged pending separate human evidence review and any later implementation gate:

- `EXPECTED_LENGTH = 162416884`;
- `EXPECTED_ETAG = "b25b315b6cd8007624387c3a00d4b1fe"` including quote characters in the actual ETag;
- offsets: `0`, `59747797`, `96862896`, `134174190`.

Candidate replacement baseline established: `true`.

Candidate baseline adopted: `false`.

## Authorization / Privacy State

Structural revalidation execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They were consumed together on the first California SCO network request of workflow run `35198720002`. No retry is authorized or performed.

Historical v1.2 execution/privacy approvals also remain `CONSUMED_SINGLE_USE_NON_REUSABLE`.

## Structural / Privacy Boundary

Execution remained governed by the accepted design:

`HEAD -> ZIP tail -> classic EOCD -> bounded Central Directory -> canonical local-header offsets`

Hard caps remained:

- HEAD max `1`;
- Range max `4`;
- HTTP total max `5`;
- Range response max `131072` bytes;
- source response-body max total `524288` bytes;
- full-body fallback `false`;
- widening `false`;
- retry `false`.

Privacy boundary remained:

- structural bytes memory-only;
- retention `0` days;
- raw Range bytes not persisted;
- compressed payload not decompressed;
- CSV not parsed;
- no row/protected field inspected;
- noncanonical member names not persisted;
- only approved derived transport/archive-layout evidence persisted.

The approved evidence schema does not persist exact request counters, so no unsupported exact count is asserted beyond the enforced caps.

## Runtime / D-008 State

Unchanged:

- semantic runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- trimming/casing/normalization;
- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- historical semantic-runner member offsets;
- D-008 `WHOLE_SOURCE_STOP` handling.

## Product / Commercial State

- approved real sources: `0`;
- candidate transport/archive-layout baseline established: `true`;
- candidate baseline adopted: `false`;
- semantic compatibility resolved: `false`;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

The structural execution removed a material transport/layout uncertainty but did not itself approve the California source.

## Next Recommended Action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`

Classification:

`A/B — MVP-1 critical-path enabler`

The review must decide whether the persisted candidate evidence is sufficient for a later separate baseline-adoption implementation gate. It must perform no source retry and must not mutate semantic-runner constants in the review itself.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
