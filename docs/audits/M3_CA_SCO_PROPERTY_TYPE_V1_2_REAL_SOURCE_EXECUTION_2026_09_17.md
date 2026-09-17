# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution — 2026-09-17

Date: 2026-09-17

Status: **EXECUTED ONCE — D-008 FAIL-CLOSED TRIGGERED — APPROVALS CONSUMED — CLEANUP REQUIRED — SOURCE NOT APPROVED**

## Task

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

Classification: `A — Product Critical`.

## Authorization

Authorization checkpoint:

`903c665af2641c56c85f1f57749ce6bd02e1b800`

Authorization audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION_2026_09_17.md`

Fresh execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_ED6A22A3`

Fresh transient-row privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_ED6A22A3`

Both approvals are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

No retry is authorized under these refs.

## One-shot execution

Execution branch:

`m3-ca-sco-v1-2-real-source-execution-once-2026-09-17`

Trigger commit:

`d826492735b6f6665d59ab875e470074005a8191`

GitHub Actions run:

`35222675324`

Run attempt:

`1`

Run result:

**SUCCESS**

Verified steps:

- authorization / branch / proposal / runtime / trigger preflight: PASS;
- exactly one bounded live runner invocation: PASS;
- execution-schema and hard-cap validation: PASS;
- derived-evidence artifact upload: PASS.

Artifact:

- id: `10496599995`;
- name: `ca-sco-property-type-v1-2-real-source-execution-2026-09-17`;
- digest: `sha256:3e52cdff838de4dfa73bf62b0361af6938be73f2aa381c68ecaf8bc1b1d37fe9`.

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once_2026_09_17.json`

## Real execution result

Machine result:

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`.

This is the exact D-008 `WHOLE_SOURCE_STOP` disposition required by the accepted contract.

No exact PROPERTY_TYPE value, raw row, PROPERTY_ID, owner/holder value, source bytes, source-field hash or exact source-field length is persisted or reported.

## Transport evidence

Transport metadata matched the adopted baseline exactly:

- HEAD status `200`;
- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

Therefore this result is not transport drift. The current adopted transport/archive-layout baseline was sufficient to reach the semantic validation boundary.

## Request / privacy boundary actually used

Actual network use:

- HEAD requests: `1`;
- Range requests: `1`;
- HTTP requests total: `2`;
- source response bytes read: `131072`.

The runner stopped within the first bounded member prefix before any row was accepted into the derived sample summary.

Persisted sample summary therefore remains:

- accepted sample rows: `0`;
- distinct persisted PROPERTY_TYPE codes: none;
- distinct persisted insurance codes: none.

Safety flags all remained `false`:

- no full archive download;
- no raw body persistence;
- no full-row persistence;
- no PROPERTY_ID persistence;
- no owner/holder persistence;
- no per-row PROPERTY_TYPE persistence;
- no transient source file;
- no identity resolution;
- no beneficiary matching;
- no outreach;
- no production classification activation.

## Execution interpretation

The run provides direct current evidence that the California SCO `$500+` source, under the unchanged v1.2 validation contract and D-008 policy, reaches `PROPERTY_TYPE_FORMAT_UNEXPECTED` in the bounded deterministic prefix and must stop whole-source fail-closed.

It does not establish the hidden value, source intent, global frequency or whether a different future contract could lawfully accept the source.

Under the **current** contract, however, the source cannot be approved for the MVP-1 vertical slice because deterministic continuation is prohibited by D-008.

## Product impact

Further retries or transport diagnostics would not address the observed blocker and are not authorized. Under the MVP-1 product strategy, repeating them would add user time without opening the commercial path.

The commercially shortest safe path is to freeze this California source under the current contract and select the next lawful real-source candidate, unless the Product Owner later explicitly chooses to redesign the PROPERTY_TYPE semantic contract.

## Cleanup

The temporary workflow and trigger must be deleted in the cleanup checkpoint containing this execution record. No workflow-based retry path may remain.

## Next action

Perform repository-only evidence review/source decision and then move directly to:

`SELECT_ALTERNATE_REAL_SOURCE_FOR_MVP1`

Do not perform another California SCO request under the consumed approvals.