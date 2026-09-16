# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-offline`

This branch was created from the completed implementation-authorization checkpoint:

`b98faa9ff6e24404ed8a6028dda21c0cf0041222`

The implementation-authorization result was:

`PASS_BOUNDED_IMPLEMENTATION_AUTHORIZED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

## Offline Implementation Functional Checkpoint

Functional implementation checkpoint before documentation-only state refresh:

`f69262a632b6bf0eed1385639aea3c59bb9a94ac`

GitHub Actions CI:

`35100766657` — **SUCCESS**

Verified CI markers:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `235 passed`;
- smoke tests: `6 passed`;
- full pytest: `292 passed`;
- reviewer frontend lint: PASS;
- reviewer frontend typecheck: PASS;
- reviewer frontend build: PASS;
- Streamlit safety smoke: PASS;
- Streamlit startup smoke: PASS.

The subsequent implementation audit / PROJECT_STATE / ROADMAP / handover refresh commits are documentation-only. On restart, always verify the remote branch HEAD and latest CI rather than assuming this file is the branch tip.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect, in this order as relevant:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION.md`
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE_IMPLEMENTATION.md`
3. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`
4. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW.md`
5. `scripts/ca_sco_property_type_semantic_verification.py`
6. `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`
7. `schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`
8. relevant unit/contract tests.

## Completed Single Next Action

Completed:

`IMPLEMENT_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE`

Implementation audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE_IMPLEMENTATION.md`

Implementation state:

`IMPLEMENTED_OFFLINE_CI_GREEN_HUMAN_IMPLEMENTATION_REVIEW_REQUIRED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Meaning:

- the reviewed/authorized runtime delta is implemented;
- execution contract `1.2.0` exists;
- synthetic/offline regression validation is green;
- completed implementation still requires an explicit human implementation review;
- no real-source execution has been performed or authorized by this task.

## Governing Decision

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design policy:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

## Implemented Runtime State

Runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Current runner output contract version:

`1.2.0`

Current versioned execution schema:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

Historical immutable execution schema:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

The historical v1.1 schema was not modified.

## Exact v1.2 Behavior

The runner initializes:

`control_disposition = null`

Only the legacy stop reason:

`PROPERTY_TYPE_FORMAT_UNEXPECTED`

maps to:

- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

The legacy result remains unchanged:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`.

For unrelated runner stops and successful/inconclusive outcomes:

`control_disposition = null`

No existing result field was removed or reinterpreted.

## Fail-Closed / Continuation Boundary

The implementation reuses the existing exception-driven `RunnerStop` flow.

Synthetic/offline regression coverage proves that the targeted mismatch:

- remains fail-closed;
- gets only the exact D-008 non-value-bearing control metadata;
- stops before a later canonical source member is requested;
- does not silently skip a row;
- does not introduce a second continuation mechanism.

Source continuation remains:

`false`

## Validation Boundary — Frozen

Regex remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No implementation change was made to:

- parser;
- projector;
- trim behavior;
- case conversion;
- Unicode normalization;
- alternate-token acceptance;
- transport budget;
- row budget;
- source continuation behavior.

Regression tests explicitly retain rejection of lowercase, whitespace-padded and Unicode-lookalike synthetic values.

## Privacy / Persistence Boundary — Frozen

The v1.2 `control_disposition` may contain only non-value-bearing:

- `status_code`;
- `reason_code`.

The v1.2 schema rejects additional/source-value-bearing fields in that object.

Do not persist or expose through the new disposition:

- exact or transformed `PROPERTY_TYPE`;
- derivatives of the hidden value;
- row/field hashes;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No row-specific human inspection or real-row quarantine persistence is authorized.

## Regression / Repair Evidence

The first functional CI attempt identified one obsolete historical-proposal assertion: it required the *current* runner to remain at schema version `1.1.0` even after the explicitly authorized versioned implementation.

The repair changed only that test boundary so the historical proposal validates directly against the immutable v1.1 schema while current runtime may be v1.2. No runtime behavior changed during this repair.

Final functional checkpoint:

`f69262a632b6bf0eed1385639aea3c59bb9a94ac`

Final functional CI:

`35100766657` — **SUCCESS**

## Rollback Requirement

Rollback remains possible by reverting only the implementation commits.

No database migration, source-state migration or historical-evidence migration is required or authorized.

Rollback restores runner output contract `1.1.0` and removes v1.2 `control_disposition` emission without rewriting historical evidence.

## Real-Source / Governance Boundary

This implementation did **not**:

- request `claimit.ca.gov`;
- request a new authority source;
- execute semantic verification on a real source;
- inspect a real row or field;
- reconstruct or infer the hidden real `PROPERTY_TYPE` value;
- reuse consumed approvals;
- create or grant execution/privacy approvals;
- enable source continuation;
- activate the source policy;
- activate the registry;
- activate production classification;
- enter identity resolution, genealogy, beneficiary matching, outreach or claim submission.

Current governance state:

- D-008 accepted as design: `true`;
- bounded implementation authorized: `true`;
- runtime implementation completed: `true`;
- current runner output contract: `1.2.0`;
- v1.2 schema created: `true`;
- historical v1.1 schema preserved: `true`;
- synthetic/offline validation: `PASS`;
- completed implementation human-reviewed: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged: `true`;
- regex/normalization unchanged: `true`;
- historical execution/privacy/authority approvals consumed and non-reusable;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- downstream identity/genealogy/matching/outreach/claim gates remain closed.

## DECISIONS.md Handling

`DECISIONS.md` is intentionally unchanged.

Reason: this implementation executes the already accepted D-008 design and the already reviewed/authorized implementation strategy. It introduces no new architectural or governance decision and does not supersede D-008.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_IMPLEMENTATION_REVIEW`

This gate must review only whether the completed implementation conforms to:

- D-008 / `WHOLE_SOURCE_STOP`;
- `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- the reviewed implementation proposal;
- the owner implementation authorization;
- backward compatibility / v1.1 immutability;
- exact control mapping;
- fail-closed/no-continuation behavior;
- regression coverage;
- privacy/persistence boundary;
- rollback boundary.

A PASS at this gate may accept the implementation as conforming. It must **not** authorize or perform a real-source execution.

## Do Not Do During the Next Human Implementation Review

Do not:

- access `claimit.ca.gov`;
- access new authority sources;
- run a real-source semantic verification;
- infer or reconstruct the hidden real `PROPERTY_TYPE` value;
- change runtime while merely reviewing it;
- change parser/projector;
- modify or relax `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- add trim, case conversion or Unicode normalization;
- reuse or invent execution/privacy approval tokens;
- persist real rows/fields or expand privacy scope;
- enable source continuation;
- activate source policy, registry or production classification;
- begin identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Restart Instruction

At the start of the next task:

1. verify the remote HEAD of `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-offline`;
2. verify the latest CI for that remote HEAD;
3. read the five canonical files in order;
4. read the implementation authorization and completed implementation audit;
5. inspect the v1.2 runner/schema/tests without modifying them;
6. execute only the `SINGLE NEXT ACTION` above.
