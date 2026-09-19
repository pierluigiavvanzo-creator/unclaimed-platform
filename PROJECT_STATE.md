# PROJECT_STATE.md

Last updated: 2026-09-19

## Superseding Current Event — Fourth Attempt Approvals Granted Offline

The Product Owner supplied both exact approval phrases on 2026-09-19.

State:

`GRANTED_NOT_CONSUMED / SINGLE USE / NON-REUSABLE / ZERO RETRY`

The grants are bound to integrated runner checkpoint
`1c4be944004c85936d53506a5998b9aeffc9aed0` and CI
`35428062292 — SUCCESS`. Limits remain one download, zero retries, 450,000,000
compressed bytes, 2,000,000,000 uncompressed bytes, one archive member, 14 fields and a
65,536-byte streaming-parser chunk.

This repository action performed no source access, fresh listing preflight, download, archive
opening or owner-PII processing. Fresh listing preflight requires a later, separate explicit
authorization.

## Superseding Current Event — Fourth Attempt Runner Prepared Offline

Authorized and completed:

`PREPARE_NY_OSC_FOURTH_ATTEMPT_RUNNER_AND_CONTRACTS_OFFLINE`

State:

`READY_OFFLINE / APPROVALS_NOT_GRANTED / ZERO SOURCE ACCESS / ZERO RETRY`

Prepared:

- `scripts/ny_osc_gate4_transient_local.ps1`;
- fourth-attempt transient-local and transient-PII approval schemas;
- two approval templates with status `NOT_GRANTED`;
- contract and static fail-closed tests;
- offline technical-preparation audit.

The runner binds attempt 4 to the reviewed proposal, two distinct future approval references, one
shared verified runner checkpoint and CI run, unchanged byte/member/field limits, and the
65,536-byte streaming parser. All approval checks occur before the temporary directory is
created. The runner contains no network client.

No NY OSC access, remote preflight, download, archive opening or real owner-PII processing
occurred. Operational approval remains a separate human gate.

## Superseding Current Event — Fourth Attempt Proposed Offline

Prepared:

`sources/proposals/ny_osc_owner_name_file_fourth_bounded_attempt_authorization.v1.json`

State:

`PROPOSED_NOT_AUTHORIZED / REPOSITORY_ONLY / ZERO SOURCE ACCESS`

The proposal references integrated streaming-parser checkpoint
`3e58eeb27b47ca89d01f6b45159c8a01bef94bf0` and CI
`35425632178 — SUCCESS`. It preserves one download, zero retries and all existing byte,
member, field and privacy bounds.

Both third-attempt approvals remain consumed and non-reusable. The fourth runner and approval
artifacts do not exist, the two proposed approval phrases remain `NOT_GRANTED`, and no source
access or preflight occurred.

## Superseding Current Event — Streaming Multiline Parser Implemented Offline

Completed:

`IMPLEMENT_NY_OSC_STREAMING_MULTILINE_QUOTED_RECORD_PARSER_OFFLINE`

The byte-level discovery parser now recognizes `LF` and `CRLF` as record boundaries only
outside double quotes. Newlines inside quoted fields are consumed without retaining owner
field bytes. EOF inside an open quote and all existing structural violations remain
fail-closed.

The state machine retains constant-size structural state rather than complete logical records.
Existing archive, uncompressed-size, member-count, 14-field and privacy bounds remain
unchanged. Synthetic coverage includes multiline LF/CRLF, quoted pipes, doubled quotes,
following records and negative fail-closed cases.

No NY OSC access, real-file processing, runner change, approval creation or fourth-attempt
preparation occurred.

## Superseding Current Event — Multiline Quoted-Record Analysis Complete

Completed:

`ANALYZE_NY_OSC_MALFORMED_QUOTED_RECORD_OFFLINE`

Decision:

`ANALYZED_OFFLINE_REMEDIATION_FEASIBLE_NOT_IMPLEMENTED`

The current parser treats every physical line as a complete record. It therefore blocks a
logical record that contains an embedded newline inside a quoted field. This mechanism is
confirmed from code; whether the deleted real record actually used that dialect remains
unconfirmed.

A byte-level streaming state machine can support logical multiline records with constant
auxiliary memory while retaining only structural state and never decoding or buffering owner
fields. Python's text-based `csv` reader was not selected because it would decode and
materialize owner fields.

No parser, runner, approval or execution contract changed. No source access occurred and no
fourth attempt is prepared or authorized.

## Superseding Current Event — Third Attempt Consumed Fail-Closed

The third bounded NY OSC attempt executed once and stopped:

`BLOCKED / MALFORMED_QUOTED_RECORD`

Persisted non-PII evidence:

- compressed archive bytes: `409,477,526`;
- one archive member;
- selected text member uncompressed bytes: `1,939,569,781`;
- `165,438` complete records and ASCII property-type tokens before the block;
- delimiter observed: pipe;
- header: not observed;
- local raw ZIP logically deleted;
- no raw path or owner values returned or persisted.

Both third-attempt approvals are now
`CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO RETRY`. No fourth download is authorized.

The result does not prove source corruption. The retained evidence is also consistent with a
parser-dialect mismatch such as an embedded line break inside a quoted field. Exact causality
cannot be confirmed because the raw file and offending row were intentionally not retained.

