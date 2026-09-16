# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

California SCO `PROPERTY_TYPE` handling remains governed by `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`, accepted policy `WHOLE_SOURCE_STOP`, implementation strategy `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`, and runner output contract `1.2.0`.

The v1.2 implementation, real-source execution proposal, proposal review and fresh single-use authorization are complete.

The authorized one-shot real-source execution has now been performed exactly once.

Execution result:

`STOPPED_FAIL_CLOSED / TRANSPORT_METADATA_DRIFT`

The runner stopped on live archive metadata drift before any source body or row was read. No `PROPERTY_TYPE` value was observed, so semantic compatibility remains unresolved.

## Execution Checkpoints

Execution branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-once`

Authorization checkpoint:

`5872db1368a5b9a2cdee79a0c2e54aa0b9b00dfa`

Authorization CI:

`35121670753` — **SUCCESS**

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

State of both approvals:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They were consumed when run `35123686954` invoked the authorized real-source runner. No retry is authorized and these refs must never be reused.

All earlier execution/privacy approvals also remain consumed and non-reusable.

## Actual Bounded Execution Result

Actual request usage:

- HEAD requests: `1`;
- Range requests: `0`;
- total HTTP requests: `1`;
- source body bytes read: `0`;
- rows examined: `0`.

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

The changed content length and ETag caused deterministic fail-closed stop reason:

`TRANSPORT_METADATA_DRIFT`

Because this was an unrelated transport stop, v1.2 correctly emitted:

`control_disposition = null`

The D-008 `PROPERTY_TYPE_NONCONFORMING_STOPPED / PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE` mapping was not reached during this execution.

## Proof Boundary

This execution proves only that:

- the live archive HEAD metadata no longer matches the runner's pinned content length and ETag;
- the runner failed closed before body access;
- v1.2 evidence remained schema-conforming and privacy-safe.

It does **not** establish whether source content, source structure or `PROPERTY_TYPE` semantics changed.

It does **not** resolve semantic compatibility.

No update to the pinned transport baseline is authorized by this evidence alone.

## Workflow Lifecycle

The temporary one-shot workflow and execution marker were removed immediately after the single run.

Current repository state contains neither:

`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`

nor:

`.github/ca-sco-property-type-semantic-verification-once.trigger.json`

No workflow-based retry path remains.

## Privacy / Safety Result

The execution persisted only allowed derived evidence.

No raw body, full row, `PROPERTY_ID`, owner/holder value, per-row `PROPERTY_TYPE`, offending bytes, source-derived hash/exact field length or record values were persisted.

All execution safety flags remained `false`, including full archive download, raw-body persistence, row persistence, identity resolution, beneficiary matching, outreach and production-classification activation.

No source body bytes were read and no source row was examined.

## Source / Product Governance State

- D-008 accepted as design: `true`;
- v1.2 implementation completed and human-reviewed: `true`;
- real-source proposal prepared and human-reviewed: `true`;
- one-shot real-source authorization granted and consumed: `true`;
- authorized real-source executions performed under those refs: `1`;
- retry authorized: `false`;
- temporary workflow present: `false`;
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

`DECISIONS.md` remains unchanged because this execution applied existing D-008 and the reviewed authorization without creating a new architectural decision.

## Next Recommended Action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

The evidence review must be repository-only. It must not make another source request, retry the execution, reuse consumed approvals, change the pinned transport baseline, modify runtime/parser/projector/regex, activate source policy/registry/production classification or open downstream identity/genealogy/matching/outreach/claim work.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
