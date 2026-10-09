# NY OSC Line-Local Quote Dialect Arbitration — Review Remediation Offline

Date: 2026-09-20

Classification: `A — Product Critical`

## Requested action

`REMEDIATE_NY_OSC_LINE_LOCAL_QUOTE_DIALECT_ARBITRATION_REVIEW_FINDINGS_OFFLINE`

## Baseline

- branch: `ny-osc-line-local-quote-dialect-arbitration-offline`;
- reviewed checkpoint: `9370acd5f171755b29b50f153b0eb929b6fd753f`;
- reviewed CI: `35512354582 — SUCCESS`;
- review result: `CHANGES_REQUIRED_BEFORE_MERGE`.

## Finding 1 — unknown mode fallback

Review confirmed that Python `Literal` typing does not enforce the
`quote_dialect_mode` value at runtime. The reviewed implementation selected
`LINE_LOCAL_ARBITRATION` only on an exact match and otherwise fell through to
`MULTILINE_LEGACY`.

The remediation adds an explicit allow-list check at the beginning of
`discover_ny_owner_name_schema()`, before archive-size checks or ZIP parsing.
Any unrecognized mode raises:

`ValueError("unsupported quote dialect mode")`

There is no fallback to the legacy parser.

## Finding 2 — boundary regressions

Repository-native regression coverage is added for the two state variables that
can span fixed 64 KiB input chunks:

- `_pending_cr`;
- `_pending_quote`.

The tests place:

1. CR at byte 65535 and LF at byte 65536;
2. the first quote of a doubled-quote pair at byte 65535 and the second quote
   at byte 65536.

Both cases use `LINE_LOCAL_ARBITRATION` and require successful discovery of
the documented 14-field structure.

## Preserved behavior

- historical `MULTILINE_LEGACY` remains unchanged;
- no historical runner is modified;
- line-local arbitration remains not runtime activated;
- `QUOTE_DIALECT_AMBIGUOUS` remains fail-closed;
- true non-quote field-count mismatch remains
  `UNEXPECTED_DATA_FIELD_COUNT`;
- no owner row/value is returned or persisted.

## Source/network boundary

No OSC access, listing preflight, download, real Owner Name File opening,
owner-PII processing, retry or sixth-attempt preparation occurred.

## State at commit

`REMEDIATION_IMPLEMENTED / NOT_RUNTIME_ACTIVATED / CI_PENDING`
