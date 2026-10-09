# NY OSC Structural Diagnostic Telemetry — Offline Implementation

Date: 2026-09-19

Classification: `A — Product Critical`

## Trigger

The fourth bounded NY OSC attempt executed once and stopped fail-closed with:

`UNEXPECTED_DATA_FIELD_COUNT`

Observed non-PII metadata:

- documented field count: `14`;
- observed structural field count: `13`;
- complete records before block: `213454`;
- Property Type Code ASCII-valid records before block: `213454`;
- compressed archive bytes: `409477526`;
- selected text member bytes: `1939569781`;
- raw local archive logically deleted;
- no owner values returned or persisted.

Both fourth-attempt approvals are consumed, single-use, non-reusable and authorize zero
retry.

## Diagnostic problem

An observed structural field count of 13 does not distinguish:

1. a source record containing fewer than the documented 13 pipe delimiters; from
2. a record containing 13 or more raw pipe bytes where at least one pipe is interpreted as
   non-structural while the parser is inside a quoted field.

No fifth source access is required or authorized by this implementation.

## Implementation

The byte-level streaming scanner gains bounded structural counters only:

- raw pipe count;
- structural pipe count;
- suppressed pipe count;
- quote byte count;
- quote-open events;
- quote-close events;
- doubled-quote pairs;
- physical line breaks observed inside quoted content.

No record bytes, field values, field lengths, offsets, hashes, Property ID, owner/holder
values or raw paths are retained by the diagnostic contract.

The existing schema-discovery result contract remains unchanged. A separate versioned JSON
Schema defines the structural diagnostic result. The existing parser still fails closed when
the field count differs from 14.

## Classifications

- `RAW_DELIMITER_COUNT_BELOW_DOCUMENTED`;
- `QUOTE_SUPPRESSED_DELIMITER_OBSERVED`;
- `QUOTED_DELIMITER_INTERACTION_AMBIGUOUS`;
- `STRUCTURAL_MISMATCH_UNCLASSIFIED`.

These classifications describe parser-observed structure only. They do not authorize row
acceptance, normalization, repair, row skipping, quarantine, source activation or retry.

## Synthetic evidence

Synthetic cases cover:

- true 13-field structural shape: 12 raw / 12 structural pipes;
- 14 physical segments with one pipe suppressed by quote state: 13 raw / 12 structural pipes;
- valid quoted pipe with 14 structural fields, which emits no blocking diagnostic;
- multiline quoted content with structural-only line-break counting.

Existing multiline, doubled-quote and 64 KiB boundary regression coverage remains active.

## Execution boundary

This implementation is repository/synthetic-only. It performs no OSC access, fresh listing
preflight, download, owner-file opening or new PII processing.

The fourth-attempt execution evidence is recorded from the Product Owner-supplied runtime
output. No fifth attempt is authorized.


## Verification

GitHub Actions run:

`35444131105 — SUCCESS`

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety smoke;
- Streamlit startup smoke;
- frontend lint;
- frontend typecheck;
- frontend build.


## Execution bridge remediation

Review identified that parser-side telemetry was not initially carried through the transient-local execution bridge.

Remediation:
- historical execution receipt v1.0.0 remains unchanged;
- new execution receipt v1.1.0 carries structural diagnostics;
- UNEXPECTED_DATA_FIELD_COUNT requires a structural diagnostic;
- other outcomes require structural_diagnostic = null;
- synthetic unit and contract tests cover both blocked and valid input;
- existing fail-closed and privacy bounds are unchanged.

Initial remediation CI 35446723423 failed because two bridge return paths still instantiated v1.0.0. That constructor-only defect was corrected without changing parser or policy logic.

Final remediation checkpoint: 03c1e2fb6a3b24e4afd9a4dff12b713a57b3390e

Final remediation CI: 35446786002 — SUCCESS
