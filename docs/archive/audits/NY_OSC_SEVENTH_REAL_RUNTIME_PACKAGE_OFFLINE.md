# NY OSC Seventh Real Runtime Package — Offline Implementation and Review

Date: 2026-09-21

Classification: `A — Product Critical / Real-Capable Runtime Package`

Status:

`IMPLEMENTED_AND_REVIEWED_OFFLINE / PASS / REAL_CAPABLE_NOT_AUTHORIZED / ZERO SOURCE ACCESS`

## Requested action

`IMPLEMENT_AND_REVIEW_NY_OSC_SEVENTH_REAL_RUNTIME_PACKAGE_OFFLINE`

## Reviewed baseline

Branch:

`ny-osc-seventh-attempt-execution-auth-binding-remediation-offline`

HEAD:

`18c270bd89d7c4e0c37a5bc046a1f09e49dc672e`

CI:

`35653220457 — SUCCESS`

Preceding human review:

`HUMAN_REVIEW_NY_OSC_SEVENTH_ATTEMPT_EXECUTION_AUTH_BINDING_REMEDIATION_OFFLINE = PASS`

## Reuse-first decision

No new external dependency was introduced.

The package reuses:

- Gate 6 protected-package/self-binding pattern;
- existing dedicated OS-temp execution model;
- existing transient logical-deletion behavior;
- reviewed RAW-literal schema discovery;
- existing structural diagnostic v1.0;
- existing versioned JSON-Schema/Pydantic contract pattern.

Gate 6 and historical v1.1/v1.2 contracts remain unchanged.

## Implemented approval and preflight contracts

Created:

- `schemas/common/ny_osc_seventh_attempt_transient_local_approval.schema.json`;
- `schemas/common/ny_osc_seventh_attempt_transient_pii_approval.schema.json`;
- `schemas/common/ny_osc_seventh_fresh_listing_preflight_receipt.schema.json`;
- `schemas/common/ny_osc_seventh_execution_authorization.schema.json`.

These are schemas only. No seventh approval, preflight or execution artifact is created.

The local approval grants retention scope only and no download.

The PII approval grants transient-processing scope only and no download.

The preflight receipt must remain non-PII, perform no download and no owner-file open.

The final execution authorization is the only future artifact allowed to grant:

`ONE_MANUAL_DOWNLOAD_TO_DEDICATED_OS_TEMP`

plus:

`ONE_BOUND_GATE7_EXECUTION`.

## Authorization v1.3

Created:

`schemas/agents/ny_transient_local_execution_authorization_v1_3.schema.json`

Contract:

`1.3.0`

It accepts exactly:

- mode `AUTHORIZED_REAL_ONCE`;
- attempt number 7;
- reviewed proposal checkpoint
  `18c270bd89d7c4e0c37a5bc046a1f09e49dc672e`;
- a verified runner checkpoint;
- four non-empty refs:
  local approval, PII approval, fresh preflight receipt and execution authorization;
- `DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`;
- one manual download;
- zero retries;
- no direct network client.

The authorization cannot represent `SYNTHETIC_TEST`.

## Result v1.4

Created:

`schemas/agents/ny_transient_local_execution_result_v1_4.schema.json`

Contract:

`1.4.0`

It requires:

- execution mode `AUTHORIZED_REAL_ONCE`;
- attempt 7;
- proposal and runner provenance;
- RAW-literal parser provenance;
- quote-dialect diagnostic always null;
- structural diagnostic only for unexpected field count;
- execution-authorization ref;
- execution-authorization single-use consumption provenance;
- no owner PII in consumption provenance;
- no raw path or owner values returned.

Quote-specific reason codes are absent from the v1.4 reason surface.

## Runtime v1.4

Created:

`src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_4.py`

Functions:

- `build_real_execution_authorization_v1_3`;
- `execute_transient_local_file_discovery_v1_4`.

The builder requires all four machine-bound artifacts and verifies:

- attempt 7;
- proposal ref/checkpoint/CI;
- common runner checkpoint and successful runner CI;
- local/PII/execution approvals granted and not consumed;
- exact-match preflight;
- preflight age between 0 and 900 seconds;
- no preflight download, owner-file open or PII processing;
- distinct refs;
- execution authorization bound to the exact preflight receipt;
- unchanged caps/privacy scope;
- exactly one manual download and zero retries.

The executor:

