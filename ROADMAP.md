# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | OFFLINE CODE-SHAPE PROVENANCE REVIEW VERIFIED; SEMANTIC COMPATIBILITY STILL UNRESOLVED | second run `34995672539` stopped fail-closed on decoded shape mismatch; provenance review CI `35003900554` SUCCESS; no semantic change justified |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | Streamlit active; Vercel runtime integration decommissioned |

## Completed M3 Work

- California source/legal inventory complete.
- A01 acquisition contracts/adapters and fail-closed real-source boundary implemented.
- Immutable raw storage/provenance and privacy/data-minimization gate implemented.
- SCO source registered disabled and not approved.
- `$500+` bounded transport and structure evidence canonicalized.
- Four CSV members and identical 25-label header verified.
- First-purpose persisted scope minimized.
- `PROPERTY_TYPE` semantic proposal, runner design and synthetic/mock implementation CI verified.
- Historical first owner-authorized real semantic attempt executed once and stopped fail-closed under schema v1.0.0.
- Offline diagnosis established that v1.0 conflated invalid UTF-8 and decoded shape mismatch.
- v1.1 diagnostic remediation implemented, reviewed and promoted to canonical.
- Second bounded execution proposal prepared, reviewed and CI verified.
- Fresh second-run execution/privacy authorization package CI verified; approvals were then consumed by the single authorized run.
- Second owner-authorized bounded real semantic attempt executed exactly once.
- Second execution evidence validated against schema v1.1.0 and hard caps.
- Second one-shot workflow removed immediately after the run; steady state is ABSENT.
- Workflow logs verified to contain no source row or `PROPERTY_TYPE` values.
- Offline code-shape provenance proposal prepared and human-reviewed PASS.
- Repository-only code-shape provenance review completed and CI verified on run `35003900554`.
- Provenance review result: `NO_SEMANTIC_CHANGE_JUSTIFIED_FROM_RETAINED_PROVENANCE`.

## Second Real Semantic Attempt — v1.1

Run: `34995672539`  
Execution SHA: `e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`  
Result: `STOPPED_FAIL_CLOSED`  
Stop: `PROPERTY_TYPE_FORMAT_UNEXPECTED`

Actual budget: 1 HEAD; 1 Range GET; 2 HTTP requests; 131072 source-body bytes; 0 accepted/examined rows; no retry; no widening.

Safe interpretation under v1.1:
- not the invalid-UTF-8 stop class;
- successfully decoded, non-empty projected `PROPERTY_TYPE`;
- failed unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

The offending source value remains intentionally unknown/unpersisted. Fresh second-run execution and privacy approvals are CONSUMED and cannot be reused.

## Offline Provenance Review Result

Verified review branch:
`m3-ca-sco-property-type-code-shape-provenance-offline-review`

Review result SHA:
`b274e9db0a28dae1c9f6a1a25c657978dd27d7b4`

Review CI:
`35003900554` — SUCCESS

Classification:

1. `PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1` — `SUPPORTED_BY_REPOSITORY_EVIDENCE`
2. `GENERAL_CODE_SHAPE_AA99` — `PROVENANCE_INSUFFICIENT`
3. `SPECIAL_CODE_ZZZZ` — `PROVENANCE_INSUFFICIENT`
4. `CALIFORNIA_INSURANCE_CODE_SET` — `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`
5. `CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY` — `SUPPORTED_BY_REPOSITORY_EVIDENCE`

Aggregate: supported `2`; external-reference assertion not archived `1`; provenance insufficient `2`.

The review does not justify trimming, uppercasing, normalization, parser changes, regex modification/relaxation, broader code-domain assumptions or another source execution.

## Current Safety State

- stable `main`: `bfddf8ee3ef32eedb91af888c998ef72f5cdd15e`
- canonical development branch: `m2-state-governance-core`
- canonical development HEAD: `e97c1f62959f603bdd3df79538d4b70255594c70`
- source policy: `PROPOSED`
- real acquisition authorization: false
- registry: disabled/unapproved
- approved real sources: `0`
- semantic compatibility: unresolved
- production classification: inactive
- one-shot workflow: absent
- identity resolution: BLOCKED
- genealogy: BLOCKED
- beneficiary matching: BLOCKED
- outreach: BLOCKED
- claim submission: BLOCKED

## Next Product Work

1. Decide whether to prepare a separate **authority archival / provenance acquisition proposal** to resolve `GENERAL_CODE_SHAPE_AA99` and `SPECIAL_CODE_ZZZZ` and independently verify the externally referenced California insurance-code assertion.
2. Do not access or download external authority content until that separate proposal has passed an explicit human gate.
3. Do not change parser, regex, trimming, casing or normalization based on the current retained evidence.
4. Do not perform another SCO request without a new execution proposal and fresh execution/privacy approvals.
5. Source approval/registry activation, A02 normalization, identity, genealogy, matching and outreach remain independent later gates.

## Out of Scope Until Later Gates

- automatic retry or third SCO request;
- reuse of consumed second-run approvals;
- external authority retrieval without a separately approved provenance-acquisition proposal;
- wider byte/request/row budgets without separate evidence and approval;
- persistence of raw rows or offending values;
- source-value trimming, uppercasing or normalization without evidence;
- regex relaxation without authority-supported evidence and review;
- source approval or registry activation;
- production insurance classification;
- identity resolution, beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
