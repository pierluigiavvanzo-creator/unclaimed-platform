# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Status

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy gates, SCO governance/transport evidence, the `$500+` bounded structure inspection, the two-field privacy boundary, the `PROPERTY_TYPE` semantic-verification proposal, the bounded runner design, and the bounded `PROPERTY_TYPE` runner implementation are canonical on `m2-state-governance-core`.

Promoted runner-implementation functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`.

Canonical post-promotion CI:
`34961511401` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Promotion Evidence

Before promotion:
- canonical `6105c22a7d31df7afca00282eff7e9798e98b868`;
- candidate `3f612837e4dbb86839942555c34b9384ff4e99a1`;
- ahead `4`;
- behind `0`;
- merge-base exactly `6105c22a7d31df7afca00282eff7e9798e98b868`.

Owner explicitly approved:
`m3-ca-sco-property-type-runner-implementation -> m2-state-governance-core`.

Promotion was a non-force fast-forward to:
`3f612837e4dbb86839942555c34b9384ff4e99a1`.

Canonical post-promotion CI:
`34961511401` — SUCCESS.

## Canonical Runner Implementation

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Implementation authorization evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_runner_implementation_approval.v1.json`

Implementation audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_IMPLEMENTATION.md`

Network one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

Current state:
ABSENT.

The runner is transport-injectable and was validated only with synthetic/mock transport. A fixed real HTTP transport exists for a later separately authorized execution gate, but no real SCO request was made during implementation or promotion.

## Fixed Safety Boundary

Hard caps remain unchanged:
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

Ignored Range/non-206 causes STOP before the unexpected response body is consumed.

## Privacy / Persistence Boundary

The runner verifies the exact canonical 25-column header and projects only `PROPERTY_TYPE` for semantic verification. `PROPERTY_ID` is not used or persisted during semantic verification.

Never persist/log as execution evidence:
- raw Range bodies;
- full rows;
- `PROPERTY_ID` values;
- owner/holder values;
- per-row `PROPERTY_TYPE` values.

Allowed evidence remains derived summary only: aggregate row counts, rows/member, distinct `PROPERTY_TYPE` codes, distinct official insurance codes, request/byte counters, semantic status and stop reason.

Real CSV parsing may transiently expose prohibited owner/holder bytes. Therefore real execution remains blocked until separate transient-row privacy approval.

## Verification History

Implementation functional CI:
`34951460475` — SUCCESS for Ruff, mypy, contract, smoke, full pytest including runner unit tests, frontend lint/typecheck/build, and Streamlit smoke.

Candidate docs-closure CI:
`34951888095` — SUCCESS.

Canonical post-promotion CI:
`34961511401` — SUCCESS.

Intermediate failed runs are retained in history:
- `34950942449`: Ruff import rule only;
- `34951326633`: historical proposal contract still asserted permanent runner absence.

Both were corrected narrowly without force-push or history rewrite.

## Network / Real Data State

Across implementation and promotion:
- new SCO network requests: `0`;
- new SCO response-body bytes: `0`;
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
- runner implementation canonical but authorized only for synthetic/mock validation;
- real semantic execution authorized `false`;
- transient-row privacy approval absent;
- real row access BLOCKED;
- real PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

Promotion did not authorize or execute real data access.

## Next Recommended Action

Human semantic-execution review gate only:

`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`

Any later real one-shot semantic sampling requires explicit owner execution approval **and** transient-row privacy approval before any real row can be read. Source approval/registry activation remain separate later gates.
