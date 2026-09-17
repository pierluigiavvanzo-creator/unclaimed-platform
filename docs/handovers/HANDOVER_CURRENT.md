# HANDOVER_CURRENT.md

Last updated: 2026-09-17

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical technical source of truth.

## Current Working Branch

`m3-ca-sco-v1-2-real-source-execution-once-adopted-baseline`

Always verify remote HEAD and latest CI before any new modification.

## Priority Product Strategy

Read immediately after `AGENTS.md`:

`PRODUCT_STRATEGY_MVP1.md`

Priority objective:

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

Optimize for the shortest safe path to one approved real source and then immediately to the MVP-1 vertical slice.

## Latest Completed Action

Completed:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

Classification:

`A — Product Critical`

## Owner Authorization Used

Owner authorization:

`APPROVO FRESH SINGLE-USE EXECUTION + TRANSIENT-ROW PRIVACY`

Fresh execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_C18CDDFC`

Fresh privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_C18CDDFC`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry is authorized.

Authorization audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_ADOPTED_BASELINE_AUTHORIZATION.md`

## Execution Lifecycle

Authorization checkpoint:

`7e4ebb91cd8d25be4f4b45ee08ec6bd3a5be5a36`

Execution branch:

`m3-ca-sco-v1-2-real-source-execution-once-adopted-baseline`

Preflight-only workflow run:

`35227794053` — **SUCCESS**

The live execution step was skipped in preflight.

Real execution trigger commit:

`273a402345783c07c5f3c7bc842e0cd0000b3f01`

One-shot real execution run:

`35227857742` — **SUCCESS**, attempt `1`.

Artifact:

- id `10499528807`;
- name `ca-sco-property-type-v1-2-real-source-execution-2026-09-17`;
- digest `sha256:e5addd9bebfa5524d03ce2c6766ca4997b84ab497d0a4a2f865d252619dc1b37`.

Temporary workflow and trigger were removed immediately after the run.

## Persisted Derived Evidence

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_adopted_baseline.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_ADOPTED_BASELINE.md`

## Adopted Transport Baseline — Live Result

Expected and observed transport metadata matched:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- HEAD status `200`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Therefore transport/archive-layout drift is not the active blocker.

## Actual Request Boundary

The single authorized run used:

- HEAD requests: `1`;
- Range requests: `1`;
- HTTP total: `2`;
- source body bytes read: `131072`;
- full archive download: `false`.

All hard caps were respected.

## Machine Result

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

This is the exact D-008 `WHOLE_SOURCE_STOP` outcome. No continuation occurred.

Persisted sample summary contains zero row values and no source code values. The contract intentionally prevents persistence of the nonconforming value, bytes, hash or exact length.

## Privacy / Safety Result

PASS.

No raw body, full row, PROPERTY_ID, owner/holder value, per-row PROPERTY_TYPE, offending value material or source-value-bearing control metadata was persisted.

No temporary source file, identity resolution, beneficiary matching, outreach or production classification occurred.

## Source / Product State

- transport/archive-layout baseline: live-confirmed;
- semantic compatibility resolved positively: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- production classification: inactive;
- real MVP-1 candidate cases: `0`;
- active blocker: `PROPERTY_TYPE` compatibility under the current strict validation/no-normalization contract;
- identity resolution, genealogy, beneficiary matching, outreach and claims remain BLOCKED.

## Canonical Read Order Before Any New Change

1. `AGENTS.md`
2. `PRODUCT_STRATEGY_MVP1.md`
3. `PROJECT_STATE.md`
4. `ROADMAP.md`
5. `DECISIONS.md`
6. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect at least:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_ADOPTED_BASELINE_AUTHORIZATION.md`;
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_ADOPTED_BASELINE.md`;
3. `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_adopted_baseline.json`;
4. proposal `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`;
5. runner `scripts/ca_sco_property_type_semantic_verification.py`;
6. D-008 in `DECISIONS.md`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

Classification:

`A — Product Critical`

The review must not perform another California SCO request or reuse the consumed approvals.

It must establish the minimum safe product decision from the evidence:

- transport is confirmed and should not be re-diagnosed;
- the live run reached `PROPERTY_TYPE_FORMAT_UNEXPECTED` under the unchanged strict regex;
- D-008 fail-closed mapping operated correctly;
- the exact source value was intentionally not persisted and must not be guessed;
- the source is not yet approved for production.

The review should choose between:

1. a separately reviewed compatibility-remediation proposal grounded in authoritative California source semantics; or
2. rejecting/deferring this California source for MVP-1 and moving to another lawful source.

Do not add broad diagnostics, infrastructure or governance work. The next action after evidence review should materially shorten the path to the first approved real source.