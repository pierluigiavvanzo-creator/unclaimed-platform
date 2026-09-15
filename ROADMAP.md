# ROADMAP.md

Last updated: 2026-09-15

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas, Windows/CI validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic state/gates/audit/budget, Windows/CI green |
| M3 — California Data Spike | `PROPERTY_TYPE` RUNNER DESIGN CANDIDATE + CI VERIFIED — IMPLEMENTATION/EXECUTION BLOCKED | Candidate `b0824d7c...`; CI `34946533156` SUCCESS; runner absent; policy `PROPOSED`; registry disabled |
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
- Bounded semantic runner design and future execution evidence contract created and candidate CI verified.

## Current Candidate

Branch:
`m3-ca-sco-property-type-runner-design`

HEAD:
`b0824d7cbbe693b1d75f3564abac458bcbc5d5e0`

CI:
`34946533156` — SUCCESS.

Candidate contains design/contract/example/test/audit only.

Absent by contract:
- `scripts/ca_sco_property_type_semantic_verification.py`;
- `.github/workflows/ca-sco-property-type-semantic-verification-once.yml`.

## Fixed Runner Design

Future execution sequence:
1. validate canonical proposal and approvals;
2. require transient-row privacy approval before network;
3. one exact HEAD;
4. one fixed Range GET/member;
5. reject non-206 without consuming the unexpected body;
6. verify local member metadata and exact 25-column header;
7. incrementally decompress in memory;
8. parse max four complete rows/member;
9. project only `PROPERTY_TYPE`;
10. discard transient row material immediately;
11. persist derived summary only.

## Fixed Safety Caps

- 4 members;
- 4 rows/member;
- 16 rows total;
- 1 HEAD;
- 4 Range GET;
- 5 HTTP requests total;
- 131,072 body bytes/Range;
- 524,288 body bytes total;
- 1,048,576 uncompressed transient bytes total;
- 32,768 bytes/logical record;
- no additional Range;
- no full-body fallback;
- no automatic cap widening.

## Persistence Boundary

Allowed future evidence:
- aggregate row counts;
- rows/member;
- distinct `PROPERTY_TYPE` codes;
- distinct official insurance codes;
- transport/request counters;
- semantic status/stop reason.

Prohibited:
- raw body;
- full rows;
- `PROPERTY_ID` values;
- owner/holder values;
- per-row `PROPERTY_TYPE` values.

## Current Safety State

- source policy `PROPOSED`;
- real acquisition false;
- registry disabled/unapproved;
- approved real sources `0`;
- runner implementation false;
- semantic execution false;
- transient-row privacy approval absent;
- CSV real-row access BLOCKED;
- PII processing BLOCKED;
- identity resolution BLOCKED;
- beneficiary matching BLOCKED;
- outreach BLOCKED.

## Next Product Work

1. Human decision on `HUMAN_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_APPROVAL`.
2. If approved, implement the bounded runner on a new candidate using existing Range primitives.
3. Validate runner only with synthetic ZIP/mock HTTP behavior.
4. Keep network one-shot workflow absent until a later explicit execution gate.
5. Actual SCO row access requires separate execution approval and transient-row privacy approval.
6. Source approval/registry activation, A02 normalization, identity, matching and outreach remain later
   independent gates.

## Out of Scope Until Later Gates

- real semantic sampling now;
- any real CSV row read;
- automatic budget widening;
- full-body fallback;
- source approval or registry activation;
- beneficiary matching, genealogy, outreach or claim submission;
- promotion to `main` without a separate stable-checkpoint gate.
