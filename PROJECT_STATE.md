# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The original live-source mismatch was classified as `ASCII_STRUCTURAL_MISMATCH`; the separately reviewed and authorized source-format diagnostic then produced `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`.

The nonconforming-row handling proposal has now completed human review with decision:

`PASS_WITH_MANDATORY_POLICY_DECISION_TIGHTENINGS`

The review accepts the proposal as a valid fail-closed design comparison but does not select or authorize a runtime handling policy.

Semantic compatibility remains unresolved. No runtime remediation, row skipping, quarantine persistence, source continuation or source activation is authorized.

## Handling Proposal Review

Gate:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW`

Review branch:

`m3-ca-sco-property-type-nonconforming-row-handling-proposal-review`

Reviewed proposal final HEAD:

`9d5dc3feaa3a9fa63ce5af0dd2c3749a7bee7c87`

Reviewed functional package checkpoint:

`f29c4423c885d37956bea4aba02e4db241409452`

Package CI:

`35093840690` — SUCCESS

Proposal final CI:

`35094071730` — SUCCESS

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_PROPOSAL_REVIEW.md`

## Candidate Options — Still Unselected

The reviewed proposal compares:

1. `WHOLE_SOURCE_STOP`
2. `ROW_LEVEL_DEFER_OR_QUARANTINE`
3. `HUMAN_REVIEW_ROUTE`

No option is selected or implemented.

The existing fail-closed runtime behavior remains unchanged: stop when the nonconforming PROPERTY_TYPE condition is encountered.

## Mandatory Next-Artifact Tightenings

The next policy-decision proposal must incorporate:

- T-1: separate control disposition from source continuation;
- T-2: distinguish metadata-only defer from real-row/field quarantine;
- T-3: keep human review metadata-only unless separate privacy authorization exists;
- T-4: preserve current STOP behavior until a later policy is explicitly approved;
- T-5: any future continuation proposal must define non-value-bearing completeness/audit evidence and privacy-review any counters/identifiers;
- T-6: policy selection and runtime implementation remain separate gates.

## Validation / Privacy Boundary

Unchanged validation rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, regex relaxation or alternate token acceptance is authorized.

Real-row/field retention for quarantine and row-specific human inspection remain privacy expansions and are not authorized.

All historical execution/privacy/authority approval tokens remain consumed and non-reusable.

## Governance State

- parser/projector unchanged;
- regex unchanged;
- handling policy selected: `false`;
- runtime handling change authorized: `false`;
- remediation authorized: `false`;
- additional source execution authorized: `false`;
- additional privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- source continuation after nonconformance authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL`

The artifact must incorporate T-1 through T-6 and may propose a single deterministic policy for subsequent human review. It must not implement runtime behavior, access the source, expand privacy exposure, activate source/registry/production classification or enter downstream work.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
