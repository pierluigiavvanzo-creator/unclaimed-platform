# NY MVP-1 Follow-Up Cost → Case Economics Integration — Offline

Date: 2026-09-18

Classification: `A — Product Critical`

## Objective

Connect the verified follow-up-cost measurement contract to the existing explicit case-economics contract without inventing or substituting cost values.

## Reuse decision

Reused directly:

- `NyMvp1FollowUpCostMeasurementResult`;
- `NyMvp1ExplicitCaseEconomicsInput`;
- `NyMvp1ExplicitCaseEconomicsResult`;
- `compute_explicit_case_economics`;
- existing JSON Schema draft 2020-12 conventions.

No new library or economics engine is introduced.

Decision:

`REUSE EXISTING CONTRACTS + THIN FAIL-CLOSED ADAPTER`

## Integration rule

A measured follow-up cost may enter the explicit case-economics contract only when:

`fully_loaded_follow_up_cost_state = COMPUTED_FROM_MEASURED_COMPONENTS`

and:

`fully_loaded_follow_up_cost_cents != null`

If either condition is false, the integration result is:

`BLOCKED_FOLLOW_UP_COST_UNAVAILABLE`

with:

- `measured_follow_up_cost_cents = null`;
- no explicit economics input;
- no explicit economics result.

The direct machine/data cost is intentionally not substituted for the unavailable fully loaded cost.

## Provenance

The bridge preserves:

- candidate case id;
- follow-up cost measurement id;
- all component-level follow-up cost evidence refs;
- value evidence ref;
- fee evidence ref.

The existing single `cost_evidence_ref` field receives a deterministic aggregate measurement reference:

`follow-up-cost-measurement:<measurement_id>`

This reference points back to the measurement result whose component evidence refs remain visible in the bridge result.

## Safety / scope

This implementation is synthetic/test-only.

It does not:

- access or download the NY OSC Owner Name File;
- process real owner PII;
- infer or invent a labor rate;
- infer or invent case value;
- infer or invent an agreed fee;
- make a commercial continue/stop recommendation;
- perform outreach, representation, fee agreement or claim activity.

## Cross-module note

This is a bounded cross-module integration between the already verified follow-up-cost measurement domain and case-economics domain. No existing contract is modified or version-broken; the new bridge is additive and rollback is deletion of the bridge module, its two schemas, tests and this audit.

## Acceptance criteria

- fully loaded measured cost flows into `measured_follow_up_cost_cents`;
- missing documented labor rate blocks the integration;
- machine/data direct cost alone is never relabeled as fully loaded cost;
- all cost evidence refs survive the bridge;
- existing case-economics arithmetic remains authoritative;
- no commercial recommendation is introduced.