Next work is restricted to synthetic offline diagnosis and remediation design.

## Superseding Current Event — Third Attempt Authorized, Not Yet Consumed

The Product Owner supplied both exact third-attempt approval phrases on 2026-09-18.

State:

`GRANTED_NOT_CONSUMED / SINGLE USE / NON-REUSABLE / ZERO RETRY`

The grants are bound to integrated runner checkpoint
`2d871ee041abe9cccc0e0fa32b849bbe223bdfa2` and CI `35385157576 — SUCCESS`. Bounds remain one download,
zero retries, 450,000,000 compressed bytes, 2,000,000,000 uncompressed bytes and one
archive member. Fresh exact listing preflight remains mandatory.

This repository change performed no source access, remote preflight, download, archive
opening or owner-PII processing. Execution may occur only after this authorization package
passes CI and is integrated.

## Superseding Current Event — Third Attempt Runner Prepared Offline

The Product Owner authorized technical preparation only and explicitly did not authorize
download, remote preflight, or source access.

Candidate artifacts:

- `scripts/ny_osc_gate3_transient_local.ps1`;
- third-attempt transient-local and transient-PII approval schemas;
- two approval templates with status `NOT_GRANTED`;
- attempt-number binding in the shared transient-local execution bridge;
- fail-closed ordering and authorization-binding tests.

State:

`READY_OFFLINE / VERIFIED_CI / APPROVALS_NOT_GRANTED / ZERO_SOURCE_ACCESS`


Candidate verification checkpoint:

`5aa606f9f79dc05508628d8a97f514cce7e4f770`

CI:

`35384965991 — SUCCESS`


The runner cannot advance past its prechecks while the templates remain `NOT_GRANTED`.
No network request, listing check, download, owner-file opening, or owner-PII processing
occurred.

## Superseding Current Event — Third Attempt Offline Proposal

The quote-aware offline repair is integrated at:

`85d5f0c1101e5d66add27b9e1f445e7bba54a3b0`

Verification CI:

`35381899112 — SUCCESS`

A bounded third-attempt proposal now exists:

`sources/proposals/ny_osc_owner_name_file_third_bounded_attempt_authorization.v1.json`

State:

`PROPOSED_NOT_AUTHORIZED / REPOSITORY_ONLY / ZERO_SOURCE_ACCESS`

The proposal preserves one-download/zero-retry limits, does not widen byte or archive bounds,
does not reuse the consumed second-attempt approvals or runner, and requires two new explicit
single-use human approvals plus a fresh listing preflight before any future execution.

No third-attempt runner or approval artifacts exist. No source access, download, owner-file
opening, or owner-PII processing occurred.

## Superseding Current Event — Second NY Attempt Consumed Fail-Closed

Repository package inspected from checkpoint:

`61a533e035dfba45d0c1359b8eee0fdbba41d7d8`

The second bounded NY OSC attempt was executed once and is now consumed.

Result:

`BLOCKED / UNEXPECTED_DATA_FIELD_COUNT`

Persisted non-PII execution metadata:

- compressed archive bytes: `409,477,526`;
- archive members: `1`;
- selected text member uncompressed bytes: `1,939,569,781`;
- local raw ZIP logically deleted: yes;
- physical secure erasure guaranteed: no;
- no raw path returned;
- no owner values persisted or returned.

Both second-attempt approvals are:

`CONSUMED_SINGLE_USE_NON_REUSABLE / ZERO RETRY`

No third download is authorized.

Offline root-cause work found that the discovery parser used a raw byte `split` on every
pipe. That parser cannot distinguish a structural delimiter from a pipe inside a quoted
field. The observed failure is consistent with that limitation, but the deleted real row
prevents claiming it as proven real-file causality.

The offline repair candidate now:

- performs byte-level quote-aware pipe splitting without decoding owner fields;
- fails closed on an unclosed quoted record;
- preserves only already-authorized non-PII structural counters on blocked outcomes;
- checks approval consumption in PowerShell before creating the download directory or
  asking the Product Owner to download;
- records the second execution result and both approvals as consumed;
- includes synthetic regression and contract tests.

Source activation, production classification and a third real execution remain blocked.

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ny-second-attempt-approved-ready-execution`

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

Safety bounds remain unchanged from the consumed first attempt. Second-attempt approvals are now granted but not consumed. A fresh remote-listing preflight is still mandatory before the single authorized download.

Fresh preflight is mandatory immediately before any execution.

## NY OSC Second Attempt — Approved / Verified Ready

Both second-attempt approvals are granted and not consumed.

Verified execution branch:

`mvp1-ny-second-attempt-approved-ready-execution`

Verified checkpoint:

`d157046c9cdf375fe88918ddaf41f97422de70a4`

CI:

`35364955860 — SUCCESS`

The second attempt remains single-use and zero-retry. Fresh remote-listing preflight is mandatory immediately before download.

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

`REVIEW_AND_INTEGRATE_NY_OSC_THIRD_ATTEMPT_RUNNER_OFFLINE`

Classification: `A — Product Critical / Offline Safety Implementation`.

Run repository CI and review the runner/contracts. Do not grant either approval, perform a
remote preflight, access the source, or download the Owner Name File.
