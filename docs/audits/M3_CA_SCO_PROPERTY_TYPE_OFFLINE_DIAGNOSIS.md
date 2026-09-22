# M3 California SCO — PROPERTY_TYPE Offline Evidence Review and Diagnosis

Date: 2026-09-15

Status: **OFFLINE / SYNTHETIC DIAGNOSIS ONLY — NO NEW SCO NETWORK ACCESS**

## Scope

This audit reviews the persisted evidence from the single bounded real `PROPERTY_TYPE` semantic attempt and diagnoses the existing runner using repository code plus synthetic CSV fixtures only.

No SCO request, source-body access, retry, workflow creation, source approval, registry activation, production classification, identity resolution, beneficiary matching or outreach is authorized or performed by this task.

The prior execution authorization was consumed by workflow run `34965097988` and is not reused here.

## Evidence reviewed

- Execution evidence: `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`
- Execution audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_EXECUTION.md`
- Runner: `scripts/ca_sco_property_type_semantic_verification.py`
- Runner unit tests: `tests/unit/test_ca_sco_property_type_semantic_verification_runner.py`
- Semantic proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`
- Execution schema: `schemas/common/property_type_semantic_verification_execution.schema.json`

Persisted real-run facts remain unchanged:

- semantic result `STOPPED_FAIL_CLOSED`;
- stop reason `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- 1 HEAD request;
- 1 Range GET;
- 2 HTTP requests total;
- 131,072 source-body bytes read;
- 0 accepted/examined rows;
- no retry;
- no offending `PROPERTY_TYPE` value persisted or logged.

## What the existing stop path proves

The real run passed the fixed transport identity checks and obtained the expected first-member Range. It also progressed through local ZIP-member parsing, DEFLATE prefix processing, collection of the required logical records, and exact canonical-header verification before the first data-row semantic processing stopped.

Therefore the observed stop is downstream of transport identity, first-member ZIP metadata and exact header verification.

The evidence does **not** establish the content of the offending value, and this audit does not infer it.

## Root-cause ambiguity discovered

The existing runner emits the same reason code, `PROPERTY_TYPE_FORMAT_UNEXPECTED`, from two materially different failure paths:

1. `_project_property_type()` catches `UnicodeDecodeError` while decoding the projected field as UTF-8 and maps it to `PROPERTY_TYPE_FORMAT_UNEXPECTED`.
2. `_process_member()` maps a successfully decoded, non-empty `PROPERTY_TYPE` that does not match `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` to the same `PROPERTY_TYPE_FORMAT_UNEXPECTED` reason.

This means the historical real-run evidence cannot distinguish:

- **encoding path:** the projected field bytes were not valid UTF-8; or
- **shape path:** the field decoded successfully but did not satisfy the current token-shape rule.

This is a diagnostic limitation in the runner's failure taxonomy. It is not evidence that either specific cause occurred.

### Consequence for previous inference

Because an encoding failure can raise the same stop reason inside `_project_property_type()` before the caller receives the projected value and column count, the persisted stop reason alone does **not** prove that the caller reached the 25-column check, non-empty check and regex check.

If the stop came from the shape path, then the row had already passed the 25-column and non-empty checks. If it came from the encoding path, those downstream caller checks were not reached. Current evidence cannot choose between these branches.

## Synthetic parser differential review

A new offline regression test compares the custom `_project_property_type()` projector with Python's standard-library `csv.reader(..., strict=True)` using privacy-safe synthetic 25-column records covering:

- ordinary CSV;
- commas in the first field;
- escaped quotes in the first field;
- an embedded newline in an unrelated field;
- commas and escaped quotes in a later field;
- an embedded CRLF in an unrelated field;
- all-fields-quoted CSV.

For this deterministic matrix, the custom projector must return the same field at zero-based index `1` as `csv.reader` and report exactly 25 columns.

This is evidence only for the tested standard CSV cases. It does not prove the real SCO row uses exactly the same dialect or that the custom parser is universally correct.

## Synthetic reproduction of the ambiguity

The offline regression suite constructs two synthetic first-member prefixes:

- a valid UTF-8 row whose synthetic `PROPERTY_TYPE` has leading whitespace and therefore fails the existing regex;
- a row whose synthetic projected `PROPERTY_TYPE` contains an invalid UTF-8 byte.

Under the current runner, both produce exactly:

`PROPERTY_TYPE_FORMAT_UNEXPECTED`

This deterministically reproduces the diagnostic collision without using any real source data.

## Regex assessment

The current rule is:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The repository's authoritative semantic proposal supports the official California SCO insurance codes `IN01-IN08` and `IN99`, but the current persisted real evidence does not reveal the actual first-row value.

Therefore there is **no evidence basis in this task to loosen, trim, normalize, lowercase-fold or otherwise change the regex or source value**.

Examples such as leading/trailing whitespace, lowercase codes or different code lengths are synthetic diagnostic probes only. They are not claims about the SCO data.

## Diagnosis outcome

Supported conclusions:

1. The real attempt reached first-member data-row semantic processing after transport/member/header checks.
2. A projection failure caused the fail-closed stop before any row was accepted.
3. The current stop taxonomy conflates UTF-8 decoding failure with decoded-value regex mismatch.
4. The custom field projector matches `csv.reader` on the committed deterministic standard-CSV edge-case matrix.
5. No standard-CSV projection defect is reproduced by that matrix.
6. The real root cause remains unresolved because the offending value/bytes were intentionally not retained.
7. There is no current basis to relax the semantic regex.

Not supported:

- claiming the real value contained whitespace;
- claiming the real value was non-UTF-8;
- claiming the SCO dataset violates NAUPA codes;
- claiming the custom parser is definitively bug-free;
- retrying the source to discover the value;
- widening privacy, row, request or byte budgets.

## Smallest remediation proposal

The smallest safe next code change is **offline-only diagnostic taxonomy remediation**, not another network attempt:

- introduce a distinct future stop reason such as `PROPERTY_TYPE_ENCODING_UNEXPECTED` for UTF-8 decode failure;
- keep `PROPERTY_TYPE_FORMAT_UNEXPECTED` for successfully decoded values that fail the existing shape rule;
- preserve historical execution evidence unchanged and schema-valid;
- add regression tests for both branches;
- do not add raw values, bytes, hashes, lengths, prefixes or per-row diagnostics to persisted/logged evidence without a separate privacy design and human review;
- keep the one-shot network workflow absent.

This remediation changes a machine contract and runner behavior, so it should be implemented only after an explicit human review gate rather than silently folded into this diagnosis.

## Governance state

Unchanged:

- source policy `PROPOSED`;
- source real acquisition authorization `false`;
- registry disabled and not approved;
- approved real sources `0`;
- production classification inactive;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED;
- one-shot network workflow ABSENT.

## Next gate

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_REVIEW`

The next decision is whether to authorize the offline-only contract/runner remediation that separates encoding failure from format failure. Even after that remediation, a second real SCO execution would still require a separate fresh execution authorization plus transient-row privacy authorization.
