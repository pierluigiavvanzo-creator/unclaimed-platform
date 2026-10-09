# M3 California SCO — PROPERTY_TYPE Source-Format Diagnostic Execution

Date: 2026-09-16

Status: **EXECUTED — EVIDENCE AWAITING HUMAN REVIEW**

## Purpose

Record the bounded one-shot source-format diagnostic execution authorized by the two fresh owner approvals and preserve only the reviewed coarse evidence.

This audit does not authorize remediation, parser/regex changes, source approval, registry activation or any further network execution.

## Authorization basis

Reviewed authorization functional package:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Authorization review decision:

`PASS`

Fresh approvals consumed for this execution:

1. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
2. `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Both approval evidence records:

- pin the exact reviewed package SHA above;
- are single-use;
- are non-reusable;
- were consumed before the first network request;
- now have status `CONSUMED`.

## One-shot execution

Execution branch:

`m3-ca-sco-property-type-source-format-diagnostic-execution-one-shot`

Workflow run:

`35090057224` — **SUCCESS**

The workflow completed in this order:

1. preflight both fresh approval evidence records;
2. consume both approvals;
3. execute the bounded source-format diagnostic;
4. persist only coarse evidence;
5. remove the one-shot workflow and commit the closed state.

Post-execution closure commit:

`badd71e2e32d32b48fdd255127931222941716dd`

The one-shot workflow is absent from the closed tree.

## Network and source boundary actually used

Persisted counters show:

- source identity verified: `true`;
- HEAD requests: `1`;
- Range GET requests: `1`;
- HTTP requests total: `2`;
- source response-body bytes read: `131072`;
- transient rows examined: `1`;
- full-row cross-check rows examined: `1`.

No retry, redirect, additional Range request, full-body fallback, authority request or alternate source request was introduced by this execution.

## Result

Persisted status:

`SOURCE_FORMAT_CLASSIFIED`

Persisted class:

`INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

Fail-closed reason:

`null`

## Safe interpretation

Within the pre-reviewed classifier precedence, this class supports only the following bounded conclusions for the one row examined:

- strict full-row UTF-8 decoding did not fail;
- strict Python standard-library CSV parsing did not fail;
- the independent parser produced the canonical 25-column shape;
- the independent parser's field at zero-based index `1` agreed with the current custom projector's `PROPERTY_TYPE` field;
- that agreed field still failed the unchanged regex:
  `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Therefore the observed mismatch is **not explained by disagreement between the current custom projector and the independently configured strict standard-library CSV parser for that row**.

This evidence does not reveal, retain or justify reconstruction of the exact field value and does not establish a specific malformed value shape beyond the coarse classifier result.

## Privacy and persistence result

All persisted safety flags are `false`, including:

- full archive downloaded;
- raw response body persisted;
- full row persisted;
- any row field value persisted;
- `PROPERTY_TYPE` persisted;
- `PROPERTY_TYPE` derivative persisted;
- `PROPERTY_ID` persisted;
- owner/holder value persisted;
- row hash persisted;
- exact row length persisted;
- parser exception text persisted;
- source-derived free text persisted;
- remediation performed.

The exact `PROPERTY_TYPE`, its bytes, hash, exact length, fragments, codepoints and transformed forms remain unretained and must not be reconstructed or inferred.

## Approval lifecycle closure

Execution approval evidence:

`sources/evidence/ca_sco_property_type_source_format_diagnostic_execution_approval.v1.json`

Full-row transient privacy approval evidence:

`sources/evidence/ca_sco_property_type_source_format_diagnostic_full_row_transient_privacy_approval.v1.json`

Both are now `CONSUMED` and permanently non-reusable.

## Runtime / governance state

Unchanged:

- current projector unchanged;
- current regex unchanged;
- trimming/casing/normalization unchanged;
- no remediation applied;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved pending human evidence review;
- production classification remains inactive;
- downstream identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EVIDENCE_REVIEW`

That review must evaluate only the retained coarse evidence. It must not reconstruct the source value, re-run the source diagnostic, reuse either consumed approval, change parser/regex/runtime behavior, or apply remediation implicitly.
