# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

M3 California remains active only as the minimum critical-path enabler required to reach one lawful approved real source.

## Current Engineering Milestone

M3 — California Data Spike Readiness + Product Visibility

M0, M1 and M2 are VERIFIED.

## Current Working Checkpoint

Current branch:

`m3-ca-sco-v1-2-real-source-execution-once-adopted-baseline`

Latest completed action:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

Classification:

`A — Product Critical`

Execution trigger checkpoint:

- HEAD `273a402345783c07c5f3c7bc842e0cd0000b3f01`;
- one-shot run `35227857742` — **SUCCESS**, attempt `1`;
- artifact `10499528807`;
- artifact digest `sha256:e5addd9bebfa5524d03ce2c6766ca4997b84ab497d0a4a2f865d252619dc1b37`.

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_ADOPTED_BASELINE.md`

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_adopted_baseline.json`

## Adopted Transport / Archive-Layout Baseline

The live execution confirmed the adopted transport baseline:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- canonical offsets remain `0`, `59745428`, `96861315`, `134172553`.

Transport/archive-layout drift is not the active blocker.

## Real Execution Result

Machine result:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

D-008 `WHOLE_SOURCE_STOP` operated exactly as designed. No source continuation occurred.

Actual request use:

- HEAD `1`;
- Range `1`;
- HTTP total `2`;
- source body bytes read `131072`;
- full archive downloaded `false`.

No raw/source-value evidence was persisted.

## Authorization / Privacy State

Fresh approvals created from explicit Product Owner authorization:

- `OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_C18CDDFC`;
- `OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_C18CDDFC`.

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry is authorized.

Temporary one-shot workflow and trigger have been removed.

## Runtime / Contract Boundary

Unchanged:

- runner `scripts/ca_sco_property_type_semantic_verification.py`;
- runtime contract `1.2.0`;
- proposal `1.1.0`;
- regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser/projector;
- no trimming/casing/normalization;
- deterministic request/sample caps;
- no widening / no retry;
- D-008 fail-closed mapping;
- privacy/persistence allowlists.

## Product / Commercial State

- approved real sources: `0`;
- transport/archive-layout baseline: **CONFIRMED LIVE**;
- real-source semantic execution completed: `true`;
- semantic compatibility resolved positively: `false`;
- active blocker: `PROPERTY_TYPE` compatibility under current strict contract;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`;
- commercial baseline from real cases: not established;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED.

## Next Recommended Action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

Classification:

`A — Product Critical`

The review must not retry the consumed execution or reopen transport diagnostics. It should decide the shortest safe path to MVP-1:

1. a separately reviewed compatibility-remediation path grounded in authoritative source semantics; or
2. reject/defer this California source and move to another lawful source.

Use `docs/handovers/HANDOVER_CURRENT.md` as the restart point.