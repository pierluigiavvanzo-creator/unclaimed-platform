# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Unified Working Branch

`m3-unified-mvp1`

This branch unifies:

1. the latest verified technical state from `m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal-review`;
2. the product-priority strategy from `PRODUCT_STRATEGY_MVP1.md`;
3. D-009, which makes `MVP-1 — First Economically Actionable Case` the priority product objective.

Technical base HEAD:

`b8f703db18207661cd799b0baf1f0dac1bfdc398`

Technical base CI:

`35187432747` — **SUCCESS**

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Minimum target vertical slice:

`APPROVED REAL SOURCE`

`-> bounded acquisition`

`-> normalization`

`-> insurance classification`

`-> candidate case creation`

`-> provenance / evidence package`

`-> case economics`

`-> reviewer console`

`-> human continue / stop decision`

M3 California source work is retained only as the minimum critical-path enabler needed to reach one lawful approved real source. Once one approved real source exists, priority shifts immediately to the MVP-1 vertical slice and commercial measurement rather than further infrastructure expansion.

## Latest Completed Technical Action

Completed:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

Review result:

`PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW.md`

Reviewed proposal artifacts:

- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`;
- `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`;
- `schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`;
- `tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`.

The review performed no California SCO request, HEAD, Range GET, authority retrieval, source-body access, workflow creation, approval grant, retry, baseline adoption or runtime mutation.

## Accepted Bounded Revalidation Design

Accepted for a later separately authorized gate:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

The design requires:

1. one exact-endpoint HTTPS HEAD observation;
2. bounded Range read of archive tail to locate classic ZIP EOCD;
3. bounded central-directory metadata read only if needed and still within caps;
4. derive canonical `relative offset of local header` values from central-directory metadata only;
5. same-object ETag / `If-Match` consistency;
6. `Content-Range` total consistency with HEAD-observed length;
7. unique presence of all four canonical members;
8. candidate offsets within observed archive length;
9. persistence only of bounded derived transport/layout evidence;
10. human evidence review before any runner constant change.

Rejected paths:

- HEAD-only baseline refresh;
- arithmetic rebasing of historical offsets;
- full archive download and inspection.

## Hard Caps

No widening is accepted:

- HEAD max `1`;
- Range max `4`;
- HTTP total max `5`;
- response bytes/range max `131072`;
- source response-body bytes total max `524288`;
- full-body fallback `false`;
- automatic widening `false`;
- automatic retry `false`.

Fail closed on:

- request/byte cap exhaustion;
- missing or ambiguous classic EOCD;
- ZIP64;
- multi-disk ZIP;
- ETag/content-length object drift;
- missing/duplicate canonical member;
- any layout ambiguity or inability to finish within the approved caps.

## Baseline State

Endpoint:

`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Historical pinned transport:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- Accept-Ranges `bytes`.

Historical canonical local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` -> `0`;
2. `From_500_To_Beyond_2_of_4.csv` -> `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` -> `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` -> `134174190`.

These historical values remain stale for future execution planning but are not proven invalid.

One-shot observed drift evidence remains evidence only:

- HTTP `200`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Candidate replacement baseline remains unresolved:

- content length = `null`;
- ETag = `null`;
- all four canonical member offsets = `null`.

No baseline value has been adopted.

## Authorization / Privacy State

Consumed v1.2 execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed v1.2 transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They must not be reused.

The accepted bounded structural design requires fresh single-use:

- structural revalidation execution approval;
- structural-byte privacy approval.

Neither is currently granted.

Accepted privacy boundary:

- structural bytes memory-only;
- retention `0` days;
- raw Range bytes not persisted;
- compressed payload not decompressed or interpreted;
- CSV not parsed;
- no row or protected field observed;
- no `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder or other record value observed;
- noncanonical member names not persisted;
- only bounded derived transport/layout evidence may persist.

## Runtime / Governance State

D-008 remains binding:

- policy: `WHOLE_SOURCE_STOP`;
- implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- runtime contract: `1.2.0`;
- validation: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

No change to:

- `scripts/ca_sco_property_type_semantic_verification.py`;
- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- canonical member offsets;
- parser/projector;
- regex;
- trimming/casing/normalization.

D-009 is now binding for prioritization and product progress.

Current source/product state:

- approved real sources: `0`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- semantic compatibility: unresolved;
- production classification: inactive;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

## MVP-1 Commercial Measurements To Establish

Once a real vertical slice is lawfully available, capture where available:

- records examined;
- records surviving insurance classification;
- candidate cases produced;
- candidate-to-review conversion;
- human review time per candidate;
- automated processing cost per candidate;
- source/data cost per candidate;
- supportable recoverable-value or value-band evidence;
- legally supportable fee/revenue basis;
- principal failure/drop-off reasons;
- false-positive or unresolved-case signals;
- additional manual research burden before commercial action.

These are measurement requirements, not predeclared success thresholds.

## Canonical Read Order Before Any New Change

Read in exact order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW.md`
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`
3. `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`
4. `schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`
5. `tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`
6. `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`
7. `scripts/ca_sco_property_type_semantic_verification.py`
8. prior authorization artifacts/patterns as needed.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

Classification:

`A/B — MVP-1 critical-path enabler`

This next task is repository-only and must remain separate from execution.

It may decide whether to grant fresh single-use:

- structural revalidation execution approval;
- structural-byte privacy approval.

Any granted authorization must be pinned to the exact accepted proposal/review checkpoint, exact endpoint, exact request/byte caps, classic-ZIP-only structural scope, zero-retention privacy boundary, fail-closed conditions and one-shot/no-retry semantics.

It must not:

- perform a California SCO or other external request;
- perform HEAD or Range GET;
- reuse consumed approval refs;
- execute structural revalidation;
- adopt content length, ETag or member offsets;
- update runner constants;
- implement or trigger a network workflow;
- modify parser/projector/regex/normalization;
- activate source policy, registry, production classification or downstream work.

If authorization is granted, the actual bounded structural revalidation must remain a later separate `SINGLE NEXT ACTION` and consume the fresh refs on first network invocation.

## Restart Instruction

1. verify remote HEAD of `m3-unified-mvp1`;
2. verify latest CI for that exact HEAD;
3. read the six canonical files in exact order;
4. read the review audit and accepted proposal artifacts;
5. execute only `HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`;
6. perform no external request during authorization.
