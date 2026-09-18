# PROJECT_STATE.md

Last updated: 2026-09-18

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ny-first-download-retry-proposal`

Latest verified product implementation checkpoint:

`688469e87fc39da20b7906b3825c81367a594b16`

Product implementation CI:

`35359065170` — SUCCESS.

Classification: `A — Product Critical`.

Current lifecycle has two bounded tracks:

`NY_REQUEST_SUBMITTED_GATE1_CONSUMED -> AWAITING_NY_OSC_ACCESS_INSTRUCTIONS`

and, while that external dependency is pending:

`SYNTHETIC_DOWNSTREAM_SLICE_VERIFIED -> STREAMLIT_REMOTE_DEPLOYMENT_VERIFIED -> FIRST_SCHEMA_DISCOVERY_HARNESS_VERIFIED_OFFLINE`

## California State

Latest bounded California live run:

`35255228459` — attempt `1` — SUCCESS.

Observed:

- source bytes: `524288`;
- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`.

California remains `HELD / NOT YET APPROVED`, not rejected. The current California SCO `PROPERTY_TYPE` path is frozen for MVP-1 absent genuinely new evidence.

## New York OSC Owner Name File

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

Registry/source state:

- registered: yes;
- enabled: false;
- approved for use: false;
- acquired: false;
- physical schema: `UNKNOWN_UNTIL_FIRST_AUTHORIZED_FILE`;
- production parser/classification: inactive.

Primary MVP-1 authority target:

`IN03 — Proceeds Due Beneficiaries`

## NY Authorization / Privacy State

### Gate 1 — request access only

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

State:

`CONSUMED_SINGLE_USE_NON_REUSABLE`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

The Product Owner confirmed manual submission of the official request once on 2026-09-17. Repository tooling did not independently verify the external submit. Requester contact values are intentionally not persisted.

Access instructions received: no as of the latest Gmail check on 2026-09-18.

### Gate 2 — first bounded download / transient PII

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

State:

`NOT GRANTED / NOT READY`

Before Gate 2:

1. receive OSC access instructions;
2. observe non-content access/download constraints;
3. define explicit `max_download_bytes`;
4. separately review/authorize one bounded first download and memory-only schema discovery.

No Owner Name File download, real owner PII processing, raw persistence, identity resolution, beneficiary matching, outreach, representation, fee agreement or claim activity is currently authorized.

## Offline MVP-1 Downstream Slice

Integrated onto the current NY branch from the already verified reusable branch rather than rewritten.

Path:

`SYNTHETIC_POST_SCHEMA_MAPPING -> exact NY insurance classification -> IN03 candidate -> economics -> reviewer`

Integration checkpoint:

`75156c5419616b67eff658c8c3c8d6775849546c`

CI:

`35317313977` — SUCCESS.

Verified behavior:

- exact `IN03` -> primary MVP-1 insurance classification;
- other exact recorded NY insurance codes -> insurance/non-primary;
- unknown codes are not promoted by normalization or inference;
- only exact `IN03` creates the narrow synthetic candidate;
- deterministic case id;
- no identity resolution or beneficiary matching;
- no real source or PII access;
- reviewer API and Streamlit surface exercised.

Audit:

`docs/audits/MVP1_SYNTHETIC_VERTICAL_SLICE_OFFLINE.md`

## NY MVP-1 Economics Evidence

Official-source benchmark:

`docs/audits/NY_MVP1_RECOVERABLE_VALUE_EVIDENCE_BENCHMARK_OFFLINE.md`

Current fail-closed product facts:

- Owner Name File does not provide the exact recoverable dollar amount;
- exact recoverable value remains `UNKNOWN_PRE_CLAIM_REVIEW`;
- the 15% figure is represented only as the statutory cap for the scoped APL §1416 location-service rule, subject to legal applicability/exceptions;
- actual fee rate remains unsupported until explicit evidence exists;
- expected follow-up cost remains `NOT_MEASURED`;
- commercial actionability remains `NOT_COMPUTABLE_PRE_CONTACT`;
- no commercial threshold or case value is invented.

Implemented contracts:

- `schemas/economics/ny_mvp1_precontact_evidence.schema.json`;
- `schemas/economics/ny_mvp1_explicit_case_economics_input.schema.json`;
- `schemas/economics/ny_mvp1_explicit_case_economics_result.schema.json`;
- `src/unclaimed_platform/domain/ny_mvp1_value_evidence.py`.

