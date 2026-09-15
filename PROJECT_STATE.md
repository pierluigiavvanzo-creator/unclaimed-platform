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

A repository-only code-shape provenance review has now been completed and CI verified. It found that the retained repository evidence does **not** justify changing the semantic rule.

Review decision:
`NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE`

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
- Provenance review schema, machine evidence, audit and contract tests added and CI verified.

## Code-Shape Provenance Offline Review

Machine evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_CODE_SHAPE_PROVENANCE_OFFLINE_REVIEW.md`

Classification result:

- `PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1` -> `SUPPORTED_BY_REPOSITORY_EVIDENCE`
- `GENERAL_CODE_SHAPE_AA99` -> `PROVENANCE_INSUFFICIENT`
- `SPECIAL_CODE_ZZZZ` -> `PROVENANCE_INSUFFICIENT`
- `CALIFORNIA_INSURANCE_CODE_SET` -> `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`
- `CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY` -> `SUPPORTED_BY_REPOSITORY_EVIDENCE`

Aggregate:
- supported by retained repository evidence: `2`
- repository assertion with external reference not archived: `1`
- provenance insufficient: `2`

Important boundary:
- the second-column position is directly supported by the retained four-member headers;
- projector compatibility is supported only for the committed deterministic synthetic CSV matrix;
- the repository records and enforces `AA99|ZZZZ`, but retained evidence does not prove it is the complete authoritative source grammar;
- `IN01-IN08` and `IN99` are retained as a repository assertion attributed to an external SCO authority document whose content is not archived in the approved offline evidence set.

## Fixed Safety / Governance State

Unchanged and fail-closed:

- source policy: `PROPOSED`
- source real-acquisition authorization: `false`
- registry: disabled/unapproved
- approved real sources: `0`
- semantic compatibility: unresolved
- production classification: inactive
- one-shot network workflow: ABSENT
- identity resolution: BLOCKED
- genealogy: BLOCKED
- beneficiary matching: BLOCKED
- outreach: BLOCKED
- claim submission: BLOCKED

No trimming, uppercasing, normalization, parser change, regex change/relaxation, logging expansion, privacy expansion or third real execution is authorized.

## Consumed Approvals

The following approvals were consumed by the second execution and remain non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

Any future real execution requires a new proposal plus fresh explicit execution and transient-row privacy approvals.

## Next Recommended Action

Decide whether to prepare a **separate bounded authority archival / provenance acquisition proposal** to resolve the two `PROVENANCE_INSUFFICIENT` assumptions and independently verify the externally referenced California insurance-code assertion.

This state creates no authorization to access SCO, retrieve/download external authority documents, modify the runner/parser/regex, or perform another real execution. A separate human gate is required before any such action.
