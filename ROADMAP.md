# ROADMAP.md

Last updated: 2026-09-24

## Product validation critical path

ONE AUTHORIZED REAL SOURCE
-> ONE TARGETABLE BOUNDED CASE
-> ONE REVIEWABLE ECONOMIC RESULT

No broad scale build is scheduled before this path is economically validated.

## Stage 1 — Real-source evidence — COMPLETED

NY OSC Attempt 11 proved:

- 14,994,489 physical records;
- 2,792,990 authority-backed insurance records;
- 203,921 primary IN03 aggregate candidates;
- bounded real-source processing;
- no owner/raw values returned;
- recoverable value UNKNOWN_FROM_SOURCE.

All Attempt-11 grants are consumed/non-reusable/zero-retry.

## Stage 2 — Stage A synthetic materialization — COMPLETED / MERGED

Action:

IMPLEMENT_AND_REVIEW_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION

PR #34 — MERGED

Merge commit:

9fc0c782ae575307be38c3f6b55b8f5ce477d372

Post-merge CI:

35920762625 — SUCCESS

Stage A proved one-candidate transient/economic instrumentation.

Its FIRST_ELIGIBLE_RECORD_IN_SOURCE_ORDER rule is retained only as synthetic technical proof.

## Stage 3 — Value proposition / targetability reframe — IMPLEMENTED AND VERIFIED ON FEATURE BRANCH

Branch:

mvp1-targetable-opportunity-reframe

Strategic change:

The product no longer treats candidate discovery alone as the commercial proposition.

Target thesis:

MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE

New proposed real-P1 selection:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Holder Report Year is persistence evidence only, not a value or awareness signal.

Decision:

D-012

Canonical strategy candidate:

PRODUCT_STRATEGY_MVP1.md v3.0

## Stage 4 — Synthetic Targetable Opportunity Filter V1 — VERIFIED

Implementation:

src/unclaimed_platform/domain/ny_mvp1_targetable_opportunity.py

Contract:

schemas/common/ny_mvp1_targetable_opportunity_filter.schema.json

Tests:

- tests/unit/test_ny_mvp1_targetable_opportunity.py
- tests/contract/test_ny_mvp1_targetable_opportunity_contract.py

Targetability classes:

- T0_SELF_SERVICE_LIKELY
- T1_UNRESOLVED_BUT_LOCATABLE
- T2_ESTATE_OR_REPRESENTATIVE_PATH
- T3_HARD_BUT_BOUNDED
- T4_UNBOUNDED_OR_UNRESOLVED_STOP

No numeric targetability score.

F0-F3 remain friction-only.

New primary P1 metric:

TARGETABILITY_DECISION_COST

PRE_VALUE_DISCOVERY_COST remains the umbrella cost metric.

Verified checkpoint:

89a3fcc0528571e465f73b94552165d3ccea14e6

CI:

35993271424 — SUCCESS

## Stage 5 — Human review / integration — NEXT

Execute only:

HUMAN_REVIEW_TARGETABLE_OPPORTUNITY_REFRAME_AND_SYNTHETIC_FILTER_V1

Review questions:

1. Is the updated value proposition accepted?
2. Is persistence-first selection accepted for P1?
3. Are T0-T4 accepted as the targetability vocabulary?
4. Is the separation F0-F3 friction versus T0-T4 targeting accepted?
5. Is TARGETABILITY_DECISION_COST accepted as the primary P1 sub-metric?
6. Is L1 new external cash spend = USD 0.00 accepted?
7. Is L2 budget correctly left unset pending Product Owner decision?
8. Should the feature branch be merged into main?

No real-source action is included in this stage.

## Stage 6 — Fresh real P1 targetability scope — NOT STARTED

Only after Stage 5 acceptance/integration.

Future action:

DEFINE_FRESH_REAL_P1_TARGETABILITY_EXECUTION_SCOPE

Must define:

- exact transient PII fields;
- durable non-PII ledger fields;
- retention/disposal;
- lawful/privacy scope;
- one-candidate selection execution mechanics;
- fresh single-use approvals;
- L2 incremental budget;
- third-party API/data policy;
- stop conditions;
- outreach separation.

No previous approval may be reused.

## Stage 7 — Pilot P1 one real case — NOT AUTHORIZED

Question:

Can one case be shown to have material service need and bounded resolvability at low enough evidenced cost to justify the next authorization before recoverable value is known?

P1 does not require recovery.

Valid terminal outcomes include:

- TARGETABLE_CONTINUE_TO_SEPARATE_OUTREACH_REVIEW
- STOP_SELF_SERVICE_LOW_NEED
- STOP_UNBOUNDED_RESOLUTION_COST
- STOP_LEGAL_PRIVACY_SCOPE
- STOP_TARGETABILITY_NOT_ESTABLISHED_WITHIN_BUDGET

## Stage 8 — Pilot P2 ~5 cases — CONDITIONAL

Only after P1 review.

Management-learning batch, not statistical sample.

Do not simply take next source rows.

Test variation in:

- persistence;
- targetability class;
- friction lane;
- estate/non-estate path where evidenced;
- targetability decision cost.

## Stage 9 — Pilot P3 ~20–30 cases — CONDITIONAL

Only if P2 supports continuation.

Measure an initial empirical distribution of:

- targetable-opportunity rate;
- service need;
- resolvability;
- targetability decision cost;
- contactability;
- outreach conversion;
- value-known rate;
- recovery/fee economics.

No claim of statistical representativeness from sample size alone.

## Frozen backlog before evidence justifies it

Freeze by default:

- broad multi-state expansion;
- generic agent-framework expansion;
- graph infrastructure;
- generalized genealogy infrastructure;
- mass outreach automation;
- large durable PII architecture;
- non-critical UI polish;
- parser/source diagnostics without a demonstrated blocker.

## Git health

Canonical main remains unchanged by this branch until Product Owner explicitly approves integration.

Verified main baseline before this work:

23de3a6ef5f1d6335691e17206285b4ec5f923af
