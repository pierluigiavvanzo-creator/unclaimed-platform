# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Status

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy gates, SCO governance/transport evidence, the `$500+` bounded structure inspection, the two-field privacy boundary, the `PROPERTY_TYPE` semantic-verification proposal, and the bounded `PROPERTY_TYPE` runner design are canonical on `m2-state-governance-core`.

Promoted runner-design functional SHA:
`62e32ebe38e218bbe4312f48ff2fa2eefb010df9`.

Canonical post-promotion CI:
`34947637509` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Canonical Runner Design

Design proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_runner_design.v1.json`

Design schema:
`schemas/common/property_type_semantic_runner_design.schema.json`

Future execution evidence schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

Synthetic examples:
`schemas/examples/ca_sco_500_plus_property_type_semantic_verification_execution.examples.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_DESIGN_REVIEW.md`

Contract test:
`tests/contract/test_ca_sco_property_type_semantic_runner_design.py`

Design status remains:
`DESIGN_REVIEW_ONLY_NOT_IMPLEMENTATION_AUTHORIZED`.

## Fixed Future Runner Boundary

Planned runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Current state:
ABSENT.

Planned one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

Current state:
ABSENT.

Hard caps remain:
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
- no extra Range request;
- no full-body fallback;
- no automatic cap widening.

If Range is ignored or a member response is not HTTP 206, the future runner must STOP before consuming an unexpected full body.

## Privacy / Persistence Boundary

Future execution may persist only derived summary evidence: aggregate row counts, rows/member, distinct `PROPERTY_TYPE` codes, distinct official insurance codes, transport/request counters, semantic status and stop reason.

Never persist/log raw Range bodies, full rows, `PROPERTY_ID`, owner/holder values, or per-row `PROPERTY_TYPE` values.

Transient full-row exposure remains separately gated. Real execution requires an explicit transient-row privacy approval. Buffer retention remains `0 days` with immediate disposal after projection or STOP.

## Authorization State

Unchanged and fail-closed:
- source policy `PROPOSED`;
- real acquisition authorized `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- runner implementation authorized `false`;
- semantic execution authorized `false`;
- transient-row privacy approval absent;
- real row access BLOCKED;
- real PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

Promotion did not implement a runner, create a network workflow, read a real row, approve PII, approve the source, or activate the registry.

## Promotion Evidence

Before promotion:
- canonical `c1b7482cd2e0155c0763b80846a2ec1361173b8e`;
- candidate `62e32ebe38e218bbe4312f48ff2fa2eefb010df9`;
- ahead `2`;
- behind `0`;
- merge-base exactly `c1b7482cd2e0155c0763b80846a2ec1361173b8e`.

Owner explicitly approved:
`m3-ca-sco-property-type-runner-design -> m2-state-governance-core`.

Promotion was a non-force fast-forward to:
`62e32ebe38e218bbe4312f48ff2fa2eefb010df9`.

Canonical post-promotion CI:
`34947637509` — SUCCESS.

## Next Recommended Action

Human implementation gate only:

`HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL`

If approved, the next candidate may implement the bounded runner and test it only against synthetic fixtures/mocked transport. It must not create an executable network workflow or read a real SCO row.

Actual one-shot semantic execution remains a later, separate gate requiring explicit execution approval plus transient-row privacy approval.
