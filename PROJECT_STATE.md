# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary, but semantic compatibility with the live source remains unresolved.

A separate bounded diagnostic/remediation evidence proposal has now been prepared and CI-verified on branch:

`m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal`

Proposal package checkpoint SHA:

`020044d3013449fabe566c5164b8f99f9d8cc9ab`

Proposal CI:

`35015429439` — SUCCESS

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_diagnostic_remediation_evidence.v1.json`

Schema:

`schemas/common/property_type_diagnostic_remediation_evidence_proposal.schema.json`

Audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL.md`

### Verified basis

The second bounded semantic execution remains the latest real PROPERTY_TYPE source execution:

- run `34995672539`;
- schema `1.1.0`;
- result `STOPPED_FAIL_CLOSED`;
- stop `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- the v1.1 runner distinguishes UTF-8 encoding failure from decoded format mismatch;
- therefore the observed mismatch was a decoded, non-empty PROPERTY_TYPE that failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- the exact offending value, bytes, hash, length and fragments were not retained and must not be reconstructed or inferred.

The completed authority provenance review established that the current regex is not contradicted by the archived authority and did not authorize trimming, casing, normalization, parser change or regex relaxation.

### Proposed future diagnostic boundary — not yet authorized

If a later human gate and fresh execution/privacy approvals authorize diagnostic source access, the proposal limits it to:

- the exact existing `claimit.ca.gov` endpoint and pinned source identity;
- first canonical member only;
- at most 4 transient data rows;
- stop at the first reproduced format mismatch;
- 1 HEAD maximum;
- 1 Range GET maximum;
- 2 HTTP requests maximum total;
- 131072 source response-body bytes maximum total;
- no retry, redirect, extra range, full-body fallback or automatic widening.

The only proposed persisted semantic evidence is a coarse categorical diagnostic class plus bounded counters and safety flags. Exact PROPERTY_TYPE values, bytes, hashes, lengths, fragments, codepoints, transformed values, full rows, raw bodies, PROPERTY_ID and owner/holder values remain forbidden from persistence/logging.

No diagnostic class authorizes remediation automatically.

### Governance remains fail-closed

- proposal preparation performed no SCO/`claimit.ca.gov` source request;
- no diagnostic execution was performed;
- no network workflow was created;
- runner/parser/regex/normalization/logging/persistence were not modified;
- previous semantic execution/privacy approvals remain CONSUMED + NON-REUSABLE;
- authority archival approval remains CONSUMED + NON-REUSABLE;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED;
- no third real semantic execution is authorized;
- no approval token is defined by this proposal.

## Next Recommended Action

Perform only:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

Review the proposal, schema, audit and contract-test package. Do not access the source or implement remediation during this review.

A PASS would still require a separate explicit diagnostic execution/authorization artifact and fresh execution/privacy approvals before any source access.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
