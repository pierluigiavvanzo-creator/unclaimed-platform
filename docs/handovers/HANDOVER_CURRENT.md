# HANDOVER_CURRENT.md

Last updated: 2026-09-24

## AUTHORITATIVE CURRENT STATE — PRODUCT VALIDATION / TARGETABILITY DISCOVERY MODE

Repository:

pierluigiavvanzo-creator/unclaimed-platform

Canonical integration branch:

main

Verified main HEAD before this work:

23de3a6ef5f1d6335691e17206285b4ec5f923af

Active feature branch:

mvp1-targetable-opportunity-reframe

Main has NOT been changed by this work.

## Product objective

ONE AUTHORIZED REAL SOURCE
-> ONE TARGETABLE BOUNDED CASE
-> ONE REVIEWABLE ECONOMIC RESULT

Primary economic rule:

BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE

Strategic metric:

ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME

## Updated value proposition

The product is not a paid shortcut to a free OSC claim.

The value proposition to validate is:

Find unresolved insurance-beneficiary opportunities that the rightful person or authorized representative may not be effectively resolving through ordinary processes, determine whether the case is practically resolvable at bounded cost, and provide compliant discovery/location/recovery assistance where that assistance creates real value.

The owner/authorized representative must never be led to believe that payment is required to obtain New York State unclaimed funds.

## Why this reframe was required

Facts already established:

- NY OSC direct claim processing is free.
- New York recognizes Abandoned Property Location Service Providers.
- The applicable provider fee is capped by law at 15 percent; this is a ceiling, not an assumed realized fee.
- The Owner Name File does not disclose recoverable amount.
- 2026 expedited payment covers qualifying simple cases up to USD 5,000.
- Estate claims do not qualify for the expedited program.
- Deceased-owner/estate claims can require entitlement and court/representative documentation.

Therefore candidate volume alone is not the business.

The commercially interesting hypothesis is:

MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE

not:

DIFFICULT CASE = HIGH VALUE

and not:

IN03 = PROFITABLE CASE.

## Real-source evidence already established

Attempt 11 completed the bounded aggregate product slice.

Authoritative aggregate result:

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

Stage A remains valid as technical evidence.

Important reinterpretation:

FIRST_ELIGIBLE_RECORD_IN_SOURCE_ORDER was a synthetic determinism test and is NOT the proposed future P1 economic-targeting rule.

## Product strategy v3

PRODUCT_STRATEGY_MVP1.md is updated to version 3.0 on the active branch.

Future P1 selection proposal:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Meaning:

use the oldest Holder Report Year among otherwise eligible records; source ordinal breaks ties.

Holder Report Year is only a persistence signal.

It does not prove:

- beneficiary awareness/unawareness;
- death;
- contactability;
- claim complexity;
- recoverable value;
- willingness to pay.

No fixed age threshold is invented.

## Targetability model

### Service need

SERVICE_NEED_STATE:

- UNKNOWN
- LOW_EVIDENCE
- MATERIAL_EVIDENCE

### Resolvability

RESOLVABILITY_STATE:

- UNKNOWN
- EASY
- BOUNDED
- UNBOUNDED

### Estate / representative

ESTATE_PATH_STATE:

- NOT_EVALUATED
- NO_EVIDENCE
- EVIDENCE_PRESENT

REPRESENTATIVE_PATH_STATE:

- NOT_EVALUATED
- IDENTIFIED
- BOUNDED_DISCOVERABLE
- NOT_BOUNDED

### Awareness

Before separate outreach authorization:

AWARENESS_STATE = UNKNOWN_UNTIL_OUTREACH

Do not label a beneficiary unaware before contact evidence exists.

## Targetability classes T0-T4

T0_SELF_SERVICE_LIKELY

Low service-need evidence + easy resolution. Low priority for paid direct-owner service. Not a low-value label.

T1_UNRESOLVED_BUT_LOCATABLE

Material service need + easy/low-cost resolvability. Core direct-service target hypothesis.

T2_ESTATE_OR_REPRESENTATIVE_PATH

Deceased/estate evidence + identified or bounded-discoverable representative path. Complex-service hypothesis, not a high-value label.

T3_HARD_BUT_BOUNDED

Material service need + harder identity/contactability + explicit bounded next step.

T4_UNBOUNDED_OR_UNRESOLVED_STOP

No bounded next step, unavailable legal/privacy scope or disproportionate cost. Stop rather than build more architecture.

If evidence is insufficient:

UNRESOLVED_REQUIRES_L2

No T class is fabricated.

## F0-F3 status

F0-F3 remain observed process-friction lanes only.

They are NOT:

- targetability classes;
- value predictions;
- ranking scores;
- automatic commercial decisions.

No automatic mapping exists between T0-T4 and F0-F3.

## Economic metric changes

PRE_VALUE_DISCOVERY_COST remains the umbrella metric.

New primary P1 sub-metric:

TARGETABILITY_DECISION_COST

Definition:

evidenced incremental cost to determine material service need and bounded resolvability before outreach/value research.

P1 optimization now begins with:

