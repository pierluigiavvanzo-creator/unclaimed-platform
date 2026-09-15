# M3 California SCO — PROPERTY_TYPE Diagnostic Remediation

Date: 2026-09-15

Status: **OFFLINE REMEDIATION CANDIDATE — NO SCO NETWORK/BODY ACCESS**

## Human authorization

Owner instruction:

`autorizzo remediation diagnostica offline`

This authorization permits only the repository/code/test remediation described by the preceding offline diagnosis. It does not authorize a second SCO request, transient real-row exposure, source approval, registry activation, production classification, identity resolution, matching or outreach.

## Scope

The prior offline diagnosis established that the historical stop code `PROPERTY_TYPE_FORMAT_UNEXPECTED` conflated two distinct branches:

1. UTF-8 decode failure while projecting `PROPERTY_TYPE`;
2. a successfully decoded non-empty value failing the unchanged token-shape regex.

This remediation separates those branches without changing the source-value normalization policy or widening any execution boundary.

## Exact code change

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Before remediation, `_project_property_type()` mapped `UnicodeDecodeError` to:

`PROPERTY_TYPE_FORMAT_UNEXPECTED`

After remediation, the same exception maps to:

`PROPERTY_TYPE_ENCODING_UNEXPECTED`

`PROPERTY_TYPE_FORMAT_UNEXPECTED` remains reserved for a successfully decoded, non-empty value that fails the existing rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The regex itself is unchanged. No `.strip()`, case-folding, normalization or code-domain relaxation is introduced.

## Machine contract versioning

Historical v1.0.0 schema remains frozen at:

`schemas/common/property_type_semantic_verification_execution.schema.json`

It continues to validate the historical real evidence and intentionally does **not** recognize the new encoding-specific reason.

Future remediated runner output uses:

`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

with payload:

`schema_version: 1.1.0`

The v1.1.0 stop-reason enum adds:

`PROPERTY_TYPE_ENCODING_UNEXPECTED`

This explicit minor contract version prevents silent enum-domain drift for consumers pinned to v1.0.0 and follows ADR-0002's versioned-machine-contract principle. No migration of historical evidence is performed or required.

The historical real evidence remains unchanged:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Its persisted schema version remains `1.0.0` and its persisted stop reason remains:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

The remediation must not retroactively reinterpret that historical reason. The historical root cause remains unresolved.

## Regression coverage

Updated synthetic tests verify that:

- future runner output declares `schema_version: 1.1.0`;
- a decoded shape mismatch still yields `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- invalid UTF-8 in the projected field now yields `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- the v1.1.0 schema permits both differentiated reasons;
- the frozen v1.0.0 schema does not permit `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- historical v1.0.0 execution evidence continues to validate against the frozen v1.0.0 schema;
- the existing regex remains strict and unchanged;
- the previously committed standard-CSV projector differential matrix still passes;
- the one-shot network workflow remains absent.

## Privacy boundary

No diagnostic payload is expanded with source content. The runner still does not persist or log:

- raw Range bodies;
- full CSV rows;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE` values;
- offending field bytes;
- offending field fragments;
- field hashes;
- field lengths.

Only the categorical stop reason becomes more precise for a future separately authorized execution.

## Network / execution state

This remediation performs no SCO network request and creates no network workflow.

The prior one-shot authorization remains consumed by run `34965097988` and is not reusable.

The path:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

must remain absent.

## Governance state

Unchanged:

- source policy `PROPOSED`;
- source real-acquisition authorization `false`;
- registry disabled and not approved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Acceptance criteria

The remediation is acceptable only if repository CI confirms:

- Ruff green;
- mypy green;
- contract tests green, including historical v1.0.0 evidence validation;
- smoke tests green;
- full pytest green, including the two differentiated synthetic failure paths and v1.1.0 validation;
- frontend lint/typecheck/build green;
- Streamlit safety/startup smoke green.

## Next gate

After successful candidate CI:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_REVIEW`

Promotion or any later real re-execution remains a separate human decision. A second SCO attempt requires fresh explicit semantic-execution and transient-row privacy authorization.
