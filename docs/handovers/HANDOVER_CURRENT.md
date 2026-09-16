# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-16

## Purpose

Authoritative restart point for a new ChatGPT session. GitHub is the source of truth. Before taking any action, re-read the canonical project files and verify the remote branch HEAD and CI rather than relying on chat memory.

## Repository / Current Branch

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-proposal`
- last verified proposal-final HEAD before this handover refresh: `8682dfd0118e0d2cac107f945585bb5fa332151f`
- proposal-final CI: `35097630322` — **SUCCESS**
- functional package checkpoint: `56e82a2bde7c1d77ac197dc2ac21f84ecd1a930d`
- package CI: `35097296456` — **SUCCESS**

Because this handover refresh itself creates a later documentation commit, the next session must first verify the current remote branch HEAD before acting.

## Mandatory Initial Read Order

Before ANY modification, read in this order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then read the implementation-proposal artifacts below before performing the review.

## Current Implementation-Proposal Package

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`

Schema:

`schemas/common/property_type_nonconforming_row_handling_policy_implementation_proposal.schema.json`

Audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL.md`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_implementation_proposal.py`

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

The proposal package and the final persistent checkpoint both passed the full GitHub CI pipeline.

## Accepted Governing Decision

Decision record:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design policy:

`WHOLE_SOURCE_STOP`

Completed policy-decision review result:

`PASS_POLICY_DECISION_ACCEPTED_AS_DESIGN_IMPLEMENTATION_NOT_AUTHORIZED`

D-008 is accepted as design only. It is **not implemented or activated in runtime**.

## Evidence Boundary

The retained real-source evidence remains bounded to one previously examined row:

1. strict full-row UTF-8 decoding succeeded;
2. strict stdlib CSV parsing succeeded;
3. exactly one canonical 25-column record was produced;
4. stdlib field index `1` agreed with the custom projector `PROPERTY_TYPE` field;
5. the agreed field failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Do not infer or reconstruct:

- the exact `PROPERTY_TYPE` value;
- token shape beyond the retained coarse evidence;
- frequency;
- source intent;
- semantic correctness;
- a supposedly correct transformation.

The accepted policy is a platform-side fail-closed handling design. It does not assert that the hidden source value is semantically invalid in the source system.

## Current Runtime Observation — Unchanged

Runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Verified runner blob SHA at the proposal base:

`ae4d3f0ce3fffd6e2e6f45d5611abd1aa4ced30d`

Current execution schema version:

`1.1.0`

Historical schema:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Verified historical schema blob SHA:

`33c829116eea0b568cfe16c664ffbeee9d00e013`

Current mismatch behavior:

- regex mismatch raises `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- result remains `STOPPED_FAIL_CLOSED`;
- `stop_reason` remains `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- existing fail-closed control flow prevents processing later source members after the trigger;
- no `control_disposition` exists in runtime output.

No runtime file and no historical v1.1 execution schema were modified while preparing the implementation proposal.

## Proposed Minimal Implementation — Human Review Required

Strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

A later separately authorized implementation would:

1. modify only `scripts/ca_sco_property_type_semantic_verification.py`;
2. create `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
3. leave historical v1.1 schema immutable;
4. preserve every existing v1.1 field and its meaning;
5. change future runner output schema version to `1.2.0`;
6. add nullable top-level `control_disposition`;
7. map only legacy `PROPERTY_TYPE_FORMAT_UNEXPECTED` to:
   - `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
   - `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
8. keep `control_disposition = null` for all unrelated stop reasons and successful results;
9. preserve source continuation as `false` through the existing fail-closed control flow.

Legacy compatibility is mandatory:

- `semantic_result_status = STOPPED_FAIL_CLOSED` remains;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED` remains;
- no existing field is removed or reinterpreted;
- historical v1.1 evidence remains validated by the historical v1.1 schema.

## Validation Boundary

Unchanged:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Not authorized:

- trim;
- ASCII uppercasing;
- Unicode normalization;
- alternate-token acceptance;
- parser/projector changes;
- regex relaxation.

## Privacy / Persistence Boundary

Future `control_disposition` may contain only the non-value-bearing:

- `status_code`;
- `reason_code`.

Forbidden from persistence or exposure:

- exact or transformed `PROPERTY_TYPE`;
- row/field hashes;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No privacy expansion, real-row quarantine or row-specific human inspection is proposed or authorized.

## Regression Design

A later implementation must be validated with synthetic/offline tests covering at least:

1. structural mismatch preserves legacy `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the mismatch emits the exact D-008 control status/reason;
3. no later member is requested after the trigger;
4. unrelated runner stop leaves `control_disposition = null`;
5. success leaves `control_disposition = null`;
6. v1.2 rejects source-value-bearing control fields;
7. historical v1.1 schema/evidence remain unchanged;
8. regex/projector/no-normalization guards remain green.

No real-source test is required to accept the code implementation itself. Any future real-source execution remains a separate governance gate.

## Rollback

Rollback is limited to reverting future implementation commit(s).

No database migration, source-state migration or historical-evidence migration is required.

Rollback would restore runner output schema `1.1.0` and remove future v1.2 `control_disposition` emission while leaving the historical v1.1 contract intact.

## Approval / Governance State

No new approval token is defined or granted by the implementation proposal or this handover refresh.

All historical execution/privacy/authority approvals remain consumed and non-reusable.

Current state:

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- implementation proposal prepared: `true`;
- implementation proposal CI-green: `true`;
- implementation proposal human-reviewed: `false`;
- policy active in runtime: `false`;
- runtime implementation authorized: `false`;
- v1.2 execution schema created: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW`

Review the prepared implementation proposal against:

- D-008;
- backward compatibility;
- schema/versioning discipline;
- exact control-vocabulary mapping;
- regression coverage;
- rollback sufficiency;
- privacy/persistence boundary;
- source-continuation boundary;
- separation between code implementation and any future real-source execution.

The review may PASS, FAIL, or require proposal remediation. It must not silently perform implementation.

## Prohibited During the Next Action

Do **not**:

- access `claimit.ca.gov` or authority endpoints;
- inspect, infer or reconstruct the hidden `PROPERTY_TYPE` value;
- reuse consumed approvals;
- modify the runtime runner;
- create the actual v1.2 execution schema;
- change parser/projector or regex;
- introduce trim/case/Unicode normalization;
- persist or expose a real row or field;
- enable source continuation;
- grant real-source execution merely because the proposal passes review;
- activate source policy, registry or production classification;
- enter downstream identity resolution, genealogy, beneficiary matching, outreach or claim work.

A PASS may define the later implementation authorization gate, but must not combine implementation with real-source execution.

## New-Chat Restart Instruction

In a new chat, instruct the model to use GitHub as source of truth, read the five canonical files in the mandatory order above, verify the current branch HEAD and CI, then execute **only**:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW`

No runtime modification is authorized by merely starting the new chat or reading this handover.
