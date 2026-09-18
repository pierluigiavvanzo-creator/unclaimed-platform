# NY OSC Row-Shape Root-Cause Diagnostic — Offline

Date: 2026-09-18

Status: `IMPLEMENTED_SYNTHETIC_ONLY / NO THIRD REAL ATTEMPT AUTHORIZED`

## Trigger

The second bounded real execution stopped fail-closed with:

`UNEXPECTED_DATA_FIELD_COUNT`

The blocked-result contract did not retain the already-computed non-PII field count or header state. That telemetry gap is now corrected offline.

## Root-cause discipline

After two real fail-closed attempts, no third parser patch is selected from guesswork.

Official OSC public material supports only that the Owner Name File is delivered as a zipped delimited text file and carries owner, property-nature, reporting-time and reporting-organization information. The project documentation separately records a 14-field documented layout.

The public material reviewed does not establish the physical quoting, escaping or multiline-record rules of the downloaded file.

Therefore these remain hypotheses, not conclusions:

1. a pipe character may occur inside a quoted text field;
2. a trailing delimiter may create an extra empty field;
3. a quoted field may span a physical line;
4. the physical layout may differ from the documented 14-field layout.

## Diagnostic design

A separate byte-level diagnostic now compares, in aggregate only:

- raw pipe-based field-count histogram;
- double-quote-aware field-count histogram;
- count of physical lines ending in a delimiter;
- count of lines with unbalanced double quotes;
- count of lines resolving to exactly 14 fields under each counting method.

It does not decode or return field values.

The number of physical lines scanned is a required authorization parameter; there is no production default.

## Existing harness telemetry fix

When the normal schema-discovery harness blocks on row width or Property Type Code shape, it now preserves:

- the observed non-PII field count;
- the already-determined header state.

No owner value is added to the result contract.

## Real-data state

- attempt v1: consumed;
- attempt v2: consumed;
- v2 raw file logically deleted;
- no v2 retry authorized;
- no third download authorized.

## Next decision

Review and approve a dedicated third-run **row-shape diagnostic** only if the Product Owner accepts one more bounded real download. Do not authorize a production parser retry until the aggregate row-shape evidence identifies the physical-format cause.
