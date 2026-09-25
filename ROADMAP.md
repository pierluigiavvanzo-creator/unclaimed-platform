# ROADMAP.md

Last updated: 2026-09-25

## Product target

UNITED STATES + CANADA MULTI-REGISTRY UNCLAIMED-ASSET INTELLIGENCE AND RECOVERY PLATFORM

Required target capabilities:

- multi-registry acquisition/normalization;
- cross-registry dedup/linking;
- evidence-aware AI confidence scoring;
- lead prioritization;
- people/owner/heir finding;
- case economics;
- jurisdiction-specific compliance;
- contract builder;
- fee calculator;
- CRM/case management;
- authorized outreach/claim workflow;
- outcome learning/calibration.

Patentability is not a roadmap objective.

Performance, reliability and efficiency are the primary product objectives.

## Current critical path — Stage B

ONE AUTHORIZED REAL SOURCE
-> ONE TARGETABLE BOUNDED CASE
-> ONE REVIEWABLE ECONOMIC RESULT

Stage B uses NY OSC as the first validated adapter.

This does NOT limit the product to New York.

Broad simultaneous registry implementation remains deferred until real targetability economics are measured.

## Stage 1 — Aggregate real-source evidence — COMPLETE

NY OSC Attempt 11 established:

- 14,994,489 records;
- 2,792,990 authority-backed insurance records;
- 203,921 primary IN03 aggregate candidates;
- recoverable value UNKNOWN_FROM_SOURCE.

Historical execution/privacy grants are consumed and non-reusable.

## Stage 2 — Synthetic one-candidate materialization — COMPLETE

PR #34 — MERGED.

## Stage 3 — Targetable Opportunity Filter V1 — COMPLETE / CANONICAL

PR #36 — MERGED.

Target thesis:

MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE

T0-T4 targetability is separate from F0-F3 friction.

## Stage 4 — Fresh real P1 execution scope — COMPLETE / CANONICAL

PR #37 — MERGED.

Merge commit:

755bd4c6dbd18e4a204c513e68e456c517e9dbf7

Post-merge CI:

35999157888 — SUCCESS

Product Owner scope approval:

APPROVE_NY_MVP1_REAL_P1_TARGETABILITY_EXECUTION_SCOPE_V1

No real execution was authorized.

## Stage 5 — Offline real P1 runner and approval contracts — COMPLETE / CANONICAL

PR #38 — MERGED.

Verified runner-integration checkpoint:

e2856c61a77e2ff8ca6f973b9090beb87a754ebc

Always verify the live remote `main` HEAD because documentation-only reconciliation commits may follow this checkpoint.

Post-merge CI:

35999333460 — SUCCESS

Product Owner runner approval:

APPROVE_NY_MVP1_REAL_P1_TARGETABILITY_RUNNER_OFFLINE

Implemented:

- two-pass bounded local runner;
- L0 PII-minimized persistence-first selection;
- L1 selected-ordinal transient materialization;
- seven fresh single-use gate contracts/templates;
- preflight receipt contract;
- non-PII run-result/Economic Case Ledger contract;
- disposal fail-closed behavior;
- L2-A provider-binding seam;
- L1-only CLI and PowerShell wrapper.

D-013 is canonical.

## Stage 6 — Gate-state verification — COMPLETE

All seven fresh P1 templates remain:

NOT_GRANTED

No owner authorization or execution reference exists.

## Stage 7 — Controller territorial-scope readiness — COMPLETE / BIFURCATED

PR #41 — MERGED.

Merge commit:

6703d98f351f6e5dbc6a7be98f91099dae8f47e4

Post-merge CI:

36009473009 — SUCCESS

Accepted framework:

- US_CONTROLLER_US_MARKET — preferred MVP hypothesis pending real entity facts;
- EU_CONTROLLER_OR_EU_ESTABLISHMENT — GDPR Article 3(1) track;
- NON_EU_CONTROLLER_ARTICLE_3_2 — conditional EU-targeting/monitoring track;
- US_CONTROLLER_WITH_EU_PROCESSOR_ONLY — separate controller/processor analysis.

All seven P1 gates remain NOT_GRANTED.

## Stage B / Pilot P1 fast-track — PREPARED OFFLINE

Stage B means:

ONE REAL BOUNDED TARGETABILITY EXPERIMENT.

Fast-track lanes:

### B0 — Controller facts — BLOCKED ON HUMAN FACTS

