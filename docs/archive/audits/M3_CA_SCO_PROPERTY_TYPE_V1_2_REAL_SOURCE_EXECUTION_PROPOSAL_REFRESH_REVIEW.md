# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution Proposal Refresh Review

Date: 2026-09-17

Status: **REVIEW COMPLETED — FAIL_MINIMAL_REMEDIATION_REQUIRED — REPOSITORY ONLY — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Action

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_REVIEW`

Classification: `A — Product Critical`.

## Reviewed checkpoint

Branch:

`m3-ca-sco-v1-2-real-source-proposal-adopted-baseline-refresh`

Reviewed HEAD:

`16a7e6f82a17a3f27b74195067aa1cff34bcba0e`

CI:

`35218563391` — **SUCCESS**

The reviewed branch is eight commits ahead of adopted-baseline checkpoint `6188806e58ac87ccde7b8d6d20dcb2bbbec67c28` and zero commits behind it.

## Review result

`FAIL_MINIMAL_REMEDIATION_REQUIRED`

The refreshed proposal correctly binds the execution plan to the adopted transport/archive-layout baseline and remains non-authorizing, but it does **not** satisfy the stated requirement that the accepted v1.2 execution design be preserved while changing only stale baseline/provenance binding and strictly dependent assertions.

The issue is contract preservation, not runtime behavior and not transport evidence.

## What passes

### Adopted baseline binding — PASS

Proposal `1.1.0` matches the active semantic runner:

- expected length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- canonical offsets `0`, `59745428`, `96861315`, `134172553`.

The contract test compares these values directly with the runner.

### Historical artifact preservation — PASS

Historical proposal `1.0.0` remains unchanged and is explicitly referenced as provenance.

### Sampling and transport caps — PASS

Preserved:

- four canonical members;
- max 4 rows/member and 16 total;
- max 1 HEAD, 4 Range and 5 HTTP requests;
- existing byte caps;
- no additional range;
- no full-body fallback;
- no widening.

The refresh also adds explicit `automatic_retry_allowed = false`, which is conservative.

### Runtime / D-008 boundary — PASS

Preserved:

- runtime contract `1.2.0`;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no trimming, uppercasing or normalization;
- parser/projector unchanged;
- D-008 `WHOLE_SOURCE_STOP` status/reason mapping;
- no continuation after `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

### Authorization / network boundary — PASS

The proposal remains `PROPOSAL_ONLY_NOT_AUTHORIZED`.

Fresh execution and transient-row privacy approvals remain required and not granted.

All prior approvals remain consumed/non-reusable.

No California SCO request or network workflow was performed or authorized by the refresh/review.

## Contract-preservation defect

The historical proposal `1.0.0` contained explicit reviewed fields that are absent from proposal `1.1.0` and its schema even though they are unrelated to the adopted transport baseline.

The removed fields include:

### Historical authorization provenance

- `historical_authorization_state.consumed_approval_refs`

### Execution question

- `execution_question.question`

### Sampling rationale

- `sample_plan.sample_bias_note`

### PROPERTY_TYPE control vocabulary

- `row_processing_controls.official_insurance_codes`

### v1.2 outcome contract

- `v1_2_outcome_contract.unrelated_stop_control_disposition`
- `v1_2_outcome_contract.non_stopped_control_disposition`
- `v1_2_outcome_contract.specific_real_source_outcome_required_for_proposal_acceptance`

### Privacy / persistence boundary

- `privacy_controls.control_disposition_allowed_persisted_fields`
- `privacy_controls.control_disposition_source_value_bearing_fields_allowed`
- `privacy_controls.derived_summary_persistence_allowed`
- `privacy_controls.allowed_persisted_derived_fields`

### Acceptance contract

- top-level `acceptance_criteria`

These removals are outside the authorized purpose of the refresh. In particular, removing explicit privacy/persistence allowlists weakens the proposal as a frozen authorization boundary even though current runtime code and execution schema remain unchanged.

## Required minimal remediation

Do **not** redesign the proposal.

Create the smallest repository-only remediation that:

1. restores the omitted historical design fields above with exactly the previously reviewed values;
2. retains proposal version `1.1.0` unless schema/versioning rules require a strictly additive patch revision;
3. retains the adopted length, ETag and four offsets already present;
4. retains the new adopted-baseline provenance/checkpoint fields;
5. retains `automatic_retry_allowed = false`;
6. updates the v1.1 schema to require the restored fields;
7. extends the contract test to assert equality of all restored design fields against the historical proposal where appropriate;
8. performs no source access and changes no runtime/parser/projector/regex/normalization/D-008 behavior.

## Product impact

This is a narrow repository-contract defect. It does not reopen transport diagnostics and does not invalidate the adopted runtime baseline.

The shortest path to MVP-1 remains:

`minimal proposal contract remediation -> human review -> fresh single-use authorization -> exactly one bounded real-source semantic execution -> evidence review -> source decision`.

## DECISIONS.md assessment

No new architecture, product-strategy or policy decision is introduced. `DECISIONS.md` remains unchanged.

## Next single action

Execute exclusively:

`REMEDIATE_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REFRESH_CONTRACT_PRESERVATION`

Classification:

`A — Product Critical`

This next action is repository-only and must restore the omitted reviewed fields without changing the adopted baseline, runtime behavior, privacy scope, D-008, source policy, registry, production classification or downstream gates.