COST_TO_DETERMINE_SERVICE_NEED_AND_RESOLVABILITY

before spending to learn exact value.

L1 maximum new external cash spend:

USD 0.00

Paid APIs in L1:

NOT ALLOWED

Paid data purchase in L1:

NOT ALLOWED

L2 incremental budget:

UNSET_REQUIRES_PRODUCT_OWNER

No L2 spend is authorized.

## Synthetic Targetable Opportunity Filter V1

Implementation:

src/unclaimed_platform/domain/ny_mvp1_targetable_opportunity.py

Contract:

schemas/common/ny_mvp1_targetable_opportunity_filter.schema.json

Tests:

- tests/unit/test_ny_mvp1_targetable_opportunity.py
- tests/contract/test_ny_mvp1_targetable_opportunity_contract.py

Proposal:

sources/proposals/ny_mvp1_targetable_opportunity_filter.v1.json

Audit:

docs/audits/TARGETABLE_OPPORTUNITY_VALUE_PROPOSITION_REFRAME_2026-09-24.md

Review:

docs/audits/NY_MVP1_TARGETABLE_OPPORTUNITY_FILTER_REVIEW.md

Decision:

D-012

## Verification

Verified implementation checkpoint:

89a3fcc0528571e465f73b94552165d3ccea14e6

CI:

35993271424 — SUCCESS

Verified:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest suite;
- frontend lint;
- frontend typecheck;
- frontend build;
- Streamlit safety smoke;
- Streamlit startup smoke.

An initial full-pytest run failed only because unit and contract test modules had identical basenames.

Repair:

the contract test was renamed.

No product logic changed.

## Safety boundary

The entire new package is synthetic/offline only.

It does NOT authorize or perform:

- NY OSC access;
- remote preflight;
- download;
- real candidate materialization;
- owner PII processing;
- identity resolution;
- beneficiary matching;
- address enrichment;
- third-party API use;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

No previous real-source/privacy approval may be reused.

## Economic Discovery Ladder — current interpretation

L0 — SOURCE QUALIFICATION / TARGET SIGNAL

Exact eligibility + persistence signal only.

L1 — TRANSIENT ONE-CANDIDATE MATERIALIZATION

Minimum candidate structure + measured L1 cost. No identity/outreach/value work.

L2 — MINIMAL TARGETABILITY DISCOVERY

Question:

CAN THIS OWNER OR AUTHORIZED REPRESENTATIVE BE IDENTIFIED/CONTACTED AT BOUNDED COST, AND IS THERE MATERIAL SERVICE NEED?

Produces T0-T4 or unresolved state and TARGETABILITY_DECISION_COST.

L3 — OUTREACH / SERVICE FIT

Separate authorization. Awareness may become evidence-backed only here.

L4 — VALUE EVIDENCE

Evidence-backed value only; unknown remains explicit if unavailable.

L5 — EXPLICIT CASE ECONOMICS

Only after value, actual/agreed fee and fully loaded cost are evidenced.

## Pilot sequence

P1:

one targetability experiment.

Question:

Can we establish material service need and bounded resolvability cheaply enough to justify the next authorization before recoverable value is known?

P2:

approximately five deliberately varied cases only after P1 review.

Do not simply use the next five rows.

P3:

approximately 20–30 only if P2 supports continuation.

Management gates, not statistical guarantees.

## Current single next action

Execute only:

HUMAN_REVIEW_TARGETABLE_OPPORTUNITY_REFRAME_AND_SYNTHETIC_FILTER_V1

The Product Owner review should decide whether to accept:

1. value proposition v3;
2. persistence-first P1 selection;
3. T0-T4 vocabulary;
4. F0-F3 / T0-T4 separation;
5. TARGETABILITY_DECISION_COST;
6. L1 external cash spend ceiling USD 0.00;
7. L2 budget remaining unset;
8. integration of the active branch into main.

No real candidate execution is part of this review.

If approved and integrated, next separate action:

DEFINE_FRESH_REAL_P1_TARGETABILITY_EXECUTION_SCOPE

That future action must still define fresh single-use privacy/execution gates, exact PII scope, retention/disposal and any L2 incremental budget.

## Canonical read order

1. AGENTS.md
2. PRODUCT_STRATEGY_MVP1.md
3. PROJECT_STATE.md
4. ROADMAP.md
5. DECISIONS.md
6. docs/handovers/HANDOVER_CURRENT.md

Then verify remote main and active branch HEAD.

## Git status

Canonical main baseline before work:

23de3a6ef5f1d6335691e17206285b4ec5f923af

Active branch:

mvp1-targetable-opportunity-reframe

Verified implementation checkpoint:

89a3fcc0528571e465f73b94552165d3ccea14e6

Verified CI:

35993271424 — SUCCESS

Documentation commits after the verified implementation checkpoint may advance the feature-branch HEAD; verify latest branch HEAD and CI before integration.

COMMIT/PUSH:

Feature-branch commits have been created through the authorized GitHub connector work.

MERGE:

NOT EXECUTED.

Main remains unchanged.
