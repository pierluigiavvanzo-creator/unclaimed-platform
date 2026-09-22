# M3 — CA SCO PROPERTY_TYPE Second Bounded Semantic Execution Proposal

Date: 2026-09-15  
Status: **PROPOSAL ONLY — NOT AUTHORIZED — NO SCO NETWORK/BODY ACCESS**

## 1. Purpose

Prepare, without contacting the California SCO endpoint, an evidence-backed proposal for a possible second bounded `PROPERTY_TYPE` semantic execution using the canonical remediated runner and execution contract v1.1.0.

This task does **not** authorize or perform the second execution. It stops at the human gate `HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_REVIEW`.

## 2. Isolation and canonical base

Candidate branch:
`m3-ca-sco-property-type-second-execution-proposal`

Created from verified canonical development HEAD:
`e97c1f62959f603bdd3df79538d4b70255594c70`.

Canonical branch:
`m2-state-governance-core`.

Stable `main` is not modified.

## 3. Historical evidence that motivates a second execution

The first owner-authorized bounded real attempt was GitHub Actions run `34965097988` and ended `STOPPED_FAIL_CLOSED` under historical execution schema v1.0.0 with stop reason `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Observed historical budget use was limited to one HEAD, one Range GET, two total HTTP requests, 131072 source-response body bytes and zero accepted/examined rows. There was no retry or budget widening.

The offending real source value/bytes were intentionally not persisted or logged and are not inferred here.

Offline diagnosis later established that the pre-remediation runner conflated two distinct conditions under the same historical reason: invalid UTF-8 while projecting `PROPERTY_TYPE`, and successfully decoded values that failed the unchanged token-shape regex. The historical root cause therefore remains unresolved.

## 4. Why the proposal uses v1.1.0

The canonical remediated runner now emits execution schema version `1.1.0` and distinguishes:

- invalid UTF-8 in projected `PROPERTY_TYPE` -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded non-empty value failing `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

The historical v1.0.0 schema/evidence remain frozen and are not migrated or reinterpreted.

A second bounded execution would therefore be capable of producing diagnostically narrower fail-closed evidence than the first attempt without relaxing parsing or semantic rules.

## 5. Historical approvals are consumed

The first execution used:

- execution approval: `OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`;
- transient-row privacy approval: `OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`.

Both approvals were consumed by run `34965097988`. They are explicitly **not reusable**.

This proposal contains no replacement approval references and does not infer authorization from the owner's request to prepare the proposal.

## 6. Fresh human approvals required before any second real execution

Two fresh approvals are required:

1. **Second bounded semantic-execution approval** — authorizing exactly one bounded real run of the canonical v1.1.0 runner against the fixed CA SCO `$500+` endpoint under the unchanged caps below.
2. **Second transient-row privacy approval** — authorizing the runner's bounded in-memory observation of transient row bytes solely to project `PROPERTY_TYPE`, with zero-day retention and immediate disposal.

Until both are explicitly granted and recorded as new versioned authorization evidence:

- no SCO request may occur;
- no one-shot network workflow may be created or enabled;
- no live CLI execution may occur.

## 7. Proposed execution boundary — unchanged

The proposal preserves the canonical safety caps exactly:

- 4 canonical members;
- maximum 4 data rows/member;
- maximum 16 data rows total;
- maximum 1 HEAD request;
- maximum 4 Range GET requests;
- maximum 5 HTTP requests total;
- maximum 131072 response-body bytes per Range;
- maximum 524288 source-response body bytes total;
- maximum 262144 uncompressed transient bytes/member;
- maximum 1048576 uncompressed transient bytes total;
- maximum 32768 bytes/logical record;
- no additional Range;
- no full-body fallback;
- no automatic widening.

Deterministic sample selection remains the first four complete data rows following the verified header in each of the four canonical CSV members. No representativeness claim is made.

## 8. Semantic and privacy boundary — unchanged

Semantic rule remains:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Official insurance codes remain:
`IN01`, `IN02`, `IN03`, `IN04`, `IN05`, `IN06`, `IN07`, `IN08`, `IN99`.

No trimming, uppercasing, normalization or regex relaxation is proposed.

Privacy/persistence remains:

- transient processing memory-only;
- retention `0` days;
- immediate disposal after projection or stop;
- no raw body persistence;
- no full-row persistence;
- no `PROPERTY_ID` persistence;
- no owner/holder persistence;
- no per-row `PROPERTY_TYPE` persistence;
- no offending bytes, hashes or lengths persisted;
- no record/source values in logs;
- only bounded derived aggregate summary fields may be persisted after an authorized execution.

## 9. Network state during proposal preparation

No California SCO request is part of this proposal task.

The one-shot workflow path `.github/workflows/ca-sco-property-type-semantic-verification-once.yml` remains absent. The proposal records that path only as the future, ephemeral workflow location that could be recreated **after** fresh authorization and removed again after the single run.

## 10. Governance state not changed by this proposal

This proposal does not:

- approve the source;
- enable or approve the source registry entry;
- activate production insurance classification;
- authorize identity resolution;
- authorize beneficiary matching;
- authorize genealogy;
- authorize outreach;
- authorize claim submission;
- promote anything to `main`.

The source policy remains `PROPOSED`; real acquisition remains unauthorized; the registry remains disabled/unapproved; approved real sources remain `0`.

## 11. Proposed machine artifacts

New, versioned candidate artifacts:

- `schemas/common/property_type_second_semantic_execution_proposal.schema.json`;
- `sources/proposals/ca_sco_segment_500_plus.property_type_second_semantic_execution.v1.json`;
- `tests/contract/test_ca_sco_property_type_second_semantic_execution_proposal.py`;
- this audit.

The historical proposal, historical authorization evidence, historical v1.0.0 execution evidence/schema, canonical runner and canonical v1.1.0 execution schema are not modified by this proposal.

## 12. Acceptance criteria for proposal review

Before authorization can be considered, review must confirm:

- proposal validates against its versioned schema;
- candidate is based on canonical `e97c1f6...`;
- v1.1.0 execution schema is pinned;
- old approvals are recorded as consumed/non-reusable;
- both fresh approvals are still `REQUIRED_NOT_GRANTED`;
- caps exactly match the canonical runner;
- privacy boundary is unchanged;
- v1.1 diagnostic reasons include both encoding and decoded-format failures;
- one-shot workflow remains absent;
- no SCO request/body access occurred while preparing the proposal;
- source/registry/classification/identity/matching/outreach gates remain closed.

## 13. Next gate

`HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_REVIEW`

A positive review at this gate would authorize preparation of **new authorization evidence and a temporary one-shot execution workflow** under a separately recorded fresh execution approval plus fresh transient-row privacy approval. It would not itself approve the source or downstream processing.
