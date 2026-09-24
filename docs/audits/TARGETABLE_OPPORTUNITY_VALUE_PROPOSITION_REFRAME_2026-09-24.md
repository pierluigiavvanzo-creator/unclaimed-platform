# TARGETABLE OPPORTUNITY / VALUE PROPOSITION REFRAME — 2026-09-24

Classification: A — Product Critical

Status: ACCEPTED DESIGN DIRECTION / OFFLINE ONLY / REAL P1 NOT AUTHORIZED

## 1. Why the product thesis changes

The NY OSC Owner Name File has already proven that candidate supply is not the immediate bottleneck: Attempt 11 found 203,921 aggregate IN03 records. The file does not disclose recoverable amounts.

New York also provides a free direct claim path. OSC explicitly states there is no charge for processing claims or returning funds. New York nevertheless recognizes Abandoned Property Location Service Providers, subject to required disclosures, written/notarized agreement requirements and a statutory fee ceiling of 15 percent for the applicable location-service scope.

Therefore the product must not optimize for merely finding a name that the owner can easily claim for free.

The economic target is the subset where the platform creates material service value because the right person is unaware, unresolved, hard to reach, or faces meaningful recovery/documentation complexity, while the case is still resolvable at a bounded cost.

## 2. Updated value proposition

Primary value proposition:

Find unresolved insurance-beneficiary opportunities that the rightful person or authorized representative may not be effectively reaching through ordinary processes, identify whether the case is practically resolvable at bounded cost, and provide compliant discovery/location/recovery assistance where that assistance creates real value.

Mandatory customer disclosure principle:

The service must never imply that payment is required to obtain funds from New York State. The owner or authorized representative can claim directly through OSC without paying a provider fee.

The product earns its value from discovery, location, disambiguation, documentation support, coordination and complex-case assistance — not from privileged access to State funds.

## 3. Target customer

The initial target is NOT every IN03 record.

The desired population is:

IN03
-> unresolved long enough to justify a persistence hypothesis
-> material service need evidenced
-> owner or authorized representative resolvable at bounded cost
-> compliant contact/recovery path can be separately authorized.

Particularly important hypotheses to validate:

- unresolved but locatable owner;
- deceased owner / estate / authorized-representative path that is bounded and documentable;
- harder identity/contactability case with a clear next bounded information step.

The platform must not infer that difficult means high value.

## 4. What official evidence supports

Official NY OSC evidence establishes:

1. the downloadable list includes name, last-known address, property nature, when it was reported and by whom;
2. dollar values are not disclosed in the list;
3. direct OSC search/claim processing is free;
4. location-service providers are recognized and may submit claims with the required agreement;
5. the maximum applicable provider fee is 15 percent of recovered cash/value, but 15 percent is a ceiling and not an assumed realized fee;
6. the Expedited Payment Program was expanded in 2026 to qualifying payments up to USD 5,000;
7. estate claims do not qualify for that expedited program;
8. deceased-owner/estate claims can require death evidence, entitlement evidence and, in some cases, a court-appointed representative.

Official source references:

- https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers
- https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form
- https://www.osc.ny.gov/press/releases/2026/04/dinapoli-fast-track-payment-program-returns-48-million-unclaimed-funds
- https://www.osc.ny.gov/unclaimed-funds/claimants/claims-deceased-owners-and-estates
- https://www.osc.ny.gov/unclaimed-funds/claimants/required-documentation
- https://www.nysenate.gov/legislation/laws/ABP/1416
- https://www.nysenate.gov/legislation/laws/GBS/393-E

## 5. Parameter model — old versus new

### 5.1 Source eligibility remains deterministic

Initial P1 source eligibility remains:

- documented 14-field physical shape;
- exact Property Type Code IN03;
- Property Owner Count exactly 1;
- non-empty Property ID;
- valid Holder Report Year for the persistence-first selection experiment.

This is eligibility, not economic attractiveness.

### 5.2 First-source-order selection is superseded for future real P1

Stage A used:

FIRST_ELIGIBLE_RECORD_IN_SOURCE_ORDER

