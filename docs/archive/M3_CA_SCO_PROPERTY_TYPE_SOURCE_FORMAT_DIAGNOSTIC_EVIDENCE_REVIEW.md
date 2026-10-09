# M3 California SCO — PROPERTY_TYPE Source-Format Diagnostic Evidence Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS — NONCONFORMING ROW-HANDLING PROPOSAL JUSTIFIED — NO RUNTIME CHANGE AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EVIDENCE_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- review base branch: `m3-ca-sco-property-type-source-format-diagnostic-execution-one-shot`
- review base HEAD: `dbf4826a013daf604a48719c5b2dd92980f1a335`
- final execution CI: `35090434652` — SUCCESS
- reviewed authorization package: `cd76250b9527be91e7e7ac4b3aa658c864cf9172`
- one-shot execution run: `35090057224` — SUCCESS
- execution evidence: `sources/evidence/ca_sco_segment_500_plus.property_type_source_format_diagnostic.execution.v1.json`
- execution audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION.md`
- execution evidence contract test: `tests/contract/test_ca_sco_property_type_source_format_diagnostic_execution_evidence.py`

This review is repository-only. It performs no `claimit.ca.gov` request, no authority request, no source-body access, no real-row reinspection, no value reconstruction and no remediation.

## Decision

`PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_NO_RUNTIME_CHANGE_AUTHORIZED`

The retained source-format diagnostic evidence is internally consistent with the reviewed execution contract and is sufficient to justify preparation of a separate **offline deterministic handling proposal** for rows whose `PROPERTY_TYPE` is nonconforming under the current authoritative shape boundary.

The evidence is **not** sufficient to authorize acceptance, transformation, normalization, parser change, regex change, row skipping, quarantine persistence, source activation or any other runtime behavior.

## Evidence integrity review

Persisted result:

- `diagnostic_result_status`: `SOURCE_FORMAT_CLASSIFIED`
- `source_format_diagnostic_class`: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`
- `fail_closed_reason_code`: `null`
- source identity verified: `true`
- HEAD requests: `1`
- Range GET requests: `1`
- HTTP requests total: `2`
- source response-body bytes read: `131072`
- transient rows examined: `1`
- full-row cross-check rows examined: `1`

All protected persistence/remediation safety flags are `false`. No row/field content, `PROPERTY_TYPE`, derivative, `PROPERTY_ID`, owner/holder value, row hash, exact row length, parser exception text, raw body or source-derived free text was persisted. No remediation was performed.

Both fresh source-format approvals were consumed before source access and remain single-use/non-reusable:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

The temporary source-format one-shot workflow is absent from the final execution tree.

## What the source-format class establishes

Under the reviewed fixed classifier precedence, for the one examined row:

1. strict full-row UTF-8 decoding succeeded;
2. strict Python stdlib `csv.reader` parsing succeeded;
3. exactly one canonical 25-column CSV record was produced;
4. the stdlib field at zero-based index `1` agreed with the current custom projector's `PROPERTY_TYPE` field;
5. the agreed field still failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

Therefore, for that row, the observed mismatch is not explained by disagreement between the current custom projector and the independently configured strict stdlib CSV comparator.

Combined with already retained repository evidence that the canonical source header places `PROPERTY_TYPE` at zero-based index `1`, this is sufficient to treat the observed condition as a **field-level nonconformance at the canonical PROPERTY_TYPE position**, bounded to the one examined row.

## Authority interaction

The already archived and human-reviewed California SCO authority established, within its recorded scope boundary, that:

- enumerated California property-type codes use the `AA99` shape except the explicit special token `ZZZZ`;
- `ZZZZ` is directly supported;
- insurance codes `IN01-IN08` and `IN99` are directly supported.

The current source-format evidence does not contradict the authority document. Instead, it shows that the one examined live-source field remains structurally outside the unchanged accepted shape after an independent CSV parser agrees on the field boundary.

No additional authority retrieval is justified at this checkpoint because the unresolved question is no longer whether the archived authority supports the accepted code shape.

## What this review does not establish

The retained evidence does not reveal and this review does not infer:

- the exact `PROPERTY_TYPE` value;
- its bytes, hash, exact length, fragments, codepoints or transformed form;
- a specific malformed token shape;
- whether the value is an isolated source-data anomaly;
- whether the source intentionally introduced a new semantic token;
- how frequently this condition occurs;
- whether other rows are affected;
- whether the entire source should be rejected because of one nonconforming row;
- whether a nonconforming row should be skipped, quarantined, retained for human review or handled in another way;
- whether any trim, case conversion, normalization or regex relaxation would be correct.

No positive theory about the hidden source value is promoted to fact.

## Diagnostic branch assessment

A further parser-vs-parser source-format diagnostic is **not justified** by the retained evidence at this checkpoint: the independently configured strict stdlib parser and current projector already agreed on the relevant field for the examined row.

A repeat of the same bounded diagnostic would therefore add source exposure without addressing the remaining product decision.

A new real-source diagnostic would require a separate proposal, privacy boundary, execution authorization and fresh single-use approvals; none is authorized by this review.

## Remediation / handling assessment

Direct remediation remains unjustified. In particular, this review does not authorize:

- trim-on-ingest or trim-before-validation;
- ASCII uppercasing or case folding;
- Unicode normalization;
- regex relaxation or alternate token acceptance;
- parser replacement or modification;
- silent row skipping;
- silent source-level continuation after a mismatch;
- persistence of a real nonconforming row for later inspection;
- source approval or registry activation;
- production insurance classification activation.

However, the evidence is now sufficient to justify designing a deterministic policy for the **known condition** “canonical `PROPERTY_TYPE` field is structurally nonconforming”. That policy must preserve fail-closed behavior and explicitly define how the platform should stop, defer, quarantine, or require human review without silently changing source semantics.

## Governance state after review

Unchanged and fail-closed:

- current projector unchanged;
- current regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- source-format execution approvals: consumed / non-reusable;
- source-format full-row privacy approval: consumed / non-reusable;
- remediation authorized: `false`;
- additional source execution authorized: `false`;
- source policy: `PROPOSED`;
- registry: disabled / not approved;
- approved real sources: `0`;
- semantic compatibility: unresolved;
- production classification: inactive;
- identity resolution: BLOCKED;
- genealogy: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED;
- claim submission: BLOCKED.

## Next single action

Prepare only an offline, separate:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL`

The proposal is design-only. It must not access the source or authority network and must not inspect or reconstruct the unretained value.

At minimum, the proposal must:

- preserve the unchanged current validation rule while comparing deterministic fail-closed handling options;
- explicitly distinguish whole-source stop, row-level defer/quarantine, and human-review routing rather than choosing behavior implicitly;
- define non-value-bearing reason/status codes and bounded observability;
- forbid silent correction, normalization or semantic acceptance of the nonconforming value;
- define any privacy/persistence implications before proposing retention of a real row or protected field;
- require a separate reviewed authorization path before any future real-source execution or privacy expansion;
- leave source policy, registry and production classification inactive unless separately approved.

No runtime handling change, remediation, source activation or additional execution is authorized by this review.