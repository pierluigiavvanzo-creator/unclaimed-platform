# M3 California SCO — MVP-1 Same-Bytes Deeper Live Evidence Review

Date: 2026-09-17

Status: **PASS EXECUTION / PASS PRIVACY / INSURANCE DISCOVERY NOT OBSERVED / CA PROPERTY_TYPE DISCOVERY PATH HELD**

## Scope

Review the single authorized same-bytes deeper live execution under:

`HUMAN_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_LIVE_VALIDATION_AUTHORIZATION`

Run:

`35255228459` — attempt `1` — SUCCESS.

Persisted derived evidence:

`sources/evidence/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.module_live_once.v1.json`

Approval record:

`sources/evidence/ca_sco_mvp1_same_bytes_deeper_insurance_discovery_live_validation_approval.v1.json`

## Authorization lifecycle

Fresh refs:

- execution: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_REAL_SOURCE_VALIDATION_BOUNDED_D4F29A61`;
- privacy: `OWNER_APPROVAL_2026-09-17_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_TRANSIENT_ROW_PRIVACY_BOUNDED_D4F29A61`.

Both were consumed before source access and are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry or rerun is authorized.

The temporary workflow and trigger were removed after execution.

## Transport result

PASS.

Observed live metadata matched the adopted baseline:

- HEAD status: `200`;
- content length: `162560390`;
- content type: `application/zip`;
- accept-ranges: `bytes`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- last-modified observed: `Wed, 16 Sep 2026 16:43:22 GMT`.

Authorized source use remained exactly within the unchanged same-byte boundary:

- HEAD requests: `1 / 1`;
- Range GET requests: `4 / 4`;
- HTTP requests total: `5 / 5`;
- source body bytes read: `524288 / 524288`;
- no additional Range;
- no full-body fallback;
- no full archive download.

## Same-bytes deeper classification result

The validator reached the full logical-row cap in every canonical member:

- member 1: `256` rows — `ROW_CAP_REACHED`;
- member 2: `256` rows — `ROW_CAP_REACHED`;
- member 3: `256` rows — `ROW_CAP_REACHED`;
- member 4: `256` rows — `ROW_CAP_REACHED`;
- total rows examined: `1024 / 1024`.

Classification result:

- `DEFER_UNCLASSIFIABLE`: `1024`;
- shape-valid non-target rows: `0`;
- recognized insurance rows: `0`;
- `IN03` rows: `0`;
- distinct authority-backed insurance codes: `[]`.

Semantic result:

`NO_INSURANCE_CODE_OBSERVED_IN_BOUNDED_SAMPLE`

Stop reason:

`null`

This is a `64x` increase in logical-row depth over the prior `16`-row run without increasing source-response bytes.

## Privacy result

PASS.

All safety-state flags are false. No raw source body, full row, `PROPERTY_ID`, per-row/source `PROPERTY_TYPE`, malformed value or derivative, owner/holder value, identity resolution, beneficiary matching, outreach or production classification activation was persisted or performed.

Persisted evidence is limited to aggregate counts, per-member scan metadata, exact recognized authority-backed insurance codes (none observed), request controls and transport metadata.

## Evidence interpretation

The evidence supports all of the following:

1. the adopted transport/archive path remains stable;
2. D-010 continuation remains valid against the live source;
3. the same four fixed compressed prefixes contain at least `256` complete rows per member under the existing transient caps;
4. no exact California authority-backed insurance code was observed in `1024` examined rows;
5. all `1024` examined `PROPERTY_TYPE` values remained unclassifiable under the unchanged deterministic boundary.

The evidence does **not** prove that the complete California source contains no insurance records. The scan is bounded and deterministic.

However, repeating or widening the same `PROPERTY_TYPE` discovery pattern is no longer the shortest credible path to MVP-1. The new evidence materially lowers the expected product value of another equivalent California `PROPERTY_TYPE` scan.

## Product decision

California source activation remains:

`HELD / NOT YET APPROVED`

The California SCO `PROPERTY_TYPE` discovery path is **frozen for MVP-1 pending genuinely new evidence or a separately justified authority-backed interpretation path**.

This is not source rejection and does not alter D-010. It is a prioritization decision under `PRODUCT_STRATEGY_MVP1.md` to avoid repeated diagnostics that do not shorten the path to the first economically actionable case.

Current state:

- approved real sources: `0`;
- production classification: inactive;
- real MVP-1 candidates: `0`.

## Next product-critical action

`BENCHMARK_MVP1_ALTERNATIVE_LAWFUL_REAL_SOURCE_PATHS_OFFLINE`

Classification: `A — Product Critical`.

Goal:

Select the highest-leverage lawful public/authorized source path that can expose insurance relevance deterministically with less semantic friction than the current California `PROPERTY_TYPE` path. Repository-first/reuse-first applies. The benchmark must compare concrete source candidates on authority/provenance, insurance-specific signal, machine accessibility, privacy burden, acquisition cost, update cadence and time-to-first-candidate.

No new California live access is part of that offline benchmark. Any later real-source access requires its own applicable authorization gate.
