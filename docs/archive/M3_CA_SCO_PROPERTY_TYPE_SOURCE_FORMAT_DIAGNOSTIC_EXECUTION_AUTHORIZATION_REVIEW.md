# M3 California SCO — PROPERTY_TYPE Source-Format Diagnostic Execution Authorization Review

Date: 2026-09-16

## Review gate

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

## Result

`PASS`

The execution/authorization contract is accepted for progression to the owner-approval gate. This PASS accepts only the bounded authorization design. It does **not** grant either approval, create approval evidence, authorize network execution, authorize real full-row exposure, create a network workflow, or authorize parser/regex/runtime/remediation changes.

## Package reviewed

Authorization branch:

`m3-ca-sco-property-type-source-format-diagnostic-execution-authorization`

Authorization functional package checkpoint:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Package CI:

`35082891083` — SUCCESS

Final authorization-state HEAD reviewed:

`e73681941ef9794d54bef78b53361ea45baccbf9`

Final authorization-state CI:

`35083155026` — SUCCESS

Reviewed artifacts:

- `sources/proposals/ca_sco_segment_500_plus.property_type_source_format_diagnostic_execution_authorization.v1.json`
- `schemas/common/property_type_source_format_diagnostic_execution_authorization.schema.json`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION.md`
- `tests/contract/test_ca_sco_property_type_source_format_diagnostic_execution_authorization.py`

## Findings

### 1. No scope widening

The execution boundary is no wider than the reviewed source-format proposal:

- exact pinned `claimit.ca.gov` endpoint and source identity;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced `ASCII_STRUCTURAL_MISMATCH`;
- maximum 1 transient full-row independent cross-check on that mismatch row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- no redirects;
- no additional ranges;
- no full-body fallback;
- no automatic widening;
- no authority endpoint or other-source access.

### 2. T-1 through T-5 are machine-locked

The artifact and schema lock the five mandatory tightenings from the proposal review:

- T-1: exact first-match classifier precedence;
- T-2: same in-memory logical-record bytes, no re-read;
- T-3: explicit `io.StringIO(decoded_row, newline="")`-equivalent framing with pinned `csv.reader` dialect;
- T-4: exactly one independent CSV record or fail-closed;
- T-5: enumerated non-source-bearing fail-closed reason codes with no parser exception/source-derived free text.

Contract tests cover synthetic embedded LF, embedded CRLF and multiple-record behavior.

### 3. Privacy expansion remains separately gated

The artifact recognizes one full-row transient cross-check as a privacy expansion and keeps it unauthorized. It is limited to one logical row, same in-memory bytes only, immediately discarded after classification/fail-closed, with no persistence/logging of row or field content.

### 4. Fresh approvals are distinct and ungranted

The reviewed contract defines exactly two fresh approval references:

1. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
2. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Both are:

- single-use;
- non-reusable;
- `granted: false` at review time;
- required before any network request;
- required to be represented by separate approval evidence;
- required to pin the exact authorization functional package SHA:
  `cd76250b9527be91e7e7ac4b3aa658c864cf9172`.

No approval evidence exists at this review checkpoint and no approval is inferred from generic wording.

### 5. Historical approvals remain consumed

All prior execution/privacy/authority approvals remain consumed and permanently non-reusable. None may satisfy either fresh source-format approval requirement.

### 6. Output/persistence boundary remains non-value-bearing

A later separately authorized execution may persist only the categorical result/fail-closed reason, source identity boolean, bounded counters and safety flags. It may not persist or log the full row, any field value, PROPERTY_TYPE or protected derivatives, PROPERTY_ID, owner/holder values, row hashes/exact lengths, parser exception text or source-derived free text.

### 7. No runtime remediation is authorized

The independent parser remains diagnostic-only. The current projector and regex remain unchanged. No class automatically authorizes remediation.

## What this PASS does not authorize

This PASS does not authorize:

- `claimit.ca.gov` access;
- real full-row exposure;
- creation or execution of a source-format network workflow;
- grant or consumption of either fresh approval;
- parser/projector changes;
- regex changes or relaxation;
- trim/case/Unicode normalization;
- logging or persistence expansion;
- remediation;
- additional authority retrieval;
- source approval or registry activation;
- production classification;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## Governance state

Unchanged:

- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- authority provenance: resolved within recorded scope;
- semantic compatibility: unresolved;
- production classification: inactive;
- downstream gates: BLOCKED.

## Next gate

The next permissible action is the explicit owner authorization gate for **both** fresh tokens. Generic wording such as `procedi` or `vai avanti` must not be interpreted as either approval.

Required exact approval references:

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Only after both exact approvals are explicitly granted may separate approval evidence be persisted, each pinned to:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Network execution remains blocked until both valid approval evidence records exist.