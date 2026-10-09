# NY MVP-1 STAGE B / PILOT P1 ACCELERATION — OFFLINE REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Mode: OFFLINE / NO REAL SOURCE ACCESS

Result:

STAGE_B_FAST_TRACK_PREPARED_OFFLINE

## 1. Stage B definition

For this project, Stage B is Pilot P1:

ONE REAL, BOUNDED, PERSISTENCE-SELECTED IN03 CASE
-> TARGETABILITY DECISION OR BOUNDED STOP
-> MEASURED TARGETABILITY_DECISION_COST
-> HUMAN REVIEW.

Stage B does not require:

- outreach;
- a signed customer agreement;
- known recoverable value;
- claim submission;
- recovery;
- profitability proof.

Those are later discovery/economic stages.

## 2. Baseline

PR #41 legal-readiness bifurcation is merged.

Verified main checkpoint:

6703d98f351f6e5dbc6a7be98f91099dae8f47e4

Post-merge main CI:

36009473009 — SUCCESS

All seven P1 execution/privacy gates remain NOT_GRANTED.

No historical execution approval is reusable.

## 3. Fast-track decision

The Stage B path is reduced to six practical dependencies:

1. controller operating-model/entity facts;
2. L1 privacy minimization;
3. US/NY pre-contact legal/security readiness;
4. exact L2-A provider/manual research source set;
5. fresh single-use approval chain;
6. one P1 execution followed by economic review.

Anything not necessary for those dependencies remains frozen.

## 4. L1-only direct PII minimization

The previous runner performed a second-pass selected-record materialization even when L2-A was not authorized.

That second pass could buffer:

- Property ID value;
- Owner Name;
- Holder Name.

This was not necessary for an L1-only outcome.

The Stage B branch changes the L1-only second pass to verify only:

- structural width;
- Property ID presence boolean;
- Property Type Code;
- Property Owner Count;
- Holder Report Year.

It does not buffer:

- Property ID value;
- Owner Name;
- Holder Name;
- address fields.

Important:

The P1 transient-PII/file gate is NOT removed.

Reason:

the local source archive still contains owner PII and the streaming process still operates on the source file. The code change minimizes field-level materialization; it does not pretend the source file is non-PII.

If L2-A is fully pre-authorized, direct PII materialization remains available only for the selected ordinal and only for the bounded approved targetability purpose.

## 5. US / New York pre-contact scope

Official OSC material states that:

- the Owner Name File is provided for research;
- it contains potential owner names, last-known addresses, property nature and reporting information;
- it can be downloaded as a zipped delimited text file;
- the list is updated quarterly;
- amounts and taxpayer-identification numbers are not included.

OSC's current Location Service Provider page also states that no charge is imposed by OSC for processing claims or returning funds.

Official sources:

- https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers
- https://www.osc.ny.gov/unclaimed-funds/resources/owner-name-file-request-form

## 6. Claim-path requirements are downstream of Stage B

OSC's current Requirements and Procedures for Abandoned Property Location Service Providers state that licensing or registration is not required by OSC.

For the LSP claim path, OSC requires:

- direct contact with the account owner or duly appointed representative;
- a written authorization/fee agreement;
- signature by the owner/authorized estate representative;
- witness/notary acknowledgment;
- disclosure that funds can be obtained directly from OSC without a fee;
- fee no greater than 15%;
- provider collection of its fee from the client rather than OSC withholding the fee.

These requirements are preserved for L3+/claim readiness.

Stage B stops before:

- outreach;
- sale of the service to a contacted candidate;
- agreement execution;
- claim submission.

Therefore the project does not need to implement claim-submission machinery to learn whether P1 is targetable.

Official sources:

- https://www.osc.ny.gov/files/unclaimed-funds/resources/2025/pdf/aplsp-requirements-and-procedures-highlight-changes-1.pdf
- https://www.osc.ny.gov/files/unclaimed-funds/pdf/sample-finder-agreement.pdf
- https://www.nysenate.gov/legislation/laws/ABP/1416
- https://www.nysenate.gov/legislation/laws/GBS/393-E

