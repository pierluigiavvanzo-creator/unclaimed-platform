# NY OSC Line-Local Quote Dialect Arbitration — Offline Implementation

Date: 2026-09-20

Classification: `A — Product Critical`

## Scope

Implemented exclusively:

`IMPLEMENT_NY_OSC_LINE_LOCAL_QUOTE_DIALECT_ARBITRATION_OFFLINE`

No OSC access, listing preflight, download, real archive opening, owner-PII processing,
retry, sixth-attempt preparation, source activation, identity resolution, beneficiary
matching or outreach occurred.

## Repository baseline

- branch: `mvp1-ny-second-attempt-approved-ready-execution`
- baseline HEAD: `8c3df1bd26822044cf87ab808e2a45b15714a464`

## Root-cause basis

The fifth-attempt retained structural telemetry supplied by the Product Owner reported:

- `raw_pipe_count = 228072`;
- `physical_line_breaks_inside_quotes = 17543`;
- documented physical-row pipe count = `13`.

The exact identity:

`(17543 + 1) * 13 = 228072`

supports the conclusion that the multiline interpretation merged the structural
equivalent of 17,544 ordinary 14-field physical rows after one quote-open event.

## Implementation

The historical multiline parser remains available and unchanged for reproducibility.
A new explicit mode is added:

`LINE_LOCAL_ARBITRATION`

In that mode:

1. LF/CRLF are hard physical-record boundaries.
2. Quote state never survives a physical-record boundary.
3. Every line is scanned simultaneously under a raw-pipe interpretation and a
   same-line quote-aware interpretation.
4. If the two interpretations produce different field boundaries, processing stops
   fail-closed with `QUOTE_DIALECT_AMBIGUOUS`.
5. If a physical line ends with quote state still open, processing stops with the
   same bounded ambiguity reason.
6. No owner field or complete raw row is returned, decoded or persisted.
7. A versioned non-PII diagnostic records structural counters only.
8. A true field-count mismatch without quote ambiguity continues to use
   `UNEXPECTED_DATA_FIELD_COUNT`.

The existing `MULTILINE_LEGACY` mode remains the default in this offline
implementation, so historical runners do not silently change behavior.

## New diagnostic contract

`schemas/agents/ny_owner_name_quote_dialect_diagnostic_result.schema.json`

Version: `1.0.0`.

The contract exposes only raw/quote-aware field counts, pipe counts, suppressed-pipe
count, quote counters, whether the physical line ended inside quote state, and a
bounded structural classification. It exposes no owner values, record bytes, offsets,
hashes or raw paths.

## Synthetic coverage

Added cases for:

- ordinary/balanced quote behavior through existing tests;
- open quote at physical EOL cannot absorb the next line;
- same-line quoted-pipe disagreement blocks as quote-dialect ambiguity;
- balanced quotes without embedded pipe remain accepted;
- true 13-field row still uses the existing field-count fail-closed path.

## Runtime boundary

This change does not activate line-local arbitration in the existing transient-local
execution bridge or any historical attempt runner.

Attempt 5 is already consumed and must not be retried. Any future real execution
requires separate integration, review, fresh approvals and explicit authorization.

## State before CI

`IMPLEMENTED_OFFLINE / NOT_RUNTIME_ACTIVATED / CI_PENDING`
