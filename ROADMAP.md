# ROADMAP.md

Last updated: 2026-09-19

## Current Override — Fifth Attempt Proposal Merged / Runner Preparation Offline

PR #14 is merged at:

`289aabfc69a363683d978391623716fe13bb7b5b`

Verified proposal CI:

`35460348569 — SUCCESS`

No separate post-merge CI run was observed during this reconciliation.

The fifth proposal remains governance-only and does not authorize OSC access or execution.
Operational fifth-attempt artifacts are not yet prepared.

Current bounded task:

`PREPARE_NY_OSC_FIFTH_ATTEMPT_RUNNER_AND_CONTRACTS_OFFLINE`

Required scope:

- prepare a dedicated attempt-5 runner;
- prepare fifth transient-local and transient-PII approval schemas;
- prepare both approval templates with status `NOT_GRANTED`;
- bind attempt number 5 and exact fifth approval phrases;
- require distinct approval refs;
- preserve one-download/zero-retry and unchanged caps;
- require successful runner checkpoint/CI before any approval can become operational;
- perform all authorization checks before creating the temp directory;
- reuse the shared schema-discovery parser and verified v1.1 transient execution bridge;
- do not reuse fourth runner or fourth approvals;
- no OSC access, preflight, download, owner-file opening, approval grant or execution.

## Historical Override — Fifth Attempt Proposal Prepared Offline (Pre-Review/Merge)

Completed:

`PREPARE_NY_OSC_FIFTH_BOUNDED_ATTEMPT_PROPOSAL_OFFLINE`

State:

`PROPOSED_NOT_AUTHORIZED / ONE DOWNLOAD MAX / ZERO RETRY / ZERO SOURCE ACCESS`

The proposal preserves all current limits and uses the merged structural-diagnostic capability
as its only new diagnostic objective. It does not modify parser acceptance behavior.

Before any real fifth attempt, separate future work would still be required for:

1. human review of this proposal;
2. offline preparation and CI verification of the fifth runner and approval templates;
3. two explicit single-use approvals;
4. a separately authorized fresh exact listing preflight;
5. a separately authorized one-time execution.

Current next gate:

`HUMAN_REVIEW_NY_OSC_FIFTH_BOUNDED_ATTEMPT_PROPOSAL`

## Current Override — PR #12 Merged / Fifth-Attempt Preparation Is Offline Only

PR #12 is merged into the canonical development branch at:

`dc603d68ff6aeb234c2ad793b85fa1bb2f4805c8`

The merged package contains structural-only NY OSC diagnostics, the remediated transient-local
execution bridge, and the additive v1.1.0 execution-result contract while preserving historical
v1.0.0 receipts.

Verified PR CI:

`35446925652 — SUCCESS`

No separate post-merge CI run was observed during reconciliation.

Fourth-attempt approvals are consumed and non-reusable; zero retry remains binding. No fifth
source access, preflight, download or execution is authorized.

Current bounded task:

`PREPARE_NY_OSC_FIFTH_BOUNDED_ATTEMPT_PROPOSAL_OFFLINE`

This task is repository-only governance preparation. It must not create granted approvals or
perform source access.

## Historical Override — Fourth Attempt Consumed / Structural Telemetry Candidate (Pre-Merge)

Completed real execution:

`EXECUTE_NY_OSC_FOURTH_BOUNDED_ATTEMPT_ONCE_AFTER_PASSED_FRESH_LISTING_PREFLIGHT`

Result:

`BLOCKED / UNEXPECTED_DATA_FIELD_COUNT`

Both fourth approvals are consumed and non-reusable; zero retry remains binding. The raw ZIP
was logically deleted and no owner values were returned or persisted.

Current offline implementation candidate:

`IMPLEMENT_NY_OSC_STRUCTURAL_DIAGNOSTIC_TELEMETRY_OFFLINE`

It distinguishes raw delimiters from parser-structural delimiters using non-PII counters only,
while preserving the existing 14-field fail-closed rule. CI `35444131105` verified both `quality` and `streamlit-candidate` as SUCCESS on the
isolated candidate branch. No fifth download is authorized.

