# HANDOVER_CURRENT.md

Last updated: 2026-09-24

## CURRENT MODE

PRODUCT VALIDATION / TARGETABILITY DISCOVERY

Repository:

pierluigiavvanzo-creator/unclaimed-platform

Canonical branch:

main

Canonical main HEAD:

322c38027a2a214246f1a52ca0854b7b93d171b7

Post-merge main CI:

35994103772 — SUCCESS

PR #36:

MERGED

## Canonical product objective

ONE AUTHORIZED REAL SOURCE
-> ONE TARGETABLE BOUNDED CASE
-> ONE REVIEWABLE ECONOMIC RESULT

Primary rule:

BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE

Target thesis:

MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE

## Proven source state

Attempt 11 established:

- 14,994,489 records;
- 2,792,990 authority-backed insurance records;
- 203,921 primary IN03 aggregate candidates;
- value unknown from source;
- no real candidate materialization yet.

All historical real-source/privacy approvals are consumed/non-reusable.

## Canonical targetability state

PRODUCT_STRATEGY_MVP1 v3.0 and D-012 are canonical.

Selection rule planned for real P1:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Holder Report Year is persistence-only, not a value/awareness/death/contactability signal.

T0-T4 = targetability.

F0-F3 = process friction only.

No numeric targetability score.

## Active work

Branch:

mvp1-real-p1-targetability-execution-scope

Single task:

DEFINE_FRESH_REAL_P1_TARGETABILITY_EXECUTION_SCOPE

Status:

DEFINED / OFFLINE DESIGN ONLY / NOT AUTHORIZED

Artifacts:

- sources/proposals/ny_mvp1_real_p1_targetability_execution_scope.v1.json
- schemas/common/ny_mvp1_real_p1_targetability_execution_scope.schema.json
- tests/contract/test_ny_mvp1_real_p1_targetability_execution_scope_contract.py
- docs/audits/NY_MVP1_REAL_P1_TARGETABILITY_EXECUTION_SCOPE_REVIEW.md

## Proposed real P1 design

### Pass L0

Streaming whole-file selection using only:

- structure;
- exact IN03;
- owner-count = 1;
- Property ID presence boolean;
- Holder Report Year;
- ordinal.

No owner-name/address ranking.

### L1

Second pass on selected ordinal only.

Transient:

- Property ID;
- Property Type Code;
- Property Owner Count;
- Owner Name;
- Holder Name;
- Holder Report Year.

No address.

No owner PII persistence/logging/return.

External cash budget:

USD 0.00.

### L2-A

Defined but separately gated.

May use selected Owner Name + OSC last-known address only after separate PII approval.

Goal:

service need + resolvability.

Proposed P1 L2-A cap:

- paid spend USD 0.00;
- manual research 900 seconds.

No paid data broker/API, FCRA consumer-report product, genealogy, beneficiary matching, outreach or value research.

No provider/search engine may receive owner PII until its privacy/terms use is explicitly reviewed and approved.

## One-download rule

L1 and L2-A may share one download only when every L1/L2-A approval is already granted before the download.

Otherwise:

L1 -> disposal -> local file logical deletion -> STOP.

No mid-session waiting for new authorization.

## Legal/privacy preconditions

Before real execution:

- identify controller;
- record controller establishment;
- determine applicable law;
- document legal basis;
- document transparency obligations/plan.

If GDPR applies, Article 6 basis must be documented; legitimate interests is not preapproved. If Article 6(1)(f) is selected, project policy requires a documented LIA. Article 14 must be analyzed because data are obtained from a source other than the data subject.

## Fresh gates proposed

All single-use/non-reusable/zero-retry:

1. APPROVE_NY_MVP1_P1_TRANSIENT_LOCAL_FILE_ONCE
2. APPROVE_NY_MVP1_P1_L1_TRANSIENT_PII_ONCE
3. AUTHORIZE_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_ONCE
4. AUTHORIZE_NY_MVP1_P1_L1_EXECUTION_ONCE
5. APPROVE_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_ONCE
6. APPROVE_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_ONCE
7. AUTHORIZE_NY_MVP1_P1_L2A_EXECUTION_ONCE

None is currently granted.

## Current prohibitions

Do not perform:

- source access;
- remote preflight;
- download;
- real candidate materialization;
- owner PII processing;
- external PII queries;
- identity/contact enrichment;
- beneficiary matching;
- genealogy;
- outreach;
- value research;
- fee agreement;
- representation;
- claim activity.

## SINGLE NEXT ACTION

HUMAN_REVIEW_NY_MVP1_REAL_P1_TARGETABILITY_EXECUTION_SCOPE_V1

Required Product Owner phrase:

APPROVE_NY_MVP1_REAL_P1_TARGETABILITY_EXECUTION_SCOPE_V1

If approved:

IMPLEMENT_AND_REVIEW_REAL_P1_TARGETABILITY_RUNNER_OFFLINE

The runner implementation remains offline and synthetic/test-only until a later fresh authorization chain.

## Context restart order

1. AGENTS.md
2. PRODUCT_STRATEGY_MVP1.md
3. PROJECT_STATE.md
4. ROADMAP.md
5. DECISIONS.md
6. docs/handovers/HANDOVER_CURRENT.md

Then verify remote main and active feature branch before modification.
