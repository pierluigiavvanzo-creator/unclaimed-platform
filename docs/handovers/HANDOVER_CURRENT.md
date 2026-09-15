# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Use repository evidence, not conversational memory.

## Repository / Branches

- Repository: `pierluigiavvanzo-creator/unclaimed-platform`
- Stable branch: `main`
- Canonical development branch: `m2-state-governance-core`
- Canonical housekeeping HEAD before current candidate: `830aaaed68bd4d2f9298eaede80b5e67918e935b`
- Current candidate: `m3-ca-sco-property-type-semantic-verification-proposal`
- Functional candidate HEAD: `6a39502a19f2127b154b95bf0014a8c76c5ae752`
- Functional candidate CI: `34942475352` — SUCCESS
- Stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e` — unchanged
- Never develop directly on `main`.

The canonical housekeeping HEAD contains no functional change relative to the prior verified closure:
temporary setup files were created and immediately removed, leaving the canonical content tree unchanged.

## Verified Baseline

- M0 VERIFIED.
- M1 VERIFIED.
- M2 VERIFIED.
- M3 California source/legal readiness COMPLETE.
- M3 acquisition/raw persistence/privacy CANONICAL + VERIFIED.
- Streamlit reviewer CANONICAL + CI VERIFIED.
- SCO source governance CANONICAL + CI VERIFIED.
- SCO transport/source-approval/data-scope readiness CANONICAL + CI VERIFIED.
- SCO segmented transport evidence CANONICAL + CI VERIFIED.
- SCO `$500+` bounded structure inspection EXECUTED + CANONICAL + CI VERIFIED.
- SCO two-field field/privacy boundary CANONICAL + CI VERIFIED.
- Repository-side Vercel integration DECOMMISSIONED.
- Supabase untouched.

## Canonical `$500+` Structure Evidence

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Prior owner-authorized structure-only run:
`34864433849` — SUCCESS.

Observed:
- four non-encrypted DEFLATED CSV members;
- identical 25-label header candidate;
- member local-header offsets evidenced;
- 5 HTTP `206` Range responses in that prior structure-only run;
- total source-body bytes `393,216`;
- full archive downloaded false;
- CSV data rows parsed `0`;
- record values persisted false.

No real data row has yet been sampled.

## Canonical Product Purpose / Field Boundary

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Canonical proposed persisted/allowed first-purpose scope:
1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

`HOLDER_NAME`, owner identity/address and holder identity/address fields remain prohibited for first
triage.

Official California SCO NAUPA documentation states that the listed NAUPA codes are used by California and
defines insurance codes:
`IN01`, `IN02`, `IN03`, `IN04`, `IN05`, `IN06`, `IN07`, `IN08`, `IN99`.

Authority:
`https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`.

## Current Candidate — PROPERTY_TYPE Semantic Verification Proposal

Files:
- `schemas/common/property_type_semantic_verification_proposal.schema.json`
- `schemas/examples/ca_sco_500_plus_property_type_semantic_verification.examples.json`
- `sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`
- `tests/contract/test_ca_sco_property_type_semantic_verification_proposal.py`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL.md`

Proposal status:
`PROPOSAL_ONLY_NOT_AUTHORIZED`.

No new SCO network request or source-body access occurred.

No execution runner exists:
`scripts/ca_sco_property_type_semantic_verification.py` — ABSENT.

No one-shot network workflow exists:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml` — ABSENT.

Contract tests enforce both absences.

## Exact Semantic Question

In a deterministic bounded prefix sample across all four canonical CSV members:

1. are observed `PROPERTY_TYPE` values NAUPA-style code tokens; and
2. is every observed `IN`-prefixed value one of official SCO insurance codes `IN01-IN08` or `IN99`?

Proof boundary:
`SAMPLE_ONLY_DOES_NOT_PROVE_FULL_DATASET_DOMAIN_OR_GLOBAL_CODE_FREQUENCY`.

Even a future success cannot activate production classification.

## Deterministic Sampling Plan

Selection:
`FIRST_COMPLETE_DATA_ROWS_AFTER_VERIFIED_HEADER_PER_CANONICAL_MEMBER`.

Canonical members and local-header offsets:
1. `From_500_To_Beyond_1_of_4.csv` — `0`
2. `From_500_To_Beyond_2_of_4.csv` — `59,747,797`
3. `From_500_To_Beyond_3_of_4.csv` — `96,862,896`
4. `From_500_To_Beyond_4_of_4.csv` — `134,174,190`

Caps:
- max 4 data rows/member;
- max 16 data rows total;
- header is not a data row;
- prefix sample only;
- no statistical representativeness claim.

Before any data row, a future runner must verify the exact canonical 25-column header.

## Transport / Byte Caps

Future execution design is fixed to:
- endpoint `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- HTTPS only;
- host `claimit.ca.gov`;
- redirects denied;
- exact canonical Content-Length `162,416,884`;
- exact canonical ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- `Accept-Ranges: bytes`;
- `If-Match` required;
- network inactivity timeout 10 seconds;
- max 1 HEAD request;
- max 4 Range GET requests;
- max 5 HTTP requests total;
- max `131,072` body bytes per Range;
- max `524,288` source body bytes total;
- max `262,144` uncompressed transient bytes/member;
- max `1,048,576` uncompressed transient bytes total;
- max `32,768` bytes/logical CSV record;
- full-body request false;
- no additional Range when a sample is incomplete within cap.

