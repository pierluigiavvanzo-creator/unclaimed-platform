# NY OSC Nonconforming Row Handling Policy Proposal

Date: 2026-09-18

Status: `PROPOSAL_ONLY_NOT_AUTHORIZED`

## Trigger

Two single-use real executions have now been consumed.

Attempt 1 stopped on:

`PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`

Attempt 2 stopped on:

`UNEXPECTED_DATA_FIELD_COUNT`

Both executions deleted the temporary raw archive and returned no owner values.

The second fail-closed result proves only that at least one scanned nonblank row did not split into the documented 14 fields. Because the current blocked-result path discards scan progress, it does not show whether valid rows existed before the trigger.

## Reuse-first decision

Reuse the already adopted California control concept:

`ROW_DEFER_CONTINUE_METADATA_ONLY`

but create a NY-specific contract.

A nonconforming NY row is not repaired, normalized into validity, treated as non-insurance, persisted, quarantined, or shown to a human.

## Proposed NY behavior

For a row whose physical field count is not exactly 14:

1. increment an aggregate deferred-row counter;
2. parse no field from that row;
3. persist no row-specific metadata;
4. continue to the next row.

For an exact-14-field row whose normalized Property Type Code still fails the strict ASCII-alphanumeric shape:

1. increment a separate aggregate defer counter;
2. do not persist the value;
3. do not classify it as non-insurance;
4. continue.

Completeness accounting must make deferred rows visible in aggregate.

## Mandatory completeness invariant

For non-header, nonblank rows:

`total_nonblank_data_rows_seen = exact_14_field_rows_count + deferred_field_count_rows_count`

No silent omission is permitted.

## Explicit non-changes

This proposal does not:

- introduce a quote-aware CSV parser;
- infer a new delimiter;
- infer encoding;
- decode owner fields;
- alter the documented 14-field layout;
- alter the documented Property Type Code position;
- activate insurance classification;
- approve or enable the source;
- authorize another download.

## Human gate

Approval phrase:

`APPROVO NY OSC ROW DEFER CONTINUE METADATA ONLY POLICY`

Approval authorizes only bounded offline implementation and synthetic tests. A future real-file execution would still require a separate, fresh authorization.
