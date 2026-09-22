# M3 California SCO $500+ — Field / Privacy / Retention Readiness Review

Date: 2026-09-15

Status: **CANDIDATE — NON-AUTHORIZING — NO NEW SCO NETWORK/BODY ACCESS**

## Purpose

Refine the first real-data triage boundary using the canonical 25-label `$500+` structure evidence and current official California references. This review does not approve the source, PII, row access, registry activation, matching or outreach.

Product purpose remains:

`INSURANCE_RELEVANCE_TRIAGE_ONLY`

## Canonical evidence reused

- `sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`
- four CSV members;
- identical 25-label header candidate;
- zero CSV data rows sampled.

No California SCO request or source-body access was performed by this review.

## Official external references used for review

California SCO publishes standard property type codes used by California, including insurance codes `IN01` through `IN08` and `IN99`:

- `https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`

Examples include individual/group policy benefits, proceeds due beneficiaries, matured policies/endowments/annuities, premium refunds and other insurance amounts.

Privacy references consulted:

- CCPA statute: `https://cppa.ca.gov/regulations/pdf/20260101_ccpa_statute.pdf`
- CPPA data-broker guidance: `https://cppa.ca.gov/data_brokers/`

These references are evidence for review only. The package explicitly records `HUMAN_COUNSEL_REQUIRED`; it does not claim a final legal interpretation or project applicability determination.

## Key review change — HOLDER_NAME removed

The earlier draft proposed three future fields:

- `PROPERTY_ID`
- `PROPERTY_TYPE`
- `HOLDER_NAME`

That scope was too broad for the first purpose. Official SCO/NAUPA property-type documentation already defines insurance-specific property codes. Therefore holder identity is not justified merely to decide whether a record is insurance-related.

Revised proposed persisted/allowed scope:

1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

`HOLDER_NAME` is now **PROHIBITED** for `INSURANCE_RELEVANCE_TRIAGE_ONLY`.

The bulk CSV's actual `PROPERTY_TYPE` row values have not yet been sampled. The proposal therefore does not assume that the bulk field is already proven to use the published code domain. A later separately authorized bounded semantic verification must confirm compatibility before production classification relies on `IN01-IN08/IN99`.

## Field partition

All 25 verified labels remain classified exactly once.

Required:

- `PROPERTY_ID`
- `PROPERTY_TYPE`

Optional:

- none

Prohibited for the first triage purpose:

- `OWNER_NAME`
- all owner address/geography fields
- `HOLDER_NAME`
- all holder address/geography fields

Unresolved/not allowlisted:

- `CASH_REPORTED`
- `SHARES_REPORTED`
- `NAME_OF_SECURITIES_REPORTED`
- `NO_OF_OWNERS`
- `CURRENT_CASH_BALANCE`
- `NUMBER_OF_PENDING_CLAIMS`
- `NUMBER_OF_PAID_CLAIMS`
- `CUSIP`

## Critical transport/privacy finding

Field minimization at persistence time does **not** mean the source can deliver only those two columns.

The verified members are CSV files. No server-side column-projection capability has been established. Reading a real CSV row may therefore transiently expose bytes belonging to prohibited owner/holder columns before the parser discards them.

The machine contract now distinguishes:

- persisted/allowed field scope: two fields;
- transient source-row processing risk: unresolved and separately gated.

Controls fixed by schema:

- no full-row persistence;
- no raw archive persistence;
- no use of nonallowlisted values;
- no persistence of nonallowlisted values;
- row access remains false;
- separate transient-row privacy approval required before any real row access.

## PII conclusion at this gate

The prior header heuristic did not classify `PROPERTY_ID` or `PROPERTY_TYPE` as potential PII labels. The two-field persisted scope therefore contains no field previously flagged by that heuristic.

This does **not** prove that real row processing is PII-free. The source row contains prohibited identity/address columns and any actual row access can transiently process their bytes.

Accordingly:

- real PII authorization remains false;
- actual row PII presence remains unverified;
- no identity resolution, matching or outreach is authorized.

The current CCPA statute excludes information lawfully made available from government records from its definition of personal information, but project applicability, other laws, downstream enrichment, data-broker status and use restrictions require human counsel review. This audit does not decide those issues.

## Retention refinement

The prior seven-day retention candidate was removed because there was no source/legal/product evidence establishing seven days as the correct production duration.

Revised candidate:

- raw ZIP persistence: false;
- full-row persistence: false;
- transient source-row buffer retention: `0 days`;
- transient buffer disposal: immediate after projection or stop;
- projected two-field triage-record retention: unresolved;
- approved retention-policy ref: null.

No production duration is invented.

## Privacy candidate

Status remains `DRAFT_NOT_TRUSTED`.

Candidate allowed fields are exactly:

- `PROPERTY_ID`
- `PROPERTY_TYPE`

Required controls remain encryption at rest, least privilege and access logging. Record values in logs, export, identity resolution, beneficiary matching and outreach remain prohibited. A trusted policy reference remains null.

## Future semantic verification stage

A future stage is defined but intentionally non-executable:

- field: `PROPERTY_TYPE`;
- goal: verify that bulk row values are compatible with official SCO/NAUPA property-type code semantics;
- row limit: not yet selected;
- row access: false;
- network execution: false.

A row/sample limit must be chosen as part of a separate execution proposal; it is not invented here.

## Remaining blockers

- production retention policy not approved;
- project privacy policy not trusted;
- actual row PII presence unverified;
- transient full-row privacy review required;
- bulk `PROPERTY_TYPE` value semantics unverified;
- real-acquisition client not reviewed;
- source approval reference missing;
- source policy remains `PROPOSED`;
- registry remains disabled/unapproved.

## Safety state

This review authorizes none of the following:

- source approval;
- network/body access;
- row access;
- PII processing;
- identity resolution;
- beneficiary matching;
- outreach.

Next gate:

**human/legal transient-row privacy review**, followed—only if approved—by a separately designed bounded semantic-verification proposal for `PROPERTY_TYPE`.
