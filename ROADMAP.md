# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` REAL ATTEMPT STOPPED FAIL-CLOSED; DIAGNOSIS + v1.1 REMEDIATION CANONICAL AND VERIFIED | Historical run `34965097988`; canonical promotion target `36954b89...`; canonical CI `34980324993` SUCCESS; network workflow absent |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; Vercel runtime integration decommissioned |

## Completed M3 Readiness Work

- California source/legal inventory complete.
- A01 acquisition contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` transport and bounded structure evidence canonicalized.
- Four CSV members and identical 25-label header verified.
- First-purpose persisted scope reduced to `PROPERTY_ID` + `PROPERTY_TYPE`.
- `HOLDER_NAME` and identity/address fields prohibited for first triage.
- `PROPERTY_TYPE` semantic proposal, runner design and synthetic/mock runner implementation CI verified.
- One bounded owner-authorized real semantic attempt completed once and stopped fail-closed.
- Derived execution evidence persisted; offending value/bytes intentionally not persisted.
- One-shot network workflow removed immediately after the run.
- Offline evidence review and synthetic diagnosis completed + CI verified.
- Diagnostic remediation implemented and versioned as future execution contract v1.1.0.
- Historical execution contract v1.0.0 preserved frozen and unchanged.
- Human remediation evidence review APPROVED on 2026-09-15.
- Remediation lineage promoted by fast-forward into `m2-state-governance-core`.
- Canonical post-promotion CI `34980324993` SUCCESS.

## Historical Real Semantic Attempt

Run:
`34965097988`

Result:
`STOPPED_FAIL_CLOSED`

Historical schema version:
`1.0.0`

Historical stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Budget actually used:
- 1 HEAD;
- 1 Range GET;
- 2 HTTP requests total;
- 131072 source-body bytes;
- 0 accepted/examined rows;
- no retry;
- no cap widening.

The historical root cause remains unresolved. The prior execution and transient-row privacy approvals were consumed and cannot be reused.

## Canonical Diagnostic Remediation

Promotion target:
`36954b89e57d056801a10a302de568d853b46e0d`

Canonical promotion CI:
`34980324993` — SUCCESS.

Rollback checkpoint:
`checkpoint-pre-property-type-remediation-promotion` -> `c3f0dc7e374d21283358e4e1e8d403f078f08acb`.

Canonical future behavior:
- UTF-8 decode failure -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded shape failure -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- regex remains `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`;
- no source-value normalization;
- no raw values/bytes/hashes/lengths persisted or logged;
- one-shot network workflow remains absent.

Machine contracts:
- historical/frozen schema `1.0.0`: `schemas/common/property_type_semantic_verification_execution.schema.json`;
- future/remediated schema `1.1.0`: `schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`.

## Current Safety State

- stable `main` remains at `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`;
- source policy `PROPOSED`;
- source-level real acquisition authorization false;
- registry disabled/unapproved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- network workflow absent;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Next Product Work

1. Prepare an isolated, evidence-backed proposal for a possible **second bounded `PROPERTY_TYPE` semantic execution** using the canonical v1.1.0 runner.
2. The proposal must make no SCO request and must not recreate a one-shot network workflow yet.
3. Preserve all current request/byte/row caps and privacy constraints unless a separately evidenced change is explicitly approved.
4. Stop at a fresh human decision gate before any real execution.
5. Any second real execution requires both a new semantic-execution approval and a new transient-row privacy approval.
6. Source approval/registry activation, A02 normalization, identity, matching and outreach remain later independent gates.

## Out of Scope Until Later Gates

- automatic retry of the semantic run;
- another SCO request under the consumed authorization;
- wider byte/request/row budgets without separate evidence and approval;
- persisting raw row/value evidence;
- trimming, uppercasing or normalizing source values;
- relaxing the `PROPERTY_TYPE` regex without evidence;
- source approval or registry activation;
- production insurance classification;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
