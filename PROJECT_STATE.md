# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

California SCO `PROPERTY_TYPE` handling remains governed by `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`, accepted policy `WHOLE_SOURCE_STOP`, implementation strategy `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`, and runner output contract `1.2.0`.

The v1.2 implementation, real-source execution proposal/review, fresh single-use authorization, one-shot real-source execution and human execution-evidence review are complete.

The one-shot execution result remains:

`STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`

Human evidence-review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

The evidence is accepted as valid proof that the runner failed closed before body access when the live HEAD metadata no longer matched the pinned transport identity. It provides no new `PROPERTY_TYPE` semantic evidence.

## Review Checkpoint

Review branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-evidence-review`

Review base execution HEAD:

`05a475ef2ddd0ed86f4e934c919bb1d98c58d566`

Review base CI:

`35124327126` — **SUCCESS**

Human review artifact:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`

## Execution Evidence

Real execution trigger checkpoint:

`c32df1725390de8784e9bb2f29bea8b4f933abac`

One-shot workflow run:

`35123686954` — **SUCCESS**, attempt `1`

Cleanup/evidence checkpoint:

`448e209d7c8afaec4e0f4b6efc1e5598803d87e5`

Cleanup/evidence CI:

`35124024271` — **SUCCESS**

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`

Evidence contract test:

`tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`

## Single-Use Approval State

Execution approval ref:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Transient-row privacy approval ref:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They were consumed when run `35123686954` invoked the authorized real-source runner. No retry is authorized and these refs must never be reused. All earlier execution/privacy approvals also remain consumed and non-reusable.

## Actual Bounded Execution Result

Actual request/data usage:

- HEAD requests: `1`;
- Range requests: `0`;
- total HTTP requests: `1`;
- source body bytes read: `0`;
- rows examined: `0`;
- `PROPERTY_TYPE` values observed: `0`.

Expected pinned transport metadata:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`.

Observed live HEAD metadata:

- HTTP status: `200`;
- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

The changed content length and ETag caused deterministic fail-closed stop reason `TRANSPORT_METADATA_DRIFT`. Because this was an unrelated transport stop, v1.2 correctly emitted `control_disposition = null`.

The D-008 `PROPERTY_TYPE_NONCONFORMING_STOPPED / PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE` mapping was not reached.

## Baseline Staleness / Archive Layout

The evidence review found that future execution planning cannot safely refresh only content length and ETag.

The current runner and reviewed sample plan also pin four ZIP local-header offsets:

- `From_500_To_Beyond_1_of_4.csv` → `0`;
- `From_500_To_Beyond_2_of_4.csv` → `59747797`;
- `From_500_To_Beyond_3_of_4.csv` → `96862896`;
- `From_500_To_Beyond_4_of_4.csv` → `134174190`.

Because the live ZIP identity changed, the old transport and archive-layout pins are treated as **stale for future execution planning**. This does not mean that the historical offsets are proven wrong; it means they must not be blindly reused or arithmetically rebased without a separately reviewed verification path.

No new ETag, content length or member offset has been adopted by the review.

## Proof Boundary

The execution/review establish only that:

- the live HEAD metadata differed from the pinned transport identity at execution time;
- the runner stopped fail-closed before body access;
- v1.2 evidence remained schema-conforming and privacy-safe;
- approvals were consumed and workflow/trigger were removed.

They do **not** establish whether source contents, ZIP member layout, CSV structure or `PROPERTY_TYPE` semantics changed.

Semantic compatibility remains unresolved.

## Workflow Lifecycle / Privacy

The temporary one-shot workflow and execution marker remain absent. No workflow-based retry path remains.

No raw body, full row, `PROPERTY_ID`, owner/holder value, per-row `PROPERTY_TYPE`, offending bytes/hash/exact field length or record values were persisted. No source row was examined.

## Source / Product Governance State

- D-008 accepted as design: `true`;
- v1.2 implementation completed and human-reviewed: `true`;
- one-shot real-source execution completed: `true`;
- execution evidence human-reviewed: `true`;
- execution evidence accepted: `true`;
- consumed approvals reusable: `false`;
- retry authorized: `false`;
- temporary workflow present: `false`;
- current transport/archive-layout baseline suitable for blind reuse: `false`;
- baseline refresh authorized: `false`;
- another network verification authorized: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- parser/projector unchanged: `true`;
- regex/normalization unchanged: `true`;
- semantic compatibility resolved: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

`DECISIONS.md` remains unchanged because the evidence review does not introduce a new architectural decision.

## Next Recommended Action

Prepare exclusively:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

This next action is repository-only and design-only. It must perform no network/source request, must not update current runner constants or infer new member offsets, must not grant approvals or create a workflow, and must not activate source policy, registry, production classification or downstream work.

Any later network revalidation requires a separate reviewed proposal and fresh single-use authorization before the first request.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
