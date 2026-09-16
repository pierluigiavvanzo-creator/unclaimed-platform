# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | V1.2 REAL-SOURCE EVIDENCE REVIEW PASS; TRANSPORT + ARCHIVE-LAYOUT BASELINE REFRESH PROPOSAL NEXT | one-shot stopped fail-closed before body access; approvals consumed; no retry; baseline refresh not authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- D-008 accepted `WHOLE_SOURCE_STOP` as design;
- accepted implementation strategy: `ADDITIVE_VERSIONED_CONTROL_DISPOSITION`;
- v1.2 implementation completed and human-reviewed;
- runner output contract remains `1.2.0`;
- real-source execution proposal/review and fresh single-use authorization completed;
- authorized one-shot execution performed exactly once;
- one-shot evidence human-reviewed and accepted;
- both fresh approvals consumed and non-reusable;
- no retry authorized;
- source continuation remains `false`;
- semantic compatibility remains unresolved.

Human evidence-review result:

`PASS_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_ACCEPTED_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL_JUSTIFIED_NO_REBASELINE_RETRY_OR_RUNTIME_CHANGE_AUTHORIZED`

## Reviewed One-Shot Result

Execution branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-v1-2-real-source-execution-once`

Execution final HEAD before review:

`05a475ef2ddd0ed86f4e934c919bb1d98c58d566`

Execution final CI:

`35124327126` — **SUCCESS**

One-shot run:

`35123686954` — **SUCCESS**, attempt `1`

Execution outcome:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = TRANSPORT_METADATA_DRIFT`;
- `control_disposition = null`.

Actual usage:

- 1 HEAD request;
- 0 Range requests;
- 1 HTTP request total;
- 0 source body bytes read;
- 0 rows examined;
- no `PROPERTY_TYPE` value observed.

## Transport / Archive-Layout Finding

Expected transport identity:

- content length `162416884`;
- ETag `"b25b315b6cd8007624387c3a00d4b1fe"`.

Observed live HEAD:

- content length `162560390`;
- ETag `"222dd79f04c2a0a8fff166b01c8da746"`;
- HTTP status `200`;
- content type `application/zip`;
- Accept-Ranges `bytes`;
- Last-Modified `Wed, 16 Sep 2026 16:43:22 GMT`.

The runner also pins four ZIP local-header offsets used by the deterministic sample plan:

- `From_500_To_Beyond_1_of_4.csv` → `0`;
- `From_500_To_Beyond_2_of_4.csv` → `59747797`;
- `From_500_To_Beyond_3_of_4.csv` → `96862896`;
- `From_500_To_Beyond_4_of_4.csv` → `134174190`.

Because the live ZIP identity changed, a future path cannot safely update only content length and ETag while assuming the historical archive-layout offsets remain valid. The existing transport/archive-layout baseline is therefore stale for future execution planning, but no new baseline values are adopted by this review.

## Approval / Workflow State

Consumed execution approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_A2139884`

Consumed privacy approval:

`OWNER_APPROVAL_2026-09-16_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_A2139884`

Both remain `CONSUMED_SINGLE_USE_NON_REUSABLE`.

The temporary one-shot workflow and trigger marker remain absent. No retry path remains.

## Evidence Review Artifact

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_EVIDENCE_REVIEW.md`

The review is repository-only and performs no source access.

## Privacy / Source Governance

No raw source body or row was read during the stopped execution. No protected source values were persisted.

No rebaseline, runtime modification, another network verification or approval grant is authorized by the evidence review.

Source policy remains `PROPOSED`. Registry remains disabled/unapproved. Approved real sources remain `0`. Production classification and all downstream identity/genealogy/matching/outreach/claim gates remain inactive.

## Next Product Work

Prepare exclusively:

`PROPERTY_TYPE_TRANSPORT_AND_ARCHIVE_LAYOUT_BASELINE_REFRESH_PROPOSAL`

The proposal must be repository-only and design-only. It must:

- distinguish transport identity from ZIP archive-layout/member-offset assumptions;
- define fail-closed refresh/revalidation options;
- avoid adopting the newly observed ETag/content length without a later separately authorized verification;
- avoid inferring or arithmetically rebasing member offsets;
- preserve existing runtime, parser/projector, regex, privacy and downstream closures;
- require a separate human-reviewed authorization before any future network request.

It must not perform source or authority access, update runner constants, create a network workflow, grant approvals, retry the prior run or activate source/registry/production/downstream gates.
