# PROJECT_STATE.md

Last updated: 2026-09-18

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ny-follow-up-cost-measurement-offline`

Latest verified product implementation checkpoint:

`e9c1bc0e310f1b7b65f4153c90d5efb5d812caa0`

Product implementation CI:

`35321285527` — SUCCESS.

Classification: `A — Product Critical`.

Current lifecycle has two bounded tracks:

`NY_REQUEST_SUBMITTED_GATE1_CONSUMED -> AWAITING_NY_OSC_ACCESS_INSTRUCTIONS`

and, while that external dependency is pending:

`SYNTHETIC_DOWNSTREAM_SLICE_VERIFIED -> NY_VALUE_EVIDENCE_VISIBLE_IN_REVIEWER -> FOLLOW_UP_COST_MEASUREMENT_CONTRACT_VERIFIED`

## California State

Latest bounded California live run:

`35255228459` — attempt `1` — SUCCESS.

Observed:

- source bytes: `524288`;
- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`.

California remains `HELD / NOT YET APPROVED`, not rejected. The current California SCO `PROPERTY_TYPE` path is frozen for MVP-1 absent genuinely new evidence.

## New York OSC Owner Name File

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

Registry/source state:

- registered: yes;
- enabled: false;
- approved for use: false;
- acquired: false;
- physical schema: `UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE`;
- production parser/classification: inactive.

Primary MVP-1 authority target:

`IN03 — Proceeds Due Beneficiaries`

## NY Authorization / Privacy State

### Gate 1 — request access only

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

State:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

The Product Owner confirmed manual submission of the official request once on 2026-09-17. Repository tooling did not independently verify the external submit. Requester contact values are intentionally not persisted.

Access instructions received: no as of the latest Gmail check on 2026-09-18.

### Gate 2 — first bounded download / transient PII

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

State:

`NOT GRANTED / NOT READY`

Before Gate 2:

1. receive OSC access instructions;
2. observe non-content access/download constraints;
3. define explicit `max_download_bytes`;
4. separately review/authorize one bounded first download and memory-only schema discovery.

No Owner Name File download, real owner PII processing, raw persistence, identity resolution, beneficiary matching, outreach, representation, fee agreement or claim activity is currently authorized.

## Offline MVP-1 Downstream Slice

Integrated onto the current NY branch from the already verified reusable branch rather than rewritten.

Path:

`SYNTHETIC_POST_SCHEMA_MAPPING -> exact NY insurance classification -> IN03 candidate -> economics -> reviewer`

Integration checkpoint:

`75156c5419616b67eff658c8c3c8d6775849546c`

CI:

`35317313977` — SUCCESS.

Verified behavior:

- exact `IN03` -> primary MVP-1 insurance classification;
- other exact recorded NY insurance codes -> insurance/non-primary;
- unknown codes are not promoted by normalization or inference;
- only exact `IN03` creates the narrow synthetic candidate;
- deterministic case id;
- no identity resolution or beneficiary matching;
- no real source or PII access;
- reviewer API and Streamlit surface exercised.

Audit:

`docs/audits/MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE.md`

## NY MVP-1 Economics Evidence

Official-source benchmark:

`docs/audits/NY_MVP1_RECOVERABLE_VALUE_EVIDENCE_BENCHMARK_OFFLINE.md`

Current fail-closed product facts:

- Owner Name File does not provide the exact recoverable dollar amount;
- exact recoverable value remains `UNKNOWN_PRE_CLAIM_REVIEW`;
- the 15% figure is represented only as the statutory cap for the scoped APL §1416 location-service rule, subject to legal applicability/exceptions;
- actual fee rate remains unsupported until explicit evidence exists;
- expected follow-up cost remains `NOT_MEASURED`;
- commercial actionability remains `NOT_COMPUTABLE_PRE_CONTACT`;
- no commercial threshold or case value is invented.

Implemented contracts:

- `schemas/economics/ny_mvp1_precontact_evidence.schema.json`;
- `schemas/economics/ny_mvp1_explicit_case_economics_input.schema.json`;
- `schemas/economics/ny_mvp1_explicit_case_economics_result.schema.json`;
- `src/unclaimed_platform/domain/ny_mvp1_value_evidence.py`.

Explicit later arithmetic accepts evidence-backed integer cents and basis points only. It makes no automatic continue/stop recommendation.

Reviewer integration:

- `GET /api/reviewer/mvp1/economics/precontact`;
- fail-closed Streamlit adapter;
- Streamlit `NY PRE-CONTACT ECONOMICS` card.

Latest cumulative CI:

`35318092067` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety smoke;
- Streamlit startup smoke;
- frontend lint;
- frontend typecheck;
- frontend build.

One prior CI `35317731747` failed only because a unit test and contract test shared the same Python module basename. The contract test was renamed; no product logic changed. Repair CI `35317814189` was SUCCESS.

## NY MVP-1 Follow-Up Cost Measurement

Completed offline:

`IMPLEMENT_NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE`

Verified checkpoint:

`e9c1bc0e310f1b7b65f4153c90d5efb5d812caa0`

CI:

`35321285527` — SUCCESS.

Implemented measured dimensions:

- automated processing cost per candidate in integer cents;
- source/data cost per candidate in integer cents;
- human review time per candidate in integer seconds;
- additional manual research time per candidate in integer seconds.

Every measured component requires an evidence reference and observation timestamp. No default monetary or time assumption is supplied.

Human time is not converted into money unless an explicit documented labor rate is provided. Without that rate, fully loaded follow-up cost remains `NOT_COMPUTABLE_NO_LABOR_RATE`.

Implemented:

- `src/unclaimed_platform/domain/ny_mvp1_follow_up_cost.py`;
- `schemas/economics/ny_mvp1_follow_up_cost_measurement_input.schema.json`;
- `schemas/economics/ny_mvp1_follow_up_cost_measurement_result.schema.json`;
- unit and contract tests;
- `docs/audits/NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE.md`.

The contract requires `owner_pii_included = false` and returns `no_commercial_recommendation = true`.

Three early CI runs stopped on test-file lint/syntax only. After two corrective patches, the mandatory root-cause audit identified a connector escape-sequence serialization defect in the test edit. The audited repair is recorded in:

`docs/audits/NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_RUFF_ROOT_CAUSE.md`

No domain logic or schema semantics changed in that repair.

## Current Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- NY source: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: `CONSUMED / NON-REUSABLE`;
- NY access instructions: pending;
- NY Gate 2: not granted;
- real owner PII processed: no;
- synthetic IN03 classification-to-reviewer path: `READY / VERIFIED`;
- NY pre-contact economics evidence contract: `READY / VERIFIED`;
- follow-up cost measurement contract: `READY / VERIFIED`;
- real measured candidate costs: `0`;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`INTEGRATE_NY_MVP1_FOLLOW_UP_COST_WITH_CASE_ECONOMICS_OFFLINE`

Classification: `A — Product Critical`.

Goal:

Connect the verified follow-up-cost measurement result to the existing explicit case-economics input without inventing values. A fully loaded measured cost may populate `measured_follow_up_cost_cents` only when the measurement state is `COMPUTED_FROM_MEASURED_COMPONENTS`; otherwise the integration must fail closed and preserve the cost as unavailable.

Use synthetic/test inputs only. Do not access the Owner Name File, process real owner PII, create fee agreements, perform outreach or submit claims.
