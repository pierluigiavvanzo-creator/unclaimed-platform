# NORTH_AMERICA_MULTI_REGISTRY_PRODUCT_TARGET_V1.md

Date: 2026-09-24

Status: PRODUCT TARGET — AUTHORITATIVE DIRECTION

Owner: Product Owner

## 1. Product geography

The product target is NOT limited to New York OSC.

Target market:

UNITED STATES + CANADA

The platform must be designed to ingest and operate across multiple lawful/authorized unclaimed-property, insurance, estate, corporate, governmental and other relevant public/authorized registries, subject to source-by-source legal/terms/privacy review.

New York OSC is the first validated source adapter / pilot anchor.

It is NOT the permanent product boundary.

No registry is considered supported until its source contract, legal/terms status, schema, provenance and acquisition method are verified.

## 2. Product category

The target is a North American multi-registry unclaimed-asset intelligence and recovery operating platform.

The platform must support an end-to-end workflow:

MULTI_REGISTRY_DISCOVERY
-> INGEST / NORMALIZE / DEDUP
-> CANDIDATE / LEAD GENERATION
-> EVIDENCE-AWARE AI CONFIDENCE
-> LEAD PRIORITIZATION
-> PEOPLE / OWNER / HEIR FINDING
-> CASE ECONOMICS
-> COMPLIANCE / HUMAN GATES
-> CONTRACT BUILDER
-> FEE CALCULATOR
-> CRM / CASE MANAGEMENT
-> OUTREACH / CLAIM WORKFLOW WHEN AUTHORIZED
-> RECOVERY / OUTCOME / LEARNING LOOP

The platform should automate or semi-automate each stage only where reliability, evidence, compliance and economics justify automation.

Human review remains mandatory for legal/privacy gates, ambiguous identity, material contradictions and other high-risk decisions.

## 3. Required product capabilities

### 3.1 Multi-registry source layer

Required:

- source registry;
- jurisdiction metadata;
- acquisition adapters;
- schema/version contracts;
- provenance;
- raw hash / snapshot evidence;
- source freshness;
- terms/legal state;
- source-specific parser/normalizer;
- deduplication and cross-registry linking;
- failure isolation so one registry does not break the platform.

Target geography:

- US federal/state/territorial sources where lawful and relevant;
- Canadian federal/provincial/territorial sources where lawful and relevant.

No source coverage claim is allowed without verified source support.

### 3.2 AI confidence and evidence scoring

Required:

- multidimensional confidence, not one opaque score;
- evidence quality;
- identity confidence;
- owner/heir/beneficiary confidence where applicable;
- contradiction tracking;
- source reliability/provenance;
- uncertainty preservation;
- calibration against real outcomes when enough evidence exists.

AI output must remain explainable enough for human review.

No model may convert missing evidence into fabricated certainty.

### 3.3 Lead prioritization

Required:

- service need;
- resolvability;
- expected research burden;
- legal/privacy availability;
- source persistence;
- evidence strength;
- jurisdiction friction;
- estimated/known economic value only when evidence-backed;
- targetability decision cost;
- later outcome data.

The ranking objective is NOT theoretical gross value alone.

The ranking objective is:

MAXIMIZE EXPECTED USABLE ECONOMIC VALUE PER UNIT OF OPERATOR TIME AND CAPITAL

subject to legal/privacy constraints and evidence quality.

Stage B remains value-blind where the source does not disclose value.

### 3.4 People finder / identity resolution

Required:

- modular provider adapters;
- public-source research;
- identity disambiguation;
- owner/contact resolution;
- death/estate evidence;
- heir/representative path;
- bounded genealogy when justified;
- provider terms/privacy/FCRA or analogous legal status;
- cost/time ledger;
- confidence and contradiction output.

No single people-search provider becomes a hard dependency.

### 3.5 Contract builder

Required later, after jurisdiction-specific legal readiness:

- jurisdiction-aware agreement templates;
- variable clauses;
- mandatory disclosures;
- fee caps/rules;
- owner/representative roles;
- signature/notary/witness requirements where applicable;
- versioned legal template provenance;
- human/legal approval gate before production use.

Do not create universal legal language that silently ignores jurisdiction.

### 3.6 Fee calculator

Required:

- jurisdiction-specific fee rules/caps;
- agreement fee;
- recoverable value when known;
- service costs;
- taxes/processing costs where relevant;
- contribution margin;
- stop/go thresholds only when evidence-backed.

No guessed value may be converted into a fee.

### 3.7 CRM / case operating system

Required:

- lead/case lifecycle;
- owner/heir/representative entities;
- tasks;
- reviewer decisions;
- evidence;
- communications;
- contracts;
- fees;
- claim milestones;
- deadlines;
- status;
- costs;
- outcome;
- audit trail;
- deduplication/case linking;
- permissions and PII controls.

The CRM must be case/evidence aware, not just a generic contact database.

## 4. Automation philosophy

Target:

AUTOMATE REPETITIVE, HIGH-CONFIDENCE, REVERSIBLE WORK.

SEMI-AUTOMATE AMBIGUOUS OR MATERIAL DECISIONS.

HUMAN-GATE LEGAL, PRIVACY, IDENTITY-CONFLICT AND IRREVERSIBLE ACTIONS.

Automation should be measured by:

