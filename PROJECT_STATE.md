# PROJECT_STATE.md

Last updated: 2026-09-24

## Authoritative product state

The project is in PRODUCT VALIDATION / NORTH AMERICA MULTI-REGISTRY TARGETABILITY MODE.

Long-term product target:

UNITED STATES + CANADA MULTI-REGISTRY UNCLAIMED-ASSET INTELLIGENCE AND RECOVERY PLATFORM

Current Stage B experiment:

ONE AUTHORIZED REAL SOURCE -> ONE TARGETABLE BOUNDED CASE -> ONE REVIEWABLE ECONOMIC RESULT

Primary economic rule:

BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE

Guiding metric:

ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME


## Product target clarification

Product geography:

UNITED STATES + CANADA

New York OSC is the first validated source adapter / Stage B pilot anchor.

It is NOT the permanent product boundary.

Target platform capabilities:

- multi-registry acquisition and normalization;
- cross-registry deduplication/linking;
- evidence-aware AI confidence scoring;
- lead prioritization;
- people/owner/heir/representative finding;
- case economics;
- jurisdiction-specific compliance;
- contract builder;
- fee calculator;
- CRM / case management;
- outreach and claim workflow when separately authorized;
- outcome learning/calibration.

Patentability is not a product priority.

Competitive advantage must be demonstrated through measurable:

- reliability;
- useful-lead precision;
- lower false positives;
- confidence calibration;
- lower operator minutes per case;
- lower targetability decision cost;
- lower cost per targetable lead;
- faster time to targetability/recovery;
- better conversion between workflow stages;
- better case economics.

No numeric performance thresholds are invented before real evidence exists.

Stage B remains intentionally narrow so that the engine is validated before broad USA/Canada source integration.

## Canonical main

Canonical branch:

main

