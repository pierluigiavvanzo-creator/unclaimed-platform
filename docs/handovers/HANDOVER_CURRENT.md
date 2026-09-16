# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-transport-archive-layout-baseline-refresh-proposal`

Created from evidence-review checkpoint:

`9dbdc3c6f1ef05c577c26c9e3524ba74fdbfda56`

Evidence-review checkpoint CI:

`35125609902` — **SUCCESS**

## Completed Action

Completed:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

Proposal audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`

Machine proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`

Schema:

`schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`

This completed action is repository-only and design-only. It performed no California SCO request, no HEAD, no Range GET, no authority retrieval, no source-body access and no retry.

## Governing Evidence

Reviewed one-shot execution result remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`;
- HEAD requests = `1`;
- Range requests = `0`;
- HTTP requests total = `1`;
- source body bytes read = `0`;
- rows examined = `0`.

Human evidence-review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

Evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Evidence review:

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

These historical values are `STALE_FOR_FUTURE_EXECUTION_PLANNING_NOT_PROVEN_INVALID`.

One-shot observed drift evidence:

- HTTP `200`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Observed values are evidence only and are not adopted.

Candidate replacement baseline remains entirely unresolved:

- content length = `null`;
- ETag = `null`;
- all four canonical member offsets = `null`.

## Proposed Strategy

The proposal rejects:

- `HEAD_ONLY_TRANSPORT_REFRESH` — insufficient archive-layout proof;
- `ARITHMETIC_MEMBER_OFFSET_REBASE` — unsupported inference;
- `FULL_ARCHIVE_DOWNLOAD_AND_INSPECTION` — excessive scope.

It proposes for human review only:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

Future design, if later approved and separately authorized:

1. one exact-endpoint HEAD for transport identity;
2. bounded Range read of archive tail to locate classic ZIP EOCD;
3. bounded central-directory metadata read only if needed;
4. derive the four canonical `relative offset of local header` values from central-directory metadata;
5. require same-object ETag/length consistency;
6. persist only bounded derived transport/layout evidence;
7. stop for human evidence review before any runner constant changes.

## Preserved Hard Caps

The proposal does not widen the existing source-exposure limits:

- HEAD max `1`;
- Range max `4`;
- HTTP total max `5`;
- response bytes/range max `131072`;
- source response-body bytes total max `524288`;
- full-body fallback `false`;
- automatic widening `false`;
- automatic retry `false`.

If the central directory cannot be resolved within these limits, later execution must stop fail-closed.

## Structural / Privacy Boundary

Proposed later structural access is limited to ZIP metadata. It must not:

- decompress member payload;
- parse CSV;
- inspect rows or protected fields;
- use historical offsets to derive new offsets;
- persist raw Range bytes;
- persist noncanonical member names.

Because a bounded tail Range may contain opaque compressed bytes adjacent to ZIP metadata, a later execution requires a fresh single-use **structural-byte privacy approval** as well as a fresh single-use execution approval.

Both refs are currently `null`; neither approval is granted by this proposal.

## Consumed Approval State

Consumed execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No consumed approval may be reused.

## Runtime / D-008 State

Decision:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design:

`WHOLE_SOURCE_STOP`

Implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

Runtime contract:

`1.2.0`

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The proposal changes none of:

- `scripts/ca_sco_property_type_semantic_verification.py`;
- `EXPECTED_LENGTH`;
- `EXPECTED_ETAG`;
- canonical member offsets;
- parser/projector;
- regex;
- trimming/casing/normalization.

`DECISIONS.md` remains unchanged because the bounded structural strategy is only proposed, not accepted.

## Source / Downstream Governance

Current state:

- baseline-refresh proposal prepared: `true`;
- proposal human-reviewed: `false`;
- network revalidation authorized: `false`;
- fresh execution approval granted: `false`;
- fresh structural-byte privacy approval granted: `false`;
- workflow creation authorized: `false`;
- retry authorized: `false`;
- candidate baseline established: `false`;
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

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL.md`
2. `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`
3. `schemas/common/property_type_transport_archive_layout_baseline_refresh_proposal.schema.json`
4. `tests/contract/test_ca_sco_property_type_transport_archive_layout_baseline_refresh_proposal.py`
5. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`
6. `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`
7. `scripts/ca_sco_property_type_semantic_verification.py`
8. `docs/audits/M3_CA_SCO_TRANSPORT_PREFLIGHT_PROPOSAL.md`
9. `schemas/common/source_transport_preflight_proposal.schema.json` as reuse context.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW`

This next task is repository-only.

It must review whether the proposed bounded central-directory strategy is sufficient, internally consistent, privacy-bounded and compatible with current fail-closed governance.

It may accept, reject or require revision of the proposal.

It must not:

- perform a California SCO or other external request;
- perform HEAD or Range GET;
- grant fresh execution or privacy approvals;
- reuse consumed approval refs;
- create a network workflow;
- retry the v1.2 execution;
- update `EXPECTED_LENGTH`, `EXPECTED_ETAG` or canonical member offsets;
- implement EOCD/central-directory runtime code;
- modify runner/parser/projector/regex/normalization;
- adopt candidate baseline values;
- activate source policy, registry, production classification or downstream work.

If the proposal is later accepted, any network revalidation remains a separate gate and requires fresh single-use approvals before the first request.

## Restart Instruction

1. verify remote HEAD of the current proposal branch;
2. verify latest CI for that exact HEAD;
3. read the five canonical files in exact order;
4. read the proposal audit, machine proposal, schema and contract test;
5. execute only the `SINGLE NEXT ACTION`;
6. perform no external request during proposal review.
