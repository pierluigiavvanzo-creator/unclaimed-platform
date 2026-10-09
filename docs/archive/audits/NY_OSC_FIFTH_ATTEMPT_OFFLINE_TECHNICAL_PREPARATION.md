# NY OSC Fifth Attempt — Offline Runner and Contracts Preparation

Date: 2026-09-20

Classification: `A — Product Critical / Offline Execution Preparation`

## Authorization boundary

The Product Owner authorized only:

`PREPARE_NY_OSC_FIFTH_ATTEMPT_RUNNER_AND_CONTRACTS_OFFLINE`

This work performs no NY OSC access, remote listing preflight, download, archive opening,
real Owner Name File processing, owner-PII processing, approval grant or fifth execution.

## Canonical baseline

Canonical branch:

`mvp1-ny-second-attempt-approved-ready-execution`

Baseline HEAD:

`0efab7f2a7040c75bf6401cd08fd7057dd9eb578`

Reviewed and merged fifth proposal:

`sources/proposals/ny_osc_owner_name_file_fifth_bounded_attempt_authorization.v1.json`

Proposal checkpoint used for exact approval binding:

`8ce856ddbeac5d2300f808729a887803e212b240`

Verified proposal CI:

`35460348569 — SUCCESS`

## Prepared candidate artifacts

- `scripts/ny_osc_gate5_transient_local.ps1`;
- `schemas/common/ny_osc_fifth_attempt_transient_local_approval.schema.json`;
- `schemas/common/ny_osc_fifth_attempt_transient_pii_approval.schema.json`;
- `sources/evidence/ny_osc_owner_name_file_fifth_attempt_transient_local_approval.v1.json`;
- `sources/evidence/ny_osc_owner_name_file_fifth_attempt_transient_pii_approval.v1.json`;
- `tests/contract/test_ny_osc_fifth_attempt_approvals.py`;
- `tests/contract/test_ny_osc_gate5_runner_static.py`.

Both approval templates remain:

`NOT_GRANTED`

Their runner checkpoint and runner CI fields remain null until a later repository commit and
successful CI exist. No approval can become operational without those later bindings.

## Reuse decision

Reused unchanged:

- shared schema-discovery parser;
- shared transient-local execution bridge;
- `build_real_execution_authorization(... expected_attempt_number=5)`;
- execution result contract `v1.1.0`;
- structural diagnostic contract `v1.0.0`.

Not reused:

- fourth-attempt runner;
- fourth-attempt approval artifacts.

The fourth approvals remain consumed and non-reusable.

## Preserved bounds

- attempt number: 5;
- one download maximum;
- zero retries;
- 450,000,000 compressed bytes maximum;
- 2,000,000,000 uncompressed bytes maximum;
- one archive member;
- exactly one text member;
- pipe delimiter;
- 14 documented fields;
- 65,536-byte parser chunk;
- no automatic widening;
- no automatic retry.

## Diagnostic binding

The fifth PII approval contract additionally fixes:

- required transient execution result contract: `1.1.0`;
- required structural diagnostic contract: `1.0.0`;
- structural diagnostic persistence: allowed only as derived non-PII metadata.

If a later authorized execution again returns `UNEXPECTED_DATA_FIELD_COUNT`, the shared v1.1
bridge is expected to emit the sanitized structural diagnostic. This preparation does not
alter parser acceptance behavior.

## Fail-closed ordering

Before the runner creates any temporary directory, it checks both fifth approvals, attempt 5,
the exact proposal ref/checkpoint/CI, exact authorization phrases, reuse/retry policy,
distinct approval refs, runner checkpoint/CI, retention bounds, execution bounds, diagnostic
contract versions and privacy scope.

The prepared templates are `NOT_GRANTED`, so an unmodified candidate runner fails before
temporary-directory creation.

## Network boundary

The PowerShell runner contains no HTTP/network client. A future fresh exact listing preflight
and the single download remain separate explicit human gates.

## State after preparation

`READY_CANDIDATE_OFFLINE / APPROVALS_NOT_GRANTED / ZERO SOURCE ACCESS / ZERO RETRY`

## Next gate

`HUMAN_REVIEW_NY_OSC_FIFTH_ATTEMPT_RUNNER_AND_CONTRACTS_OFFLINE`


## Repository verification

Initial implementation checkpoint:

`17a89dc9a44c4bb8e6403092964b7a12d24d7eaa`

Initial CI:

`35474348294 — FAILED_RUFF_ONLY`

The only findings were four E501 line-length violations in
`tests/contract/test_ny_osc_fifth_attempt_approvals.py`. No runner, schema, privacy or domain
behavior failed.

First corrective checkpoint:

`88aa210111f2f2427d7e62b9b133bb0b9ea7371d`

CI:

`35474384505 — FAILED_RUFF_SYNTAX`

The first formatting correction inserted literal escaped `\\n` sequences into the Python
test file. This was a connector-side patching defect, not a runner or domain defect. No runner,
approval schema/template, privacy rule or execution bound changed.

Functional verification checkpoint:

`64b25f350fc2b7fc80fd3d518bd5c8aabd06a178`

CI:

`35474454565 — SUCCESS`

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety/startup;
- frontend lint;
- frontend typecheck;
- frontend build.

The corrective loop closed after two corrective commits. No third corrective patch was needed.

## Final offline state

`READY_OFFLINE / VERIFIED_CI / APPROVALS_NOT_GRANTED / ZERO SOURCE ACCESS / ZERO RETRY`

Approval templates intentionally retain null runner checkpoint/CI fields while `NOT_GRANTED`.
A later explicit grant step, if authorized, must bind them to a reviewed/integrated runner
checkpoint and successful CI; this preparation does not grant them.

No OSC access, listing preflight, download, real Owner Name File opening, owner-PII processing
or fifth execution occurred.

## Review gate

`HUMAN_REVIEW_NY_OSC_FIFTH_ATTEMPT_RUNNER_AND_CONTRACTS_OFFLINE`
