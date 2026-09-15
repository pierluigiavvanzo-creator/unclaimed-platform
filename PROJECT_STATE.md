# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance review is complete and CI-verified. PROPERTY_TYPE semantic compatibility with the live source remains unresolved.

Authority archive provenance review branch:
`m3-ca-sco-property-type-authority-archive-provenance-review`

Review decision:
`ARCHIVED_AUTHORITY_RESOLVES_TARGET_PROVENANCE_SOURCE_SEMANTIC_MISMATCH_REMAINS`

Review evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_authority_archive_provenance.review.v1.json`

Review audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_AUTHORITY_ARCHIVE_PROVENANCE_REVIEW.md`

Review package checkpoint SHA:
`0b08163c624165fed4394e74265363fab53b2f5a`

Review CI:
`35013841037` — SUCCESS

### Authority findings

- `SPECIAL_CODE_ZZZZ`: `SUPPORTED_BY_ARCHIVED_AUTHORITY`.
- `CALIFORNIA_INSURANCE_CODE_SET`: `SUPPORTED_BY_ARCHIVED_AUTHORITY` for `IN01`-`IN08` and `IN99`.
- `GENERAL_CODE_SHAPE_AA99`: `SUPPORTED_BY_ARCHIVED_AUTHORITY_WITH_SCOPE_BOUNDARY`; every property type code enumerated by the authority other than `ZZZZ` uses the two-uppercase-Latin-letter plus two-digit shape, but the authority does not make every arbitrary `AA99` token semantically valid and does not independently state an abstract ASCII regex grammar.

The existing shape regex is not contradicted by the archived authority. No regex, parser, trimming, casing or normalization change is authorized.

### Unresolved live-source issue

The second bounded semantic execution remains the latest real PROPERTY_TYPE source execution:

- run `34995672539`;
- result `STOPPED_FAIL_CLOSED`;
- stop `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- projected PROPERTY_TYPE decoded successfully and was non-empty but did not match the unchanged shape regex;
- exact offending value was not retained and must not be reconstructed or inferred.

The authority review does not explain the source mismatch. Semantic compatibility therefore remains `UNRESOLVED`.

### Governance remains fail-closed

- authority archival approval: CONSUMED + NON-REUSABLE;
- previous semantic execution/privacy approvals: CONSUMED + NON-REUSABLE;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- production classification: inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED;
- no third real semantic execution is authorized;
- no additional authority retrieval is authorized;
- no diagnostic/remediation execution or runtime modification is authorized by the provenance review.

## Next Recommended Action

Human decision only:

`DECIDE_WHETHER_TO_PREPARE_BOUNDED_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL`

This is a proposal-preparation decision only. The completed provenance review defines no approval token and creates no authorization to inspect/reconstruct the unretained source value, access SCO again, modify runtime semantics, or perform another real execution.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
