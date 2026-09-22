# M3 California SCO — PROPERTY_TYPE Source-Format Diagnostic Proposal

Date: 2026-09-16

Status: **PROPOSAL ONLY — NOT AUTHORIZED FOR NETWORK, FULL-ROW EXPOSURE, EXECUTION OR REMEDIATION**

## Purpose

Design the smallest next diagnostic that could distinguish a source-format/projector divergence from a structural source-field mismatch after the completed bounded diagnostic classified the first reproduced mismatch as:

`ASCII_STRUCTURAL_MISMATCH`

This task is proposal preparation only. It performs no source or authority request and no real-row inspection.

## Verified base

- review branch: `m3-ca-sco-property-type-diagnostic-evidence-review`
- review HEAD: `9195d27e17b89703f7179a9db2ba5dccad43a75e`
- review CI: `35058889923` — SUCCESS
- diagnostic run: `35019840276` — SUCCESS
- diagnostic evidence: `sources/evidence/ca_sco_segment_500_plus.property_type_diagnostic.execution.v1.json`
- diagnostic class: `ASCII_STRUCTURAL_MISMATCH`
- diagnostic evidence review decision: `PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`

The exact source `PROPERTY_TYPE` value, bytes, hash, exact length, fragments, codepoints and transformed form remain unretained and must not be reconstructed or inferred.

## Why source-format is the next justified branch

The completed classifier already excluded a mismatch explained solely by surrounding ASCII SPACE/TAB, ASCII case, their combination, or non-ASCII/disallowed-control content.

The archived SCO authority has already resolved the targeted authority provenance for the enumerated `AA99` shape (with the recorded scope boundary), `ZZZZ`, and `IN01-IN08` / `IN99`. Current evidence creates no new authority-specific contradiction.

Repository synthetic differential tests already show that the current narrow projector agrees with Python `csv.reader(..., strict=True)` across the committed standard-CSV edge-case matrix. That synthetic evidence is useful but does not prove that the real source row is parsed identically by both mechanisms.

Accordingly, the smallest remaining discriminating test would be an independent parser cross-check of only the first real row that reproduces the already-established `ASCII_STRUCTURAL_MISMATCH` condition.

## Proposed future source boundary — not authorized now

If a later separately reviewed and authorized execution artifact is created, it may be no wider than:

- exact existing `claimit.ca.gov` endpoint and pinned source identity;
- first canonical ZIP member only;
- at most 4 transient data rows while seeking the first reproduced target mismatch;
- at most 1 full-row independent cross-check, and only on that first reproduced mismatch row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes total;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- redirects forbidden;
- additional ranges forbidden;
- full-body fallback forbidden;
- automatic widening forbidden;
- source identity drift or failure to reproduce the target mismatch -> fail closed.

This proposal itself grants none of those permissions.

## Independent parser contract

A future execution artifact would have to pin the independent parser before network access:

- implementation: Python standard-library `csv.reader`;
- `strict=True`;
- delimiter `,`;
- quote character `"`;
- `doublequote=True`;
- no escape character;
- `skipinitialspace=False`;
- strict UTF-8 row decode;
- exactly 25 canonical columns expected;
- `PROPERTY_TYPE` at zero-based index `1`;
- current narrow projector unchanged;
- current regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no Unicode normalization;
- no accepted value substitution or runtime remediation.

The independent parser is a diagnostic comparator only, not a replacement parser.

## Explicit privacy expansion

A full-row `csv.reader` cross-check is materially different from the previous narrow-field diagnostic because it would transiently decode all fields in one real row, which may include personal data.

Therefore:

- full-row transient exposure is explicitly classified as a privacy expansion;
- this proposal does **not** authorize it;
- a future execution requires a fresh execution approval and a separate fresh full-row transient privacy approval;
- those approvals must be single-use, non-reusable and pinned to the exact reviewed execution artifact;
- this proposal defines no approval token.

Even if later authorized, only one mismatch row may undergo full-row parsing in memory. The row and all of its fields must be discarded without persistence or logging.

Forbidden persistence includes:

- full row;
- any row field value;
- `PROPERTY_TYPE` value or bytes;
- hashes or exact lengths of the row or field;
- fragments or codepoints;
- transformed values;
- `PROPERTY_ID`;
- owner/holder values;
- parser exception text derived from source data;
- source-derived free text.

## Proposed future categorical outcomes

Only these non-value-bearing classes are proposed:

1. `FULL_ROW_UTF8_DECODE_FAILED`
2. `STDLIB_STRICT_CSV_PARSE_FAILED`
3. `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
4. `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
5. `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

Each class is a diagnostic branch only. None automatically authorizes remediation.

### Interpretation boundary

- `FULL_ROW_UTF8_DECODE_FAILED` would justify only a separate encoding/format evidence proposal.
- `STDLIB_STRICT_CSV_PARSE_FAILED` would justify only a separate dialect/format evidence proposal.
- `STDLIB_COLUMN_SHAPE_NOT_CANONICAL` would justify only a separate schema/format evidence proposal.
- `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER` could justify considering a separate offline projector-remediation proposal, but would not authorize changing the parser.
- `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH` would mean both parsers agree on the selected field and it still fails the unchanged regex; that could justify a separate source-code-domain/source-evolution evidence proposal, not regex relaxation.

## Reuse assessment

No new dependency is proposed. The design reuses:

- the existing narrow projector;
- the existing source identity and ZIP bounds;
- Python standard-library `csv.reader`, already used in the repository's synthetic differential matrix;
- the existing current regex unchanged.

No external package or repository is required for proposal preparation.

## Authorization state

This proposal authorizes only its own offline preparation.

It does **not** authorize:

- source access;
- authority retrieval;
- full-row transient exposure;
- network workflow creation;
- diagnostic execution;
- parser or runner change;
- regex change or relaxation;
- trimming/casing/normalization;
- logging or persistence expansion;
- remediation;
- source approval;
- registry activation;
- production classification;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.

All five historical execution/privacy/authority approvals recorded by the proposal remain consumed and non-reusable.

## Durable package

- proposal: `sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic.v1.json`
- schema: `schemas/common/property_type_source_format_diagnostic_proposal.schema.json`
- contract test: `tests/contract/test_ca_sco_property_type_source_format_diagnostic_proposal.py`

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW`

Human review must decide whether the design and its explicit full-row privacy expansion are acceptable. A PASS would still not authorize network execution or full-row exposure; a separate execution/authorization artifact with fresh approvals would be required.
