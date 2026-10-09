# NY MVP-1 REAL P1 TARGETABILITY RUNNER — OFFLINE IMPLEMENTATION REVIEW

Date: 2026-09-24

Classification: A — Product Critical

Result: PASS_OFFLINE_RUNNER_REAL_EXECUTION_NOT_AUTHORIZED

## Human scope approval

The Product Owner explicitly approved:

APPROVE_NY_MVP1_REAL_P1_TARGETABILITY_EXECUTION_SCOPE_V1

This approval authorized only:

IMPLEMENT_AND_REVIEW_REAL_P1_TARGETABILITY_RUNNER_OFFLINE

It did not authorize source access, remote preflight, download, real candidate materialization, owner PII processing, identity/contact enrichment, outreach, value research, representation or claim activity.

PR #37 remains open and unmerged. This runner branch is stacked on top of the approved scope branch.

## Verified runner checkpoint

Runner checkpoint:

6a73a4e3da189affe530f6ca9e32259c828e803d

GitHub Actions:

35997991872 — SUCCESS

Verified:

- Ruff;
- core/API/storage/UI mypy;
- NY OSC line-local runtime mypy gate;
- contract tests;
- smoke tests;
- full pytest suite;
- Streamlit safety smoke;
- Streamlit startup smoke;
- frontend lint;
- frontend typecheck;
- frontend build.

## Implementation

### Fresh approval binding

New module:

src/unclaimed_platform/domain/ny_mvp1_p1_authorization.py

It validates seven fresh single-use gate types and binds them to:

- the approved P1 scope reference;
- the approved scope blob SHA;
- a specific runner checkpoint;
- a successful runner CI run;
- a fresh preflight receipt;
- the approved download-start freshness window.

No historical NY OSC approval is accepted by this binding.

### Approval contracts

New schemas:

- schemas/common/ny_mvp1_p1_single_use_gate.schema.json
- schemas/common/ny_mvp1_p1_fresh_listing_preflight_receipt.schema.json

Seven gate templates were created under sources/proposals.

Every gate template is:

- status = NOT_GRANTED;
- owner_authorization = null;
- execution_approval_ref = null;
- runner_checkpoint = null;
- single_use = true;
- reusable = false;
- retry_authorized = false.

Therefore repository state alone cannot execute P1.

### Two-pass bounded local runner

New module:

src/unclaimed_platform/adapters/sources/ny_owner_name_p1_targetability_local.py

The module contains no network client.

#### Pass L0 — selection

The entire authorized TXT member is streamed.

Only these observations are buffered/derived for selection:

- Property ID non-whitespace presence boolean;
- Property Type Code;
- Property Owner Count;
- Holder Report Year;
- source record ordinal;
- structural pipe count.

Owner Name and address fields are neither decoded nor buffered for ranking.

Eligibility is exact:

- 13 pipes / documented 14-field physical width;
- Property Type Code exactly IN03;
- Property Owner Count exactly 1;
- Property ID has a non-whitespace value;
- Holder Report Year is a positive strict decimal.

Selection is:

PERSISTENCE_FIRST_OLDEST_HOLDER_REPORT_YEAR_THEN_SOURCE_ORDER

Tie-break:

lowest source ordinal.

There is no fixed age threshold and no value inference.

#### Pass L1 — selected ordinal only

The same already-authorized local archive is reopened.

Only the selected source ordinal is materially buffered.

L1 buffers only:

- Property ID;
- Property Type Code;
- Property Owner Count;
- Owner Name;
- Holder Name;
- Holder Report Year.

Address bytes are not buffered when L2-A is not pre-authorized.

The transient candidate is a private, non-serializable-by-design dataclass with a redacted repr.

The result never returns:

- Owner Name;
- Property ID;
- Holder Name;
- address;
- raw row.

### L2-A seam

A typed provider protocol exists only as a dependency-injection seam.

There is NO production provider implementation and NO CLI provider option.

L2-A can execute only when:

