# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory. Verify current remote branch heads at every restart.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- Canonical development branch: `m2-state-governance-core`
- Canonical dev HEAD before second proposal: `e97c1f62959f603bdd3df79538d4b70255594c70`
- Second-execution proposal branch: `m3-ca-sco-property-type-second-execution-proposal`
- Reviewed proposal SHA: `ac6d234dda19b1eb8c8f8ceb0206730bcc419bcb`
- Proposal CI: `34993467536` — SUCCESS
- Second-execution branch: `m3-ca-sco-property-type-second-semantic-execution`
- Fresh authorization commit: `acd627f841650541e7dd2441c2c83e20aaf108b5`
- Authorization staging CI: `34995492373` — SUCCESS
- Temporary execution workflow commit: `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`
- Workflow-removal commit: `d6e83a44b2069a2fa746c09d1ae33622654e5d43`
- Never develop directly on `main`.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness complete.
- M3 acquisition/raw persistence/privacy canonical and verified.
- Streamlit reviewer canonical and verified.
- SCO `$500+` bounded structure inspection canonicalized.
- Canonical `PROPERTY_TYPE` runner uses future execution schema v1.1.0.
- Historical v1.0 evidence remains frozen.
- v1.1 distinguishes encoding failure from decoded shape failure.
- Second bounded execution proposal passed human review.
- Fresh second execution/privacy approvals were granted and then consumed.
- Second bounded real execution was performed exactly once.
- Second one-shot workflow was removed immediately after execution.
- Repository-side Vercel integration remains decommissioned.
- Supabase remains untouched.

## Historical First Real One-Shot Execution

Run `34965097988`; schema `1.0.0`; result `STOPPED_FAIL_CLOSED`; stop reason
`PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Exact counters: HEAD `1`; Range GET `1`; HTTP total `2`; source body bytes
`131072`; accepted/examined rows `0`; no retry; no widening.

Because v1.0 conflated invalid UTF-8 and decoded shape mismatch, the historical
root cause remains unresolved. Historical execution/privacy approvals are
CONSUMED and non-reusable.

Historical evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

## Canonical v1.1 Diagnostic Remediation

Historical/frozen schema:
`schemas/common/property_type_semantic_verification_execution.schema.json` -> `1.0.0`

Remediated schema:
`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json` -> `1.1.0`

Exact v1.1 distinction:
- invalid UTF-8 projected `PROPERTY_TYPE` -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`
- successfully decoded, non-empty value failing `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`

No trimming, case folding, uppercasing, normalization, code-domain relaxation or raw value logging is canonical.

## Second Bounded Real Semantic Execution

Human approvals granted:
- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both are now **CONSUMED** by the single execution below and cannot be reused.

Authorization evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_second_semantic_execution_approval.v1.json`

Authorization audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_AUTHORIZATION.md`

One-shot GitHub Actions run: `34995672539`  
Execution commit: `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`  
Workflow result: SUCCESS  
Semantic result: `STOPPED_FAIL_CLOSED`  
Execution schema: `1.1.0`  
Stop reason: `PROPERTY_TYPE_FORMAT_UNEXPECTED`

Workflow SUCCESS means the bounded runner, validation and evidence upload completed. It does **not** mean semantic compatibility passed.

Exact observed counters:
- HEAD `1`
- Range GET `1`
- HTTP total `2`
- source body bytes `131072`
- sample rows accepted/examined `0`
- no retry
- no cap widening

Transport metadata matched the fixed expected target metadata before the Range GET.

### Safe interpretation

Because this run used v1.1.0, its stop reason means the projected `PROPERTY_TYPE` decoded successfully, was non-empty, and failed the unchanged token-shape regex. This rules out `PROPERTY_TYPE_ENCODING_UNEXPECTED` as the stop class for this run.

It does **not** reveal the offending value, prove why the shape differs, or justify trimming, normalization, uppercasing or regex relaxation. Do not infer the offending source value.

`sample_rows_examined: 0` is the persisted accepted/examined counter. Do not interpret it as proof that no transient record bytes were parsed before the fail-closed stop.

### Derived artifact

- artifact ID: `10408035386`
- artifact name: `ca-sco-property-type-second-semantic-execution-2026-09-15`
- artifact ZIP digest: `sha256:c0189177dcca91696e85b3b9fd67c1c896c3af30b13c79b0aa3670998f621732`

