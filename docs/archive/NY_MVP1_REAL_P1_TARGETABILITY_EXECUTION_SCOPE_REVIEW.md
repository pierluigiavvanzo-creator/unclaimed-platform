# NY MVP-1 REAL P1 TARGETABILITY EXECUTION SCOPE — OFFLINE REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Result: READY_FOR_HUMAN_SCOPE_REVIEW / REAL_EXECUTION_NOT_AUTHORIZED

## Objective

Define the smallest fresh real-data execution envelope capable of testing one real NY OSC IN03 case for targetability without yet authorizing source access, PII processing, outreach, value research, representation or claim activity.

The governing product question is:

CAN MATERIAL SERVICE NEED AND BOUNDED RESOLVABILITY BE ESTABLISHED CHEAPLY ENOUGH TO JUSTIFY THE NEXT AUTHORIZATION BEFORE RECOVERABLE VALUE IS KNOWN?

## Baseline

Canonical main:

322c38027a2a214246f1a52ca0854b7b93d171b7

Post-merge main CI:

35994103772 — SUCCESS

Targetability strategy:

PRODUCT_STRATEGY_MVP1.md v3.0

Decision:

D-012

Attempt 11 aggregate supply:

203,921 primary IN03 records.

Real candidate materialization remains NOT AUTHORIZED.

## Legal/privacy framing

This artifact is a software/privacy control design, not a legal opinion.

Official NY OSC material confirms that Location Service Providers are recognized, that the downloadable list contains names, last-known addresses, property nature, reporting time and reporter, and that claim amounts and taxpayer identifiers are not disclosed in that list.

New York Abandoned Property Law §1416 regulates fee agreements for abandoned-property location services and caps the applicable fee at 15 percent of recoverable property.

New York General Business Law §393-e requires the direct-free-claim disclosure in solicitations and agreements.

New York GBL §899-aa distinguishes personal information from private information and excludes lawfully public government-record information from the statutory definition of private information. This does NOT make the project treat owner name/address as unrestricted data: project controls continue to treat them as owner PII.

GBL §899-bb requires reasonable safeguards, including disposal, where its private-information scope applies.

If processing occurs in the context of an EU establishment, GDPR territorial scope may apply even where the data processing itself occurs outside the EU. Before real execution, the controller identity/establishment and an applicable Article 6 legal basis must therefore be documented. Legitimate interests is not preapproved by this design. If Article 6(1)(f) is selected, a documented balancing/LIA is required by project policy. Because the proposed data are not collected from the data subject, the execution plan must also address Article 14 transparency obligations and any applicable exception.

Official references:

- https://www.osc.ny.gov/unclaimed-funds/resources/location-service-providers
- https://www.nysenate.gov/legislation/laws/ABP/1416
- https://www.nysenate.gov/legislation/laws/GBS/393-E
- https://www.nysenate.gov/legislation/laws/GBS/899-AA
- https://www.nysenate.gov/legislation/laws/GBS/899-BB
- https://eur-lex.europa.eu/eli/reg/2016/679/

## Architecture choice: two-pass, one-download when fully preauthorized

The future real runner should not buffer owner PII while deciding which candidate wins the persistence-first selection.

Pass 1:

stream the authorized source and retain only:
- structural conformance;
- exact IN03 flag;
- owner-count = 1;
- Property ID present boolean;
- Holder Report Year;
- source record ordinal.

Do not decode/buffer Owner Name or address in the selection pass.

Select:

OLDEST HOLDER REPORT YEAR

with:

LOWEST SOURCE RECORD ORDINAL

as deterministic tie-breaker.

Pass 2:

re-read the same already-authorized local file and decode transient candidate fields only when the selected source ordinal is reached.

This avoids retaining PII for every eligible candidate and avoids a second download.

## L1 scope

L1 materializes exactly one selected candidate.

Transient fields:

- Property ID;
- Property Type Code;
- Property Owner Count;
- Owner Name;
- Holder Name;
- Holder Report Year.

No address fields.

No owner PII is returned, persisted or logged.

Holder Name is also not persisted because the project does not yet have evidence that every holder value is necessarily non-personal.

Allowed durable state is restricted to non-owner case/provenance/economic data.

L1 new external cash spend:

USD 0.00

L1 paid API/data:

NONE.

If L2-A was not separately approved before the download, L1 must dispose the candidate PII, logically delete the local file and stop.

## L2-A scope

L2-A is defined but NOT authorized.

Objective:

ESTABLISH SERVICE NEED + RESOLVABILITY

without outreach or value research.

If separately approved, L2-A may transiently use the selected candidate's OSC last-known address fields in addition to Owner Name and limited reporting metadata.