## Current Override — Fourth Attempt Approvals Granted Offline

Completed:

`REGISTER_NY_OSC_FOURTH_ATTEMPT_APPROVALS_OFFLINE`

State:

`GRANTED_NOT_CONSUMED / SINGLE USE / ZERO RETRY / NO SOURCE ACCESS`

Both exact approvals are bound to the integrated runner and successful CI. No preflight or
execution occurred. The next required gate is separate authorization for one fresh exact
listing preflight.

## Current Override — Fourth Attempt Runner Prepared Offline

Completed:

`PREPARE_NY_OSC_FOURTH_ATTEMPT_RUNNER_AND_CONTRACTS_OFFLINE`

State:

`READY_OFFLINE / NOT AUTHORIZED FOR PREFLIGHT OR EXECUTION`

The fourth runner, approval contracts, ungranted templates and fail-closed tests are prepared.
No limits were widened. The next gate is human review of this offline package; preflight,
download and source access remain unauthorized.

## Current Override — Fourth Attempt Proposal Prepared Offline

Completed:

`PREPARE_NY_OSC_FOURTH_BOUNDED_ATTEMPT_PROPOSAL_OFFLINE`

State:

`PROPOSED_NOT_AUTHORIZED / ONE DOWNLOAD / ZERO RETRY`

No limits are widened. The proposal requires a fresh exact listing preflight, a separately
prepared and verified fourth runner, and two new exact single-use approvals. No source access,
preflight or download occurred.

## Current Override — Streaming Multiline Parser Implemented Offline

Completed:

`IMPLEMENT_NY_OSC_STREAMING_MULTILINE_QUOTED_RECORD_PARSER_OFFLINE`

State:

`IMPLEMENTED_SYNTHETIC_ONLY / NO SOURCE ACCESS / NO FOURTH ATTEMPT`

The parser assembles logical records across physical lines using bounded structural state,
without decoding or buffering owner fields. All existing caps and fail-closed conditions are
preserved.

A fourth attempt remains a separate Product Owner decision and would require an offline
proposal, independently verified tooling, two new approvals and a fresh preflight.

## Current Override — Multiline Parser Remediation Is Feasible Offline

Completed:

`ANALYZE_NY_OSC_MALFORMED_QUOTED_RECORD_OFFLINE`

State:

`FEASIBLE / NOT IMPLEMENTED / SYNTHETIC ONLY / NO FOURTH ATTEMPT`

The selected design is a byte-level streaming state machine that recognizes record boundaries
only outside quotes and retains no owner-field bytes. Existing archive, uncompressed-size,
member-count and 14-field bounds remain unchanged.

Next bounded task:

`IMPLEMENT_NY_OSC_STREAMING_MULTILINE_QUOTED_RECORD_PARSER_OFFLINE`

## Current Override — Third Attempt Consumed Fail-Closed

Completed once:

`EXECUTE_NY_OSC_THIRD_BOUNDED_ATTEMPT_ONCE_AFTER_FRESH_PREFLIGHT`

Result:

`BLOCKED / MALFORMED_QUOTED_RECORD`

Both approvals are consumed and non-reusable. The raw ZIP was logically deleted; no owner
values were returned or persisted. No fourth attempt is authorized. The next bounded task is
synthetic offline analysis of parser-dialect handling, without source access or new execution
preparation.

## Current Override — Third Attempt Authorized, Awaiting Verified Integration

Approved:

`AUTHORIZE_NY_OSC_THIRD_BOUNDED_ATTEMPT_ONCE`

State:

`GRANTED_NOT_CONSUMED / ONE DOWNLOAD / ZERO RETRY`

The exact local-file and transient-PII grants are bound to runner checkpoint
`2d871ee041abe9cccc0e0fa32b849bbe223bdfa2` and CI `35385157576 — SUCCESS`. All byte/member caps remain
unchanged and a fresh exact listing preflight is required before download. Repository
preparation performed zero source access.

## Current Override — Third Attempt Proposal Prepared Offline

Completed:

`PREPARE_NY_OSC_THIRD_BOUNDED_ATTEMPT_PROPOSAL_OFFLINE`

