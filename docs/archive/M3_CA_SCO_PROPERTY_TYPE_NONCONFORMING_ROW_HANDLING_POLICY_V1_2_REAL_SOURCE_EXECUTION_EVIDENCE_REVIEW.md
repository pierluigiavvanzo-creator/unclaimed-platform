# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution Evidence Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS — EVIDENCE ACCEPTED — TRANSPORT + ARCHIVE-LAYOUT BASELINE REFRESH PROPOSAL JUSTIFIED — NO REBASELINE, RETRY OR RUNTIME CHANGE AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- review base branch: `m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-once`;
- review base HEAD: `05a475ef2ddd0ed86f4e934c919bb1d98c58d566`;
- review base CI: `35124327126` — **SUCCESS**;
- one-shot execution run: `35123686954` — **SUCCESS**, attempt `1`;
- real execution trigger checkpoint: `c32df1725390de8784e9bb2f29bea8b4f933abac`;
- cleanup/evidence checkpoint: `448e209d7c8afaec4e0f4b6efc1e5598803d87e5`;
- cleanup/evidence CI: `35124024271` — **SUCCESS**;
- execution artifact id: `10457344882`;
- artifact digest: `sha256:c4146f9bced7722fa5da26a8c1d2ace5a65e610fac7ae190d720bd098e06e6e0`;
- persisted evidence: `sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`;
- execution audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`;
- evidence contract test: `tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`.

This review is repository-only. It performs no California SCO request, no source-body access, no row access, no retry, no approval reuse and no runtime modification.

## Decision

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

The persisted v1.2 execution evidence is internally consistent with the reviewed execution contract, the execution audit and the permanent contract test. It is sufficient to accept the one-shot result as valid evidence of a deterministic fail-closed transport stop.

The evidence is also sufficient to justify preparation of a separate **offline transport-and-archive-layout baseline refresh proposal**.

It is **not** sufficient to authorize:

- direct replacement of the pinned content length or ETag;
- inference or replacement of ZIP member offsets;
- another source request or execution retry;
- reuse of consumed approvals;
- any runner/parser/projector/regex/normalization change;
- source activation, registry activation or production classification;
- any downstream identity, genealogy, beneficiary matching, outreach or claim action.

## Evidence integrity review

Persisted result:

- `schema_version = 1.2.0`;
- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

Actual request/data use:

- HEAD requests: `1`;
- Range requests: `0`;
- HTTP requests total: `1`;
- source response-body bytes read: `0`;
- source rows examined: `0`;
- distinct `PROPERTY_TYPE` codes observed: none;
- distinct insurance codes observed: none.

All persisted safety flags remained `false`. No raw body, full row, `PROPERTY_ID`, owner/holder value, per-row `PROPERTY_TYPE`, offending bytes/hash/exact source-field length, transient source file, identity resolution, beneficiary matching, outreach or production classification was persisted or performed.

The evidence validates against `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json` and its permanent contract test confirms workflow/trigger removal and downstream closure.

## Transport evidence reviewed

Pinned expected transport metadata:

- content length: `162416884`;
- ETag: `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type: `application/zip`;
- Accept-Ranges: `bytes`.

Observed live HEAD metadata during the single authorized execution:

- HTTP status: `200`;
- content length: `162560390`;
- ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- content type: `application/zip`;
- Accept-Ranges: `bytes`;
- Last-Modified: `Wed, 16 Sep 2026 16:43:22 GMT`.

The changed content length and ETag are sufficient to establish that the runner's previously pinned transport identity no longer matched the live HEAD observation at execution time. They are not sufficient to establish why the archive changed or whether the observed values should become a new durable baseline.

## Archive-layout dependency review

The reviewed runner does not depend only on content length and ETag. It also pins the local ZIP-header offsets used for the four canonical members:

1. `From_500_To_Beyond_1_of_4.csv` — offset `0`;
2. `From_500_To_Beyond_2_of_4.csv` — offset `59747797`;
3. `From_500_To_Beyond_3_of_4.csv` — offset `96862896`;
4. `From_500_To_Beyond_4_of_4.csv` — offset `134174190`.

