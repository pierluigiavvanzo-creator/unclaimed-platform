# M3 CA SCO PROPERTY_TYPE Semantic Runner Design Review

Date: 2026-09-15  
Status: DESIGN REVIEW ONLY — IMPLEMENTATION AND EXECUTION NOT AUTHORIZED

## Scope

This review translates the canonical `PROPERTY_TYPE` semantic-verification proposal into an implementation-ready deterministic runner design without creating or executing the runner.

No California SCO request is made by this task. No CSV data row is read. No transient row privacy approval is granted.

Canonical proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`

Canonical structure evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`

## Reuse-first review

### Existing repository implementation

`REUSE`

`scripts/ca_sco_500_plus_data_scope_inspection.py` already implements the critical bounded transport primitives needed here:

- exact HTTPS host/path binding;
- HEAD metadata verification;
- explicit `Range` + `If-Match`;
- hard rejection of non-206 responses before consuming an unexpected full body;
- exact `Content-Range` verification;
- ZIP local-header parsing;
- STORED/DEFLATED handling;
- bounded incremental decompression;
- fail-closed reason codes;
- no raw source persistence.

The semantic runner should reuse or extract these primitives rather than introduce a second transport model.

### Python standard library

`REUSE`

Use `http.client`, `ssl`, `struct`, `zlib`, `csv`, `re`, `json`, and `pathlib`.
Python `zipfile`/`zlib` documentation is useful as format/reference guidance, but the runner should keep explicit byte/request control rather than delegate remote I/O.

Reference:
https://docs.python.org/3/library/zipfile.html

### python-remotezip / remotezip

`REJECT FOR THIS RUNNER`

Observed 2026-09-15:

- PyPI package `remotezip` 0.12.6;
- MIT license;
- Python 3.11 compatible;
- PyPI classifier `Production/Stable`;
- GitHub repository `gtsystem/python-remotezip` shows active CI and approximately 134 stars / 29 forks in the retrieved evidence.

Reason for rejection:
the project requires exact request counts, exact response-byte caps, no automatic request widening, explicit fail-closed behavior when a server ignores Range, and derived-summary-only persistence. A general-purpose remote ZIP abstraction adds behavior and dependency surface that is unnecessary because the repository already has a verified bounded Range implementation.

Reference:
https://pypi.org/project/remotezip/
https://github.com/gtsystem/python-remotezip

### Papyrine/RemoteZip

`REJECT`

This is a C#/.NET library rather than Python. Its documented fallback can buffer the full file when a server ignores Range. That is explicitly incompatible with this project, which must stop without reading a full-body `200` response.

Reference:
https://github.com/Papyrine/RemoteZip

## Deterministic runner design

The future runner path is fixed:

`scripts/ca_sco_property_type_semantic_verification.py`

It remains ABSENT in this design candidate.

The future one-shot workflow path is fixed:

`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

It also remains ABSENT.

### Inputs

A future runner must require:

1. non-empty execution approval reference;
2. non-empty transient-row privacy approval reference;
3. output path;
4. fixed 10-second network inactivity timeout unless a later proposal changes it.

The endpoint is not caller-selectable.

### Preflight order

1. Load and validate the canonical proposal.
2. Require runtime evidence of separate implementation/execution authorization.
3. Require transient-row privacy approval.
4. Perform exactly one HEAD against the fixed endpoint.
5. Verify HTTP 200, exact Content-Length, media type, `Accept-Ranges`, and ETag.
6. For each of the four canonical members, issue at most one fixed 131,072-byte Range GET from the canonical local-header offset.
7. Require HTTP 206 and exact `Content-Range`.
8. Parse the ZIP local header and validate member metadata.
9. Incrementally DEFLATE in memory.
10. Verify the exact canonical 25-column CSV header before accepting any data row.
11. Parse at most four complete rows/member.
12. Read/project only column index 1 (`PROPERTY_TYPE`) for semantic evaluation.
13. Discard transient full-row material immediately.
14. Persist only the derived summary contract.

## Exact safety caps

- 4 canonical CSV members;
- 4 rows/member maximum;
- 16 rows total maximum;
- 1 HEAD maximum;
- 4 Range GET maximum;
- 5 HTTP requests total maximum;
- 131,072 source bytes per Range maximum;
- 524,288 source response-body bytes total maximum;
- 262,144 uncompressed transient bytes/member maximum;
- 1,048,576 uncompressed transient bytes total maximum;
- 32,768 bytes/logical CSV record maximum;
- no additional Range request;
- no full-body fallback.

These are project safety caps, not source facts.

## Range-ignore behavior

If the server returns `200` or any status other than `206` to a Range GET:

- do not consume the response body;
- stop as `RANGE_RESPONSE_NOT_PARTIAL`;
- do not retry with a broader request;
- do not fall back to full download.

This is a hard design invariant.

## Row/privacy behavior

Because the source is CSV, prohibited owner/holder values may exist in the same transient decompressed row bytes even though only `PROPERTY_TYPE` is projected.

Therefore:

- transient full-row privacy approval remains mandatory before execution;
- no raw row may be persisted;
- `PROPERTY_ID` must not be used or persisted in this semantic check;
- owner/holder values must not be used, persisted, or logged;
- per-row `PROPERTY_TYPE` values must not be logged or persisted;
- only distinct code sets and aggregate counts may be persisted;
- transient buffers have retention `0 days` and are disposed immediately after projection or STOP.

## Semantic behavior

Code shape:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Official insurance codes:
`IN01`, `IN02`, `IN03`, `IN04`, `IN05`, `IN06`, `IN07`, `IN08`, `IN99`.

A future execution may produce:

- `SAMPLE_COMPATIBLE_INSURANCE_CODE_OBSERVED`;
- `SAMPLE_CODE_SHAPE_COMPATIBLE_NO_INSURANCE_CODE_OBSERVED`;
- `STOPPED_FAIL_CLOSED`.

No outcome activates production classification.

## New contracts in this candidate

- `schemas/common/property_type_semantic_runner_design.schema.json`
- `schemas/common/property_type_semantic_verification_execution.schema.json`
- `schemas/examples/ca_sco_500_plus_property_type_semantic_verification_execution.examples.json`
- `sources/proposals/ca_sco_segment_500_plus.property_type_semantic_runner_design.v1.json`
- `tests/contract/test_ca_sco_property_type_semantic_runner_design.py`

The execution contract deliberately contains only derived data and transport/request counters. It has no field capable of carrying raw rows, `PROPERTY_ID`, owner values, holder values, or per-row `PROPERTY_TYPE`.

## Gate conclusion

Design status:
`DESIGN_REVIEW_ONLY_NOT_IMPLEMENTATION_AUTHORIZED`

Runner:
ABSENT

Network workflow:
ABSENT

Network/body access in this task:
0

Next gate:
`HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL`

Only after that gate may the runner file be implemented. Actual one-shot execution that reads real rows remains a later, separate approval and still requires transient-row privacy approval.
