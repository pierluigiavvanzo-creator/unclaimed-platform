# NY MVP-1 STAGE B — US CONTROLLER FACT BINDING + L2-A MANUAL PROVIDER REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Mode: OFFLINE / NO REAL PII / NO SOURCE ACCESS

Result:

PARTIAL_PASS_PROVIDER_CANDIDATE_READY_CONTROLLER_FACTS_STILL_REQUIRED

This review does not constitute legal advice and does not authorize any real P1 gate.

## 1. Baseline

Stage B acceleration PR #42 is merged.

Main checkpoint:

5721b764c4c0dfc89bd3455f9870cee15c17e1d5

Post-merge CI:

36011409899 — SUCCESS

All seven P1 gates remain NOT_GRANTED.

## 2. Controller fact binding

The preferred operating model remains:

US_CONTROLLER_US_MARKET

The repository still does not contain enough facts to bind that model to a real entity.

The project must not invent:

- legal entity name;
- entity type;
- formation state;
- formation jurisdiction;
- principal business address;
- privacy contact;
- EU establishment facts;
- EU live-PII access facts;
- contracting entity;
- fee-receiving entity.

A fact-binding template has therefore been created with null factual fields.

If the intended US company has not yet been formed, the correct factual value later is:

NOT_YET_FORMED

not an invented LLC name.

Real P1 remains blocked until a genuine controller exists and the facts are supplied.

## 3. L2-A manual-provider objective

Stage B needs enough evidence to decide:

- service need;
- resolvability;
- possible estate/representative path;
- T0-T4 or bounded stop;
- TARGETABILITY_DECISION_COST.

It does not need:

- outreach;
- known recoverable value;
- agreement conversion;
- claim submission;
- recovery.

The provider decision should therefore optimize information gained per unit of time, not build a general identity stack.

## 4. Proposed provider candidate

Provider ID:

google-search-manual-us-v1

Mode:

MANUAL_BROWSER_ONLY

Proposed use:

A US-based authorized controller operator performs at most three minimized manual Google Search queries during the separately approved L2-A window.

No API.

No automation.

No bot.

No paid product.

No data broker.

No consumer-report product.

External cash spend:

USD 0.00

Manual cap:

900 seconds.

## 5. Why Google Search is only a discovery tool

Google's current US Terms of Service are effective 2026-07-30 and identify Google LLC as the US service provider.

The Terms explicitly contemplate use of Google services on behalf of an organization/business, subject to an authorized representative accepting the terms.

They also require users to comply with law and respect privacy rights.

Google's current Privacy Policy is effective 2026-05-26.

The Privacy Policy states that activity information can include search terms and that Google collects browser/device/network activity. Depending on settings, signed-in search activity may be stored in account history. Signed-out users still have browser/device-associated controls and processing.

Therefore:

A Google query containing a candidate's name/location is an external PII disclosure/query.

It must never be treated as "free of privacy impact" merely because no cash is paid.

Official sources:

- https://policies.google.com/terms/embedded
- https://policies.google.com/privacy/embedded

## 6. Required query minimization

Maximum search count for P1:

3

This is a Product Owner experiment bound, not a profitability threshold.

Query 1 template:

OWNER_FULL_NAME + LAST_KNOWN_CITY + STATE

Query 2 only if ambiguous:

OWNER_FULL_NAME + LAST_KNOWN_ZIP

Query 3 only if still ambiguous:

OWNER_FULL_NAME + ONE_PUBLIC_CONTEXT_TERM_SELECTED_BY_HUMAN

Do not include unless separately reviewed:

- SSN;
- DOB;
- phone;
- email;
- full street address;
- Property ID;
- beneficiary name;
- relative name.

Never persist:

- actual query string;
- query URL;
- screenshot;
- copied snippet containing PII.

## 7. AI summaries are not evidence

Google AI Overview / AI Mode output is not accepted as targetability evidence.

Search-result snippets are also not sufficient evidence by themselves.

The human researcher must open and verify the underlying public source page.

Durable output remains limited to:

- evidence state;
- source category;
- non-PII source domain;
- opaque evidence reference;
- time/cost;
- targetability result/stop.

No copied PII or page content may enter the Economic Case Ledger.

## 8. Source-page acceptance rule

A page discovered through Google may support Stage B only if:

- it is accessible without login;
- it is not paywalled;
- its terms do not prohibit the intended commercial/research use;
- the human verifies the relevant evidence directly;
- only non-PII evidence metadata are persisted.

