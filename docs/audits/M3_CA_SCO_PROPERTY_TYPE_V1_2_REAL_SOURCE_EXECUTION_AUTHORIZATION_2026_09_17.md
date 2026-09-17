# M3 California SCO — PROPERTY_TYPE v1.2 Real-Source Execution Authorization — 2026-09-17

Date: 2026-09-17

Status: **HUMAN/OWNER AUTHORIZATION COMPLETED — PASS — FRESH SINGLE-USE EXECUTION + PRIVACY APPROVALS GRANTED — ONE-SHOT PATH AUTHORIZED — EXECUTION NOT PERFORMED BY THIS RECORD**

## Authorization gate

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_AUTHORIZATION`

## Owner authorization

Owner instruction received verbatim:

`APPROVO FRESH SINGLE-USE EXECUTION + TRANSIENT-ROW PRIVACY`

This authorization grants exactly one bounded real-source semantic execution and exactly one transient-row memory-only privacy approval under the frozen reviewed proposal boundary. It does not itself perform network access.

## Authoritative checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- authorization base branch: `m3-ca-sco-v1-2-proposal-contract-preservation-remediation`
- authorization base HEAD: `c18cddfc92bf3bb69f40b76170e687136e7fd21a`
- authorization base CI: `35221904089` — **SUCCESS**
- reviewed proposal checkpoint: `ed6a22a3ed5c727b3b4dd7f14416bb06acab2903`
- proposal review result: `PASS_REMEDIATED_V1_2_REAL_SOURCE_EXECUTION_PROPOSAL_ACCEPTED_FOR_FRESH_SINGLE_USE_AUTHORIZATION`
- proposal id: `ca.sco.segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution`
- proposal version: `1.1.0`
- proposal path: `sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling_policy_v1_2_real_source_execution.v1_1.json`
- runtime contract: `1.2.0`
- governing decision: `D-008 — WHOLE_SOURCE_STOP`

## Fresh approval references

Execution approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_REAL_SOURCE_EXECUTION_BOUNDED_ED6A22A3`

Transient-row privacy approval:

`OWNER_APPROVAL_2026-09-17_CA_SCO_PROPERTY_TYPE_V1_2_TRANSIENT_ROW_PRIVACY_BOUNDED_ED6A22A3`

Both approvals are:

- status: `GRANTED_NOT_CONSUMED`;
- fresh: `true`;
- single-use: `true`;
- reusable: `false`;
- bound to proposal version `1.1.0`;
- bound to reviewed proposal checkpoint `ed6a22a3ed5c727b3b4dd7f14416bb06acab2903`;
- bound to runtime contract `1.2.0`;
- not substitutes for and not derived from any consumed historical approval.

They become `CONSUMED_SINGLE_USE_NON_REUSABLE` when the authorized runner first invokes the real source. No retry is authorized under these refs.

## Authorized execution boundary

The later one-shot execution may use only:

- 4 canonical members;
- max 4 data rows/member and 16 total;
- max 1 HEAD, 4 Range, 5 HTTP requests total;
- max 131072 response bytes/range;
- max 524288 source response-body bytes total;
- max 262144 transient uncompressed bytes/member;
- max 1048576 transient uncompressed bytes total;
- max 32768 bytes/logical record;
- no extra Range;
- no full-body fallback;
- no automatic widening;
- no automatic retry.

Validation remains exactly `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`. No trimming, case conversion, normalization, regex relaxation, parser change or projector change is authorized.

D-008 remains fail closed. If `PROPERTY_TYPE_FORMAT_UNEXPECTED` occurs, the only permitted control disposition is:

- `status_code = PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- `reason_code = PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- no later source continuation.

## Privacy boundary

The privacy approval authorizes only transient in-memory full-row observation required to project `PROPERTY_TYPE` during this single run.

Not authorized for persistence:

- raw body;
- full row;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE`;
- offending bytes/value hash/exact field length;
- row-specific inspection or quarantine.

Persisted evidence is limited to the already reviewed derived execution summary and non-value-bearing control-disposition fields.

## Source / product separation

This authorization does not activate the source, registry, production classification, identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Next action

Proceed directly to exactly one:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

Create a temporary branch-pinned workflow, validate authorization and frozen boundaries before source access, perform at most one live execution, upload/persist only contract-approved derived evidence, consume both refs on first live invocation, remove the workflow and trigger immediately after the run, then perform evidence review/source decision.