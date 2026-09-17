# M3 California SCO — PROPERTY_TYPE v1.2 Adopted-Baseline Real-Source Execution Authorization

Date: 2026-09-17

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — PASS — FRESH SINGLE-USE EXECUTION + PRIVACY APPROVALS GRANTED — ONE-SHOT PATH AUTHORIZED — EXECUTION NOT YET PERFORMED**

## Authorization gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

## Owner authorization

The Product Owner explicitly authorized:

`APPROVO FRESH SINGLE-USE EXECUTION + TRANSIENT-ROW PRIVACY`

This authorization applies only to the frozen, human-reviewed proposal `1.1.0` and adopted transport/archive-layout baseline.

## Authoritative checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- authorization base branch: `m3-ca-sco-v1-2-proposal-contract-preservation-remediation`
- authorization base HEAD: `c18cddfc92bf3bb69f40b76170e687136e7fd21a`
- authorization base CI: `35221904089` — **SUCCESS**
- proposal review result: `PASS_REMEDIATED_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_FOR_FRESH_SINGLE_USE_AUTHORIZATION`
- proposal id: `ca.sco.segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution`
- proposal version: `1.1.0`
- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`
- governing decision: `D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`
- runtime contract: `1.2.0`

## Decision

`PASS_FRESH_SINGLE_USE_EXECUTION_PRIVACY_APPROVALS_GRANTED_ONE_SHOT_PATH_AUTHORIZED_EXECUTION_NOT_PERFORMED`

## Fresh approval references

Execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_C18CDDFC`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_C18CDDFC`

Both approvals are:

- status: `GRANTED_NOT_CONSUMED`;
- fresh: `true`;
- single-use: `true`;
- reusable: `false`;
- bound to proposal version `1.1.0`;
- bound to reviewed checkpoint `c18cddfc92bf3bb69f40b76170e687136e7fd21a`;
- bound to runtime contract `1.2.0`;
- valid only for the exact adopted baseline, sample, transport, validation and privacy boundaries below;
- independent of all historical approvals.

All prior execution/privacy approvals remain consumed and non-reusable.

The fresh approvals become consumed when the authorized one-shot workflow invokes the real-source runner. No automatic retry is authorized.

## Authorized adopted baseline

- expected content length: `162560390`;
- expected ETag: `"222dd79f04c2a0a8fff166b01c8da746"`;
- canonical member offsets: `0`, `59745428`, `96861315`, `134172553`.

## Authorized execution scope

A dedicated execution branch may:

1. create the temporary workflow `.github/workflows/ca-sco-property-type-semantic-verification-once.yml`;
2. pin it to this authorization checkpoint and the two fresh approval refs;
3. run a repository-local preflight before source access;
4. perform exactly one bounded real-source execution of `scripts/ca_sco_property_type_semantic_verification.py`;
5. validate the derived result against `schemas/common/property_type_semantic_verification_execution.v1_2.schema.json` and the hard caps;
6. persist/upload only permitted derived evidence;
7. remove the temporary workflow and trigger immediately after the run;
8. mark both approvals consumed;
9. stop at evidence review/source decision.

Workflow creation authorized: `true`.

Real-source execution authorized: `true`.

Real-source execution performed by this authorization record: `false`.

## Fixed sample / transport caps

Authorization is limited exactly to:

- 4 canonical members;
- max 4 data rows/member;
- max 16 data rows total;
- max 1 HEAD request;
- max 4 Range requests;
- max 5 HTTP requests total;
- max 131072 response bytes/range;
- max 524288 source response-body bytes total;
- max 262144 transient uncompressed bytes/member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes/logical record;
- no additional range;
- no full-body fallback;
- no automatic widening;
- no automatic retry.

## Validation / D-008 boundary

Validation remains exactly:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, normalization, regex relaxation, parser change or projector change is authorized.

If `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs, the exact fail-closed mapping remains:

- `semantic_result_status = STOPPED_FAIL_CLOSED`;
- `stop_reason = PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- `control_disposition.status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `control_disposition.reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- source continuation = `false`;
- no silent row skip.

## Privacy / persistence authorization

The privacy approval authorizes only transient in-memory full-row observation required to project `PROPERTY_TYPE` during this one bounded execution.

Boundary:

- memory-only;
- zero retention days;
- immediate disposal;
- no raw-body persistence;
- no full-row persistence;
- no `PROPERTY_ID`, owner/holder or per-row `PROPERTY_TYPE` persistence;
- no offending bytes/hash/exact-length persistence;
- no record values in logs;
- no real-row quarantine;
- no row-specific human inspection;
- persisted `control_disposition` limited to `status_code` and `reason_code`;
- only the reviewed derived-summary allowlist may persist.

No privacy expansion is authorized.

## Product/source separation

This gate does not approve the source for production and does not open identity, genealogy, beneficiary matching, outreach or claims.

`DECISIONS.md` remains unchanged.

## Next action

Execute immediately and exclusively:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

After the single execution, remove the temporary workflow/trigger, consume both approval refs, preserve only permitted derived evidence, and move directly to evidence review/source decision.