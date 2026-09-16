# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | SOURCE-FORMAT DIAGNOSTIC EXECUTED; HUMAN EVIDENCE REVIEW NEXT | run `35090057224` SUCCESS; class `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH` |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- first bounded diagnostic run `35019840276`: `ASCII_STRUCTURAL_MISMATCH`;
- source-format diagnostic proposal and authorization contract completed human review;
- source-format authorization package: `cd76250b9527be91e7e7ac4b3aa658c864cf9172`;
- source-format one-shot execution run `35090057224`: SUCCESS;
- source-format result: `SOURCE_FORMAT_CLASSIFIED`;
- source-format class: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- source identity verified;
- one HEAD + one Range GET, two HTTP requests total;
- 131072 source response-body bytes;
- one transient row examined;
- one transient full-row stdlib cross-check examined;
- both fresh source-format approvals consumed and non-reusable;
- one-shot source-format workflow removed after execution;
- no remediation performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Evidence Meaning — Pending Human Review

The retained class supports the bounded conclusion that, for the one examined row:

- strict full-row UTF-8 decode succeeded;
- strict stdlib CSV parse succeeded;
- canonical 25-column shape was obtained;
- stdlib column index `1` agreed with the custom projector PROPERTY_TYPE field;
- that agreed field still failed the unchanged regex.

The exact field value and its protected derivatives were not persisted and must not be reconstructed or inferred.

This result does not itself authorize parser, regex, trim, case, normalization or other remediation.

## Privacy / Execution Closure

All persisted sensitive-data/remediation safety flags are false. The diagnostic persisted no row/field content, PROPERTY_TYPE, derivatives, PROPERTY_ID, owner/holder values, row hash/exact length, parser exception text or source-derived free text.

Consumed fresh tokens:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

They may not be reused.

## Next Product Work

Perform exclusively:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EVIDENCE_REVIEW`

The review may evaluate the retained coarse class and decide the next governance step, but it must not perform new source access, reuse consumed approvals, reconstruct the exact source value, or silently modify parser/regex/runtime behavior.

## Still Out of Scope

- another real source execution without a new separately reviewed authorization path;
- reuse of any consumed approval;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- new authority retrieval without separate justification;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