Explicit later arithmetic accepts evidence-backed integer cents and basis points only. It makes no automatic continue/stop recommendation.

Reviewer integration:

- `GET /api/reviewer/mvp1/economics/precontact`;
- fail-closed Streamlit adapter;
- Streamlit `NY PRE-CONTACT ECONOMICS` card.

Latest cumulative CI:

`35318092067` — SUCCESS.

Passed:

- Ruff;
- mypy;
- contract tests;
- smoke tests;
- full pytest;
- Streamlit safety smoke;
- Streamlit startup smoke;
- frontend lint;
- frontend typecheck;
- frontend build.

One prior CI `35317731747` failed only because a unit test and contract test shared the same Python module basename. The contract test was renamed; no product logic changed. Repair CI `35317814189` was SUCCESS.

## NY MVP-1 Follow-Up Cost Measurement

Completed offline:

`IMPLEMENT_NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE`

Verified checkpoint:

`e9c1bc0e310f1b7b65f4153c90d5efb5d812caa0`

CI:

`35321285527` — SUCCESS.

Implemented measured dimensions:

- automated processing cost per candidate in integer cents;
- source/data cost per candidate in integer cents;
- human review time per candidate in integer seconds;
- additional manual research time per candidate in integer seconds.

Every measured component requires an evidence reference and observation timestamp. No default monetary or time assumption is supplied.

Human time is not converted into money unless an explicit documented labor rate is provided. Without that rate, fully loaded follow-up cost remains `NOT_COMPUTABLE_NO_LABOR_RATE`.

Implemented:

- `src/unclaimed_platform/domain/ny_mvp1_follow_up_cost.py`;
- `schemas/economics/ny_mvp1_follow_up_cost_measurement_input.schema.json`;
- `schemas/economics/ny_mvp1_follow_up_cost_measurement_result.schema.json`;
- unit and contract tests;
- `docs/audits/NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_CONTRACT_OFFLINE.md`.

The contract requires `owner_pii_included = false` and returns `no_commercial_recommendation = true`.

Three early CI runs stopped on test-file lint/syntax only. After two corrective patches, the mandatory root-cause audit identified a connector escape-sequence serialization defect in the test edit. The audited repair is recorded in:

`docs/audits/NY_MVP1_FOLLOW_UP_COST_MEASUREMENT_RUFF_ROOT_CAUSE.md`

No domain logic or schema semantics changed in that repair.

## NY MVP-1 Follow-Up Cost → Case Economics Integration

Completed offline:

`INTEGRATE_NY_MVP1_FOLLOW_UP_COST_WITH_CASE_ECONOMICS_OFFLINE`

Verified checkpoint:

`65748470ca69b71afd859d411a7f5673bb7bd823`

CI:

`35336436604` — SUCCESS.

Implemented an additive fail-closed bridge between the verified follow-up-cost measurement result and the existing explicit case-economics contract.

Rules now enforced:

- only `fully_loaded_follow_up_cost_state = COMPUTED_FROM_MEASURED_COMPONENTS` may populate `measured_follow_up_cost_cents`;
- missing documented labor rate produces `BLOCKED_FOLLOW_UP_COST_UNAVAILABLE`;
- direct machine/data cost alone is never substituted as fully loaded follow-up cost;
- all follow-up cost evidence refs are preserved;
- value evidence ref and fee evidence ref are preserved;
- the existing case-economics arithmetic remains authoritative;
- no automatic commercial recommendation is introduced.

Implemented:

- `src/unclaimed_platform/domain/ny_mvp1_case_economics_integration.py`;
- `schemas/economics/ny_mvp1_case_economics_integration_input.schema.json`;
- `schemas/economics/ny_mvp1_case_economics_integration_result.schema.json`;
- unit + contract tests;
- `docs/audits/NY_MVP1_FOLLOW_UP_COST_CASE_ECONOMICS_INTEGRATION_OFFLINE.md`.

The first CI run exposed one contract-only gap: the JSON Schema did not yet encode the cross-field invariant that a blocked integration must keep the cost and nested economics objects null. The schema was tightened with conditional `if/then` rules; Python semantics were unchanged. Final CI passed.

## NY MVP-1 Integrated Economics Reviewer Exposure

