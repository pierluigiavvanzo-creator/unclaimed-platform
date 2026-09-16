# M3 California SCO — PROPERTY_TYPE Nonconforming Row Handling Policy v1.2 Implementation Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS — V1.2 IMPLEMENTATION ACCEPTED AS CONFORMING — REAL-SOURCE EXECUTION NOT AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_IMPLEMENTATION_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- implementation branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-offline`
- reviewed remote HEAD: `7d40f410752cdaef96faeae4aaafc1ca86b13e18`
- reviewed CI: `35101304555` — **SUCCESS**
- functional implementation checkpoint: `f69262a632b6bf0eed1385639aea3c59bb9a94ac`
- functional CI: `35100766657` — **SUCCESS**
- authorization base: `b98faa9ff6e24404ed8a6028dda21c0cf0041222`
- governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- accepted handling design: `WHOLE_SOURCE_STOP`
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`
- implementation authorization: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_AUTHORIZATION.md`
- implementation audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_OFFLINE_IMPLEMENTATION.md`

This review is repository-only. It performs no request to `claimit.ca.gov`, no request to a new authority source, no real-source semantic-verification execution, no real-row/field inspection, no hidden-value reconstruction, no approval-token reuse, no privacy expansion and no runtime modification.

## Decision

`PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`

The completed v1.2 implementation conforms to D-008, the reviewed implementation proposal and the owner implementation authorization.

This PASS accepts the bounded offline implementation as conforming. It does **not** authorize a real-source execution, source continuation, privacy expansion, source-policy activation, registry activation, production classification or downstream work.

## D-008 / WHOLE_SOURCE_STOP conformity

PASS.

The implementation preserves the accepted fail-closed handling design:

- the targeted nonconforming `PROPERTY_TYPE` remains fail-closed;
- legacy `semantic_result_status = STOPPED_FAIL_CLOSED` is preserved;
- legacy `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED` is preserved;
- source continuation after the trigger remains `false`;
- no later canonical member is requested after the trigger in the synthetic regression;
- no silent row skip or alternate continuation mechanism was introduced;
- no semantic claim is made about the hidden source value beyond the structural mismatch against the unchanged validator.

## Additive versioning / backward compatibility

PASS.

Current runner output contract is now:

`1.2.0`

New schema:

`schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`

Historical schema remains:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

The reviewed current v1.1 blob SHA is exactly:

`33c829116eea0b568cfe16c664ffbeee9d00e013`

which matches the pre-implementation blob SHA recorded by the implementation proposal and implementation audit.

No existing v1.1 result field was removed or reinterpreted. The new v1.2 field is additive.

## Exact control mapping

PASS.

The runner initializes:

`control_disposition = null`

Only the legacy stop reason:

`PROPERTY_TYPE_FORMAT_UNEXPECTED`

maps to exactly:

- `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

Unrelated `RunnerStop` outcomes and successful/inconclusive outcomes retain:

`control_disposition = null`

The v1.2 JSON Schema independently enforces the same mapping: `PROPERTY_TYPE_FORMAT_UNEXPECTED` requires the exact non-null D-008 disposition, while all other stop reasons/outcomes require `control_disposition = null`.

## Validation semantics

PASS and unchanged.

Regex remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The implementation introduced no:

- trim;
- ASCII or Unicode case conversion;
- Unicode normalization;
- alternate-token acceptance;
- parser change;
- projector change;
- regex relaxation or replacement.

Synthetic regression coverage explicitly rejects lowercase, whitespace-padded and Unicode-lookalike values under the unchanged rule.

## Regression coverage

PASS.

The reviewed tests cover every required implementation-authorization regression family:

1. synthetic structural mismatch preserves `STOPPED_FAIL_CLOSED` and `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
2. the same mismatch emits exactly `PROPERTY_TYPE_NONCONFORMING_STOPPED` and `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
3. the mismatch stops after the first affected member and does not request a later member;
4. unrelated runner stops keep `control_disposition = null`;
5. successful and no-insurance/inconclusive results keep `control_disposition = null`;
6. v1.2 rejects source-value-bearing/additional control-disposition fields;
7. historical v1.1 contract shape remains unchanged and the historical second semantic execution still validates against the v1.1 schema;
8. regex and no-normalization guards remain green.

