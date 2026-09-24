# PRODUCT_STRATEGY_MVP1.md

Version: 3.2
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

The product target is NOT limited to New York OSC.

Target geography:

UNITED STATES + CANADA

The product target is a North American multi-registry unclaimed-asset intelligence and recovery operating platform.

The value proposition to validate is:

Continuously discover unresolved opportunities across lawful/authorized registries, normalize and link registry records, prioritize the leads most likely to create real service value, resolve owner/heir/representative identity at bounded cost, and move viable cases through compliant contract, fee, CRM and recovery workflows with the highest practical reliability and efficiency.

New York OSC is the first validated source adapter / pilot anchor.

It is NOT the permanent product boundary.

The platform must ultimately support:

- multi-registry acquisition and normalization;
- evidence-aware AI confidence scoring;
- lead prioritization;
- people/owner/heir finding;
- case economics;
- jurisdiction-specific compliance;
- contract builder;
- fee calculator;
- CRM / case management;
- outreach and claim workflow when separately authorized;
- outcome learning and calibration.

The product must never imply that a paid intermediary is legally required where a direct free claim path exists.

Commercial value must come from discovery, prioritization, location, identity resolution, documentation, coordination, complex-case execution, speed, reliability and lower user/operator effort.

## 3. Target customer

The long-term target is not every record from one registry.

The desired North American opportunity population is:

lawful/authorized registry record
-> unresolved opportunity
-> sufficient source/evidence quality
-> material service need
-> owner/heir/beneficiary/authorized representative resolvable at bounded cost
-> jurisdictionally compliant contact/recovery path
-> economically viable service workflow.

Current Stage B remains narrower:

NY OSC exact IN03
-> unresolved/persistent opportunity
-> material service need
-> owner or authorized representative resolvable at bounded cost
-> separately authorized compliant next step.

Stage B is an experiment anchor, not the permanent market scope.

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

### 4.1 Stage nomenclature

Stage A:

SYNTHETIC-ONLY instrumentation and one-candidate mechanics.

Status:

COMPLETE.

Stage B:

PILOT P1 — ONE REAL BOUNDED TARGETABILITY EXPERIMENT.

Stage B exit is:

ONE evidence-backed targetability decision or bounded stop
+ measured TARGETABILITY_DECISION_COST
+ human review.

Stage B does not require outreach, a signed customer agreement, known recoverable value, claim submission, recovery or profitability proof.

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

## 8. Confidence scoring and targetability scoring

Stage B v1 still uses evidence states and deterministic targetability classes.

targetability_score = null

Do not invent weights, probabilities or opaque point systems before real P1/P2 evidence supports them.

The PRODUCT TARGET nevertheless explicitly includes evidence-aware AI confidence scoring.

Future scoring must be multidimensional and calibrated against observed outcomes, including at minimum:

- identity confidence;
- evidence quality;
- source reliability;
- contradiction state;
- resolvability confidence;
- targetability confidence;
- jurisdiction/compliance availability;
- later economic outcome evidence.

No AI confidence score may replace provenance or human review where ambiguity or legal risk is material.

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

### L1 — Selected-record verification / minimal materialization

Goal:

- verify the selected candidate with the minimum approved data;
- measure L1 machine/operator cost;
- preserve no durable owner PII.

For L1-only execution, direct owner PII is not required for the targetability experiment and should not be field-buffered.

The selected-row second pass may use only:

- structural width;
- Property ID presence boolean;
- Property Type Code;
- Property Owner Count;
- Holder Report Year.

Direct PII materialization is reserved for a separately pre-authorized L2 targetability purpose.

No identity resolution, outreach or value research at L1.

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

Stage B L2-A experiment bounds:

- external paid spend: USD 0.00;
- manual research cap: 900 seconds;
- no paid API;
- no paid data broker;
- no consumer-report/FCRA product.

The 900-second limit is a Product Owner experiment cap, not an evidence-backed profitability threshold.

The exact L2-A provider or manual research source set still requires separate privacy/terms review and explicit approval.

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

