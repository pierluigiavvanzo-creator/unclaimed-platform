# NY MVP-1 TARGETABLE OPPORTUNITY FILTER V1 — REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Result: PASS_SYNTHETIC_ONLY_REAL_P1_NOT_AUTHORIZED

## Objective

Replace first-source-order economic targeting with a tested synthetic targetability layer that distinguishes:

SERVICE NEED x RESOLVABILITY

without predicting recoverable value.

## Strategic result

The updated MVP-1 value proposition is:

Find unresolved insurance-beneficiary opportunities that the rightful person or authorized representative may not be effectively resolving through ordinary processes, determine whether the case is practically resolvable at bounded cost, and provide compliant discovery/location/recovery assistance where that assistance creates real value.

The free OSC claim path remains explicit. The product does not claim privileged access to funds.

## Implemented parameters

Future real P1 selection policy:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Guardrails:

- Holder Report Year is persistence evidence only;
- no fixed age threshold;
- no owner-PII-based ranking;
- no value prediction;
- no random selection.

Targetability evidence states:

- SERVICE_NEED_STATE;
- RESOLVABILITY_STATE;
- ESTATE_PATH_STATE;
- REPRESENTATIVE_PATH_STATE;
- AWARENESS_STATE.

Targetability classes:

- T0_SELF_SERVICE_LIKELY;
- T1_UNRESOLVED_BUT_LOCATABLE;
- T2_ESTATE_OR_REPRESENTATIVE_PATH;
- T3_HARD_BUT_BOUNDED;
- T4_UNBOUNDED_OR_UNRESOLVED_STOP.

Insufficient evidence yields:

UNRESOLVED_REQUIRES_L2

and no fabricated T class.

F0-F3 remain process-friction observations only and are explicitly excluded from targeting/value scoring.

Numeric targetability scoring is disabled:

targetability_score = null

## Economic changes

PRE_VALUE_DISCOVERY_COST is retained.

New primary P1 sub-metric:

TARGETABILITY_DECISION_COST

L1 maximum new external cash spend:

USD 0.00

L1 paid APIs:

NOT ALLOWED

L1 paid data purchase:

NOT ALLOWED

L2 incremental budget:

UNSET_REQUIRES_PRODUCT_OWNER

## Implementation

New module:

src/unclaimed_platform/domain/ny_mvp1_targetable_opportunity.py

New machine contract:

schemas/common/ny_mvp1_targetable_opportunity_filter.schema.json

Tests:

tests/unit/test_ny_mvp1_targetable_opportunity.py

tests/contract/test_ny_mvp1_targetable_opportunity_contract.py

Proposal:

sources/proposals/ny_mvp1_targetable_opportunity_filter.v1.json

Strategy/audit:

PRODUCT_STRATEGY_MVP1.md v3.0

docs/audits/TARGETABLE_OPPORTUNITY_VALUE_PROPOSITION_REFRAME_2026-09-24.md

Decision:

D-012

## Defect found and repaired

The first full pytest run failed because the unit and contract test files had the same Python module basename.

Root cause:

pytest import-file collision, not targetability logic.

Repair:

renamed the contract test to:

test_ny_mvp1_targetable_opportunity_contract.py

No product logic changed.

## Verification

Verified branch checkpoint:

89a3fcc0528571e465f73b94552165d3ccea14e6

GitHub Actions:

35993271424 — SUCCESS

Verified:

- Ruff;
- mypy core/API/storage/UI;
- NY OSC runtime mypy gate;
- contract tests;
- smoke tests;
- full pytest suite;
- reviewer frontend lint;
- reviewer frontend typecheck;
- reviewer frontend build;
- Streamlit safety smoke;
- Streamlit startup smoke.

## Safety review

The implementation is synthetic-only.

It does not:

- access NY OSC;
- perform remote preflight;
- download data;
- materialize a real candidate;
- process real owner PII;
- perform identity resolution;
- perform address enrichment;
- use third-party APIs;
- perform outreach;
- research value;
- create fee agreements;
- perform representation;
- submit a claim.

authorization_granted remains false in the machine contract.

## Review conclusion

PASS_SYNTHETIC_ONLY_REAL_P1_NOT_AUTHORIZED

The filter is suitable for human review and integration into main as a product-strategy/synthetic-contract milestone.

A future real P1 still requires fresh legal/privacy review and separate single-use execution/privacy approvals.
