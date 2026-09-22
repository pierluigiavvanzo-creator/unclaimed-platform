# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution

Date: 2026-09-16

Status: **EXECUTED ONCE — STOPPED FAIL-CLOSED ON TRANSPORT_METADATA_DRIFT — APPROVALS CONSUMED — WORKFLOW REMOVED — HUMAN EVIDENCE REVIEW REQUIRED**

## Task

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

## Authorized base

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- authorization branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-authorization`
- authorization HEAD: `5872db1368a5b9a2cdee79a0c2e54aa0b9b00dfa`
- authorization CI: `35121670753` — **SUCCESS**
- authorization result: `PASS_FRESH_SINGLE_USE_EXECUTION_PRIVACY_APPROVALS_GRANTED_ONE_SHOT_PATH_AUTHORIZED_EXECUTION_NOT_PERFORMED`
- reviewed proposal SHA: `a2139884d99bcd0bd1c06ea7374778347bbd64b1`
- runtime contract: `1.2.0`

## Execution branch / preflight

Execution branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-once`

A temporary one-shot workflow was staged first without an execution marker. Its initial preflight run `35122352570` completed successfully with the real-source execution step skipped.

Historical tests that incorrectly treated the current repository filesystem as their historical workflow state were isolated only during staging. The final staging checkpoint was:

- staging HEAD: `9b06673fdadd76a753d0029a991b5951f5c0f1a0`;
- staging CI: `35123453086` — **SUCCESS**;
- ruff: PASS;
- mypy: PASS;
- contract tests: `245 passed`;
- smoke tests: `6 passed`;
- full pytest: PASS;
- frontend lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS.

All temporary staging-only test support was removed before the real execution marker was committed.

## One-shot trigger / drift guard

Real execution trigger commit:

`c32df1725390de8784e9bb2f29bea8b4f933abac`

Comparison from authorization checkpoint `5872db1368a5b9a2cdee79a0c2e54aa0b9b00dfa` to the trigger commit contained exactly two paths:

1. `.github/workflows/ca-sco-property-type-semantic-verification-once.yml`;
2. `.github/ca-sco-property-type-semantic-verification-once.trigger.json`.

No runner, execution schema, parser/projector, regex, policy, registry or production configuration changed.

## Fresh approvals consumed

Execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both approvals are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They were consumed when the one-shot workflow invoked the authorized real-source runner. No retry is authorized or available under these refs.

## One-shot workflow run

GitHub Actions run:

`35123686954`

Run attempt:

`1`

Result:

**SUCCESS**

Verified steps:

- authorization/branch/runtime/trigger preflight: PASS;
- execution gate: PASS;
- authorized bounded real-source runner invocation: PASS;
- v1.2 evidence/schema/hard-cap validation: PASS;
- derived-evidence artifact upload: PASS.

Artifact:

- artifact id: `10457344882`;
- artifact name: `ca-sco-property-type-v1-2-real-source-execution-2026-09-16`;
- artifact digest: `sha256:c4146f9bced7722fa5da26a8c1d2ace5a65e610fac7ae190d720bd098e06e6e0`.

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

## Execution result

Machine result:

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

This is an unrelated transport stop, so `control_disposition = null` is the correct v1.2 contract behavior. D-008 `PROPERTY_TYPE_NONCONFORMING_STOPPED` mapping was not reached and was not evaluated against source rows in this run.

## Transport evidence

Expected transport metadata encoded in the reviewed runner:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type: `application/zip`;
- Accept-Ranges: `bytes`.

Observed HEAD metadata during the single authorized execution:

- HTTP status: `200`;
- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

The changed content length and ETag caused the deterministic `TRANSPORT_METADATA_DRIFT` stop.

## Request / data boundary actually used

Actual request summary:

- HEAD requests: `1`;
- Range requests: `0`;
- HTTP requests total: `1`;
- source body bytes read: `0`.

Actual sample summary:

- sample rows examined: `0`;
- rows examined in every canonical member: `0`;
- distinct PROPERTY_TYPE codes: none observed;
- distinct insurance codes: none observed.

Therefore this execution did **not** inspect any source row, did **not** observe any `PROPERTY_TYPE` value, and provides no new evidence about PROPERTY_TYPE semantic compatibility. It establishes only that the currently served archive metadata differs from the runner's pinned transport metadata and that the runner failed closed before body access.

## Privacy / persistence result

PASS.

The persisted evidence contains no raw body, row, `PROPERTY_ID`, owner/holder value, per-row `PROPERTY_TYPE`, offending bytes, hash or exact source-field length.

Safety flags all remained `false`, including:

- full archive downloaded;
- raw body persisted;
- full rows persisted;
- PROPERTY_ID persisted;
- owner/holder values persisted;
- per-row PROPERTY_TYPE persisted;
- identity resolution;
- beneficiary matching;
- outreach;
- production classification activation.

No transient source file was created.

## Workflow lifecycle

The temporary workflow and execution marker are removed immediately in the cleanup/evidence checkpoint following the run. No workflow-based retry path remains in the repository.

## Governance state after execution

- authorized one-shot real-source execution performed: `true`;
- execution count under fresh refs: `1`;
- fresh execution approval consumed: `true`;
- fresh privacy approval consumed: `true`;
- retry authorized: `false`;
- semantic compatibility resolved: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

`DECISIONS.md` is unchanged because the run applies existing D-008/runtime/authorization rules and introduces no new architectural decision.

## Interpretation boundary

`TRANSPORT_METADATA_DRIFT` does not establish whether the source content is valid or invalid, whether the source structure changed, or whether PROPERTY_TYPE semantics changed. The evidence supports only that the live archive's HEAD metadata no longer matches the pinned expected content length and ETag.

No source metadata baseline update, new execution approval, retry, source activation or runtime change is authorized by this result.

## Next single action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

That review may assess the derived execution evidence and determine the next governance proposal. It must not reuse the consumed approvals or perform another real-source request.
