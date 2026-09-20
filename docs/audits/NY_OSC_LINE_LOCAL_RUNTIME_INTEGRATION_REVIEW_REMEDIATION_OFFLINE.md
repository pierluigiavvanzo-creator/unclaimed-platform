# NY OSC Line-Local Runtime Integration — Review Remediation

Date: 2026-09-20

Classification: `A — Product Critical / Review Remediation`

## Requested action

`REMEDIATE_NY_OSC_LINE_LOCAL_RUNTIME_INTEGRATION_REVIEW_FINDINGS_OFFLINE`

## Reviewed checkpoint

`75ff9b87cd1d20258b98d97cae00f3130988fd34`

## Finding 1 — canonical JSON Schema parity

The v1.2 runtime model was stricter than the canonical JSON Schema for ordinary
blocked reason/status bindings.

This remediation makes the v1.2 reason set explicit in both the Pydantic model
and JSON Schema, and binds every supported reason to its allowed status,
schema-result presence and diagnostic shape.

Local bridge reasons require BLOCKED and schema_result=null.

Discovery-origin reasons require a non-null schema result with exactly matching
status and reason code.

`DOCUMENTED_14_FIELD_LAYOUT_CONFIRMED` is the only DISCOVERED reason.

`UNEXPECTED_DATA_FIELD_COUNT` requires only the structural diagnostic.

`QUOTE_DIALECT_AMBIGUOUS` requires only the quote-dialect diagnostic.

All other reasons require both diagnostics to be null.

Unknown future v1.2 reasons fail closed and require explicit contract evolution.

Negative contract tests cover ordinary blocked reason mismatch, discovered
reason mismatch and local-cap reason carrying a schema result.

## Finding 2 — targeted mypy coverage

The repository CI previously did not type-check adapters/sources.

A separate named CI step now type-checks exactly:

- ny_owner_name_transient_local_execution.py
- ny_owner_name_transient_local_execution_v1_2.py

A contract test asserts this targeted CI coverage remains present.

## Preserved boundaries

No parser algorithm change.
No Gate 5 change.
No consumed approval change.
No source access.
No download.
No PII processing.
No retry.
No sixth-attempt preparation.
No runtime operational activation.

## State at commit

`REMEDIATION_IMPLEMENTED / NOT_RUNTIME_ACTIVATED / CI_PENDING`

## First remediation CI feedback

Run `35524403552` reached the newly added targeted mypy step and failed there
before pytest/frontend stages.

The targeted check exposed four static-typing issues in the runtime file:

- two Literal assignment issues for the shared FINDERS.zip constant;
- two loop-variable type conflicts caused by reusing the same `expected` name
  across string and heterogeneous/bool validation dictionaries.

The follow-up correction:

- types `EXPECTED_LOCAL_NAME` as `Literal["FINDERS.zip"]`;
- uses distinct loop variables for binding, local-scope and processing-scope
  validation.

No runtime behavior, parser algorithm, approval semantics or operational scope
is changed by this static-typing correction.

## State after targeted mypy correction

`REMEDIATION_IMPLEMENTED / MYPY_FIX_COMMITTED / CI_RETRY_PENDING`

