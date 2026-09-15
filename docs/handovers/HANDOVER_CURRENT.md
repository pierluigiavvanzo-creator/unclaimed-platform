# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Canonical development branch: `m2-state-governance-core`
- Canonical development HEAD: `c3f0dc7e374d21283358e4e1e8d403f078f08acb`
- Historical execution evidence branch: `m3-ca-sco-property-type-semantic-execution`
- Historical execution evidence closure SHA: `3ca12f17c0a16ca49205b4d17117f3b41b6efd58`
- Offline diagnosis branch: `m3-ca-sco-property-type-offline-diagnosis`
- Diagnosis closure/base for remediation: `8aa6c61594232b54b351d0a2063d9de2031a28f7`
- Current remediation candidate: `m3-ca-sco-property-type-diagnostic-remediation`
- Current remediation functional SHA: `ec688df61c56276c36facf2f598a1ad90b97fe5d`
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
- One bounded owner-authorized real `PROPERTY_TYPE` semantic attempt EXECUTED ONCE and STOPPED FAIL-CLOSED.
- Offline evidence review + diagnosis COMPLETED + CI VERIFIED.
- Offline diagnostic remediation IMPLEMENTED ON ISOLATED CANDIDATE + CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical Runner Before Remediation Promotion

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Canonical runner functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`

Canonical runner CI:
`34961511401` — SUCCESS.

The remediation candidate is not yet promoted to the canonical development branch.

## Historical Real One-Shot Execution

Workflow run:
`34965097988`

Semantic result:
`STOPPED_FAIL_CLOSED`

Historical persisted stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Exact observed counters:
- HEAD `1`;
- Range GET `1`;
- HTTP requests total `2`;
- source response-body bytes `131072`;
- accepted/examined rows `0`;
- retry none;
- cap widening none.

Execution evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Execution audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_EXECUTION.md`

The offending real source value/bytes were intentionally not persisted or logged and must not be inferred.

The human execution approval and transient-row privacy approval were consumed by run `34965097988`; they are not reusable.

The temporary one-shot workflow was removed after execution and remains ABSENT.

## Offline Diagnosis

Owner instruction:
`procedi con evidence review e diagnosi offline`

Functional diagnostic SHA:
`1405d33b7c09373f738dc87f6c93b05a0c342461`

Diagnostic CI:
`34968418681` — SUCCESS.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_OFFLINE_DIAGNOSIS.md`

The diagnosis established a failure-taxonomy collision in the pre-remediation runner:

1. UTF-8 decoding failure inside `_project_property_type()` emitted `PROPERTY_TYPE_FORMAT_UNEXPECTED`.
2. A successfully decoded, non-empty value failing `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` emitted the same reason.

Therefore the historical real evidence cannot distinguish encoding failure from decoded-value shape failure.

The committed synthetic differential matrix found no standard-CSV projector mismatch against Python `csv.reader(..., strict=True)` for the tested privacy-safe cases. This does not prove the parser universally correct.

No evidence justified trimming, normalization, uppercasing or regex relaxation.

## Offline Diagnostic Remediation

Owner instruction:
`autorizzo remediation diagnostica offline`

Candidate branch:
`m3-ca-sco-property-type-diagnostic-remediation`

Base:
`8aa6c61594232b54b351d0a2063d9de2031a28f7`

Functional remediation commit:
`ec688df61c56276c36facf2f598a1ad90b97fe5d`

Functional remediation CI:
`34969967725` — SUCCESS for both `quality` and `streamlit-candidate`.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION.md`

### Exact behavior now implemented on the candidate

- invalid UTF-8 in the projected `PROPERTY_TYPE` field -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- successfully decoded, non-empty value failing the unchanged token-shape rule -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Unchanged regex:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No `.strip()`, case folding, uppercasing, source-value normalization or code-domain relaxation was introduced.

### Machine contract

Schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

The stop-reason enum was extended with:
`PROPERTY_TYPE_ENCODING_UNEXPECTED`.

`schema_version` remains `1.0.0` because the change is additive/backward-compatible: existing valid payloads remain valid and no field or previously accepted reason is removed or reinterpreted.

The historical persisted execution evidence remains unchanged and continues to validate. Its historical reason remains `PROPERTY_TYPE_FORMAT_UNEXPECTED`; do not retroactively reinterpret it using the new code.

### Regression tests

Updated:
`tests/unit/test_ca_sco_property_type_offline_diagnosis.py`

The suite now verifies:
- decoded shape mismatch still -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- invalid UTF-8 -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- both reasons are present in the schema enum;
- regex behavior is unchanged;
- standard-CSV projector differential cases still pass;
- network one-shot workflow remains absent.

Full repository CI `34969967725` passed Ruff, mypy, contract, smoke, full pytest, frontend lint/typecheck/build and Streamlit safety/startup smoke.

### Functional diff boundary

Compared with remediation base `8aa6c615...`, functional commit `ec688df6...` is ahead by 1, behind by 0, merge-base exactly the base, and changes only:

1. `scripts/ca_sco_property_type_semantic_verification.py`
2. `schemas/common/property_type_semantic_verification_execution.schema.json`
3. `tests/unit/test_ca_sco_property_type_offline_diagnosis.py`
4. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION.md`

## Network / Privacy State During Remediation

No SCO request was made.
No source body was read.
No network workflow was created.
No raw row/value/byte/hash/length diagnostic was persisted or logged.
No prior execution authorization was reused.

One-shot workflow steady state:
ABSENT.

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

Semantic compatibility remains unresolved. Production classification remains inactive. Identity resolution, beneficiary matching and outreach remain BLOCKED.

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

## SINGLE NEXT ACTION

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_REVIEW`

Review the CI-verified candidate. Do not automatically promote it and do not perform another SCO request.

If later explicitly authorized for promotion, first recheck:
- remediation candidate CI still SUCCESS;
- canonical `m2-state-governance-core` has not drifted unexpectedly;
- compare/merge-base is safe;
- changed-file set is bounded and understood.

Then promotion, if authorized, must use a non-force history-preserving update and must be followed by canonical post-promotion CI verification before declaring success.

Any second real SCO execution is a different later gate and requires fresh explicit semantic-execution approval plus transient-row privacy approval.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
Canonical dev: c3f0dc7e374d21283358e4e1e8d403f078f08acb
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e
Historical real run: 34965097988
Historical result: STOPPED_FAIL_CLOSED
Historical stop: PROPERTY_TYPE_FORMAT_UNEXPECTED
Historical root cause: UNRESOLVED
Execution approval: CONSUMED
Network workflow: ABSENT
Diagnosis SHA: 1405d33b7c09373f738dc87f6c93b05a0c342461
Diagnosis CI: 34968418681 SUCCESS
Remediation branch: m3-ca-sco-property-type-diagnostic-remediation
Remediation functional SHA: ec688df61c56276c36facf2f598a1ad90b97fe5d
Remediation CI: 34969967725 SUCCESS
Future encoding failure: PROPERTY_TYPE_ENCODING_UNEXPECTED
Future decoded shape failure: PROPERTY_TYPE_FORMAT_UNEXPECTED
Regex: UNCHANGED
Source policy: PROPOSED
Registry: DISABLED + NOT APPROVED
Approved real sources: 0
Identity/matching/outreach: BLOCKED
NEXT: HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_REVIEW
CONTEXT HEALTH: coherent; repository is source of truth
```