- contains no network client;
- accepts only an already-downloaded local `FINDERS.zip`;
- requires the dedicated OS-temp path;
- calls schema discovery in `AUTHORIZED_TRANSIENT_MEMORY_ONLY` mode;
- binds schema discovery to `DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`;
- fails closed on quote diagnostics or unknown v1.4 reason codes;
- logically deletes the local archive in `finally`;
- does not claim physical secure erasure;
- returns no owner values or raw path.

The module exposes no CLI/main.

## Gate 7

Created:

`scripts/ny_osc_gate7_transient_local.ps1`

Before any temp-directory creation it verifies:

- all four required artifacts exist;
- local/PII/execution approvals are `GRANTED_NOT_CONSUMED`;
- all four bindings target attempt 7;
- proposal ref/checkpoint/CI match;
- runner checkpoint and runner CI match;
- fresh preflight is `EXACT_MATCH`;
- fresh preflight is <=900 seconds old and not future-dated;
- observed listing equals the proposal listing;
- preflight contains no PII and performed no download/open;
- execution authorization binds the exact preflight receipt;
- execution authorization grants exactly one manual download and one Gate 7 execution;
- all four refs are distinct;
- the protected Gate 7 package matches the approved runner checkpoint.

Only after these checks does Gate 7 create the dedicated OS-temp directory.

Gate 7 contains no HTTP/network client. Download remains a separately authorized manual action.

## Synthetic regression coverage

Offline tests use only synthetic ZIP content.

Verified:

- four-artifact builder happy path;
- stale preflight blocked;
- mismatched execution/preflight ref blocked;
- synthetic RAW-14 succeeds through the real-capable runtime;
- RAW-15 remains fail-closed;
- owner values do not appear in result serialization;
- local archive is logically deleted;
- runtime has no CLI or network client;
- authorization v1.3 rejects `SYNTHETIC_TEST`;
- result v1.4 requires execution-auth consumption provenance;
- quote-specific reason codes are rejected;
- historical synthetic v1.2/v1.3 remain unchanged;
- Gate 7 static ordering and no-network requirements.

## CI history

Three intermediate implementation failures were development-harness findings only:

- `35657082992`: two Ruff E501 findings in the new unit test;
- `35657224749`: mypy required the proposal-checkpoint constant to retain Literal typing;
- `35657320542`: connector-side literal `\\n` formatting caused one Ruff failure.

No source access or runtime execution occurred during those failures.

Functional verification checkpoint:

`1d842ec70f24ef9192fc3ef6cfae58121cec87ea`

GitHub CI:

`35657403979 — SUCCESS`

Results:

- Ruff: PASS;
- mypy core: 19 source files PASS;
- mypy NY OSC runtimes: 4 source files PASS;
- contract tests: 421 passed;
- smoke tests: 16 passed;
- full pytest: 604 passed;
- Streamlit safety/startup: PASS;
- frontend lint/typecheck/build: PASS.

## Human review result

`IMPLEMENT_AND_REVIEW_NY_OSC_SEVENTH_REAL_RUNTIME_PACKAGE_OFFLINE = PASS`

Review findings:

- version-additive architecture preserved: PASS;
- synthetic v1.2/v1.3 unchanged: PASS;
- Gate 6 unchanged: PASS;
- four-reference authorization binding: PASS;
- fresh preflight exact/fresh binding: PASS;
- explicit single-download semantics: PASS;
- no-network runtime: PASS;
- no-network Gate 7: PASS;
- protected package self-binding before temp creation: PASS;
- v1.4 non-PII execution-authorization provenance: PASS;
- no seventh real evidence artifacts created: PASS;
- no OSC access/download/real owner-PII processing: PASS.

## Explicitly absent / not authorized

No seventh transient-local approval artifact.
No seventh transient-PII approval artifact.
No seventh preflight receipt artifact.
No seventh execution-authorization artifact.
No OSC access.
No preflight.
No download.
No real owner-file open.
No real owner-PII processing.
No seventh execution.
No source activation.
No identity resolution, beneficiary matching, outreach, contracting, representation or claim activity.
No merge.

## Rollback

Return to:

`18c270bd89d7c4e0c37a5bc046a1f09e49dc672e`

## Next gate

`HUMAN_NY_OSC_SEVENTH_TRANSIENT_LOCAL_FILE_RETENTION_AUTHORIZATION`

Required owner phrase for that gate:

`APPROVO NY OSC SEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE`

That future grant remains retention-scope-only and does not authorize preflight, download or execution.
