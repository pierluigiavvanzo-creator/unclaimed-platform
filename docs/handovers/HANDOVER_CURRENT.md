# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before the semantic-execution line of work: `c3f0dc7e374d21283358e4e1e8d403f078f08acb`
- Execution evidence branch: `m3-ca-sco-property-type-semantic-execution`
- Execution evidence closure SHA: `3ca12f17c0a16ca49205b4d17117f3b41b6efd58`
- Current diagnosis branch: `m3-ca-sco-property-type-offline-diagnosis`
- Offline diagnostic functional SHA: `1405d33b7c09373f738dc87f6c93b05a0c342461`
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` — unchanged
- Never develop directly on `main`.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition/raw persistence/privacy CANONICAL + VERIFIED.
- Streamlit reviewer CANONICAL + CI VERIFIED.
- SCO `$500+` bounded structure inspection CANONICAL + CI VERIFIED.
- SCO two-field privacy boundary CANONICAL + CI VERIFIED.
- SCO `PROPERTY_TYPE` semantic proposal CANONICAL + CI VERIFIED.
- SCO bounded runner design CANONICAL + CI VERIFIED.
- SCO bounded runner implementation CANONICAL + SYNTHETIC/MOCK CI VERIFIED.
- One owner-authorized bounded real `PROPERTY_TYPE` semantic attempt EXECUTED ONCE and STOPPED FAIL-CLOSED.
- Offline evidence review + synthetic diagnosis COMPLETED and CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical Runner

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Promoted functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`

Canonical post-promotion CI:
`34961511401` — SUCCESS.

## Source / Segment Identity

Endpoint:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Canonical transport identity:
- Content-Length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- Accept-Ranges `bytes`.

The archive has four canonical non-encrypted DEFLATED CSV members and the verified 25-column header. `PROPERTY_TYPE` is zero-based index `1`.

## Consumed Human Execution Authorization

Execution approval ref:
`OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`

Transient-row privacy approval ref:
`OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

Authorization commit:
`6ba8d62824f0f0e8eaaa0eefbb8dc1bfdb58898e`

Authorization CI:
`34964924686` — SUCCESS.

Those approvals were consumed by the single real run `34965097988`. They are **not reusable** for a retry or second real execution.

## Real One-Shot Execution

Temporary workflow commit:
`dd5dc80a22307586c341b703de8fe03d6861df29`

Workflow run:
`34965097988`

Semantic result:
`STOPPED_FAIL_CLOSED`

Persisted stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Observed counters:
- HEAD `1`;
- Range GET `1`;
- HTTP requests total `2`;
- source-body bytes `131072`;
- accepted/examined rows `0`;
- retry none;
- cap widening none.

Execution evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Execution audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_EXECUTION.md`

Artifact ID:
`10394467215`

Artifact ZIP digest:
`sha256:24a39a739872b0d9b3f0bff9a17c22f8ab1a443ddbcf82b7f9126d546ed1a66d`

Persisted JSON SHA-256 before repository persistence:
`790dabcf1c04946ad930de467f204cb0af6fe78c25bae86b1ca541e4fc07b96a`

The offending real value/bytes were intentionally not persisted or logged and must not be inferred.

## Network Workflow Steady State

The temporary one-shot workflow was removed immediately after execution at commit:
`bc1b0a955037d35dfa1a37b0c29497c219a04609`.

Current network one-shot workflow:
ABSENT.

Execution evidence steady-state CI:
`34965713695` — SUCCESS.

Do not recreate or run a network workflow without a new explicit human execution + privacy authorization.

## Offline Diagnosis

User authorized:
`procedi con evidence review e diagnosi offline`

Diagnosis branch:
`m3-ca-sco-property-type-offline-diagnosis`

Base:
`3ca12f17c0a16ca49205b4d17117f3b41b6efd58`

Functional diagnostic commit:
`1405d33b7c09373f738dc87f6c93b05a0c342461`

Diagnostic CI:
`34968418681` — SUCCESS for Ruff, mypy, contract, smoke, full pytest including new offline diagnostic tests, frontend lint/typecheck/build and Streamlit safety/startup smoke.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_OFFLINE_DIAGNOSIS.md`

Tests:
`tests/unit/test_ca_sco_property_type_offline_diagnosis.py`

No SCO request/body access occurred during the diagnosis. The runner, regex, execution schema, source policy, registry and network workflow were not changed.

## Root-Cause Finding

The current runner has a diagnostic collision:

1. `_project_property_type()` catches `UnicodeDecodeError` and raises `PROPERTY_TYPE_FORMAT_UNEXPECTED`.
2. `_process_member()` raises the same `PROPERTY_TYPE_FORMAT_UNEXPECTED` when a successfully decoded, non-empty value fails `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Therefore the historical real evidence cannot distinguish:

