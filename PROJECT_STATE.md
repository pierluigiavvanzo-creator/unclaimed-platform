# PROJECT_STATE.md

Last updated: 2026-09-16

## Current Milestone

M3 — California Data Spike Readiness + Product Visibility

## Current Status

M0, M1 and M2 are VERIFIED.

PROPERTY_TYPE authority provenance is resolved within the recorded proof boundary. The live-source mismatch was classified by one bounded diagnostic execution as `ASCII_STRUCTURAL_MISMATCH`. Human evidence review justified a separate source-format diagnostic proposal. That proposal and its execution/authorization artifact have now completed human review. Semantic compatibility remains unresolved and no runtime remediation is authorized.

## Source-Format Diagnostic Authorization Review

Gate:

`HUMAN_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW`

Decision:

`PASS`

Review audit:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_AUTHORIZATION_REVIEW.md`

Reviewed authorization functional package:

`cd76250b9527be91e7e7ac4b3aa658c864cf9172`

Authorization package CI:

`35082891083` — SUCCESS

Reviewed final authorization-state HEAD:

`e73681941ef9794d54bef78b53361ea45baccbf9`

Final authorization-state CI:

`35083155026` — SUCCESS

The PASS accepts only the bounded authorization contract. It does not grant network access, real full-row exposure, workflow creation, diagnostic execution, parser/regex/runtime changes or remediation.

## Fresh Approval State

The reviewed artifact defines two fresh approvals:

- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Current state for both:

- single-use: `true`;
- reusable: `false`;
- granted: `false`;
- separate approval evidence required: `true`;
- exact package pin required: `cd76250b9527be91e7e7ac4b3aa658c864cf9172`.

No approval evidence exists yet. Generic wording such as `procedi` or `vai avanti` must not be interpreted as either token.

All prior execution/privacy/authority approvals remain `CONSUMED` and permanently non-reusable.

## Reviewed Execution Boundary — Still Not Authorized

- exact pinned `claimit.ca.gov` endpoint and source identity;
- first canonical ZIP member only;
- maximum 4 transient rows while seeking the first reproduced `ASCII_STRUCTURAL_MISMATCH`;
- maximum 1 transient full-row independent cross-check on that mismatch row;
- maximum 1 HEAD + 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- no redirects/additional ranges/full-body fallback/automatic widening;
- no authority endpoint or other-source access.

T-1 through T-5 are machine-locked, including fixed class precedence, same-row no re-read, explicit `StringIO(..., newline="")` framing, exactly one parsed record, and enumerated fail-closed reasons.

## Safety / Governance State

- parser unchanged;
- regex unchanged: `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- trimming/casing/normalization unchanged;
- source-format diagnostic execution authorized: `false`;
- full-row transient privacy exposure authorized: `false`;
- network workflow authorized: `false`;
- remediation authorized: `false`;
- additional authority retrieval authorized: `false`;
- source policy remains `PROPOSED`;
- registry remains disabled / not approved;
- approved real sources remain `0`;
- production classification remains inactive;
- identity resolution, genealogy, beneficiary matching, outreach and claim submission remain BLOCKED.

## Next Recommended Action

The owner must explicitly grant **both** exact fresh approvals if execution is desired:

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_EXECUTION_BOUNDED`

`APPROVE_PROPERTY_TYPE_SOURCE_FORMAT_DIAGNOSTIC_FULL_ROW_TRANSIENT_PRIVACY_BOUNDED`

Do not create approval evidence or a network workflow before both exact tokens are explicitly granted.

Use `docs/handovers/HANDOVER_CURRENT.md` as the complete restart point.