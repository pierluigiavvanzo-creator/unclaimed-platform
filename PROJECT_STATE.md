# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Canonical Baseline

M0, M1 and M2 are VERIFIED. M3 California source/legal readiness, acquisition/raw persistence/privacy
gates, SCO source governance, transport evidence, source-approval readiness, data-scope proposals,
segmented transport evidence, the `$500+` bounded structure inspection, and the revised two-field
field/privacy readiness boundary are canonical on `m2-state-governance-core`.

Canonical content-equivalent housekeeping HEAD before the current candidate:
`830aaaed68bd4d2f9298eaede80b5e67918e935b`.

The housekeeping commits only created and immediately removed temporary empty/placeholder setup files;
the resulting tree is the same canonical content tree as the prior verified closure. No policy, registry,
runtime, source evidence, or product contract changed in those housekeeping commits.

Stable `main` remains unchanged at:
`bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`.

## Current Candidate

Branch:
`m3-ca-sco-property-type-semantic-verification-proposal`

Functional candidate HEAD:
`6a39502a19f2127b154b95bf0014a8c76c5ae752`.

Functional CI:
`34942475352` — SUCCESS for both `quality` and `streamlit-candidate`.

Candidate diff from canonical before persistent-doc closure:
- ahead `1`;
- behind `0`;
- merge-base exactly `830aaaed68bd4d2f9298eaede80b5e67918e935b`;
- exactly five added proposal/contract/audit files;
- no policy, registry, runtime adapter, execution runner, or network workflow changes.

## Canonical `$500+` Evidence Reused

Exact structure evidence:
`sources/evidence/ca_sco_segment_500_plus.data_scope.execution.v1.json`.

Verified prior facts:
- four non-encrypted DEFLATED CSV members;
- identical 25-label header candidate;
- local member offsets already evidenced;
- no real data row has yet been sampled;
- prior structure-only run downloaded no full archive and parsed zero CSV data rows.

Canonical field/privacy readiness:
`sources/proposals/ca_sco_segment_500_plus.field_privacy_readiness.v1.json`.

Persisted/allowed first-purpose scope remains:
1. `PROPERTY_ID`
2. `PROPERTY_TYPE`

`HOLDER_NAME` and owner/holder identity/address fields remain prohibited for first triage.

## PROPERTY_TYPE Semantic Verification Candidate

Proposal:
`sources/proposals/ca_sco_segment_500_plus.property_type_semantic_verification.v1.json`.

Schema:
`schemas/common/property_type_semantic_verification_proposal.schema.json`.

Audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SEMANTIC_VERIFICATION_PROPOSAL.md`.

The exact future semantic question is intentionally narrow:

In a deterministic bounded prefix sample across all four canonical CSV members, are `PROPERTY_TYPE`
values NAUPA-style code tokens, and is every observed `IN`-prefixed value one of the official California
SCO insurance codes `IN01-IN08` or `IN99`?

Even a successful sample is explicitly not proof of the complete dataset domain or code frequencies and
does not activate production classification.

## Proposed Future Execution Caps

Project safety caps, not source facts:
- first 4 complete data rows after the verified header per canonical CSV member;
- maximum 4 data rows/member;
- maximum 16 data rows total;
- maximum 1 HEAD request;
- maximum 4 Range GET requests;
- maximum 5 HTTP requests total;
- maximum `131,072` response-body bytes per member Range;
- maximum `524,288` total source response-body bytes;
- maximum `262,144` uncompressed transient bytes/member;
- maximum `1,048,576` uncompressed transient bytes total;
- maximum `32,768` bytes per logical CSV record;
- no full-body request;
- no extra Range request if the sample is incomplete inside the fixed prefix cap.

## Privacy / Persistence Boundary

The canonical transient-row privacy blocker remains in force. CSV row parsing may transiently expose
prohibited columns before projection.

The proposal requires:
- separate transient-row privacy approval before any execution;
- in-memory transient processing only;
- no temporary source files;
- no raw ZIP, Range body, full-row, owner/holder, or `PROPERTY_ID` persistence;
- no nonallowlisted value use or persistence;
- transient buffer retention `0 days`;
- immediate disposal after projection or STOP;
- no raw bytes or record values in logs;
- no per-row `PROPERTY_TYPE` persistence.

Only a derived `PROPERTY_TYPE` summary may eventually be persisted.

## Proposal Outcomes

- `SAMPLE_COMPATIBLE_INSURANCE_CODE_OBSERVED` — bounded sample is code-shaped and at least one official
  insurance code is observed; still does not activate production.
- `SAMPLE_CODE_SHAPE_COMPATIBLE_NO_INSURANCE_CODE_OBSERVED` — explicitly inconclusive for insurance
  mapping.
- `STOPPED_FAIL_CLOSED` — any transport, CSV, privacy, semantic, row, request, or byte condition fails.

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

No new SCO network/body access occurred while preparing or testing this proposal.

## Next Recommended Action

Human promotion gate only:

`m3-ca-sco-property-type-semantic-verification-proposal -> m2-state-governance-core`

Promotion, if approved, remains non-authorizing. After canonical CI, a separate
`HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW` is required before implementation/execution may read even
one real CSV data row.
