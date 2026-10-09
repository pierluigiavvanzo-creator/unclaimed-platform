# M3 California SCO PROPERTY_TYPE Authority Archive Provenance Review

Date: 2026-09-15

## Classification

D — Diagnostic / Technical.

## Review gate

`HUMAN_PROPERTY_TYPE_AUTHORITY_ARCHIVE_PROVENANCE_REVIEW`

## Result

`ARCHIVED_AUTHORITY_RESOLVES_TARGET_PROVENANCE_SOURCE_SEMANTIC_MISMATCH_REMAINS`

The archived California State Controller's Office authority resolves the previously missing authority provenance for the three targeted PROPERTY_TYPE claims, subject to the shape boundary described below. It does **not** resolve the already observed live-source semantic mismatch and does not authorize any runtime or semantic change.

## Authority reviewed

Immutable archive:

`sources/authority/ca/sco/upd_naupa_ii_codes_dormancy_periods/7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5.pdf`

Verified SHA-256:

`7884f765e66d59526d530c0e90ee952a5ca7a70a99eaa060e5fc775f35a721e5`

Verified size: `329585` bytes.

Archived by one-shot run: `35012019831`.

Archive provenance:

`sources/evidence/ca_sco_property_type_authority_archive.v1.json`

The archival approval is consumed and non-reusable.

## Review method

The review used only the already archived repository copy. No new request to the SCO authority URL and no SCO dataset access occurred.

The archive hash and size were verified first. An offline review workflow then extracted text as a helper and rendered all four PDF pages. All four rendered pages were visually inspected. Offline extractor run: `35013189623`.

Text extraction was not treated as authoritative where layout mattered; the rendered pages were used to verify table membership and section placement.

## Authority observations

### Document scope

Page 1 identifies the document as **Standard NAUPA II Electronic File Format Codes & Dormancy Periods** from the California State Controller's Office, Unclaimed Property Division. It states that the tables represent NAUPA standard codes used by California, then begins the **Property Type Codes** tables. Pages 2 and 3 continue those property-type tables.

### GENERAL_CODE_SHAPE_AA99

Prior claim:

> Every non-ZZZZ PROPERTY_TYPE value must be exactly two uppercase ASCII letters followed by two digits.

Review classification:

`SUPPORTED_BY_ARCHIVED_AUTHORITY_WITH_SCOPE_BOUNDARY`

Across the Property Type Codes enumerated on pages 1-3, every listed property type code other than `ZZZZ` visually consists of two uppercase Latin letters followed by two digits. Page 3 then provides `ZZZZ` in the `All Others` section.

This removes the prior authority-provenance gap for the **enumerated code shape**, but the boundary matters: the PDF does not state an abstract regular expression or declare that every arbitrary token matching `AA99` is semantically valid. It also does not separately state an encoding-level ASCII rule. Therefore the authority supports the necessary shape observed across its enumerated California property-type codes, not unrestricted membership of any `AA99` token.

The existing shape regex is not contradicted by this authority. This review does not authorize changing, relaxing, trimming, uppercasing, or normalizing source values.

### SPECIAL_CODE_ZZZZ

Prior claim:

> ZZZZ is a valid special PROPERTY_TYPE token.

Review classification:

`SUPPORTED_BY_ARCHIVED_AUTHORITY`

Page 3 directly lists `ZZZZ` under `All Others` with the description `Properties Not Identified Above` and a three-year dormancy period. This directly resolves the prior provenance gap for `ZZZZ`.

The proof does not extend to any other four-letter special token.

### CALIFORNIA_INSURANCE_CODE_SET

Prior claim:

> California uses insurance PROPERTY_TYPE codes IN01-IN08 and IN99 as recorded by the semantic proposal.

Review classification:

`SUPPORTED_BY_ARCHIVED_AUTHORITY`

Page 1 contains an `Insurance` section under Property Type Codes and directly enumerates:

- `IN01`
- `IN02`
- `IN03`
- `IN04`
- `IN05`
- `IN06`
- `IN07`
- `IN08`
- `IN99`

The previously external-reference-only repository assertion is now backed by the immutable archived authority.

## What this review does not establish

The second bounded semantic execution previously stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`: the projected value decoded successfully, was non-empty, and did not match the unchanged shape regex. The exact offending value was deliberately not retained and is not reconstructed or inferred here.

The authority review therefore does **not** explain why the live source produced a nonconforming value. It cannot determine whether the source value reflects formatting, source evolution, a data-quality condition, a field-level anomaly, or another cause without a separate bounded diagnostic design.

Accordingly:

- semantic compatibility remains unresolved;
- no parser change is authorized;
- no regex change or relaxation is authorized;
- no trimming, uppercasing, casing conversion, or normalization is authorized;
- no source-value reconstruction or classification is authorized by this review;
- no third real semantic execution is authorized;
- no additional authority retrieval is authorized;
- no source approval, registry activation, or production classification is authorized.

## Safety state

Unchanged:

- source policy: `PROPOSED`;
- registry: disabled and not approved;
- approved real sources: `0`;
- production classification: inactive;
- identity resolution: blocked;
- genealogy: blocked;
- beneficiary matching: blocked;
- outreach: blocked;
- claim submission: blocked;
- prior execution/privacy approvals: consumed and non-reusable;
- authority archival approval: consumed and non-reusable.

## Durable evidence

Machine-readable review:

`sources/evidence/ca_sco_segment_500_plus.property_type_authority_archive_provenance.review.v1.json`

Schema:

`schemas/common/property_type_authority_archive_provenance_review.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_authority_archive_provenance_review.py`

## Next gate

A separate human decision is required before additional diagnostic/remediation work.

Recommended decision:

`DECIDE_WHETHER_TO_PREPARE_BOUNDED_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL`

This review does not define an approval token and does not itself authorize proposal preparation, diagnostic execution, runtime modification, or another real source execution.