## 7. Legislative watch — no false blocker

NY Assembly Bill A3372 (2025-2026) proposes changes to disclosures for abandoned-property location-service solicitations/agreements.

As of 2026-09-24, the official NY Senate legislation page shows the bill as ACTIVE / IN ASSEMBLY COMMITTEE.

It is therefore:

MONITOR_DOWNSTREAM

not:

CURRENT_STAGE_B_LAW.

Official source:

https://www.nysenate.gov/legislation/bills/2025/A3372

Before any L3 outreach/agreement work, the project must re-check whether the bill or a successor has become law.

## 8. L2-A fast-track model

Stage B needs L2-A because the P1 question is targetability, not merely deterministic selection.

P1 constraints remain:

- external paid spend = USD 0.00;
- manual research <= 900 seconds;
- no paid API;
- no paid data broker;
- no consumer-report/FCRA product;
- no outreach;
- no value research;
- no genealogy;
- no beneficiary matching.

The preferred P1 implementation is:

MANUAL_BOUNDED_RESEARCH_WITH_NON_PII_RESULT_ENTRY_AND_EXACT_SOURCE_PROVIDER_BINDING.

Reason:

for one case, building a generalized identity/data-broker stack would increase architecture before measuring whether targetability has economic value.

The exact search/provider/source set is still a human/privacy gate.

## 9. Controller fast-track

The preferred legal hypothesis already accepted for review is:

US_CONTROLLER_US_MARKET.

But it remains a hypothesis until the actual entity facts are supplied.

The minimum factual package is:

- exact controller legal name, or explicit ENTITY_NOT_YET_FORMED;
- entity type;
- formation/incorporation jurisdiction;
- principal business/establishment address;
- any relevant EU branch/office/employee/agent/stable arrangement;
- any EU person/entity with live owner-PII access;
- entity that signs LSP agreements;
- entity that receives fees;
- US-only market / no EU targeting or monitoring;
- privacy contact if defined.

These facts are not code and cannot be safely invented.

## 10. What can now run in parallel

While controller facts are supplied, the repository can continue offline on:

- L1 minimization tests;
- Stage B approval packet;
- L2-A provider/source-set review;
- P1 result/economic review templates.

No source access is necessary.

## 11. Stage B exit outcomes

Any of these is a valid P1 result:

- TARGETABLE_CONTINUE_TO_SEPARATE_OUTREACH_REVIEW;
- STOP_SELF_SERVICE_LOW_NEED;
- STOP_UNBOUNDED_RESOLUTION_COST;
- STOP_LEGAL_PRIVACY_SCOPE;
- STOP_TARGETABILITY_NOT_ESTABLISHED_WITHIN_BUDGET.

STOP is useful economic evidence.

## 12. Remaining human input groups

The fast-track intentionally collapses remaining human dependencies to three groups:

1. CONTROLLER_OPERATING_MODEL_AND_ENTITY_FACTS;
2. EXACT_L2A_PROVIDER_OR_MANUAL_RESEARCH_SOURCE_SET;
3. FRESH_SINGLE_USE_EXECUTION_APPROVALS.

No additional architecture should be inserted ahead of P1 unless a concrete blocker requires it.

## 13. Safety boundary

This acceleration work authorizes none of the following:

- remote preflight;
- source download;
- real candidate materialization;
- real owner-PII processing;
- external PII query;
- outreach;
- value research;
- fee agreement;
- claim activity;
- any P1 gate.

## 14. Review result

STAGE_B_FAST_TRACK_PREPARED_OFFLINE

Recommended Product Owner review phrase:

APPROVE_NY_MVP1_STAGE_B_P1_ACCELERATION_OFFLINE_V1

If approved, the next offline action is:

COMPLETE_US_CONTROLLER_FACT_BINDING_AND_L2A_MANUAL_PROVIDER_REVIEW_OFFLINE

The actual P1 remains separately gated.
