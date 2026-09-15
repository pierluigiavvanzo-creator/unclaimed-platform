# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Diagnostic Approvals Granted Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-diagnostic-execution-one-shot`
- authorization package checkpoint SHA: `daeaa7bfb7f7d73a61f011d394cc88393625866c`
- authorization review: `PASS`
- execution approval evidence: PRESENT / `GRANTED_NOT_YET_CONSUMED`
- transient-row privacy approval evidence: PRESENT / `GRANTED_NOT_YET_CONSUMED`
- both approvals: single-use, non-reusable, pinned to package SHA above

## Exact One-Shot Boundary

The current gate is:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

Before network the one-shot execution must verify and consume both fresh approvals. Only then may it use:

- exact endpoint `https://claimit.ca.gov/upd-property-records/04_From_500_To_Beyond.zip`;
- pinned content length `162416884`;
- pinned ETag `"b25b315b6cd8007624387c3a00d4b1fe"`;
- media type `application/zip`;
- byte-range support `bytes`;
- canonical member `From_500_To_Beyond_1_of_4.csv` only;
- max 4 transient data rows;
- stop at first reproduced format mismatch;
- max 1 HEAD + 1 Range GET;
- max 2 HTTP requests total;
- max 131072 source response-body bytes;
- max 262144 uncompressed transient bytes;
- max 32768 bytes per logical record;
- retries `0`;
- redirects forbidden;
- additional range/full-body fallback/automatic widening forbidden;
- authority and any other source/endpoint access forbidden.

## Deterministic Diagnostic Contract

Current validation regex remains unchanged:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

Classification precedence:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

Whitespace probe is only boundary `U+0020` SPACE / `U+0009` TAB. Case probe is ASCII-only `a-z -> A-Z`. Non-ASCII is `> U+007F`; disallowed ASCII controls are `U+0000-U+001F` plus `U+007F`, subject to fixed precedence for boundary TAB.

These are in-memory diagnostic predicates only. They do not authorize runtime trimming/casing/normalization or any remediation.

## Output / Privacy Boundary

Persist only:

- `diagnostic_result_status`;
- coarse `diagnostic_class` or null;
- enumerated `fail_closed_reason_code` or null;
- `source_identity_verified`;
- bounded HEAD/range/HTTP/body/row counters;
- fixed safety flags.

Never persist/log exact PROPERTY_TYPE, bytes, hash, exact length, fragments, codepoints, transformed value, full row, raw response body, PROPERTY_ID, owner/holder values, distinct source code lists, or source-derived free text.

## Consumed Approvals — Never Reuse

Historical approvals remain consumed/non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

The two current diagnostic approvals are granted but not yet consumed. They must become `CONSUMED` before the first source request.

## SINGLE NEXT ACTION

Execute only:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

After any result — `DIAGNOSTIC_CLASSIFIED` or `STOPPED_FAIL_CLOSED` — stop at:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`

Do not modify parser/regex/runtime semantics, apply remediation, activate source policy/registry/production classification, or enter identity/genealogy/matching/outreach/claim work.
