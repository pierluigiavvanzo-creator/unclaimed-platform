# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Proposal

Date: 2026-09-16

Status: **PROPOSAL PREPARED — HUMAN REVIEW REQUIRED — NO RUNTIME CHANGE AUTHORIZED**

## Purpose

Define and compare deterministic fail-closed handling options for the already evidenced condition that the canonical `PROPERTY_TYPE` field is structurally nonconforming under the unchanged validation rule.

This is an offline design artifact only. It performs no source or authority request, no real-row access and no value reconstruction. It does not select or implement a handling policy.

## Evidence basis

Base review branch:

`m3-ca-sco-property-type-source-format-diagnostic-evidence-review`

Base HEAD:

`27b1a19874449b0170fc0c47328340122d443529`

Base CI:

`35092673600` — SUCCESS

Source-format execution run:

`35090057224` — SUCCESS

Retained class:

`INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

Human evidence-review decision:

`PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_NO_RUNTIME_CHANGE_AUTHORIZED`

The reviewed evidence supports only that, for the one examined row, strict UTF-8 decode and strict stdlib CSV parse succeeded, the canonical 25-column shape was produced, stdlib column index `1` agreed with the current projector's `PROPERTY_TYPE` field, and the agreed field still failed the unchanged regex.

The exact field value, derivatives, frequency, cause and source intent remain unknown.

## Validation boundary remains unchanged

The proposal machine-locks:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

and continues to forbid:

- trim before validation;
- ASCII uppercasing/case conversion;
- Unicode normalization;
- alternate-token acceptance;
- parser/projector change;
- regex relaxation.

The archived SCO authority remains the existing provenance basis for the accepted enumerated shape boundary. This proposal performs no additional authority retrieval.

## Candidate handling options

### 1. `WHOLE_SOURCE_STOP`

At the first deterministically detected nonconforming canonical `PROPERTY_TYPE`, stop the active source path and emit only non-value-bearing status/reason evidence.

Benefit: strongest fail-closed boundary and no selective omission of an unexplained source condition.

Cost: one nonconforming row may block useful processing of the source segment until a separately governed decision is made.

### 2. `ROW_LEVEL_DEFER_OR_QUARANTINE`

Treat the row as non-processable and consider continuation only under a separately reviewed deterministic continuation policy.

Benefit: could isolate nonconforming rows while preserving processing of independently conforming rows.

Cost: introduces completeness/selection risk. Persisting a real quarantined row or field would create a new privacy/persistence boundary.

This proposal does **not** authorize continuation, silent skipping or persistence of a real row.

### 3. `HUMAN_REVIEW_ROUTE`

Stop deterministic processing and create a non-value-bearing human-review event.

Benefit: keeps an unknown semantic condition under explicit human governance.

Cost: metadata-only review cannot determine the hidden token's semantics. Showing or retaining the real row/value for row-specific review would require a separately reviewed privacy expansion.

## No option selected

`selected_option` is deliberately `null`.

The proposal does not choose among the three alternatives and does not authorize any of them in runtime.

A later human proposal review may accept, reject or require tightening of the design. Selection or implementation of an actual runtime handling policy remains a later separately governed step.

## Non-value-bearing observability

Proposed status vocabulary:

- `PROPERTY_TYPE_NONCONFORMING_STOPPED`
- `PROPERTY_TYPE_NONCONFORMING_DEFERRED_POLICY_REQUIRED`
- `PROPERTY_TYPE_NONCONFORMING_HUMAN_REVIEW_REQUIRED`

Proposed reason vocabulary:

- `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`
- `ROW_CONTINUATION_POLICY_NOT_AUTHORIZED`
- `REAL_ROW_RETENTION_NOT_AUTHORIZED`
- `ROW_SPECIFIC_HUMAN_INSPECTION_NOT_AUTHORIZED`

These codes contain no source-derived value and do not authorize persistence of:

- exact `PROPERTY_TYPE`;
- transformed/derived `PROPERTY_TYPE`;
- row or field hashes;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row or field content in logs.

## Privacy and persistence boundary

Metadata-only design does not itself expand privacy exposure.

The following are explicitly classified as future privacy expansions and remain unauthorized:

- retaining a real nonconforming row or field for quarantine;
- exposing a real row or field for row-specific human inspection.

Either would require a separate reviewed authorization path before any real-source execution or persistence expansion.

## Approval lifecycle

All seven historical execution/privacy/authority approvals relevant to this chain remain consumed and non-reusable, including both source-format approvals consumed by run `35090057224`.

This proposal defines **no approval token**.

## Runtime and governance state

Unchanged:

- no source or authority network request;
- no real-row access;
- no runner/parser/regex/normalization change;
- no logging or persistence change;
- no source policy or registry modification;
- no source continuation after nonconformance;
- no row skipping or quarantine persistence;
- no remediation;
- source policy remains `PROPOSED`;
- registry remains disabled/unapproved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Durable proposal package

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling.v1.json`

Schema:

`schemas/common/property_type_nonconforming_row_handling_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_proposal.py`

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW`

That review must compare the three options and their governance/privacy consequences. It must not silently select or implement runtime handling, access the source, inspect the hidden value, expand privacy exposure, activate the source or enter downstream work.