That rule remains historical evidence that one candidate can be materialized deterministically.

It is no longer the planned economic-selection rule for real P1.

Future P1 design uses:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Rationale:

Holder Report Year is available without using owner identity as a ranking variable. An older report is a persistence signal that the item has remained unresolved longer.

Interpretation guard:

Older report year does NOT prove:
- higher recoverable value;
- beneficiary unawareness;
- owner death;
- contact difficulty;
- willingness to pay.

Tie-breaker is lowest source record ordinal.

No fixed age threshold is invented.

### 5.3 New targetability axes

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

AWARENESS_STATE:
- UNKNOWN_UNTIL_OUTREACH
- UNAWARE_CONFIRMED
- AWARE_CONFIRMED

Before an outreach gate, awareness must remain UNKNOWN_UNTIL_OUTREACH.

### 5.4 Targetability classes

T0_SELF_SERVICE_LIKELY
- low service-need evidence;
- easy resolvability;
- no material complexity evidenced;
- deprioritize for paid direct-owner service;
- no inference about low monetary value.

T1_UNRESOLVED_BUT_LOCATABLE
- material service-need evidence;
- easy/low-cost resolvability;
- core direct-service target hypothesis.

T2_ESTATE_OR_REPRESENTATIVE_PATH
- deceased/estate evidence exists;
- rightful representative is identified or bounded-discoverable;
- complex-service target hypothesis;
- no inference of high value.

T3_HARD_BUT_BOUNDED
- meaningful service need;
- identity/contactability is harder but a bounded next step exists within an explicitly approved budget.

T4_UNBOUNDED_OR_UNRESOLVED_STOP
- no bounded next information step;
- cost/scope has become disproportionate;
- privacy/legal scope unavailable;
- stop rather than add architecture.

When evidence is insufficient, the state is UNRESOLVED_REQUIRES_L2 and no T class is fabricated.

### 5.5 F0-F3 remain but are orthogonal

Existing friction lanes remain backward-compatible observations of process friction.

They are NOT:
- a value score;
- a targetability score;
- a ranking rule;
- a commercial decision.

F0-F3 may coexist with T0-T4.

Example:
- T2 + F3 can mean a targetable estate case with high process friction;
- T0 + F0 can mean easy/self-service;
- no mapping is automatic.

### 5.6 No targetability score

Version 1 uses deterministic evidence states and classes.

No weighted numeric score is allowed until real P1/P2 evidence supports weights.

targetability_score = null

This prevents false precision.

## 6. Economic parameters

PRE_VALUE_DISCOVERY_COST remains the umbrella metric for evidenced cost accumulated before sufficient value evidence exists.

New sub-metric:

TARGETABILITY_DECISION_COST

Definition:

The fully evidenced incremental cost required to determine whether the case has material service need and bounded resolvability before outreach/value research.

P1 primary optimization target becomes:

COST_TO_DETERMINE_SERVICE_NEED_AND_RESOLVABILITY

before:

COST_TO_LEARN_VALUE.

Required economic states:

TARGETABILITY_DECISION_COST_STATE:
- NOT_MEASURED
- MEASURING
- MEASURED

PRE_VALUE_DISCOVERY_COST states remain:
- NOT_STARTED
- MEASURING
- VALUE_KNOWN
- VALUE_STILL_UNKNOWN_STOPPED
- VALUE_REQUIRES_UNAUTHORIZED_SCOPE

No cost may be monetized from human time without a documented labor-rate evidence reference.

## 7. Economic Discovery Ladder — revised interpretation

L0 — SOURCE QUALIFICATION / TARGET SIGNAL
- exact deterministic eligibility;
- non-PII persistence signal;
- no owner-value inference.

L1 — TRANSIENT ONE-CANDIDATE MATERIALIZATION
- transient minimum candidate structure;
- measure L1 cost;
- no identity resolution;
- no outreach;
- no value research.

L2 — MINIMAL TARGETABILITY DISCOVERY
Question:
CAN THIS OWNER OR AUTHORIZED REPRESENTATIVE BE IDENTIFIED/CONTACTED AT BOUNDED COST, AND IS THERE MATERIAL SERVICE NEED?