The first implementation CI exposed one obsolete proposal test that incorrectly required the *current* runner to remain permanently at `1.1.0`. The remediation changed only that historical-test boundary so the historical proposal checks the immutable v1.1 schema directly. No runtime behavior was changed by the remediation.

## CI evidence

PASS.

Final reviewed HEAD CI `35101304555` completed successfully for both `quality` and `streamlit-candidate`.

Verified markers include:

- ruff: PASS;
- mypy: PASS;
- contract tests: PASS;
- smoke tests: PASS;
- full pytest: PASS;
- reviewer frontend lint: PASS;
- reviewer frontend typecheck: PASS;
- reviewer frontend build: PASS;
- Streamlit safety smoke: PASS;
- Streamlit startup smoke: PASS.

The functional implementation checkpoint `f69262a632b6bf0eed1385639aea3c59bb9a94ac` recorded:

- contract tests: `235 passed`;
- smoke tests: `6 passed`;
- full pytest: `292 passed`;
- mypy: no issues in 19 source files.

## Scope / diff review

PASS.

Comparison from authorization base `b98faa9ff6e24404ed8a6028dda21c0cf0041222` to reviewed implementation HEAD `7d40f410752cdaef96faeae4aaafc1ca86b13e18` shows only:

- `scripts/ca_sco_property_type_semantic_verification.py`;
- new `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`;
- minimum relevant unit/contract tests;
- implementation audit and durable state/handover documentation.

No source policy, registry, parser/projector module, one-shot network workflow or production-classification surface was modified by the implementation branch.

## Privacy / persistence boundary

PASS.

The new `control_disposition` permits only non-value-bearing:

- `status_code`;
- `reason_code`.

Its schema uses `additionalProperties: false` and rejects source-value-bearing additions.

The implementation does not add persistence or exposure through `control_disposition` for exact/transformed `PROPERTY_TYPE`, hidden-value derivatives, row/field hashes, exact lengths, `PROPERTY_ID`, owner/holder values, source-derived free text or real row/field content.

No real-row quarantine or row-specific human inspection was introduced.

## Rollback

PASS.

Rollback remains bounded to reverting the implementation commits.

No database migration, source-state migration or historical-evidence migration is required. Reverting the implementation restores runner output contract `1.1.0` and removes v1.2 `control_disposition` emission while leaving historical v1.1 evidence intact.

## Real-source / governance separation

PASS.

Implementation acceptance and future real-source execution remain separate gates.

This review does **not**:

- authorize access to `claimit.ca.gov`;
- authorize access to a new authority source;
- authorize or perform real-source semantic verification;
- authorize reuse of consumed execution/privacy approvals;
- create or grant a new execution/privacy approval token;
- authorize source continuation;
- expand privacy;
- activate source policy or registry;
- activate production classification;
- begin identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Governance state after review

- D-008 accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- bounded implementation authorized: `true`;
- runtime implementation completed: `true`;
- completed implementation human-reviewed: `true`;
- implementation review result: `PASS_V1_2_IMPLEMENTATION_ACCEPTED_AS_CONFORMING_REAL_SOURCE_EXECUTION_NOT_AUTHORIZED`;
- current runner output contract: `1.2.0`;
- v1.2 execution schema created: `true`;
- historical v1.1 schema preserved: `true`;
- synthetic/offline validation: `PASS`;
- parser/projector unchanged: `true`;
- regex/normalization unchanged: `true`;
- real-source execution authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- downstream identity/genealogy/matching/outreach/claim gates remain closed.

## Next explicit action

No real-source execution is automatically unlocked by this PASS.

The next bounded action is proposal-only:

`PREPARE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL`

That future proposal may define a fresh, separately reviewable execution/privacy authorization path for a bounded v1.2 real-source verification. Proposal preparation must itself remain non-executing and must not access `claimit.ca.gov`, reuse consumed approvals, widen privacy, enable source continuation or activate source/registry/production classification.