Completed offline:

`EXPOSE_NY_MVP1_INTEGRATED_CASE_ECONOMICS_IN_REVIEWER_OFFLINE`

Verified checkpoint:

`8274660554733d39e7dc7c522676bc709fb90214`

CI:

`35339962098` — SUCCESS.

Added reviewer API:

`GET /api/reviewer/mvp1/economics/integrated`

The deterministic synthetic reviewer contract exposes two states side by side:

- `READY_WITH_DOCUMENTED_LABOR_RATE -> READY_FOR_EXPLICIT_ECONOMICS`;
- `BLOCKED_WITHOUT_DOCUMENTED_LABOR_RATE -> BLOCKED_FOLLOW_UP_COST_UNAVAILABLE`.

The ready scenario shows a synthetic fully loaded follow-up cost and the existing explicit economics arithmetic. The blocked scenario keeps the fully loaded cost unavailable and makes clear that direct machine/data cost is `NOT FULLY LOADED`.

Both scenarios preserve evidence refs and state:

`no_commercial_recommendation = true`

Streamlit now renders two corresponding MVP-1 integrated-economics cards. Safety flags remain explicit:

- real source accessed: false;
- Owner Name File downloaded: false;
- real owner PII processed: false;
- automatic commercial recommendation: false.

Added contract:

`schemas/ui/ny_mvp1_integrated_economics_reviewer.schema.json`

and API/Streamlit smoke plus contract coverage.

The first CI run `35339876798` stopped on mypy because synthetic fixture components were supplied as dictionaries. They were replaced with the already existing typed `MeasuredCostComponent` and `MeasuredDurationComponent` models. No economics values or behavior changed. Final CI passed.

Audit:

`docs/audits/NY_MVP1_INTEGRATED_CASE_ECONOMICS_REVIEWER_OFFLINE.md`

## NY MVP-1 Reviewer Deployment Candidate

Completed offline:

`PREPARE_NY_MVP1_REVIEWER_DEPLOYMENT_CANDIDATE_OFFLINE`

Verified checkpoint:

`2a4c4bc6e3103bc7d5800facd0fbe4d8a01c2e16`

CI:

`35344178149` — SUCCESS.

Candidate state:

`READY_OFFLINE_NOT_REMOTELY_DEPLOYED`

Prepared deployment coordinates:

- repository: `pierluigiavvanzo-creator/unclaimed-platform`;
- branch: `mvp1-ny-reviewer-deployment-candidate-offline`;
- entrypoint: `apps/reviewer-streamlit/streamlit_app.py`;
- Python: `3.11`;
- requirements: `apps/reviewer-streamlit/requirements.txt`;
- secrets: none required for the synthetic-only candidate.

Deployment dependencies are pinned to the versions exercised by CI:

- `streamlit==1.63.0`;
- `fastapi==0.141.1`;
- `pydantic==2.13.5`.

Product-facing Streamlit wording now uses `MVP-1 Reviewer Console` instead of the legacy M3-only page title. The page has an above-content `Synthetic/test-only deployment candidate` warning and synthetic monetary labels remain explicit.

The existing CI startup contract was verified against the exact candidate entrypoint and requirements:

- requirements installation: PASS;
- safety smoke: PASS;
- Streamlit startup: PASS;
- `/_stcore/health`: PASS;
- Ruff/mypy/contract/smoke/full pytest: PASS;
- frontend lint/typecheck/build: PASS.

The first candidate CI `35344088288` failed only on two Ruff E501 copy lines. Copy was shortened without changing safety or behavior; final CI passed.

Deployment checklist:

`apps/reviewer-streamlit/DEPLOYMENT_CANDIDATE.md`

Audit:

`docs/audits/NY_MVP1_REVIEWER_DEPLOYMENT_CANDIDATE_OFFLINE.md`

Rollback baseline:

`6b14edfa39aab0c9bfe7be840820859075c7a708`

No remote deployment has been performed or claimed.

## NY MVP-1 Streamlit Remote Deployment Verification

Completed:

`VERIFY_NY_MVP1_STREAMLIT_REMOTE_DEPLOYMENT`

Remote URL:

`https://unclaimed-platform-mvp1-reviewer.streamlit.app/`

Verification basis:

