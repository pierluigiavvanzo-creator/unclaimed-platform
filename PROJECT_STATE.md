# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

The versioned `PROPERTY_TYPE` diagnostic remediation has passed human evidence review and has been promoted by fast-forward into the canonical development branch.

No second California SCO request has been authorized or executed. Semantic compatibility remains unresolved and production classification remains inactive.

## Canonical Baseline

Canonical development branch:
`m2-state-governance-core`

Canonical remediation lineage promotion target:
`36954b89e57d056801a10a302de568d853b46e0d`

Canonical promotion CI:
`34980324993` — SUCCESS.

Pre-promotion rollback checkpoint:
`checkpoint-pre-property-type-remediation-promotion` -> `c3f0dc7e374d21283358e4e1e8d403f078f08acb`.

Stable `main` remains:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Completed and Verified

- M3 California source/legal readiness baseline.
- Immutable raw storage/provenance and privacy/data-minimization controls.
- Streamlit reviewer canonical and CI verified.
- California SCO `$500+` bounded structure inspection.
- Two-field first-purpose privacy boundary.
- `PROPERTY_TYPE` semantic proposal and bounded runner.
- One owner-authorized bounded real semantic attempt, executed once and stopped fail-closed.
- Offline evidence review and diagnosis.
- Offline diagnostic remediation with explicit execution-contract versioning.
- Human evidence review of remediation: APPROVED on 2026-09-15.
- Remediation lineage fast-forwarded into canonical development branch.
- Canonical post-promotion CI `34980324993`: SUCCESS.

## Historical Real Bounded Semantic Attempt

Run:
`34965097988`

Result:
`STOPPED_FAIL_CLOSED`

Historical schema:
`1.0.0`

Historical stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Observed counters:
- HEAD requests: `1`;
- Range GET requests: `1`;
- HTTP requests total: `2`;
- source body bytes read: `131072`;
- accepted/examined rows: `0`;
- retry: none;
- cap widening: none.

The historical root cause remains unresolved because the v1.0.0 runner used the same stop reason for UTF-8 decoding failure and decoded-value shape failure. The offending real value/bytes were intentionally not persisted or logged.

The prior execution and transient-row privacy approvals were consumed by run `34965097988` and are not reusable.

## Canonical Diagnostic Remediation

Historical/frozen execution schema:
`schemas/common/property_type_semantic_verification_execution.schema.json` -> `1.0.0`.

Future/remediated execution schema:
`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json` -> `1.1.0`.

Future behavior:
- invalid UTF-8 in projected `PROPERTY_TYPE` -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- successfully decoded, non-empty value failing `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$` -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

The regex is unchanged. No trimming, uppercasing, normalization, code-domain relaxation, raw source-value logging or budget widening was introduced.

Historical v1.0.0 evidence remains unchanged and continues to validate against the frozen v1.0.0 schema.

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
- one-shot network workflow ABSENT;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Test Status

Canonical promotion CI `34980324993`: SUCCESS on promoted SHA `36954b89e57d056801a10a302de568d853b46e0d`.

Candidate functional CI `34971353630`: SUCCESS for `quality` and `streamlit-candidate`.

No SCO network request occurred during remediation or promotion.

## Next Recommended Action

Prepare, on an isolated branch, an evidence-backed proposal for a possible **second bounded `PROPERTY_TYPE` semantic execution** using the canonical v1.1.0 runner.

The proposal must not perform network access. It must preserve current caps and privacy constraints and stop at a fresh human gate. Any second real SCO execution requires new explicit semantic-execution approval and new transient-row privacy approval.