Proposal:

`sources/proposals/ny_osc_owner_name_file_third_bounded_attempt_authorization.v1.json`

State:

`PROPOSED_NOT_AUTHORIZED / ZERO SOURCE ACCESS`

The proposed envelope remains one download, zero retries, unchanged byte/member caps,
quote-aware offline parser checkpoint verified, consumed approvals non-reusable, and fresh
listing preflight mandatory. No execution runner or granted approval artifact was created.

## Current Override — NY Second Attempt Consumed

The second bounded NY OSC attempt completed fail-closed with
`UNEXPECTED_DATA_FIELD_COUNT`. Both second-attempt approvals are consumed and cannot be
reused. The raw ZIP was logically deleted and no owner values were returned or persisted.

Current offline candidate repairs quote-aware pipe parsing and blocked-result structural
observability using synthetic fixtures only. No third real execution is authorized.

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

### First schema-discovery harness — offline ready

Completed:

`IMPLEMENT_NY_OSC_FIRST_SCHEMA_DISCOVERY_HARNESS_OFFLINE`

Checkpoint:

`9885377addec66d2802f58f6fa7184c2cd8ffdb1`

CI:

`35353395811` — SUCCESS.

Prepared before Gate 2:

- byte-bounded ZIP validation;
- uncompressed-size and member-count guards;
- 14-field documented KAPS layout validation;
- non-PII property-type-column mapping;
- no owner-value persistence/logging;
- aggregate-only schema metadata output.

This removes implementation work from the post-Gate2 critical path. Real execution remains blocked until current archive size and explicit Gate 2 approval exist.

### Transient local-file execution bridge

Completed:

`IMPLEMENT_NY_OSC_TRANSIENT_LOCAL_FILE_RUNNER_OFFLINE`

Checkpoint:

`688469e87fc39da20b7906b3825c81367a594b16`

CI:

`35359065170` — SUCCESS.

The Product Owner approved a single-use transient-local-file retention exception. The tested runner now resolves the browser-save transport mismatch while preserving:

- dedicated OS-temp location only;
- no durable raw persistence;
- no repository/cloud/chat copy;
- immediate logical deletion in `finally`;
- Gate 2 artifact required before execution;
- no physical secure-erasure claim.

No real file was used.

### NY second bounded attempt — approved / ready

Checkpoint:

`d157046c9cdf375fe88918ddaf41f97422de70a4`

CI:

`35364955860 — SUCCESS`

Both v2 approvals are granted/not consumed. Fresh preflight remains mandatory before the single authorized download.

### NY third-attempt runner — offline candidate

Prepared under an explicit zero-source-access boundary:

- attempt-specific fail-closed PowerShell runner;
- transient-local and transient-PII schemas;
- `NOT_GRANTED` approval templates;
- shared runtime binding to an exact attempt number;
- tests preventing pre-gate temp-directory creation, network clients, approval reuse,
  automatic retry, or bound widening.

State:

`READY_OFFLINE / CI_35384965991_SUCCESS / NOT AUTHORIZED FOR EXECUTION`

Checkpoint: `5aa606f9f79dc05508628d8a97f514cce7e4f770`.

## MVP-1 Remaining Product Path

`OSC access instructions DONE / current listing size OBSERVED / Gate 2 v1 CONSUMED_FAIL_CLOSED / transient-local runner VERIFIED / ONE REAL EXECUTION NEXT / schema-discovery harness READY`

in parallel with:

`follow-up cost contract DONE -> case-economics integration DONE -> reviewer exposure DONE -> deployment-candidate readiness DONE -> remote deploy VERIFIED -> commercial measurement capture when real source is authorized`

then, once a lawful real source is available:

`real schema mapping -> insurance classification -> candidate -> evidence/provenance -> economics -> reviewer -> human continue/stop`

## Next Product Work

Execute exclusively:

`REVIEW_AND_INTEGRATE_NY_OSC_THIRD_ATTEMPT_RUNNER_OFFLINE`

Classification: `A — Product Critical / Offline Safety Implementation`.

No source/network request, remote preflight, approval grant, or download is authorized.
