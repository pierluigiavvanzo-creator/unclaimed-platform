# NY OSC Third Bounded Attempt Authorization

Date: 2026-09-18

## Decision

The Product Owner supplied both exact third-attempt authorization phrases:

- `APPROVO NY OSC THIRD TRANSIENT LOCAL FILE BOUNDED ONCE`
- `APPROVO NY OSC OWNER NAME FILE THIRD BOUNDED TRANSIENT PII ATTEMPT ONCE`

The corresponding artifacts are registered as
`GRANTED_NOT_CONSUMED / SINGLE USE / NON-REUSABLE / ZERO RETRY`.

## Technical binding

The grants are bound to the integrated offline runner checkpoint
`2d871ee041abe9cccc0e0fa32b849bbe223bdfa2` and successful CI run `35385157576`.

The execution envelope remains unchanged:

- attempt number: 3;
- downloads maximum: 1;
- retries maximum: 0;
- compressed archive maximum: 450,000,000 bytes;
- uncompressed content maximum: 2,000,000,000 bytes;
- archive members maximum: 1;
- expected remote and local filename: `FINDERS.zip`;
- fresh exact listing preflight required;
- dedicated OS temporary directory required;
- immediate logical deletion required;
- durable raw persistence, repository persistence, cloud sync and chat upload forbidden;
- physical secure erasure not guaranteed;
- owner rows, owner fields and row-specific inspection not persisted or logged.

The two execution approval references are distinct. Previously consumed approvals remain
non-reusable.

## Repository activity in this change

This change only records authorization and updates repository contracts, policy, tests and
project state. It performs no NY OSC network access, remote preflight, download, archive
opening or owner-PII processing.

## Next controlled action

After this authorization package is independently verified by CI and integrated, the Product
Owner may run `scripts/ny_osc_gate3_transient_local.ps1`. The script must stop before
download on any listing drift or failed authorization precheck. Any terminal execution
consumes both approvals; no automatic or manual retry is authorized by these grants.
