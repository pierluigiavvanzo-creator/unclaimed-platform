# PRODUCT_STRATEGY_MVP1.md

Version: 3.0
Date: 2026-09-24
Status: AUTHORITATIVE PRODUCT-VALIDATION PRIORITY
Owner: Product Owner

## 1. Strategic command

Until MVP-1 is validated, optimize for:

ONE AUTHORIZED REAL SOURCE
-> ONE TARGETABLE BOUNDED CASE
-> ONE REVIEWABLE ECONOMIC RESULT

Primary economic rule:

BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE

Guiding metric:

ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME

The project must not optimize code volume, agent count, architecture breadth, diagnostic depth or governance completeness as ends in themselves.

## 2. Updated value proposition

The product is not a paid shortcut to a free New York State claim.

The value proposition to validate is:

Find unresolved insurance-beneficiary opportunities that the rightful person or authorized representative may not be effectively resolving through ordinary processes, determine whether the case is practically resolvable at bounded cost, and provide compliant discovery/location/recovery assistance where that assistance creates real value.

The customer must never be led to believe that payment is required to obtain New York State unclaimed funds.

New York OSC offers direct search/claim processing without a provider fee. A commercial service must therefore create value through discovery, location, disambiguation, documentation support, coordination or complex-case assistance.

## 3. Target customer

The initial target is not every IN03 record.

The desired population is:

exact IN03
-> unresolved/persistent opportunity
-> material service need
-> owner or authorized representative resolvable at bounded cost
-> separately authorized compliant contact/recovery path.

Important target hypotheses:

- unresolved but locatable owner;
- deceased owner / estate / authorized-representative path that remains bounded and documentable;
- harder identity/contactability case for which the next information step is explicit and bounded.

Do not infer:

difficulty = high value
old record = high value
estate = high value
IN03 = profitable case.

## 4. Current evidence

NY OSC Attempt 11 established:

- 14,994,489 total physical records;
- 2,792,990 authority-backed insurance records;
- 203,921 primary IN03 aggregate candidates;
- candidate materialization remains separately gated;
- recoverable value is not disclosed by the source.

Stage A established, using synthetic-only fixtures:

- one-candidate transient materialization mechanics;
- non-PII case ID derivation;
- Economic Case Ledger;
- friction lanes F0-F3;
- PRE_VALUE_DISCOVERY_COST;
- bounded incremental budget handling;
- reuse hooks into cost/value/economics components.

Stage A's FIRST_ELIGIBLE_RECORD_IN_SOURCE_ORDER rule was a technical determinism test. It is not the future real P1 economic-targeting rule.

## 5. Targetability model

### 5.1 Deterministic source eligibility

Initial P1 eligibility remains:

- documented 14-field physical shape;
- exact Property Type Code IN03;
- Property Owner Count exactly 1;
- non-empty Property ID;
- usable Holder Report Year for the persistence experiment.

Eligibility is not economic attractiveness.

### 5.2 Persistence-first P1 selection

Future real P1 design uses:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

The oldest Holder Report Year among eligible records is selected; lowest source record ordinal is the deterministic tie-breaker.

Holder Report Year is interpreted only as a persistence signal.

It does not prove:
- awareness/unawareness;
- contactability;
- death;
- complexity;
- recoverable value;
- willingness to pay.

No fixed age threshold is invented.

### 5.3 Service-need axis

SERVICE_NEED_STATE:

- UNKNOWN
- LOW_EVIDENCE
- MATERIAL_EVIDENCE

### 5.4 Resolvability axis

RESOLVABILITY_STATE:

- UNKNOWN
- EASY
- BOUNDED
- UNBOUNDED

### 5.5 Estate / representative axis

ESTATE_PATH_STATE:

- NOT_EVALUATED
- NO_EVIDENCE
- EVIDENCE_PRESENT

REPRESENTATIVE_PATH_STATE:

- NOT_EVALUATED
- IDENTIFIED
- BOUNDED_DISCOVERABLE
- NOT_BOUNDED

### 5.6 Awareness axis

AWARENESS_STATE:

- UNKNOWN_UNTIL_OUTREACH
- UNAWARE_CONFIRMED
- AWARE_CONFIRMED

No beneficiary may be labeled "unaware" before evidence produced by a separately authorized contact/outreach stage.

## 6. Targetability classes T0-T4

T0_SELF_SERVICE_LIKELY

- low service-need evidence;
- easy resolvability;
- no material complexity evidenced;
- deprioritize for a paid direct-owner service;
- does not mean low monetary value.

