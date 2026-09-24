# PROJECT_STATE.md

Last updated: 2026-09-24

## Authoritative product state

The project is in PRODUCT VALIDATION / TARGETABILITY DISCOVERY MODE.

Primary objective:

ONE AUTHORIZED REAL SOURCE -> ONE TARGETABLE BOUNDED CASE -> ONE REVIEWABLE ECONOMIC RESULT

Primary economic rule:

BUY ECONOMIC INFORMATION BEFORE BUILDING SCALE

Guiding metric:

ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME

## Canonical main

Canonical branch:

main

Current verified main HEAD:

322c38027a2a214246f1a52ca0854b7b93d171b7

Main post-merge CI:

35994103772 — SUCCESS

PR #36:

MERGED

PRODUCT_STRATEGY_MVP1 v3.0 and D-012 are canonical.

## Real-source evidence already established

NY OSC Attempt 11 established:

- 14,994,489 physical records;
- 2,792,990 authority-backed insurance records;
- 203,921 primary IN03 aggregate candidates;
- real candidate materialization: NOT AUTHORIZED;
- recoverable value: UNKNOWN_FROM_SOURCE.

All historical execution/privacy approvals are consumed, non-reusable and zero-retry.

## Current targetability model

Future real P1 selection:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Holder Report Year is persistence evidence only.

Target thesis:

MATERIAL SERVICE NEED x BOUNDED RESOLVABILITY x EVIDENCED COST DISCIPLINE

T0-T4 = targetability.

F0-F3 = process friction only.

No numeric targetability score.

## Fresh real P1 execution scope — HUMAN APPROVED

Scope branch:

mvp1-real-p1-targetability-execution-scope

PR #37:

OPEN / NOT MERGED

Product Owner approval:

APPROVE_NY_MVP1_REAL_P1_TARGETABILITY_EXECUTION_SCOPE_V1

The approval authorized only offline implementation/review of the runner.

It did NOT authorize source access, PII processing or real P1 execution.

## Offline real P1 targetability runner — IMPLEMENTED AND VERIFIED

Active implementation branch:

mvp1-real-p1-targetability-runner-offline

Verified runtime checkpoint:

6a73a4e3da189affe530f6ca9e32259c828e803d

Verified CI:

35997991872 — SUCCESS

Review:

docs/audits/NY_MVP1_REAL_P1_TARGETABILITY_RUNNER_OFFLINE_REVIEW.md

Decision:

D-013

### Runtime architecture

L0 pass:

- streams full authorized TXT member;
- buffers/derives only structural shape, exact IN03, owner-count=1, Property ID presence boolean, Holder Report Year and source ordinal;
- does not decode or buffer Owner Name/address for ranking;
- selects oldest eligible Holder Report Year, then lowest source ordinal.

L1 pass:

- reopens the same already-authorized local archive;
- materially buffers only the selected ordinal;
- transiently permits Property ID, Property Type Code, Property Owner Count, Owner Name, Holder Name and Holder Report Year;
- does not persist/return/log owner PII or Holder Name;
- excludes address unless L2-A was fully pre-authorized.

L2-A seam:

- dependency-injection protocol only;
- no production provider implementation;
- no CLI provider option;
- provider must be bound by approved provider/terms/budget gate;
- external paid spend fixed at USD 0.00;
- manual research capped at 900 seconds;
- returned evidence must be non-PII.

Local archive:

- logically deleted after execution attempt;
- physical secure erasure is not claimed;
- deletion failure => BLOCKED / DISPOSAL_FAILED.

## Fresh approval contracts

Created:

- schemas/common/ny_mvp1_p1_single_use_gate.schema.json
- schemas/common/ny_mvp1_p1_fresh_listing_preflight_receipt.schema.json

Seven gate templates exist under sources/proposals.

All seven currently remain:

NOT_GRANTED

with no owner authorization, no approval ref and no runner checkpoint.

No gate is active.

## Runner contracts and tests

Created:

- src/unclaimed_platform/domain/ny_mvp1_p1_authorization.py
- src/unclaimed_platform/adapters/sources/ny_owner_name_p1_targetability_local.py
- schemas/common/ny_mvp1_real_p1_targetability_run_result.schema.json
- tests/unit/test_ny_mvp1_p1_authorization.py
- tests/unit/test_ny_mvp1_real_p1_targetability_runner.py
- tests/contract/test_ny_mvp1_p1_runner_contracts.py
- scripts/ny_mvp1_p1_targetability_execute.py
- scripts/ny_mvp1_p1_targetability_local.ps1

The production CLI is intentionally L1-only until a provider-specific L2-A review exists.

## Current safety boundary

No source access, remote preflight, download, real candidate materialization, real owner PII processing, external PII query, identity/contact enrichment, beneficiary matching, genealogy, outreach, value research, fee agreement, representation or claim activity is authorized by this implementation milestone.

## Current next action

HUMAN_REVIEW_NY_MVP1_REAL_P1_TARGETABILITY_RUNNER_OFFLINE

If the Product Owner accepts the runner, repository integration may be authorized.

Runner approval must NOT be treated as any of the seven real execution/privacy grants.
