# M3 California SCO — PROPERTY_TYPE v1.2 Proposal Contract-Preservation Remediation

Date: 2026-09-17

Status: **REMEDIATION IMPLEMENTED — CI GREEN — REPOSITORY ONLY — HUMAN RE-REVIEW REQUIRED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Action

`REMEDIATE_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_CONTRACT_PRESERVATION`

Classification: `A — Product Critical`.

## Trigger

Human refresh review result:

`FAIL_MINIMAL_REMEDIATION_REQUIRED`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW.md`

The review found that proposal `1.1.0` correctly adopted the current transport/archive-layout baseline but omitted reviewed design fields from historical proposal `1.0.0` that were unrelated to baseline rebinding.

## Implementation checkpoint

Branch:

`m3-ca-sco-v1-2-proposal-contract-preservation-remediation`

Implementation HEAD before this closure record:

`509567fb250386e266faf96e3d9acef04631f724`

CI:

`35220182596` — **SUCCESS**

The remediation is three commits ahead of review-closure checkpoint `1ac80c13ca01db1e373e77215855fb3665ad7aa8` and zero commits behind it.

## Restored reviewed fields

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

## Preserved adopted-baseline binding

Unchanged:

- expected length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- canonical offsets `0`, `59745428`, `96861315`, `134172553`;
- adopted-baseline provenance/checkpoint `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28` / CI `35210199280`;
- `automatic_retry_allowed = false`.

## Contract verification

The v1.1 schema now requires the restored fields with the reviewed historical values.

The contract test now proves:

- equality of restored historical design fields against proposal `1.0.0`;
- official insurance codes remain equal to the runner set;
- privacy persisted-field allowlist remains only `status_code` and `reason_code`;
- schema rejection when the privacy allowlist or acceptance contract is removed;
- existing baseline, authorization, retry and normalization protections remain active.

CI `35220182596` passed Ruff, mypy, contract tests, smoke tests, full pytest, Streamlit safety/startup smoke, frontend lint, typecheck and build.

## Runtime / network / authorization boundary

This remediation did not:

- modify the semantic runner;
- modify parser/projector/regex/trimming/casing/normalization;
- modify D-008;
- modify source policy, registry or production classification;
- perform any California SCO request;
- create or trigger a network workflow;
- grant or reuse execution/privacy approvals;
- perform real-row or source-body access;
- activate downstream identity/genealogy/matching/outreach/claim work.

All prior execution/privacy approvals remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

## Decision-file assessment

No new architecture, product-strategy or policy decision is introduced. `DECISIONS.md` remains unchanged.

## Next gate

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

The re-review should be limited to confirming that the previously identified omissions are restored while the adopted baseline and non-authorizing boundary remain unchanged. A PASS should move directly to fresh single-use execution and transient-row privacy authorization for exactly one bounded real-source semantic execution.
