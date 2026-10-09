# M3 California SCO — PROPERTY_TYPE Diagnostic Execution

Date: 2026-09-15

Status: **ONE-SHOT EXECUTION COMPLETED — EVIDENCE REVIEW REQUIRED**

## Execution identity

- branch: `m3-ca-sco-property-type-diagnostic-execution-one-shot`
- authorization package SHA: `daeaa7bfb7f7d73a61f011d394cc88393625866c`
- GitHub Actions run: `35019840276`
- execution approval: `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- transient-row privacy approval: `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both fresh approvals were verified and changed from `GRANTED_NOT_YET_CONSUMED` to `CONSUMED` before the first source request. They are single-use and non-reusable.

## Bounded execution result

Persisted evidence:

`sources/evidence/ca_sco_segment_500_plus.property_type_diagnostic.execution.v1.json`

Result:

`DIAGNOSTIC_CLASSIFIED`

Diagnostic class:

`ASCII_STRUCTURAL_MISMATCH`

Fail-closed reason:

`null`

Source identity verified:

`true`

Counters:

- HEAD requests: `1`
- Range GET requests: `1`
- HTTP requests total: `2`
- source response-body bytes read: `131072`
- transient data rows examined: `1`

No retry, redirect, additional range, full-body fallback or widening was used.

## Privacy / persistence result

The evidence records that all protected persistence/remediation flags remained `false`:

- full archive downloaded;
- raw response body persisted;
- exact PROPERTY_TYPE persisted;
- PROPERTY_TYPE derivative persisted;
- full row persisted;
- PROPERTY_ID persisted;
- owner/holder values persisted;
- remediation performed.

The exact offending PROPERTY_TYPE value, bytes, hash, exact length, fragments, codepoints and transformed value were not persisted and must not be reconstructed or inferred.

## Bounded interpretation

Under the reviewed deterministic classifier, `ASCII_STRUCTURAL_MISMATCH` is reached only after the earlier diagnostic predicates do not explain the mismatch. Therefore the coarse evidence does not support a mismatch explained solely by:

- surrounding ASCII SPACE/TAB;
- ASCII case only;
- surrounding ASCII SPACE/TAB plus ASCII case;
- non-ASCII or disallowed ASCII control content.

This is a classification of the bounded observation, not authorization to infer the exact source value or to change parser/regex/runtime behavior.

## Governance state

This execution does **not** authorize:

- regex relaxation;
- trimming, casing or normalization in runtime;
- parser changes;
- remediation of any kind;
- source policy approval;
- registry activation;
- production classification;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.

The temporary diagnostic workflow removed itself after execution and cannot be re-run from the final branch state.

## Next gate

Stop at:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`

Human review must decide what the coarse diagnostic evidence justifies. No remediation follows automatically from this execution.
