# PROJECT_STATE.md

Last updated: 2026-09-15

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The live-source format mismatch has now been classified by one bounded diagnostic execution, but no remediation or production semantic compatibility decision has been authorized.

Diagnostic authorization package SHA:
`daeaa7bfb7f7d73a61f011d394cc88393625866c`

Authorization review:
`PASS`

One-shot diagnostic branch:
`m3-ca-sco-property-type-diagnostic-execution-one-shot`

One-shot GitHub Actions run:
`35019840276` — SUCCESS

Execution evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_diagnostic.execution.v1.json`

Execution audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION.md`

## Diagnostic Result

Result status:
`DIAGNOSTIC_CLASSIFIED`

Diagnostic class:
`ASCII_STRUCTURAL_MISMATCH`

Fail-closed reason:
`null`

Verified bounded counters:

- source identity verified: `true`;
- HEAD requests: `1`;
- Range GET requests: `1`;
- HTTP requests total: `2`;
- source response-body bytes read: `131072`;
- transient data rows examined: `1`.

The exact PROPERTY_TYPE value and its bytes/hash/exact length/fragments/codepoints/transformed form were not persisted and must not be reconstructed or inferred.

Under the fixed classifier, this coarse class means the mismatch was not explained solely by surrounding ASCII SPACE/TAB, ASCII case, the combination of those probes, or non-ASCII/disallowed-control content. It does not reveal the source value and does not authorize a parser, regex, trimming, casing, normalization, or remediation change.

## Approval State

Both fresh diagnostic approvals are now `CONSUMED` and permanently non-reusable:

- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`;
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`.

They both pin package SHA `daeaa7bfb7f7d73a61f011d394cc88393625866c` and execution run `35019840276`.

Historical semantic/privacy/authority approvals also remain consumed and non-reusable.

## Safety State

- one-shot diagnostic workflow removed after execution;
- full archive downloaded: `false`;
- raw body persisted: `false`;
- exact PROPERTY_TYPE persisted: `false`;
- PROPERTY_TYPE derivative persisted: `false`;
- full row persisted: `false`;
- PROPERTY_ID persisted: `false`;
- owner/holder values persisted: `false`;
- remediation performed: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Perform only:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_EVIDENCE_REVIEW`

Review the coarse diagnostic evidence and decide what, if anything, it justifies. Do not infer the exact source value and do not implement remediation during the review.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
