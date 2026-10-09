# NY OSC Second Attempt — Root-Cause Audit and Offline Remediation

Date: 2026-09-18

Classification: `A — Product Critical / Offline Safety Repair`

Status: `OFFLINE_VERIFIED / REPOSITORY_CI_PENDING / NO_REAL_RETRY_AUTHORIZED`

## Trigger

The authorized second bounded attempt was consumed once and stopped fail-closed with:

`UNEXPECTED_DATA_FIELD_COUNT`

The raw ZIP was logically deleted in the existing `finally` boundary. No raw path or owner
values were returned or persisted. Physical secure erasure is not claimed.

## Confirmed execution facts

- archive bytes: `409,477,526`;
- archive member count: `1`;
- selected text member uncompressed bytes: `1,939,569,781`;
- expected documented layout width: `14`;
- the previous implementation did not retain the observed field count on failure;
- both second-attempt approvals are consumed, single-use and non-reusable.

Evidence:

`sources/evidence/ny_osc_owner_name_file_second_attempt_execution_result.v1.json`

## Root-cause analysis

The parser used:

`line.split(b"|")`

This treats every pipe byte as a delimiter, including a pipe inside a double-quoted field.
The first-attempt repair added recognition of quoted headers and quoted Property Type Code
tokens, but it did not implement quote-aware record splitting.

The sequence of failures is therefore consistent with this mechanism:

1. first attempt stopped when a quoted/documented header was interpreted as data;
2. the offline repair recognized that header;
3. the second attempt advanced to a data record;
4. raw splitting could then produce a width other than 14 if a quoted field contained a
   pipe.

This is a strong code-level hypothesis, not proof of the deleted real record's contents.
No owner-field value is inferred or reconstructed.

## Offline remediation

The repair candidate:

- replaces raw pipe splitting with a byte-level quote-aware splitter;
- preserves doubled quotes while scanning;
- never decodes, logs, persists or returns owner fields;
- fails closed with `MALFORMED_QUOTED_RECORD` for an unclosed double quote;
- uses existing contract fields to retain only permitted structural observations on a
  blocked result: delimiter presence, field count, recognized documented-header state and
  aggregate completed-record counters;
- records both second-attempt approvals as consumed;
- adds a PowerShell status check before temp-directory creation and before the Product
  Owner is asked to download, preventing replay after consumption.

No new parser dependency was added. Existing byte-level code, standard library ZIP handling,
Pydantic contracts and JSON Schema validation were reused.

## Synthetic regression coverage

Tests cover:

- a quoted owner field containing a pipe while preserving 14 structural fields;
- doubled quotes inside a quoted non-target field;
- unclosed quote fail-closed behavior;
- field-count failure retaining only non-PII structural diagnostics;
- documented-header metadata preservation without owner-row persistence;
- consumed-approval schema validation;
- execution-result contract validation;
- PowerShell consumption checks occurring before the download prompt.

## Safety boundary

This audit does not authorize:

- another NY OSC download;
- real owner-row persistence or inspection;
- source activation;
- production classification;
- identity resolution or beneficiary matching;
- outreach, representation, fee agreement or claim activity.

Any third real attempt requires a separate proposal, successful repository CI, fresh listing
preflight and new explicit single-use approvals.

## Local verification

Environment:

- Python `3.12.14` (repository supports `>=3.11,<3.13`);
- isolated `.venv` created from `pyproject.toml`;
- no OSC network access and no real source file.

Results:

- Ruff: `PASS`;
- mypy with `MYPYPATH=src`: `PASS`, 19 source files;
- full pytest: `438 passed`, `0 failed`, 2 dependency deprecation warnings;
- targeted NY repair suite: `30 passed`, `0 failed`.

Repository CI remains required after the patch is applied to the canonical Git branch.
