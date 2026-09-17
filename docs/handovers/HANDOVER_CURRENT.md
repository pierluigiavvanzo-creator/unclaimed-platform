# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal-review`

Created from reviewed proposal checkpoint:

`359b1c1a86d34edabcd028e5e5fbb6fc3acba781`

Reviewed proposal CI:

`35139290645` — **SUCCESS**

## Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

Review result:

`PASS_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_ACCEPTED_AS_DESIGN_FRESH_AUTHORIZATION_REQUIRED_REVALIDATION_NOT_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW.md`

The review is repository-only. It performed no California SCO request, HEAD, Range GET, authority retrieval, source-body access, workflow creation, approval grant, retry, baseline adoption or runtime mutation.

## Reviewed Proposal

Proposal audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`

Machine proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`

Schema:

`schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`

Proposal status remains:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

## Governing Evidence

Previously accepted v1.2 one-shot result remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`;
- HEAD requests = `1`;
- Range requests = `0`;
- HTTP requests total = `1`;
- source body bytes read = `0`;
- rows examined = `0`.

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Human evidence review:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`

## Baseline State

Endpoint:

`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Historical pinned transport:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- Accept-Ranges `bytes`.

Historical canonical local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` → `0`;
2. `From_500_To_Beyond_2_of_4.csv` → `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` → `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` → `134174190`.

These historical values remain `STALE_FOR_FUTURE_EXECUTION_PLANNING_NOT_PROVEN_INVALID`.

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

No larger implicit read is permitted.

## Structural Privacy Boundary

A later structural execution may encounter opaque compressed bytes adjacent to ZIP metadata. Therefore it requires a fresh single-use structural-byte privacy approval as well as a fresh single-use execution approval.

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

## Consumed Approval State

Consumed v1.2 execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed v1.2 transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They must not be reused.

Fresh structural-revalidation approval refs are currently absent / ungranted.

## Runtime / D-008 State

Decision:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted policy:

`WHOLE_SOURCE_STOP`

Implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

Runtime contract:

`1.2.0`

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No change to:

- `scripts/ca_sco_property_type_semantic_verification.py`;
- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- canonical member offsets;
- parser/projector;
- regex;
- trimming/casing/normalization.

`DECISIONS.md` remains unchanged. The accepted structural strategy is a bounded operational verification design under existing deterministic/fail-closed governance and does not introduce new architecture or runtime semantics.

## Source / Downstream Governance

Current state:

- baseline-refresh proposal prepared: `true`;
- proposal human-reviewed: `true`;
- proposal accepted as bounded design: `true`;
- network revalidation authorized: `false`;
- fresh execution approval granted: `false`;
- fresh structural-byte privacy approval granted: `false`;
- workflow creation authorized: `false`;
- retry authorized: `false`;
- current historical baseline suitable for blind reuse: `false`;
- candidate replacement baseline established: `false`;
- candidate baseline adopted: `false`;
- source continuation authorized: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- semantic compatibility: unresolved;
- production classification: inactive;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

## Canonical Read Order Before Any New Change

Read in exact order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

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

This next task is **repository-only** and must remain separate from execution.

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

1. verify remote HEAD of the current review branch;
2. verify latest CI for that exact HEAD;
3. read the five canonical files in exact order;
4. read the review audit and accepted proposal artifacts;
5. execute only `HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION`;
6. perform no external request during authorization.