These are project safety caps, not source facts. Widening requires a new proposal and human gate.

## Row Processing Rules

- expected column count `25`;
- header must match canonical labels exactly;
- `PROPERTY_TYPE` zero-based column index `1`;
- bounded code-shape rule `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- any observed `IN`-prefixed value must be one of the nine official insurance codes;
- non-insurance code semantics are not claimed by this proposal;
- `PROPERTY_ID` use false during semantic verification;
- nonallowlisted field use false;
- nonallowlisted persistence false;
- full-row persistence false.

## Privacy / Persistence Boundary

The source is CSV and no server-side column projection is established. A future row read may transiently
expose prohibited owner/holder bytes.

Therefore a separate transient-row privacy approval remains mandatory before execution.

Allowed future persistence is only a derived summary:
- number of sample rows examined;
- rows examined/member;
- distinct observed `PROPERTY_TYPE` codes;
- distinct observed official insurance codes;
- semantic result status;
- stop reason.

Explicitly not persisted:
- raw ZIP;
- raw Range body;
- full row;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE` values.

Transient buffers:
- retention `0 days`;
- disposal `IMMEDIATE_AFTER_PROJECTION_OR_STOP`.

Logs:
- no raw bytes;
- no record values;
- no owner/holder values;
- no `PROPERTY_ID`;
- no per-row `PROPERTY_TYPE`.

## Semantic Outcomes

`SAMPLE_COMPATIBLE_INSURANCE_CODE_OBSERVED`
- all observed values match bounded code shape;
- at least one complete row comes from every member;
- at least one official insurance code is observed;
- every observed `IN`-prefixed value is official.

`SAMPLE_CODE_SHAPE_COMPATIBLE_NO_INSURANCE_CODE_OBSERVED`
- code-shape checks pass;
- no `IN`-prefixed value is observed;
- outcome is explicitly inconclusive for insurance mapping.

`STOPPED_FAIL_CLOSED`
- any deterministic stop condition triggers.

Production activation remains false for all outcomes.

## Stop Conditions

- transport metadata drift;
- Range response not partial;
- content-range mismatch;
- member metadata mismatch;
- header mismatch;
- CSV parse error;
- row column-count mismatch;
- empty or malformed `PROPERTY_TYPE`;
- unrecognized `IN`-prefixed code;
- logical-record/transient decompression cap exceeded;
- incomplete sample inside fixed member prefix;
- row/request/byte cap exceeded;
- privacy approval missing;
- unexpected response-body behavior.

## Candidate Verification

Functional HEAD:
`6a39502a19f2127b154b95bf0014a8c76c5ae752`.

CI:
`34942475352` — SUCCESS for both `quality` and `streamlit-candidate`.

Passed:
- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- frontend install/lint/typecheck/build;
- Streamlit safety/startup smoke.

Tests verify:
- proposal remains non-authorizing and unexecuted;
- runner/workflow remain absent;
- row/request/byte caps are exact;
- canonical member offsets and transport identity match existing evidence;
- persistence is derived-summary-only;
- source policy and registry remain fail closed;
- execution and cap widening are schema-invalid.

## Canonical Authorization State — UNCHANGED

SCO source policy remains:
- `status: PROPOSED`;
- `real_acquisition_authorized: false`;
- `authorized_processing_purposes: []`;
- `allowed_fields: []`;
- `allow_pii: false`.

Registry remains:
- `enabled: false`;
- `approved_for_use: false`.

Approved real sources: `0`.

Real row access, PII processing, identity resolution, beneficiary matching and outreach remain BLOCKED.

## SINGLE NEXT ACTION

**HUMAN PROMOTION GATE ONLY**

Decide whether to promote:

`m3-ca-sco-property-type-semantic-verification-proposal -> m2-state-governance-core`

Promotion must remain non-authorizing and must not implement or execute a network runner.

After promotion and canonical CI, the next separate gate is:

`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`

That later gate must still distinguish implementation/review of a bounded runner from actual one-shot
execution that reads real rows.

## Handover Status

```text
M0: VERIFIED
M1: VERIFIED
M2: VERIFIED
M3 SCO $500+ structure: CANONICAL + CI VERIFIED
M3 two-field privacy boundary: CANONICAL + CI VERIFIED
Canonical base for candidate: 830aaaed68bd4d2f9298eaede80b5e67918e935b
Current candidate: m3-ca-sco-property-type-semantic-verification-proposal
Functional candidate SHA: 6a39502a19f2127b154b95bf0014a8c76c5ae752
Functional candidate CI: 34942475352 SUCCESS
Semantic rows cap: 16 total / 4 per member
Range requests cap: 4
Source body cap: 524288 bytes
Full-body request: false
Runner: ABSENT
Network workflow: ABSENT
New SCO network/body access: 0
Real acquisition: BLOCKED
Real row access: BLOCKED
Real PII: BLOCKED
Matching: BLOCKED
Outreach: BLOCKED
SCO policy: PROPOSED
SCO registry: DISABLED + NOT APPROVED
Approved real sources: 0
main: bfddf8ee3ef32eedb91af888c998ef72f5cdd15e UNCHANGED
NEXT: human promotion gate only
CONTEXT HEALTH: coherent; repository is source of truth
```