Priority during Stage B is:

TARGETABILITY EVIDENCE BEFORE VALUE RESEARCH
and
VALUE EVIDENCE BEFORE SCALE.

Product target after Stage B is:

NORTH_AMERICA_MULTI_REGISTRY_PLATFORM

covering USA + Canada through versioned source adapters and jurisdiction policy modules.

Freeze during Stage B:

- simultaneous implementation of many registries before P1 economics are validated;
- generic new agent frameworks without measured benefit;
- graph infrastructure without a demonstrated need;
- generalized genealogy infrastructure before bounded identity economics are measured;
- mass outreach automation before legal/readiness evidence;
- large durable PII architecture;
- non-critical UI polish;
- source/parser work without a demonstrated blocker.

Do NOT freeze the multi-registry architecture itself.

Generic downstream components must avoid hard-coding NY-specific semantics so that additional US and Canadian registries can be added after Stage B without redesigning targetability, confidence, economics, CRM, contracts or fee logic.

## 16. Reuse-first rule

Reuse existing:

- Stage A transient-materialization contracts;
- Economic Case Ledger;
- follow-up cost component;
- pre-contact value-evidence component;
- explicit case-economics component;
- reviewer surfaces.

For North American expansion, reuse/wrap mature components before custom code for:

- source ingestion;
- entity resolution;
- confidence/calibration;
- CRM/case management;
- document/contract generation;
- workflow orchestration;
- search/provider adapters.

Add custom code where the competitive performance advantage is actually measured.

Performance and efficiency outrank novelty/patentability.

## 16.1 Product performance objective

Patentability is NOT a primary objective.

The competitive objective is superior measured execution:

BETTER RELIABILITY
+ LOWER COST
+ LOWER OPERATOR TIME
+ HIGHER USEFUL-LEAD PRECISION
+ BETTER STAGE CONVERSION
+ FASTER TIME TO TARGETABILITY / RECOVERY

Required measurement family:

- verified registry coverage;
- source refresh latency;
- ingest success/error rate;
- normalization error rate;
- duplicate/cross-registry link quality;
- lead precision / false-positive rate;
- confidence calibration;
- TIME_TO_TARGETABILITY;
- TARGETABILITY_DECISION_COST;
- COST_PER_TARGETABLE_LEAD;
- HUMAN_MINUTES_PER_CASE;
- AUTOMATION_RATE_BY_STAGE;
- HUMAN_OVERRIDE_RATE;
- identity-resolution success rate;
- outreach contact rate;
- agreement conversion rate;
- value-known rate;
- claim success rate;
- time to recovery;
- fully loaded case cost;
- contribution before overhead.

No numeric promotion thresholds are invented before real evidence exists.

## 17. Current Stage B critical path

Stage B / Pilot P1 is now the next product-critical milestone.

Fast-track sequence:

1. bind the real controller operating model and entity facts;
2. preserve L1-only direct-PII minimization;
3. complete the US/New York pre-contact readiness track actually triggered by the controller facts;
4. approve one exact L2-A provider or manual research source set;
5. create fresh single-use approvals bound to the final runner checkpoint and successful CI;
6. execute one real bounded P1;
7. perform human economic review before any P2 expansion;
8. if P1/P2 support continuation, freeze a generic Source Adapter Contract and begin prioritized USA+Canada multi-registry expansion.

Do not insert broad multi-registry implementation ahead of P1 unless a demonstrated blocker requires it.

Do not let the Stage B NY adapter leak NY-specific semantics into generic downstream modules.

All seven real P1 execution/privacy gates remain separately authorized and non-reusable.

No source access, download, real PII processing, external PII query, outreach, value research, fee agreement, representation or claim activity is authorized by this strategy update.

## 18. Canonical read order

1. AGENTS.md
2. PRODUCT_STRATEGY_MVP1.md
3. PROJECT_STATE.md
4. ROADMAP.md
5. DECISIONS.md
6. docs/handovers/HANDOVER_CURRENT.md

Law, privacy, security and explicit authorization gates remain superior constraints.
