# HANDOVER_CURRENT.md

Last updated: 2026-09-23

## AUTHORITATIVE CURRENT STATE — PRODUCT VALIDATION / ECONOMIC DISCOVERY MODE

Repository:

`pierluigiavvanzo-creator/unclaimed-platform`

Canonical integration branch:

`main`

Current canonical `main` HEAD:

`9fc0c782ae575307be38c3f6b55b8f5ce477d372`

Current product objective:

`ONE AUTHORIZED REAL SOURCE -> ONE BOUNDED VERTICAL SLICE -> ONE REVIEWABLE ECONOMIC RESULT`

Primary economic rule:

`BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE`

Strategic metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

Do not optimize architecture, diagnostics, agents, parsers or governance as ends in themselves.

## Canonical operating constraints

- GitHub is the source of truth.
- Do not invent data, sources, APIs, legal conclusions, economic values or probabilities.
- Repository-first / reuse-first.
- Deterministic core.
- Fail closed on ambiguity, missing authorization or missing evidence.
- Every implementation requires tests.
- Human approval gates remain mandatory for privacy, PII, real-source execution, outreach, fee/representation and claim activity.
- No Work or Codex for this project.
- Commit/push/merge decisions remain human-controlled.
- User is Product Owner, not debugger or QA operator.

## Real-source status already established

NY OSC Owner Name File remains the active real-source candidate.

Attempt 11 completed the bounded aggregate product slice.

Authoritative aggregate result:

- total physical records: `14,994,489`;
- structurally conforming: `14,994,477`;
- structurally deferred: `12`;
- authority-backed insurance: `2,792,990`;
- primary `IN03` aggregate candidates: `203,921`;
- other insurance: `2,589,069`;
- no authority-backed insurance match: `12,201,486`;
- unclassifiable Property Type Code: `1`;
- candidate outcome: `CANDIDATES_PRESENT_AGGREGATE_ONLY`;
- candidate materialization: `NOT_AUTHORIZED_AGGREGATE_ONLY`;
- recoverable value: `UNKNOWN_FROM_SOURCE`;
- economic actionability: `VALUE_EVIDENCE_REQUIRED`.

No owner/raw values were returned by the aggregate execution.

All Attempt-11 execution/privacy approvals are consumed, non-reusable and zero-retry.

The local archive was logically deleted after execution. Physical secure erasure was not guaranteed.

## Economic feasibility conclusion

Whole-project economic audit status:

`CONDITIONAL_CONTINUE_ECONOMIC_VALIDATION_NOT_SCALE`

The project has proven candidate supply, but not yet unit economics.

Current downstream bottleneck:

`ONE LAWFULLY MATERIALIZED CANDIDATE -> VALUE/EVIDENCE -> CASE ECONOMICS -> REVIEWER DECISION`

No project-level ROI, CAC, LTV, expected recovery value or profitability forecast is authoritative yet.

## STAGE A — COMPLETED, MERGED, CI PASS

Stage A action:

`IMPLEMENT_AND_REVIEW_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION`

Purpose:

prove, with synthetic-only inputs, that one future real candidate can be processed through the economic instrumentation layer without persisting owner PII in the economic ledger.

Implementation branch:

`mvp1-ny-synthetic-one-candidate-transient-materialization`

Implementation commit:

`8910bb3cb38958d149c343bb8fdc5b02bba88ba4`

Pull request:

`#34 — MERGED`

Merge commit:

`9fc0c782ae575307be38c3f6b55b8f5ce477d372`

Pre-merge PR CI:

`35920078741 — SUCCESS`

Post-merge `main` CI:

`35920762625 — SUCCESS`

Stage A changed exactly five files:

1. `src/unclaimed_platform/domain/ny_osc_one_candidate_transient_materialization.py`
2. `schemas/common/ny_osc_synthetic_one_candidate_transient_materialization.schema.json`
3. `tests/unit/test_ny_osc_one_candidate_transient_materialization.py`
4. `tests/contract/test_ny_osc_synthetic_one_candidate_transient_materialization.py`
5. `docs/audits/NY_OSC_SYNTHETIC_ONE_CANDIDATE_TRANSIENT_MATERIALIZATION_REVIEW.md`

Stage A now provides tested interfaces/contracts for:

- deterministic first-eligible-candidate selection in source order;
- non-PII case ID derivation;
- friction lanes `F0/F1/F2/F3`;
- lane-change provenance;
- Economic Case Ledger;
- Economic Discovery Ladder state;
- `PRE_VALUE_DISCOVERY_COST`;
- measured machine/data/human-time components;
- explicit Product Owner incremental stage budget;
- bounded stop reasons;
- value-evidence state;
- reuse hooks for follow-up-cost, value-evidence and explicit case-economics components.

Stage A remained synthetic-only.

It did NOT authorize or perform:

- source access;
- remote preflight;
- download;
- real candidate materialization;
- owner PII processing;
- identity resolution;
- beneficiary matching;
- address enrichment;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

## Friction lanes

Lane assignment measures process friction, not value.

Never infer:

`F3 = HIGH VALUE`

or:

`F0 = LOW VALUE`

