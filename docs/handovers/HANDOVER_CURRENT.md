# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Canonical development branch: `m2-state-governance-core`
- Canonical remediation lineage promotion target: `36954b89e57d056801a10a302de568d853b46e0d`
- Canonical promotion CI: `34980324993` — SUCCESS
- Pre-promotion rollback checkpoint: `checkpoint-pre-property-type-remediation-promotion` -> `c3f0dc7e374d21283358e4e1e8d403f078f08acb`
- Historical execution evidence branch: `m3-ca-sco-property-type-semantic-execution`
- Historical execution evidence closure SHA: `3ca12f17c0a16ca49205b4d17117f3b41b6efd58`
- Offline diagnosis branch: `m3-ca-sco-property-type-offline-diagnosis`
- Historical remediation candidate: `m3-ca-sco-property-type-diagnostic-remediation`
- Never develop directly on `main`.

At every restart, verify the current remote branch heads instead of assuming a documentation SHA is the current HEAD.

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
- Diagnostic remediation v1.1 IMPLEMENTED + CI VERIFIED.
- Human remediation evidence review APPROVED on 2026-09-15.
- Remediation lineage PROMOTED to canonical development by fast-forward.
- Canonical post-promotion CI `34980324993` SUCCESS.
- Historical execution machine contract remains frozen as v1.0.0; future remediated execution contract is v1.1.0.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Historical Real One-Shot Execution

Workflow run:
`34965097988`

Semantic result:
`STOPPED_FAIL_CLOSED`

Historical persisted schema version:
`1.0.0`

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

Functional diagnostic SHA:
`1405d33b7c09373f738dc87f6c93b05a0c342461`

Diagnostic CI:
`34968418681` — SUCCESS.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_OFFLINE_DIAGNOSIS.md`

The diagnosis established a failure-taxonomy collision in the pre-remediation runner:

1. UTF-8 decoding failure inside `_project_property_type()` emitted `PROPERTY_TYPE_FORMAT_UNEXPECTED`.
2. A successfully decoded, non-empty value failing `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` emitted the same reason.

Therefore the historical real evidence cannot distinguish encoding failure from decoded-value shape failure. The historical root cause remains unresolved.

The committed synthetic differential matrix found no standard-CSV projector mismatch against Python `csv.reader(..., strict=True)` for the tested privacy-safe cases. This does not prove the parser universally correct.

No evidence justified trimming, normalization, uppercasing or regex relaxation.

## Canonical Diagnostic Remediation

Remediation audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION.md`

Final functional remediation SHA:
`f7a9bf9ac5614dacc38d7e1d1fdc7f5f03a687ef`

Candidate functional CI:
`34971353630` — SUCCESS for `quality` and `streamlit-candidate`.

Human evidence review decision:
`APPROVE_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION` on 2026-09-15.

Canonical fast-forward promotion target:
`36954b89e57d056801a10a302de568d853b46e0d`

Canonical post-promotion CI:
`34980324993` — SUCCESS.

Exact future behavior now canonical:
- invalid UTF-8 in projected `PROPERTY_TYPE` -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- successfully decoded, non-empty value failing the unchanged token-shape rule -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Unchanged regex:
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No `.strip()`, case folding, uppercasing, source-value normalization or code-domain relaxation was introduced.

### Machine contracts

Historical/frozen v1.0.0 schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

- `$id` remains v1.0.0;
- `schema_version` remains `1.0.0`;
- it does not recognize `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- historical persisted evidence continues to validate against it unchanged.

Future/remediated v1.1.0 schema:
`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

- `$id` is v1.1.0;
- `schema_version` is `1.1.0`;
- it recognizes `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- it preserves `PROPERTY_TYPE_FORMAT_UNEXPECTED` for decoded shape mismatch.

The canonical runner emits `schema_version: 1.1.0` for future executions.

The historical real evidence is NOT migrated or reinterpreted. Its persisted `schema_version: 1.0.0` and `PROPERTY_TYPE_FORMAT_UNEXPECTED` remain historical facts with unresolved root cause.

## Network / Privacy State

No SCO request was made during diagnosis, remediation, evidence review or promotion.
No source body was read during those stages.
No network workflow was recreated.
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

## Context Health / Chat Rotation

The owner explicitly requested proactive warning **before** chat length/context degradation becomes operationally risky.

Do not wait for mistakes or branch confusion. Warn early when the conversation becomes long enough that state reconstruction or instruction retention may degrade. Before recommending a new chat:

1. safely finish or stop the current bounded task;
2. update `PROJECT_STATE.md`, `ROADMAP.md` when applicable, `DECISIONS.md` when applicable, and this handover;
3. record branch/test/network/governance state;
4. provide a compact ready-to-paste restart prompt.

Repository memory remains the source of truth.

## SINGLE NEXT ACTION

Prepare an **isolated, evidence-backed proposal for a possible second bounded `PROPERTY_TYPE` semantic execution** using the canonical v1.1.0 runner.

Constraints for that proposal:

1. create/use a bounded feature/candidate branch from the current canonical development head;
2. do not perform an SCO request;
3. do not recreate the one-shot network workflow during proposal preparation;
4. preserve current byte/request/row caps unless a separate evidence-backed change is explicitly approved;
5. preserve the current privacy boundary and do not persist source rows, per-row values, offending bytes, hashes or lengths;
6. explicitly show that the previous execution and privacy approvals were consumed and cannot be reused;
7. define fresh semantic-execution and transient-row privacy approval requirements;
8. stop at a human review/authorization gate before any second real execution;
9. do not approve the source, activate the registry, enable production classification, identity resolution, matching or outreach as part of this task.

A second real SCO execution is a later, separate gate and requires fresh explicit semantic-execution approval plus fresh transient-row privacy approval.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
Canonical remediation promotion target: 36954b89e57d056801a10a302de568d853b46e0d
Canonical promotion CI: 34980324993 SUCCESS
Pre-promotion rollback checkpoint: checkpoint-pre-property-type-remediation-promotion -> c3f0dc7e374d21283358e4e1e8d403f078f08acb
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e
Historical real run: 34965097988
Historical schema: 1.0.0
Historical result: STOPPED_FAIL_CLOSED
Historical stop: PROPERTY_TYPE_FORMAT_UNEXPECTED
Historical root cause: UNRESOLVED
Historical execution approval: CONSUMED
Historical transient-row privacy approval: CONSUMED
Network workflow: ABSENT
Diagnosis SHA: 1405d33b7c09373f738dc87f6c93b05a0c342461
Diagnosis CI: 34968418681 SUCCESS
Remediation functional SHA: f7a9bf9ac5614dacc38d7e1d1fdc7f5f03a687ef
Remediation candidate CI: 34971353630 SUCCESS
Human remediation review: APPROVED
Future execution schema: 1.1.0
Future encoding failure: PROPERTY_TYPE_ENCODING_UNEXPECTED
Future decoded shape failure: PROPERTY_TYPE_FORMAT_UNEXPECTED
Regex: UNCHANGED
Source policy: PROPOSED
Registry: DISABLED + NOT APPROVED
Approved real sources: 0
Identity/matching/outreach: BLOCKED
NEXT: prepare isolated second bounded PROPERTY_TYPE execution proposal; NO NETWORK; stop at fresh human authorization gate
CONTEXT HEALTH: warn owner proactively before chat length/context degradation becomes risky
```
