# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The retained live-source diagnostic chain remains bounded by `ASCII_STRUCTURAL_MISMATCH` and `INDEPENDENT_PARSER_AGREES_FIELD_STRUCTURAL_MISMATCH`.

The policy-decision proposal for nonconforming canonical `PROPERTY_TYPE` has completed human review with decision:

`PASS_POLICY_DECISION_ACCEPTED_AS_DESIGN_IMPLEMENTATION_NOT_AUTHORIZED`

Accepted design policy:

`WHOLE_SOURCE_STOP`

This is now an accepted governance/design decision, recorded as `D-008` in `DECISIONS.md`, but it is **not implemented or activated in runtime**. Existing fail-closed STOP behavior remains operationally unchanged. Semantic compatibility remains unresolved.

## Policy-Decision Review Checkpoint

Review gate:

`HUMAN_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW`

Review branch:

`m3-ca-sco-property-type-nonconforming-row-handling-policy-decision-proposal-review`

Reviewed proposal final HEAD:

`5e6f538a03f0b5e61c4559a27431e9718b29e265`

Reviewed functional package checkpoint:

`33abf635dc2b3f3893300b5e6adf3e35abeefcb8`

Package CI:

`35095481531` — SUCCESS

Proposal final CI:

`35095734936` — SUCCESS

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_DECISION_PROPOSAL_REVIEW.md`

Decision record:

`D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE`

## Accepted Design Contract — Not Yet Implemented

Policy:

`WHOLE_SOURCE_STOP`

Future control disposition after a separately reviewed implementation:

- status: `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- reason: `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- metadata-only: `true`;
- real row/field retained: `false`.

Source continuation:

- continue after triggering row: `false`;
- process later rows after trigger: `false`;
- silent row skip: `false`;
- silent continuation: `false`.

The accepted design does not claim that the source value is semantically invalid in the source system; it defines only the platform's fail-closed handling while source semantic compatibility remains unresolved.

## Validation / Privacy Boundary

Unchanged validation rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

No trim, case conversion, Unicode normalization, alternate-token acceptance, parser/projector change or regex relaxation is authorized.

No persistence of exact/derived PROPERTY_TYPE, real row/field content, hashes, exact row/field lengths, PROPERTY_ID, owner/holder values or source-derived free text is authorized.

Real-row quarantine and row-specific human inspection remain separate privacy expansions and are not authorized.

All historical execution/privacy/authority approvals remain consumed and non-reusable. No fresh execution or privacy approval exists.

## Governance State

- policy decision accepted as design: `true`;
- accepted design policy: `WHOLE_SOURCE_STOP`;
- policy active in runtime: `false`;
- runtime implementation authorized: `false`;
- parser/projector unchanged;
- regex unchanged;
- remediation authorized: `false`;
- additional source execution authorized: `false`;
- source continuation authorized: `false`;
- additional privacy expansion authorized: `false`;
- real-row quarantine persistence authorized: `false`;
- row-specific human inspection authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

Prepare exclusively, offline:

`PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_IMPLEMENTATION_PROPOSAL`

The artifact must identify the smallest deterministic runtime/contract/test changes required to implement the accepted `WHOLE_SOURCE_STOP` design, with rollback and regression coverage. It must not itself modify runtime code, access a real source, define/grant execution approvals, expand privacy exposure, activate source/registry/production classification or enter downstream work.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.