Need only the factual US/EU controller/entity record.

### B1 — L1 privacy minimization — IMPLEMENTED OFFLINE / PENDING REVIEW

L1-only selected-row verification does not field-buffer direct owner PII.

### B2 — US/NY pre-contact readiness — MOSTLY DEFINED

OSC research/list access is separated from downstream claim-path requirements.

No claim/outreach machinery is required to complete Stage B.

### B3 — L2-A provider/manual research binding — NEXT AFTER B0

Constraints:

- USD 0 external paid spend;
- 900-second manual cap;
- no paid API/data broker/FCRA consumer-report product;
- no outreach;
- no value research.

### B4 — Fresh single-use approval chain — NOT STARTED

All seven gates remain NOT_GRANTED.

### B5 — One real P1 — NOT AUTHORIZED

One candidate maximum.

### B6 — Human economic review — CONDITIONAL ON P1

Review targetability result/stop and TARGETABILITY_DECISION_COST before any P2.

## Stage B acceleration integration — COMPLETE

Product Owner approval:

APPROVE_NY_MVP1_STAGE_B_P1_ACCELERATION_OFFLINE_V1

PR #42 — MERGED.

Merge commit:

5721b764c4c0dfc89bd3455f9870cee15c17e1d5

Post-merge CI:

36011409899 — SUCCESS

## B0 — US controller fact binding — BINDER READY / HUMAN FORMATION FACTS REQUIRED

No entity fact is invented.

Controller Fact Binder V1 is canonical after PR #47.

Merge commit:

06de8ec5c6a2734e5f126174b5483606fca6505a

Post-merge CI:

36050081205 — SUCCESS

Required factual input remains the blocker for binding the preferred US-controller track.

Current factual state:

NOT_YET_FORMED

### B0.1 — Formation-readiness pack — PREPARED OFFLINE

Prepared:

- controller fact packet template;
- formation checklist;
- CPA/attorney question set;
- post-formation-to-P1 runbook.

These artifacts reduce post-formation delay but grant no P1 authority.

All seven P1 gates remain NOT_GRANTED.

## B3 — L2-A manual provider review — PREPARED OFFLINE

Candidate:

google-search-manual-us-v1

Proposed bounds:

- manual US operator only;
- max 3 minimized queries;
- max 900 seconds;
- USD 0;
- no API/bot/data broker/FCRA product;
- no AI-generated summary as evidence;
- no persisted PII query material.

WebSurrogate is excluded for Stage B commercial research under current Terms of Use absent express permission/new legal review.

## Stage B controller/provider review — COMPLETE

Product Owner approval:

APPROVE_NY_MVP1_STAGE_B_US_CONTROLLER_AND_L2A_MANUAL_REVIEW_V1

PR #43 — MERGED.

Merge commit:

97341caddf2da95765ccced4dcbd11ccccdad336

Post-merge CI:

36016356389 — SUCCESS

Accepted offline provider candidate:

google-search-manual-us-v1

All seven P1 gates remain NOT_GRANTED.

## Competitive Moat Gate — COMPLETE / PASS WITH REFRAME

Rapid competitive review found that broad AI/unclaimed-property search, case prioritization, owner research and end-to-end recovery workflows already exist.

Closest workflow competitor:

ClaimTrace — California-focused property import, value/tractability/risk vetting, research, outreach, agreement, claim and payment pipeline.

Stage B hypothesis:

NY_IN03_VALUE_BLIND_TARGETABILITY_ENGINE

Long-term performance hypothesis:

NORTH_AMERICA_MULTI_REGISTRY_TARGETABILITY_AND_RECOVERY_OPERATING_SYSTEM

The target advantage is measured lead quality, confidence, operator efficiency, conversion and case economics — not category novelty.

P1/P2/P3 must create the first proprietary economic/targetability evidence.

LLC formation remains just-in-time before real P1.

Preferred bootstrap state:

Wyoming, subject to US tax/legal and NY nexus review.

## Parallel frontend lane — FRONTEND_PRODUCT_UX_V1_OFFLINE

Status:

MERGED / HUMAN DESIGN SELECTION PENDING

Branch checkpoint:

f9af170ac14153b9f2bfbca19851591792d219c9

CI:

36110319804 — SUCCESS

Three synthetic/no-PII concepts are available:

- A — Intelligence Control Room;
- B — Executive Intelligence;
- C — Evidence Investigation Workspace.

