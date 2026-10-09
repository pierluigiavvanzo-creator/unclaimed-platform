# NY OSC Streaming Multiline Quoted-Record Parser — Offline Implementation

Date: 2026-09-19

## Scope

Implemented:

`IMPLEMENT_NY_OSC_STREAMING_MULTILINE_QUOTED_RECORD_PARSER_OFFLINE`

The change is restricted to the byte-level schema-discovery parser, synthetic tests and project
documentation. It performs no source access, download, preflight, real-file processing,
approval creation or fourth-attempt preparation.

## Implementation

The parser now streams physical lines into a logical-record state machine.

Record boundaries:

- `LF` terminates a record only outside double quotes;
- `CRLF` terminates a record only outside double quotes;
- line endings inside double quotes are consumed as field content;
- EOF inside an open quote remains `MALFORMED_QUOTED_RECORD`.

The state machine does not retain complete records or owner fields. It retains only:

- quote state;
- current field index and count;
- whether a pipe was observed;
- incremental exact/normalized documented-header match state;
- non-empty ASCII-alphanumeric validity for Property Type Code;
- aggregate record counters.

The normalized-header matcher operates incrementally and preserves existing support for a UTF-8
BOM, surrounding whitespace and quoted documented header names.

## Privacy and bounds

Unchanged:

- archive download cap;
- uncompressed member cap;
- archive-member cap;
- exactly one text member;
- expected 14-field layout;
- no owner-row persistence;
- no owner-field decoding or logging;
- no row-specific human inspection;
- non-PII aggregate output only.

Auxiliary parsing memory is constant relative to logical-record length. Existing archive bytes
are still handled under the previously established execution contract; this change does not
widen that contract.

## Synthetic verification matrix

Coverage includes:

- LF inside a quoted owner field;
- CRLF inside a quoted owner field;
- quoted pipe plus multiline content;
- doubled quotes inside multiline content;
- a following logical record;
- exact header and no-header behavior through the existing suite;
- EOF inside an open quote;
- wrong field count after multiline assembly;
- invalid Property Type Code after a valid multiline record;
- serialized output contains no synthetic owner value.

## Execution gate

This implementation does not authorize real execution. The third attempt remains consumed and
non-reusable. No fourth runner, approval artifact, preflight or download is created.

After CI and integration, the next action is a separate Product Owner decision on whether to
prepare an offline-only fourth-attempt proposal.
