# NY OSC MALFORMED_QUOTED_RECORD — Offline Analysis

Date: 2026-09-19

## Decision

Status:

`ANALYZED_OFFLINE_REMEDIATION_FEASIBLE_NOT_IMPLEMENTED`

A bounded multiline quoted-record parser is technically feasible without decoding, returning,
logging or persisting owner fields. This analysis does not modify the production parser,
runner, approvals or execution policy and does not authorize a fourth attempt.

## Confirmed facts

The third attempt retained only aggregate non-PII evidence and stopped after 165,438 complete
records with `MALFORMED_QUOTED_RECORD`.

The current implementation:

1. iterates over the ZIP member with `for raw_line in stream`;
2. strips the physical `CR/LF`;
3. invokes the quoted-pipe splitter on that physical line;
4. blocks if the quote state is still open at the end of the physical line.

Therefore a logically valid record containing an embedded newline in a quoted field is
indistinguishable from a truly unclosed quoted record in the current implementation.

Because neither the raw file nor the offending row was retained, an embedded quoted newline is
a compatible hypothesis, not a confirmed property of the NY OSC file. Source corruption is
not claimed.

## Reuse-first evaluation

Python's standard `csv` reader is designed around text rows and produces decoded string
fields. Using it here would decode and materialize owner-name and address fields, conflicting
with the existing byte-level privacy contract. Introducing a third-party CSV dependency for
this narrow structural discovery task is not justified before a smaller byte-level design is
tested.

Selected direction:

`BYTE_LEVEL_STREAMING_STATE_MACHINE`

## Bounded design

The parser should consume bytes incrementally and treat `LF` or `CRLF` as a logical record
boundary only while outside quotes. Newline bytes encountered inside quotes are consumed as
field content without retaining that content.

The state machine retains only:

- quote state;
- current field index and structural field count;
- incremental header-match state for the first logical record;
- non-empty/ASCII-alphanumeric state for field index 1;
- aggregate record counters.

It must not retain a complete owner row or owner field. Auxiliary memory can therefore remain
constant with respect to logical-record length. CPU and total input remain bounded by the
existing archive and uncompressed-size caps.

Doubled quotes remain the only supported escaped-quote convention. EOF while inside quotes,
wrong field count after logical-record assembly, invalid Property Type Code shape and
unsupported quote placement must continue to fail closed.

## Synthetic acceptance matrix

Required before any integration:

- LF and CRLF inside a quoted synthetic owner field;
- quoted pipe plus multiline content;
- doubled quotes inside multiline content;
- records following a multiline record;
- exact header and no-header layouts;
- EOF with an open quote;
- wrong field count after logical assembly;
- invalid Property Type Code;
- serialized result contains no synthetic owner value.

## Next gate

The next permitted task is:

`IMPLEMENT_NY_OSC_STREAMING_MULTILINE_QUOTED_RECORD_PARSER_OFFLINE`

That task may change the parser and synthetic tests only. It may not create a runner, approval,
preflight, download or fourth-attempt proposal. A future real execution would remain subject to
a separate decision after implementation, review and CI.
