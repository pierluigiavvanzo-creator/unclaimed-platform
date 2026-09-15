# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Provenance Review Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-authority-archive-provenance-review`
- archive checkpoint base: `cb4b3a3975794e10cadcbf96a6e22a13cc324dbf`
- authority archival run: `35012019831` — SUCCESS
- authority archive SHA-256: `7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5`
- provenance review package checkpoint SHA: `0b08163c624165fed4394e74265363fab53b2f5a`
- provenance review CI: `35013841037` — SUCCESS
- review audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_AUTHORITY_ARCHIVE_PROVENANCE_REVIEW.md`
- review evidence: `sources/evidence/ca_sco_segment_500_plus.property_type_authority_archive_provenance.review.v1.json`

## Verified Baseline

- M0: VERIFIED
- M1: VERIFIED
- M2: VERIFIED
- M3 authority target provenance: RESOLVED WITH BOUNDED AA99 INTERPRETATION
- M3 live PROPERTY_TYPE semantic compatibility: UNRESOLVED
- second bounded semantic run: `34995672539` -> `STOPPED_FAIL_CLOSED`
- second stop: `PROPERTY_TYPE_FORMAT_UNEXPECTED`
- previous semantic execution/privacy approvals: CONSUMED + NON-REUSABLE
- authority archival approval: CONSUMED + NON-REUSABLE
- source policy: `PROPOSED`
- registry: disabled / not approved
- approved real sources: `0`
- production classification: inactive
- identity/genealogy/beneficiary matching/outreach/claim submission: BLOCKED

## Authority Archive Provenance Review Result

Review gate completed:
`HUMAN_PROPERTY_TYPE_AUTHORITY_ARCHIVE_PROVENANCE_REVIEW`

Machine decision:
`ARCHIVED_AUTHORITY_RESOLVES_TARGET_PROVENANCE_SOURCE_SEMANTIC_MISMATCH_REMAINS`

Reviewed immutable authority:
`sources/authority/ca/sco/upd_naupa_ii_codes_dormancy_periods/7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5.pdf`

Review method:

- existing repository archive only;
- archive SHA-256 and byte count verified before interpretation;
- text extraction used only as a helper;
- all 4 pages rendered and visually reviewed;
- offline extractor run `35013189623` — SUCCESS;
- temporary extractor workflow removed after review;
- no authority network retrieval during review;
- no SCO dataset, `claimit.ca.gov`, source-row or offending-value access during review.

Classifications:

1. `GENERAL_CODE_SHAPE_AA99`
   - `SUPPORTED_BY_ARCHIVED_AUTHORITY_WITH_SCOPE_BOUNDARY`
   - every authority-enumerated Property Type Code other than `ZZZZ` consists of two uppercase Latin letters followed by two digits;
   - this does not state an abstract encoding regex and does not make arbitrary `AA99` tokens semantically valid.

2. `SPECIAL_CODE_ZZZZ`
   - `SUPPORTED_BY_ARCHIVED_AUTHORITY`
   - page 3 lists `ZZZZ` under `All Others` as `Properties Not Identified Above`.

3. `CALIFORNIA_INSURANCE_CODE_SET`
   - `SUPPORTED_BY_ARCHIVED_AUTHORITY`
   - page 1 directly enumerates `IN01` through `IN08` plus `IN99` in the Insurance section.

The current shape regex is not contradicted by the authority. The review does not authorize regex relaxation, trimming, uppercasing, normalization or parser changes.

## Why Semantic Compatibility Is Still Unresolved

The second real bounded run already established that the projected PROPERTY_TYPE decoded successfully, was non-empty, and failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The exact offending value was intentionally not retained and must not be reconstructed or inferred.

The archived authority confirms the target provenance but does not explain why the live source produced a nonconforming value. A separate bounded diagnostic/remediation evidence design is required before further characterization.

## Current Safety Boundary

Do not:

- reuse any consumed approval;
- retrieve the authority again without a new bounded proposal/gate;
- access SCO datasets or `claimit.ca.gov` without a newly authorized bounded scope;
- reconstruct or infer the unretained offending PROPERTY_TYPE value;
- change parser, regex, trimming, casing or normalization;
- classify/remediate the source value under authority of this review;
- run a third PROPERTY_TYPE semantic execution without a new proposal and fresh execution/privacy approvals;
- activate source policy, registry or production classification;
- perform identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## SINGLE NEXT ACTION

Human decision only:

`DECIDE_WHETHER_TO_PREPARE_BOUNDED_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL`

Choose whether to authorize preparation of a separate bounded diagnostic/remediation evidence proposal, or stop this M3 semantic line of work.

No canonical approval token for that proposal-preparation decision is defined by the completed provenance review. Do not invent one silently.

If proposal preparation is authorized, proposal preparation alone must not access SCO, reconstruct the offending value, modify runtime semantics or perform another real execution. Any later diagnostic execution or remediation must pass its own explicit human gate with fresh approvals where required.