Proposed experimental limits:

- external paid data/API spend: USD 0.00;
- manual research cap: 900 seconds;
- no paid data broker;
- no consumer-report/FCRA product;
- no account creation or paid login;
- no genealogy;
- no beneficiary matching;
- no outreach;
- no value research.

The 900-second limit is a Product Owner experiment cap proposed only to make P1 bounded. It is not claimed to be an evidence-backed profitability threshold.

A provider/search tool may not receive owner PII merely because this scope is approved. The specific provider/tool must first pass a privacy/terms review and be included in the separately approved L2-A provider/budget grant.

## One-download co-execution

One download may serve L1 + L2-A only when, before the download:

- legal/privacy preconditions are complete;
- transient local-file grant exists;
- L1 transient-PII grant exists;
- fresh source preflight is authorized and passes;
- L1 execution is authorized;
- L2-A PII scope is approved;
- L2-A provider/tool scope is approved;
- L2-A budget is approved;
- L2-A execution is authorized.

Mid-session waiting for a new authorization is prohibited.

If only L1 is approved:

L1 -> disposal -> delete local file -> STOP.

This prevents open-ended PII retention merely to avoid another download.

## Proposed L2-A durable outputs

Allowed:

- service_need_state;
- resolvability_state;
- estate_path_state;
- representative_path_state;
- awareness_state = UNKNOWN_UNTIL_OUTREACH;
- targetability state/class;
- friction lane if separately evidenced;
- targetability-decision cost;
- human research seconds;
- external cash spend;
- generic source type/domain;
- explicit stop reason;
- next information objective.

Forbidden:

- Owner Name;
- Property ID;
- source raw row;
- street address;
- phone/email;
- relatives/beneficiary names;
- PII-derived hashes;
- PII-bearing query strings;
- PII-bearing URLs;
- copied external PII content;
- guessed value/fee/recovery probability.

## Economic ledger

The ledger remains free of direct owner PII.

It may remain linkable through source ordinal/snapshot/case ID and therefore must not be represented as guaranteed anonymous data.

The ledger must record:

- selection rule/version;
- Holder Report Year;
- persistence signal;
- targetability axes and class/null;
- TARGETABILITY_DECISION_COST;
- PRE_VALUE_DISCOVERY_COST;
- machine/data/human time;
- external spend;
- legal/privacy scope reference;
- authorization references;
- stop reason;
- disposal result.

Value remains:

UNKNOWN_PRE_CLAIM_REVIEW.

No automatic commercial GO decision is permitted.

## Fresh single-use gates

All future execution gates are new, single-use, non-reusable and zero-retry.

Proposed sequence:

1. HUMAN_NY_MVP1_P1_TRANSIENT_LOCAL_FILE_APPROVAL
2. HUMAN_NY_MVP1_P1_L1_TRANSIENT_PII_APPROVAL
3. HUMAN_NY_MVP1_P1_FRESH_LISTING_PREFLIGHT_AUTHORIZATION
4. HUMAN_NY_MVP1_P1_L1_EXECUTION_AUTHORIZATION

Optional L2-A, all granted before the same download if co-executed:

5. HUMAN_NY_MVP1_P1_L2A_TARGETABILITY_PII_SCOPE_APPROVAL
6. HUMAN_NY_MVP1_P1_L2A_PROVIDER_AND_BUDGET_APPROVAL
7. HUMAN_NY_MVP1_P1_L2A_EXECUTION_AUTHORIZATION

No historical attempt grant is reusable.

## Mandatory stops

Fail closed if:

- controller/applicable-law status is unresolved;
- required legal basis/transparency plan is unresolved;
- fresh listing does not match;
- file/archive bounds are exceeded;
- deterministic IN03/single-owner eligibility cannot be established;
- owner PII would enter L0 ranking;
- owner PII would be persisted/logged/returned at L1;
- L1 requires address/external lookup;
- L1 would incur new external spend;
- L2-A is not separately approved;
- external provider privacy/terms review is missing;
- paid/FCRA data becomes necessary;
- proposed L2-A manual cap is exceeded;
- targetability needs unsupported inference;
- genealogy/beneficiary matching is required;
- outreach/value research/claim/representation is required;
- logical disposal fails.

## Review result

READY_FOR_HUMAN_SCOPE_REVIEW

The scope is deliberately narrow enough to support a real P1 without silently opening a general identity-resolution platform.

Approval of this scope will NOT authorize real execution.

If the Product Owner approves the scope, the next action is:

IMPLEMENT_AND_REVIEW_REAL_P1_TARGETABILITY_RUNNER_OFFLINE

That next action must build/test the runner and fresh approval contracts without accessing NY OSC or processing real PII.
