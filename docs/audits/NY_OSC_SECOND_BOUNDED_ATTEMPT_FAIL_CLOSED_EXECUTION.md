# NY OSC Second Bounded Attempt — Fail-Closed Execution Evidence

Date: 2026-09-18

Status: `BLOCKED_FAIL_CLOSED`

Reason: `UNEXPECTED_DATA_FIELD_COUNT`

Persisted non-PII metadata:

- archive bytes: `409,477,526`;
- archive members: `1`;
- selected text member present: yes;
- selected member uncompressed bytes: `1,939,569,781`;
- documented field count: `14`;
- observed data field count: not retained by the current fail-closed result;
- local raw ZIP logically deleted: yes;
- no owner values returned or persisted.

Both second-attempt approvals are consumed, single-use and non-reusable. No retry is authorized.

This result establishes only that at least one nonblank row encountered by the current strict scanner did not split into exactly 14 pipe-delimited fields. It does not establish malformed OSC source data.

The fail-closed result does not reveal whether the mismatch occurred on the first data row or later because aggregate scan progress is discarded on that path.

Next work is offline only: source-specific nonconforming-row policy proposal. No third download is authorized.