- all three L2-A grants were already granted before the download;
- the provider/budget gate binds a specific provider_id;
- the runtime provider object has the same provider_id;
- returned evidence is non-PII;
- external cash spend is exactly USD 0.00;
- manual research is <= 900 seconds.

The provider result can contain only targetability states, opaque evidence refs, generic source categories/domains and measured bounded cost/time.

It cannot return owner PII.

The existing T0-T4 classifier is reused.

### Local deletion

The local archive is logically deleted after any execution attempt that reaches the local runner.

The output records:

- LOGICAL_DELETION_COMPLETED; or
- LOGICAL_DELETION_FAILED.

The runner never claims secure physical erasure.

A deletion failure converts the run to BLOCKED / DISPOSAL_FAILED.

## CLI and PowerShell

New local-only entrypoint:

scripts/ny_mvp1_p1_targetability_execute.py

New Windows wrapper:

scripts/ny_mvp1_p1_targetability_local.ps1

The CLI intentionally supports L1 only.

It has no network source client and no L2-A provider argument.

This prevents a future user/operator from silently attaching an unreviewed search/data provider through the command line.

## Output contract

New schema:

schemas/common/ny_mvp1_real_p1_targetability_run_result.schema.json

The durable result can include:

- non-PII selection summary;
- non-PII Economic Case Ledger;
- T0-T4 targetability decision when an approved injected provider is present;
- cost/time evidence;
- stop reason;
- disposal result;
- authorization provenance.

It explicitly fixes:

- owner_pii_returned = false;
- owner_pii_persisted = false;
- raw_row_persisted = false;
- outreach = false;
- value research = false;
- claim activity = false;
- reusable = false;
- retry_authorized = false.

## Tests

New tests cover:

- persistence-first oldest-year selection;
- deterministic source-order tie-break;
- malformed structural row defer;
- zero eligible candidate stop;
- serialized output contains no synthetic owner/property/address/holder markers;
- L2-A T1 classification through a synthetic injected provider;
- 900-second cap;
- provider binding mismatch;
- provider missing fail-closed;
- archive boundary failure;
- seven NOT_GRANTED gate templates;
- gate contract rejects fake grant without runner binding;
- preflight privacy boundary;
- result contract rejects PII persistence expansion;
- result contract rejects reusable execution;
- fresh authorization builder;
- rejection of NOT_GRANTED gate;
- rejection of partial L2-A approval set;
- successful full L2-A binding with approved provider/budget fixture.

All test inputs are synthetic.

## Defects found and repaired during implementation

### Defect 1 — Ruff forward-annotation style

The initial runner used quoted return annotations that Ruff UP037 rejected.

Repair:

use postponed annotations without quotes.

Product logic changed:

NO.

### Defect 2 — test f-string

One authorization test used an unnecessary f-string and Ruff rejected it.

Repair:

remove the f prefix.

Product logic changed:

NO.

### Defect 3 — CLI/wrapper newline serialization

The first connector write stored literal \n sequences rather than actual newlines in the CLI/wrapper files.

Repair:

rewrite both files with real line breaks.

Product logic changed:

NO.

Final checkpoint after repairs:

6a73a4e3da189affe530f6ca9e32259c828e803d

Final CI:

35997991872 — SUCCESS

## Security/privacy assessment

PASS for offline implementation scope.

Important limitations remain:

1. No real execution grant exists.
2. No fresh preflight receipt exists.
3. No controller/legal-basis/transparency artifact has been approved.
4. No L2-A provider has been selected/reviewed.
5. No external PII query is authorized.
6. Gate templates remain NOT_GRANTED.
7. PR #37 scope is not yet merged.
8. The runner implementation branch is not merged.

## Review conclusion

PASS_OFFLINE_RUNNER_REAL_EXECUTION_NOT_AUTHORIZED

The code is technically ready for Product Owner review.

Recommended next action:

HUMAN_REVIEW_NY_MVP1_REAL_P1_TARGETABILITY_RUNNER_OFFLINE

Approval of the runner should authorize repository integration only.

It must NOT be interpreted as any of the seven execution/privacy grants.