The reviewed real-source proposal freezes the same four offsets in its `sample_plan`.

Because the live ZIP's identity changed, this review cannot assume that the old local-header offsets remain correct. A direct update of only content length and ETag could therefore bind future range requests to stale archive-layout assumptions.

Accordingly, the old transport and archive-layout pins are considered **stale for future execution planning**, but they are not overwritten by this review.

## Proof boundary

This review accepts the following as established:

- exactly one authorized execution occurred;
- the execution stopped fail-closed before body access;
- the live HEAD metadata differed from the pinned content length and ETag;
- no row or `PROPERTY_TYPE` value was observed;
- privacy/persistence boundaries were preserved;
- the approvals were consumed and the workflow/trigger were removed;
- no retry path remains.

This review does **not** establish:

- whether the ZIP contents changed semantically;
- whether the canonical member names changed;
- whether the four historical local-header offsets remain valid;
- whether any CSV layout or field meaning changed;
- whether `PROPERTY_TYPE` is currently conforming or nonconforming;
- whether the new observed ETag/content length are stable enough to pin;
- whether another real-source execution should be authorized.

Semantic compatibility therefore remains unresolved.

## Approval / workflow lifecycle

Consumed execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed transient-row privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

They must not be reused. No retry is authorized.

The temporary one-shot workflow and trigger marker remain absent from the repository. This review creates no workflow and performs no source access.

## Baseline-refresh proposal boundary

A separate offline proposal is justified because a future bounded execution requires a reviewed method for refreshing or revalidating all transport/archive-layout assumptions together.

That future proposal must remain design-only and must, at minimum:

- distinguish transport identity pins from archive-layout/member-offset pins;
- preserve fail-closed behavior on identity or layout mismatch;
- compare deterministic refresh/revalidation strategies without silently selecting live values;
- define how a later separately authorized check could establish a fresh content length and ETag;
- define how a later separately authorized structural check could establish canonical member identity and local-header offsets without broad source-body acquisition;
- avoid assuming that current observed metadata or historical offsets remain stable;
- prohibit inferred offsets or unverified arithmetic rebasing;
- preserve existing sample, privacy, byte and request caps unless a separate reviewed design explicitly changes them;
- require fresh, single-use authorization before any later network request;
- define a separate privacy gate if any later design could expose source rows or protected fields;
- leave source policy, registry, production classification and downstream gates closed.

The proposal must not itself access the source or update the current runner constants.

## Runtime / D-008 state

D-008 remains unchanged. The accepted policy remains `WHOLE_SOURCE_STOP`; implementation strategy remains `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`; execution schema remains `1.2.0`; validation remains `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The `PROPERTY_TYPE_FORMAT_UNEXPECTED` D-008 control-disposition mapping was not reached in the one-shot execution. No parser, projector, regex, trimming, casing or normalization change is justified by the transport evidence.

`DECISIONS.md` therefore requires no new decision entry for this review.

## Governance state after review

Fail-closed state remains:

- one-shot real-source execution performed: `true`;
- execution count under the consumed fresh refs: `1`;
- retry authorized: `false`;
- consumed approvals reusable: `false`;
- temporary workflow present: `false`;
- current transport/archive-layout baseline suitable for blind reuse: `false`;
- baseline refresh authorized: `false`;
- another network verification authorized: `false`;
- semantic compatibility resolved: `false`;
- source continuation authorized: `false`;
- privacy expansion authorized: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- production classification: inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission: BLOCKED.

## Next single action

Prepare exclusively:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

This next task is repository-only and design-only. It must perform no source request, no HEAD request, no Range request and no authority request. It must not update runner constants, infer new member offsets, grant approvals, create a network workflow, retry the prior execution or activate any downstream gate.

Any later network revalidation must be separately proposed, human-reviewed and authorized with fresh single-use approval references before the first request.