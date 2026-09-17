# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-transport-archive-layout-revalidation-once`

Always verify the remote branch HEAD and its latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

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

M3 California work is only a critical-path enabler for the first lawful approved real source.

## Latest Completed Action

Completed:

`EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`

Classification:

`A/B — MVP-1 critical-path enabler`

Execution result:

`CANDIDATE_BASELINE_ESTABLISHED`

No baseline value was adopted.

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EXECUTION.md`

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`

Evidence schema:

`schemas/common/property_type_transport_archive_layout_revalidation_execution.v1.schema.json`

Evidence contract test:

`tests/contract/test_ca_sco_property_type_transport_archive_layout_revalidation_execution.py`

## Execution Checkpoints

Authorization checkpoint:

- branch: `m3-ca-sco-transport-archive-layout-revalidation-authorization`;
- HEAD: `4079fb44b36699e9b05821761c222d063a89648d`;
- CI: `35196883549` — **SUCCESS**.

Implementation preflight checkpoint:

- HEAD: `e87e7d20d766ad06ca0feb8805ac00c4a6ed547c`;
- dedicated preflight run: `35198561293` — **SUCCESS**;
- general CI: `35198561164` — **SUCCESS**;
- real source execution in preflight: skipped.

Execution trigger checkpoint:

`de4c20e0a4158da0497d2ca9c2090589636b40e0`

Real one-shot workflow:

- run: `35198720002`;
- job: `105128028851`;
- attempt: `1`;
- conclusion: **SUCCESS**;
- rerun: not authorized / not performed.

The one-shot job successfully completed implementation/authorization validation, repository-only tests, real structural execution, evidence/privacy validation, and derived-evidence artifact upload.

## Artifact Provenance

GitHub Actions artifact:

- id: `10487072813`;
- name: `ca-sco-transport-archive-layout-revalidation-2026-09-17`;
- artifact digest: `sha256:2ed7f3e620a50f635f3eae7dad5efca80f3dc86d239c728dd12dfd23eda07e65`.

Persisted evidence file SHA-256:

`120f5ee2eef859578adb922f15138bab65cb19e7979274ed9360c24b9b071d64`

## Candidate Evidence

Observed transport candidate:

- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`;
- observed at: `2026-09-17T08:15:58.436797Z`.

Canonical match status:

`ALL_CANONICAL_MEMBERS_UNIQUE`

Additional members:

`0`

Candidate canonical local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` -> `0`;
2. `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
3. `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
4. `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

These values are **candidate evidence only**. They have not been adopted into the semantic runner or source policy.

## Authorization State After Execution

Structural revalidation execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They were consumed together on the first California SCO network request of the successful one-shot run. No retry is authorized.

Historical v1.2 approvals also remain consumed and non-reusable.

## Accepted Structural / Privacy Boundary

Accepted design remains:

`BOUNDED_ZIP_CENTRAL_DIRECTORY_METADATA_REVALIDATION`

Path:

`HEAD -> ZIP tail -> classic EOCD -> bounded Central Directory -> canonical relative local-header offsets`

Hard caps:

- HEAD max `1`;
- Range max `4`;
- HTTP total max `5`;
- response bytes/range max `131072`;
- source response-body bytes total max `524288`;
- full-body fallback `false`;
- automatic widening `false`;
- automatic retry `false`.

Structural constraints:

- exact HTTPS endpoint / host;
- same-object ETag / `If-Match` consistency;
- `Content-Range` total consistent with HEAD length;
- classic ZIP only;
- ZIP64 rejected;
- multi-disk rejected;
- central-directory metadata only;
- no decompression;
- no CSV parsing;
- no row/field inspection;
- canonical member names unique;
- candidate offsets derived from Central Directory only.

Privacy boundary:

- structural bytes memory-only;
- retention `0` days;
- raw Range bytes not persisted;
- compressed payload not decompressed;
- CSV not parsed;
- no protected record field inspected;
- noncanonical member names not persisted;
- only approved derived evidence persisted.

The approved evidence schema intentionally does not persist exact request counters. Do not invent them.

## Historical Runtime Baseline Remains Unchanged

Semantic runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Runtime contract:

`1.2.0`

Historical pins still in runtime:

- `EXPECTED_LENGTH = 162416884`;
- `EXPECTED_ETAG = "b25b315b6cd8007624387c3a00d4b1fe"` including HTTP quote characters;
- canonical offsets: `0`, `59747797`, `96862896`, `134174190`.

Other runtime state remains unchanged:

- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector unchanged;
- trimming/casing/normalization unchanged;
- D-008 `WHOLE_SOURCE_STOP` unchanged.

No candidate value may be treated as adopted until a separate human evidence review and later separately authorized implementation gate complete.

## Source / Product State

- approved real sources: `0`;
- candidate transport/archive-layout baseline established: `true`;
- candidate baseline adopted: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- semantic compatibility: unresolved;
- production classification: inactive;
- real MVP-1 candidate cases: `0`;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

`DECISIONS.md` remains unchanged because this execution did not introduce a new architecture, strategy or policy decision.

## Temporary Workflow Cleanup

The one-shot workflow and trigger are execution-only artifacts and must not remain active after this completed run. The completed execution-state commit removes:

- `.github/workflows/ca-sco-transport-archive-layout-revalidation-once.yml`;
- `.github/ca-sco-transport-archive-layout-revalidation-once.trigger.json`;
- the temporary execution-stage contract test tied to workflow presence.

The structural verifier, execution evidence schema, synthetic unit tests and reuse audit remain for provenance and deterministic verification.

## Canonical Read Order Before Any New Change

Read in exact order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EXECUTION.md`;
2. `sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`;
3. `schemas/common/property_type_transport_archive_layout_revalidation_execution.v1.schema.json`;
4. `tests/contract/test_ca_sco_property_type_transport_archive_layout_revalidation_execution.py`;
5. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_AUTHORIZATION.md`;
6. `sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation_approval.v1.json`;
7. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_REVIEW.md`;
8. `sources/proposals/ca_sco_segment_500_plus.property_type_transport_archive_layout_baseline_refresh.v1.json`;
9. `scripts/ca_sco_property_type_semantic_verification.py`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`

Classification:

`A/B — MVP-1 critical-path enabler`

This next action is repository-only.

It must:

- review the persisted evidence and execution provenance;
- verify candidate values are evidence-only and runtime pins remain unchanged;
- decide whether evidence is sufficient to justify a later separate baseline-adoption implementation gate;
- keep both consumed approval refs non-reusable.

It must not:

- perform another California SCO request;
- retry the one-shot execution;
- grant replacement execution/privacy approvals;
- adopt content length, ETag or offsets in the same review;
- modify semantic-runner constants;
- change parser/projector/regex/normalization;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, matching, outreach or claim submission.

## Restart Instruction

1. verify remote HEAD of `m3-ca-sco-transport-archive-layout-revalidation-once`;
2. verify latest CI for that exact HEAD;
3. read the six canonical files in exact order;
4. inspect the execution audit + persisted evidence + contract test;
5. execute only `HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`;
6. perform no source/network request during that review.
