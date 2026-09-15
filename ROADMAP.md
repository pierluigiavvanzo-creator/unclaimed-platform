# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | BOUNDED AUTHORITY PROVENANCE ACQUISITION PROPOSAL VERIFIED; HUMAN REVIEW REQUIRED | authority proposal package `963c205b...`; CI `35005451605` SUCCESS; retrieval not authorized |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; Vercel runtime integration decommissioned |

## Completed M3 Work

- California source/legal inventory complete.
- A01 acquisition contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` bounded transport and structure evidence canonicalized.
- Four CSV members and identical 25-label header verified.
- First-purpose persisted scope minimized.
- Historical first real semantic attempt stopped fail-closed under schema v1.0.0.
- v1.1 diagnostic remediation implemented, reviewed and promoted.
- Second bounded real semantic attempt executed exactly once under v1.1.0 and stopped fail-closed on decoded shape mismatch.
- Second execution/privacy approvals consumed and non-reusable.
- One-shot workflow removed; steady state ABSENT.
- Offline code-shape provenance proposal prepared and human-reviewed PASS.
- Repository-only provenance review completed and CI verified.
- Review decision: `NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE`.
- Separate authority archival/provenance acquisition proposal prepared and CI verified.

## Offline Provenance Review Result

Classification:

1. `PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1` — `SUPPORTED_BY_REPOSITORY_EVIDENCE`
2. `GENERAL_CODE_SHAPE_AA99` — `PROVENANCE_INSUFFICIENT`
3. `SPECIAL_CODE_ZZZZ` — `PROVENANCE_INSUFFICIENT`
4. `CALIFORNIA_INSURANCE_CODE_SET` — `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`
5. `CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY` — `SUPPORTED_BY_REPOSITORY_EVIDENCE`

Aggregate: supported `2`; external-reference assertion not archived `1`; provenance insufficient `2`.

No semantic/runtime change is justified by retained provenance.

## Authority Provenance Proposal

Branch:
`m3-ca-sco-property-type-authority-provenance-acquisition-proposal`

Verified proposal package SHA:
`963c205b662cf56260ca7af14d71c65a6916c30f`

Verified CI:
`35005451605` — SUCCESS

Artifacts:

- `schemas/common/property_type_authority_provenance_acquisition_proposal.schema.json`
- `sources/proposals/ca_sco_segment_500_plus.property_type_authority_provenance_acquisition.v1.json`
- `tests/contract/test_ca_sco_property_type_authority_provenance_acquisition_proposal.py`

Proposal status: `PROPOSAL_ONLY_NOT_AUTHORIZED`.

The proposal is limited to the already-retained official SCO authority reference and defines a future bounded archive contract: one exact HTTPS GET, one host, one PDF/all pages, no redirect, no retry, immutable SHA-256 archive and versioned provenance metadata.

No authority request/download was performed while preparing this proposal.

## Current Safety State

- stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- canonical development branch: `m2-state-governance-core`
- source policy: `PROPOSED`
- authority retrieval authorized by current proposal: false
- real source acquisition authorization: false
- registry: disabled/unapproved
- approved real sources: `0`
- semantic compatibility: unresolved
- production classification: inactive
- semantic one-shot workflow: absent
- identity resolution: BLOCKED
- genealogy: BLOCKED
- beneficiary matching: BLOCKED
- outreach: BLOCKED
- claim submission: BLOCKED

## Next Product Work

1. Perform `HUMAN_PROPERTY_TYPE_AUTHORITY_PROVENANCE_ACQUISITION_PROPOSAL_REVIEW`.
2. Review only the proposal/schema/contract package; do not retrieve the external authority during review.
3. If review passes and retrieval is desired, create a separate explicit authority-archival execution/authorization artifact before any network access.
4. After any later archive operation, perform a separate human provenance review before changing semantic assumptions.
5. Do not change parser, regex, trimming, casing or normalization from the current evidence.
6. Do not perform another SCO semantic execution without a new proposal and fresh execution/privacy approvals.

## Out of Scope Until Later Gates

- authority download merely because the proposal exists;
- additional authority discovery or link following;
- SCO dataset or `claimit.ca.gov` access for this authority task;
- automatic retry or third SCO semantic request;
- reuse of consumed second-run approvals;
- persistence of raw SCO rows or offending values;
- source-value trimming, uppercasing or normalization without evidence;
- regex/parser modification without authority-supported evidence and review;
- source approval or registry activation;
- production insurance classification;
- identity resolution, beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