- UTF-8 encoding failure; from
- decoded-value regex/shape failure.

This corrects the provisional interpretation that the real stop necessarily proved a decoded value reached the regex check. It does not.

If the stop was the decoded shape path, the row had passed the caller's 25-column and non-empty checks. If the stop was the encoding path, those caller checks were not reached. Current evidence cannot select the branch.

## Synthetic Differential Finding

The committed offline regression matrix compares `_project_property_type()` with Python `csv.reader(..., strict=True)` on synthetic 25-column CSV covering:
- ordinary records;
- commas in first field;
- escaped quotes in first field;
- embedded newline in an unrelated field;
- later commas/escaped quotes;
- embedded CRLF in an unrelated field;
- fully quoted CSV.

For all committed cases, the custom projector returns the same index-1 value and 25-column count as the standard library.

A separate synthetic test reproduces the ambiguity: both a decoded shape mismatch and an invalid UTF-8 projected field produce the same historical stop reason.

Supported conclusions only:
- no standard-CSV projection bug was reproduced by the committed matrix;
- the failure taxonomy is ambiguous;
- the real root cause remains unresolved because the source value/bytes were deliberately not retained;
- there is no evidence basis to trim, normalize, lowercase-fold or relax the current regex.

Do not claim:
- that the real value contained whitespace;
- that it was non-UTF-8;
- that SCO violates NAUPA codes;
- that the custom parser is universally bug-free.

## Fixed Safety Caps

Unchanged:
- max 4 members;
- max 4 rows/member;
- max 16 rows total;
- max 1 HEAD;
- max 4 Range GET;
- max 5 HTTP requests;
- max 131072 body bytes/Range;
- max 524288 source-body bytes total;
- max 262144 uncompressed transient bytes/member;
- max 1048576 uncompressed transient bytes total;
- max 32768 bytes/logical record;
- no extra Range;
- no full-body fallback;
- no automatic widening.

## Governance State

SCO source policy remains:
- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `authorized_processing_purposes: []`;
- `allowed_fields: []`;
- `allow_pii: false`.

Registry remains:
- `enabled: false`;
- `approved_for_use: false`.

Approved real sources: `0`.

Semantic compatibility unresolved. Production classification inactive. Identity resolution, beneficiary matching and outreach remain BLOCKED.

## SINGLE NEXT ACTION

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_REVIEW`

Smallest proposed remediation is offline/code-only:

- add a separate future `PROPERTY_TYPE_ENCODING_UNEXPECTED` stop reason for UTF-8 decode failure;
- reserve `PROPERTY_TYPE_FORMAT_UNEXPECTED` for decoded values that fail the unchanged shape rule;
- keep historical evidence unchanged and valid;
- add regression coverage for both paths;
- do not persist/log raw values, bytes, hashes, lengths or fragments;
- keep the one-shot network workflow absent.

This changes the runner machine contract, so do not implement it silently without human approval.

Even after remediation, any second real SCO attempt is a separate later gate requiring fresh explicit semantic-execution approval plus transient-row privacy approval.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
Canonical runner: PRESENT + SYNTHETIC/MOCK CI VERIFIED
Real one-shot run: 34965097988
Real semantic result: STOPPED_FAIL_CLOSED
Historical stop reason: PROPERTY_TYPE_FORMAT_UNEXPECTED
Root cause: UNRESOLVED — ENCODING VS DECODED-SHAPE AMBIGUITY
Execution approval: CONSUMED
Network workflow: ABSENT
Offline diagnosis branch: m3-ca-sco-property-type-offline-diagnosis
Offline diagnostic SHA: 1405d33b7c09373f738dc87f6c93b05a0c342461
Offline diagnostic CI: 34968418681 SUCCESS
Regex relaxation: NOT JUSTIFIED
Source policy: PROPOSED
Registry: DISABLED + NOT APPROVED
Approved real sources: 0
Identity/matching/outreach: BLOCKED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_REVIEW
CONTEXT HEALTH: coherent; repository is source of truth
```