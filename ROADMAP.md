# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | SOURCE-FORMAT DIAGNOSTIC PROPOSAL PREPARED; HUMAN REVIEW REQUIRED | proposal checkpoint `d8dc240b...18b2`; CI `35060253297` SUCCESS |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` previously stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- one-shot diagnostic run `35019840276`: SUCCESS;
- diagnostic result `DIAGNOSTIC_CLASSIFIED`;
- diagnostic class `ASCII_STRUCTURAL_MISMATCH`;
- diagnostic evidence review decision: `PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`;
- exact source value and protected derivatives remain unretained;
- no remediation performed;
- source-format diagnostic proposal prepared offline;
- proposal package checkpoint `d8dc240bd74e271f88b2ef4583f6b79e533918b2`;
- proposal CI `35060253297`: SUCCESS;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Source-Format Diagnostic Proposal

The proposal is design-only and remains:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

It proposes a future independent parser comparison only after a separately reviewed execution artifact and fresh approvals.

The source/request bounds do not widen:

- exact pinned endpoint and identity;
- first canonical member only;
- maximum 4 transient rows while reproducing the target mismatch;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retry/redirect/additional range/full-body fallback/automatic widening.

The independent comparator is pinned to Python standard-library `csv.reader(..., strict=True)`, canonical comma/quote settings, strict UTF-8 decode, 25 columns and zero-based field index `1`. The current custom projector and regex remain unchanged.

## Privacy Boundary

A real-row `csv.reader` comparison would transiently decode all fields in one row and is therefore explicitly treated as a privacy expansion.

The proposal limits any future full-row cross-check to one mismatch row but does **not** authorize it. A later execution requires fresh single-use execution and full-row transient privacy approvals pinned to the exact reviewed execution artifact.

No source value, full row, field value, hash, exact length, fragment, codepoint, transformed value, PROPERTY_ID, owner/holder value, parser exception text or source-derived free text may persist or be logged.

No approval token is defined by this proposal.

## Proposed Future Classes

- `FULL_ROW_UTF8_DECODE_FAILED`
- `STDLIB_STRICT_CSV_PARSE_FAILED`
- `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
- `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
- `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

None authorizes remediation automatically.

## Next Product Work

Perform only:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW`

The review must decide whether the design and explicit one-row full-row privacy expansion are acceptable. A review PASS still must not be treated as execution/privacy approval.

## Still Out of Scope

- reuse of any consumed approval;
- source or authority network access under the proposal;
- real full-row exposure before a fresh privacy approval;
- source-value reconstruction or inference;
- exact source-value or row hashing/length capture, fragments or codepoints;
- parser or regex changes;
- trimming, casing or normalization runtime changes;
- Unicode normalization;
- automatic remediation;
- new authority retrieval at this checkpoint;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
