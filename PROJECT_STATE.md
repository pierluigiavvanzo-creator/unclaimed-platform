# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy
gates, SCO source governance, transport evidence, source-approval readiness, segmented transport evidence,
the `$500+` bounded structure inspection, the two-field privacy boundary, and the `PROPERTY_TYPE`
semantic-verification proposal are canonical on `m2-state-governance-core`.

Canonical HEAD before the current runner-design candidate:
`c1b7482cd2e0155c0763b80846a2ec1361173b8e`.

Canonical semantic-proposal post-promotion CI:
`34944076797` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Current Candidate

Branch:
`m3-ca-sco-property-type-runner-design`

Functional candidate HEAD:
`b0824d7cbbe693b1d75f3564abac458bcbc5d5e0`.

Functional CI:
`34946533156` — SUCCESS for both `quality` and `streamlit-candidate`.

Diff from canonical:
- ahead `1`;
- behind `0`;
- merge-base exactly `c1b7482cd2e0155c0763b80846a2ec1361173b8e`;
- six added design/contract/example/test/audit files;
- no runner file;
- no network workflow;
- no source policy or registry modification;
- no SCO request or source-body access.

## Canonical `$500+` Facts Reused

Exact structure evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Verified:
- four non-encrypted DEFLATED CSV members;
- identical 25-label header candidate;
- canonical local-header offsets;
- prior structure inspection read `393,216` source bytes;
- no real CSV data row has yet been sampled.

Canonical first-purpose scope remains:
1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

For semantic verification, `PROPERTY_ID` use/persistence remains prohibited. Owner/holder identity/address
fields remain prohibited.

## Runner Design Candidate

Design proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_runner_design.v1.json`

Design schema:
`schemas/common/property_type_semantic_runner_design.schema.json`

Future execution evidence schema:
`schemas/common/property_type_semantic_verification_execution.schema.json`

Synthetic execution examples:
`schemas/examples/ca_sco_500_plus_property_type_semantic_verification_execution.examples.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_DESIGN_REVIEW.md`

Contract test:
`tests/contract/test_ca_sco_property_type_semantic_runner_design.py`

Design status:
`DESIGN_REVIEW_ONLY_NOT_IMPLEMENTATION_AUTHORIZED`.

## Reuse Decision

- existing repository bounded Range runner primitives: `REUSE`;
- Python standard library transport/ZIP/DEFLATE/CSV primitives: `REUSE`;
- `remotezip`: `REJECT` for this task because the project requires exact hard request/byte caps,
  no fallback/widening behavior, and derived-summary-only persistence;
- C# `Papyrine/RemoteZip`: `REJECT`, including because documented full-buffer fallback on ignored Range
  is incompatible with fail-closed project behavior.

No new runtime dependency was added.

## Fixed Future Runner Boundary

Future runner path:
`scripts/ca_sco_property_type_semantic_verification.py`

Current state:
ABSENT.

Future one-shot workflow:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

Current state:
ABSENT.

Hard caps remain:
- 4 canonical CSV members;
- 4 rows/member maximum;
- 16 rows total maximum;
- 1 HEAD maximum;
- 4 Range GET maximum;
- 5 HTTP requests maximum;
- 131,072 response-body bytes/Range maximum;
- 524,288 source response-body bytes total maximum;
- 262,144 uncompressed transient bytes/member maximum;
- 1,048,576 uncompressed transient bytes total maximum;
- 32,768 bytes/logical CSV record maximum;
- no extra Range;
- no full-body fallback.

If the server ignores Range or returns non-206, the future runner must stop before consuming the
unexpected body.

## Execution Evidence Boundary

The new execution schema can persist only:
- execution/approval references;
- expected/observed transport metadata;
- request and byte counters;
- aggregate sample-row counts;
- rows examined/member;
- distinct `PROPERTY_TYPE` codes;
- distinct official insurance codes;
- semantic status;
- stop reason;
- fixed false safety flags.

It has no field for:
- raw ZIP or Range body;
- raw/full CSV rows;
- `PROPERTY_ID` values;
- owner/holder values;
- per-row `PROPERTY_TYPE` values.

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

## Next Recommended Action

Human implementation gate only:

`HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL`

If approved, the next candidate may implement the bounded runner and exercise it only against synthetic
fixtures/mocked transport. It must not create an executable network workflow or read a real SCO row.

Actual one-shot execution remains a later separate gate and requires explicit execution approval plus
transient-row privacy approval.
