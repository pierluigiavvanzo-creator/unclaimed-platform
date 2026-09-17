# M3 California SCO — PROPERTY_TYPE v1.2 Adopted-Baseline Real-Source Execution Authorization

Date: 2026-09-17

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — PASS — SINGLE-USE EXECUTION + PRIVACY APPROVALS CONSUMED — EXECUTED ONCE — NON-REUSABLE**

## Authorization gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

## Owner authorization

The Product Owner explicitly authorized:

`APPROVO FRESH SINGLE-USE EXECUTION + TRANSIENT-ROW PRIVACY`

This authorization applied only to the frozen, human-reviewed proposal `1.1.0` and adopted transport/archive-layout baseline.

## Authoritative checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- authorization base branch: `m3-ca-sco-v1-2-proposal-contract-preservation-remediation`
- authorization base HEAD: `c18cddfc92bf3bb69f40b76170e687136e7fd21a`
- authorization base CI: `35221904089` — **SUCCESS**
- proposal review result: `PASS_REMEDIATED_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_FOR_FRESH_SINGLE_USE_AUTHORIZATION`
- proposal version: `1.1.0`
- runtime contract: `1.2.0`

## Fresh approval references

Execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_C18CDDFC`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_C18CDDFC`

Both approvals are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They were consumed when GitHub Actions run `35227857742`, attempt `1`, invoked the authorized live runner. No retry is authorized under these refs.

## Execution lifecycle

- authorization checkpoint: `7e4ebb91cd8d25be4f4b45ee08ec6bd3a5be5a36`;
- execution branch: `m3-ca-sco-v1-2-real-source-execution-once-adopted-baseline`;
- preflight run: `35227794053` — SUCCESS, source execution skipped;
- real execution trigger commit: `273a402345783c07c5f3c7bc842e0cd0000b3f01`;
- real execution run: `35227857742` — SUCCESS;
- run attempt: `1`;
- artifact id: `10499528807`;
- artifact digest: `sha256:e5addd9bebfa5524d03ce2c6766ca4997b84ab497d0a4a2f865d252619dc1b37`;
- temporary trigger removed after execution;
- temporary workflow removed after execution.

## Authorized adopted baseline used

- expected content length: `162560390`;
- expected ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- canonical member offsets: `0`, `59745428`, `96861315`, `134172553`.

Observed transport metadata matched the adopted baseline.

## Actual bounded request use

- HEAD requests: `1`;
- Range requests: `1`;
- HTTP requests total: `2`;
- source body bytes read: `131072`;
- full archive downloaded: `false`.

All hard caps were respected.

## Execution outcome

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

D-008 therefore operated exactly as authorized. Source continuation stopped immediately.

## Privacy / persistence result

PASS.

No raw body, full row, `PROPERTY_ID`, owner/holder value, per-row `PROPERTY_TYPE`, offending bytes/hash/exact length, or source-value-bearing control metadata was persisted. No identity resolution, beneficiary matching, outreach or production classification occurred.

Permitted derived evidence is stored at:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_adopted_baseline.json`

## Product/source state

This execution does not approve the source for production. Semantic compatibility is not resolved positively under the current strict boundary because the live bounded run reached `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real sources remain `0`; production classification remains inactive.

`DECISIONS.md` remains unchanged.

## Next gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

The evidence review must not retry the consumed execution. Its purpose is to decide the minimum safe product-critical path to resolve the `PROPERTY_TYPE` compatibility blocker or reject this source for MVP-1.