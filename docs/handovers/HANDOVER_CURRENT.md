# HANDOVER_CURRENT.md

Last updated: 2026-09-16

## Repository

`pierluigiavvanzo-creator/unclaimed-platform`

GitHub is the canonical source of truth.

## Current Working Branch

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-evidence-review`

Created from execution checkpoint:

`05a475ef2ddd0ed86f4e934c919bb1d98c58d566`

Execution-checkpoint CI:

`35124327126` — **SUCCESS**

## Completed Action

Completed:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

Human review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

Review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`

Meaning:

- the persisted one-shot evidence is accepted as internally consistent, schema-conforming and privacy-safe;
- the one-shot `TRANSPORT_METADATA_DRIFT` stop is accepted as valid fail-closed behavior;
- the evidence justifies only a later offline proposal for refreshing/revalidating the transport + ZIP archive-layout baseline;
- this review performs no network/source access;
- no rebaseline, retry, runtime change, approval grant or downstream activation is authorized.

## Reviewed Execution Evidence

One-shot execution run:

`35123686954` — **SUCCESS**, attempt `1`

Real execution trigger checkpoint:

`c32df1725390de8784e9bb2f29bea8b4f933abac`

Cleanup/evidence checkpoint:

`448e209d7c8afaec4e0f4b6efc1e5598803d87e5`

Cleanup/evidence CI:

`35124024271` — **SUCCESS**

Artifact:

- id: `10457344882`;
- name: `ca-sco-property-type-v1-2-real-source-execution-2026-09-16`;
- digest: `sha256:c4146f9bced7722fa5da26a8c1d2ace5a65e610fac7ae190d720bd098e06e6e0`.

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`

Evidence contract test:

`tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`

Machine result:

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

## Actual Request / Data Boundary

Actual execution usage:

- HEAD requests: `1`;
- Range requests: `0`;
- HTTP requests total: `1`;
- source body bytes read: `0`;
- sample rows examined: `0`;
- rows examined in every canonical member: `0`;
- distinct `PROPERTY_TYPE` codes observed: none;
- distinct insurance codes observed: none.

No source row, `PROPERTY_TYPE`, `PROPERTY_ID`, owner/holder or other record value was observed or persisted.

## Transport Evidence

Pinned expected metadata:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type: `application/zip`;
- Accept-Ranges: `bytes`.

Observed live HEAD metadata:

- HTTP status: `200`;
- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

The content-length and ETag mismatch caused the deterministic transport stop before body access.

The observed values are evidence from one timestamp, not an automatically adopted replacement baseline.

## Archive-Layout Dependency

The current runner and reviewed real-source proposal also pin four ZIP local-header offsets:

1. `From_500_To_Beyond_1_of_4.csv` — `0`;
2. `From_500_To_Beyond_2_of_4.csv` — `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` — `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` — `134174190`.

Because the live ZIP identity changed, the evidence review does not assume these historical offsets remain valid. It also does not declare them invalid, because no archive body/layout was inspected in the stopped run.

For future execution planning, transport identity and archive-layout/member-offset pins must therefore be refreshed or revalidated together under a separate reviewed design. No new offsets may be inferred or arithmetically rebased from the observed size difference.

## Approval State / Retry Closure

Execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They must not be reused. No retry is authorized.

The temporary one-shot workflow and trigger marker remain absent. No workflow-based retry path remains.

## Canonical Read Order Before Any New Change

Read in order:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `ROADMAP.md`
4. `DECISIONS.md`
5. `docs/handovers/HANDOVER_CURRENT.md`

Then inspect, in this order as relevant:

1. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`
2. `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`
3. `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`
4. `tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`
5. `scripts/ca_sco_property_type_semantic_verification.py`
6. `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1.json`
7. `docs/audits/M3_CA_SCO_TRANSPORT_PREFLIGHT_PROPOSAL.md`
8. `docs/audits/M3_CA_SCO_TRANSPORT_PREFLIGHT_EXECUTION.md`
9. authorization/proposal-review artifacts as needed.

## Governing Runtime / D-008 State

Decision:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

Accepted design:

`WHOLE_SOURCE_STOP`

Accepted implementation strategy:

`ADDITIVE_VERSIONED_CONTROL_DISPOSITION`

Current runner output contract:

`1.2.0`

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

The D-008 `PROPERTY_TYPE_FORMAT_UNEXPECTED` control-disposition mapping was not reached in the stopped one-shot execution. This review makes no new semantic claim about `PROPERTY_TYPE`.

`DECISIONS.md` remains unchanged because the evidence review introduces no new architectural decision.

## Privacy / Persistence State

The stopped run read zero source body bytes and zero source rows.

No raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact source-field length, record values in logs, real-row quarantine or row-specific human inspection occurred.

No privacy expansion is authorized.

## Source / Downstream Governance

Current state:

- one-shot real-source execution performed: `true`;
- execution evidence human-reviewed: `true`;
- execution evidence accepted: `true`;
- execution count under consumed fresh refs: `1`;
- consumed approvals reusable: `false`;
- retry authorized: `false`;
- temporary workflow present: `false`;
- current transport/archive-layout baseline suitable for blind reuse: `false`;
- baseline refresh authorized: `false`;
- another network verification authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

## SINGLE NEXT ACTION

Prepare exclusively:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

This next task is **repository-only and design-only**.

It must define a bounded proposal for how transport identity and ZIP archive-layout/member offsets could later be refreshed or revalidated together. It must compare deterministic fail-closed options and preserve provenance of old versus proposed baselines.

It must not:

- perform a California SCO or other external request;
- perform HEAD, Range GET or authority retrieval;
- reuse consumed approval refs;
- grant fresh approvals;
- create a network workflow;
- retry the prior execution;
- update `EXPECTED_LENGTH`, `EXPECTED_ETAG` or canonical member offsets;
- infer or arithmetically rebase offsets;
- modify runner/parser/projector/regex/normalization;
- widen privacy or source continuation;
- activate source policy, registry or production classification;
- begin identity resolution, genealogy, beneficiary matching, outreach or claim work.

If the later proposal recommends any network revalidation, that execution must remain a separate gate with human review and fresh single-use authorization before the first request. Any row/protected-field exposure would require an explicitly reviewed privacy boundary.

## Restart Instruction

1. verify remote HEAD of the current evidence-review branch;
2. verify latest CI for that exact HEAD;
3. read the five canonical files in order;
4. read the evidence-review audit, execution audit/evidence/test, runner and reviewed execution proposal;
5. execute only the `SINGLE NEXT ACTION`;
6. perform no external request during the proposal task.
