# NY OSC Transient Local File Runner — Offline

Date: 2026-09-18

Status: `IMPLEMENTED_SYNTHETIC_ONLY / LOCAL RETENTION APPROVAL GRANTED / GATE2 NOT GRANTED`

## Product Owner authorization

Exact authorization:

`APPROVO NY OSC FIRST DOWNLOAD TRANSIENT LOCAL FILE BOUNDED ONCE`

This approval is recorded as a single-use, non-reusable local-retention exception only.

It does not authorize the Owner Name File download or Gate 2 transient PII processing by itself.

## Purpose

Resolve the execution-transport mismatch between:

- OSC's browser workflow, which saves `FINDERS.zip` to local storage; and
- the project's prior memory-only/no-durable-raw-persistence boundary.

## Runtime design

The runner accepts a local archive only when:

- both the transient-local-file approval and Gate 2 approval artifacts are present and unconsumed;
- the file is named `FINDERS.zip`;
- the file lives under an OS temp directory whose path contains the dedicated prefix `unclaimed-ny-osc-gate2-`;
- compressed size is within the Gate 2 byte cap.

It then:

1. reads the bounded ZIP into memory;
2. delegates to the verified NY schema-discovery harness;
3. returns only non-PII aggregate/schema metadata;
4. logically deletes the local ZIP in a `finally` block;
5. fails closed if deletion fails.

No local path is returned in the persisted result.

## Deletion semantics

The runner guarantees only logical filesystem deletion.

It does not claim physical secure erasure from SSD/HDD media.

For this reason the approved scope also forbids:

- OneDrive/Dropbox/cloud-sync locations;
- repository paths;
- chat uploads;
- durable retention;
- owner-field logging.

## Gate 2 dependency

The PowerShell orchestration script refuses to proceed unless a separate Gate 2 approval artifact exists.

No real file was used in implementation or tests.

## Safety state

- local-retention approval: GRANTED / NOT CONSUMED;
- Gate 2: NOT GRANTED;
- real download performed: no;
- real owner PII processed: no.