This lane is reversible and does not authorize P1.

No permanent component-library dependency should be added until the Product Owner chooses the preferred composition.

## Parallel decision-engine lane — AUDIT COMPLETE / INTEGRATION DEFERRED

Artifact:

docs/audits/DECISION_ENGINE_BENCHMARK_AUDIT_V1_OFFLINE.md

Reuse-first result:

- deterministic core: KEEP / AUTHORITATIVE;
- Jev: DEFER_FOR_P1 / BENCHMARK_FIRST_AFTER_P1;
- Laya: DEFER / CONDITIONAL_WRAP;
- Open-Jev: INSPIRE / BENCHMARK_ONLY;
- custom decision model: REJECT_NOW.

Economic priority order:

expected error cost -> human minutes saved -> safe automation coverage -> calibration -> privacy/provider overhead -> model inference cost -> latency.

Do not add a model adapter before P1/P2 produces enough labelled domain evidence and the Product Owner decides whether the relevant data class may be processed by an external provider.

## Parallel entity-resolution lane — V1 EXECUTED / NO AUTO-LINKER ADOPTION

Artifact:

docs/audits/ENTITY_RESOLUTION_REUSE_BENCHMARK_V1_OFFLINE.md

Executed synthetic comparison:

- RapidFuzz weighted baseline;
- Dedupe RecordLink;
- Splink probabilistic linkage.

Result:

NO_SAFE_SYNTHETIC_WINNER

Current reuse decisions:

- RapidFuzz: REUSE_AS_FEATURE_PRIMITIVE;
- Splink: DEFER_AND_REBENCHMARK_WITH_DOMAIN_LABELS;
- Dedupe: DEFER_SECONDARY_CHALLENGER;
- custom entity-resolution model: REJECT_NOW.

Do not continue synthetic threshold tuning before Stage B evidence.

Trigger V2 only when labelled P1/P2 identity cases or representative observed field-shape/error patterns exist.

V2 should benchmark normalization explicitly:

libpostal / name normalization -> RapidFuzz features -> Splink/Dedupe -> human review.

## Technical consolidation gate — DEFER UNTIL TRIGGER

Do not convert the technical audit into pre-P1 refactoring.

Start consolidation when:

- P1 supports P2 continuation; or
- real PII is about to enter a web UI; or
- durable multi-user state/audit becomes necessary; or
- multi-registry generic persistence becomes necessary.

Priority sequence when triggered:

authentication/RBAC -> durable database -> durable audit -> stable service/repository interfaces -> integration/security/adversarial tests -> dependency locking -> historical runtime consolidation.

## B0 factual controller binding — NEXT

Return immediately to Stage B.

Execute only:

HUMAN_DECIDE_AND_FORM_US_CONTROLLER_ENTITY_FOR_REAL_P1

After a genuine controller exists:

bind entity facts -> prepare fresh single-use approvals -> one real P1 -> human economic review.

Real P1 remains NOT AUTHORIZED.

## Post-Stage-B source architecture — CONDITIONAL

Only if P1/P2 support continuation:

1. freeze a generic versioned Source Adapter Contract;
2. define canonical normalized RegistryRecord / OpportunityCandidate contracts;
3. create a jurisdiction/source capability matrix;
4. benchmark additional registries by accessibility, legal/terms viability, data richness, refresh rate, candidate density and integration cost;
5. add US registries in evidence-backed priority order;
6. add Canadian registries in evidence-backed priority order;
7. add cross-registry dedup/linking;
8. calibrate AI confidence against observed outcomes;
9. expand modular people-finder providers;
10. activate jurisdiction-aware contract builder, fee calculator and CRM workflows only after relevant legal readiness.

Do not implement registry count as a vanity metric.

## P2 — approximately five cases — CONDITIONAL

Only if P1 supports continuation.

## P3 — approximately 20–30 cases — CONDITIONAL

Only if P2 supports continuation.

## Frozen before evidence justifies it

- simultaneous broad US/Canada registry implementation before Stage B evidence;
- general genealogy platform beyond bounded needs;
- mass outreach;
- paid identity-data stack before unit economics justify it;
- large durable PII database;
- generic agent expansion without measured performance benefit;
- non-critical UI work.

Not frozen:

- multi-registry target architecture;
- source-adapter contracts;
- registry-independent downstream interfaces;
- performance instrumentation needed to compare future source adapters.
