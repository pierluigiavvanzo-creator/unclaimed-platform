# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy gates, SCO source governance, transport evidence, source-approval readiness, data-scope proposals, segmented transport evidence and the `$500+` bounded structure inspection are canonical on `m2-state-governance-core`.

Canonical development HEAD before the current candidate:
`74af507796f8bcc4ab45baba6abffe6714f9f6c6`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Current Candidate

Branch:
`m3-ca-sco-field-privacy-readiness`

Functional review HEAD:
`648b81b973a4b169c14bcdfd76ac4fa71e76f2e9`.

Functional CI:
`34939909880` — SUCCESS for both `quality` and `streamlit-candidate`.

The candidate is non-authorizing and performed zero new SCO network/body access.

## Canonical `$500+` Structure Evidence

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Verified facts:
- four CSV members;
- identical 25-label header candidate;
- 5 HTTP Range responses in the prior authorized structure-only run;
- total source-body bytes read `393,216`;
- full archive downloaded `false`;
- CSV data rows parsed `0`;
- record values persisted `false`.

## Refined Product Purpose

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Current proposed persisted/allowed row scope is now only:
1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

`HOLDER_NAME` has been removed from the first triage scope and is now prohibited for this purpose.

Reason: official California SCO/NAUPA documentation defines insurance property codes `IN01-IN08` and `IN99`, so holder identity is not justified merely to determine insurance relevance. The bulk CSV's actual `PROPERTY_TYPE` row-value semantics remain unverified because zero data rows have been sampled.

Official code reference:
`https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`.

## Critical Privacy / Transport Boundary

The source members are CSV files and no server-side column projection capability has been established. A real row read may therefore transiently expose bytes from prohibited owner/holder columns before projection, even though those values would not be persisted or used.

Machine controls now require:
- no raw ZIP persistence;
- no full-row persistence;
- no use/persistence of nonallowlisted values;
- real row access `false`;
- separate transient-row privacy approval before any row access.

## PII / Retention State

The two proposed persisted fields were not identified by the prior header heuristic as potential PII labels. This does not establish that real row processing is PII-free because prohibited identity/address columns are present in the same CSV rows.

Retention candidate:
- transient source-row buffer retention: `0 days`;
- disposal: immediate after projection or stop;
- projected triage-record retention duration: unresolved;
- approved retention policy ref: null.

The earlier seven-day candidate was removed because no production/legal evidence justified that duration.

Privacy candidate remains `DRAFT_NOT_TRUSTED`; trusted privacy-policy ref remains null.

## External Privacy Review References

- current CCPA statute reference: `https://cppa.ca.gov/regulations/pdf/20260101_ccpa_statute.pdf`;
- CPPA data-broker guidance: `https://cppa.ca.gov/data_brokers/`.

These are review references only. Project applicability and final legal interpretation remain `HUMAN_COUNSEL_REQUIRED`.

## Authorization State

Unchanged and fail-closed:
- source policy `PROPOSED`;
- real acquisition authorized `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- real row access BLOCKED;
- real PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Current Blocking Items

Before any real row access/acquisition:
- production retention policy approved;
- trusted project privacy policy approved;
- transient full-row privacy review completed;
- bounded `PROPERTY_TYPE` semantic-verification plan approved;
- real-acquisition client reviewed;
- source approval reference assigned;
- source policy separately approved;
- registry separately enabled.

## Next Recommended Action

Human/legal review of the **transient CSV row-processing boundary** and the revised two-field minimization. If accepted, promote this candidate as non-authorizing. Only after a separate later gate design a bounded semantic-verification execution for `PROPERTY_TYPE`; do not read rows yet.
