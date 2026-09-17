# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-transport-archive-layout-revalidation-once`

Verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California work is only a critical-path enabler for the first lawful approved real source. Avoid additional diagnostics/governance that do not shorten that path.

## Latest Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`

Classification:

`A/B — MVP-1 critical-path enabler`

Review result:

`PASS_CANDIDATE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_EVIDENCE_ACCEPTED_FOR_SEPARATE_ADOPTION_IMPLEMENTATION`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW.md`

Reviewed base checkpoint:

- HEAD: `ac7ced81299d5a563e4c4beeb74858ba28e2b50a`;
- CI: `35199132893` — **SUCCESS**.

The review was repository-only. It performed no California SCO request and no retry.

## Execution Provenance

Successful one-shot structural revalidation:

- run `35198720002`;
- job `105128028851`;
- attempt `1`;
- conclusion **SUCCESS**;
- rerun not authorized / not performed.

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EXECUTION.md`

Artifact provenance:

- artifact id `10487072813`;
- artifact digest `sha256:2ed7f3e620a50f635f3eae7dad5efca80f3dc86d239c728dd12dfd23eda07e65`;
- evidence SHA-256 `120f5ee2eef859578adb922f15138bab65cb19e7979274ed9360c24b9b071d64`.

## Human-Accepted Candidate Baseline

Candidate transport:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Canonical status:

`ALL_CANONICAL_MEMBERS_UNIQUE`

Additional members:

`0`

Candidate canonical local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` -> `0`;
2. `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
3. `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
4. `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

These values are accepted as sufficient evidence for a separate repository-only adoption implementation, but are not yet adopted.

## Current Runtime Baseline — Still Historical

Semantic runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Runtime contract:

`1.2.0`

Current runtime pins remain:

- `EXPECTED_LENGTH = 162416884`;
- `EXPECTED_ETAG = "b25b315b6cd8007624387c3a00d4b1fe"`;
- offsets `0`, `59747797`, `96862896`, `134174190`.

Other runtime behavior remains unchanged:

- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector unchanged;
- trimming/casing/normalization unchanged;
- D-008 `WHOLE_SOURCE_STOP` unchanged.

## Approval State

Structural execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Current state of both:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Important: the historical authorization JSON still records its pre-execution `GRANTED_NOT_CONSUMED` snapshot. That artifact is provenance only and must never be treated as current/fresh authority after run `35198720002`.

No replacement network/privacy approval exists.

## Product / Source State

- approved real sources: `0`;
- candidate transport/archive-layout baseline established: `true`;
- human evidence review accepted: `true`;
- candidate baseline adopted: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- semantic compatibility: unresolved;
- production classification: inactive;
- real MVP-1 candidate cases: `0`;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Canonical Read Order Before Any New Change

Read in exact order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW.md`;
2. `sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`;
3. `tests/contract/test_ca_sco_property_type_transport_archive_layout_revalidation_execution.py`;
4. `scripts/ca_sco_property_type_semantic_verification.py`.

## SINGLE NEXT ACTION

Execute exclusively:

`IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`

Classification:

`A/B — MVP-1 critical-path enabler`

This next action is repository-only.

It may:

- set `EXPECTED_LENGTH = 162560390`;
- set `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- set canonical member offsets to `0`, `59745428`, `96861315`, `134172553`;
- update regression/contract tests strictly as required;
- run full CI and smoke tests;
- update state/roadmap/handover after green verification.

It must not:

- perform any California SCO request;
- reuse consumed approvals;
- change parser/projector/regex/trimming/casing/normalization;
- change D-008 semantics;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, beneficiary matching, outreach or claim submission.

After CI-green baseline adoption, return immediately to the shortest safe path toward a freshly authorized real-source semantic verification and then one approved real source.

## Restart Instruction

1. verify remote HEAD and latest CI;
2. read the six canonical files;
3. inspect the evidence-review audit and persisted candidate evidence;
4. execute only `IMPLEMENT_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION`;
5. perform no source/network request.
