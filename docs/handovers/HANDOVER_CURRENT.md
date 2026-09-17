# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-transport-archive-layout-revalidation-authorization`

Authorization base branch:

`m3-unified-mvp1`

Authorization base HEAD:

`3d4d8a76e47d88eca77ca6d899b85341ba8beaf2`

Authorization base CI:

`35195330933` — **SUCCESS**

The authorization branch was created from that exact unified checkpoint. Re-verify its remote HEAD and CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Target vertical slice:

`APPROVED REAL SOURCE`
`-> bounded acquisition`
`-> normalization`
`-> insurance classification`
`-> candidate case creation`
`-> provenance / evidence package`
`-> case economics`
`-> reviewer console`
`-> human continue / stop decision`

M3 California work is only a critical-path enabler for the first lawful approved real source. Do not expand diagnostics/governance/infrastructure unless it materially shortens that path.

## Latest Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`

Classification:

`A/B — MVP-1 critical-path enabler`

Result:

`PASS_FRESH_SINGLE_USE_STRUCTURAL_REVALIDATION_EXECUTION_AND_STRUCTURAL_BYTE_PRIVACY_APPROVALS_GRANTED_EXECUTION_NOT_PERFORMED`

Authorization audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION.md`

Machine authorization:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation_approval.v1.json`

Authorization schema:

`schemas/common/property_type_transport_archive_layout_revalidation_authorization.schema.json`

Authorization contract test:

`tests/contract/test_ca_sco_property_type_transport_archive_layout_revalidation_authorization.py`

This gate was repository-only. It performed no California SCO request, HEAD, Range GET, source-body read, CSV access, structural revalidation, candidate-baseline establishment/adoption or runtime mutation.

## Accepted Design Checkpoint

Accepted proposal review branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal-review`

Accepted review HEAD:

`b8f703db18207661cd799b0baf1f0dac1bfdc398`

Accepted review CI:

`35187432747` — **SUCCESS**

Reviewed proposal branch:

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`

Reviewed proposal HEAD:

`359b1c1a86d34edabcd028e5e5fbb6fc3acba781`

Reviewed proposal CI:

`35139290645` — **SUCCESS**

Accepted review result:

`PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`

Accepted design:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

## Fresh Authorization State

Fresh structural revalidation execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Fresh structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

State of both:

- `GRANTED_NOT_CONSUMED`;
- fresh: `true`;
- single-use: `true`;
- reusable: `false`;
- consumption trigger: first authorized California SCO network request of the later execution;
- automatic retry: not authorized.

Historical approvals remain consumed and non-reusable:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Do not reuse them.

## Exact Future Execution Boundary

Endpoint:

`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Transport / consistency:

- HTTPS only;
- exact host `claimit.ca.gov`;
- one HEAD observation before Range reads;
- same-object ETag / `If-Match` consistency required;
- `Content-Range` total must match HEAD-observed content length.

Hard caps:

- HEAD max `1`;
- Range max `4`;
- HTTP total max `5`;
- response bytes/range max `131072`;
- source response-body bytes total max `524288`;
- full-body fallback `false`;
- automatic widening `false`;
- automatic retry `false`.

Structural path:

`HEAD -> ZIP tail -> classic EOCD -> bounded Central Directory -> canonical relative local-header offsets`

Canonical members:

1. `From_500_To_Beyond_1_of_4.csv`;
2. `From_500_To_Beyond_2_of_4.csv`;
3. `From_500_To_Beyond_3_of_4.csv`;
4. `From_500_To_Beyond_4_of_4.csv`.

Required structural constraints:

- classic ZIP only;
- ZIP64 unsupported;
- multi-disk unsupported;
- central-directory metadata only;
- no decompression;
- no CSV parsing;
- no row/field inspection;
- no arithmetic rebasing from historical offsets;
- canonical member names unique;
- candidate offsets derived only from central-directory metadata;
- offsets inside observed content length.

Fail closed on request/byte cap exhaustion, EOCD ambiguity/missing, ZIP64, multi-disk, object identity drift, canonical member missing/duplicate, or any layout ambiguity/unresolvable condition.

## Structural-Byte Privacy Boundary

Authorized only for the later one-shot structural execution:

- structural Range bytes memory-only;
- retention `0` days;
- immediate disposal;
- raw Range bytes not persisted;
- compressed payload not parsed/decompressed;
- CSV not parsed;
- no row or protected field inspected;
- no `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder or other record value observed;
- noncanonical member names not persisted.

