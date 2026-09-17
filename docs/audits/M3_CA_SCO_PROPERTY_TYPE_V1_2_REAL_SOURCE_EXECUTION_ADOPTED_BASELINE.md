# M3 California SCO — PROPERTY_TYPE v1.2 Adopted-Baseline Real-Source Execution

Date: 2026-09-17

Status: **EXECUTED ONCE — STOPPED FAIL-CLOSED ON PROPERTY_TYPE_FORMAT_UNEXPECTED — APPROVALS CONSUMED — WORKFLOW REMOVED — EVIDENCE REVIEW REQUIRED**

## Task

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

Classification: `A — Product Critical`.

## Authorized base

- authorization branch: `m3-ca-sco-v1-2-real-source-execution-authorization-adopted-baseline`;
- authorization checkpoint: `7e4ebb91cd8d25be4f4b45ee08ec6bd3a5be5a36`;
- reviewed checkpoint: `c18cddfc92bf3bb69f40b76170e687136e7fd21a`;
- proposal version: `1.1.0`;
- runtime contract: `1.2.0`.

## One-shot lifecycle

Execution branch:

`m3-ca-sco-v1-2-real-source-execution-once-adopted-baseline`

Preflight-only run:

`35227794053` — **SUCCESS**

The source execution step was skipped because no trigger marker existed.

Real execution trigger commit:

`273a402345783c07c5f3c7bc842e0cd0000b3f01`

Real execution run:

`35227857742` — **SUCCESS**, attempt `1`.

Artifact:

- id: `10499528807`;
- name: `ca-sco-property-type-v1-2-real-source-execution-2026-09-17`;
- digest: `sha256:e5addd9bebfa5524d03ce2c6766ca4997b84ab497d0a4a2f865d252619dc1b37`.

The temporary trigger and workflow were removed immediately after the run. No retry path remains.

## Approval consumption

Execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_C18CDDFC`

Privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_C18CDDFC`

Both are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

## Transport verification

Expected and observed values matched:

- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- HEAD status: `200`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

Therefore the adopted transport/archive-layout baseline was not the blocker in this execution.

## Request boundary actually used

- HEAD requests: `1`;
- Range requests: `1`;
- HTTP requests total: `2`;
- source response-body bytes read: `131072`;
- full archive downloaded: `false`.

All configured request and byte caps remained respected.

## Machine result

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

This is the exact D-008 `WHOLE_SOURCE_STOP` behavior.

The run did not silently skip the condition and did not continue to later source members.

## Sample result

Persisted derived summary:

- `sample_rows_examined = 0`;
- rows examined per canonical member: all `0`;
- distinct PROPERTY_TYPE codes persisted: none;
- distinct insurance codes persisted: none.

The execution contract intentionally does not persist the nonconforming source value, its bytes, hash or exact length. Therefore the evidence proves structural nonconformance against the current strict boundary but does not disclose or identify the source value.

## Privacy / safety result

PASS.

All safety flags remained false, including:

- raw-body persistence;
- full-row persistence;
- PROPERTY_ID persistence;
- owner/holder persistence;
- per-row PROPERTY_TYPE persistence;
- temporary source files;
- identity resolution;
- beneficiary matching;
- outreach;
- production classification activation.

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_adopted_baseline.json`

## Product interpretation

The transport blocker is closed. The current blocker is now specifically semantic/contract compatibility of `PROPERTY_TYPE` under the unchanged regex and no-normalization policy.

This run does not support source approval for MVP-1 under the current contract. It also does not establish that the source is commercially unusable; it establishes only that the current validation boundary and the live source are incompatible at the first triggering condition reached by the bounded runner.

Do not retry this execution or reopen transport diagnostics without new contradictory evidence.

## Source / downstream state

- approved real sources: `0`;
- semantic compatibility resolved: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification: inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claims: blocked.

## Next gate

Execute:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

The review should make the minimum product-critical decision: either define a separately reviewed compatibility-remediation path grounded in authoritative source semantics, or reject/defer this California source for MVP-1 and move to another lawful source. No further transport work is justified by this execution.