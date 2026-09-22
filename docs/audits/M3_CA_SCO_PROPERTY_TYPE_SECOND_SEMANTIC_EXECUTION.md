# M3 — CA SCO PROPERTY_TYPE Second Bounded Semantic Execution

Date: 2026-09-15  
Status: **EXECUTED ONCE — STOPPED FAIL-CLOSED — EVIDENCE REVIEW REQUIRED**

## 1. Scope

This audit records the single owner-authorized second bounded real `PROPERTY_TYPE`
semantic execution using the canonical v1.1.0 runner.

It does not approve the California SCO source, activate the source registry,
enable production classification, authorize identity resolution, beneficiary
matching, genealogy, outreach, or claim submission.

## 2. Fresh approvals

The owner explicitly granted:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`

The authorization package was staged on
`m3-ca-sco-property-type-second-semantic-execution` and passed CI run
`34995492373`.

Both approvals were single-use and are **CONSUMED** by the real execution
recorded below. They cannot authorize any retry or later network execution.

## 3. Execution identity

Execution branch:
`m3-ca-sco-property-type-second-semantic-execution`

Authorization commit:
`acd627f841650541e7dd2441c2c83e20aaf108b5`

Temporary workflow execution commit:
`e27c0b72e39d63f0ae8fc6e9dd1fb92c234dcbcc`

GitHub Actions one-shot run:
`34995672539`

Execution schema:
`schemas/common/property_type_semantic_verification_execution.v1_1.schema.json`

Persisted schema version:
`1.1.0`

## 4. Result

Semantic result:
`STOPPED_FAIL_CLOSED`

Stop reason:
`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Exact observed counters:

- HEAD requests: `1`
- Range GET requests: `1`
- HTTP requests total: `2`
- source response-body bytes read: `131072`
- sample rows accepted/examined: `0`
- retry: none
- cap widening: none

The transport HEAD matched the runner's expected content length, media type,
range support and ETag before the single bounded Range GET was processed.

## 5. What v1.1.0 allows us to conclude

The canonical v1.1.0 runner separates:

- invalid UTF-8 during `PROPERTY_TYPE` projection ->
  `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- a successfully decoded, non-empty projected value that fails the unchanged
  token-shape regex -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Therefore this run narrows the observed failure class to a **decoded,
non-empty `PROPERTY_TYPE` shape mismatch** under the unchanged rule
`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`.

This does **not** reveal the offending value and does not establish why the
source value has that shape. It does not justify trimming, uppercasing,
normalization, regex relaxation, or a broader code domain.

`sample_rows_examined: 0` is the persisted accepted/examined counter. It must
not be interpreted as proof that no transient record bytes were parsed before
the fail-closed stop.

## 6. Privacy and persistence verification

The runner output was redirected to `/dev/null` during the live execution.
The workflow logs contain the command, approval references and validation
marker, but no source row values and no `PROPERTY_TYPE` values.

The persisted evidence contains only bounded derived execution metadata,
counters, transport metadata, result/status fields and safety flags.

It does not persist:

- raw response body;
- full rows;
- `PROPERTY_ID`;
- owner/holder values;
- per-row `PROPERTY_TYPE`;
- offending bytes;
- offending value hashes;
- offending value lengths.

All persisted safety flags remain false.

## 7. Artifact and workflow lifecycle

Workflow artifact:

- artifact ID: `10408035386`
- artifact name:
  `ca-sco-property-type-second-semantic-execution-2026-09-15`
- artifact ZIP digest:
  `sha256:c0189177dcca91696e85b3b9fd67c1c896c3af30b13c79b0aa3670998f621732`

Only the derived v1.1 execution JSON was uploaded.

The one-shot workflow was removed immediately after execution.

Workflow-removal commit:
`d6e83a44b2069a2fa746c09d1ae33622654e5d43`

Steady-state one-shot workflow:
**ABSENT**

No retry was performed or authorized.

## 8. Governance state

Unchanged and fail-closed:

- source policy remains `PROPOSED`;
- source-level real acquisition authorization remains false;
- registry remains disabled and unapproved;
- approved real sources remain `0`;
- semantic compatibility remains unresolved;
- production classification remains inactive;
- identity resolution remains blocked;
- beneficiary matching remains blocked;
- genealogy remains blocked;
- outreach remains blocked.

## 9. Persisted evidence

Repository evidence path:

`sources/evidence/ca_sco_segment_500_plus.property_type_semantic.execution.v1_1.second.json`

The historical first execution remains unchanged under schema v1.0.0 and is
not reinterpreted.

## 10. Next gate

`HUMAN_PROPERTY_TYPE_SECOND_SEMANTIC_EXECUTION_EVIDENCE_REVIEW`

The next task is evidence review/offline decision-making only. A third network
execution would require a new proposal and fresh explicit execution/privacy
approvals.
