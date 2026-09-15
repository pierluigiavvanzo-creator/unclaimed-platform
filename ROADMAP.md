# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` RUNNER IMPLEMENTATION CANONICAL + SYNTHETIC/MOCK CI VERIFIED — REAL EXECUTION BLOCKED | Promoted `3f612837...`; canonical CI `34961511401` SUCCESS; workflow absent; policy `PROPOSED`; registry disabled |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; Vercel runtime integration decommissioned |

## Completed M3 readiness work

- California source/legal inventory complete.
- A01 contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` transport and bounded structure evidence canonicalized.
- Four CSV members and identical 25-label header verified with zero data rows sampled.
- First-purpose persisted scope reduced to `PROPERTY_ID` + `PROPERTY_TYPE`.
- `HOLDER_NAME` and identity/address fields prohibited for first triage.
- Transient CSV prohibited-field exposure isolated as a separate privacy boundary.
- `PROPERTY_TYPE` semantic-verification proposal canonical + CI verified.
- Bounded semantic runner design and execution evidence contract canonical + CI verified.
- Bounded `PROPERTY_TYPE` runner implementation promoted to canonical after synthetic/mock-only verification.

## Canonical Runner Implementation

Promoted functional SHA:
`3f612837e4dbb86839942555c34b9384ff4e99a1`

Canonical post-promotion CI:
`34961511401` — SUCCESS.

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Implementation audit:
`docs/audits/M3_CA_SCO_PROPERTY_TYPE_RUNNER_IMPLEMENTATION.md`

Implementation authorization:
`sources/evidence/ca_sco_segment_500_plus.property_type_runner_implementation_approval.v1.json`

Network one-shot workflow remains absent:
`.github/workflows/ca-sco-property-type-semantic-verification-once.yml`.

## Promotion Evidence

Before promotion:
- canonical `6105c22a7d31df7afca00282eff7e9798e98b868`;
- candidate `3f612837e4dbb86839942555c34b9384ff4e99a1`;
- ahead `4`;
- behind `0`;
- merge-base exactly canonical `6105c22a7d31df7afca00282eff7e9798e98b868`.

Promotion used a non-force fast-forward.

## Fixed Safety Caps

- 4 members;
- 4 rows/member;
- 16 rows total;
- 1 HEAD;
- 4 Range GET;
- 5 HTTP requests total;
- 131,072 body bytes/Range;
- 524,288 body bytes total;
- 262,144 uncompressed transient bytes/member;
- 1,048,576 uncompressed transient bytes total;
- 32,768 bytes/logical record;
- no additional Range;
- no full-body fallback;
- no automatic cap widening.

Ignored Range/non-206 causes STOP before the unexpected body is consumed.

## Synthetic / Mock Verification

Covered and passing:
- official insurance code sample -> compatible success;
- no insurance code -> inconclusive;
- unknown `IN` code -> fail closed;
- non-206 Range -> stop without body read;
- header mismatch -> fail closed;
- row column-count mismatch -> fail closed;
- missing execution/privacy approval -> fail before transport;
- execution evidence remains derived-summary only;
- live CLI path is explicit opt-in;
- network one-shot workflow remains absent.

CI evidence:
- functional `34951460475` — SUCCESS;
- candidate docs closure `34951888095` — SUCCESS;
- canonical post-promotion `34961511401` — SUCCESS.

## Current Safety State

- source policy `PROPOSED`;
- real acquisition false;
- registry disabled/unapproved;
- approved real sources `0`;
- runner implementation canonical but real execution unauthorized;
- real semantic execution false;
- transient-row privacy approval absent;
- CSV real-row access BLOCKED;
- PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

No new SCO network/body access occurred during implementation or promotion.

## Next Product Work

1. Human decision at `HUMAN_PROPERTY_TYPE_SEMANTIC_EXECUTION_REVIEW`.
2. Any real bounded semantic execution requires explicit execution approval **plus** transient-row privacy approval.
3. Keep the one-shot network workflow absent until that later gate is explicitly authorized.
4. Keep source policy `PROPOSED` and registry disabled until separate source-approval gates are satisfied.
5. Source approval/registry activation, A02 normalization, identity, matching and outreach remain later independent gates.

## Out of Scope Until Later Gates

- real semantic sampling now;
- any real CSV row read;
- creation/execution of the one-shot network workflow without explicit approval;
- automatic budget widening;
- full-body fallback;
- source approval or registry activation;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
