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

M3 California is only a critical-path enabler for the first lawful approved real source. Optimize for the shortest safe path; do not add diagnostics, governance or infrastructure unless they materially unblock an A-risk or MVP-1 exit criterion.

## Latest Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification:

`A — Product Critical`

Reviewed checkpoint:

- HEAD `ed6a22a3ed5c727b3b4dd7f14416bb06acab2903`;
- CI `35220411955` — **SUCCESS**.

Review result:

`PASS_REMEDIATED_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_FOR_FRESH_SINGLE_USE_AUTHORIZATION`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REMEDIATION_RE_REVIEW.md`

## Re-Review Basis

The previous review had returned `FAIL_MINIMAL_REMEDIATION_REQUIRED` because proposal `1.1.0` omitted 12 reviewed fields from historical proposal `1.0.0`.

The remediation restored all 12 exactly:

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

The v1.1 schema requires them and contract tests compare them with historical proposal `1.0.0` where appropriate.

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

Historical proposal `1.0.0` remains unchanged as provenance.

## Preserved Execution Design

Unchanged:

- four canonical members;
- deterministic first-complete-row prefix sampling;
- max 4 data rows/member and 16 total;
- max 1 HEAD, 4 Range, 5 HTTP requests;
- existing byte caps;
- no additional Range;
- no full-body fallback;
- no automatic widening;
- `automatic_retry_allowed = false`;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP` fail-closed behavior;
- memory-only transient-row privacy boundary;
- persisted control-disposition fields limited to `status_code` and `reason_code`;
- no source-value-bearing control-disposition fields;
- reviewed derived-summary allowlist only;
- no row/value persistence or row-specific human inspection.

## Network / Approval State

No California SCO request has been performed by the remediation or re-review.

No network execution workflow exists for this action.

All prior execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Fresh single-use real-source execution approval: **NOT GRANTED**.

Fresh transient-row privacy approval: **NOT GRANTED**.

## Source / Product State

- transport/archive-layout baseline adopted: `true`;
- proposal `1.1.0` accepted for fresh authorization: `true`;
- approved real sources: `0`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- semantic compatibility: unresolved;
- production classification: inactive;
- real MVP-1 candidate cases: `0`;
- commercial baseline from real cases: not established;
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

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REMEDIATION_RE_REVIEW.md`;
2. proposal `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`;
3. schema `schemas/common/property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal.v1_1.schema.json`;
4. contract test `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_v1_2_real_source_execution_proposal_v1_1.py`;
5. `scripts/ca_sco_property_type_semantic_verification.py`;
6. historical authorization audit/provenance needed to mint fresh single-use refs without reusing consumed approvals.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

Classification:

`A — Product Critical`

This is a material human authorization gate.

It may grant exactly two fresh single-use references:

1. one bounded real-source semantic execution approval;
2. one transient-row memory-only privacy approval.

The authorization must remain bound to proposal `1.1.0`, the adopted runner baseline and the existing request/byte/privacy/D-008 limits.

It must not itself:

- perform a California SCO request;
- create/trigger the network execution workflow;
- reuse any consumed approval;
- modify runtime/parser/projector/regex/normalization;
- widen sample/request/byte/privacy limits;
- change D-008;
- activate source policy, registry, production classification or downstream work.

After explicit authorization, proceed directly to exactly one bounded real-source semantic execution, consume both fresh refs on first network invocation, persist only contract-approved derived evidence, remove the one-shot workflow after execution, then perform evidence review and source decision. Do not reopen transport diagnostics absent contradictory evidence.
