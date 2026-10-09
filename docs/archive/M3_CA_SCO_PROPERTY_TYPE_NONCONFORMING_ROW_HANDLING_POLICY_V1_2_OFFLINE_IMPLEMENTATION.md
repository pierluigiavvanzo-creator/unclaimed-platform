# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy v1.2 Offline Implementation

Date: 2026-09-16

Status: **IMPLEMENTED OFFLINE — CI GREEN — HUMAN IMPLEMENTATION REVIEW REQUIRED — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Task

`IMPLEMENT_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE`

## Authorization base

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- authorization branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-authorization`
- authorization HEAD: `b98faa9ff6e24404ed8a6028dda21c0cf0041222`
- authorization artifact: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION.md`
- authorization result: `PASS_BOUNDED_IMPLEMENTATION_AUTHORIZED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`
- governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- accepted design policy: `WHOLE_SOURCE_STOP`
- implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

## Implementation branch and functional checkpoint

Implementation branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-offline`

Functional implementation checkpoint:

`f69262a632b6bf0eed1385639aea3c59bb9a94ac`

GitHub Actions CI:

`35100766657` — **SUCCESS**

The implementation and validation were repository-local/offline with respect to the real CA SCO source. No request to `claimit.ca.gov` and no request to a new authority source was performed by this task.

## Implemented runtime delta

Modified:

`scripts/ca_sco_property_type_semantic_verification.py`

The bounded delta is:

1. future runner output schema version is now `1.2.0`;
2. a nullable top-level `control_disposition` is initialized to `null`;
3. only legacy `PROPERTY_TYPE_FORMAT_UNEXPECTED` maps to:
   - `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
   - `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
4. legacy mismatch output remains:
   - `semantic_result_status = STOPPED_FAIL_CLOSED`;
   - `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
5. unrelated stops retain `control_disposition = null`;
6. successful/inconclusive outcomes retain `control_disposition = null`.

No existing result field was removed or reinterpreted.

## New versioned execution contract

Created:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

The v1.2 schema:

- requires `schema_version = 1.2.0`;
- adds only the nullable `control_disposition` control metadata;
- permits inside the non-null disposition only `status_code` and `reason_code`;
- requires the exact D-008 status/reason when `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- requires `control_disposition = null` for all other stop reasons and non-stopped outcomes;
- rejects additional/source-value-bearing fields in `control_disposition`.

Historical contract:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

remains unchanged. Its pre-implementation blob SHA remains:

`33c829116eea0b568cfe16c664ffbeee9d00e013`

## Validation semantics

Unchanged regex:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No implementation change was made to:

- parser;
- projector;
- trim behavior;
- case conversion;
- Unicode normalization;
- accepted token vocabulary;
- transport budget;
- row budget;
- source continuation behavior.

## Fail-closed / continuation behavior

The existing exception-driven fail-closed control flow is reused.

For the targeted structural mismatch:

- `STOPPED_FAIL_CLOSED` remains unchanged;
- `PROPERTY_TYPE_FORMAT_UNEXPECTED` remains unchanged;
- `control_disposition` adds the D-008 metadata;
- processing exits before requesting a later canonical source member;
- source continuation remains `false`;
- no silent row skip or alternate continuation mechanism was introduced.

## Privacy / persistence boundary

The new control metadata contains only non-value-bearing:

- `status_code`;
- `reason_code`.

This implementation does not persist or expose through `control_disposition`:

- exact or transformed `PROPERTY_TYPE`;
- any derivative of the hidden value;
- row/field hashes;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No privacy expansion, real-row quarantine or row-specific human inspection was implemented.

## Regression coverage

Updated synthetic/offline tests prove:

1. a synthetic structural mismatch preserves `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the same mismatch emits exactly `PROPERTY_TYPE_NONCONFORMING_STOPPED` and `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
3. no later member is requested after the trigger;
4. unrelated runner stops leave `control_disposition = null`;
5. successful/inconclusive results leave `control_disposition = null`;
6. the v1.2 schema rejects source-value-bearing control fields;
7. the historical v1.1 schema remains unchanged in contract shape;
8. lowercase, whitespace-padded and Unicode-lookalike synthetic values remain rejected without normalization;
9. the exact regex remains unchanged.

Two historical proposal contract tests were adjusted only to stop treating the *current* runner as permanently v1.1. They continue to verify that their historical proposals and v1.1 contract records remain pinned to the historical state.

## CI evidence

Functional CI `35100766657` on `f69262a632b6bf0eed1385639aea3c59bb9a94ac` completed successfully.

Markers:

- `ruff`: PASS;
- `mypy`: PASS, no issues in 19 source files;
- contract tests: `235 passed`;
- smoke tests: `6 passed`;
- full pytest: `292 passed`;
- reviewer frontend lint: PASS;
- reviewer frontend typecheck: PASS;
- reviewer frontend build: PASS;
- Streamlit safety smoke: PASS;
- Streamlit startup smoke: PASS.

The first functional CI attempt exposed one obsolete historical-proposal assertion that required the current runner to remain `1.1.0`. The repair changed that assertion to inspect the immutable v1.1 schema directly. No runtime behavior changed during that repair.

## Rollback

Rollback remains bounded to reverting the implementation commits on this branch.

Rollback requires no:

- database migration;
- source-state migration;
- historical-evidence migration.

Rollback restores runner output to `1.1.0` and removes v1.2 `control_disposition` emission while preserving historical v1.1 evidence.

## Explicitly not performed / not authorized

This task did not and does not authorize:

- access to `claimit.ca.gov`;
- access to new authority sources;
- real-source semantic-verification execution;
- reconstruction or inference of the hidden real `PROPERTY_TYPE` value;
- parser/projector changes;
- regex changes or relaxation;
- trim/case/Unicode normalization;
- reuse of consumed approvals;
- creation or granting of execution/privacy approval tokens;
- real-row/field persistence;
- privacy expansion;
- source continuation;
- source-policy activation;
- registry activation;
- production-classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Governance state after implementation

- D-008 accepted as design: `true`;
- bounded implementation authorization: `true`;
- runtime implementation completed: `true`;
- runtime output contract version: `1.2.0`;
- v1.2 execution schema created: `true`;
- synthetic/offline regression validation: `PASS`;
- human review of the completed implementation: `pending`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- downstream identity/genealogy/matching/outreach/claim gates remain closed.

## Next explicit gate

Perform exclusively a human review of the completed bounded implementation:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_IMPLEMENTATION_REVIEW`

A PASS at that gate may accept the implementation as conforming to D-008 and the authorization. It must not itself authorize or perform a real-source execution.
