# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The original live-source mismatch was classified as `ASCII_STRUCTURAL_MISMATCH`; the separately reviewed and authorized source-format diagnostic then produced `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`.

The human source-format diagnostic evidence review accepted that evidence and justified only an offline deterministic handling proposal for a canonical `PROPERTY_TYPE` field that remains structurally nonconforming. That proposal is now prepared and CI-green. No handling option has been selected or implemented.

Semantic compatibility remains unresolved. No runtime remediation, row skipping, quarantine persistence, source continuation or source activation is authorized.

## Nonconforming PROPERTY_TYPE Handling Proposal

Branch:

`m3-ca-sco-property-type-nonconforming-row-handling-proposal`

Functional package checkpoint:

`f29c4423c885d37956bea4aba02e4db241409452`

Package CI:

`35093840690` — **SUCCESS**

Proposal:

`sources/proposals/ca_sco_segment_500_plus.property_type_nonconforming_row_handling.v1.json`

Schema:

`schemas/common/property_type_nonconforming_row_handling_proposal.schema.json`

Audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL.md`

Contract test:

`tests/contract/test_ca_sco_property_type_nonconforming_row_handling_proposal.py`

Proposal status:

`PROPOSAL_ONLY_NOT_AUTHORIZED`

## Evidence Basis

Source-format execution run:

`35090057224` — SUCCESS

Retained class:

`INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`

Source-format evidence review decision:

`PASS_NONCONFORMING_PROPERTY_TYPE_HANDLING_PROPOSAL_JUSTIFIED_NO_RUNTIME_CHANGE_AUTHORIZED`

Base review HEAD:

`27b1a19874449b0170fc0c47328340122d443529`

Base review CI:

`35092673600` — SUCCESS

For the one examined row, strict full-row UTF-8 decode and strict stdlib CSV parse succeeded, exactly one canonical 25-column record was produced, stdlib column index `1` agreed with the current custom projector's PROPERTY_TYPE field, and that agreed field still failed `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The exact field value, its protected derivatives, frequency, cause and source intent remain unknown and must not be inferred.

## Candidate Handling Options — No Selection

The proposal compares exactly three fail-closed options:

1. `WHOLE_SOURCE_STOP`
2. `ROW_LEVEL_DEFER_OR_QUARANTINE`
3. `HUMAN_REVIEW_ROUTE`

`selected_option` remains `null`.

None is authorized by the proposal.

The unchanged validation rule is machine-locked and the proposal forbids silent row skipping, silent source continuation, automatic correction, normalization, regex relaxation and semantic acceptance of a nonconforming value.

## Privacy / Persistence Boundary

Metadata-only handling design does not itself expand privacy exposure.

The following remain explicit future privacy expansions and are **not authorized**:

- retaining a real row or field for quarantine;
- exposing a real row or field for row-specific human review.

Either requires a separate reviewed authorization path before real-source execution or persistence expansion.

The proposal defines no approval token.

## Approval State

All prior execution/privacy/authority approvals remain `CONSUMED` and permanently non-reusable, including:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

No fresh approval exists for handling-policy implementation, source continuation, real-row retention or another real-source execution.

## Governance State

- parser/projector unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- handling policy selected: `false`;
- runtime handling change authorized: `false`;
- remediation authorized: `false`;
- additional source execution authorized: `false`;
- additional privacy expansion authorized: `false`;
- row quarantine persistence authorized: `false`;
- source continuation after nonconformance authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Perform exclusively:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW`

Review the three design options and their fail-closed, completeness and privacy consequences. Do not select or implement runtime behavior during the review, access the source, reconstruct the hidden value, expand privacy exposure, activate the source/registry or enter downstream work.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
