# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Proposal Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-proposal`
- base review HEAD: `63a6b09cf129202021c80a1c04a479ca2186fe4b`
- base review CI: `35096424256` — SUCCESS
- functional package checkpoint: `56e82a2bde7c1d77ac197dc2ac21f84ecd1a930d`
- package CI: `35097296456` — SUCCESS
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`
- schema: `schemas/common/property_type_nonconforming_row_handling_policy_implementation_proposal.schema.json`
- audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL.md`
- contract test: `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_implementation_proposal.py`
- proposal status: `PROPOSAL_ONLY_NOT_AUTHORIZED`

## Accepted Governing Decision

Decision record:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design policy:

`WHOLE_SOURCE_STOP`

Completed review decision:

`PASS_POLICY_DECISION_ACCEPTED_AS_DESIGN_IMPLEMENTATION_NOT_AUTHORIZED`

D-008 remains a design decision only. Runtime implementation is still unauthorized.

## Evidence Boundary

The retained real-source evidence remains bounded to one previously examined row:

1. strict full-row UTF-8 decoding succeeded;
2. strict stdlib CSV parsing succeeded;
3. exactly one canonical 25-column record was produced;
4. stdlib field index `1` agreed with the custom projector PROPERTY_TYPE field;
5. the agreed field failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Do not infer the exact value, token shape, frequency, cause, source intent or correctness of any transformation.

## Current Runtime Observation — Unchanged

Runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Base blob SHA:

`ae4d3f0ce3fffd6e2e6f45d5611abd1aa4ced30d`

Current execution schema:

`1.1.0`

Historical schema:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Base blob SHA:

`33c829116eea0b568cfe16c664ffbeee9d00e013`

Current mismatch behavior:

- regex mismatch raises `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- result remains `STOPPED_FAIL_CLOSED`;
- `stop_reason` remains `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- the exception already prevents processing later members after the trigger;
- no `control_disposition` exists in runtime output.

No runtime file or historical execution schema was modified while preparing this proposal.

## Proposed Minimal Implementation — Human Review Required

Strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

A later separately authorized implementation would:

1. modify only `scripts/ca_sco_property_type_semantic_verification.py`;
2. create new execution schema `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
3. leave v1.1 schema immutable;
4. preserve every existing v1.1 field and its meaning;
5. change future runner output schema version to `1.2.0`;
6. add nullable top-level `control_disposition`;
7. map only legacy `PROPERTY_TYPE_FORMAT_UNEXPECTED` to:
   - `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
   - `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
8. keep `control_disposition = null` for all other stops and success;
9. preserve source continuation as `false` through the existing fail-closed control flow.

Legacy compatibility is mandatory:

- `semantic_result_status = STOPPED_FAIL_CLOSED` remains;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED` remains;
- no existing field is removed or reinterpreted;
- historical v1.1 evidence remains validated by historical v1.1 schema.

## Validation / Privacy Boundary

Unchanged regex:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Still unauthorized:

- trim;
- ASCII uppercasing;
- Unicode normalization;
- alternate-token acceptance;
- parser/projector change;
- regex relaxation.

Future `control_disposition` may contain only the non-value-bearing `status_code` and `reason_code`.

Forbidden in that control disposition and persistence boundary:

- exact or transformed PROPERTY_TYPE;
- row/field hashes;
- exact row/field lengths;
- PROPERTY_ID;
- owner/holder values;
- source-derived free text;
- real row/field content.

No privacy expansion or row-specific human inspection is proposed.

## Regression Design

A later implementation must be accepted using synthetic/offline tests covering at least:

1. structural mismatch preserves legacy `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the mismatch emits exact D-008 control status/reason;
3. no later member is requested after the trigger;
4. unrelated runner stop leaves control disposition null;
5. success leaves control disposition null;
6. v1.2 rejects source-value-bearing control fields;
7. v1.1 historical schema/evidence remain unchanged;
8. regex/projector/no-normalization guards remain green.

No real-source test is required for implementation acceptance. A future real-source execution remains a separate gate.

## Rollback

Rollback is limited to reverting future implementation commit(s).

No database migration, source-state migration or historical-evidence migration is required.

Rollback restores output schema `1.1.0` and removes future v1.2 control-disposition emission while preserving the historical v1.1 contract.

## Approval / Governance State

No new approval token is defined or granted by this proposal.

All historical execution/privacy/authority approvals remain consumed and non-reusable.

Current state:

- implementation proposal prepared: `true`;
- implementation proposal human-reviewed: `false`;
- policy active in runtime: `false`;
- runtime implementation authorized: `false`;
- v1.2 execution schema created: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- source policy `PROPOSED`;
- registry disabled / not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission BLOCKED.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW`

Review the implementation proposal against D-008, backward compatibility, versioning, regression coverage, rollback, privacy and source-continuation boundaries.

During this review do **not**:

- access `claimit.ca.gov` or authority endpoints;
- inspect/reconstruct the hidden PROPERTY_TYPE value;
- reuse consumed approvals;
- modify the runtime runner;
- create the v1.2 execution schema;
- change parser/projector or regex;
- introduce trim/case/Unicode normalization;
- persist/expose a real row or field;
- enable source continuation;
- grant a real-source execution merely because the proposal passes review;
- activate source policy, registry or production classification;
- enter downstream identity/genealogy/matching/outreach/claim work.

A PASS may authorize or tighten a later implementation gate, but must not silently combine implementation with real-source execution.