- operator minutes saved;
- error/false-positive rate;
- cost per targetable lead;
- time to targetability;
- evidence completeness;
- conversion between stages;
- human override rate;
- economic contribution.

Automation percentage alone is NOT a success metric.

## 5. Competitive-performance objective

Patentability is NOT a primary product objective.

The competitive objective is:

BETTER PERFORMANCE + HIGHER RELIABILITY + LOWER COST + LOWER OPERATOR TIME + BETTER CONVERSION

than alternative workflows/products.

The platform should build a defensible operating/data advantage through:

- normalized multi-registry coverage;
- proprietary outcome history;
- evidence-grounded identity resolution;
- calibrated confidence;
- targetability economics;
- cross-registry linkage;
- workflow speed;
- lower manual minutes per resolved case;
- higher useful-lead precision;
- better legal/compliance execution.

Any moat claim must be supported by measured performance, not feature novelty.

## 6. Core performance metrics

No numeric thresholds are invented yet.

Required measurement set:

- REGISTRY_COVERAGE_VERIFIED_COUNT
- SOURCE_REFRESH_LATENCY
- INGEST_SUCCESS_RATE
- NORMALIZATION_ERROR_RATE
- DUPLICATE_LINK_PRECISION
- LEAD_PRECISION
- FALSE_POSITIVE_RATE
- CONFIDENCE_CALIBRATION
- TIME_TO_TARGETABILITY
- TARGETABILITY_DECISION_COST
- COST_PER_TARGETABLE_LEAD
- HUMAN_MINUTES_PER_CASE
- AUTOMATION_RATE_BY_STAGE
- HUMAN_OVERRIDE_RATE
- IDENTITY_RESOLUTION_SUCCESS_RATE
- OUTREACH_CONTACT_RATE
- AGREEMENT_CONVERSION_RATE
- VALUE_KNOWN_RATE
- CLAIM_SUCCESS_RATE
- TIME_TO_RECOVERY
- FULLY_LOADED_CASE_COST
- CONTRIBUTION_BEFORE_OVERHEAD
- ECONOMIC_VALUE_X_USABLE_PRODUCT_VALUE_PER_USER_TIME

Metrics become promotion gates only after sufficient real evidence exists.

## 7. Stage B relationship to the North America target

Stage B remains deliberately narrow.

Current Stage B role:

prove the targetability / economics / privacy / execution loop on ONE real bounded source/case using the already-developed NY OSC adapter.

Stage B DOES NOT redefine the product as New York-only.

Stage B exit should answer:

CAN THE CORE ENGINE TURN ONE AUTHORIZED REGISTRY RECORD INTO A RELIABLE TARGETABILITY DECISION AT CONTROLLED COST?

After Stage B/P1 evidence, the next architecture work must generalize the source adapter contract so additional US and Canadian registries can plug into the same downstream engine.

Do NOT implement dozens of registries before Stage B economics are validated.

Do NOT hard-code NY semantics into generic downstream modules.

NY-specific logic must remain in:

- source adapter;
- jurisdiction policy;
- source taxonomy mapping;
- legal/compliance policy.

Generic downstream components must remain registry-independent where feasible.

## 8. Post-Stage-B platform expansion sequence

If P1/P2 support continuation:

1. freeze the generic Source Adapter Contract;
2. create canonical normalized RegistryRecord / OpportunityCandidate contracts;
3. add source/jurisdiction capability matrix;
4. benchmark next registries by:
   - data accessibility;
   - legal/terms viability;
   - insurance relevance;
   - owner/beneficiary fields;
   - value availability;
   - refresh frequency;
   - expected candidate density;
   - integration cost;
5. add US registries in evidence-backed priority order;
6. add Canadian registries in evidence-backed priority order;
7. implement cross-registry dedup/linking;
8. calibrate AI confidence against outcomes;
9. expand people-finder provider layer;
10. activate contract builder / fee calculator / CRM jurisdiction modules only after legal readiness.

No geography is added merely for coverage vanity.

## 9. Architectural implication

Target architecture:

SOURCES / REGISTRIES
        ↓
SOURCE ADAPTERS
        ↓
CANONICAL NORMALIZED RECORDS
        ↓
DEDUP / LINKING
        ↓
TARGETABILITY + CONFIDENCE
        ↓
PEOPLE / HEIR / REPRESENTATIVE RESOLUTION
        ↓
CASE ECONOMICS + COMPLIANCE
        ↓
CRM / CONTRACT / FEE / CLAIM WORKFLOW
        ↓
OUTCOMES
        ↓
CALIBRATION / PRIORITIZATION LEARNING LOOP

Every layer must expose versioned contracts.

## 10. Current strategic constraint

Do not confuse:

PRODUCT TARGET = USA + CANADA MULTI-REGISTRY PLATFORM

with:

CURRENT EXPERIMENT = NY OSC STAGE B P1

Both are true simultaneously.

The first defines architecture and roadmap.

The second defines the smallest next experiment.

## 11. Immediate next action

Return to Stage B.

Do not begin broad multi-registry implementation yet.

First:

- establish/bind the real US controller when the Product Owner is ready;
- prepare fresh single-use P1 gates;
- execute ONE real bounded P1;
- review targetability and economic evidence.

Then use the result to decide the first multi-registry expansion wave.
