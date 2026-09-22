# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy Implementation Proposal

Date: 2026-09-16

Status: **PROPOSAL PREPARED — HUMAN REVIEW REQUIRED — NO RUNTIME IMPLEMENTATION AUTHORIZED**

## Purpose

Define, offline and design-only, the smallest deterministic runtime/contract/test delta needed to implement `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`.

This task does **not** implement the policy. It performs no source or authority request, no real-row/field access, no privacy expansion and no source/registry/production activation.

## Base checkpoint

- branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-decision-proposal-review`
- HEAD: `63a6b09cf129202021c80a1c04a479ca2186fe4b`
- CI: `35096424256` — SUCCESS
- completed gate: `HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW`
- decision: `PASS_POLICY_DECISION_ACCEPTED_AS_DESIGN_IMPLEMENTATION_NOT_AUTHORIZED`
- decision record: `D-008`
- accepted design policy: `WHOLE_SOURCE_STOP`

## Current runtime observation

The existing runner remains:

`scripts/ca_sco_property_type_semantic_verification.py`

Observed blob SHA at the base checkpoint:

`ae4d3f0ce3fffd6e2e6f45d5611abd1aa4ced30d`

The current runner already has the fail-closed control flow required by the accepted design:

1. `PROPERTY_TYPE` is projected by the current unchanged projector;
2. the unchanged regex is evaluated;
3. a mismatch raises `RunnerStop("PROPERTY_TYPE_FORMAT_UNEXPECTED")`;
4. `execute()` catches that stop and returns `semantic_result_status = "STOPPED_FAIL_CLOSED"` with `stop_reason = "PROPERTY_TYPE_FORMAT_UNEXPECTED"`;
5. the exception prevents processing of later source members after the triggering condition.

Therefore D-008 does **not** require a new stop mechanism, parser, normalizer, continuation mechanism or persistence layer.

## Historical execution contract

Current execution schema:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Observed blob SHA:

`33c829116eea0b568cfe16c664ffbeee9d00e013`

Schema version:

`1.1.0`

The v1.1 contract already records the legacy fail-closed result and stop reason. Historical v1.1 evidence must remain valid and reproducible, so the proposal explicitly forbids modifying this schema.

## Minimal implementation strategy

Proposed strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

A later separately authorized implementation would modify exactly one existing runtime file:

`scripts/ca_sco_property_type_semantic_verification.py`

and create one new versioned execution contract:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

No existing execution schema would be modified.

## Future execution contract 1.2.0

The proposed future `1.2.0` execution contract would retain all existing v1.1 fields and semantics and add one nullable top-level field:

`control_disposition`

For the exact legacy condition:

`stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`

it would contain only:

- `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`
- `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`

For every other runner stop and every successful result:

`control_disposition = null`

This makes the D-008 platform control decision explicit without rewriting or reinterpreting the historical runner result.

## Backward compatibility

The later implementation must preserve:

- `semantic_result_status = STOPPED_FAIL_CLOSED` for the existing mismatch;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED` as the legacy machine reason;
- all other existing result fields and meanings;
- the immutable v1.1 schema for historical evidence.

No existing field may be removed or assigned a new meaning.

## Validation boundary

Unchanged:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The implementation proposal authorizes no:

- trim;
- ASCII uppercasing;
- Unicode normalization;
- alternate token acceptance;
- parser/projector modification;
- regex relaxation.

## Continuation boundary

D-008 requires whole-source stop after the trigger.

The current `RunnerStop` control flow already enforces this. The proposed implementation therefore does not add or persist a new continuation state.

Regression tests must prove that after a synthetic `PROPERTY_TYPE_FORMAT_UNEXPECTED` trigger no later canonical member is requested or processed.

Still false:

- continuation after trigger;
- processing later rows/members after trigger;
- silent row skip;
- silent source continuation.

## Privacy / persistence boundary

Only the following non-value-bearing control vocabulary is proposed for future persistence:

- `status_code`
- `reason_code`

The future `control_disposition` must not contain or derive:

- exact `PROPERTY_TYPE`;
- transformed/normalized `PROPERTY_TYPE`;
- hashes of row or field;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No row-specific human inspection is introduced.

The implementation plan therefore requires no privacy expansion.

## Regression coverage required before implementation acceptance

All implementation verification is synthetic/offline.

Required tests:

1. synthetic structural mismatch preserves `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the same mismatch emits exactly the D-008 status/reason in the future v1.2 control disposition;
3. the same mismatch causes no request for a later source member after the trigger;
4. an unrelated `RunnerStop` leaves `control_disposition = null`;
5. a successful result leaves `control_disposition = null`;
6. v1.2 schema rejects source-value-bearing control fields;
7. historical v1.1 schema/evidence remain unchanged and valid;
8. regex, projector and no-normalization guards remain green.

A real-source execution is **not** required to accept the code implementation. Any later real-source execution remains a separate gate with separate authorization requirements.

## Rollback

Rollback is limited to the future implementation commit or commits.

No database migration, source-state migration or historical evidence migration is required.

Rollback would:

- restore runner output schema version `1.1.0`;
- remove future v1.2 `control_disposition` emission;
- leave the historical v1.1 schema and evidence intact.

## Reuse / scope

The proposal reuses:

- the existing deterministic runner;
- the existing `RunnerStop` mechanism;
- the existing legacy stop reason;
- the existing fail-closed loop-exit behavior.

It requires no new external dependency, parser, persistence layer or network workflow.

## Authorization boundary

This artifact authorizes only proposal preparation.

It does **not** authorize:

- runtime code changes;
- creation of the v1.2 execution schema;
- a real-source execution;
- source or authority network access;
- privacy expansion;
- source continuation;
- parser/projector changes;
- regex changes;
- normalization changes;
- source activation;
- registry activation;
- production classification activation.

No new approval token is defined or granted.

All historical execution/privacy/authority approvals remain consumed and non-reusable.

## Preparation evidence

During preparation of this proposal:

- runtime code modified: `false`;
- v1.1 execution schema modified: `false`;
- v1.2 execution schema created: `false`;
- network request to source/authority performed: `false`;
- real row/field access performed: `false`;
- source policy modified: `false`;
- registry modified: `false`.

## Governance state

Unchanged:

- D-008 accepted as design: `true`;
- runtime implementation authorized: `false`;
- policy active in runtime: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- real-source execution authorized: `false`;
- source policy `PROPOSED`;
- registry disabled/unapproved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- downstream identity/genealogy/matching/outreach/claim gates closed.

## Durable package

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`

Schema:

`schemas/common/property_type_nonconforming_row_handling_policy_implementation_proposal.schema.json`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_implementation_proposal.py`

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW`

A future PASS may accept or tighten this implementation design, but must not silently execute a real source or widen privacy/source/registry/downstream permissions.
