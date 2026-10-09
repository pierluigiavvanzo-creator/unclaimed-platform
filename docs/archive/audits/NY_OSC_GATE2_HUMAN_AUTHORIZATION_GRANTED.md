# NY OSC Gate 2 — Human Authorization Granted

Date: 2026-09-18

Status: `GRANTED_NOT_CONSUMED`

## Product Owner authorization

Exact authorization:

`APPROVO NY OSC OWNER NAME FILE FIRST DOWNLOAD TRANSIENT PII BOUNDED ONCE`

Approval ref:

`OWNER_APPROVAL_2026-09-18_NY_OSC_FIRST_DOWNLOAD_TRANSIENT_PII_BOUNDED_ONCE_A7D4C2F1`

Single use: yes.

Reusable: no.

Retry authorized: no.

## Authorized execution

Exactly one bounded first-file download and transient schema-discovery execution, subject to all of the following:

- current listing identity must still match `FINDERS.zip / 390.51 MB / 9/16/2026, 1:33:31 PM`;
- `max_download_bytes = 450,000,000`;
- `max_uncompressed_bytes = 2,000,000,000`;
- `max_archive_members = 1`;
- exactly one text member;
- transient local file only under the separately approved one-shot local-retention exception;
- immediate logical deletion after bounded processing;
- no owner-row persistence;
- no owner-field logging;
- no row-specific human inspection;
- only derived non-PII schema metadata may persist.

## Not authorized

This approval does not authorize:

- source activation;
- production classification activation;
- identity resolution;
- beneficiary matching;
- outreach;
- fee agreement;
- representation;
- claim activity.

## Execution state

The approval is granted but not consumed.

No Owner Name File has been downloaded under this approval yet.

Next action:

`EXECUTE_NY_OSC_FIRST_DOWNLOAD_TRANSIENT_PII_BOUNDED_ONCE`
