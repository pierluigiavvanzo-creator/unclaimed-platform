# M3 California SCO — PROPERTY_TYPE Diagnostic Evidence Review

Date: 2026-09-16

Status: **HUMAN REVIEW COMPLETED — PASS — SOURCE-FORMAT DIAGNOSTIC PROPOSAL JUSTIFIED — NO REMEDIATION AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`

## Reviewed checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- review base branch: `m3-ca-sco-property-type-diagnostic-execution-one-shot`
- review base HEAD: `347375e1a1813cc84dc5a8b7d1f8856824d221ba`
- review base CI: `35020139785` — SUCCESS
- authorization package SHA: `daeaa7bfb7f7d73a61f011d394cc88393625866c`
- diagnostic execution run: `35019840276` — SUCCESS
- execution evidence: `sources/evidence/ca_sco_segment_500_plus.property_type_diagnostic.execution.v1.json`
- execution audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION.md`

The review is repository-only. It performs no `claimit.ca.gov` or SCO request, no authority retrieval, no source-body access, no transient real-row inspection and no remediation.

## Decision

`PASS_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL_JUSTIFIED_NO_REMEDIATION_AUTHORIZED`

The persisted diagnostic evidence is internally consistent with the reviewed execution contract and is sufficient to justify preparation of a separate **offline source-format diagnostic proposal**.

It is **not** sufficient to authorize any parser, regex, trimming, casing, normalization or production-semantic change.

## Evidence integrity review

Persisted result:

- `diagnostic_result_status`: `DIAGNOSTIC_CLASSIFIED`
- `diagnostic_class`: `ASCII_STRUCTURAL_MISMATCH`
- `fail_closed_reason_code`: `null`
- source identity verified: `true`
- HEAD requests: `1`
- Range GET requests: `1`
- HTTP requests total: `2`
- source response-body bytes read: `131072`
- transient data rows examined: `1`

All protected persistence/remediation safety flags are `false`:

- exact PROPERTY_TYPE persisted: `false`
- PROPERTY_TYPE derivative persisted: `false`
- raw body persisted: `false`
- full row persisted: `false`
- PROPERTY_ID persisted: `false`
- owner/holder values persisted: `false`
- full archive downloaded: `false`
- remediation performed: `false`

Both fresh diagnostic approvals were consumed before source access and remain single-use/non-reusable.

The temporary one-shot workflow is absent from the final execution branch state.

## What `ASCII_STRUCTURAL_MISMATCH` establishes

The reviewed deterministic classifier precedence was:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

Within that contract, the observed mismatch was not explained solely by:

- surrounding ASCII SPACE/TAB;
- ASCII case;
- surrounding ASCII SPACE/TAB plus ASCII case;
- non-ASCII content or a disallowed ASCII control character.

The class therefore establishes only a **coarse negative boundary**: the decoded non-empty projected value remained structurally incompatible with the unchanged shape regex after the earlier bounded predicates failed to explain it.

## What the class does not establish

The persisted class does not reveal and this review does not infer:

- the exact PROPERTY_TYPE value;
- its bytes, hash, exact length, fragments or codepoints;
- a specific prefix, suffix, character position or alternate token shape;
- whether the source contains a data-quality anomaly;
- whether the live source evolved away from the archived authority table;
- whether the custom projector mishandled this real row;
- whether a full-row standard-library CSV parse would produce a different field;
- whether the source column meaning changed;
- whether any particular regex relaxation would be correct.

Accordingly, no positive structural theory is promoted to fact by this review.

## Authority branch assessment

The archived California SCO authority has already been human-reviewed and resolved the targeted provenance questions:

- the enumerated California property-type codes use the observed `AA99` shape, subject to the recorded scope boundary;
- `ZZZZ` is directly supported;
- `IN01-IN08` and `IN99` are directly supported.

That authority review also explicitly concluded that the live-source semantic mismatch remained unresolved and did not authorize regex relaxation, trimming, case conversion or normalization.

The present diagnostic evidence creates no contradiction specific enough to justify another authority retrieval. Therefore the `AUTHORITY_DIAGNOSTIC` branch of the earlier `SOURCE_FORMAT_OR_AUTHORITY_DIAGNOSTIC_PROPOSAL` decision map is **not justified at this checkpoint**.

If a later separately authorized source-format diagnostic produces a new, non-value-bearing contradiction that specifically requires authority clarification, that would require a new bounded authority proposal and fresh human gate.

## Source-format / parser branch assessment

Prior offline synthetic differential tests showed that the current custom PROPERTY_TYPE projector agrees with Python `csv.reader(..., strict=True)` on the committed standard-CSV edge-case matrix. That evidence is useful but does not prove the real source row follows only those tested forms or that the projector is universally correct.

The earlier diagnostic/remediation proposal explicitly kept a real-row full-parser crosscheck out of scope because it would broaden transient exposure beyond the narrow field projector and would therefore require a separate privacy design.

The current `ASCII_STRUCTURAL_MISMATCH` result makes a separate source-format diagnostic design the smallest justified next investigation. That design may evaluate whether any further bounded, non-value-bearing source-format or parser discriminator is worth proposing, but this review does not select or execute such a discriminator.

## Remediation decision

The following are **not justified** by the reviewed evidence and remain unauthorized:

- trim-on-ingest or trim-before-validation;
- ASCII uppercasing or case folding;
- combined trim + case conversion;
- Unicode normalization;
- regex relaxation or alternate token acceptance;
- parser replacement or parser modification;
- runtime source-value transformation;
- source approval or registry activation;
- production insurance classification activation.

A direct runtime remediation would overclaim what the coarse class proves.

## Governance state after review

Unchanged and fail-closed:

- current regex: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- parser unchanged;
- trimming/casing/normalization unchanged;
- diagnostic execution approval: consumed / non-reusable;
- transient-row privacy approval: consumed / non-reusable;
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

`PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_PROPOSAL`

The proposal must be design-only and must not perform source or authority network access. It must not reconstruct or infer the unretained value, and it must not change parser, regex, trimming, casing, normalization, persistence or runtime behavior.

If the proposal later contemplates any further real-source inspection, it must define a new narrow privacy boundary and separate fresh single-use execution/privacy approvals pinned to the exact reviewed artifact before any network request.

No remediation or additional source execution is authorized by this review.