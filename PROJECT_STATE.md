# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The live-source mismatch was classified by one bounded diagnostic execution as `ASCII_STRUCTURAL_MISMATCH`; human evidence review passed; the separate source-format diagnostic proposal was prepared offline, CI-verified, and has now completed human proposal review. Semantic compatibility remains unresolved and no runtime remediation is authorized.

Diagnostic execution run:
`35019840276` — SUCCESS

Diagnostic evidence review decision:
`PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`

Source-format proposal package checkpoint:
`d8dc240bd74e271f88b2ef4583f6b79e533918b2`

Source-format proposal CI:
`35060253297` — SUCCESS

Source-format proposal review audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW.md`

## Source-Format Proposal Human Review

Gate:
`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_REVIEW`

Decision:
`PASS_WITH_MANDATORY_EXECUTION_ARTIFACT_TIGHTENINGS`

The proposal design is accepted only as a basis for preparing a separate execution/authorization artifact. The review does not authorize network access, real full-row exposure, diagnostic execution, workflow creation, parser/regex/runtime changes or remediation.

The explicit one-row full-row transient privacy expansion is acceptable as a **future design boundary only** because it remains limited to one reproduced mismatch row, persists/logs no row or field content, and requires a separate fresh full-row transient privacy approval plus a separate fresh execution approval before any network request.

## Mandatory Tightenings for the Future Execution Artifact

The next artifact must incorporate all of the following without widening scope:

1. `T-1` — fixed first-match classifier precedence in the exact order:
   - `FULL_ROW_UTF8_DECODE_FAILED`
   - `STDLIB_STRICT_CSV_PARSE_FAILED`
   - `STDLIB_COLUMN_SHAPE_NOT_CANONICAL`
   - `PROJECTOR_STDLIB_PROPERTY_TYPE_DIFFER`
   - `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`
2. `T-2` — the comparator must use the exact same transient logical-row bytes already in memory; no re-read or extra Range request.
3. `T-3` — exact stdlib newline/multiline framing must be pinned, e.g. `io.StringIO(decoded_row, newline="")` feeding `csv.reader` with the pinned dialect, or an equivalently explicit standard-library construction covered by synthetic regression tests.
4. `T-4` — the independent comparator must yield exactly one CSV record; zero or multiple records stop fail-closed under an enumerated non-source-bearing reason code.
5. `T-5` — all non-classification fail-closed reason codes must be enumerated; free-text/parser exception output remains forbidden.

## Proposal / Privacy Boundary

The reviewed future design remains no wider than:

- exact pinned source endpoint and identity;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced target mismatch;
- maximum 1 full-row independent cross-check on that mismatch row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries/redirects/additional ranges/full-body fallback/automatic widening.

No source value, full row, field value, hash, exact length, fragment, codepoint, transformed value, PROPERTY_ID, owner/holder value, parser exception text or source-derived free text may persist or be logged.

## Approval State

All prior execution/privacy/authority approvals remain `CONSUMED` and permanently non-reusable, including:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

No source-format execution or full-row privacy approval has been granted.

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

Prepare only, offline, a separate:

`PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_ARTIFACT`

It must incorporate T-1 through T-5, perform no network access or real full-row exposure during preparation, and leave any future execution/full-row privacy approvals ungranted until a later human gate.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.