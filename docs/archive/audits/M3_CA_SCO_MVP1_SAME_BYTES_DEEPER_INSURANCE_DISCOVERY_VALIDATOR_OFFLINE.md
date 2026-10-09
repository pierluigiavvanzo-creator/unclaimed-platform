# M3 California SCO — MVP-1 Same-Bytes Deeper Insurance Discovery Validator Offline

Date: 2026-09-17

Status: **PASS — OFFLINE VALIDATOR READY FOR FRESH SINGLE-USE LIVE AUTHORIZATION**

## Scope

Implement exclusively:

`IMPLEMENT_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_VALIDATOR_OFFLINE`

Classification: `A — Product Critical`.

No California source request was made by this work package.

## Authoritative base

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- base branch: `mvp1-ca-property-type-row-defer-live-validation-module-once`;
- base HEAD: `846d59debd4d62e2e1253f648d7c63b3aa43c07c`;
- base CI: `35243614321` — SUCCESS;
- D-010: `ROW_DEFER_CONTINUE_METADATA_ONLY`;
- prior live evidence: `sources/evidence/ca_sco_mvp1_property_type_row_defer.module_live_once.v2.json`.

The prior live sample processed `16/16` rows, deferred all `16`, observed no authority-backed insurance code, and left source activation held.

## Reuse-first result

The implementation reuses the existing repository components rather than introducing a new parser, ZIP library or source client:

- adopted HEAD/Range transport and hard byte envelope;
- canonical ZIP local-header parser;
- `_RecordCollector` logical-record framing;
- strict CSV header/projector behavior;
- existing uncompressed/logical-record hard caps;
- D-010 California PROPERTY_TYPE classifier;
- Python standard-library `zlib` already used by the historical runner.

Decision: `REUSE / WRAP` existing deterministic components. No external dependency is justified because the repository already covers the required transport, deflate, CSV projection, classification and fail-closed behavior; adding a third-party component would increase integration and security surface without reducing the critical-path work.

## Implementation

New runner:

`scripts/ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

Blob:

`d7c7321aa01a86af346dfbe8c1d7cde6e91d1755`

New tests:

`tests/unit/test_ca_sco_mvp1_same_bytes_deeper_insurance_discovery.py`

Blob:

`2ffd378a4b9a94eef8f68907b0dbd24660fbcb8b`

The historical/live-validated D-010 runner is not modified.

## Same-byte contract

Any later separately authorized live execution of this runner remains bounded by the existing source-response envelope:

- HEAD: max `1`;
- Range GET: max `4`;
- HTTP total: max `5`;
- Range bytes: `131072` each;
- total source response-body bytes: max `524288`;
- no additional Range;
- no full-body fallback.

Only logical-row depth increases.

New logical-row caps:

- max complete data rows per canonical member: `256`;
- max complete data rows total: `1024`.

Existing transient decompression caps remain unchanged:

- max uncompressed bytes per member: `262144`;
- max uncompressed bytes total: `1048576`;
- max logical record bytes: `32768`.

This gives a maximum logical-row depth increase of `64x` over the previous `4 rows/member` sample without increasing source-response bytes.

## Row handling

- only complete logical CSV records are classified;
- an incomplete trailing record at the end of a fixed Range prefix is ignored rather than persisted or guessed;
- nonconforming/unknown values remain `DEFER_UNCLASSIFIABLE` under D-010;
- no trimming, uppercasing, normalization, repair, regex relaxation or semantic inference is introduced;
- exact authority-backed insurance codes remain `IN01-IN08` and `IN99`;
- `IN03` remains the primary MVP-1 target;
- row content, source PROPERTY_TYPE values, PROPERTY_ID, owner/holder values and PII are not persistence outputs;
- persisted/returned discovery evidence is limited to aggregate counts, per-member row counts/scan status and exact recognized authority-backed insurance codes.

Structural/transport/header/CSV-column/byte-cap failures remain fail-closed.

## Offline test evidence

CI:

`35244998206` — SUCCESS.

Verified:

1. module-mode CLI startup works offline;
2. `IN03` located after the historical four-row boundary is discovered;
3. source request/byte envelope remains `1 HEAD + 4 Range + 524288 bytes` in the synthetic transport contract;
4. the `256 rows/member` hard cap prevents row `257` from being observed;
5. authority-backed `IN01`/`IN99` are reported without inventing `IN03`;
6. transport metadata drift still stops before Range reads;
7. Ruff, mypy, contract tests, smoke tests, full pytest, Streamlit safety/startup, frontend lint/typecheck/build all pass.

## Product decision

The offline hypothesis is technically ready for one fresh bounded real-source validation.

This audit does **not**:

- approve the California source;
- activate the registry;
- activate production classification;
- authorize source access;
- authorize transient-row privacy exposure;
- authorize retry or rerun;
- create a real candidate.

## Next gate

`HUMAN_CA_SCO_MVP1_SAME_BYTES_DEEPER_INSURANCE_DISCOVERY_LIVE_VALIDATION_AUTHORIZATION`

A fresh explicit Product Owner authorization must mint exactly one single-use execution approval plus one single-use transient-row privacy approval before any live source access.

If a recognized insurance code is observed, perform the source activation decision immediately and move toward the MVP-1 vertical slice. Do not reopen generic PROPERTY_TYPE/transport diagnostics.
