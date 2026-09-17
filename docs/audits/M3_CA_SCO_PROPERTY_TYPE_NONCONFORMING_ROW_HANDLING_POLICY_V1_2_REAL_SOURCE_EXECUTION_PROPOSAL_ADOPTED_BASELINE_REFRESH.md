# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution Proposal — Adopted-Baseline Refresh

Date: 2026-09-17

Status: **REFRESH COMPLETED — CI GREEN — REPOSITORY ONLY — HUMAN PROPOSAL REVIEW REQUIRED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Action

`REFRESH_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_FOR_ADOPTED_BASELINE`

Classification:

`A — Product Critical`

MVP-1 blocker addressed:

`FIRST APPROVED REAL SOURCE -> existing bounded semantic-execution proposal was stale after transport/archive-layout baseline adoption`

## Authoritative base

Repository:

`pierluigiavvanzo-creator/unclaimed-platform`

Base branch:

`m3-ca-sco-transport-archive-layout-baseline-adoption`

Base HEAD:

`6188806e58ac87ccde7b8d6d20dcb2bbbec67c28`

Base CI:

`35210199280` — **SUCCESS**

Adopted-baseline audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_ADOPTION.md`

Reviewed structural evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`

## Refresh checkpoint

Branch:

`m3-ca-sco-property-type-v1-2-real-source-proposal-adopted-baseline-refresh`

Functional refresh HEAD:

`c4dfc596b18fccd3348a388c1d08647d5cd00a45`

GitHub Actions CI:

`35217101641` — **SUCCESS**

Verified CI markers:

- Ruff: PASS;
- mypy: PASS;
- contract tests: PASS;
- smoke tests: PASS;
- full pytest: PASS;
- frontend lint: PASS;
- frontend typecheck: PASS;
- frontend build: PASS;
- Streamlit safety smoke: PASS;
- Streamlit startup smoke: PASS.

## Reuse-first decision

No new execution design, transport library, parser, projector or workflow mechanism is introduced.

Decision:

`REUSE existing v1.2 proposal + existing runner + existing schema/test pattern`

Only stale baseline/provenance bindings were refreshed. This avoids unnecessary custom work and keeps the task on the shortest path to one bounded real-source semantic verification.

## Refreshed proposal

Proposal path:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Proposal version:

`1.1.0`

Proposal status remains:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

Prepared on:

`2026-09-17`

The proposal base now points to the CI-green adopted-baseline checkpoint and records the accepted baseline-adoption and evidence-review provenance.

## Adopted canonical offsets

The sample plan now matches the active semantic runner and reviewed structural evidence exactly:

- `From_500_To_Beyond_1_of_4.csv` -> `0`;
- `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
- `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
- `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

The contract regression verifies that these offsets equal both the runner constants and persisted structural evidence, and that runner content length / ETag still equal the reviewed adopted values.

## Authorization state

All prior execution/privacy approvals remain consumed and non-reusable, including the historical v1.2 semantic execution/privacy approvals and the structural-revalidation execution/privacy approvals.

The refreshed proposal still requires fresh single-use:

- execution approval;
- transient-row privacy approval.

Current proposal values remain:

- `execution_approval_status = REQUIRED_NOT_GRANTED`;
- `execution_approval_ref = null`;
- `transient_row_privacy_approval_status = REQUIRED_NOT_GRANTED`;
- `transient_row_privacy_approval_ref = null`;
- `network_workflow_creation_authorized = false`;
- `real_execution_authorized = false`.

No fresh approval is created or granted by this refresh.

## Preserved execution boundary

Unchanged:

- runtime contract `1.2.0`;
- deterministic four-member prefix sample;
- max 4 data rows/member;
- max 16 data rows total;
- max 1 HEAD request;
- max 4 Range requests;
- max 5 HTTP requests total;
- max 131072 response bytes/range;
- max 524288 source response-body bytes total;
- max 262144 transient uncompressed bytes/member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes/logical record;
- no additional range;
- no full-body fallback;
- no automatic widening;
- no automatic retry in the later one-shot path;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no trim/case conversion/normalization;
- parser/projector unchanged;
- D-008 `WHOLE_SOURCE_STOP` fail-closed mapping unchanged;
- privacy/persistence boundary unchanged;
- source continuation remains false after a nonconforming trigger.

## Explicitly not performed

This refresh did not:

- access California SCO;
- perform HEAD or Range requests;
- inspect source-body bytes, rows or fields;
- create or trigger a network workflow;
- execute the semantic runner against the real source;
- grant or reuse execution/privacy approvals;
- modify parser/projector/regex/normalization;
- modify source policy or registry;
- activate production classification;
- start identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## DECISIONS.md assessment

No architecture, policy or product-strategy decision changed. `DECISIONS.md` remains unchanged.

## Next gate

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW`

That review may accept or reject only proposal version `1.1.0` and its adopted-baseline provenance. It must not grant approvals, create a network workflow, perform source access or execute the real-source semantic verification.