Verified runtime-integration checkpoint (PR #38 merge):

e2856c61a77e2ff8ca6f973b9090beb87a754ebc

Documentation-only commits may advance `main` beyond this runtime checkpoint. Always verify the remote `main` HEAD at task start.

PR #37:

MVP1: define fresh real P1 targetability execution scope — MERGED

PR #37 merge commit:

755bd4c6dbd18e4a204c513e68e456c517e9dbf7

PR #37 post-merge CI:

35999157888 — SUCCESS

PR #38:

MVP1: implement and review offline real P1 targetability runner — MERGED

PR #38 runtime-integration merge commit:

e2856c61a77e2ff8ca6f973b9090beb87a754ebc

Final post-merge main CI:

35999333460 — SUCCESS

PRODUCT_STRATEGY_MVP1 v3.2, D-012, D-013 and D-014 are canonical.

Product-target companion document:

docs/NORTH_AMERICA_MULTI_REGISTRY_PRODUCT_TARGET_V1.md

## Real-source evidence already established

NY OSC Attempt 11 established:

- total physical records: 14,994,489;
- authority-backed insurance records: 2,792,990;
- primary IN03 aggregate candidates: 203,921;
- real candidate materialization: NOT AUTHORIZED;
- recoverable value: UNKNOWN_FROM_SOURCE.

All historical execution/privacy approvals are consumed, non-reusable and zero-retry.

## Canonical targetability model

Real P1 selection policy:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Holder Report Year is persistence evidence only.

It is not evidence of:

- monetary value;
- awareness;
- death;
- contactability;
- claim complexity;
- willingness to pay.

Target thesis:

MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE

T0-T4 = targetability classes.

F0-F3 = process-friction observations only.

No numeric targetability score is permitted.

## Fresh real P1 scope — APPROVED AND MERGED

Product Owner approval:

APPROVE_NY_MVP1_REAL_P1_TARGETABILITY_EXECUTION_SCOPE_V1

The approval covered the design scope only.

It did not authorize:

- source access;
- remote preflight;
- download;
- real candidate materialization;
- real owner PII processing;
- external PII queries;
- identity/contact enrichment;
- outreach;
- value research;
- representation;
- claim activity.

## Offline real P1 runner — APPROVED, MERGED AND POST-MERGE VERIFIED

Product Owner approval:

APPROVE_NY_MVP1_REAL_P1_TARGETABILITY_RUNNER_OFFLINE

The runner implements D-013.

### L0

Streams the authorized local source and derives only:

- structural shape;
- exact IN03;
- Property Owner Count = 1;
- Property ID presence boolean;
- Holder Report Year;
- source ordinal.

Owner Name/address are not decoded or buffered for ranking.

### L1

Second pass over the same already-authorized local archive.

If L2-A is NOT pre-authorized, the selected ordinal is verified without field-buffering direct owner PII.

L1-only verifies:

- structural shape;
- Property ID presence boolean;
- Property Type Code;
- Property Owner Count;
- Holder Report Year.

L1-only does not field-buffer:

- Property ID value;
- Owner Name;
- Holder Name;
- address fields.

If L2-A is fully pre-authorized before download, direct selected-candidate PII may be transiently materialized only for that separately approved targetability purpose.

No durable/returned/logged owner PII.

L1 external paid spend:

USD 0.00

### L2-A

Defined as a provider-binding seam only.

No production provider is approved.

No CLI provider option exists.

If separately approved in the future:

- external paid spend remains USD 0.00;
- manual research cap is 900 seconds;
- provider must be specifically bound to an approved privacy/terms/budget review;
- provider output must remain non-PII targetability evidence.

## Fresh approval state

Seven P1 gate templates are canonical on main.

Verified after merge:

1. P1 transient local-file gate — NOT_GRANTED
2. P1 L1 transient-PII gate — NOT_GRANTED
3. P1 fresh-listing preflight gate — NOT_GRANTED
4. P1 L1 execution gate — NOT_GRANTED
5. P1 L2-A targetability-PII gate — NOT_GRANTED
6. P1 L2-A provider/budget gate — NOT_GRANTED
7. P1 L2-A execution gate — NOT_GRANTED

For all seven:

- owner_authorization = null;
- execution_approval_ref = null;
- runner_checkpoint = null.

No real P1 execution grant exists.

## Safety boundary

Current repository state does NOT authorize or perform:

- NY OSC source access;
- remote preflight;
- download;
- real candidate materialization;
- owner PII processing;
- external PII transfer;
- identity/contact enrichment;
- beneficiary matching;
- genealogy;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

## Controller / legal basis / transparency readiness — BIFURCATED REVIEW

Action:

DEFINE_AND_REVIEW_REAL_P1_CONTROLLER_LEGAL_BASIS_AND_TRANSPARENCY_READINESS

Artifacts:

- sources/proposals/ny_mvp1_real_p1_controller_legal_basis_transparency_readiness.v1.json
- schemas/common/ny_mvp1_real_p1_controller_legal_basis_transparency_readiness.schema.json
- tests/contract/test_ny_mvp1_real_p1_legal_readiness_contract.py
- docs/audits/NY_MVP1_REAL_P1_CONTROLLER_LEGAL_BASIS_TRANSPARENCY_READINESS_REVIEW.md

Result:

BIFURCATED_READY_FOR_CONTROLLER_OPERATING_MODEL_FACTS_NOT_READY_FOR_REAL_P1

The review now distinguishes four factual tracks:

1. US_CONTROLLER_US_MARKET:
   preferred MVP hypothesis pending facts; likely outside GDPR controller scope only if the controller is genuinely US-based, has no relevant EU establishment, does not target/monitor people in the EU, and P1 remains US-only;
2. EU_CONTROLLER_OR_EU_ESTABLISHMENT:
   GDPR Article 3(1) track; Article 6/LIA/Article 14/Article 21/ROPA/DPIA readiness remains required;
3. NON_EU_CONTROLLER_ARTICLE_3_2:
   GDPR may apply if goods/services are offered to or behaviour is monitored for data subjects in the EU;
4. US_CONTROLLER_WITH_EU_PROCESSOR_ONLY:
   an EU processor does not automatically make the US controller subject to GDPR controller obligations under Article 3(1), but the processor may have its own GDPR obligations and roles/contracts require review.

Preferred MVP privacy architecture hypothesis:

- US LSP/controller owns and operates the platform for the US market;
- production owner-PII plane is US-hosted/US-operated by default;
- EU development uses synthetic/non-PII data by default;
- EU developer/contractor access to live owner PII is prohibited absent separate role/territorial-scope review;
- no EU customer targeting or behavioural monitoring for MVP1.

This is a risk-control architecture, not a nominal device to evade applicable law.

Cross-track safeguards remain:

- full Owner Name File acquisition is a material privacy/security event;
- full-file minimisation/security review remains required;
- real L1-only direct-PII necessity remains unresolved;
- all seven P1 execution/privacy gates remain NOT_GRANTED.

No real-source or PII activity was authorized or performed.

## Remaining blocker before any real P1 grant

The project now requires selection of the real controller operating model and factual entity information.

Required facts include:

- US controller, EU controller, or other operating model;
- exact controller legal name;
- entity type;
- formation/incorporation jurisdiction;
- principal establishment/business address;
- whether any EU branch, office, employee, agent or other stable arrangement participates in P1;
- whether any EU person/entity will access live owner PII;
- who signs LSP customer agreements;
- who receives LSP fees;
- confirmation of US-only MVP1 market/no EU targeting or monitoring;
- privacy contact if defined.

These facts must not be inferred from Product Owner identity, account location, GitHub ownership or developer location.

## Stage B / Pilot P1 acceleration — PREPARED OFFLINE

Stage B is now explicitly defined as:

PILOT_P1_ONE_REAL_TARGETABILITY_EXPERIMENT

Objective:

ONE REAL PERSISTENCE-SELECTED IN03 CASE
-> EVIDENCE-BACKED TARGETABILITY DECISION OR BOUNDED STOP
-> MEASURED TARGETABILITY_DECISION_COST
-> HUMAN REVIEW

Acceleration artifacts:

- sources/proposals/ny_mvp1_stage_b_pilot_p1_acceleration.v1.json
- schemas/common/ny_mvp1_stage_b_pilot_p1_acceleration.schema.json
- tests/contract/test_ny_mvp1_stage_b_acceleration_contract.py
- docs/audits/NY_MVP1_STAGE_B_PILOT_P1_ACCELERATION_REVIEW.md

Offline runner improvement:

L1-only selected-record verification no longer field-buffers:

- Property ID value;
- Owner Name;
- Holder Name;
- address fields.

It verifies only non-PII/structural target-selection facts.

The source-file PII gate remains because the archive itself still contains owner PII.

Stage B remaining human dependencies are intentionally reduced to three groups:

1. controller operating model/entity facts;
2. exact L2-A provider or manual research source set;
3. fresh single-use execution approvals.

Claim agreement, outreach, known value, recovery and profitability proof are downstream and are not Stage B exit requirements.

No real source or PII activity was authorized or performed.

## Stage B acceleration — APPROVED AND MERGED

Product Owner approval:

APPROVE_NY_MVP1_STAGE_B_P1_ACCELERATION_OFFLINE_V1

PR #42:

MERGED

Merge commit:

5721b764c4c0dfc89bd3455f9870cee15c17e1d5

Post-merge CI:

36011409899 — SUCCESS

The approval covered repository integration of the Stage B fast-track only.

It did not authorize real P1.

## US-controller fact binding + L2-A manual provider review — PREPARED OFFLINE

Artifacts:

- sources/proposals/ny_mvp1_stage_b_us_controller_fact_binding.v1.json
- schemas/common/ny_mvp1_stage_b_us_controller_fact_binding.schema.json
- sources/proposals/ny_mvp1_stage_b_l2a_manual_provider_review.v1.json
- schemas/common/ny_mvp1_stage_b_l2a_manual_provider_review.schema.json
- tests/contract/test_ny_mvp1_stage_b_us_controller_l2a_manual_review.py
- docs/audits/NY_MVP1_STAGE_B_US_CONTROLLER_L2A_MANUAL_PROVIDER_REVIEW.md

Controller result:

BLOCKED_ONLY_ON_CONTROLLER_ENTITY_FACTS_FOR_US_TRACK_BINDING

No controller/entity fact was invented.

L2-A provider candidate:

google-search-manual-us-v1

Status:

CONDITIONAL_PASS_OFFLINE_NOT_APPROVED_FOR_REAL_PII_QUERY

P1 provider bounds:

- manual browser only;
- US-based authorized controller operator;
- maximum 3 minimized searches;
- maximum 900 seconds;
- USD 0 external cash spend;
- no API;
- no automation/bot;
- no paid data broker;
- no consumer-report/FCRA product;
- no outreach;
- no value research;
- no persisted query strings/URLs/screenshots/snippets;
- Google AI Overview/AI Mode is not accepted as evidence;
- underlying public source page must be verified;
- WebSurrogate is rejected for Stage B commercial research absent express permission/new legal review.

All seven P1 gates remain NOT_GRANTED.

## Stage B US-controller + L2-A manual review — APPROVED AND MERGED

Product Owner approval:

APPROVE_NY_MVP1_STAGE_B_US_CONTROLLER_AND_L2A_MANUAL_REVIEW_V1

PR #43:

MERGED

Merge commit:

97341caddf2da95765ccced4dcbd11ccccdad336

Post-merge CI:

36016356389 — SUCCESS

Accepted offline design:

- preferred operating model remains US_CONTROLLER_US_MARKET;
- factual controller/entity fields remain unset until supplied;
- proposed L2-A provider is google-search-manual-us-v1;
- provider mode is manual-browser-only, US operator, max 3 minimized queries, max 900 seconds, USD 0;
- Google AI summaries/snippets are not evidence;
- underlying source-page verification is required;
- WebSurrogate remains excluded for Stage B commercial research absent express permission/new legal review.

All seven P1 gates remain NOT_GRANTED.

## Competitive Moat Gate — COMPLETE / REFRAME

Artifact:

docs/audits/MVP1_COMPETITIVE_MOAT_GATE_2026-09-24.md

Result:

PASS_WITH_REFRAME_CONTINUE_STAGE_B

Killed claims:

- first AI unclaimed-property platform;
- no competitors;
- unique case prioritization;
- unique owner-location AI.

Closest direct workflow competitor found:

ClaimTrace

Public evidence shows California property-file import, scoring/vetting by recoverable value, owner tractability and risk, evidence-aware research, outreach, legal workflow gates and payment ledger.

Other material competitors include Assethound.ai, Heir Crown, Sparrow, Linking Assets, Ryan, ClaimFound and AssetFynd.

Stage B differentiation hypothesis:

NY_IN03_VALUE_BLIND_TARGETABILITY_ENGINE

This remains useful only as the first experiment.

Long-term product-performance hypothesis:

NORTH_AMERICA_MULTI_REGISTRY_TARGETABILITY_AND_RECOVERY_OPERATING_SYSTEM

The product is differentiated only if it measurably improves registry coverage, lead quality, confidence, identity resolution, operator efficiency, workflow conversion and unit economics.

Proof must come from P1/P2/P3 and later cross-registry outcomes, not feature novelty.

LLC bootstrap hypothesis remains Wyoming LLC, formed just-in-time before real P1 gates, subject to US CPA/attorney review and NY nexus/foreign-qualification analysis.

## Current next action

Return to:

STAGE_B_PILOT_P1

Stage B remains NY OSC-based because that adapter is already validated.

Do NOT reinterpret this as a New York-only product decision.

Immediate dependency:

HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1

After formation:

bind controller facts -> prepare fresh single-use gate packet -> ONE REAL P1 -> human economic review.

If P1/P2 support continuation:

freeze a generic Source Adapter Contract -> prioritize additional US registries -> prioritize Canadian registries -> reuse the same downstream confidence/targetability/people-finder/economics/CRM/contracts/fee engine.

Until a genuine controller exists, keep all seven P1 gates NOT_GRANTED and continue only offline/synthetic/non-PII work.
