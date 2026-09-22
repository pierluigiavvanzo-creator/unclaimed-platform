# M3 California SCO `$500+` PROPERTY_TYPE Semantic Verification Proposal

Date: 2026-09-15

Status: **CANDIDATE PROPOSAL — NON-AUTHORIZING — NO SCO NETWORK/BODY ACCESS**

## Purpose

Define the smallest deterministic future experiment needed to test whether the bulk CSV `PROPERTY_TYPE`
field can safely support the already-canonical `INSURANCE_RELEVANCE_TRIAGE_ONLY` purpose.

This task is design/contract/test only. It does not execute a network request, read a real data row,
approve the source, authorize PII, enable the registry, perform matching, or permit outreach.

## Evidence reused

The proposal reuses:

- canonical `$500+` structure evidence:
  `sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`;
- canonical two-field field/privacy boundary:
  `sources/proposals/ca_sco_segment_500_plus.field_privacy_readiness.v1.json`;
- existing fail-closed SCO source policy and disabled registry;
- the official California SCO NAUPA code document:
  `https://www.sco.ca.gov/Files-UPD/upd_naupa_II_codes_dormancy_periods.pdf`.

The official document states that the listed NAUPA standard codes are used by California and identifies
the insurance property codes `IN01-IN08` and `IN99`.

No new SCO source-body request was made while preparing this proposal.

## Exact semantic question

The future bounded experiment asks only:

> In a deterministic prefix sample across all four canonical CSV members, are `PROPERTY_TYPE` values
> NAUPA-style code tokens, and is every observed `IN`-prefixed value one of the official California
> SCO insurance codes `IN01-IN08` or `IN99`?

This is intentionally a **sample-only** question. Even a successful sample must not be described as proof
of the full dataset's code domain, frequency distribution, or global absence of malformed values.

## Sampling boundary

The future execution proposal fixes:

- four canonical CSV members;
- first four complete data records after the already-verified header from each member;
- maximum 4 data rows/member;
- maximum 16 data rows total;
- prefix sampling only;
- no claim of statistical representativeness.

A future successful implementation must verify the exact canonical header before parsing any data row.

## Network and byte caps

Project safety caps, not source facts:

- HTTPS only;
- exact host `claimit.ca.gov`;
- redirects denied;
- `If-Match` required against the canonical ETag;
- one HEAD request maximum;
- four Range GET requests maximum;
- five HTTP requests total maximum;
- `131,072` response-body bytes maximum per member Range;
- `524,288` source response-body bytes maximum in total;
- `262,144` uncompressed transient bytes maximum per member;
- `1,048,576` uncompressed transient bytes maximum total;
- `32,768` bytes maximum per logical CSV record;
- no full-body request;
- no additional Range request if a member sample is incomplete within the prefix cap.

Any need to widen a row/request/byte cap requires a new proposal and another human gate.

## Privacy boundary

CSV transport still matters. Reading a row may transiently expose prohibited owner/holder columns before
local projection. Therefore this proposal does **not** remove the canonical transient-row privacy blocker.

A future execution requires a separate explicit transient-row privacy approval.

If later approved, the execution design would:

- hold source bytes only in memory;
- create no temporary source file;
- persist no raw ZIP, Range body, full row, owner/holder value, or `PROPERTY_ID`;
- use no nonallowlisted field value;
- dispose transient buffers immediately after projection or STOP;
- persist only a derived `PROPERTY_TYPE` summary, not per-row records;
- write no raw bytes or record values to logs.

## Derived evidence allowed

Only the following derived summary fields may be persisted:

- sample rows examined;
- rows examined per member;
- distinct observed `PROPERTY_TYPE` codes;
- distinct observed official insurance codes;
- semantic result status;
- stop reason.

Per-row `PROPERTY_TYPE` values and `PROPERTY_ID` are not persisted by this proposal.

## Semantic outcomes

`SAMPLE_COMPATIBLE_INSURANCE_CODE_OBSERVED`

Requires:

- at least one complete data row from every canonical member;
- every observed `PROPERTY_TYPE` token matches the bounded code-shape rule;
- at least one official insurance code is observed;
- every observed `IN`-prefixed token is one of `IN01-IN08` or `IN99`.

`SAMPLE_CODE_SHAPE_COMPATIBLE_NO_INSURANCE_CODE_OBSERVED`

Means the bounded sample was code-shaped but contained no `IN`-prefixed value. This is explicitly
inconclusive for the insurance mapping and cannot activate production classification.

`STOPPED_FAIL_CLOSED`

Used on any deterministic stop condition.

Even the success status does not activate production classification or real acquisition.

## Fail-closed stop conditions

The proposal stops on:

- transport metadata drift;
- Range response not `206`;
- content-range mismatch;
- canonical member metadata mismatch;
- header mismatch;
- malformed CSV;
- row column-count mismatch;
- empty `PROPERTY_TYPE`;
- unexpected code shape;
- unrecognized `IN`-prefixed code;
- logical record limit exceeded;
- transient decompression limit exceeded;
- sample incomplete within the fixed member-prefix cap;
- row/request/byte cap exhaustion;
- missing transient-row privacy approval;
- unexpected response-body behavior.

## No execution implementation

This candidate intentionally does **not** introduce:

- `scripts/ca_sco_property_type_semantic_verification.py`;
- `.github/workflows/ca-sco-property-type-semantic-verification-once.yml`.

Contract tests require both to remain absent.

## Files

- `schemas/common/property_type_semantic_verification_proposal.schema.json`
- `schemas/examples/ca_sco_500_plus_property_type_semantic_verification.examples.json`
- `sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`
- `tests/contract/test_ca_sco_property_type_semantic_verification_proposal.py`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL.md`

## Next gate

After candidate CI:

**HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW**

Promotion of this proposal, if authorized later, remains non-authorizing. A separate owner decision is
required before implementation/execution can read even one real CSV data row.