- Product Owner supplied remote screenshots from the deployed Streamlit app;
- GitHub deployment-trigger CI `35345560301` was SUCCESS;
- the deployed page loaded without a visible runtime error.

Observed remote criteria:

- page title: `MVP-1 Reviewer Console`;
- visible banner: `Synthetic/test-only deployment candidate`;
- `MVP-1 SYNTHETIC CASE` card rendered;
- `NY PRE-CONTACT ECONOMICS` card rendered;
- READY integrated economics card rendered;
- FAIL-CLOSED integrated economics card rendered;
- READY state showed `READY FOR EXPLICIT ECONOMICS`;
- blocked state showed `BLOCKED FOLLOW UP COST UNAVAILABLE`;
- blocked machine/data cost remained explicitly `NOT FULLY LOADED`;
- automatic recommendation remained `NONE — HUMAN DECISION REQUIRED`;
- Source Registry showed `0` approved real sources;
- real acquisition remained `BLOCKED`;
- beneficiary matching remained `BLOCKED`;
- governance showed `PASS SYNTHETIC ONLY`;
- PII mode showed `NO REAL PII`.

Deployment state:

`VERIFIED_REMOTE_SYNTHETIC_ONLY`

Non-blocking presentation debt observed:

- the lower synthetic raw-artifact card still uses the legacy fixture label `synthetic:m3-operations-console-demo` / `synthetic://m3/operations-console`;
- the historical M3 milestone card remains visible as provenance/history.

These do not affect the verified MVP-1 reviewer logic or safety boundary, but may be cleaned up later as presentation work.

## NY OSC First Schema Discovery Harness — Offline

Completed:

`IMPLEMENT_NY_OSC_FIRST_SCHEMA_DISCOVERY_HARNESS_OFFLINE`

Verified checkpoint:

`9885377addec66d2802f58f6fa7184c2cd8ffdb1`

CI:

`35353395811` — SUCCESS.

Official instructions now provide a documented 14-field KAPS layout and pipe delimiter. The secure-transfer screenshot also shows a pre-download `Size` column, but its historical example size is not treated as the current archive size.

Implemented bounded memory-only discovery:

- download-byte cap enforced before ZIP parsing;
- explicit uncompressed-byte cap;
- explicit archive-member cap;
- exactly one text member required;
- documented 14-field row width validation;
- exact documented header persisted only if actually observed;
- otherwise first row is treated as data and never persisted as a header;
- only the non-owner `Property Type Code` position is shape-checked;
- aggregate record counts only;
- no owner name/address decoding, logging or return;
- raw archive bytes exist only as a transient function argument and are absent from serialized contracts.

Files:

- `src/unclaimed_platform/adapters/sources/ny_owner_name_schema_discovery.py`;
- authorization/result JSON Schemas;
- unit + contract tests;
- `docs/audits/NY_OSC_OWNER_NAME_FILE_FIRST_SCHEMA_DISCOVERY_HARNESS_OFFLINE.md`.

The harness uses synthetic ZIP fixtures only. It does not connect to OSC or consume Gate 2.

## NY OSC Current Listing / Gate 2 Proposal

Current remote listing evidence supplied by Product Owner:

- `FINDERS.zip`;
- `390.51 MB`;
- last modified `9/16/2026, 1:33:31 PM`.

No file was downloaded.

Prepared bounded Gate 2 proposal:

- `max_download_bytes = 450,000,000`;
- `max_uncompressed_bytes = 2,000,000,000`;
- `max_archive_members = 1`;
- one download maximum;
- zero retries;
- exact preflight identity match required;
- any listing drift -> stop before download.

Evidence:

`sources/evidence/ny_osc_owner_name_file_current_listing_metadata.v1.json`

Proposal:

`sources/proposals/ny_osc_owner_name_file_first_download_transient_pii_authorization.v1.json`

Important execution blocker:

OSC's documented browser flow saves the ZIP to the computer, while current Gate 2 policy forbids raw-file persistence and requires memory-only discovery. The proposal is therefore ready for human review but execution is not yet allowed until a compliant memory-only transfer path is verified or a separate transient-local-file policy expansion is explicitly authorized.

## NY OSC Transient Local File Runner — Offline

Completed:

`IMPLEMENT_NY_OSC_TRANSIENT_LOCAL_FILE_RUNNER_OFFLINE`

Product Owner authorization:

