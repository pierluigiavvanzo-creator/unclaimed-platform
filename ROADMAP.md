# ROADMAP.md

Last updated: 2026-09-16

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | HANDLING PROPOSAL REVIEW PASS; POLICY-DECISION PROPOSAL NEXT | handling proposal review PASS with mandatory tightenings T-1…T-6; no runtime policy selected |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active |

## Verified M3 State

- second semantic execution `34995672539` stopped fail-closed on `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- archived authority supports the enumerated `AA99` shape with scope boundary, `ZZZZ`, and `IN01-IN08` / `IN99`;
- first bounded diagnostic run `35019840276`: `ASCII_STRUCTURAL_MISMATCH`;
- source-format one-shot execution run `35090057224`: SUCCESS;
- source-format class: `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`;
- both source-format approvals consumed and non-reusable;
- source-format evidence review justified an offline handling proposal only;
- nonconforming-row handling proposal package `f29c4423c885d37956bea4aba02e4db241409452` CI `35093840690`: SUCCESS;
- proposal final HEAD `9d5dc3feaa3a9fa63ce5af0dd2c3749a7bee7c87` CI `35094071730`: SUCCESS;
- human handling-proposal review decision: `PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS`;
- no handling policy selected;
- no remediation performed;
- source policy remains `PROPOSED`, registry disabled/unapproved, production classification inactive.

## Review Meaning

The three proposal options remain comparison categories only:

- `WHOLE_SOURCE_STOP`;
- `ROW_LEVEL_DEFER_OR_QUARANTINE`;
- `HUMAN_REVIEW_ROUTE`.

The review accepts the design space but requires the next artifact to separate control disposition from source continuation and to split metadata-only defer from real-row quarantine.

Current runtime behavior remains fail-closed STOP at the mismatch until a later policy is explicitly approved.

## Mandatory Tightenings T-1…T-6

1. model control disposition separately from source continuation;
2. distinguish metadata-only defer from real-row/field quarantine;
3. keep human review metadata-only unless a separate privacy authorization exists;
4. preserve current STOP behavior until explicit policy approval;
5. if continuation is ever proposed, define completeness/audit evidence without silently dropping a row and privacy-review any counters/identifiers;
6. keep policy selection and runtime implementation as separate gates.

## Next Product Work

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL`

It may propose one deterministic handling policy for later human review but may not implement it or authorize real-source execution.

## Still Out of Scope

- runtime handling-policy implementation;
- another real source execution without a new reviewed authorization path;
- reuse of consumed approvals;
- source-value reconstruction or inference;
- parser/projector or regex changes;
- trimming, casing or normalization runtime changes;
- automatic remediation;
- silent row skipping or source continuation;
- real-row quarantine persistence without separately reviewed privacy design;
- row-specific human inspection without separately reviewed privacy design;
- source/registry activation;
- production classification activation;
- identity resolution, genealogy, beneficiary matching, outreach or claim submission.