If those conditions cannot be satisfied:

STOP.

Do not add more providers during P1.

## 9. WebSurrogate — rejected for Stage B commercial research

New York State Unified Court System WebSurrogate is useful for estate records, but its current Terms of Use state that:

- data may not be mined or sold;
- data may not be used in any pay-for-use application;
- bots may not be used to extract data.

Because this project is evaluating a paid Location Service Provider workflow, WebSurrogate is not approved as a Stage B commercial research source under the current terms.

Status:

REJECTED_FOR_STAGE_B_COMMERCIAL_RESEARCH_ABSENT_EXPRESS_PERMISSION_OR_NEW_LEGAL_REVIEW

This is a project risk decision, not a court ruling about the scope of the terms.

Official source:

https://websurrogates.nycourts.gov/Home/TermsOfUse

## 10. Production-plane boundary

For the preferred US-controller architecture, real P1 Google queries must be performed by:

AUTHORIZED_US_CONTROLLER_OPERATOR

from:

UNITED_STATES

The EU development plane remains synthetic/non-PII by default.

A European developer/operator must not receive live owner PII merely because the tool is technically accessible.

If EU live-PII access becomes necessary:

STOP_AND_REVIEW_ROLE_TERRITORIAL_SCOPE_AND_PROCESSOR_STATUS.

## 11. Session controls

Preferred P1 setup:

- dedicated US business-controlled browser profile;
- no new consumer account required;
- search-history/personalization disabled where available;
- no project-side browser history export;
- no screenshots;
- no query logging;
- no copy of result text into AI tools;
- no API key;
- no automated scraping.

These controls reduce exposure but do not prevent Google itself from processing the search query.

## 12. Provider binding template

Future P1 provider/budget gate may bind exactly:

provider_id:

google-search-manual-us-v1

provider_terms_review_ref:

docs/audits/NY_MVP1_STAGE_B_US_CONTROLLER_L2A_MANUAL_PROVIDER_REVIEW.md

approved_external_cash_budget_cents:

0

approved_manual_research_cap_seconds:

900

paid_api_allowed:

false

paid_data_broker_allowed:

false

consumer_report_fcra_product_allowed:

false

This is only a template.

It is NOT a granted gate.

## 13. Fail-closed conditions

Stop before any query if:

- controller entity is not factually bound;
- operator is not in the US production plane;
- L2-A PII approval is absent;
- provider/budget approval is absent;
- L2-A execution authorization is absent;
- query count would exceed three;
- research time would exceed 900 seconds;
- evidence requires a prohibited/restricted source;
- identity confidence requires unsupported inference;
- outreach becomes necessary;
- value research becomes necessary.

## 14. What is now genuinely blocked

The technical/provider uncertainty has been materially reduced.

The remaining non-code blocker is controller fact binding.

Required human facts:

1. Is the intended controller company already formed?
2. Exact legal name, if formed.
3. Entity type.
4. US state/jurisdiction of formation.
5. Principal business address.
6. Any EU branch/office/employee/agent/stable arrangement relevant to P1.
7. Any EU person/entity that would access live Owner Name File PII.
8. Entity that will sign LSP agreements.
9. Entity that will receive LSP fees.
10. Confirmation that MVP1 is US-only and does not target/monitor persons in the EU.
11. Privacy contact, if already defined.

## 15. Review conclusion

Controller track:

BLOCKED_ONLY_ON_CONTROLLER_ENTITY_FACTS

L2-A manual provider candidate:

CONDITIONAL_PASS_OFFLINE_NOT_APPROVED_FOR_REAL_PII_QUERY

WebSurrogate:

REJECTED_FOR_STAGE_B_COMMERCIAL_RESEARCH_ABSENT_EXPRESS_PERMISSION_OR_NEW_LEGAL_REVIEW

All seven P1 gates:

NOT_GRANTED

## 16. Next human gate

Recommended review phrase:

APPROVE_NY_MVP1_STAGE_B_US_CONTROLLER_AND_L2A_MANUAL_REVIEW_V1

Approval accepts:

- the null-safe controller fact-binding template;
- Google Search manual US as the sole proposed external discovery provider for P1;
- max three queries / 900 seconds / USD 0;
- WebSurrogate exclusion;
- US-only live-PII operating boundary.

Approval does NOT authorize any real Google query, source access, download or P1 execution.

After approval, the only substantive facts still required before preparing the single-use gates are the real controller/entity facts listed above.
