# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-authorization`

This branch was created from reviewed implementation-design checkpoint:

`fd9aa939727812692008358709d0a0b0968fffb2`

Base review CI:

`35098890574` — **SUCCESS**

## Authorization Functional Checkpoint

Functional checkpoint after authorization artifact + project state + roadmap updates:

`4c747cb760a75c46fe3a7193c313fcf017a86d71`

CI:

`35099376111` — **SUCCESS**

The CI completed both `streamlit-candidate` and `quality` successfully, including ruff, mypy, contract tests, smoke tests, full pytest, frontend lint/typecheck/build and Streamlit smoke checks.

The later handover refresh commit is documentation-only. On restart, always verify the remote branch HEAD and latest CI rather than assuming this file is the branch tip.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect the authorization artifact, implementation proposal and proposal-review artifact listed below before acting.

## Completed Single Next Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION`

Authorization artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION.md`

Authorization result:

`PASS_BOUNDED_IMPLEMENTATION_AUTHORIZED_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Meaning:

- the reviewed runtime/schema/test implementation may now be implemented;
- synthetic/offline regression validation is authorized;
- creation of the reviewed versioned v1.2 execution schema is authorized only as part of that bounded implementation;
- runtime has **not** yet been modified by this authorization gate;
- the v1.2 execution schema has **not** yet been created by this authorization gate;
- real-source execution remains **not authorized**;
- source continuation remains **not authorized**;
- privacy expansion remains **not authorized**.

## Governing Decision

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design policy:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

## Exact Authorized Implementation Scope

The next implementation task may only:

1. modify `scripts/ca_sco_property_type_semantic_verification.py` as required by the reviewed design;
2. create `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
3. preserve historical `schemas/common/property_type_semantic_verification_execution.v1_1.schema.json` unchanged;
4. move future runner output contract from `1.1.0` to `1.2.0` only in the implementation;
5. add nullable top-level `control_disposition`;
6. preserve legacy mismatch output:
   - `semantic_result_status = STOPPED_FAIL_CLOSED`;
   - `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
7. map only legacy `PROPERTY_TYPE_FORMAT_UNEXPECTED` to:
   - `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
   - `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
8. keep `control_disposition = null` for unrelated runner stops and successful results;
9. preserve the existing exception-driven fail-closed flow so no later member is requested after the trigger;
10. preserve source continuation = `false`;
11. add or update only the minimum synthetic/offline tests required by the reviewed regression contract;
12. run repository-local and GitHub CI validation for the bounded implementation.

No existing result field may be removed or reinterpreted.

## Current Runtime State — Still Unchanged

Current runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Current execution schema:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Current runtime schema version:

`1.1.0`

Current mismatch behavior:

- `STOPPED_FAIL_CLOSED`;
- `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- no `control_disposition` field;
- later canonical members are not processed after the trigger.

The actual v1.2 execution schema does not exist yet.

## Validation Boundary — Frozen

Regex remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Do not introduce:

- trim;
- uppercasing/case conversion;
- Unicode normalization;
- alternate-token acceptance;
- parser/projector changes;
- regex relaxation or replacement.

## Privacy / Persistence Boundary — Frozen

The authorized future control metadata may contain only non-value-bearing:

- `status_code`;
- `reason_code`.

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

## Required Regression Coverage

The authorized implementation must use synthetic/offline tests proving at least:

1. structural mismatch still returns `STOPPED_FAIL_CLOSED` + `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the same mismatch adds exactly `PROPERTY_TYPE_NONCONFORMING_STOPPED` + `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
3. no later member is requested after the trigger;
4. unrelated runner stops keep `control_disposition = null`;
5. successful results keep `control_disposition = null`;
6. v1.2 rejects source-value-bearing control fields;
7. historical v1.1 schema/evidence remain unchanged and valid;
8. regex/projector/no-normalization guards remain green.

A real-source execution is neither required nor authorized to validate implementation acceptance.

## Rollback Requirement

Rollback must remain possible by reverting only the implementation commit(s).

No database migration, source-state migration or historical-evidence migration is required or authorized.

Rollback must restore runner output schema `1.1.0` and remove v1.2 `control_disposition` emission without rewriting historical evidence.

## Proposal / Review / Authorization Artifacts

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

Implementation authorization artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION.md`

Prior governing review:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW.md`

## Governance State After Authorization

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- implementation proposal prepared: `true`;
- implementation proposal human-reviewed: `true`;
- implementation design accepted: `true`;
- runtime implementation authorized: `true`;
- runtime implementation completed: `false`;
- runtime modified by authorization gate: `false`;
- execution schema v1.2 created by authorization gate: `false`;
- policy active in runtime: `false`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- real-row quarantine authorized: `false`;
- row-specific human inspection authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- normalization unchanged;
- all historical execution/privacy/authority approvals consumed and non-reusable;
- no execution/privacy approval token created or granted by this authorization;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## DECISIONS.md Handling

`DECISIONS.md` is intentionally unchanged.

Reason: the authorization applies the already accepted D-008 design and reviewed implementation strategy. It does not introduce a new architectural or governance design decision that supersedes D-008.

## SINGLE NEXT ACTION

Execute exclusively:

`IMPLEMENT_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE`

This implementation task may perform only the authorized runtime/schema/test delta and synthetic/offline validation described above.

It must **not** authorize or perform a real-source execution.

Implementation acceptance and any later real-source execution authorization must remain separate gates.

## Do Not Do During the Next Implementation Task

Do not:

- access `claimit.ca.gov`;
- access new authority sources;
- infer or reconstruct the hidden real `PROPERTY_TYPE` value;
- change parser/projector;
- modify or relax `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- add trim, case conversion or Unicode normalization;
- reuse consumed approval tokens;
- invent or grant execution/privacy approval tokens;
- authorize a real-source execution as part of implementation;
- persist real rows/fields or expand privacy scope;
- enable source continuation;
- activate source policy, registry or production classification;
- begin identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Restart Instruction

At the start of the next task:

1. verify the remote HEAD of `m3-ca-sco-property-type-nonconforming-row-handling-policy-implementation-authorization`;
2. verify the latest CI for that remote HEAD;
3. read the five canonical files in order;
4. read the implementation authorization artifact, implementation proposal and proposal-review artifact;
5. execute only the `SINGLE NEXT ACTION` above.
