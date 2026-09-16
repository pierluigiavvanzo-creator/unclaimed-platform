# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | SOURCE-FORMAT EVIDENCE REVIEW PASS; NONCONFORMING ROW-HANDLING PROPOSAL NEXT | run `35090057224` SUCCESS; class `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`; human evidence review completed |
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
- human source-format evidence review completed with decision `PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_NO_RUNTIME_CHANGE_AUTHORIZED`;
- no remediation performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Evidence Review Meaning

For the one examined row, retained evidence supports the bounded conclusion that:

- strict full-row UTF-8 decode succeeded;
- strict stdlib CSV parse succeeded;
- exactly one canonical 25-column record was produced;
- stdlib column index `1` agreed with the custom projector PROPERTY_TYPE field;
- that agreed field still failed the unchanged regex.

Therefore the mismatch is not explained by a projector-vs-stdlib field disagreement for that row.

The exact field value and protected derivatives remain unretained and must not be reconstructed or inferred.

## Closed Diagnostic Branches at This Checkpoint

The evidence review does not justify repeating the same parser-vs-parser source-format diagnostic. The archived SCO authority already supports the accepted property-type shape boundary and is not contradicted by the new evidence, so a repeat authority retrieval is also not justified at this checkpoint.

Neither conclusion authorizes remediation.

## Next Product Work

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL`

The proposal must compare deterministic fail-closed handling options for a canonical PROPERTY_TYPE field that is structurally nonconforming. It must not silently select or implement row skipping, quarantine, transformation, normalization, parser changes or regex relaxation.

Any proposal that would later retain a real nonconforming row, continue real-source processing after a mismatch, expand privacy exposure, or execute against the source requires a separate reviewed authorization path and fresh approvals where applicable.

## Still Out of Scope

- another real source execution without a new separately reviewed authorization path;
- reuse of any consumed approval;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- silent row skipping or source continuation;
- real-row quarantine persistence without separately reviewed privacy design;
- new authority retrieval without separate justification;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.