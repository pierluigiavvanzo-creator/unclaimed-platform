# M3 California SCO — MVP-1 Same-Bytes Deeper Insurance Discovery Live Validation Authorization

Date: 2026-09-17

Status: **EXECUTED ONCE — APPROVALS CONSUMED — NON-REUSABLE**

## Gate

`HUMAN_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_LIVE_VALIDATION_AUTHORIZATION`

Owner authorization:

`APPROVO FRESH SAME-BYTES DEEPER LIVE VALIDATION + TRANSIENT-ROW PRIVACY — 256/MEMBER, 1024 TOTAL, 524288 SOURCE BYTES MAX`

Classification: `A — Product Critical`.

## Authoritative base

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- base branch: `mvp1-ca-same-bytes-deeper-insurance-discovery-offline`;
- base HEAD: `eebb18693c9a75de4d060bdfeb38d98d0975ccfc`;
- base CI: `35245311115` — SUCCESS;
- authorization checkpoint: `888ec27ffc7563698dbf84c3a454a5964a015c90`;
- execution branch: `mvp1-ca-same-bytes-deeper-live-validation-once`.

## Consumed single-use refs

Execution:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_REAL_SOURCE_VALIDATION_BOUNDED_D4F29A61`

Transient-row memory-only privacy:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_TRANSIENT_ROW_PRIVACY_BOUNDED_D4F29A61`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry or rerun is authorized.

## Pinned runtime

- deeper runner @ `d7c7321aa01a86af346dfbe8c1d7cde6e91d1755`;
- D-010 classifier @ `05e8637e42070dd6f04218592d20d4a230ab948e`;
- D-010 policy @ `840d09d87187c53d26f4d562527dcb92d810a9f3`;
- transport/archive runner @ `706183d5425da16b25f8186574cc356135803326`.

Invocation used module mode:

`python -m scripts.ca_sco_mvp1_same_bytes_deeper_insurance_discovery`

## Execution

Workflow run:

`35255228459` — attempt `1` — SUCCESS.

Lifecycle:

1. offline module/blobs/bounds preflight: PASS;
2. fresh refs consumed and persisted before source access: PASS;
3. exactly one live execution: PASS;
4. derived evidence privacy/hard-cap validation: PASS;
5. derived evidence persistence/upload: PASS;
6. one-shot workflow and trigger cleanup: COMPLETE.

Persisted evidence:

`sources/evidence/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.module_live_once.v1.json`

Evidence review:

`docs/audits/M3_CA_SCO_MVP1_SAME_BYTES_DEEPER_LIVE_EVIDENCE_REVIEW.md`

## Authorized / observed envelope

- HEAD: `1 / 1`;
- Range GET: `4 / 4`;
- HTTP total: `5 / 5`;
- Range body bytes: `131072` each;
- source-response bytes: `524288 / 524288`;
- complete logical rows: `256/member`, `1024 total`;
- no additional Range;
- no full-body fallback;
- no retry/rerun.

## Privacy result

PASS.

No raw body/row, `PROPERTY_ID`, per-row/source `PROPERTY_TYPE`, owner/holder values, identity resolution, beneficiary matching or outreach data was persisted or performed.

## Semantic result

- rows examined: `1024`;
- deferred unclassifiable: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- distinct authority-backed insurance codes: `[]`;
- result: `NO_INSURANCE_CODE_OBSERVED_IN_BOUNDED_SAMPLE`;
- stop reason: none.

California source activation remains held. The current `PROPERTY_TYPE` discovery path is frozen for MVP-1 pending genuinely new evidence; do not repeat the same scan with these consumed approvals.
