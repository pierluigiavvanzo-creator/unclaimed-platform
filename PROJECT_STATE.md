# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

Canonical development branch:
`m2-state-governance-core`

Canonical HEAD before the current semantic-execution candidate:
`c3f0dc7e374d21283358e4e1e8d403f078f08acb`.

The bounded `PROPERTY_TYPE` runner implementation is canonical and synthetic/mock CI verified.

Promoted runner functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`.

Canonical post-promotion CI:
`34961511401` — SUCCESS.

Canonical docs-closure CI:
`34961870512` — SUCCESS.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Current Candidate — Bounded PROPERTY_TYPE Semantic Execution

Branch:
`m3-ca-sco-property-type-semantic-execution`

Owner authorized at `HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`:
- bounded semantic execution;
- bounded transient-row privacy exposure.

Approval refs:
- `OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`;
- `OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`.

Authorization package commit:
`6ba8d62824f0f0e8eaaa0eefbb8dc1bfdb58898e`.

Authorization CI:
`34964924686` — SUCCESS.

## Real Bounded Execution

One-shot workflow commit:
`dd5dc80a22307586c341b703de8fe03d6861df29`.

Execution run:
`34965097988` — SUCCESS at workflow level.

Execution result:
`STOPPED_FAIL_CLOSED`.

Stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Observed counters:
- HEAD requests: `1`;
- Range GET requests: `1`;
- total HTTP requests: `2`;
- source body bytes read: `131072`;
- accepted/examined data rows: `0`;
- distinct accepted `PROPERTY_TYPE` codes: `[]`;
- distinct accepted insurance codes: `[]`.

The runner processed transient bytes far enough to evaluate a candidate `PROPERTY_TYPE` in the first member and stopped before accepting a sample row. The offending value was not persisted or logged and must not be inferred.

No retry occurred. No additional Range was issued. No cap was widened.

## Persisted Evidence

Execution evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_EXECUTION.md`

Artifact:
- ID `10394467215`;
- name `ca-sco-property-type-semantic-execution-2026-09-15`;
- ZIP SHA-256 `24a39a739872b0d9b3f0bff9a17c22f8ab1a443ddbcf82b7f9126d546ed1a66d`;
- JSON SHA-256 before persistence `790dabcf1c04946ad930de467f204cb0af6fe78c25bae86b1ca541e4fc07b96a`.

All persisted safety flags are false. No raw Range body, full row, `PROPERTY_ID`, owner/holder value, or per-row `PROPERTY_TYPE` value is persisted.

## Workflow Steady State

The one-shot network workflow was temporary and was removed immediately after the single execution.

Removal commit:
`bc1b0a955037d35dfa1a37b0c29497c219a04609`.

Current network workflow state:
ABSENT.

Repository CI `34965098018` on the temporary workflow commit failed only because three historical contract tests correctly require the one-shot workflow to be absent in steady state. Those tests were not weakened.

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

The real semantic attempt does not approve the SCO source or activate production use.

Still fail-closed:
- source policy `PROPOSED`;
- real acquisition authorized by source policy `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

The execution approval is treated as consumed by run `34965097988`; it is not reusable for a retry.

## Next Recommended Action

Human evidence-review gate only:

`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`

Review the fail-closed evidence and decide the smallest diagnostic next step. Prefer repository/offline/synthetic diagnosis before any further real network access. A second real execution requires a new explicit human authorization.
