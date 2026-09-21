# NY OSC RAW-Literal Runtime Integration Proposal — Offline Remediation

Date: 2026-09-21

Classification: `A — Product Critical / Proposal Remediation`

Status:

`REMEDIATED_PROPOSED_NOT_IMPLEMENTED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

## Requested action

`REMEDIATE_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_OFFLINE_PROPOSAL`

## Reviewed baseline

Proposal branch:

`ny-osc-raw-literal-runtime-integration-offline-proposal`

Reviewed HEAD:

`056a10cd810d88b362082ff3a28e0d0bdc5f554f`

Reviewed CI:

`35597978522 — SUCCESS`

Human review result:

`CHANGES_REQUIRED_BEFORE_IMPLEMENTATION`

## Finding 1 — authorization mode wire value ambiguity

The reviewed proposal used:

`mode = "SYNTHETIC_TEST_ONLY"`

in the machine-readable proposal and schema while the audit and canonical state described the
future authorization contract as accepting:

`SYNTHETIC_TEST` only.

The historical NY runtime already uses `SYNTHETIC_TEST` as the established wire value.

### Remediation

The future authorization v1.2 proposal now uses exactly:

`mode = "SYNTHETIC_TEST"`

Synthetic-only behavior is enforced by the future contract allow-list:

`allowed_mode_values = ["SYNTHETIC_TEST"]`

and the explicit exclusion:

`forbidden_mode_values = ["AUTHORIZED_REAL_ONCE"]`.

No new protocol value is introduced.

## Finding 2 — proposal schema drift hardening

The reviewed schema allowed silent extension in two areas and did not bind the future real
activation gate list exactly.

### Remediation

The proposal schema now:

- sets `additionalProperties: false` for `implementation_boundaries`;
- binds the complete synthetic acceptance matrix exactly;
- binds the complete seven-item future activation prerequisite list exactly;
- rejects unknown synthetic-matrix fields;
- rejects unknown implementation-boundary flags;
- rejects changed future gate names;
- records these closure requirements in the proposal itself.

The schema/payload contract is versioned:

`1.1.0`.

## Preserved architecture

Historical runtime remains untouched:

- authorization v1.1 -> `LINE_LOCAL_ARBITRATION`;
- result v1.2 -> `LINE_LOCAL_ARBITRATION`;
- `execute_transient_local_file_discovery_v1_2`;
- Gate 6.

The future candidate remains version-additive:

- authorization v1.2 -> `SYNTHETIC_TEST` only;
- parser mode -> `DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`;
- result v1.3;
- future runtime function -> `execute_transient_local_file_discovery_v1_3`;
- no real authorization builder;
- no CLI change;
- no runner wiring.

## Reason/diagnostic policy preserved

RAW-literal future runtime continues to forbid:

- `QUOTE_DIALECT_AMBIGUOUS`;
- `MALFORMED_QUOTED_RECORD`.

`UNEXPECTED_DATA_FIELD_COUNT` continues to require the structural diagnostic.

`quote_dialect_diagnostic` remains required-null for the future v1.3 result envelope.

## Source/privacy boundary

No runtime code changed.
No runtime schema under `schemas/agents/` was created.
No Gate 6 change.
No Gate 7/seventh runner.
No approval artifacts.
No OSC access.
No listing preflight.
No download.
No real owner-PII processing.
No sixth retry.
No seventh-attempt preparation or execution.

## Review prerequisite remediation status

The proposal/schema hardening in this audit remains valid. A later human review found one
governance defect in the exact future prerequisite list: it referenced a superseded review that
had returned `CHANGES_REQUIRED_BEFORE_IMPLEMENTATION`.

That prerequisite-only defect is superseded by:

`docs/audits/NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_REVIEW_PREREQUISITE_REMEDIATION_OFFLINE.md`

No runtime finding from this audit is reversed.

## Next gate

`HUMAN_REVIEW_NY_OSC_RAW_LITERAL_RUNTIME_INTEGRATION_PROPOSAL_REMEDIATION_OFFLINE`


## Verification

Functional verification checkpoint:

`474c79009e4cd624988baa26dd4d580c2b44cd9f`

GitHub CI:

`35600737160 — SUCCESS`

Results:

- Ruff: PASS;
- mypy core: 19 source files PASS;
- mypy NY OSC runtime: 2 source files PASS;
- contract tests: 389 passed;
- smoke tests: 16 passed;
- full pytest: 558 passed;
- Streamlit safety/startup: PASS;
- frontend lint/typecheck/build: PASS.

The verification confirms that no runtime schema under `schemas/agents/`, no runtime v1.3
implementation, no Gate 7, no approval artifact and no real execution path were created.
