# M3 California SCO — PROPERTY_TYPE Source-Format Diagnostic Proposal Review

Date: 2026-09-16

## Classification

D — Diagnostic / Technical / Privacy.

## Review gate

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW`

## Result

`PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`

The source-format diagnostic proposal design is acceptable for progression to preparation of a separate execution/authorization artifact. This PASS approves **design only**. It does not authorize source access, authority access, real full-row exposure, workflow creation, diagnostic execution, parser/regex/runtime changes, remediation, source approval, registry activation or downstream work.

## Package reviewed

Proposal branch:

`m3-ca-sco-property-type-source-format-diagnostic-proposal`

Proposal package checkpoint:

`d8dc240bd74e271f88b2ef4583f6b79e533918b2`

Package CI:

`35060253297` — SUCCESS

Final proposal-state HEAD reviewed:

`5e0aa6fa8bc9516c2cd8447e26e3b76b7485c4e9`

Final proposal-state CI:

`35060418377` — SUCCESS

Reviewed durable artifacts:

- `sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic.v1.json`
- `schemas/common/property_type_source_format_diagnostic_proposal.schema.json`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL.md`
- `tests/contract/test_ca_sco_property_type_source_format_diagnostic_proposal.py`

## Review findings

### 1. Source boundary remains bounded

The proposal does not widen the previously reviewed request/byte envelope. Any future execution artifact may be no wider than:

- exact pinned current source endpoint and source identity;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced target mismatch;
- maximum 1 full-row independent cross-check on that first mismatch row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- no redirects;
- no additional ranges;
- no full-body fallback;
- no automatic widening.

The proposal itself authorizes no network access.

### 2. Full-row privacy expansion is explicit and appropriately gated

A future `csv.reader` comparison would transiently decode all fields in one real logical row and therefore may expose personal data in memory. The proposal correctly treats this as a new privacy expansion rather than silently inheriting the prior narrow-field privacy approval.

The proposed design limits that expansion to one mismatch row and requires, before any future network request:

1. a separately reviewed execution/authorization artifact;
2. a fresh single-use execution approval;
3. a separate fresh single-use full-row transient privacy approval;
4. both approvals pinned to the exact reviewed execution artifact.

No approval token is defined or granted by this review.

### 3. Persistence/logging boundary is acceptable

The proposal forbids persistence or logging of:

- the full row;
- any row field value;
- PROPERTY_TYPE value or bytes;
- hashes or exact lengths of row/field;
- fragments or codepoints;
- transformed values;
- PROPERTY_ID;
- owner/holder values;
- parser exception text;
- source-derived free text.

Only bounded counters, safety flags and one categorical source-format outcome may be durable if a future execution is separately authorized.

### 4. Independent parser role is correctly limited

The proposed Python standard-library `csv.reader` comparator is diagnostic only. It does not replace the current projector, does not normalize values, does not change the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`, and cannot make a source value acceptable.

The five proposed outcomes are non-value-bearing and none automatically authorizes remediation:

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

### 5. Authority branch remains closed

The archived SCO authority already resolved the targeted provenance questions within the recorded proof boundary. The source-format proposal creates no new authority-specific contradiction and correctly authorizes no additional authority retrieval.

## Mandatory tightening for the future execution/authorization artifact

A PASS on this proposal is conditional on the next artifact making the following execution semantics deterministic. These tightenings must not widen the reviewed scope.

### T-1 — Exact classifier precedence

The future execution artifact must define one fixed first-match precedence in this exact order:

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

No implementation-dependent reordering is allowed.

### T-2 — Same logical-row bytes, no re-read

The independent comparator must consume exactly the same transient logical-record bytes already assembled in memory for the first row that reproduces `ASCII_STRUCTURAL_MISMATCH`. It must not issue another source request, additional Range request or other re-read to obtain comparator input.

### T-3 — Exact stdlib newline / multiline framing

The execution artifact must pin the exact standard-library invocation semantics for embedded newline/CRLF handling rather than relying only on the words `csv.reader(strict=True)`. The design must use a deterministic text-stream framing equivalent to Python `io.StringIO(decoded_row, newline="")` feeding `csv.reader` with the already pinned dialect, or an equivalently explicit standard-library construction proven by synthetic regression tests.

This requirement exists to avoid an implementation-dependent result for valid quoted multiline fields.

### T-4 — Exactly one independent parsed record

The independent comparator must consume the one transient logical row and produce exactly one CSV record. Zero records or more than one record must stop fail-closed under an enumerated non-source-bearing reason code; they must not be silently mapped to a data class and must not persist parser exception text or source content.

### T-5 — Enumerated fail-closed reasons

The execution artifact must enumerate all non-classification fail-closed reason codes required by its control flow, including at least source identity drift, target mismatch not reproduced within bound, and independent-parser record-count/framing failure. Free-text error output remains forbidden.

## What this review does not authorize

This review does **not** authorize:

- `claimit.ca.gov` access;
- SCO authority access;
- real full-row inspection;
- creation of a network workflow;
- creation/grant/consumption of execution or privacy approvals;
- parser or runner changes;
- regex changes or relaxation;
- trimming, casing or normalization;
- logging or persistence expansion;
- remediation;
- source approval;
- registry activation;
- production classification;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.

All prior approvals remain consumed and permanently non-reusable.

## Safety state

Unchanged:

- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- production classification: inactive;
- semantic compatibility: unresolved;
- parser/regex/runtime normalization: unchanged;
- downstream identity/genealogy/matching/outreach/claim gates: BLOCKED.

## Next gate

The next permissible action is preparation only, offline, of a separate source-format diagnostic execution/authorization artifact incorporating T-1 through T-5.

Recommended next action:

`PREPARE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_ARTIFACT`

Preparation of that artifact must not perform network access or full-row exposure and must not silently define granted approvals. Any approval tokens introduced by that artifact remain ungranted until a later human authorization gate.