L2 produces:
- service_need_state;
- resolvability_state;
- estate/representative-path state where lawfully evidenced;
- T0-T4 or UNRESOLVED_REQUIRES_L2;
- TARGETABILITY_DECISION_COST.

L3 — OUTREACH / SERVICE-FIT
Separate authorization.
Only here may awareness become evidence-backed through actual contact.

L4 — VALUE EVIDENCE
Obtain evidence-backed recoverable value when lawfully possible or preserve explicit unknown state.

L5 — EXPLICIT CASE ECONOMICS
Only with value, realized/agreed fee evidence and fully loaded cost evidence.

## 8. Pilot P1 — revised question

Old question:
Can we obtain useful economic evidence and measure cost before research becomes irrational?

Revised, more precise P1 question:

Can we identify one case with material service need and bounded resolvability at low enough evidenced cost to justify asking for the next authorization, before knowing its recoverable value?

P1 success does not require:
- outreach;
- agreement;
- known value;
- recovery.

Valid P1 outcomes include:
- TARGETABLE_CONTINUE_TO_SEPARATE_OUTREACH_REVIEW;
- STOP_SELF_SERVICE_LOW_NEED;
- STOP_UNBOUNDED_RESOLUTION_COST;
- STOP_LEGAL_PRIVACY_SCOPE;
- STOP_TARGETABILITY_NOT_ESTABLISHED_WITHIN_BUDGET.

## 9. P1 budgets

L1 external incremental cash budget:

USD 0.00

Allowed:
- measured machine time/cost already available;
- measured human time;
- no paid API;
- no paid data broker;
- no paid identity enrichment.

L2 budget:
UNSET_REQUIRES_PRODUCT_OWNER

No L2 spend is authorized by this design.

## 10. Pilot P2 and P3

P2 remains approximately five cases as a management-learning batch, not a statistical sample.

P2 should deliberately test variation in:
- source persistence;
- T-class outcome;
- friction lane;
- cost concentration;
- estate versus non-estate path where lawfully evidenced.

Do not simply take the next five source rows.

P3 remains approximately 20–30 cases only if P2 supports continuation.

P3 purpose becomes empirical estimation of:
- targetable-opportunity rate;
- service-need distribution;
- resolvability distribution;
- targetability decision cost;
- contactability;
- outreach conversion;
- value-known rate;
- recovery and fee economics.

No statistical representativeness is claimed merely from sample size.

## 11. Economic Case Ledger additions

Keep the ledger free of direct owner PII.

Add:
- persistence_signal;
- holder_report_year where allowed as non-owner reporting metadata;
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

Do NOT add:
- Owner Name;
- Property ID;
- raw row;
- address;
- phone/email;
- relatives;
- PII-derived hashes;
- guessed value;
- guessed fee;
- guessed probability of recovery.

## 12. Mandatory stop conditions

Stop if:
- candidate eligibility fails;
- report year cannot support the selected persistence experiment;
- required legal/privacy authorization is missing;
- PII would be persisted/logged outside the approved envelope;
- no bounded next information step exists;
- L2 would require unapproved paid data/API use;
- targetability cannot be determined within the approved incremental budget;
- outreach is required before outreach authorization;
- value/fee/probability would need to be invented;
- a T class would be based on unsupported inference.

## 13. Value proposition consequence

The product should not market itself as a faster paid way to perform a free claim.

The core proposition to validate is:

WE FIND AND HELP RESOLVE INSURANCE-BENEFICIARY OPPORTUNITIES THAT THE RIGHTFUL PERSON OR REPRESENTATIVE IS NOT EFFECTIVELY RESOLVING ALONE.

The commercially interesting subset is therefore not highest theoretical value and not highest difficulty.

It is:

MATERIAL SERVICE NEED × BOUNDED RESOLVABILITY × EVIDENCED COST DISCIPLINE.

## 14. Non-authorization

This document does not authorize:
- source access;
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
