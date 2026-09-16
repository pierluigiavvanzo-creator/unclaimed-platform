# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance remains resolved only within the recorded proof boundary. The retained real-source diagnostic chain remains bounded by `ASCII_STRUCTURAL_MISMATCH` and `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`; semantic compatibility with the hidden source value remains unresolved.

The nonconforming-row handling design is governed by:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design policy:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

The implementation proposal passed human review, the owner granted bounded implementation authorization, the v1.2 implementation completed offline with green CI, and the completed implementation has now passed human implementation review.

Implementation review result:

`PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

Real-source execution remains separately gated and unauthorized.

## Human Implementation Review Checkpoint

Review branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-implementation-review`

Reviewed implementation HEAD:

`7d40f410752cdaef96faeae4aaafc1ca86b13e18`

Reviewed implementation CI:

`35101304555` — **SUCCESS**

Functional implementation checkpoint:

`f69262a632b6bf0eed1385639aea3c59bb9a94ac`

Functional CI:

`35100766657` — **SUCCESS**

Implementation review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_IMPLEMENTATION_REVIEW.md`

Implementation audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE_IMPLEMENTATION.md`

## Runtime Contract — v1.2 Accepted as Conforming

Current runner:

`scripts/ca_sco_property_type_semantic_verification.py`

Current output contract version:

`1.2.0`

Current versioned contract:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

Historical contract remains available and unchanged:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Current reviewed v1.1 blob SHA:

`33c829116eea0b568cfe16c664ffbeee9d00e013`

For `PROPERTY_TYPE_FORMAT_UNEXPECTED`, the runner preserves the legacy machine result:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`.

It additionally emits only:

```text
control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED
control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE
```

Other stop reasons and successful/inconclusive outcomes retain:

`control_disposition = null`

No existing result field is removed or reinterpreted.

## Fail-Closed / Continuation Invariants

The implementation reuses the existing `RunnerStop` exception-driven fail-closed flow.

Synthetic/offline regression tests verify that a targeted structural mismatch:

- remains `STOPPED_FAIL_CLOSED`;
- preserves `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- receives only the exact D-008 status/reason metadata;
- stops before any later canonical source member is requested;
- does not introduce silent row skip or alternate continuation.

Source continuation remains:

`false`

## Validation / Privacy Boundary

Validation rule remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is implemented or authorized.

The v1.2 `control_disposition` permits only the non-value-bearing:

- `status_code`;
- `reason_code`.

The schema rejects extra/source-value-bearing fields in that disposition. Exact or transformed PROPERTY_TYPE, derivatives of the hidden value, real row/field content, hashes, exact lengths, PROPERTY_ID, owner/holder values and source-derived free text remain outside the new control persistence boundary.

No real-row quarantine or row-specific human inspection is authorized.

All historical execution/privacy/authority approvals remain consumed and non-reusable. No execution/privacy approval token is created or granted by the implementation review.

## Regression / CI Evidence

Reviewed final implementation CI `35101304555` is **SUCCESS** for both `quality` and `streamlit-candidate`.

Functional checkpoint evidence includes:

- ruff: PASS;
- mypy: PASS, no issues in 19 source files;
- contract tests: `235 passed`;
- smoke tests: `6 passed`;
- full pytest: `292 passed`;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

Historical second semantic execution evidence continues to validate against the immutable v1.1 schema.

## Rollback

Rollback remains bounded to reverting the implementation commits.

No database migration, source-state migration or historical-evidence migration is required. Rollback restores runner output to `1.1.0` and removes v1.2 `control_disposition` emission without rewriting historical evidence.

## Governance State

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- implementation proposal human-reviewed: `true`;
- bounded implementation authorized: `true`;
- runtime implementation completed: `true`;
- completed implementation human-reviewed: `true`;
- implementation review result: `PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- current runner output contract version: `1.2.0`;
- execution schema v1.2 created: `true`;
- historical v1.1 contract preserved: `true`;
- synthetic/offline regression validation: `PASS`;
- parser/projector unchanged: `true`;
- regex/normalization unchanged: `true`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Prepare exclusively a non-executing proposal for the next separately governed real-source step:

`PREPARE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL`

That proposal must define a fresh, separately reviewable execution/privacy authorization path. Proposal preparation must not access `claimit.ca.gov`, perform a real-source execution, reuse consumed approvals, widen privacy, enable source continuation, change validation semantics, activate source/registry/production classification or enter downstream work.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
