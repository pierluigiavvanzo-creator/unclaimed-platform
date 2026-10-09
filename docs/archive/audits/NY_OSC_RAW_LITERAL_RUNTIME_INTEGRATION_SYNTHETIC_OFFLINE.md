# NY OSC RAW-Literal Runtime Integration — Synthetic Offline Implementation

Date: 2026-09-21

Classification: `A — Product Critical / Synthetic Runtime Integration`

Status:

`IMPLEMENTED_SYNTHETIC_ONLY / VERIFIED_OFFLINE / ZERO SOURCE ACCESS / NOT REAL-ACTIVATED`

## Requested action

`IMPLEMENT_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_SYNTHETIC_OFFLINE`

## Preconditions

Reviewed baseline branch:

`ny-osc-raw-literal-runtime-integration-review-prerequisite-remediation-offline`

Baseline HEAD:

`713023f80d06f8539038adad6dda370eb7198a10`

Baseline CI:

`35602806376 — SUCCESS`

Human review result immediately preceding implementation:

`HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_REVIEW_PREREQUISITE_REMEDIATION_OFFLINE = PASS`

Active policy:

`D-011 — NY OSC quote interpretation statistical fallback policy`

## Implemented contracts

### Authorization v1.2

Created:

`schemas/agents/ny_transient_local_execution_authorization_v1_2.schema.json`

Contract:

`1.2.0`

The contract accepts exactly:

`mode = SYNTHETIC_TEST`

and exactly:

`quote_dialect_mode = DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`

`AUTHORIZED_REAL_ONCE` is not an allowed wire value.

Existing bounded/privacy controls are preserved:

- explicit archive byte cap;
- explicit uncompressed byte cap;
- explicit archive-member cap;
- immediate logical deletion required;
- durable raw persistence false;
- repository persistence false;
- cloud sync false;
- owner-field logging false;
- row-specific human inspection false.

### Result v1.3

Created:

`schemas/agents/ny_transient_local_execution_result_v1_3.schema.json`

Contract:

`1.3.0`

Required parser provenance:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`

Allowed reason surface excludes:

- `QUOTE_DIALECT_AMBIGUOUS`;
- `MALFORMED_QUOTED_RECORD`.

`quote_dialect_diagnostic` remains a required envelope field and is always `null`.

`UNEXPECTED_DATA_FIELD_COUNT` requires the existing structural diagnostic v1.0.

Local pre-schema archive-cap failures require `schema_result = null`.

All discovery-origin reasons require a matching schema-discovery result.

## Implemented runtime

Created:

`src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_3.py`

Runtime entry function:

`execute_transient_local_file_discovery_v1_3`

Authorization type:

`NyTransientLocalExecutionAuthorizationV1_2`

Result type:

`NyTransientLocalExecutionResultV1_3`

The module deliberately contains:

- no CLI;
- no `main()`;
- no real-authorization builder;
- no Gate 6/7 runner wiring.

It reuses the existing authorized-temp-path check and schema-discovery harness.

The schema-discovery call is bound to:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`

The runtime fails closed if the RAW-literal discovery path emits any quote-dialect diagnostic
or any reason code outside the v1.3 allow-list.

## Synthetic acceptance coverage

Unit tests verify:

1. a sixth-shaped RAW-14 row with an unmatched double quote is discovered under RAW-literal;
2. a same-line quoted pipe producing RAW-15 blocks with `UNEXPECTED_DATA_FIELD_COUNT`;
3. RAW-13 blocks with `UNEXPECTED_DATA_FIELD_COUNT`;
4. local archive cap blocks before schema discovery;
5. the temporary file is logically deleted after bounded execution;
6. serialized output returns no owner values or raw path;
7. `AUTHORIZED_REAL_ONCE` is rejected by the Pydantic authorization model;
8. a non-null quote-dialect diagnostic is rejected;
9. a non-authorized filesystem path is rejected without deletion;
10. the v1.3 module exposes no CLI or real builder.

Contract tests verify:

- authorization v1.2 accepts only `SYNTHETIC_TEST`;
- line-local parser mode is rejected by v1.2;
- result v1.3 requires RAW-literal provenance;
- unexpected width requires structural diagnostic;
- quote-specific reason codes are rejected;
- quote-dialect diagnostics are rejected;
- local cap result cannot carry a schema result;
- historical v1.1/v1.2 contracts and Gate 6 remain line-local;
- CI type-checks the new v1.3 runtime.

## Historical runtime preservation

Unchanged:

- `schemas/agents/ny_transient_local_execution_authorization_v1_1.schema.json`;
- `schemas/agents/ny_transient_local_execution_result_v1_2.schema.json`;
- `src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution.py`;
- `src/unclaimed_platform/adapters/sources/ny_owner_name_transient_local_execution_v1_2.py`;
- `scripts/ny_osc_gate6_transient_local.ps1`.

Gate 6 still requires:

`LINE_LOCAL_ARBITRATION`

The sixth approvals remain consumed/non-reusable.

## CI evolution

Two intermediate CI failures were test-harness issues, not runtime semantic failures:

- `35641588153`: Ruff stopped on one overlong unit-test import line;
- `35641806933`: the historical proposal contract still asserted that future runtime schemas
  must not exist. That assertion was advanced after explicit implementation authorization while
  preserving the proposal's historical `runtime_schema_files_created=false` fact.

Functional implementation checkpoint:

`cbc30509eb8a97859cd5f1752c46dacaa91e5e8c`

GitHub CI:

`35641940057 — SUCCESS`

Results:

- Ruff: PASS;
- mypy core: 19 source files PASS;
- mypy NY OSC runtimes: 3 source files PASS;
- contract tests: 398 passed;
- smoke tests: 16 passed;
- full pytest: 575 passed;
- Streamlit safety/startup: PASS;
- frontend lint/typecheck/build: PASS.

## Source/privacy boundary

No OSC access.
No remote listing preflight.
No download.
No real owner PII.
No real authorization builder.
No Gate 7.
No seventh runner.
No seventh-attempt proposal.
No approval artifacts.
No sixth retry.
No source activation.
No production classification activation.
No identity resolution, beneficiary matching, outreach, contract or claim activity.

## Rollback

Return to baseline:

`713023f80d06f8539038adad6dda370eb7198a10`

The synthetic v1.2/v1.3 contracts and runtime have no real execution dependency.

## Next gate

`HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_SYNTHETIC_OFFLINE`
