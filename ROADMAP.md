# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | NONCONFORMING PROPERTY_TYPE HANDLING PROPOSAL PREPARED; HUMAN REVIEW NEXT | proposal package `f29c4423...9452`; CI `35093840690` SUCCESS; no option selected |
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
- both fresh source-format approvals consumed and non-reusable;
- human source-format evidence review decision: `PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_NO_RUNTIME_CHANGE_AUTHORIZED`;
- nonconforming-row handling proposal package: `f29c4423c885d37956bea4aba02e4db241409452`;
- proposal package CI `35093840690`: SUCCESS;
- no handling option selected;
- no remediation performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Nonconforming Handling Proposal

The proposal compares exactly three fail-closed designs:

- `WHOLE_SOURCE_STOP`;
- `ROW_LEVEL_DEFER_OR_QUARANTINE`;
- `HUMAN_REVIEW_ROUTE`.

No option is selected or authorized.

The proposal keeps the validation rule unchanged:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

and forbids silent row skipping, silent source continuation, semantic acceptance, automatic correction, trim/case/Unicode normalization and regex relaxation.

## Privacy Boundary

Real-row/field retention for quarantine and row-specific human inspection are explicitly classified as future privacy expansions. Neither is authorized by the proposal.

Any future real-source execution, source continuation after a mismatch, real-row retention or row-specific inspection requires a separate reviewed authorization path and fresh approvals where applicable.

## Next Product Work

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW`

The review may compare the three options and require tightening. It must not silently select or implement runtime handling, access the source, inspect/reconstruct the hidden value, retain a real row, or activate source/registry/production classification.

## Still Out of Scope

- handling-policy implementation before a later explicit gate;
- another real source execution without a new separately reviewed authorization path;
- reuse of any consumed approval;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- silent row skipping or source continuation;
- real-row quarantine persistence without separately reviewed privacy design;
- row-specific human inspection without separately reviewed privacy design;
- new authority retrieval without separate justification;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
