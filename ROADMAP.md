# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | V1.2 ONE-SHOT REAL-SOURCE EXECUTED; TRANSPORT_METADATA_DRIFT FAIL-CLOSED; HUMAN EVIDENCE REVIEW NEXT | one authorized run; no body/row access; approvals consumed; workflow removed |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- v1.2 implementation completed and human-reviewed;
- runner output contract remains `1.2.0`;
- real-source execution proposal prepared and human-reviewed PASS;
- fresh single-use execution/privacy authorization was granted;
- the authorized one-shot execution has been performed exactly once;
- both fresh approvals are consumed and non-reusable;
- no retry is authorized;
- source continuation remains `false`;
- semantic compatibility remains unresolved.

## One-Shot Real-Source Execution

Execution branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-once`

Authorization checkpoint:

`5872db1368a5b9a2cdee79a0c2e54aa0b9b00dfa`

Real execution trigger checkpoint:

`c32df1725390de8784e9bb2f29bea8b4f933abac`

One-shot run:

`35123686954` — **SUCCESS**, attempt `1`

Cleanup/evidence checkpoint:

`448e209d7c8afaec4e0f4b6efc1e5598803d87e5`

Cleanup/evidence CI:

`35124024271` — **SUCCESS**

Execution outcome:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

Actual request/data usage:

- 1 HEAD request;
- 0 Range requests;
- 1 HTTP request total;
- 0 source body bytes read;
- 0 rows examined;
- no `PROPERTY_TYPE` value observed.

## Transport Drift Evidence

Expected:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`.

Observed:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- HTTP status `200`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

The runner failed closed before body access because the live content length and ETag no longer matched the pinned transport metadata.

This evidence does not establish whether source contents, archive structure or `PROPERTY_TYPE` semantics changed. The D-008 PROPERTY_TYPE mismatch disposition was not reached.

## Approval / Workflow Lifecycle

Consumed execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both are:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

The temporary one-shot workflow and trigger marker were removed immediately after the run. No retry path remains in the repository.

## Evidence

Persisted derived evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_2.real_source_once.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION.md`

Evidence contract test:

`tests/contract/test_ca_sco_property_type_v1_2_real_source_execution_evidence.py`

The evidence validates against the v1.2 execution schema and records only permitted derived metadata.

## Privacy / Source Governance

No raw source body or row was read during the stopped execution.

No raw/full-row persistence, `PROPERTY_ID`, owner/holder, per-row `PROPERTY_TYPE`, offending bytes/hash/exact field length, real-row quarantine or row-specific human inspection occurred.

Source policy remains `PROPOSED`. Registry remains disabled/unapproved. Approved real sources remain `0`. Production classification and all downstream identity/genealogy/matching/outreach/claim gates remain inactive.

## Next Product Work

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW`

The human evidence review may assess the persisted derived evidence and define a later governance proposal if justified.

It must not:

- make another source request;
- retry the execution;
- reuse consumed approval refs;
- silently update the pinned transport metadata;
- modify runner/parser/projector/regex/normalization;
- widen privacy or source continuation;
- activate source policy, registry or production classification;
- begin downstream identity resolution, genealogy, beneficiary matching, outreach or claim submission.
