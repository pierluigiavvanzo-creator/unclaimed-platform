# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

The canonical `PROPERTY_TYPE` runner remains at execution schema v1.1.0. The second owner-authorized bounded real California SCO semantic execution was performed exactly once and stopped fail-closed with `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Second real run: `34995672539`  
Execution schema: `1.1.0`  
Result: `STOPPED_FAIL_CLOSED`  
Safe interpretation: decoded, non-empty projected `PROPERTY_TYPE` value failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The offending value/bytes were intentionally not retained and must not be inferred.

The repository-only code-shape provenance review concluded:
`NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE`.

A separate bounded authority archival / provenance acquisition proposal has now been prepared and CI verified. It is proposal-only and creates **no authority retrieval authorization**.

Semantic compatibility remains unresolved and production classification remains inactive.

## Branches / Verified Checkpoints

- stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- canonical development branch: `m2-state-governance-core`
- canonical development HEAD: `e97c1f62959f603bdd3df79538d4b70255594c70`
- second execution closure branch: `m3-ca-sco-property-type-second-semantic-execution`
- second execution closure HEAD: `9d0243987c843172fe46c971ead0bf3947098336`
- code-shape provenance proposal branch: `m3-ca-sco-property-type-code-shape-provenance-offline-proposal`
- provenance proposal SHA: `defed0c211230aad8f8cec6ff80b216223069844`
- provenance proposal CI: `35002920469` — SUCCESS
- code-shape provenance review branch: `m3-ca-sco-property-type-code-shape-provenance-offline-review`
- provenance review result SHA: `b274e9db0a28dae1c9f6a1a25c657978dd27d7b4`
- provenance review CI: `35003900554` — SUCCESS
- provenance review documentation closure HEAD: `dba496d254e94a68f7f74e0b53090cfef972a969`
- authority provenance acquisition proposal branch: `m3-ca-sco-property-type-authority-provenance-acquisition-proposal`
- authority proposal package SHA: `963c205b662cf56260ca7af14d71c65a6916c30f`
- authority proposal CI: `35005451605` — SUCCESS

## Completed and Verified

- M3 California source/legal readiness baseline.
- Immutable raw storage/provenance and privacy/data-minimization controls.
- Streamlit reviewer canonical and verified.
- California SCO `$500+` bounded structure inspection.
- Four canonical CSV members and identical 25-label headers retained.
- Historical first bounded semantic execution frozen under schema v1.0.0.
- v1.1 diagnostic taxonomy remediation implemented and promoted to canonical development.
- Second bounded real semantic execution performed exactly once under v1.1.0.
- Second one-shot workflow removed after execution; steady state remains ABSENT.
- Second execution/privacy approvals are CONSUMED and non-reusable.
- Human review of the offline code-shape provenance proposal: PASS.
- Repository-only provenance classification completed without SCO or authority network access.
- Offline provenance review CI verified.
- Separate bounded authority archival/provenance acquisition proposal prepared.
- Authority proposal schema and contract tests CI verified.

## Code-Shape Provenance Offline Review

Machine evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json`

Classification result:

- `PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1` -> `SUPPORTED_BY_REPOSITORY_EVIDENCE`
- `GENERAL_CODE_SHAPE_AA99` -> `PROVENANCE_INSUFFICIENT`
- `SPECIAL_CODE_ZZZZ` -> `PROVENANCE_INSUFFICIENT`
- `CALIFORNIA_INSURANCE_CODE_SET` -> `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`
- `CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY` -> `SUPPORTED_BY_REPOSITORY_EVIDENCE`

Aggregate: supported `2`; external-reference assertion not archived `1`; provenance insufficient `2`.

## Authority Provenance Acquisition Proposal

Proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_authority_provenance_acquisition.v1.json`

Schema:
`schemas/common/property_type_authority_provenance_acquisition_proposal.schema.json`

Contract test:
`tests/contract/test_ca_sco_property_type_authority_provenance_acquisition_proposal.py`

Proposal status:
`PROPOSAL_ONLY_NOT_AUTHORIZED`

Exactly one pre-existing repository-referenced authority is proposed:
`https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`

If a later separate human authorization permits retrieval, the machine contract limits it to:

- exact HTTPS URL on `www.sco.ca.gov`;
- exactly one `GET`;
- one single PDF, all pages;
- no redirects;
- no retries;
- no query parameters;
- no authentication or cookies;
- max response body `16777216` bytes, explicitly a project safety cap;
- immutable raw PDF archival with SHA-256 and versioned provenance metadata.

The authority archive itself would not prove any semantic claim. A separate post-archive human provenance review is mandatory before any semantic use.

## Fixed Safety / Governance State

Unchanged and fail-closed:

- authority network access authorized by current proposal: `false`
- source policy: `PROPOSED`
- source real-acquisition authorization: `false`
- registry: disabled/unapproved
- approved real sources: `0`
- semantic compatibility: unresolved
- production classification: inactive
- one-shot semantic network workflow: ABSENT
- identity resolution: BLOCKED
- genealogy: BLOCKED
- beneficiary matching: BLOCKED
- outreach: BLOCKED
- claim submission: BLOCKED

No SCO dataset access, `claimit.ca.gov` access, authority retrieval/download, crawling, source-value reconstruction, trimming, uppercasing, normalization, parser change, regex change/relaxation, logging/privacy expansion or third real execution is authorized by the proposal.

## Consumed Approvals

The following approvals were consumed by the second execution and remain non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

They do not authorize authority-document acquisition.

## Next Recommended Action

Perform only:

`HUMAN_PROPERTY_TYPE_AUTHORITY_PROVENANCE_ACQUISITION_PROPOSAL_REVIEW`

Review the bounded proposal, schema and contract tests. Do not retrieve the authority document as part of the review. A later authority retrieval requires a separate explicit authorization artifact/gate; no execution approval token is invented by this proposal.
