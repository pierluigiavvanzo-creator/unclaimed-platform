# M3 California SCO — PROPERTY_TYPE Diagnostic Execution / Authorization Artifact

Date: 2026-09-15

Status: **PREPARED OFFLINE — PENDING HUMAN AUTHORIZATION — NO DIAGNOSTIC EXECUTION AUTHORIZED**

## Purpose

This artifact converts the human-reviewed diagnostic/remediation evidence proposal into a separately reviewable execution authorization contract.

It does not perform California SCO or `claimit.ca.gov` network access, does not inspect real rows, does not execute the diagnostic, and does not authorize remediation or runtime semantic changes.

## Verified base

Review branch:

`m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal-review`

Review HEAD:

`06896084475f0f899fc3e002344e22fc49ffa54d`

Completed review gate:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

Review decision:

`PASS`

Reviewed proposal package checkpoint:

`020044d3013449fabe566c5164b8f99f9d8cc9ab`

Reviewed proposal HEAD:

`847cdf5daaa1834c3ce11fc3d6f29e2bbc36b4b4`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW.md`

## Authorization artifact

Machine-readable artifact:

`sources/proposals/ca_sco_segment_500_plus.property_type_diagnostic_execution_authorization.v1.json`

Schema:

`schemas/common/property_type_diagnostic_execution_authorization.schema.json`

Status:

`PENDING_HUMAN_AUTHORIZATION`

Current gate:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

## Fresh approvals defined, not granted

The artifact defines two fresh and independent approval references:

1. `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
2. `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both are:

- single-use;
- non-reusable;
- required to pin the reviewed authorization-artifact SHA;
- currently `granted: false`;
- jointly required before any diagnostic network access.

No approval evidence file is created during preparation.

The following prior approvals remain consumed and cannot satisfy either new gate:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

## Bounded execution contract

If and only if a later human review passes and both fresh approvals are validly granted, the diagnostic remains bounded to the previously reviewed scope:

- exact endpoint: `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- pinned content length, ETag, media type and byte-range support;
- first canonical member only: `From_500_To_Beyond_1_of_4.csv`;
- maximum `4` transient data rows;
- stop at first reproduced format mismatch;
- maximum `1` HEAD;
- maximum `1` Range GET;
- maximum `2` HTTP requests total;
- maximum `131072` source response-body bytes total;
- maximum `262144` uncompressed transient bytes;
- maximum `32768` bytes per logical record;
- zero retries;
- redirects forbidden;
- additional range forbidden;
- full-body fallback forbidden;
- automatic widening forbidden;
- authority network access forbidden;
- any other source/endpoint access forbidden;
- source identity drift -> `STOP_FAIL_CLOSED`;
- mismatch not reproduced inside the bound -> `STOP_FAIL_CLOSED`.

The artifact does not widen any reviewed network, row, byte or privacy boundary.

## Deterministic classifier tightening

The execution artifact implements the mandatory review-stage tightening in contract form.

Classification precedence is fixed:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

The unchanged validation regex is:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

### Surrounding whitespace probe

Only leading/trailing:

- `U+0020` SPACE
- `U+0009` TAB

may be removed in-memory for the diagnostic predicate.

The transformed value is never persisted and cannot become an accepted runtime value under this artifact.

### ASCII-only uppercase probe

Only `U+0061`-`U+007A` (`a-z`) map to `U+0041`-`U+005A` (`A-Z`) using the fixed ASCII offset.

All other code points remain unchanged.

Locale-sensitive casing and Unicode normalization are forbidden.

### Non-ASCII / control predicate

Non-ASCII means any code point greater than `U+007F`.

The exact disallowed ASCII control set is:

- every code point `U+0000` through `U+001F` inclusive;
- `U+007F`.

Because classifier precedence is fixed, a boundary TAB that alone makes the field fail the regex is classified first as `SURROUNDING_ASCII_WHITESPACE_ONLY`. An internal TAB, or a TAB not resolved by the prior predicates, remains eligible for `NON_ASCII_OR_CONTROL_CONTENT`.

## Synthetic regression vectors

The artifact contains only synthetic/test values covering all five classes and precedence cases. These values are not source observations and must never be interpreted as evidence about the real SCO row.

Contract tests additionally cover:

- boundary tabs versus control-content precedence;
- combined whitespace + case;
- lowercase `ZZZZ` diagnostic case behavior;
- non-ASCII content;
- internal control content;
- ASCII structural mismatch;
- ASCII-only uppercase preserving non-ASCII code points unchanged.

## Fail-closed semantics

The future diagnostic output has only two statuses:

- `DIAGNOSTIC_CLASSIFIED`
- `STOPPED_FAIL_CLOSED`

When classified:

- `diagnostic_class` must be one of the five fixed classes;
- `fail_closed_reason_code` is null.

When stopped fail-closed:

- `diagnostic_class` is null;
- `fail_closed_reason_code` must be one of the artifact's fixed enumerated reason codes;
- source-derived free text is forbidden.

The reason-code set covers approval failure, source identity drift, request/response failures, budget failures, member/projection/encoding/empty-field failures, non-reproduction within the bound, classifier invariant violations, persistence-boundary violations and network-boundary violations.

## Persistence and privacy boundary

Allowed persisted evidence is limited to:

- result status;
- coarse diagnostic class or null;
- bounded fail-closed reason code or null;
- source identity verification state;
- bounded request counters;
- source response-body byte count;
- transient row count;
- safety flags.

Forbidden from persistence/logging:

- exact `PROPERTY_TYPE`;
- bytes;
- hash;
- exact length;
- fragments;
- codepoints;
- transformed value;
- full row;
- raw response body;
- `PROPERTY_ID`;
- owner/holder values;
- distinct source code lists;
- source-derived free text.

No diagnostic class authorizes remediation.

## Current authorization state

- artifact preparation authorized: `true`
- diagnostic execution authorized: `false`
- transient-row privacy exposure authorized: `false`
- network workflow creation authorized: `false`
- network execution authorized: `false`
- runtime change authorized: `false`
- remediation authorized: `false`
- third real execution authorized: `false`

Implementation state remains:

- source request performed: `false`
- diagnostic execution performed: `false`
- network workflow created: `false`
- runner modified: `false`
- parser modified: `false`
- regex modified: `false`
- normalization modified: `false`
- logging modified: `false`
- persistence modified: `false`

## Governance state

Unchanged:

- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- semantic compatibility: unresolved;
- production classification: inactive;
- downstream identity, genealogy, beneficiary matching, outreach and claim submission gates: closed.

## What preparation does not authorize

This preparation does not authorize:

- either fresh approval;
- source access;
- workflow creation;
- diagnostic execution;
- transient real-row exposure;
- parser or regex change;
- trimming/casing/normalization as runtime behavior;
- remediation;
- source approval;
- registry activation;
- production classification;
- downstream case work.

## Next gate

Perform only:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

A PASS at that gate still does not itself execute the diagnostic. Before network access, both fresh approval evidences must exist, be single-use/non-reusable, and pin the reviewed authorization-artifact package SHA.

Only after both approvals are valid may the project enter:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

After a diagnostic result, stop at:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`