Allowed interpretation only:

`F3 = HIGHER OBSERVED PROCESS FRICTION`

`F0 = LOWER OBSERVED PROCESS FRICTION`

### F0 — Easy / self-service dominant

Economic posture:

`MINIMUM_OR_ZERO_INCREMENTAL_SPEND`

Do not perform expensive research merely to rescue an easy case.

### F1 — Identifiable / assistance case

Economic posture:

`LOW_TOUCH / AUTOMATION_FIRST`

Measure whether a low-cost assistance workflow can create enough convenience to justify payment despite the free State route.

### F2 — Hard to identify / hard to contact

Economic posture:

`BOUNDED_RESEARCH_WITH_STOP_LOSS`

Every F2 case must carry:

- current discovery stage;
- accumulated pre-value discovery cost;
- next information objective;
- Product Owner-approved incremental budget;
- explicit stop reason.

### F3 — Estate / deceased owner / complex documentation

Economic posture:

`PREMIUM_COMPLEX_CASE / HUMAN_OR_PROFESSIONAL_SUPPORT`

Measure actual legal/professional/documentation burden.

Do not assume that legal-fee sharing is lawful or economically available without specialized legal review.

## Economic Case Ledger

Every future real candidate experiment must produce one non-PII Economic Case Ledger keyed by `case_id`.

The ledger must not become a parallel owner-PII database.

Minimum categories:

### Provenance

- case ID;
- source ID;
- source snapshot/acquisition evidence;
- deterministic selection-rule version;
- physical source ordinal or other approved non-owner pointer;
- lane assignment and lane-change evidence;
- economic-stage timestamps.

### Measured costs

Record actual evidence-backed amounts only:

- compute/tool cost;
- data/API cost;
- human review time;
- manual research time;
- contact-channel cost;
- document/notary cost;
- professional/legal/external cost;
- fee-collection cost;
- other evidenced direct case cost.

Human labor cost may be computed only when a documented labor-rate evidence ref exists.

### Funnel events

Record evidence-backed state for:

- candidate selected;
- identity work;
- identity established;
- contactability;
- contact attempts;
- contact success;
- agreement offered/signed;
- value known;
- recovery started/succeeded;
- fee billed/collected;
- stop/pause reason.

### Time

Derive, when evidence exists:

- time to identifiable;
- time to contactable;
- time to contact;
- time to agreement;
- time to value known;
- time to recovery;
- time to fee collection.

Primary collected-cash metric:

`DAYS_TO_CASH = fee_collected_at - candidate_selected_at`

## PRE_VALUE_DISCOVERY_COST

Definition:

`PRE_VALUE_DISCOVERY_COST` is the fully evidenced cost accumulated before the platform knows enough about case value to make a rational continue/stop decision.

It is the principal economic-discovery metric for the current MVP phase.

Required states:

- `NOT_STARTED`;
- `MEASURING`;
- `VALUE_KNOWN`;
- `VALUE_STILL_UNKNOWN_STOPPED`;
- `VALUE_REQUIRES_UNAUTHORIZED_SCOPE`.

Core optimization target:

`COST_TO_LEARN_IF_THE_CANDIDATE_IS WORTH FURTHER SPEND`

not merely:

`COST_PER_CANDIDATE`.

No arbitrary fixed dollar stop-loss threshold is currently evidence-backed.

Every real discovery stage must therefore receive an explicit bounded incremental budget from the Product Owner.

## Economic Discovery Ladder

### L0 — Source-only qualification

Use non-PII / already-authorized classification evidence.

Goal:

determine deterministic eligibility and initial friction lane.

### L1 — Transient one-candidate materialization

Stage A proved the required synthetic contracts.

Real L1 execution remains NOT authorized.

Goal of a future authorized real L1 execution:

materialize exactly one approved candidate transiently and confirm minimum case structure while measuring machine/operator/transient-processing cost.

No durable owner PII, address enrichment, identity work, outreach or value research.

### L2 — Minimal identity/contactability discovery

Requires a separate legal/privacy authorization.

Question to answer:

`CAN THIS OWNER / AUTHORIZED REPRESENTATIVE BE IDENTIFIED AND CONTACTED AT ACCEPTABLE COST?`

No broad genealogy or unbounded manual research.

### L3 — Minimal contact/service-fit discovery

Requires separate outreach authorization.

Measure:

- actual contactability;
- response;
- willingness to engage;
- agreement conversion;
- incremental channel/human cost.

### L4 — Value-evidence discovery

Goal:

obtain evidence-backed recoverable value when lawfully possible, or establish why value remains unavailable.

Allowed terminal states include:

- `VALUE_EVIDENCE_OBTAINED`;
- `UNKNOWN_PRE_CLAIM_REVIEW`;
- `STOP_PRIVACY_SCOPE_INSUFFICIENT`;
- `STOP_REQUIRES_CLAIM_IDENTITY_OR_LEGAL_ACTION`;
- `STOP_PRE_VALUE_DISCOVERY_COST_TOO_HIGH`.

No value may be invented.

### L5 — Explicit case economics

Only when value, fee and fully loaded case-cost evidence exist.