Only these derived fields may persist:

- `OBSERVED_CONTENT_LENGTH`;
- `OBSERVED_ETAG`;
- `OBSERVED_CONTENT_TYPE`;
- `OBSERVED_ACCEPT_RANGES`;
- `OBSERVED_LAST_MODIFIED`;
- `OBSERVED_AT`;
- `CANONICAL_MEMBER_NAMES`;
- `CANONICAL_MEMBER_LOCAL_HEADER_OFFSETS`;
- `CANONICAL_MEMBER_MATCH_STATUS`;
- `ADDITIONAL_MEMBER_COUNT`;
- `REVALIDATION_RESULT_STATUS`;
- `STOP_REASON`.

## Baseline State

Historical pinned transport remains stale for future planning but not proven invalid:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`.

Historical canonical offsets remain:

1. `0`;
2. `59747797`;
3. `96862896`;
4. `134174190`.

Observed drift evidence remains evidence only:

- HTTP `200`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Candidate replacement baseline remains unresolved:

- content length: `null`;
- ETag: `null`;
- four canonical offsets: all `null`.

No value was adopted by the authorization gate.

## Candidate-Evidence / Adoption Separation

A successful later structural revalidation may persist only a **candidate** baseline under the privacy-safe derived evidence contract.

Required sequence:

1. authorization — now completed;
2. separately executed one-shot bounded structural revalidation;
3. candidate evidence persistence;
4. separate human candidate-evidence review;
5. separate implementation gate before changing `EXPECTED_LENGTH`, `EXPECTED_ETAG` or canonical offsets;
6. CI-green verification of any later runtime change.

The execution task must not combine steps 3-5.

## Runtime / Governance State

Unchanged:

- runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- `EXPECTED_LENGTH = 162416884`;
- `EXPECTED_ETAG = "b25b315b6cd8007624387c3a00d4b1fe"` including quote characters in the actual HTTP ETag value;
- historical canonical offsets unchanged;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector unchanged;
- trimming/casing/normalization unchanged;
- D-008 `WHOLE_SOURCE_STOP` unchanged.

Source/product state:

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

`DECISIONS.md` was not changed by this authorization because no architecture, policy or strategy decision changed.

## Canonical Read Order Before Any New Change

Read in exact order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION.md`;
2. `sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation_approval.v1.json`;
3. `schemas/common/property_type_transport_archive_layout_revalidation_authorization.schema.json`;
4. `tests/contract/test_ca_sco_property_type_transport_archive_layout_revalidation_authorization.py`;
5. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW.md`;
6. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`;
7. `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`;
8. `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`;
9. `scripts/ca_sco_property_type_semantic_verification.py`.

## SINGLE NEXT ACTION

Execute exclusively:

`EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`

Classification:

`A/B — MVP-1 critical-path enabler`

This must remain a separate action from authorization.

It may:

- implement the smallest repository-local verifier/workflow required by the already accepted design;
- CI-validate that bounded implementation before source access;
- perform exactly one authorized structural revalidation using the two fresh refs;
- persist only the approved derived candidate evidence;
- mark both approvals consumed on the first California SCO network request.

It must not:

- exceed the request/byte caps;
- retry or widen;
- perform a full download;
- decompress payload or parse CSV;
- inspect rows/protected fields;
- persist raw Range bytes or noncanonical member names;
- adopt candidate content length, ETag or offsets;
- modify semantic-runner constants in the same action;
- modify parser/projector/regex/normalization;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, matching, outreach or claim submission.

The execution must stop at a new, separate human candidate-evidence review before any baseline adoption.

## Restart Instruction

1. verify remote HEAD of the current working branch;
2. verify latest CI for that exact HEAD;
3. read the six canonical files in exact order;
4. verify the fresh authorization artifact and both approval refs remain `GRANTED_NOT_CONSUMED`;
5. execute only `EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`;
6. consume both approvals on the first source request and do not retry.
