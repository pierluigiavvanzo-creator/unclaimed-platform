# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-v1-2-proposal-contract-preservation-remediation`

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

`REMEDIATE_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_CONTRACT_PRESERVATION`

Classification:

`A — Product Critical`

Implementation checkpoint before closure docs:

- HEAD `509567fb250386e266faf96e3d9acef04631f724`;
- CI `35220182596` — **SUCCESS**.

Remediation audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_CONTRACT_PRESERVATION_REMEDIATION.md`

## Prior Review Finding

The prior human refresh review returned:

`FAIL_MINIMAL_REMEDIATION_REQUIRED`

because proposal `1.1.0` correctly adopted the new transport/archive-layout baseline but omitted reviewed design fields from historical proposal `1.0.0` that were unrelated to baseline rebinding.

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW.md`

## Remediation Result

Restored exactly from historical proposal `1.0.0`:

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

Proposal version remains `1.1.0`.

The v1.1 schema now requires the restored values and the contract test compares them against proposal `1.0.0` where appropriate. It also rejects removal of the privacy persisted-field allowlist and top-level acceptance contract.

## Adopted Runtime Baseline

Semantic runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Runtime contract:

`1.2.0`

Active pins remain:

- `EXPECTED_LENGTH = 162560390`;
- `EXPECTED_ETAG = "222dd79f04c2a0a8fff166b01c8da746"`;
- `From_500_To_Beyond_1_of_4.csv` -> `0`;
- `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
- `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
- `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

The remediation does not alter these pins or the adopted-baseline provenance/checkpoint.

## Preserved Execution Design

Unchanged:

- four canonical members;
- deterministic first-complete-row prefix sampling;
- max 4 data rows/member and 16 total;
- max 1 HEAD, 4 Range, 5 HTTP requests;
- existing range/body/transient/logical-record byte caps;
- no additional range;
- no full-body fallback;
- no automatic widening;
- `automatic_retry_allowed = false`;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- trimming/casing/normalization rules;
- D-008 `WHOLE_SOURCE_STOP` fail-closed control disposition;
- transient-row memory-only privacy boundary;
- persisted `control_disposition` fields limited to `status_code` and `reason_code`;
- no source-value-bearing control-disposition fields;
- reviewed derived-summary allowlist only;
- no row/value persistence or row-specific human inspection.

## Network / Approval State

This remediation performs no California SCO request and creates no network workflow.

All prior execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No fresh real-source execution or transient-row privacy approval exists yet.

## Source / Product State

- transport/archive-layout baseline adopted: `true`;
- real-source proposal rebound to adopted baseline: `true`;
- proposal contract-preservation remediation: `CI_GREEN_PENDING_HUMAN_RE_REVIEW`;
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
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_CONTRACT_PRESERVATION_REMEDIATION.md`;
3. proposal `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`;
4. schema `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.v1_1.schema.json`;
5. historical proposal `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`;
6. contract test `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal_v1_1.py`;
7. `scripts/ca_sco_property_type_semantic_verification.py`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification:

`A — Product Critical`

This is a minimum repository-only re-review of the remediation delta.

It must confirm:

- all 12 fields identified by the previous FAIL are restored exactly from historical proposal `1.0.0`;
- proposal/schema contract validity;
- adopted length, ETag and canonical offsets remain equal to the active runner;
- historical proposal remains unchanged as provenance;
- sample/request/byte caps are unchanged;
- no automatic widening or retry is introduced;
- regex/parser/projector/normalization boundaries are unchanged;
- D-008 fail-closed behavior is unchanged;
- privacy/persistence allowlists are restored and unchanged;
- proposal remains non-authorizing;
- all consumed approvals remain non-reusable;
- source policy, registry, production classification and downstream gates remain closed.

It must not:

- perform a California SCO request;
- create/trigger a network workflow;
- grant or reuse execution/privacy approvals;
- modify runtime/parser/projector/regex/normalization;
- change D-008;
- activate source policy, registry or production classification;
- start identity resolution, genealogy, beneficiary matching, outreach or claim submission.

A PASS should move directly to fresh single-use execution + transient-row privacy authorization for exactly one bounded real-source semantic execution. Do not reopen transport diagnostics without new contradictory evidence.