Then compute:

`GROSS_FEE = RECOVERED_VALUE x REALIZED_FEE_RATE`

`CONTRIBUTION_BEFORE_OVERHEAD = GROSS_FEE - FULLY_LOADED_CASE_COST`

The Product Owner decides `GO / REVISE / STOP`.

The software must not silently turn arithmetic into an automatic business decision.

## Stage B / Pilot sequence

Stage B is the next economic-validation phase, but it has NOT started.

Its governing question is:

> Can we obtain useful economic evidence and measure the case cost before the cost of research makes the model irrational?

### Pilot P1 — one real candidate

Purpose:

prove the economic-discovery process end to end and identify the exact point where value, privacy and cost become binding.

P1 success is not necessarily a recovery.

A valid outcome may be:

`STOP — PRE_VALUE_DISCOVERY_COST OR REQUIRED_SCOPE MAKES CASE IRRATIONAL`

### Pilot P2 — approximately five bounded cases

Only after P1 review.

Purpose:

identify repeated failure modes, lane differences, cost concentration and safe automation opportunities.

Five is a management-learning batch, not a statistically validated sample size.

### Pilot P3 — approximately 20–30 bounded cases

Only if P2 supports continuation.

Purpose:

obtain an initial empirical distribution for cost, time, conversion and value-known outcomes sufficient for a Product Owner scale/pivot decision.

Twenty to thirty is a management gate, not a claim of statistical representativeness.

## Pivot framework

### Scenario A

Low discovery cost + positive real contribution.

Action:

`CONTINUE_DIRECT_OWNER_LOCATION_SERVICE`

### Scenario B

Direct-owner economics weak/volatile, but professionals show willingness to pay for the tooling.

Action:

`PIVOT_OR_ADD_B2B_SOFTWARE_SERVICE_MODEL`

Do not build B2B features before willingness-to-pay evidence exists.

### Scenario C

Complex F3 cases appear attractive but legal/professional cost dominates.

Action:

`RESTRUCTURE_PARTNERSHIP_AND_PRICING_BEFORE_SCALE`

Do not assume revenue sharing with lawyers is available.

### Scenario D

Discovery cost repeatedly high + value arrives too late + no professional willingness to pay.

Action:

`FREEZE_OR_STOP_NY_DIRECT_MODEL`

Do not respond by adding architecture.

## Governance-to-economics rule

Additional governance is justified only when required to:

- lawfully run the next economic experiment;
- protect PII/security;
- preserve reproducibility/provenance;
- solve a demonstrated economic bottleneck.

Freeze by default:

- generic new agent frameworks;
- broad multi-state expansion;
- graph infrastructure;
- generalized genealogy infrastructure;
- mass outreach automation;
- large durable PII architecture;
- non-critical UI polish;
- parser work without a real blocker.

Planning heuristic during economic validation:

approximately `70–80%` of effort toward economic evidence and approximately `20%` toward the minimum legal/privacy/governance needed to obtain it safely.

This is a Product Owner planning heuristic, not an externally validated economic constant.

## SINGLE NEXT ACTION

Stage A is complete and merged.

Do NOT execute a real candidate yet.

Execute only:

`DEFINE_AND_REVIEW_MINIMUM_LEGAL_PRIVACY_SCOPE_FOR_PILOT_P1`

Purpose:

define the smallest lawful/privacy-safe authorization envelope required to obtain the next unit of economic information from exactly one real candidate.

The review must determine, before any real execution:

1. which real candidate fields may be transiently materialized at L1;
2. which fields, if any, may be persisted and why;
3. retention/disposal requirements;
4. minimum lawful basis and privacy constraints for L1;
5. whether L2 identity/contactability work is permissible and under what separately approved scope;
6. whether any third-party data/API use is required and under what evidence/cost controls;
7. whether outreach remains separately gated;
8. exact Product Owner incremental budget required for the first real discovery step;
9. exact stop conditions;
10. which approvals are single-use/non-reusable;
11. what evidence must be written to the Economic Case Ledger without owner PII.

The review must remain offline/design-only.

It must NOT authorize or perform:

- source access;
- remote preflight;
- download;
- real candidate materialization;
- owner PII processing;
- identity resolution;
- address enrichment;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

After this review, the next human decision will be whether the expected information gain justifies authorizing the minimum real Pilot P1 scope.

## Git health

Canonical integration branch:

`main`

Current `main` HEAD:

`9fc0c782ae575307be38c3f6b55b8f5ce477d372`

Economic-feasibility audit:

`PR #33 — MERGED`

Synthetic one-candidate Stage A:

`PR #34 — MERGED`

Stage A merge commit:

`9fc0c782ae575307be38c3f6b55b8f5ce477d372`

Post-merge CI:

`35920762625 — SUCCESS`

No real-case Pilot P1 authorization is currently active.

No previous real-source execution/privacy grant may be reused.

## Context continuity rule

This handover is intended to be the clean starting point for the next chat.

Before the next task, read in order:

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then verify the remote `main` HEAD before any change.

The next chat should execute only the SINGLE NEXT ACTION above unless the Product Owner explicitly changes direction.
