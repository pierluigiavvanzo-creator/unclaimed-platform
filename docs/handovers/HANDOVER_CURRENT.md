# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical HEAD before current execution candidate: `c3f0dc7e374d21283358e4e1e8d403f078f08acb`
- Current candidate: `m3-ca-sco-property-type-semantic-execution`
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
- One owner-authorized bounded real `PROPERTY_TYPE` semantic attempt EXECUTED on isolated candidate and STOPPED FAIL-CLOSED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical Runner

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Promoted functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`

Canonical post-promotion CI:
`34961511401` — SUCCESS.

Canonical docs-closure CI:
`34961870512` — SUCCESS.

## Source / Segment Identity

Endpoint:
`https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`

Expected and observed during bounded execution:
- Content-Length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 09 Sep 2026 16:32:34 GMT`.

Canonical archive has four non-encrypted DEFLATED CSV members and a verified 25-column header. `PROPERTY_TYPE` is zero-based column index `1`.

## Human Execution + Privacy Authorization

Owner instruction:
`autorizzo`

The immediately preceding gate explicitly required both bounded semantic execution approval and transient-row privacy approval. The instruction was recorded as approval of both within the already canonical caps.

Execution approval ref:
`OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`

Privacy approval ref:
`OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

Machine authorization:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic_execution_approval.v1.json`

Authorization schema:
`schemas/common/property_type_semantic_execution_authorization.schema.json`

Authorization commit:
`6ba8d62824f0f0e8eaaa0eefbb8dc1bfdb58898e`

Authorization CI:
`34964924686` — SUCCESS.

Authorized only:
- one bounded semantic execution;
- bounded transient-row in-memory exposure;
- temporary one-shot workflow needed for that run.

Not authorized:
- source approval;
- registry activation;
- identity resolution;
- beneficiary matching;
- outreach;
- production classification;
- automatic retry.

## Real One-Shot Execution

Temporary workflow commit:
`dd5dc80a22307586c341b703de8fe03d6861df29`

Workflow run:
`34965097988`

Job ID:
`104367570457`

Workflow job conclusion:
`SUCCESS`.

The job treats schema-valid fail-closed STOP as an accepted execution outcome.

Semantic result:
`STOPPED_FAIL_CLOSED`

Stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Exact observed counters:
- HEAD requests: `1`;
- Range GET requests: `1`;
- total HTTP requests: `2`;
- source response-body bytes read: `131072`;
- accepted/examined rows: `0`;
- rows examined/member: all `0`;
- distinct accepted `PROPERTY_TYPE` codes: `[]`;
- distinct insurance codes: `[]`.

The runner necessarily processed transient first-member row bytes far enough to evaluate a candidate `PROPERTY_TYPE`; it stopped before accepting/counting the row. The offending value was not persisted or logged. Do not infer or reconstruct it.

No retry occurred. No second Range request occurred. No cap widening occurred.

## Execution Evidence

Persisted evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Evidence schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_EXECUTION.md`

Contract test:
`tests/contract/test_ca_sco_property_type_semantic_execution_evidence.py`

Artifact:
- name `ca-sco-property-type-semantic-execution-2026-09-15`;
- ID `10394467215`;
- ZIP size `1283` bytes;
- ZIP digest `sha256:24a39a739872b0d9b3f0bff9a17c22f8ab1a443ddbcf82b7f9126d546ed1a66d`;
- contained JSON size `2730` bytes;
- JSON SHA-256 before persistence `790dabcf1c04946ad930de467f204cb0af6fe78c25bae86b1ca541e4fc07b96a`.

Workflow validation marker:
`BOUNDED_EVIDENCE_VALIDATED`.

All persisted safety flags are false.

## One-Shot Workflow Is Gone

Temporary path:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

The workflow was removed immediately after execution.

Removal commit:
`bc1b0a955037d35dfa1a37b0c29497c219a04609`

Current state:
ABSENT.

Do not recreate it without a new explicit human network-execution authorization.

## Ephemeral Ordinary CI

The workflow-creation push also triggered normal CI run:
`34965098018`.

- Streamlit: SUCCESS.
- Quality: FAILED at contract tests only.

Three existing contracts intentionally asserted that the one-shot workflow must be absent in steady state. They failed only because it existed during the authorized execution window. The tests were not edited. After workflow deletion they are expected to return green.

## Fixed Caps

- 4 members;
- max 4 rows/member;
- max 16 rows total;
- max 1 HEAD;
- max 4 Range GET;
- max 5 HTTP requests;
- max 131072 body bytes/Range;
- max 524288 source body bytes total;
- max 262144 uncompressed transient bytes/member;
- max 1048576 uncompressed transient bytes total;
- max 32768 bytes/logical record;
- no extra Range;
- no full-body fallback;
- no automatic widening.

The actual run consumed only 1 Range and 131072 source bytes.

## Privacy / Persistence

Transient processing for the single run was explicitly approved with:
- memory only;
- retention `0 days`;
- immediate disposal after projection/STOP.

Never persisted/logged:
- raw Range body;
- full CSV row;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE`;
- offending unexpected value.

## Governance State After Run

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

The execution approval has been consumed by run `34965097988` and is not reusable for a retry.

## SINGLE NEXT ACTION

`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`

Review the fail-closed evidence. The smallest recommended next technical step is offline/design-only diagnosis of why the current regex/projection saw `PROPERTY_TYPE_FORMAT_UNEXPECTED`, using code review and synthetic reproduction first.

Do NOT automatically:
- retry SCO network access;
- widen byte/request/row budgets;
- log or persist raw row values;
- approve/enable the source;
- activate production classification;
- start identity, matching or outreach.

Any second real execution requires a fresh explicit human execution authorization and privacy authorization.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 runner: CANONICAL + SYNTHETIC/MOCK CI VERIFIED
Canonical dev before execution candidate: c3f0dc7e374d21283358e4e1e8d403f078f08acb
Execution candidate: m3-ca-sco-property-type-semantic-execution
Execution approval commit: 6ba8d62824f0f0e8eaaa0eefbb8dc1bfdb58898e
Authorization CI: 34964924686 SUCCESS
One-shot commit: dd5dc80a22307586c341b703de8fe03d6861df29
One-shot run: 34965097988 SUCCESS
Semantic result: STOPPED_FAIL_CLOSED
Stop reason: PROPERTY_TYPE_FORMAT_UNEXPECTED
HTTP requests: 2 (1 HEAD + 1 Range)
Source body bytes: 131072
Accepted/examined rows: 0
Retry: NONE
Workflow removal commit: bc1b0a955037d35dfa1a37b0c29497c219a04609
Network workflow steady state: ABSENT
Source policy: PROPOSED
Registry: DISABLED + NOT APPROVED
Approved real sources: 0
Identity/matching/outreach: BLOCKED
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_EVIDENCE_REVIEW
CONTEXT HEALTH: coherent; repository is source of truth
```
