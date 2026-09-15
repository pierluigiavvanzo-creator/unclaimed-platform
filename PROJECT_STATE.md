# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

Canonical development branch:
`m2-state-governance-core`

Canonical HEAD:
`c3f0dc7e374d21283358e4e1e8d403f078f08acb`.

Canonical bounded `PROPERTY_TYPE` runner functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`.

Canonical runner CI:
`34961511401` — SUCCESS.

Stable `main`:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` — unchanged.

## Historical Real Bounded Semantic Attempt

Execution evidence branch:
`m3-ca-sco-property-type-semantic-execution`

Evidence closure SHA:
`3ca12f17c0a16ca49205b4d17117f3b41b6efd58`.

Owner-authorized one-shot run:
`34965097988`.

Result:
`STOPPED_FAIL_CLOSED`.

Historical persisted stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Observed counters:
- HEAD requests: `1`;
- Range GET requests: `1`;
- HTTP requests total: `2`;
- source body bytes read: `131072`;
- accepted/examined rows: `0`;
- retry: none;
- cap widening: none.

The offending source value/bytes were intentionally not persisted or logged and must not be inferred.

The prior execution and transient-row privacy approvals were consumed by run `34965097988` and are not reusable.

The one-shot network workflow remains ABSENT.

## Offline Diagnosis

Diagnosis branch:
`m3-ca-sco-property-type-offline-diagnosis`

Diagnosis functional SHA:
`1405d33b7c09373f738dc87f6c93b05a0c342461`.

Diagnosis CI:
`34968418681` — SUCCESS.

Diagnosis established that the historical reason `PROPERTY_TYPE_FORMAT_UNEXPECTED` conflated:
1. UTF-8 decode failure while projecting `PROPERTY_TYPE`;
2. decoded non-empty value failing `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

No standard-CSV projector defect was reproduced by the committed synthetic differential matrix. The real historical root cause remains unresolved.

## Current Candidate — Offline Diagnostic Remediation

Branch:
`m3-ca-sco-property-type-diagnostic-remediation`

Base diagnosis HEAD:
`8aa6c61594232b54b351d0a2063d9de2031a28f7`.

Owner authorization:
`autorizzo remediation diagnostica offline`

Functional remediation SHA:
`ec688df61c56276c36facf2f598a1ad90b97fe5d`.

Functional CI:
`34969967725` — SUCCESS for `quality` and `streamlit-candidate`.

Remediation audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION.md`

Exact behavior after remediation:
- invalid UTF-8 in projected `PROPERTY_TYPE` -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded non-empty value failing the unchanged regex -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

The regex remains unchanged. No trimming, case conversion, normalization, source-value logging, raw-byte persistence or budget widening was introduced.

The execution schema stop-reason enum now includes `PROPERTY_TYPE_ENCODING_UNEXPECTED`. This is an additive backward-compatible extension under schema version `1.0.0`; historical execution evidence remains unchanged and contract-valid.

Functional diff from the diagnosis base is exactly four files:
- `scripts/ca_sco_property_type_semantic_verification.py`;
- `schemas/common/property_type_semantic_verification_execution.schema.json`;
- `tests/unit/test_ca_sco_property_type_offline_diagnosis.py`;
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION.md`.

No SCO network/body access occurred during remediation. No network workflow was created.

## Fixed Safety Boundary

Unchanged:
- max 4 members;
- max 4 rows/member;
- max 16 rows total;
- max 1 HEAD;
- max 4 Range GET;
- max 5 HTTP requests;
- max 131072 source-body bytes/Range;
- max 524288 source-body bytes total;
- max 262144 uncompressed transient bytes/member;
- max 1048576 uncompressed transient bytes total;
- max 32768 bytes/logical record;
- no extra Range;
- no full-body fallback;
- no automatic widening.

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

Human evidence/promotion review gate:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_REVIEW`

Review the CI-verified offline remediation. Do not retry SCO access or promote the candidate automatically. Any second real execution requires fresh explicit semantic-execution and transient-row privacy authorization.
