# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The original live-source mismatch was classified as `ASCII_STRUCTURAL_MISMATCH`; the separately reviewed and authorized source-format diagnostic then produced `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`.

The human source-format diagnostic evidence review is now complete. It confirms that, for the one examined row, the strict stdlib CSV parser and current custom projector agree on the canonical PROPERTY_TYPE field while that agreed field remains structurally incompatible with the unchanged validation rule.

Semantic compatibility remains unresolved. No runtime remediation or source activation is authorized.

## Source-Format Diagnostic Evidence Review

Gate:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EVIDENCE_REVIEW`

Decision:

`PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_NO_RUNTIME_CHANGE_AUTHORIZED`

Review branch:

`m3-ca-sco-property-type-source-format-diagnostic-evidence-review`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EVIDENCE_REVIEW.md`

Review base HEAD:

`dbf4826a013daf604a48719c5b2dd92980f1a335`

Review base CI:

`35090434652` — SUCCESS

## Reviewed Evidence

One-shot source-format execution:

`35090057224` — SUCCESS

Persisted result:

- `diagnostic_result_status`: `SOURCE_FORMAT_CLASSIFIED`
- `source_format_diagnostic_class`: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`
- `fail_closed_reason_code`: `null`
- source identity verified: `true`
- HEAD requests: `1`
- Range GET requests: `1`
- HTTP requests total: `2`
- source response-body bytes: `131072`
- transient rows examined: `1`
- full-row cross-check rows examined: `1`

Within the reviewed classifier this establishes, for the one row only, that strict full-row UTF-8 decode and strict stdlib CSV parse succeeded, the canonical 25-column shape was produced, stdlib column index `1` agreed with the current projector's PROPERTY_TYPE field, and that agreed field still failed `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

It does not reveal the exact field value or justify inference of a specific malformed shape.

## Evidence Review Assessment

The parser-disagreement hypothesis is not supported for the examined row. Repeating the same parser-vs-parser diagnostic is not justified at this checkpoint.

The already archived SCO authority supports the accepted enumerated property-type shape boundary and is not contradicted by this evidence. Additional authority retrieval is not justified merely to repeat that proof.

The evidence is sufficient only to justify an offline proposal defining deterministic fail-closed handling for the known condition “canonical PROPERTY_TYPE field is structurally nonconforming”. It does not select or authorize the handling policy itself.

## Approval / Privacy State

The two source-format approvals are `CONSUMED` and permanently non-reusable:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

All source-format safety flags remain `false`: no row/field content, PROPERTY_TYPE or derivative, PROPERTY_ID, owner/holder value, row hash/exact length, parser exception text, raw body or source-derived free text was persisted; no remediation was performed.

The one-shot source-format workflow remains absent.

## Governance State

- parser/projector unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- remediation authorized: `false`;
- additional source execution authorized: `false`;
- additional privacy expansion authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL`

The proposal must compare deterministic fail-closed handling options without source/authority network access, without reconstructing the hidden value, and without changing runtime behavior. Any future real-source execution, privacy expansion, source activation or remediation requires a separate reviewed authorization path.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.