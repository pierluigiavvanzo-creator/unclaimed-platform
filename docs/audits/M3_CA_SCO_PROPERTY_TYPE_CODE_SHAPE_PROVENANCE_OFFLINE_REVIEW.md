# M3 — CA SCO PROPERTY_TYPE Code-Shape Provenance Offline Review

Date: 2026-09-15  
Status: **COMPLETED OFFLINE — FAIL-CLOSED — NO SEMANTIC CHANGE AUTHORIZED**

## 1. Scope

This review executes only the repository-only provenance classification authorized by the human PASS of `HUMAN_PROPERTY_TYPE_CODE_SHAPE_PROVENANCE_OFFLINE_PROPOSAL_REVIEW` for proposal commit `defed0c211230aad8f8cec6ff80b216223069844`.

No California SCO request, source-body access, external authority lookup, authority download, reconstruction of the offending value, network workflow creation, parser change, regex change, normalization change, privacy expansion, or reuse of consumed execution approvals is performed or authorized.

## 2. Inputs reviewed

Only retained repository artifacts were used:

- `sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`
- `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION.md`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_OFFLINE_DIAGNOSIS.md`
- `tests/unit/test_ca_sco_property_type_offline_diagnosis.py`
- `sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`
- `docs/audits/M3_CALIFORNIA_SOURCE_READINESS.md`
- `scripts/ca_sco_property_type_semantic_verification.py`

The allowed classification vocabulary is exactly:

- `SUPPORTED_BY_REPOSITORY_EVIDENCE`
- `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`
- `PROVENANCE_INSUFFICIENT`

Unknown or ambiguous provenance fails closed to `PROVENANCE_INSUFFICIENT`.

## 3. Classification results

### PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1

**Status:** `SUPPORTED_BY_REPOSITORY_EVIDENCE`

The retained data-scope execution records the same canonical 25-label header for all four CSV members. `PROPERTY_TYPE` is the second label in every retained header. The canonical runner independently uses `PROPERTY_TYPE_INDEX = 1` with zero-based indexing.

**Boundary:** this proves the retained canonical four-member header/current runner mapping. It does not establish what an unobserved future source revision will contain.

### GENERAL_CODE_SHAPE_AA99

**Status:** `PROVENANCE_INSUFFICIENT`

The semantic proposal and runner record/enforce `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`, and synthetic tests demonstrate the implementation is strict. Those artifacts establish implementation behavior, not the complete authoritative grammar of all SCO `PROPERTY_TYPE` values.

No retained authority content in the authorized offline inputs proves that every non-`ZZZZ` value must be exactly two uppercase ASCII letters followed by two digits.

**Boundary:** the current regex remains an implemented assumption, not an authority-proven universal source grammar.

### SPECIAL_CODE_ZZZZ

**Status:** `PROVENANCE_INSUFFICIENT`

`ZZZZ` appears in the current regex and therefore in implementation intent, but no retained authority content in the authorized offline inputs establishes `ZZZZ` as a valid California SCO `PROPERTY_TYPE` special token.

**Boundary:** code/proposal presence is not equivalent to semantic authority.

### CALIFORNIA_INSURANCE_CODE_SET

**Status:** `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`

The semantic proposal explicitly records the California insurance code set `IN01-IN08` and `IN99` and attributes it to an SCO NAUPA document at an external URL. The referenced authority document itself is not retained as an immutable evidence artifact within the approved offline review inputs.

The code set is therefore retained as a repository assertion with an external reference, not as direct offline proof.

**Boundary:** this review does not verify or contradict the external authority statement because external access is outside scope.

### CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY

**Status:** `SUPPORTED_BY_REPOSITORY_EVIDENCE`

The committed privacy-safe synthetic differential test compares the custom projector against `csv.reader(..., strict=True)` on the defined deterministic matrix covering ordinary records, quoted fields, commas, escaped quotes, embedded newline/CRLF cases and quote-all output. The retained audit records that no mismatch was reproduced for that matrix.

**Boundary:** this does not establish universal CSV dialect compatibility and says nothing about the unseen offending source row beyond the already persisted fail-closed result.

## 4. Aggregate result

- `SUPPORTED_BY_REPOSITORY_EVIDENCE`: **2**
- `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`: **1**
- `PROVENANCE_INSUFFICIENT`: **2**

Machine-readable evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.review.v1.json`

Schema:

`schemas/common/property_type_code_shape_provenance_offline_review.schema.json`

## 5. Decision

`NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE`

This review does **not** justify or authorize:

- regex modification or relaxation;
- trimming;
- uppercasing;
- normalization;
- parser modification;
- logging/privacy expansion;
- third real execution;
- authority network access;
- source approval;
- registry activation;
- production classification;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- claim submission.

The second-run execution and privacy approvals remain consumed and non-reusable.

## 6. Product implication

The retained evidence is sufficient to trust the current field position and the bounded synthetic parser differential result, but it is insufficient to treat the entire `AA99|ZZZZ` grammar as externally proven authority.

Because the second real run failed on decoded shape under that rule, changing the implementation before resolving provenance would risk adapting the product to an unverified assumption rather than to an authoritative source contract.

## 7. Governance state

Unchanged and fail-closed:

- source policy: `PROPOSED`;
- registry: disabled/unapproved;
- semantic compatibility: unresolved;
- production classification: inactive;
- identity resolution: blocked;
- genealogy: blocked;
- beneficiary matching: blocked;
- outreach: blocked;
- claim submission: blocked;
- one-shot network workflow: absent.

## 8. Next step

This review creates **no new authorization token**.

A separate human gate is required before any external-authority retrieval, authority-document archival, semantic-contract change, parser/regex modification, or further real execution.

The recommended next decision is whether to prepare a separate, bounded **authority archival / provenance acquisition proposal** that can resolve the two `PROVENANCE_INSUFFICIENT` assumptions and independently verify the externally referenced insurance-code assertion without changing runtime behavior.
