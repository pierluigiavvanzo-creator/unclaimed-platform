# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy Implementation Authorization

Date: 2026-09-16

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — PASS — BOUNDED IMPLEMENTATION AUTHORIZED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Authorization gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION`

## Authoritative checkpoint reviewed

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- authorization base branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-proposal-review`
- authorization base HEAD: `fd9aa939727812692008358709d0a0b0968fffb2`
- authorization base CI: `35098890574` — SUCCESS
- governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- accepted handling design: `WHOLE_SOURCE_STOP`
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`
- implementation proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`
- human review: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW.md`
- human review result: `PASS_IMPLEMENTATION_PROPOSAL_ACCEPTED_AS_DESIGN_RUNTIME_IMPLEMENTATION_NOT_AUTHORIZED`

The owner has explicitly authorized the reviewed implementation design to proceed to implementation. This authorization changes governance state only. It does not itself modify runtime code, create the v1.2 execution schema, execute against a real source, expand privacy, or activate any source/registry/production path.

## Decision

`PASS_BOUNDED_IMPLEMENTATION_AUTHORIZED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Implementation is authorized only within the exact reviewed boundary below.

## Authorized implementation scope

A subsequent implementation task may:

1. modify `scripts/ca_sco_property_type_semantic_verification.py` only as required by the reviewed design;
2. create `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
3. preserve `schemas/common/property_type_semantic_verification_execution.v1_1.schema.json` unchanged;
4. change future runner output contract version from `1.1.0` to `1.2.0` only as part of the implementation;
5. add nullable top-level `control_disposition` metadata;
6. preserve legacy mismatch output exactly:
   - `semantic_result_status = STOPPED_FAIL_CLOSED`;
   - `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
7. map only `PROPERTY_TYPE_FORMAT_UNEXPECTED` to:
   - `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
   - `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
8. keep `control_disposition = null` for unrelated runner stops and successful results;
9. add or update the minimum synthetic/offline tests required to prove the reviewed regression contract;
10. run repository-local and GitHub CI validation necessary to verify the bounded implementation.

No existing result field may be removed or reinterpreted.

## Validation semantics remain frozen

The regex remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

This authorization does not permit:

- trim;
- ASCII or Unicode case conversion;
- Unicode normalization;
- alternate-token acceptance;
- parser change;
- projector change;
- regex relaxation or replacement.

## Fail-closed / continuation boundary

The implementation must preserve the existing exception-driven stop behavior.

Required invariants:

- `STOPPED_FAIL_CLOSED` remains the legacy machine result for the targeted mismatch;
- `PROPERTY_TYPE_FORMAT_UNEXPECTED` remains the legacy stop reason;
- source continuation after the trigger remains `false`;
- later source members/rows after the trigger remain unprocessed;
- no silent row skip is introduced;
- no second continuation mechanism is introduced.

## Privacy / persistence boundary

The future `control_disposition` may contain only non-value-bearing:

- `status_code`;
- `reason_code`.

The implementation must not persist or expose through the new disposition:

- exact or transformed `PROPERTY_TYPE`;
- derivatives of the hidden value;
- row/field hashes;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No row-specific human inspection or real-row quarantine persistence is authorized.

## Required synthetic/offline regression coverage

Implementation acceptance must prove at least:

1. a synthetic structural mismatch still returns `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. that mismatch emits exactly `PROPERTY_TYPE_NONCONFORMING_STOPPED` and `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE` in `control_disposition`;
3. no later member is requested after the trigger;
4. unrelated runner stops leave `control_disposition = null`;
5. successful results leave `control_disposition = null`;
6. v1.2 rejects source-value-bearing control fields;
7. historical v1.1 schema/evidence remain unchanged and valid;
8. regex, projector and no-normalization guards remain green.

A real-source execution is not required and is not authorized for implementation acceptance.

## Rollback

Rollback remains limited to reverting the implementation commit(s).

No database migration, source-state migration or historical-evidence migration is authorized or required.

Rollback must restore runner output schema version `1.1.0` and remove v1.2 `control_disposition` emission without rewriting historical evidence.

## Explicitly not authorized

This gate does **not** authorize:

- access to `claimit.ca.gov`;
- access to any new authority source;
- any real-source semantic-verification execution;
- reconstruction or inference of the hidden real `PROPERTY_TYPE` value;
- parser/projector changes;
- regex changes or relaxation;
- trim, uppercasing, case conversion or Unicode normalization;
- reuse of consumed historical approval tokens;
- invention or granting of execution/privacy approval tokens;
- persistence of real rows/fields;
- privacy expansion;
- source continuation;
- source-policy activation;
- registry activation;
- production-classification activation;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- claim submission.

## Governance state after authorization

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- implementation proposal reviewed PASS: `true`;
- implementation authorization granted: `true`;
- authorized implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- runtime implementation completed: `false`;
- runtime modified by this authorization gate: `false`;
- execution schema v1.2 created by this authorization gate: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector change authorized: `false`;
- regex/normalization change authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- downstream identity/genealogy/matching/outreach/claim gates remain closed.

## Next single action

Execute only the bounded implementation and synthetic/offline validation authorized above:

`IMPLEMENT_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE`

That implementation task must remain repository-local/offline with respect to the real CA SCO source. It must not be combined with any future real-source execution authorization or execution.
