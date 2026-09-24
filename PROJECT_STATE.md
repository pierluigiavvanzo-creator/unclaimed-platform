# PROJECT_STATE.md

Last updated: 2026-09-24

## Authoritative product state

The project is in PRODUCT VALIDATION / TARGETABILITY DISCOVERY MODE.

Primary objective:

ONE AUTHORIZED REAL SOURCE -> ONE TARGETABLE BOUNDED CASE -> ONE REVIEWABLE ECONOMIC RESULT

Primary economic rule:

BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE

Guiding metric:

ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME

## Canonical integration branch

main

Verified remote main HEAD before this work:

23de3a6ef5f1d6335691e17206285b4ec5f923af

PR #35 is merged.

The current work is isolated on:

mvp1-targetable-opportunity-reframe

No merge to main has been executed.

## Real-source evidence already established

NY OSC Attempt 11 completed one bounded aggregate real-source product slice.

Authoritative result:

sources/evidence/ny_osc_owner_name_file_eleventh_attempt_execution_result.v1.json

Observed:

- total physical records: 14,994,489;
- structurally conforming: 14,994,477;
- structurally deferred: 12;
- authority-backed insurance: 2,792,990;
- primary IN03 aggregate candidates: 203,921;
- candidate materialization: NOT_AUTHORIZED_AGGREGATE_ONLY;
- recoverable value: UNKNOWN_FROM_SOURCE.

No owner/raw values were returned.

All Attempt-11 execution/privacy approvals are consumed, non-reusable and zero-retry.

## Stage A — completed and merged

Action:

IMPLEMENT_AND_REVIEW_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION

PR #34 — MERGED

Merge commit:

9fc0c782ae575307be38c3f6b55b8f5ce477d372

Post-merge CI:

35920762625 — SUCCESS

Stage A proved synthetic transient materialization and economic instrumentation.

Stage A used FIRST_ELIGIBLE_RECORD_IN_SOURCE_ORDER only to prove deterministic technical behavior.

It remains historical/technical evidence and is no longer the proposed economic-targeting rule for future real P1.

## Product-value reframe — 2026-09-24

Product Owner direction:

Do not target candidates merely because IN03 exists or because a case appears difficult.

Target the subset where the service can create material value despite the free OSC claim path:

MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE

Updated value proposition:

Find unresolved insurance-beneficiary opportunities that the rightful person or authorized representative may not be effectively resolving through ordinary processes, determine whether the case is practically resolvable at bounded cost, and provide compliant discovery/location/recovery assistance where that assistance creates real value.

The product must never imply that a customer must pay to obtain funds from OSC.

## D-012 — targetable opportunity policy

Accepted on the active branch.

Future P1 proposed selection rule:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Holder Report Year is a persistence signal only.

It is not evidence of:

- monetary value;
- awareness;
- death;
- contactability;
- willingness to pay.

No fixed age threshold is invented.

## Targetability parameters

SERVICE_NEED_STATE:

- UNKNOWN
- LOW_EVIDENCE
- MATERIAL_EVIDENCE

RESOLVABILITY_STATE:

- UNKNOWN
- EASY
- BOUNDED
- UNBOUNDED

ESTATE_PATH_STATE:

- NOT_EVALUATED
- NO_EVIDENCE
- EVIDENCE_PRESENT

REPRESENTATIVE_PATH_STATE:

- NOT_EVALUATED
- IDENTIFIED
- BOUNDED_DISCOVERABLE
- NOT_BOUNDED

AWARENESS_STATE before outreach:

UNKNOWN_UNTIL_OUTREACH

Targetability classes:

- T0_SELF_SERVICE_LIKELY
- T1_UNRESOLVED_BUT_LOCATABLE
- T2_ESTATE_OR_REPRESENTATIVE_PATH
- T3_HARD_BUT_BOUNDED
- T4_UNBOUNDED_OR_UNRESOLVED_STOP

Insufficient evidence:

UNRESOLVED_REQUIRES_L2

No numeric targetability score is allowed in v1.

## Friction lanes

F0-F3 remain backward-compatible process-friction observations only.

They are not:

- value scores;
- targetability scores;
- ranking scores;
- automatic commercial decisions.

No automatic mapping exists between F0-F3 and T0-T4.

## Economic parameters

PRE_VALUE_DISCOVERY_COST remains the umbrella metric.

New primary P1 sub-metric:

TARGETABILITY_DECISION_COST

Definition:

the evidenced incremental cost required to determine whether the case has material service need and bounded resolvability before outreach/value research.

L1 maximum new external cash spend:

USD 0.00

L1 paid API calls:

NOT ALLOWED

L1 paid data purchases:

NOT ALLOWED

L2 incremental budget:

UNSET_REQUIRES_PRODUCT_OWNER

## Synthetic Targetable Opportunity Filter V1 — VERIFIED

Implementation:

src/unclaimed_platform/domain/ny_mvp1_targetable_opportunity.py

Machine contract:

schemas/common/ny_mvp1_targetable_opportunity_filter.schema.json

Tests:

tests/unit/test_ny_mvp1_targetable_opportunity.py

tests/contract/test_ny_mvp1_targetable_opportunity_contract.py

Proposal:

sources/proposals/ny_mvp1_targetable_opportunity_filter.v1.json

Strategy/audits:

- PRODUCT_STRATEGY_MVP1.md v3.0
- docs/audits/TARGETABLE_OPPORTUNITY_VALUE_PROPOSITION_REFRAME_2026-09-24.md
- docs/audits/NY_MVP1_TARGETABLE_OPPORTUNITY_FILTER_REVIEW.md

Verified implementation checkpoint:

89a3fcc0528571e465f73b94552165d3ccea14e6

CI:

35993271424 — SUCCESS

Verified:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety/startup;
- frontend lint;
- frontend typecheck;
- frontend build.

Initial CI defect:

pytest import collision caused by identical unit/contract test basenames.

Repair:

contract test renamed.

No product logic changed.

## Safety / authorization state

The targetability implementation is synthetic-only.

It does NOT authorize or perform:

- source access;
- remote preflight;
- download;
- real candidate materialization;
- real owner PII processing;
- identity resolution;
- beneficiary matching;
- address enrichment;
- third-party API use;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

No previous real-source/privacy authorization may be reused.

## Current blocker

The technical targetability model is verified synthetically.

The remaining blocker to real P1 is human/legal/privacy authorization for a strictly bounded real experiment.

L2 identity/contactability spend is not authorized and has no budget yet.

## Current next action

Execute only:

HUMAN_REVIEW_TARGETABLE_OPPORTUNITY_REFRAME_AND_SYNTHETIC_FILTER_V1

If accepted, merge/integrate this branch only with explicit Product Owner authorization.

After integration, the next separate design gate will be:

DEFINE_FRESH_REAL_P1_TARGETABILITY_EXECUTION_SCOPE

That later gate must establish the exact PII envelope, retention/disposal, single-use approvals and Product Owner L2 incremental budget before any real candidate is processed.
