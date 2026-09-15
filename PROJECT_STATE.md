# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

Canonical development branch:
`m2-state-governance-core`

Canonical HEAD before the semantic-execution candidate:
`c3f0dc7e374d21283358e4e1e8d403f078f08acb`.

Canonical bounded `PROPERTY_TYPE` runner functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`.

Canonical runner post-promotion CI:
`34961511401` — SUCCESS.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Real Bounded Semantic Attempt

Execution candidate branch:
`m3-ca-sco-property-type-semantic-execution`

Evidence-closure HEAD:
`3ca12f17c0a16ca49205b4d17117f3b41b6efd58`.

Owner-authorized one-shot run:
`34965097988`.

Result:
`STOPPED_FAIL_CLOSED`.

Persisted stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Observed counters:
- HEAD requests: `1`;
- Range GET requests: `1`;
- HTTP requests total: `2`;
- source body bytes read: `131072`;
- accepted/examined rows: `0`;
- retry: none;
- cap widening: none.

The offending source value was intentionally not persisted or logged and must not be inferred.

Execution evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Execution audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_EXECUTION.md`

Execution steady-state CI:
`34965713695` — SUCCESS.

The one-shot workflow was removed at:
`bc1b0a955037d35dfa1a37b0c29497c219a04609`.

Current network workflow state:
ABSENT.

The prior execution authorization is consumed by run `34965097988` and is not reusable for a retry.

## Current Candidate — Offline Diagnosis

Branch:
`m3-ca-sco-property-type-offline-diagnosis`

Base:
`3ca12f17c0a16ca49205b4d17117f3b41b6efd58`.

Diagnostic implementation/audit SHA:
`1405d33b7c09373f738dc87f6c93b05a0c342461`.

Diagnostic CI:
`34968418681` — SUCCESS for `quality` and `streamlit-candidate`.

Files added:
- `tests/unit/test_ca_sco_property_type_offline_diagnosis.py`;
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_OFFLINE_DIAGNOSIS.md`.

No SCO network/body access occurred during this diagnosis. No runner, regex, execution schema, source policy, registry or network workflow was changed.

## Offline Diagnosis Findings

The existing runner uses the same stop code, `PROPERTY_TYPE_FORMAT_UNEXPECTED`, for two different branches:

1. UTF-8 decoding failure inside `_project_property_type()`;
2. successfully decoded, non-empty `PROPERTY_TYPE` that later fails the regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Therefore the historical real-run evidence cannot distinguish **encoding failure** from **decoded-value shape failure**.

This corrects the earlier provisional interpretation that the stop necessarily proved a decoded value reached the regex check. It does not.

The committed offline regression matrix compares the custom projector with Python `csv.reader(..., strict=True)` on synthetic 25-column records covering commas, escaped quotes, embedded LF/CRLF and fully quoted CSV. The projector matches the standard-library parser for all committed cases and reports 25 columns.

A separate synthetic test reproduces the diagnostic collision: both a decoded shape mismatch and an invalid UTF-8 projected field result in `PROPERTY_TYPE_FORMAT_UNEXPECTED` under the current runner.

Supported conclusion:
- no standard-CSV projector defect was reproduced by the committed matrix;
- the failure taxonomy is diagnostically ambiguous;
- the real root cause remains unresolved because raw/offending bytes were intentionally not retained;
- there is no evidence basis to relax, trim or normalize the regex.

## Fixed Safety Boundary

Unchanged hard caps:
- 4 canonical CSV members;
- 4 rows/member maximum;
- 16 rows total maximum;
- 1 HEAD maximum;
- 4 Range GET maximum;
- 5 HTTP requests maximum total;
- 131,072 source-body bytes/Range maximum;
- 524,288 source-body bytes total maximum;
- 262,144 uncompressed transient bytes/member maximum;
- 1,048,576 uncompressed transient bytes total maximum;
- 32,768 bytes/logical CSV record maximum;
- no extra Range;
- no full-body fallback;
- no automatic cap widening.

## Governance State

Still fail-closed:
- source policy `PROPOSED`;
- source real-acquisition authorization `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED;
- one-shot network workflow ABSENT.

## Next Recommended Action

Human review gate:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_REVIEW`

Smallest proposed remediation, still offline only:
- add a distinct future stop reason such as `PROPERTY_TYPE_ENCODING_UNEXPECTED` for UTF-8 decode failures;
- retain `PROPERTY_TYPE_FORMAT_UNEXPECTED` for decoded values that fail the existing regex;
- preserve historical execution evidence unchanged and schema-valid;
- add regression coverage for both branches;
- do not add raw values, bytes, hashes, lengths or value fragments to logs/evidence;
- keep the network workflow absent.

A second real SCO execution remains a separate later gate requiring fresh explicit execution and transient-row privacy authorization.