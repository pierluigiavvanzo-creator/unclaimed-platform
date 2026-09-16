# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The live-source mismatch was classified by one bounded diagnostic execution as `ASCII_STRUCTURAL_MISMATCH`, human evidence review passed, and a separate source-format diagnostic proposal has now been prepared offline and CI-verified. Semantic compatibility remains unresolved and no runtime remediation is authorized.

Diagnostic execution run:
`35019840276` — SUCCESS

Diagnostic evidence review decision:
`PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`

Source-format proposal branch:
`m3-ca-sco-property-type-source-format-diagnostic-proposal`

Source-format proposal package checkpoint:
`d8dc240bd74e271f88b2ef4583f6b79e533918b2`

Source-format proposal CI:
`35060253297` — SUCCESS

Proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic.v1.json`

Schema:
`schemas/common/property_type_source_format_diagnostic_proposal.schema.json`

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL.md`

Contract test:
`tests/contract/test_ca_sco_property_type_source_format_diagnostic_proposal.py`

## Proposal State

Status:
`PROPOSAL_ONLY_NOT_AUTHORIZED`

The proposal designs a possible future independent source-format cross-check only. It performs no source request, authority request, full-row source access, diagnostic execution, workflow creation, parser change, regex change, normalization change, logging expansion, persistence expansion or remediation.

The future design preserves the existing bounded source limits:

- exact pinned endpoint and source identity only;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced target mismatch;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries, redirects, additional ranges, full-body fallback or automatic widening.

## Explicit Full-Row Privacy Expansion — Not Authorized

The proposed independent comparator is Python standard-library `csv.reader(..., strict=True)` with the canonical comma/quote dialect, strict UTF-8 row decode, exactly 25 expected columns and `PROPERTY_TYPE` at zero-based index `1`.

Using it on a real row would transiently decode the full row, which may include personal data. The proposal therefore treats this as an explicit privacy expansion and limits any future cross-check to **one** mismatch row.

The proposal does not authorize that exposure. A later execution requires:

- a fresh, separately reviewed execution artifact;
- a fresh single-use execution approval;
- a separate fresh single-use full-row transient privacy approval;
- both approvals pinned to the exact reviewed execution artifact before network access.

This proposal defines no approval token.

Even if later authorized, no full row, field value, PROPERTY_TYPE, bytes, hash, exact length, fragment, codepoint, transformed value, PROPERTY_ID, owner/holder value, row hash, row exact length, parser exception text or source-derived free text may persist or be logged.

## Proposed Future Diagnostic Classes

Only these non-value-bearing classes are designed:

- `FULL_ROW_UTF8_DECODE_FAILED`
- `STDLIB_STRICT_CSV_PARSE_FAILED`
- `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
- `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
- `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

No class automatically authorizes remediation.

## Approval State

All prior execution/privacy/authority approvals remain `CONSUMED` and permanently non-reusable, including:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

## Safety / Governance State

- parser unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- source-format diagnostic execution authorized: `false`;
- full-row transient privacy exposure authorized: `false`;
- network workflow authorized: `false`;
- remediation authorized: `false`;
- additional authority retrieval authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Perform only:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW`

Review the design, especially the explicit one-row full-row transient privacy expansion. A PASS would approve only the proposal design; it would not authorize source access, full-row exposure or execution.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
