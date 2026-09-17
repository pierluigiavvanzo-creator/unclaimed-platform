# ROADMAP.md

Last updated: 2026-09-17

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | REAL EXECUTION COMPLETED; CURRENT SOURCE FAIL-CLOSED / NOT APPROVED | run `35222675324`; D-008 triggered on real source under adopted transport baseline |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | reviewer surface active |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — SELECT ALTERNATE REAL SOURCE NEXT | approved real source -> acquisition -> normalization -> insurance classification -> candidate -> evidence -> economics -> reviewer -> human decision |

## Product Priority

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

The California `$500+` source has now reached the real semantic boundary and deterministically stopped under D-008. Do not spend more time on identical diagnostics or retries. Reopen California only if a new contradiction appears or the Product Owner explicitly authorizes redesign of the PROPERTY_TYPE semantic contract.

## Verified Real-Source Execution

Execution:

`EXECUTE_PROPERTY_TYPE_NONCONFORMING_ROW_HANDLING_POLICY_V1_2_REAL_SOURCE_EXECUTION_ONCE`

Run:

`35222675324` — **SUCCESS**

Artifact:

`10496599995`

Digest:

`sha256:3e52cdff838de4dfa73bf62b0361af6938be73f2aa381c68ecaf8bc1b1d37fe9`

Observed outcome:

- adopted transport metadata matched exactly;
- 1 HEAD + 1 Range request;
- 131072 source-body bytes read;
- `STOPPED_FAIL_CLOSED`;
- `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- D-008 status `PROPERTY_TYPE_NONCONFORMING_STOPPED`;
- D-008 reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`;
- no raw/row/person data persisted;
- no retry performed.

Both 2026-09-17 fresh approval refs are consumed and non-reusable.

## California Decision

Evidence review:

`PASS_EXECUTION_EVIDENCE_ACCEPTED`

Source decision:

`REJECT_CA_SCO_500_PLUS_AS_APPROVED_MVP1_SOURCE_UNDER_CURRENT_V1_2_CONTRACT`

Source policy remains `PROPOSED`; registry remains disabled/unapproved; approved real source count remains `0`.

## Commercial Interpretation

The blocker is no longer transport readiness. It is source/contract compatibility. Another execution under the same unchanged contract has no credible path to new product value and is therefore deprioritized.

The shortest path to MVP-1 is now:

`alternate lawful source -> bounded source verification -> source approval -> MVP-1 vertical slice`

Once a source is approved, immediately prioritize:

`acquisition -> normalization -> insurance classification -> candidate -> provenance/evidence -> case economics -> Streamlit reviewer -> human continue/stop`

Collect the real commercial baseline specified in `PRODUCT_STRATEGY_MVP1.md`; do not invent thresholds before real case data.

## Next Product Work

`SELECT_ALTERNATE_REAL_SOURCE_FOR_MVP1`

Classification:

`A — Product Critical`

Required output should be a short ranked-by-fit candidate set based on factual criteria, followed by selection of the smallest lawful bounded verification path. Do not rank political choices; this is purely a technical/product source selection.

Evaluate each source for:

- access legality / source terms;
- provenance;
- freshness/stability;
- machine readability;
- relevant insurance/unclaimed-property signal;
- privacy burden;
- expected integration effort;
- compatibility with current schemas;
- credible time to first economically actionable case.

Prefer existing repository components and public official sources over new custom infrastructure.
