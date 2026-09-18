# ROADMAP.md

Last updated: 2026-09-18

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Versioned schemas and validation green |
| M2 — State & Governance Core | VERIFIED | Deterministic governance core verified |
| M3 — California Data Spike | COMPLETE FOR CURRENT MVP-1 HYPOTHESIS; CA PROPERTY_TYPE PATH FROZEN | run `35255228459` + derived evidence |
| M3 Product Visibility — Operations Console | STREAMLIT ACTIVE | reviewer surface verified |
| MVP-1 — First Economically Actionable Case | IN PROGRESS — NY ACCESS PENDING; REMOTE STREAMLIT REVIEWER VERIFIED | remote URL + CI `35345560301` |

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

`receive OSC access instructions — DONE`

`-> observe non-content download constraints — PARTIAL; size metadata requested from OSC`

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

### Follow-up cost → case economics integration

Implemented a thin fail-closed adapter from measured follow-up cost into the existing explicit economics engine.

Checkpoint:

`65748470ca69b71afd859d411a7f5673bb7bd823`

CI:

`35336436604` — SUCCESS.

Verified:

- fully loaded measured cost can populate explicit case economics;
- missing labor rate blocks integration;
- direct machine/data cost cannot be substituted;
- all cost evidence refs remain visible;
- existing fee/value evidence remains preserved;
- no commercial recommendation is introduced.

Audit:

`docs/audits/NY_MVP1_FOLLOW_UP_COST_CASE_ECONOMICS_INTEGRATION_OFFLINE.md`

### Integrated case economics reviewer

Implemented reviewer exposure of both deterministic synthetic economics states:

- ready with documented fully loaded follow-up cost;
- blocked without documented labor-rate/cost.

API:

`/api/reviewer/mvp1/economics/integrated`

Streamlit shows the two states side by side and explicitly labels machine/data-only cost as not fully loaded in the blocked state.

Checkpoint:

`8274660554733d39e7dc7c522676bc709fb90214`

CI:

`35339962098` — SUCCESS.

Audit:

`docs/audits/NY_MVP1_INTEGRATED_CASE_ECONOMICS_REVIEWER_OFFLINE.md`

### Streamlit deployment candidate

Completed:

`PREPARE_NY_MVP1_REVIEWER_DEPLOYMENT_CANDIDATE_OFFLINE`

Candidate state:

`READY_OFFLINE_NOT_REMOTELY_DEPLOYED`

Checkpoint:

`2a4c4bc6e3103bc7d5800facd0fbe4d8a01c2e16`

CI:

`35344178149` — SUCCESS.

Prepared:

- MVP-1 page/title language;
- explicit synthetic/test-only deployment banner;
- synthetic monetary labels;
- pinned Streamlit/FastAPI/Pydantic runtime;
- exact branch/entrypoint/Python 3.11 coordinates;
- no-secrets synthetic deployment path;
- deployment checklist;
- rollback to `6b14edfa39aab0c9bfe7be840820859075c7a708`.

Remote deployment is not yet performed.

### Remote Streamlit deployment

Completed:

`VERIFY_NY_MVP1_STREAMLIT_REMOTE_DEPLOYMENT`

Remote URL:

`https://unclaimed-platform-mvp1-reviewer.streamlit.app/`

Verified from Product Owner remote screenshots plus green deployment-trigger CI:

- MVP-1 title and synthetic/test-only banner;
- READY integrated economics card;
- FAIL-CLOSED integrated economics card;
- no visible runtime error;
- approved real sources = 0;
- real acquisition blocked;
- beneficiary matching blocked;
- no real PII.

State:

`VERIFIED_REMOTE_SYNTHETIC_ONLY`

Non-blocking debt: legacy synthetic M3 raw-artifact label remains visible in the lower audit card.

## MVP-1 Remaining Product Path

`OSC access instructions / Gate 2 / schema discovery`

in parallel with:

`follow-up cost contract DONE -> case-economics integration DONE -> reviewer exposure DONE -> deployment-candidate readiness DONE -> remote deploy VERIFIED -> commercial measurement capture when real source is authorized`

then, once a lawful real source is available:

`real schema mapping -> insurance classification -> candidate -> evidence/provenance -> economics -> reviewer -> human continue/stop`

## Next Product Work

Execute exclusively:

`AWAIT_NY_OSC_FILE_SIZE_METADATA_RESPONSE`

Classification: `A — Product Critical / External Dependency`.

The frontend deployment milestone is closed. OSC access instructions have now arrived. Await OSC's reply with `NYSFINDERS.ZIP` size metadata so `max_download_bytes` can be evidence-based before Gate 2.