T1_UNRESOLVED_BUT_LOCATABLE

- material service-need evidence;
- easy/low-cost resolvability;
- core direct-service target hypothesis.

T2_ESTATE_OR_REPRESENTATIVE_PATH

- deceased/estate evidence exists;
- rightful representative is identified or bounded-discoverable;
- complex-service target hypothesis;
- does not imply high value.

T3_HARD_BUT_BOUNDED

- material service need;
- identity/contactability is harder;
- an explicit bounded next information step exists within an approved budget.

T4_UNBOUNDED_OR_UNRESOLVED_STOP

- no bounded next information step;
- legal/privacy scope unavailable;
- or incremental cost becomes disproportionate;
- stop rather than add architecture.

When evidence is insufficient:

TARGETABILITY_STATE = UNRESOLVED_REQUIRES_L2

No T class may be fabricated.

## 7. Friction lanes F0-F3

F0-F3 remain backward-compatible process-friction observations.

They are orthogonal to T0-T4.

They must never be used as:
- value prediction;
- targetability score;
- ranking score;
- automatic commercial decision.

Allowed meaning only:

F0 = lower observed process friction
F1 = identifiable/assistance process friction
F2 = harder bounded research friction
F3 = estate/complex-document process friction

No automatic T/F mapping exists.

## 8. No targetability scoring yet

Version 1 uses evidence states and deterministic classes.

targetability_score = null

Do not create weights, probabilities or point systems before real P1/P2 evidence supports them.

## 9. Economic metrics

PRE_VALUE_DISCOVERY_COST remains the umbrella measure of evidenced cost accumulated before sufficient value evidence exists.

New primary P1 sub-metric:

TARGETABILITY_DECISION_COST

Definition:

the fully evidenced incremental cost required to determine whether a case has material service need and bounded resolvability before outreach/value research.

P1 optimization target becomes:

COST_TO_DETERMINE_SERVICE_NEED_AND_RESOLVABILITY

before:

COST_TO_LEARN_IF_THE CASE HAS SUFFICIENT VALUE.

TARGETABILITY_DECISION_COST_STATE:

- NOT_MEASURED
- MEASURING
- MEASURED

Human labor cost may be monetized only when a documented labor-rate evidence reference exists.

## 10. Economic Case Ledger

Every future real candidate experiment must emit a durable ledger without direct owner PII.

Retain:

- case_id;
- source_id;
- source snapshot/acquisition evidence;
- selection rule version;
- source record ordinal;
- Holder Report Year when allowed as reporting metadata;
- friction lane and evidence;
- stage timestamps;
- machine/data/human-time evidence;
- PRE_VALUE_DISCOVERY_COST;
- value-evidence state;
- explicit stop reason.

Add:

- persistence_signal;
- service_need_state;
- resolvability_state;
- estate_path_state;
- representative_path_state;
- awareness_state;
- targetability_state;
- targetability_class;
- targetability_decision_cost_state;
- targetability_decision_cost_cents when fully evidenced;
- targetability_evidence_refs;
- targetability_stop_reason;
- next_information_objective.

Do not persist:

- Owner Name;
- Property ID;
- raw row;
- address;
- phone/email;
- relatives;
- owner-PII-derived hashes;
- guessed value;
- guessed fee;
- guessed probability of recovery.

## 11. Economic Discovery Ladder

### L0 — Source qualification / target signal

Use non-PII/already-authorized evidence.

Goal:

- deterministic eligibility;
- persistence signal;
- no owner-value inference.

### L1 — Transient one-candidate materialization

Goal:

- materialize the minimum approved candidate structure transiently;
- measure L1 machine/operator cost;
- preserve no durable owner PII.

No identity resolution, outreach or value research.

### L2 — Minimal targetability discovery

Requires separate legal/privacy authorization.

Question:

CAN THIS OWNER OR AUTHORIZED REPRESENTATIVE BE IDENTIFIED/CONTACTED AT BOUNDED COST, AND IS THERE MATERIAL SERVICE NEED?

Outputs:

- service_need_state;
- resolvability_state;
- estate/representative-path state where lawfully evidenced;
- T0-T4 or UNRESOLVED_REQUIRES_L2;
- TARGETABILITY_DECISION_COST.

No broad genealogy or unbounded manual research.

### L3 — Outreach / service-fit discovery

Separate outreach authorization required.

Only here may awareness become evidence-backed through actual contact.

Measure:
- actual contactability;
- response;
- awareness;
- willingness to engage;
- agreement conversion;
- channel/human cost.

