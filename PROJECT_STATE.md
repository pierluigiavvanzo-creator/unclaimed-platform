# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Status

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy gates, SCO source governance, transport evidence, source-approval readiness, segmented transport evidence, the `$500+` bounded structure inspection, the two-field privacy boundary, and the `PROPERTY_TYPE` semantic-verification proposal are canonical on `m2-state-governance-core`.

Promoted semantic-proposal SHA:
`06004c9cb61b39692d153d9172c37cebf168ddc5`.

Canonical post-promotion CI:
`34943657157` — SUCCESS for both `quality` and `streamlit-candidate`.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

Streamlit remains the active reviewer target. Repository-side Vercel integration remains decommissioned. Supabase remains untouched.

## Canonical `$500+` Structure Evidence

Exact evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Verified prior facts:
- four non-encrypted DEFLATED CSV members;
- identical 25-label header candidate across all four members;
- prior bounded structure run used HTTP Range only;
- total source-body bytes read `393,216`;
- full archive downloaded `false`;
- CSV data rows parsed `0`;
- record values persisted `false`.

No real CSV data row has yet been sampled.

## Canonical Product Purpose / Field Boundary

Purpose:
`INSURANCE_RELEVANCE_TRIAGE_ONLY`.

Canonical proposed persisted/allowed first-purpose scope:
1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

`HOLDER_NAME` and owner/holder identity/address fields remain prohibited for first triage.

The actual bulk CSV `PROPERTY_TYPE` row-value semantics remain unverified because zero data rows have been sampled.

## Canonical PROPERTY_TYPE Semantic-Verification Proposal

Proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`.

Schema:
`schemas/common/property_type_semantic_verification_proposal.schema.json`.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL.md`.

Verification audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL_VERIFICATION.md`.

The exact future semantic question is intentionally narrow:

In a deterministic bounded prefix sample across all four canonical CSV members, are observed `PROPERTY_TYPE` values NAUPA-style code tokens, and is every observed `IN`-prefixed value one of the official California SCO insurance codes `IN01-IN08` or `IN99`?

A successful sample would remain sample-only evidence. It would not prove the complete dataset domain, global frequencies, or activate production classification.

## Canonical Future Execution Caps

These are project safety caps, not source facts:
- first 4 complete data rows after the verified header per canonical CSV member;
- maximum 4 data rows/member;
- maximum 16 data rows total;
- maximum 1 HEAD request;
- maximum 4 Range GET requests;
- maximum 5 HTTP requests total;
- maximum `131,072` response-body bytes per member Range;
- maximum `524,288` source response-body bytes total;
- maximum `262,144` uncompressed transient bytes/member;
- maximum `1,048,576` uncompressed transient bytes total;
- maximum `32,768` bytes per logical CSV record;
- no full-body request;
- no automatic cap widening;
- no extra Range request if the sample is incomplete inside the fixed prefix cap.

## Privacy / Persistence Boundary

The transient-row privacy blocker remains in force. CSV parsing may transiently expose prohibited owner/holder columns before projection.

The canonical proposal therefore requires:
- separate transient-row privacy approval before any execution;
- in-memory transient processing only;
- no temporary source files;
- no raw ZIP, Range body, full-row, owner/holder, or `PROPERTY_ID` persistence;
- no use or persistence of nonallowlisted values;
- transient buffer retention `0 days`;
- immediate disposal after projection or STOP;
- no raw bytes or record values in logs;
- no per-row `PROPERTY_TYPE` persistence;
- only a derived `PROPERTY_TYPE` summary may eventually be persisted.

## Authorization State

Unchanged and fail-closed:
- source policy `PROPOSED`;
- real acquisition authorized `false`;
- registry `enabled: false`;
- registry `approved_for_use: false`;
- approved real sources `0`;
- semantic execution authorized `false`;
- real row access BLOCKED;
- real PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

Promotion did not implement a runner, create a network workflow, read any real row, or authorize source access.

## Promotion Evidence

Before promotion:
- canonical `830aaaed68bd4d2f9298eaede80b5e67918e935b`;
- candidate `06004c9cb61b39692d153d9172c37cebf168ddc5`;
- ahead `2`;
- behind `0`;
- merge-base exactly `830aaaed68bd4d2f9298eaede80b5e67918e935b`.

Owner explicitly approved:
`m3-ca-sco-property-type-semantic-verification-proposal -> m2-state-governance-core`.

Promotion was a non-force fast-forward to:
`06004c9cb61b39692d153d9172c37cebf168ddc5`.

Canonical post-promotion CI:
`34943657157` — SUCCESS.

## Remaining Blocking Items

Before any semantic row execution or real acquisition:
- `HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`;
- transient full-row privacy approval;
- trusted project privacy policy;
- approved production retention policy;
- reviewed bounded execution runner;
- separate execution approval;
- real-acquisition client review;
- source approval reference;
- source policy approval;
- registry activation.

## Next Recommended Action

Human execution-design review only:

`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`

The next task may design/review a bounded runner against the canonical proposal, but implementation and actual one-shot execution must remain separately gated. Do not read a real row without an explicit later owner approval.
