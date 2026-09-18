# NY OSC Owner Name File — Access Instructions / Size Metadata Request

Date: 2026-09-18

Status: `ACCESS_INSTRUCTIONS_RECEIVED_SIZE_METADATA_PENDING`

## Evidence received

Official OSC email subject:

`New York State Unclaimed Funds Owner Name File Request`

The email and attached instructions were reviewed only for non-content access/download constraints.

Observed:

- secure FTP access is used;
- archive name: `NYSFINDERS.ZIP`;
- archive contains pipe-delimited text data;
- OSC instructions do not state the current archive size;
- no Owner Name File was downloaded;
- no owner PII was processed.

## Action taken

A reply was sent to OSC requesting only:

- current `NYSFINDERS.ZIP` archive size, preferably in bytes or MB;
- whether file-size metadata is visible in the secure FTP listing before download.

No file content was requested.

## Gate state

Gate 2 remains:

`NOT GRANTED / NOT READY`

Readiness still requires evidence-based `max_download_bytes`.

## Next action

`AWAIT_NY_OSC_FILE_SIZE_METADATA_RESPONSE`
