# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

The canonical `PROPERTY_TYPE` runner is versioned at execution schema v1.1.0.
A second owner-authorized bounded real California SCO semantic execution was
performed exactly once on 2026-09-15 and stopped fail-closed.

Second real run: `34995672539`  
Second persisted schema: `1.1.0`  
Second semantic result: `STOPPED_FAIL_CLOSED`  
Second stop reason: `PROPERTY_TYPE_FORMAT_UNEXPECTED`

Under v1.1.0 this stop reason is distinct from
`PROPERTY_TYPE_ENCODING_UNEXPECTED`. The second run therefore narrows the
observed failure class to a successfully decoded, non-empty projected
`PROPERTY_TYPE` value that failed the unchanged token-shape rule
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The offending value/bytes were not persisted or logged and must not be
inferred. Semantic compatibility remains unresolved and production
classification remains inactive.

## Branches / Baseline

- stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- canonical development branch: `m2-state-governance-core`
- canonical development HEAD before second-execution proposal:
  `e97c1f62959f603bdd3df79538d4b70255594c70`
- second-execution proposal branch:
  `m3-ca-sco-property-type-second-execution-proposal`
- reviewed proposal SHA: `ac6d234dda19b1eb8c8f8ceb0206730bcc419bcb`
- proposal CI: `34993467536` — SUCCESS
- second-execution branch:
  `m3-ca-sco-property-type-second-semantic-execution`
- fresh authorization commit: `acd627f841650541e7dd2441c2c83e20aaf108b5`
- authorization staging CI: `34995492373` — SUCCESS
- temporary execution workflow commit:
  `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`
- workflow-removal commit: `d6e83a44b2069a2fa746c09d1ae33622654e5d43`

## Completed and Verified

- M3 California source/legal readiness baseline.
- Immutable raw storage/provenance and privacy/data-minimization controls.
- Streamlit reviewer canonical and CI verified.
- California SCO `$500+` bounded structure inspection.
- Two-field first-purpose privacy boundary.
- Historical first bounded real semantic attempt executed once and stopped
  fail-closed under schema v1.0.0.
- Offline diagnosis identified the v1.0 failure-taxonomy collision.
- Diagnostic remediation versioned as execution contract v1.1.0 and promoted
  to canonical development.
- Second execution proposal prepared on isolated branch and CI verified.
- Human review of second execution proposal: PASS.
- Fresh second execution and transient-row privacy approvals granted.
- Fresh authorization package staged and CI verified.
- Second bounded real semantic execution performed exactly once.
- Second execution evidence validated against schema v1.1.0 and hard caps.
- Second one-shot workflow removed immediately after execution.
- Workflow logs verified to contain no source row or `PROPERTY_TYPE` values.

## Historical First Real Bounded Semantic Attempt

Run `34965097988`; schema `1.0.0`; result `STOPPED_FAIL_CLOSED`; stop reason
`PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Observed counters:
- HEAD `1`
- Range GET `1`
- HTTP total `2`
- source body bytes `131072`
- accepted/examined rows `0`
- retry none
- cap widening none

Because v1.0.0 used the same stop reason for UTF-8 decoding failure and
decoded-value shape failure, the first run's root cause remains unresolved.
Its evidence remains frozen and is not reinterpreted. Its execution/privacy
approvals were consumed and are not reusable.

## Second Real Bounded Semantic Attempt

Run: `34995672539`  
Execution commit: `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`  
Schema: `1.1.0`  
Result: `STOPPED_FAIL_CLOSED`  
Stop reason: `PROPERTY_TYPE_FORMAT_UNEXPECTED`

Observed counters:
- HEAD `1`
- Range GET `1`
- HTTP total `2`
- source body bytes `131072`
- accepted/examined rows `0`
- retry none
- cap widening none

Transport metadata matched the pinned target metadata before the Range GET.
Safe interpretation: the projected value decoded successfully as UTF-8, was
non-empty, and failed the unchanged token-shape regex. Invalid UTF-8 is not the
stop class for this second run.

Not established: the exact source value; why its shape differs; whether
trimming, normalization or case folding would be correct; whether the regex or
domain should change; or semantic compatibility of the source as a whole.

Fresh second-run approvals are CONSUMED and non-reusable:
- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

No retry is authorized.

Derived artifact:
- artifact ID `10408035386`
- ZIP digest `sha256:c0189177dcca91696e85b3b9fd67c1c896c3af30b13c79b0aa3670998f621732`

Persisted repository evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json`

## Canonical Diagnostic Contract

Historical/frozen schema:
`schemas/common/property_type_semantic_verification_execution.schema.json` -> `1.0.0`

Remediated schema:
`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json` -> `1.1.0`

v1.1 behavior:
- invalid UTF-8 -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`
- decoded non-empty shape failure -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`

No trimming, uppercasing, normalization, code-domain relaxation, source-value
logging or budget widening has been introduced.

## Fixed Safety Boundary

Unchanged: max 4 members; max 4 rows/member; max 16 rows total; max 1 HEAD;
max 4 Range GET; max 5 HTTP requests; max 131072 source-body bytes/Range; max
524288 source-body bytes total; max 262144 uncompressed transient bytes/member;
max 1048576 uncompressed transient bytes total; max 32768 bytes/logical
record; no extra Range; no full-body fallback; no automatic widening.

## Privacy / Workflow State

Second live runner stdout was redirected to `/dev/null`. No raw response body,
full row, `PROPERTY_ID`, owner/holder value, per-row `PROPERTY_TYPE`, offending
bytes, offending-value hash or offending-value length was persisted.

One-shot network workflow steady state: **ABSENT**.

## Governance State

Still fail-closed: source policy `PROPOSED`; source real-acquisition
authorization `false`; registry disabled/unapproved; approved real sources `0`;
semantic compatibility unresolved; production classification inactive;
identity resolution BLOCKED; genealogy BLOCKED; beneficiary matching BLOCKED;
outreach BLOCKED; claim submission BLOCKED.

## Next Recommended Action

Perform `HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`.
Review only the persisted derived v1.1 evidence and audit and decide what
offline diagnostic work, if any, is justified by the narrowed decoded-shape
failure.

Do not perform a third network execution. Any later real execution requires a
new proposal plus fresh explicit execution and transient-row privacy approvals.
