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

PRODUCT_STRATEGY_MVP1 v3.0, D-012 and D-013 are canonical.

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

Only the selected ordinal is materially buffered.

Transient six-field candidate scope:

- Property ID;
- Property Type Code;
- Property Owner Count;
- Owner Name;
- Holder Name;
- Holder Report Year.

No durable/returned/logged owner PII or Holder Name.

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

## Controller / legal basis / transparency readiness — REVIEWED

Action:

DEFINE_AND_REVIEW_REAL_P1_CONTROLLER_LEGAL_BASIS_AND_TRANSPARENCY_READINESS

Artifacts:

- sources/proposals/ny_mvp1_real_p1_controller_legal_basis_transparency_readiness.v1.json
- schemas/common/ny_mvp1_real_p1_controller_legal_basis_transparency_readiness.schema.json
- tests/contract/test_ny_mvp1_real_p1_legal_readiness_contract.py
- docs/audits/NY_MVP1_REAL_P1_CONTROLLER_LEGAL_BASIS_TRANSPARENCY_READINESS_REVIEW.md

Result:

CONDITIONAL_FAIL_NOT_READY_FOR_REAL_P1

Key findings:

1. canonical repository does not identify the legal controller or its establishment;
2. if the controller is established in the EU, GDPR Article 3(1) may apply regardless of the US source/data-subject location;
3. if GDPR applies, no final Article 6 basis is selected;
4. Article 6(1)(f) legitimate interests is the only currently plausible pre-contact candidate in the present design, but requires a documented three-part LIA before processing;
5. full Owner Name File acquisition is itself part of the personal-data processing scope and must pass necessity/minimisation review;
6. Article 14 transparency is unresolved and no Article 14(5) exception is assumed;
7. Article 21 objection handling is not implemented if legitimate interests is selected;
8. project policy requires a ROPA entry and DPIA screen before real P1 if GDPR applies;
9. real L1-only direct-PII decoding is not yet justified by necessity;
10. all seven P1 execution/privacy gates remain NOT_GRANTED.

No real-source or PII activity was authorized or performed.

## Remaining blocker before any real P1 grant

The project now requires explicit factual identification of the controller before legal readiness can progress.

Required facts:

- exact controller legal name;
- entity type;
- country/jurisdiction of establishment;
- establishment/business address;
- privacy contact if already defined.

These facts must not be inferred from the Product Owner, account holder, repository owner or chat context.

## Current next action

Execute only:

HUMAN_DEFINE_P1_CONTROLLER_IDENTITY_AND_ESTABLISHMENT

After those facts exist, the next offline action will be:

COMPLETE_P1_APPLICABLE_LAW_LIA_TRANSPARENCY_AND_DPIA_SCREEN_OFFLINE

No source access, preflight, download, PII processing or grant creation is authorized.
