# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-v1-2-real-source-proposal-adopted-baseline-refresh`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California is only a critical-path enabler for the first lawful approved real source.

## Latest Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification:

`A — Product Critical`

Reviewed implementation checkpoint:

- HEAD `16a7e6f82a17a3f27b74195067aa1cff34bcba0e`;
- CI `35218563391` — **SUCCESS**.

Review result:

`FAIL_MINIMAL_REMEDIATION_REQUIRED`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW.md`

## Why the review failed

Proposal `1.1.0` correctly binds to the adopted runtime baseline and remains non-authorizing, but the refresh was not purely conservative.

The historical proposal `1.0.0` contains reviewed fields that were omitted from `1.1.0` and its schema even though they are unrelated to transport/archive-layout rebinding.

Fields to restore exactly from the historical design:

- `historical_authorization_state.consumed_approval_refs`;
- `execution_question.question`;
- `sample_plan.sample_bias_note`;
- `row_processing_controls.official_insurance_codes`;
- `v1_2_outcome_contract.unrelated_stop_control_disposition`;
- `v1_2_outcome_contract.non_stopped_control_disposition`;
- `v1_2_outcome_contract.specific_real_source_outcome_required_for_proposal_acceptance`;
- `privacy_controls.control_disposition_allowed_persisted_fields`;
- `privacy_controls.control_disposition_source_value_bearing_fields_allowed`;
- `privacy_controls.derived_summary_persistence_allowed`;
- `privacy_controls.allowed_persisted_derived_fields`;
- top-level `acceptance_criteria`.

The explicit privacy/persistence allowlists are the most material omission because the proposal is intended to become the frozen boundary for fresh authorization.

## What remains valid

Adopted runtime baseline:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- canonical offsets `0`, `59745428`, `96861315`, `134172553`.

Runtime remains unchanged:

- contract `1.2.0`;
- parser/projector unchanged;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no trimming/casing/normalization changes;
- D-008 `WHOLE_SOURCE_STOP` unchanged;
- four-member deterministic prefix sample unchanged;
- request/byte caps unchanged;
- no widening;
- `automatic_retry_allowed = false` may remain as an additive conservative constraint.

Historical proposal remains preserved unchanged:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`

Current refreshed proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`

Current refreshed schema:

`schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.v1_1.schema.json`

Current refresh contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal_v1_1.py`

## Network / Approval State

No California SCO request was performed by the refresh or review.

No network workflow exists for this execution.

All previous execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No fresh execution or transient-row privacy approval currently exists.

## Source / Product State

- transport/archive-layout baseline adopted: `true`;
- proposal rebound to adopted baseline: `true`;
- proposal refresh review: `FAIL_MINIMAL_REMEDIATION_REQUIRED`;
- approved real sources: `0`;
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

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW.md`;
2. proposal `v1_1.json`;
3. proposal schema `v1_1.schema.json`;
4. proposal `v1.json` for exact historical values;
5. the v1.1 contract test;
6. `scripts/ca_sco_property_type_semantic_verification.py`.

## SINGLE NEXT ACTION

Execute exclusively:

`REMEDIATE_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_CONTRACT_PRESERVATION`

Classification:

`A — Product Critical`

This action is repository-only.

It must:

- restore exactly the omitted reviewed fields listed above from proposal `1.0.0` into `1.1.0`;
- preserve the adopted baseline length, ETag and offsets already present in `1.1.0`;
- preserve the current adopted-baseline provenance/checkpoint fields;
- preserve `automatic_retry_allowed = false`;
- update the v1.1 schema to require the restored fields with the historical reviewed values;
- extend the contract test to prove preservation against proposal `1.0.0` where appropriate;
- run full CI.

It must not:

- access California SCO;
- create/trigger a network workflow;
- grant or reuse execution/privacy approvals;
- change runtime/parser/projector/regex/trimming/casing/normalization;
- change D-008;
- alter the adopted transport/archive-layout baseline;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, beneficiary matching, outreach or claim submission.

After CI-green remediation, perform the minimum human re-review. A PASS should then move directly to fresh single-use execution + transient-row privacy authorization for exactly one bounded real-source semantic execution.
