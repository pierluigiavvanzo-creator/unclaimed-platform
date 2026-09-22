# M3 California SCO — PROPERTY_TYPE v1.2 Remediated Real-Source Execution Proposal Re-Review

Date: 2026-09-17

Status: **PASS — REMEDIATED PROPOSAL ACCEPTED FOR SEPARATE FRESH SINGLE-USE AUTHORIZATION — REPOSITORY ONLY — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Action

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification: `A — Product Critical`.

## Product purpose

Close the narrow contract-preservation defect without reopening transport diagnostics, so the project can move directly toward the first lawful approved real source and MVP-1 commercial validation.

## Reviewed checkpoint

Branch:

`m3-ca-sco-v1-2-proposal-contract-preservation-remediation`

Reviewed HEAD:

`ed6a22a3ed5c727b3b4dd7f14416bb06acab2903`

CI:

`35220411955` — **SUCCESS**

## Review result

`PASS_REMEDIATED_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_FOR_FRESH_SINGLE_USE_AUTHORIZATION`

The remediation resolves the exact defect recorded by the previous review and introduces no new runtime, privacy, transport or authorization widening.

## Contract-preservation verification

All 12 fields identified by the previous FAIL are restored exactly from historical proposal `1.0.0`:

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

The v1.1 schema requires these exact values and the contract test compares them with historical proposal `1.0.0` where appropriate.

## Adopted baseline verification

Proposal `1.1.0` remains bound to the active runner baseline:

- expected length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- canonical offsets `0`, `59745428`, `96861315`, `134172553`.

Historical proposal `1.0.0` remains unchanged as provenance.

## Preserved execution boundary

Unchanged:

- four canonical members;
- deterministic prefix sample;
- max 4 data rows/member and 16 total;
- max 1 HEAD, 4 Range and 5 HTTP requests;
- existing byte caps;
- no additional Range;
- no full-body fallback;
- no automatic widening;
- `automatic_retry_allowed = false`;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- trimming/casing/normalization;
- D-008 `WHOLE_SOURCE_STOP` fail-closed mapping;
- source continuation remains false after a triggering nonconformance.

## Privacy / persistence boundary

Restored and preserved:

- transient full-row bytes only after fresh privacy approval;
- memory-only processing;
- zero retention and immediate disposal;
- no raw/full-row/property-id/owner-holder/per-row PROPERTY_TYPE/offending-value persistence;
- persisted `control_disposition` limited to `status_code` and `reason_code`;
- no source-value-bearing control-disposition fields;
- only the previously reviewed derived-summary allowlist;
- no row-specific human inspection.

## Authorization / source state

The proposal remains `PROPOSAL_ONLY_NOT_AUTHORIZED`.

All prior execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No fresh execution or transient-row privacy approval exists yet.

This review performed no California SCO request, no network workflow creation/trigger, no source-body access and no real-row inspection.

Source policy remains `PROPOSED`; registry remains disabled/unapproved; semantic compatibility remains unresolved; production classification and downstream identity/genealogy/matching/outreach/claim gates remain closed.

## Decision-file assessment

No new architecture, product-strategy or policy decision is introduced. `DECISIONS.md` remains unchanged.

## Next gate

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

This next gate may grant fresh single-use execution and transient-row privacy approval references for exactly one bounded real-source semantic execution. It must not itself perform the network execution.

Once explicitly authorized, proceed directly to the one bounded execution, evidence review and source decision; do not reopen transport diagnostics absent contradictory evidence.
