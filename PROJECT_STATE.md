# PROJECT_STATE.md

Last updated: 2026-09-17

## Current Product Objective

`MVP-1 — First Economically Actionable Case`

Priority strategy source: `PRODUCT_STRATEGY_MVP1.md`

Guiding metric:

`ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME`

## Current Working Checkpoint

Branch:

`mvp1-ny-osc-request-link-authorization`

Latest product-critical lifecycle:

`CA_PATH_FROZEN_FOR_MVP1 -> ALTERNATIVE_SOURCE_BENCHMARK_COMPLETE -> NY_OSC_SELECTED -> NY_SOURCE_CONTRACT_PRIVACY_GATE_OFFLINE_READY -> NY_REQUEST_LINK_AUTHORIZATION_GRANTED -> REQUESTER_CONTACT_INPUTS_REQUIRED_BEFORE_SUBMISSION`

Classification: `A — Product Critical`.

Authorization evidence:

`sources/evidence/ny_osc_owner_name_file_request_link_authorization.v1.json`

Authorization base checkpoint:

`198821ff41abb103b6c56876a075abb6c28c9c8f`

Authorization base CI:

`35258809399` — SUCCESS.

## California State

Latest California live run:

`35255228459` — attempt `1` — SUCCESS.

Observed:

- source bytes: `524288`;
- rows examined: `1024` (`256/member`);
- `DEFER_UNCLASSIFIABLE`: `1024`;
- recognized insurance rows: `0`;
- `IN03`: `0`;
- stop reason: none.

California source approval remains `HELD / NOT YET APPROVED`. The current California SCO `PROPERTY_TYPE` discovery path is frozen for MVP-1 pending genuinely new evidence.

## New York OSC Owner Name File

Source id:

`ny.osc.unclaimed_funds.owner_name_file`

Registry state:

- registered: yes;
- enabled: false;
- approved for use: false;
- acquired: false;
- provenance required: true.

The source contract preserves only OSC-disclosed semantics:

- owner name;
- last-known address;
- nature of property;
- when reported;
- reporting organization.

Owner name and last-known address are treated as PII. Dollar amount is not disclosed by the source and is represented as:

`UNKNOWN_FROM_SOURCE`

Physical file facts remain deliberately unknown until the first separately authorized file:

- physical column names;
- delimiter;
- encoding;
- archive layout;
- representation of `nature_of_property`;
- presence of a property identifier.

No production parser or classification activation is allowed before fail-closed schema discovery.

## New York Insurance Boundary

Current authority-index evidence records the New York insurance vocabulary as:

`IN01, IN02, IN03, IN04, IN05, IN06, IN07, IN12, IN77`

Primary MVP-1 target:

`IN03 — Proceeds Due Beneficiaries`

The official property-type PDF could not be directly opened by the research tooling because OSC returned HTTP 403; the policy records this provenance limitation and does not claim visual PDF verification.

## Privacy / Authorization Boundary

First real file schema discovery is designed as:

`MEMORY_ONLY`

During that first discovery:

- raw owner file persistence: forbidden;
- owner-row persistence: forbidden;
- owner name/address logging: forbidden;
- row-specific human inspection: forbidden;
- derived non-PII schema metadata may persist.

### Gate 1 — request-link authorization

Gate:

`HUMAN_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_AUTHORIZATION`

Owner authorization received:

`APPROVO NY OSC OWNER NAME FILE REQUEST-LINK ONLY`

Approval ref:

`OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71`

State:

`GRANTED_SINGLE_USE_NOT_CONSUMED_PENDING_REQUESTER_CONTACT_DATA`

The official form currently requires:

- name;
- company;
- phone;
- email.

Those values have not been supplied in this authorization record and must not be invented. No OSC request has been submitted yet.

Gate 1 still does **not** authorize:

- Owner Name File download;
- real owner PII processing;
- raw persistence;
- schema parsing;
- identity resolution;
- beneficiary matching;
- outreach;
- representation;
- fee agreement;
- claim activity.

### Gate 2 — later first download

`HUMAN_NY_OSC_OWNER_NAME_FILE_FIRST_DOWNLOAD_TRANSIENT_PII_AUTHORIZATION`

Not granted. It requires an explicit `max_download_bytes` after access instructions / download constraints are observed. No default byte cap is invented.

## Contract / Test State

Existing NY offline package remains verified by CI `35258809399`:

- Ruff: PASS;
- mypy: PASS;
- contract tests: PASS;
- smoke tests: PASS;
- full pytest: PASS;
- Streamlit safety/startup: PASS;
- frontend lint/typecheck/build: PASS.

No new production code is required merely to record Gate 1 authorization.

## Current Product / Source State

- approved real sources: `0`;
- California source: `HELD`;
- California `PROPERTY_TYPE` discovery: `FROZEN FOR MVP-1`;
- New York OSC Owner Name File: `REGISTERED CANDIDATE / DISABLED / NOT APPROVED / NOT ACQUIRED`;
- NY Gate 1 authorization: `GRANTED / NOT CONSUMED`;
- NY request submitted: no;
- NY access instructions obtained: no;
- NY real owner PII processed: no;
- NY Gate 2 authorization: not granted;
- production insurance classification: inactive;
- real MVP-1 candidates: `0`.

## SINGLE NEXT ACTION

Execute exclusively:

`COLLECT_NY_OSC_REQUESTER_CONTACT_INPUTS_FOR_AUTHORIZED_REQUEST`

Classification: `A — Product Critical / Human Input Dependency`.

Required user-supplied values:

`name, company, phone, email`

After those values are supplied, perform exactly one authorized official request submission using approval ref `OWNER_APPROVAL_2026-09-17_NY_OSC_OWNER_NAME_FILE_REQUEST_LINK_ONLY_5F8B2C71` if an execution-capable browser/form surface is available. Mark the approval consumed only after actual submission.

Do not download the Owner Name File or process owner PII under Gate 1.
