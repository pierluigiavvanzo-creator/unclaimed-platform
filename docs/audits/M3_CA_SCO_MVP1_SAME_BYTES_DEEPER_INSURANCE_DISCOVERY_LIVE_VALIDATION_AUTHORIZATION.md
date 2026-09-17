# M3 California SCO — MVP-1 Same-Bytes Deeper Insurance Discovery Live Validation Authorization

Date: 2026-09-17

Status: **AUTHORIZED — NOT YET EXECUTED**

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
- execution branch: `mvp1-ca-same-bytes-deeper-live-validation-once`.

## Fresh single-use refs

Execution:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_REAL_SOURCE_VALIDATION_BOUNDED_D4F29A61`

Transient-row memory-only privacy:

`OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_TRANSIENT_ROW_PRIVACY_BOUNDED_D4F29A61`

Both are single-use, non-reusable and do not authorize retry/rerun.

## Pinned runtime

- deeper runner: `scripts/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py` @ `d7c7321aa01a86af346dfbe8c1d7cde6e91d1755`;
- D-010 classifier @ `05e8637e42070dd6f04218592d20d4a230ab948e`;
- D-010 policy @ `840d09d87187c53d26f4d562527dcb92d810a9f3`;
- adopted transport/archive runner @ `706183d5425da16b25f8186574cc356135803326`.

Invocation must be module mode:

`python -m scripts.ca_sco_mvp1_same_bytes_deeper_insurance_discovery`

Direct file-path execution is not authorized.

## Authorized live envelope

- HEAD: max `1`;
- Range GET: max `4`;
- HTTP total: max `5`;
- Range body bytes: max `131072` each;
- source-response bytes: max `524288` total;
- complete logical rows: max `256/member`, `1024 total`;
- transient uncompressed bytes: max `262144/member`, `1048576 total`;
- logical record bytes: max `32768`;
- no additional Range;
- no full-body fallback;
- no retry/rerun.

## Semantic and privacy boundary

D-010 remains unchanged. No trimming, normalization, repair, uppercasing, regex relaxation or semantic inference is authorized.

Persisted evidence may contain only:

- aggregate row/classification counts;
- per-member rows examined;
- per-member scan status;
- exact recognized California authority-backed insurance codes (`IN01-IN08`, `IN99`);
- transport/request control metadata.

It must not persist raw bodies/rows, `PROPERTY_ID`, source `PROPERTY_TYPE` values or derivatives, owner/holder values, row hashes, exact malformed values, identity resolution results, beneficiary matching or outreach data.

## Execution discipline

The one-shot workflow must:

1. reject `run_attempt != 1`;
2. verify this authorization record and all pinned blobs offline;
3. verify module-mode startup offline;
4. consume both fresh refs and push the consumption record **before** source access;
5. execute exactly once within the authorized bounds;
6. validate the derived evidence privacy boundary and caps;
7. persist only the allowed derived evidence;
8. remove the workflow and trigger immediately after execution;
9. never reuse or rerun consumed refs.

## Product decision after the run

- if an exact authority-backed insurance code is observed, perform the bounded California source activation decision immediately and advance toward the MVP-1 vertical slice;
- if no insurance code is observed, do not infer source absence from the bounded prefix; record the evidence and make the next product-critical decision without repeating the same scan;
- true transport/structural failures remain fail-closed and require a fresh authorization for any later live access.
