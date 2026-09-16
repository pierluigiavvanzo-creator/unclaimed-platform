# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-once`

Created from authorization checkpoint:

`5872db1368a5b9a2cdee79a0c2e54aa0b9b00dfa`

Authorization CI:

`35121670753` — **SUCCESS**

## Completed Action

Completed:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

Execution result:

`STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`

The authorized real-source execution occurred exactly once. It stopped deterministically after the live HEAD metadata differed from the runner's pinned transport metadata, before any source body or row was read.

## Execution Evidence

Real execution trigger checkpoint:

`c32df1725390de8784e9bb2f29bea8b4f933abac`

One-shot workflow run:

`35123686954` — **SUCCESS**, attempt `1`

Artifact:

- id: `10457344882`;
- name: `ca-sco-property-type-v1-2-real-source-execution-2026-09-16`;
- digest: `sha256:c4146f9bced7722fa5da26a8c1d2ace5a65e610fac7ae190d720bd098e06e6e0`.

Cleanup/evidence checkpoint:

`448e209d7c8afaec4e0f4b6efc1e5598803d87e5`

Cleanup/evidence CI:

`35124024271` — **SUCCESS**

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`

Evidence contract test:

`tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`

## Approval State

Execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They became consumed when run `35123686954` invoked the real-source runner.

No retry is authorized. These approval refs must not be reused.

All historical execution/privacy approvals also remain consumed and non-reusable.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect, in this order as relevant:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`
2. `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`
3. `tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`
4. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION.md`
5. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_REVIEW.md`
6. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`
7. `scripts/ca_sco_property_type_semantic_verification.py`
8. `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json`
9. historical v1.1 execution evidence as needed.

## Actual Request / Data Boundary

Actual execution usage:

- HEAD requests: `1`;
- Range requests: `0`;
- HTTP requests total: `1`;
- source body bytes read: `0`;
- sample rows examined: `0`;
- rows examined in every canonical member: `0`;
- distinct `PROPERTY_TYPE` codes observed: none;
- distinct insurance codes observed: none.

No source row, `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder or other record value was observed or persisted.

## Transport Metadata Evidence

Pinned expected metadata:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type: `application/zip`;
- Accept-Ranges: `bytes`.

Observed live HEAD metadata:

- HTTP status: `200`;
- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

The content-length and ETag differences caused:

`TRANSPORT_METADATA_DRIFT`

The execution stopped before body access.

## v1.2 / D-008 Interpretation

Machine result:

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

`control_disposition = null` is correct because this was an unrelated transport stop.

The accepted D-008 mapping for `PROPERTY_TYPE_FORMAT_UNEXPECTED` was not reached, and this run provides no new evidence about the semantic compatibility of `PROPERTY_TYPE`.

Semantic compatibility remains unresolved.

The evidence does not establish whether source contents, archive structure or source semantics changed. It establishes only that the live archive's HEAD metadata no longer matches the pinned transport metadata.

No transport-baseline update is authorized by this result alone.

## Workflow Lifecycle

The temporary workflow:

`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

and marker:

`.github/ca-sco-property-type-semantic-verification-once.trigger.json`

were removed immediately after the single execution.

No one-shot workflow or retry path remains in the current repository tree.

## Privacy / Safety

All persisted evidence remains derived and non-row-bearing.

No raw body, full row, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact source-field length, real-row quarantine or row-specific human inspection was persisted.

All safety flags in the execution evidence are `false`.

No privacy expansion occurred.

## Source / Downstream Governance

Current state:

- one-shot real-source execution performed: `true`;
- execution count under fresh refs: `1`;
- fresh execution approval consumed: `true`;
- fresh privacy approval consumed: `true`;
- retry authorized: `false`;
- temporary workflow present: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

`DECISIONS.md` is intentionally unchanged because this execution applies existing D-008 and the prior bounded authorization and introduces no new architectural decision.

## SINGLE NEXT ACTION

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

This is a repository-only human evidence review.

It may assess the persisted derived evidence and decide what governance proposal, if any, should follow from the transport metadata drift.

It must not perform another source request, retry the execution, reuse consumed approval refs, update the pinned transport metadata, modify runtime/parser/projector/regex/normalization, widen privacy/source continuation, activate source policy/registry/production classification or begin downstream work.

## Restart Instruction

1. verify remote HEAD of the current execution branch;
2. verify latest CI for that exact HEAD;
3. read the five canonical files in order;
4. read the execution audit, derived evidence and evidence contract test;
5. inspect authorization/proposal artifacts as needed;
6. execute only the `SINGLE NEXT ACTION`;
7. perform no real-source request during evidence review.
