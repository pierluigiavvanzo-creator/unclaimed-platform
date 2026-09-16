# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The original live-source mismatch was first classified as `ASCII_STRUCTURAL_MISMATCH`. A separately reviewed and authorized source-format diagnostic has now executed once and produced the coarse class `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`.

Semantic compatibility remains unresolved pending human evidence review. No runtime remediation is authorized.

## Source-Format Diagnostic Execution

Authorization functional package:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Authorization review:

`PASS`

One-shot execution branch:

`m3-ca-sco-property-type-source-format-diagnostic-execution-one-shot`

Execution run:

`35090057224` — **SUCCESS**

One-shot closure commit:

`badd71e2e32d32b48fdd255127931222941716dd`

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_source_format_diagnostic.execution.v1.json`

Execution audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION.md`

## Result

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

Within the reviewed classifier, this means the strict stdlib CSV comparator and current custom projector agreed on the same PROPERTY_TYPE field for the one examined row, while that agreed field still failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

This does **not** reveal the exact value or a specific malformed shape. The value and protected derivatives remain unretained and must not be reconstructed or inferred.

## Approval State

The two fresh source-format approvals are now `CONSUMED` and permanently non-reusable:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Both evidence records pin:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

and execution run:

`35090057224`

All earlier execution/privacy/authority approvals also remain consumed and non-reusable.

## Privacy / Safety State

All source-format diagnostic safety flags are `false`:

- no full archive downloaded;
- no raw body persisted;
- no full row persisted;
- no row field value persisted;
- no PROPERTY_TYPE or derivative persisted;
- no PROPERTY_ID persisted;
- no owner/holder value persisted;
- no row hash or exact row length persisted;
- no parser exception text persisted;
- no source-derived free text persisted;
- no remediation performed.

The source-format one-shot workflow is ABSENT after closure.

## Governance State

- parser/projector unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- remediation authorized: `false`;
- additional source-format execution authorized: `false`;
- additional authority retrieval authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EVIDENCE_REVIEW`

Review only the retained coarse evidence and decide what, if anything, it justifies. Do not re-run source access, reuse consumed approvals, reconstruct the PROPERTY_TYPE value, change parser/regex/runtime behavior, or apply remediation during the review.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