Persisted repository evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json`

Execution audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION.md`

## Privacy / Logs

During the live execution, runner stdout was redirected to `/dev/null`. Workflow logs contain no source rows and no `PROPERTY_TYPE` values.

No raw body, full row, `PROPERTY_ID`, owner/holder value, per-row `PROPERTY_TYPE`, offending bytes, offending-value hash or offending-value length was persisted. All execution safety flags are false.

## Workflow Lifecycle

Temporary workflow path:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

It was created only for the authorized single execution and then removed.

Workflow-removal commit:
`d6e83a44b2069a2fa746c09d1ae33622654e5d43`

Steady-state workflow: **ABSENT**. No retry was performed or authorized.

## Fixed Safety Caps

Unchanged: max 4 members; max 4 rows/member; max 16 rows total; max 1 HEAD; max 4 Range GET; max 5 HTTP requests; max 131072 body bytes/Range; max 524288 source-body bytes total; max 262144 uncompressed transient bytes/member; max 1048576 uncompressed transient bytes total; max 32768 bytes/logical record; no extra Range; no full-body fallback; no automatic widening.

## Governance State

SCO source policy remains `PROPOSED`; `real_acquisition_authorized: false`; `authorized_processing_purposes: []`; `allowed_fields: []`; `allow_pii: false`.

Registry remains disabled/unapproved. Approved real sources remain `0`. Semantic compatibility remains unresolved. Production classification remains inactive. Identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Product Alignment Note

The target product remains a proactive unclaimed-life-insurance scouting and beneficiary-matching platform. Current M3 work is primarily the **benefit-first** entry path. The architecture already contains death evidence, identity resolution, genealogy and candidate-generation modules needed for downstream matching. A complementary **death-first** entry path should be made explicit in a later product/architecture task, not folded into this semantic-evidence gate.

## Context Health / Chat Rotation

The owner explicitly requested proactive warning before chat/context degradation becomes operationally risky. This conversation has reached the point where a fresh chat is recommended after the current evidence-closure task is CI-verified. Repository memory is the source of truth.

## SINGLE NEXT ACTION

Perform:

`HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`

Scope:
1. review the persisted second-run v1.1 evidence and execution audit;
2. confirm exact counters, privacy boundary and workflow removal;
3. confirm the narrowed interpretation is only a decoded non-empty shape mismatch under the unchanged regex;
4. decide what **offline** diagnostic action, if any, is justified;
5. do not make another SCO request;
6. do not reuse either consumed second-run approval;
7. do not approve the source, activate the registry, enable production classification, identity resolution, genealogy, beneficiary matching, outreach or claim submission;
8. stop at the next explicit human gate before any new network execution.

Any third real execution requires a new proposal plus fresh explicit semantic execution and transient-row privacy approvals.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e
canonical dev before second proposal: e97c1f62959f603bdd3df79538d4b70255594c70
proposal SHA: ac6d234dda19b1eb8c8f8ceb0206730bcc419bcb
proposal CI: 34993467536 SUCCESS
execution branch: m3-ca-sco-property-type-second-semantic-execution
authorization SHA: acd627f841650541e7dd2441c2c83e20aaf108b5
authorization CI: 34995492373 SUCCESS
second execution SHA: e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc
second real run: 34995672539
second schema: 1.1.0
second result: STOPPED_FAIL_CLOSED
second stop: PROPERTY_TYPE_FORMAT_UNEXPECTED
second interpretation: DECODED NON-EMPTY SHAPE MISMATCH
second counters: HEAD=1 RANGE=1 HTTP=2 BODY=131072 ROWS=0
second execution approval: CONSUMED
second transient-row privacy approval: CONSUMED
workflow removal SHA: d6e83a44b2069a2fa746c09d1ae33622654e5d43
network workflow steady state: ABSENT
source policy: PROPOSED
registry: DISABLED + NOT APPROVED
approved real sources: 0
production classification: INACTIVE
identity/genealogy/matching/outreach: BLOCKED
NEXT: HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_EVIDENCE_REVIEW
NO THIRD NETWORK EXECUTION WITHOUT NEW PROPOSAL + FRESH APPROVALS
CONTEXT HEALTH: start a fresh chat after this closure is CI-verified
```
