# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy Implementation Proposal Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS — IMPLEMENTATION DESIGN ACCEPTED — RUNTIME IMPLEMENTATION NOT AUTHORIZED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- proposal branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-proposal`
- reviewed remote HEAD: `e9af9d61b2f216de58cd8f3ad6a6925c38aef172`
- reviewed CI: `35098004540` — SUCCESS
- accepted governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- accepted design policy: `WHOLE_SOURCE_STOP`
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`
- proposal schema: `schemas/common/property_type_nonconforming_row_handling_policy_implementation_proposal.schema.json`
- proposal audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL.md`
- proposal contract test: `tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_implementation_proposal.py`

This review is repository-only. It performs no request to `claimit.ca.gov`, no authority-source request, no real-row/field access, no hidden-value reconstruction, no approval-token reuse, no privacy expansion and no runtime modification.

## Decision

`PASS_IMPLEMENTATION_PROPOSAL_ACCEPTED_AS_DESIGN_RUNTIME_IMPLEMENTATION_NOT_AUTHORIZED`

The proposed implementation design is acceptable as the bounded future code/contract/test design for implementing `D-008`.

The accepted strategy is:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

This PASS means only that the design may proceed to a later explicit implementation-authorization gate. It does **not** authorize runtime code changes, creation of the real execution schema `1.2.0`, a real-source execution, source activation, registry activation, privacy expansion or downstream work.

## D-008 conformity

PASS.

The proposal implements the accepted `WHOLE_SOURCE_STOP` design without changing its meaning:

- nonconforming `PROPERTY_TYPE` remains fail-closed;
- source continuation after the trigger remains `false`;
- later members/rows after the trigger remain unprocessed;
- no silent skip is introduced;
- the accepted future control status is exactly `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- the accepted future control reason is exactly `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- no source-value-bearing field is added to the control disposition.

The proposal does not claim that the hidden source value is semantically invalid in the source system.

## Backward compatibility

PASS.

The proposed future implementation preserves the current machine result:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`.

No existing v1.1 field is removed or reinterpreted. Historical evidence remains governed by the immutable v1.1 execution schema.

The future control metadata is additive rather than a replacement for the legacy result.

## Versioning discipline

PASS.

Current runtime contract remains:

`1.1.0`

The proposal correctly requires a future new contract:

`1.2.0`

and forbids modifying the historical file:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

The future v1.2 contract adds only nullable top-level `control_disposition` metadata while retaining the v1.1 fields and meanings.

No actual v1.2 execution schema is created by this review.

## Exact control mapping

PASS.

Only the legacy stop reason:

`PROPERTY_TYPE_FORMAT_UNEXPECTED`

may map to:

- `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

All other runner stops and successful outcomes must keep:

`control_disposition = null`

This avoids broad reinterpretation of unrelated stop reasons.

## Validation boundary

PASS and unchanged.

Regex remains:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The design authorizes no:

- trim;
- ASCII uppercasing;
- Unicode normalization;
- alternate-token acceptance;
- parser/projector change;
- regex relaxation.

## Fail-closed and continuation boundary

PASS.

The current runner already raises `RunnerStop("PROPERTY_TYPE_FORMAT_UNEXPECTED")` inside member processing. The exception exits the current member processing and is caught by `execute()`, which returns `STOPPED_FAIL_CLOSED`; therefore no later canonical member is requested after the trigger.

The implementation design appropriately reuses this existing behavior instead of introducing a second stop or continuation mechanism.

Source continuation remains:

`false`

No continuation state is proposed for persistence in `control_disposition`.

## Regression coverage

PASS as implementation-design coverage.

A later authorized implementation must provide synthetic/offline regression coverage proving at least:

1. structural mismatch preserves `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the same mismatch emits exactly the D-008 control status/reason;
3. no later member is requested after the trigger;
4. an unrelated runner stop leaves `control_disposition = null`;
5. a successful result leaves `control_disposition = null`;
6. v1.2 rejects source-value-bearing control fields;
7. historical v1.1 schema/evidence remain unchanged and valid;
8. regex, projector and no-normalization guards remain green.

A real-source execution is not required to accept the future code implementation. Real-source execution remains a separate later governance gate.

## Rollback

PASS.

The proposed implementation is reversible by reverting only the future implementation commit(s).

No database migration, source-state migration or historical-evidence migration is required. Rollback restores runner output schema version `1.1.0` and removes the future v1.2 `control_disposition` emission while leaving historical v1.1 evidence intact.

## Privacy / persistence boundary

PASS.

Future `control_disposition` may persist only the non-value-bearing:

- `status_code`;
- `reason_code`.

It must not persist or expose:

- exact or transformed `PROPERTY_TYPE`;
- row/field hashes;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No row-specific human inspection, real-row quarantine or privacy expansion is introduced.

## Implementation / execution separation

PASS.

Three boundaries remain separate:

1. this review accepts only the implementation **design**;
2. a later explicit gate may authorize the runtime/schema/test implementation;
3. any future execution against the real CA SCO source requires another separate authorization path after implementation validation.

No implementation authorization and no real-source execution authorization are granted by this review.

## Governance state after review

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- implementation proposal prepared: `true`;
- implementation proposal human-reviewed: `true`;
- implementation design accepted: `true`;
- runtime implementation authorized: `false`;
- runtime modified by this review: `false`;
- v1.2 execution schema created: `false`;
- policy active in runtime: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- normalization unchanged;
- historical execution/privacy/authority approvals consumed and non-reusable;
- no new approval token defined or granted;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next explicit gate

The next action is an owner/human implementation-authorization decision only:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION`

If that later gate authorizes implementation, its scope must be restricted to the reviewed code/contract/test delta and synthetic/offline validation. It must not simultaneously authorize or perform real-source execution.

## Explicitly still prohibited

Until a later authorization says otherwise, do not:

- modify `scripts/ca_sco_property_type_semantic_verification.py`;
- create `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
- access `claimit.ca.gov` or new authority sources;
- infer or reconstruct the hidden `PROPERTY_TYPE` value;
- change parser/projector or regex;
- add trim, case conversion or Unicode normalization;
- reuse consumed approval tokens;
- persist real rows/fields or expand privacy scope;
- enable source continuation;
- activate source policy, registry or production classification;
- enter identity resolution, genealogy, beneficiary matching, outreach or claim submission.
