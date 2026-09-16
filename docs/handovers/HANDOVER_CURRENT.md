# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-proposal-review`

This branch was created from proposal checkpoint:

`e9af9d61b2f216de58cd8f3ad6a6925c38aef172`

Proposal checkpoint CI:

`35098004540` — **SUCCESS**

## Review Functional Checkpoint

Functional review checkpoint after review artifact + project state + roadmap updates:

`c2e22efbe068a0f0f44e0e6b8798677408f8aa45`

CI:

`35098674308` — **SUCCESS**

The CI completed both `streamlit-candidate` and `quality` successfully, including ruff, mypy, contract tests, smoke tests, full pytest, frontend lint/typecheck/build and Streamlit smoke checks.

The later handover refresh commit is documentation-only. On restart, always verify the remote branch HEAD and latest CI rather than assuming this file is the branch tip.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect the review evidence and implementation proposal artifacts listed below before acting.

## Completed Single Next Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW.md`

Review result:

`PASS_IMPLEMENTATION_PROPOSAL_ACCEPTED_AS_DESIGN_RUNTIME_IMPLEMENTATION_NOT_AUTHORIZED`

Meaning of PASS:

- the implementation **design** is acceptable;
- D-008 conformance is accepted;
- the additive/versioned contract approach is accepted;
- regression/rollback/privacy boundaries are acceptable;
- runtime implementation is **not** authorized by this review;
- creation of the actual v1.2 execution schema is **not** authorized by this review;
- real-source execution is **not** authorized by this review.

## Governing Decision

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design policy:

`WHOLE_SOURCE_STOP`

The accepted policy remains design/governance authority. It is not yet active as a new runtime control vocabulary.

## Accepted Implementation Design — Still Not Implemented

Strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

A later separately authorized implementation may make only the reviewed bounded delta:

1. modify `scripts/ca_sco_property_type_semantic_verification.py`;
2. create `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
3. preserve historical `schemas/common/property_type_semantic_verification_execution.v1_1.schema.json` unchanged;
4. move future runner output contract from `1.1.0` to `1.2.0` only in the implementation commit;
5. add nullable top-level `control_disposition`;
6. preserve legacy mismatch output:
   - `semantic_result_status = STOPPED_FAIL_CLOSED`;
   - `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
7. map only legacy `PROPERTY_TYPE_FORMAT_UNEXPECTED` to:
   - `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
   - `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
8. keep `control_disposition = null` for unrelated stop reasons and successful results;
9. preserve existing exception-driven fail-closed flow so no later member is requested after the trigger;
10. preserve source continuation = `false`.

The new control disposition is additive metadata and must not replace or reinterpret the legacy result fields.

## Current Runtime State — Unchanged

Current runner:

`script: scripts/ca_sco_property_type_semantic_verification.py`

Current execution schema:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Current runtime schema version:

`1.1.0`

Current mismatch behavior:

- `STOPPED_FAIL_CLOSED`;
- `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- no `control_disposition` field;
- the raised `RunnerStop` exits member processing and prevents later canonical members from being processed after the trigger.

The actual v1.2 execution schema does not exist yet.

## Validation Boundary — Unchanged

Regex remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Do not introduce:

- trim;
- uppercasing/case conversion;
- Unicode normalization;
- alternate-token acceptance;
- parser/projector changes;
- regex relaxation.

## Privacy / Persistence Boundary — Unchanged

The accepted future control metadata may contain only non-value-bearing:

- `status_code`;
- `reason_code`.

Do not persist or expose through the new disposition:

- exact or transformed `PROPERTY_TYPE`;
- row/field hashes;
- exact row/field lengths;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- real row/field content.

No row-specific human inspection or real-row quarantine persistence is authorized.

## Regression Requirements for Any Later Authorized Implementation

A later authorized implementation must use synthetic/offline tests to prove at least:

1. structural mismatch still returns `STOPPED_FAIL_CLOSED` + `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the same mismatch adds exactly `PROPERTY_TYPE_NONCONFORMING_STOPPED` + `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
3. no later member is requested after the trigger;
4. unrelated runner stops keep `control_disposition = null`;
5. successful results keep `control_disposition = null`;
6. v1.2 rejects source-value-bearing control fields;
7. historical v1.1 schema/evidence remain unchanged and valid;
8. regex/projector/no-normalization guards remain green.

A real-source execution is not required to validate the future code implementation itself.

## Rollback Requirement

Rollback must be possible by reverting only the future implementation commit(s).

No database migration, source-state migration or historical-evidence migration is required or authorized.

Rollback returns runner output to schema `1.1.0` and removes v1.2 `control_disposition` emission without rewriting historical evidence.

## Proposal / Review Artifacts

Implementation proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_implementation.v1.json`

Proposal schema:

`schemas/common/property_type_nonconforming_row_handling_policy_implementation_proposal.schema.json`

Proposal audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL.md`

Proposal contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_policy_implementation_proposal.py`

Human review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL_REVIEW.md`

Prior governing review:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW.md`

## Governance State After This Review

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- implementation proposal prepared: `true`;
- implementation proposal human-reviewed: `true`;
- implementation design accepted: `true`;
- policy active in runtime: `false`;
- runtime implementation authorized: `false`;
- runtime modified by review: `false`;
- execution schema v1.2 created: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- real-row quarantine authorized: `false`;
- row-specific human inspection authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- normalization unchanged;
- all historical execution/privacy/authority approvals consumed and non-reusable;
- no new approval token created or granted by this review;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## DECISIONS.md Handling

`DECISIONS.md` was intentionally not changed by this review.

Reason: no new architectural or governance decision was created. The review accepts a bounded implementation design under existing D-008; it does not supersede or alter D-008.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION`

This is an explicit human/owner gate deciding whether the already reviewed implementation design may be implemented.

A PASS at this next gate may authorize only:

- the reviewed runtime change;
- creation of the reviewed versioned v1.2 execution schema;
- corresponding synthetic/offline regression tests and validation.

It must **not** authorize or perform a real-source execution.

Implementation and real-source execution must remain separate gates.

## Do Not Do During the Next Authorization Gate

Do not:

- modify runtime while merely deciding the authorization;
- create the actual v1.2 execution schema while merely deciding the authorization;
- access `claimit.ca.gov`;
- access new authority sources;
- infer or reconstruct the hidden real `PROPERTY_TYPE` value;
- change parser/projector;
- modify or relax `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- add trim, case conversion or Unicode normalization;
- reuse consumed approval tokens;
- invent execution/privacy approval tokens;
- authorize a real-source execution as part of the implementation authorization;
- persist real rows/fields or expand privacy scope;
- enable source continuation;
- activate source policy, registry or production classification;
- begin identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Restart Instruction

At the start of the next task:

1. verify the remote HEAD of `m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-proposal-review`;
2. verify the latest CI for that remote HEAD;
3. read the five canonical files in order;
4. read the implementation proposal and human review artifact;
5. execute only the `SINGLE NEXT ACTION` above.
