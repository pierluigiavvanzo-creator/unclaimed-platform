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

## Machine contract

Schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

The stop-reason enum is extended with:

`PROPERTY_TYPE_ENCODING_UNEXPECTED`

The payload shape and all other fields are unchanged. `schema_version` remains `1.0.0` because this is an additive, backward-compatible reason-code extension: previously valid execution evidence remains valid and no existing field or accepted value is removed or reinterpreted.

The historical real evidence remains unchanged:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Its persisted stop reason remains:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

The remediation must not retroactively reinterpret that historical reason. The historical root cause remains unresolved.

## Regression coverage

Updated synthetic tests verify that:

- a decoded shape mismatch still yields `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- invalid UTF-8 in the projected field now yields `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- both reason codes are permitted by the execution schema;
- the existing regex remains strict and unchanged;
- the previously committed standard-CSV projector differential matrix still passes;
- the one-shot network workflow remains absent.

Existing contract coverage continues to validate the historical real evidence against the extended schema, proving backward compatibility for that artifact.

## Privacy boundary

No diagnostic payload is expanded. The runner still does not persist or log:

- raw Range bodies;
- full CSV rows;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE` values;
- offending field bytes;
- offending field fragments;
- field hashes;
- field lengths.

Only the categorical stop reason changes for a future execution.

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
- contract tests green;
- smoke tests green;
- full pytest green, including the two differentiated synthetic failure paths;
- frontend lint/typecheck/build green;
- Streamlit safety/startup smoke green.

## Next gate

After successful candidate CI:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_REVIEW`

Promotion or any later real re-execution remains a separate human decision. A second SCO attempt requires fresh explicit semantic-execution and transient-row privacy authorization.