### L4 — Value-evidence discovery

Obtain evidence-backed recoverable value when lawfully possible, or preserve an explicit unknown/blocked state.

No invented value.

### L5 — Explicit case economics

Only when value, actual/agreed fee and fully loaded case-cost evidence exist.

Then compute:

GROSS_FEE = RECOVERED_VALUE x REALIZED_FEE_RATE

CONTRIBUTION_BEFORE_OVERHEAD = GROSS_FEE - FULLY_LOADED_CASE_COST

The Product Owner decides GO / REVISE / STOP.

## 12. P1 budget discipline

L1 maximum new external cash spend:

USD 0.00

Allowed:
- measured machine cost;
- measured operator/reviewer time;
- no paid API;
- no paid data broker;
- no paid identity enrichment.

This is a spend ceiling, not a claim that human/machine work has zero economic cost.

L2 incremental budget:

UNSET_REQUIRES_PRODUCT_OWNER

No L2 spend is authorized by this strategy.

## 13. Pilot sequence

### P1 — one targetability experiment

Question:

Can we identify one case with material service need and bounded resolvability at low enough evidenced cost to justify asking for the next authorization, before knowing recoverable value?

P1 success does not require outreach, agreement, known value or recovery.

Valid outcomes:

- TARGETABLE_CONTINUE_TO_SEPARATE_OUTREACH_REVIEW;
- STOP_SELF_SERVICE_LOW_NEED;
- STOP_UNBOUNDED_RESOLUTION_COST;
- STOP_LEGAL_PRIVACY_SCOPE;
- STOP_TARGETABILITY_NOT_ESTABLISHED_WITHIN_BUDGET.

### P2 — approximately five bounded cases

Only after P1 review.

P2 is a management-learning batch, not a statistical sample.

Do not simply take the next five rows.

Test variation in:
- source persistence;
- T-class outcome;
- friction lane;
- targetability decision cost;
- estate versus non-estate path where lawfully evidenced.

### P3 — approximately 20–30 bounded cases

Only if P2 supports continuation.

Measure an initial empirical distribution of:
- targetable-opportunity rate;
- service-need outcomes;
- resolvability outcomes;
- targetability decision cost;
- contactability;
- outreach conversion;
- value-known rate;
- recovery/fee economics.

No statistical representativeness is claimed from sample size alone.

## 14. Stop conditions

Stop fail-closed if:

- deterministic candidate eligibility fails;
- persistence experiment cannot use a valid Holder Report Year;
- required legal/privacy authorization is missing;
- owner PII would be persisted/logged beyond the approved envelope;
- no bounded next information step exists;
- paid API/data would be required without a Product Owner budget and approval;
- targetability cannot be established within the approved budget;
- outreach is required before outreach authorization;
- value/fee/probability would have to be invented;
- T class would rely on unsupported inference.

## 15. Product priority rule

Priority is now:

TARGETABILITY EVIDENCE BEFORE VALUE RESEARCH
and
VALUE EVIDENCE BEFORE SCALE.

Freeze by default:

- broad multi-state expansion;
- generic new agent frameworks;
- graph infrastructure;
- generalized genealogy infrastructure;
- mass outreach automation;
- large durable PII architecture;
- non-critical UI polish;
- parser/source work without a demonstrated blocker.

## 16. Reuse-first rule

Reuse existing:

- Stage A transient-materialization contracts;
- Economic Case Ledger;
- follow-up cost component;
- pre-contact value-evidence component;
- explicit case-economics component;
- reviewer surfaces.

Add only the smallest targetability layer needed to distinguish service need from resolvability.

## 17. Current next action

The value-proposition and parameter reframe is authorized by the Product Owner.

Execute only:

IMPLEMENT_AND_REVIEW_SYNTHETIC_TARGETABLE_OPPORTUNITY_FILTER_V1

This implementation must remain synthetic-only.

It must:
- implement persistence-first deterministic selection using only non-owner targeting metadata;
- implement targetability evidence states/classes T0-T4;
- preserve F0-F3 as friction-only;
- expose TARGETABILITY_DECISION_COST as a distinct future economic metric;
- use no numeric targetability score;
- contain tests and a versioned machine contract;
- authorize nothing real.

It must not perform:
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

## 18. Canonical read order

1. AGENTS.md
2. PRODUCT_STRATEGY_MVP1.md
3. PROJECT_STATE.md
4. ROADMAP.md
5. DECISIONS.md
6. docs/handovers/HANDOVER_CURRENT.md

Law, privacy, security and explicit authorization gates remain superior constraints.