`APPROVO NY OSC FIRST DOWNLOAD TRANSIENT LOCAL FILE BOUNDED ONCE`

Recorded state:

`GRANTED_NOT_CONSUMED / SINGLE USE / NON-REUSABLE`

Verified checkpoint:

`688469e87fc39da20b7906b3825c81367a594b16`

CI:

`35359065170` — SUCCESS.

The transport mismatch is now resolved offline without using real data.

The runner:

- requires both the transient-local-file approval and a separate Gate 2 approval artifact;
- accepts only `FINDERS.zip`;
- requires a dedicated OS-temp directory prefixed `unclaimed-ny-osc-gate2-`;
- enforces the Gate 2 compressed-byte cap before schema discovery;
- reads the bounded ZIP into memory;
- delegates to the verified schema-discovery harness;
- returns only non-PII aggregate/schema metadata;
- logically deletes the local raw ZIP in a `finally` block;
- fails closed if deletion fails;
- never returns the local path;
- never guarantees physical secure erasure.

Durable raw persistence, repository storage, cloud-sync storage, chat upload and owner-field logging remain forbidden.

No real Owner Name File was downloaded and Gate 2 remains ungranted.

## NY OSC First Real Bounded Execution — Consumed / Fail-Closed

The first authorized real execution was consumed exactly once.

Result:

`BLOCKED_FAIL_CLOSED / PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`

Persisted non-PII execution metadata:

- compressed archive bytes: `409,477,526`;
- archive members: `1`;
- selected text member uncompressed bytes: `1,939,569,781`;
- local raw ZIP logically deleted: yes;
- no owner values returned or persisted.

Approval state:

- Gate 2 v1: `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- transient-local-file approval v1: `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- retry under v1: not authorized.

Offline remediation is now verified on synthetic fixtures:

- UTF-8 BOM-aware documented-header recognition;
- quoted documented-header recognition;
- trimming harmless outer whitespace;
- stripping one matching pair of quotes around Property Type Code;
- internal ambiguity such as `IN 03` still fails closed.

Remediation checkpoint:

`151f3a2f16c74f604fa72cc1284b2f9cd2e73f52`

CI:

`35363685148` — SUCCESS.

## NY OSC Second Bounded Attempt Proposal

Prepared after verified offline remediation.

Proposal:

`sources/proposals/ny_osc_owner_name_file_second_bounded_attempt_authorization.v1.json`

Retry script:

`scripts/ny_osc_gate2_retry_transient_local.ps1`

Safety bounds remain unchanged from the consumed first attempt. No second download is authorized yet.

Fresh preflight is mandatory immediately before any execution.

## Current Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- NY source: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1: `CONSUMED / NON-REUSABLE`;
- NY access instructions: `RECEIVED / REVIEWED NON-CONTENT ONLY`;
- NY Gate 2 v1: `CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO RETRY`;
- NY transient-local-file approval v1: `CONSUMED_SINGLE_USE_NON_REUSABLE`;
- NY transient-local runner: `READY / VERIFIED OFFLINE`;
- NY bounded first schema-discovery harness: `READY / VERIFIED OFFLINE`;
- real owner PII processed transiently once under consumed Gate 2; no owner values persisted or returned;
- synthetic IN03 classification-to-reviewer path: `READY / VERIFIED`;
- NY pre-contact economics evidence contract: `READY / VERIFIED`;
- follow-up cost measurement contract: `READY / VERIFIED`;
- follow-up cost → case economics integration: `READY / VERIFIED`;
- integrated economics reviewer/API/Streamlit: `READY / VERIFIED`;
- Streamlit deployment candidate: `DEPLOYED / VERIFIED_REMOTE_SYNTHETIC_ONLY`;
- remote Streamlit URL: `https://unclaimed-platform-mvp1-reviewer.streamlit.app/`;
- remote deployment evidence: `PRODUCT_OWNER_SCREENSHOTS + CI_35345560301_SUCCESS`;
- real measured candidate costs: `0`;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`HUMAN_NY_OSC_SECOND_BOUNDED_ATTEMPT_AUTHORIZATION_REVIEW`

Classification: `A — Product Critical / Human Authorization Gate`.

Review the verified offline remediation and the fresh second-attempt proposal.

Do not execute a second download until both new single-use approvals are explicitly granted and the secure-transfer listing is freshly verified.
