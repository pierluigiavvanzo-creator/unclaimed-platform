# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Proposal Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-nonconforming-row-handling-proposal`
- proposal functional package checkpoint: `f29c4423c885d37956bea4aba02e4db241409452`
- proposal package CI: `35093840690` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling.v1.json`
- schema: `schemas/common/property_type_nonconforming_row_handling_proposal.schema.json`
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL.md`
- contract test: `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_proposal.py`
- proposal status: `PROPOSAL_ONLY_NOT_AUTHORIZED`

## Evidence Basis

Source-format diagnostic execution run:

`35090057224` — SUCCESS

Persisted class:

`INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

Source-format human evidence-review decision:

`PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_NO_RUNTIME_CHANGE_AUTHORIZED`

Evidence-review base HEAD:

`27b1a19874449b0170fc0c47328340122d443529`

Evidence-review CI:

`35092673600` — SUCCESS

For the one examined row, retained evidence supports only that:

1. strict full-row UTF-8 decoding succeeded;
2. strict Python stdlib CSV parsing succeeded;
3. exactly one canonical 25-column record was produced;
4. stdlib field index `1` agreed with the current custom projector's PROPERTY_TYPE field;
5. that agreed field still failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Do not infer the exact value, token shape, frequency, cause, source intent or correctness of any transformation.

## Authority State

The archived SCO authority remains the existing provenance basis for the accepted code-shape boundary within its recorded scope:

- enumerated property-type codes use the `AA99` shape except explicit `ZZZZ`;
- `ZZZZ` is supported;
- insurance codes `IN01-IN08` and `IN99` are supported.

The proposal performs and authorizes no new authority retrieval.

## Candidate Handling Options — Design Only

The proposal compares exactly three alternatives:

### `WHOLE_SOURCE_STOP`

Stop the active source path at the first deterministic nonconforming canonical PROPERTY_TYPE field and persist only non-value-bearing control evidence.

### `ROW_LEVEL_DEFER_OR_QUARANTINE`

Treat the row as non-processable and consider continuation only under a separately reviewed deterministic continuation policy. Real-row/field quarantine persistence is a separate privacy expansion and is not authorized.

### `HUMAN_REVIEW_ROUTE`

Stop deterministic processing and route a non-value-bearing human-review event. Showing or retaining the real row/value for row-specific review is a separate privacy expansion and is not authorized.

## No Policy Selected

`selected_option: null`

None of the three options is authorized or implemented by the proposal.

The proposal does not authorize:

- silent row skipping;
- silent source continuation;
- automatic correction;
- semantic acceptance of a nonconforming value;
- trim/case/Unicode normalization;
- regex relaxation;
- parser/projector change;
- real-row quarantine persistence;
- row-specific human inspection;
- source or registry activation;
- production classification activation.

## Non-Value-Bearing Control Vocabulary

Status codes proposed for later review:

- `PROPERTY_TYPE_NONCONFORMING_STOPPED`
- `PROPERTY_TYPE_NONCONFORMING_DEFERRED_POLICY_REQUIRED`
- `PROPERTY_TYPE_NONCONFORMING_HUMAN_REVIEW_REQUIRED`

Reason codes proposed for later review:

- `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`
- `ROW_CONTINUATION_POLICY_NOT_AUTHORIZED`
- `REAL_ROW_RETENTION_NOT_AUTHORIZED`
- `ROW_SPECIFIC_HUMAN_INSPECTION_NOT_AUTHORIZED`

These codes do not contain source-derived values and do not authorize logging/persistence of real row or field content.

## Privacy / Persistence State

Metadata-only proposal preparation creates no new privacy exposure.

The following are explicitly future privacy expansions and remain unauthorized:

- retention of a real nonconforming row or field for quarantine;
- exposure/retention of a real row or field for row-specific human review.

Any such expansion requires a separate reviewed authorization path before real-source execution or persistence expansion.

The proposal defines no approval token.

## Approval Lifecycle

All historical execution/privacy/authority approvals in this chain remain consumed and non-reusable, including:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

None may be reused.

## Runtime / Governance State

Unchanged and fail-closed:

- custom projector unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- handling policy selected: `false`;
- runtime handling change authorized: `false`;
- remediation authorized: `false`;
- another source execution authorized: `false`;
- privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- source continuation after nonconformance authorized: `false`;
- source policy `PROPOSED`;
- registry disabled / not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission BLOCKED.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW`

Review the proposal package and choose a review decision such as `PASS`, `FAIL` or `NEEDS_REMEDIATION` based on the documented option boundaries.

During this review do **not**:

- access `claimit.ca.gov` or authority endpoints;
- inspect or reconstruct the hidden PROPERTY_TYPE value;
- select or implement a runtime handling option silently;
- reuse consumed approvals;
- change parser/projector behavior;
- change or relax the regex;
- apply trim/case/Unicode normalization;
- retain or expose a real row/field;
- authorize source continuation after nonconformance;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.

A PASS on this proposal review may justify a separate handling-policy decision/design artifact, but must not itself implement runtime behavior or authorize real-source execution.
