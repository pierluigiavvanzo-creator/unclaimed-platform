# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy gates, SCO governance/transport evidence, the `$500+` bounded structure inspection, the two-field privacy boundary, the `PROPERTY_TYPE` semantic-verification proposal, and the bounded `PROPERTY_TYPE` runner design are canonical on `m2-state-governance-core`.

Canonical development HEAD before the current implementation candidate:
`6105c22a7d31df7afca00282eff7e9798e98b868`.

Runner-design canonical CI:
`34947637509` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Current Candidate — PROPERTY_TYPE Runner Implementation

Branch:
`m3-ca-sco-property-type-runner-implementation`

Functional candidate HEAD before audit/docs closure:
`d2b8977a0fd34474ecb545c6ecfefc354b551b30`.

Functional CI:
`34951460475` — SUCCESS for both `quality` and `streamlit-candidate`.

Compare against canonical at functional closure:
- ahead `3`;
- behind `0`;
- merge-base exactly `6105c22a7d31df7afca00282eff7e9798e98b868`.

No source policy or registry change occurred.

## Owner Implementation Gate

Owner explicitly approved:
`approvo implementazione bounded runner PROPERTY_TYPE con soli test synthetic/mock`

Machine approval reference:
`OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_SYNTHETIC_MOCK_ONLY`.

Authorized:
- bounded runner implementation;
- synthetic/mock testing.

Not authorized:
- real network execution;
- network workflow;
- real row access;
- transient-row privacy exposure;
- source approval;
- registry activation.

Authorization evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_runner_implementation_approval.v1.json`.

Authorization schema:
`schemas/common/property_type_semantic_runner_implementation_authorization.schema.json`.

## Implemented Runner

Runner path:
`scripts/ca_sco_property_type_semantic_verification.py`

Candidate state:
PRESENT + SYNTHETIC/MOCK TESTED.

Network one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

Candidate state:
ABSENT.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_IMPLEMENTATION.md`.

The runner uses an injected transport for synthetic/mock testing. A fixed real HTTP transport implementation exists for a later separately authorized gate, but it was not invoked during this task and is not wired into GitHub Actions.

## Fixed Safety Boundary

Hard caps remain canonical and unchanged:
- 4 canonical CSV members;
- maximum 4 complete data rows/member;
- maximum 16 rows total;
- maximum 1 HEAD;
- maximum 4 Range GET;
- maximum 5 HTTP requests total;
- maximum 131,072 source-body bytes/Range;
- maximum 524,288 source-body bytes total;
- maximum 262,144 uncompressed transient bytes/member;
- maximum 1,048,576 uncompressed transient bytes total;
- maximum 32,768 bytes/logical CSV record;
- no extra Range;
- no full-body fallback;
- no automatic cap widening.

If Range is ignored/non-206, the runner stops before reading the unexpected body.

## Parsing / Persistence Boundary

Before accepting sampled data rows, the runner verifies the exact canonical 25-column header.

For each bounded data record it projects only zero-based column `1`, `PROPERTY_TYPE`, while counting columns. `PROPERTY_ID` is not used for semantic verification.

Never persist/log as execution evidence:
- raw Range bodies;
- full rows;
- `PROPERTY_ID` values;
- owner/holder values;
- per-row `PROPERTY_TYPE` values.

Allowed execution evidence remains derived summary only: aggregate row counts, rows/member, distinct `PROPERTY_TYPE` codes, distinct official insurance codes, request/byte counters, semantic status, and stop reason.

## Synthetic / Mock Verification

Synthetic tests cover:
- successful bounded sample with official insurance codes;
- no-insurance sample -> inconclusive;
- unknown `IN` code -> fail closed;
- ignored Range/non-206 -> STOP with zero unexpected-body reads;
- exact-header mismatch;
- row column-count mismatch;
- missing privacy approval before transport;
- missing execution approval before transport;
- explicit live-CLI opt-in;
- absence of the network one-shot workflow.

Final functional CI `34951460475` passed Ruff, mypy, contract tests, smoke tests, full pytest including the new unit tests, frontend lint/typecheck/build, and Streamlit safety/startup smoke.

Intermediate failed CI is retained in history:
- `34950942449`: Ruff import rule only;
- `34951326633`: historical proposal contract still asserted permanent runner absence.

Both were corrected narrowly without force-push or history rewrite.

## Network / Real Data State

During the entire implementation task:
- new SCO network requests: `0`;
- source response-body bytes read: `0`;
- real CSV rows read: `0`;
- real PII processed: `0`;
- network one-shot workflow created: `false`.

## Authorization State

Fail-closed state remains:
- source policy `PROPOSED`;
- real acquisition authorized `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- runner implementation authorized only for synthetic/mock: `true`;
- real semantic execution authorized `false`;
- transient-row privacy approval absent;
- real row access BLOCKED;
- real PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Next Recommended Action

Human promotion gate only:

`HUMAN_PROPERTY_TYPE_RUNNER_CANDIDATE_PROMOTION`

If approved, promote:
`m3-ca-sco-property-type-runner-implementation -> m2-state-governance-core`.

Promotion itself must remain non-executing and non-authorizing for real data. Actual one-shot semantic execution remains a later separate gate requiring explicit execution approval plus transient-row privacy approval.
