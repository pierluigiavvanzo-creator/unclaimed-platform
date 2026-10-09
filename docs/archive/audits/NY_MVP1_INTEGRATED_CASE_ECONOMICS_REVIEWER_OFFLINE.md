# NY MVP-1 Integrated Case Economics Reviewer — Offline Exposure

Date: 2026-09-18

Classification: `A — Product Critical`

## Objective

Expose the already verified follow-up-cost → case-economics integration through the existing reviewer API and Streamlit surface without opening any real-data boundary.

## Reuse

Reused directly:

- existing FastAPI reviewer router;
- existing Streamlit safe-read-model adapter pattern;
- existing Streamlit card/row visual language;
- `NyMvp1FollowUpCostMeasurementResult`;
- `NyMvp1CaseEconomicsIntegrationResult`;
- existing deterministic synthetic measurement/economics functions.

No new frontend framework, state library, charting library or economics implementation was introduced.

Decision:

`REUSE EXISTING REVIEWER + TWO SYNTHETIC STATES`

## Reviewer contract

New endpoint:

`GET /api/reviewer/mvp1/economics/integrated`

It returns one synthetic read-only snapshot containing two explicit scenarios.

### READY scenario

`READY_WITH_DOCUMENTED_LABOR_RATE`

Expected state:

`READY_FOR_EXPLICIT_ECONOMICS`

The synthetic fixture has a documented synthetic labor-rate evidence reference, so fully loaded follow-up cost exists and the already verified explicit economics engine can compute its arithmetic.

### BLOCKED scenario

`BLOCKED_WITHOUT_DOCUMENTED_LABOR_RATE`

Expected state:

`BLOCKED_FOLLOW_UP_COST_UNAVAILABLE`

The direct machine/data component remains visible for reviewer education, but the integration exposes:

- no fully loaded follow-up cost;
- no explicit economics result;
- no substitute cost.

This makes the fail-closed boundary visible rather than merely implicit in backend tests.

## Safety contract

The reviewer snapshot explicitly carries:

- `real_source_accessed = false`;
- `owner_file_downloaded = false`;
- `real_owner_pii_processed = false`;
- `automatic_commercial_recommendation = false`.

The Streamlit adapter validates these invariants again before display.

## UI

Streamlit now shows two adjacent MVP-1 integrated-economics cards:

1. ready / documented fully loaded cost;
2. blocked / incomplete labor cost.

Both are visibly synthetic. Both state that no automatic recommendation exists and a human decision remains required.

The blocked card labels direct machine/data cost as `NOT FULLY LOADED`.

## Contract-first evidence

Added:

`schemas/ui/ny_mvp1_integrated_economics_reviewer.schema.json`

The schema references the existing follow-up-cost and economics-integration result contracts rather than duplicating their definitions.

Contract and smoke tests verify:

- API ready and blocked states;
- reviewer safety flags;
- preservation of evidence refs;
- blocked state does not expose a substitute follow-up cost;
- Streamlit visual labels remain present.

## Scope boundary

No NY OSC Owner Name File was accessed or downloaded. No real owner PII was processed. No identity resolution, beneficiary matching, outreach, fee agreement, representation or claim activity was performed.
