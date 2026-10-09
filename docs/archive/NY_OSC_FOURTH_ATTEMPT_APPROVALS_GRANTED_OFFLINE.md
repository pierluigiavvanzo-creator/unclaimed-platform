# NY OSC Fourth Attempt — Approvals Granted Offline

Date: 2026-09-19

Classification: `A — Product Critical / Human Authorization Gate`

## Result

The Product Owner supplied both exact contract phrases:

- `APPROVO NY OSC FOURTH TRANSIENT LOCAL FILE BOUNDED ONCE`;
- `APPROVO NY OSC OWNER NAME FILE FOURTH BOUNDED TRANSIENT PII ATTEMPT ONCE`.

The two approval artifacts are recorded as:

`GRANTED_NOT_CONSUMED / SINGLE USE / NON-REUSABLE / ZERO RETRY`

## Binding

- attempt: `4`;
- runner checkpoint: `1c4be944004c85936d53506a5998b9aeffc9aed0`;
- runner verification CI: `35428062292 — SUCCESS`;
- proposal checkpoint: `bec3e23325f9d565428e1f7cdeac401010884827`;
- proposal CI: `35426399366 — SUCCESS`;
- approval references: distinct.

## Preserved limits

One download maximum, zero retries, 450,000,000 compressed bytes,
2,000,000,000 uncompressed bytes, one archive member, exactly one text member,
pipe delimiter, 14 documented fields and 65,536-byte parser chunks.

No automatic widening or retry is allowed.

## Activity not performed

This offline registration performed no NY OSC access, fresh listing preflight, download,
archive opening, owner-file processing or PII processing.

The approval artifacts do not themselves perform or consume the authorization. They are
consumed only on a later authorized execution path.

## Next gate

A fresh exact listing preflight remains mandatory and requires a separate explicit
authorization. Any listing drift must stop before download.
