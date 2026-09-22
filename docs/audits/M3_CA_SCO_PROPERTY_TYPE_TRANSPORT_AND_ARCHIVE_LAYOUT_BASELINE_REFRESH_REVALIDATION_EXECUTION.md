# M3 California SCO — PROPERTY_TYPE Transport + Archive-Layout Baseline Refresh Revalidation Execution

Date: 2026-09-17

Status: **ONE-SHOT EXECUTION COMPLETED — SUCCESS — CANDIDATE TRANSPORT/ARCHIVE-LAYOUT BASELINE ESTABLISHED AS EVIDENCE ONLY — FRESH APPROVALS CONSUMED — NO BASELINE ADOPTION**

## Execution action

`EXECUTE_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_ONCE`

Classification:

`A/B — MVP-1 critical-path enabler`

MVP-1 blocker addressed:

`FIRST_APPROVED_REAL_SOURCE -> transport/archive-layout baseline unresolved after TRANSPORT_METADATA_DRIFT`

## Frozen authorization / implementation checkpoints

Authorization checkpoint:

- branch: `m3-ca-sco-transport-archive-layout-revalidation-authorization`;
- HEAD: `4079fb44b36699e9b05821761c222d063a89648d`;
- CI: `35196883549` — **SUCCESS**.

Implementation preflight checkpoint:

- branch: `m3-ca-sco-transport-archive-layout-revalidation-once`;
- HEAD: `e87e7d20d766ad06ca0feb8805ac00c4a6ed547c`;
- dedicated preflight run: `35198561293` — **SUCCESS**;
- general CI run: `35198561164` — **SUCCESS**;
- source-network execution during preflight: `false`.

Trigger checkpoint:

`de4c20e0a4158da0497d2ca9c2090589636b40e0`

The trigger commit added only the exact single-use execution marker pinned to the accepted authorization/review/proposal checkpoints.

## Real one-shot workflow evidence

GitHub Actions workflow:

`ca-sco-transport-archive-layout-revalidation-once`

Run:

`35198720002`

Job:

`105128028851`

Run attempt:

`1`

Conclusion:

`SUCCESS`

The job confirms all of the following completed successfully in sequence:

1. implementation + authorization preflight validation;
2. repository-only structural verifier tests;
3. one-shot gate validation;
4. `Execute authorized structural revalidation once`;
5. derived evidence/schema/privacy validation;
6. upload of the derived evidence artifact only.

No rerun is authorized or performed.

## Approval consumption

Execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_REVALIDATION_EXECUTION_BOUNDED_B8F703DB`

Structural-byte privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_STRUCTURAL_BYTE_PRIVACY_BOUNDED_B8F703DB`

Both are now:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Consumption occurred when the authorized execution made its first California SCO network request. A retry is not authorized regardless of the outcome of this execution.

## Persisted artifact provenance

Workflow artifact:

- artifact id: `10487072813`;
- artifact name: `ca-sco-transport-archive-layout-revalidation-2026-09-17`;
- compressed artifact size: `714` bytes;
- GitHub artifact digest: `sha256:2ed7f3e620a50f635f3eae7dad5efca80f3dc86d239c728dd12dfd23eda07e65`;
- uploaded: `2026-09-17T08:15:59Z`.

Persisted derived evidence file:

`sources/evidence/ca_sco_segment_500_plus.property_type_transport_archive_layout_revalidation.execution.v1.json`

Evidence file SHA-256 after extraction:

`120f5ee2eef859578adb922f15138bab65cb19e7979274ed9360c24b9b071d64`

Evidence file size:

`895` bytes.

## Revalidation result

`REVALIDATION_RESULT_STATUS = CANDIDATE_BASELINE_ESTABLISHED`

`STOP_REASON = null`

Observed transport candidate:

- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`;
- observed at: `2026-09-17T08:15:58.436797Z`.

Canonical member match:

`ALL_CANONICAL_MEMBERS_UNIQUE`

Additional member count:

`0`

Candidate canonical local-header offsets derived from current Central Directory metadata:

1. `From_500_To_Beyond_1_of_4.csv` -> `0`;
2. `From_500_To_Beyond_2_of_4.csv` -> `59745428`;
3. `From_500_To_Beyond_3_of_4.csv` -> `96861315`;
4. `From_500_To_Beyond_4_of_4.csv` -> `134172553`.

These are candidate values only. They are not runtime constants and are not yet an adopted source baseline.

## Structural / privacy boundary outcome

The successful evidence contract contains exactly the previously authorized bounded derived fields. It contains no raw Range bytes, compressed payload, CSV row, `PROPERTY_ID`, `PROPERTY_TYPE`, owner/holder value, noncanonical member name, or other protected source record value.

The production verifier contains no CSV parser, no decompressor and no general-purpose ZIP payload reader. The execution remained bounded by the frozen caps:

- HEAD max `1`;
- Range max `4`;
- HTTP max `5`;
- response bytes/range max `131072`;
- source response-body max `524288`;
- full-body fallback `false`;
- widening `false`;
- retry `false`.

The approved evidence contract intentionally does not persist exact request counters. Therefore this audit does not invent an exact request count; it records only that the successful execution was enforced by the bounded verifier and completed inside the authorized limits.

## Adoption separation

This execution does **not** authorize or perform any of the following:

- replacement of `EXPECTED_LENGTH`;
- replacement of `EXPECTED_ETAG`;
- replacement of semantic-runner canonical member offsets;
- parser/projector/regex/normalization change;
- source policy activation;
- registry activation;
- production classification activation;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- claim submission.

The historical semantic-runner constants remain unchanged pending separate human candidate-evidence review and any later separately authorized implementation gate.

## Product state after execution

- approved real sources: `0`;
- candidate transport/archive-layout baseline established: `true`;
- candidate baseline adopted: `false`;
- semantic compatibility resolved: `false`;
- production classification active: `false`;
- real MVP-1 candidate cases: `0`.

The execution materially shortens the path to the first approved real source but does not itself approve that source.

## DECISIONS.md assessment

No new architectural, policy or strategy decision was introduced. `DECISIONS.md` remains unchanged.

## Next single action

Execute exclusively:

`HUMAN_PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_REVALIDATION_EVIDENCE_REVIEW`

Classification:

`A/B — MVP-1 critical-path enabler`

That review must decide whether the candidate transport/archive-layout evidence is sufficient to support a later separate baseline-adoption implementation gate. It must not itself rerun the source execution or silently mutate semantic-runner constants.
