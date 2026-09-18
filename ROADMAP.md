# ROADMAP.md

Last updated: 2026-09-18

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | COMPLETE FOR CURRENT MVP-1 HYPOTHESIS; CA PROPERTY_TYPE PATH FROZEN | run `35255228459` + derived evidence |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | reviewer surface verified |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — NY ACCESS PENDING; FOLLOW-UP COST MEASUREMENT CONTRACT VERIFIED | CI `35321285527` |

## Product Priority

`MVP-1 — First Economically Actionable Case`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## External Real-Source Track

Selected candidate:

`New York OSC Owner Name File`

State:

`REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`

Gate 1:

`CONSUMED / SINGLE USE / NON-REUSABLE`

Official request submission:

`PRODUCT OWNER CONFIRMED COMPLETE`

Current sequence:

`receive OSC access instructions — PENDING`

`-> observe non-content download constraints`

`-> define explicit max_download_bytes`

`-> HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

`-> one bounded first-file memory-only schema discovery`

`-> source/schema decision`

`-> real classification/candidate integration`

No real download or owner PII processing is authorized before Gate 2.

## Offline Product Track — Completed

### Synthetic downstream vertical slice

`SYNTHETIC_POST_SCHEMA_MAPPING -> exact classification -> IN03 candidate -> economics -> reviewer`

Integration commit:

`75156c5419616b67eff658c8c3c8d6775849546c`

CI:

`35317313977` — SUCCESS.

### Recoverable-value / economics evidence

Implemented fail-closed NY pre-contact economics contract:

- exact value remains unknown before permitted claim review/ownership verification;
- statutory 15% location-service cap is not treated as an assumed actual fee;
- actual fee rate requires evidence;
- follow-up cost requires measurement;
- explicit later calculations use cents/basis-points and evidence refs;
- no automatic commercial recommendation.

Reviewer exposure:

- API `/api/reviewer/mvp1/economics/precontact`;
- Streamlit `NY PRE-CONTACT ECONOMICS` card.

Latest cumulative reviewer/economics CI:

`35318092067` — SUCCESS.

### Follow-up cost measurement

Implemented deterministic, provenance-bearing measurement contracts for:

- automated processing cost per candidate;
- source/data cost per candidate;
- human review seconds;
- additional manual research seconds.

Optional documented human labor rate is required before measured human time can become monetary labor cost. Without it, fully loaded follow-up cost remains unavailable.

Checkpoint:

`e9c1bc0e310f1b7b65f4153c90d5efb5d812caa0`

CI:

`35321285527` — SUCCESS.

Audit:

`docs/audits/NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE.md`

## MVP-1 Remaining Product Path

`OSC access instructions / Gate 2 / schema discovery`

in parallel with:

`follow-up cost contract DONE -> case-economics integration -> commercial measurement capture`

then, once a lawful real source is available:

`real schema mapping -> insurance classification -> candidate -> evidence/provenance -> economics -> reviewer -> human continue/stop`

## Next Product Work

Execute exclusively:

`INTEGRATE_NY_MVP1_FOLLOW_UP_COST_WITH_CASE_ECONOMICS_OFFLINE`

Classification: `A — Product Critical`.

Purpose:

Wire only fully computed, evidence-backed follow-up cost into the existing explicit case-economics contract. If no documented labor rate exists, keep the cost unavailable rather than substituting machine/data cost as a false fully loaded cost.
