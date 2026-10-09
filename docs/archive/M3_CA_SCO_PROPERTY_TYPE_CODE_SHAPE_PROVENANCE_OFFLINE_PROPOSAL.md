# M3 — CA SCO PROPERTY_TYPE Code-Shape Provenance Offline Proposal

Date: 2026-09-15  
Status: **PROPOSAL ONLY — OFFLINE — NOT EXECUTED**

## 1. Purpose

Prepare a repository-only review plan for the retained provenance behind the
`PROPERTY_TYPE` semantic assumptions used by the canonical runner, especially
the unchanged code-shape rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The proposal is motivated by the second bounded real semantic execution, which
again stopped fail-closed with `PROPERTY_TYPE_FORMAT_UNEXPECTED` under schema
v1.1.0.

This proposal does not perform the provenance review itself. It stops at the
human gate:

`HUMAN_PROPERTY_TYPE_CODE_SHAPE_PROVENANCE_OFFLINE_PROPOSAL_REVIEW`

## 2. Branch and review base

Candidate branch:
`m3-ca-sco-property-type-code-shape-provenance-offline-proposal`

Created from second-execution closure HEAD:
`9d0243987c843172fe46c971ead0bf3947098336`.

The canonical runner remains anchored to:
`m2-state-governance-core` at
`e97c1f62959f603bdd3df79538d4b70255594c70`.

Stable `main` is not modified.

## 3. Verified trigger condition

Second real semantic execution:

- workflow run `34995672539`;
- execution schema `1.1.0`;
- result `STOPPED_FAIL_CLOSED`;
- stop reason `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- HEAD requests `1`;
- Range GET requests `1`;
- HTTP requests total `2`;
- source-response body bytes `131072`;
- accepted/examined rows `0`;
- no retry;
- no cap widening.

Under the canonical v1.1 runner ordering, that reason is narrower than the
historical v1.0 reason. It means the projected value decoded as UTF-8, the row
had the expected 25 columns, the value was non-empty, and the unchanged regex
check failed.

It does not reveal the source value and does not establish why its shape differs.

## 4. Consumed approvals remain consumed

The second execution used the explicit single-use approvals:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`;
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`.

Both were consumed by the authorized execution and are not reusable. This
proposal does not create replacement approvals and does not authorize a third
real execution.

## 5. Why provenance review precedes any third execution

The existing repository proves that the runner enforces the regex and that the
second source observation failed that rule. It does not, by itself, prove that
the regex represents the complete authoritative grammar of every possible SCO
`PROPERTY_TYPE` value.

The semantic proposal retains an external SCO NAUPA reference and records the
California insurance-code set `IN01-IN08` and `IN99`. However, the repository
does not currently retain the referenced authority document itself as an
immutable evidence artifact. An external URL recorded in repository metadata is
not equivalent to direct offline proof of all statements attributed to it.

The review must therefore separate retained evidence from retained assertions
that point to external authority, and must classify unsupported assumptions as
`PROVENANCE_INSUFFICIENT` rather than filling gaps from memory or general
knowledge.

## 6. Existing parser evidence is bounded

The committed offline diagnosis already compares the custom projector with
Python `csv.reader(..., strict=True)` on a deterministic synthetic standard-CSV
matrix covering ordinary records, quoted fields, embedded commas, escaped
quotes, embedded newline/CRLF cases and quote-all output.

No mismatch was reproduced in that matrix.

That result is useful but deliberately bounded. It does not prove universal CSV
dialect compatibility and must not be generalized beyond the committed test
matrix.

## 7. Proposed offline review questions

The future offline review will classify retained provenance for exactly these
assumptions:

1. `PROPERTY_TYPE_FIELD_IS_COLUMN_INDEX_1` — verify the second-field position
   against retained data-scope evidence and the runner.
2. `GENERAL_CODE_SHAPE_AA99` — identify retained repository evidence proving
   that every non-`ZZZZ` value must be two uppercase ASCII letters plus two
   digits, or classify provenance insufficient.
3. `SPECIAL_CODE_ZZZZ` — identify retained repository evidence for `ZZZZ` as a
   valid special token, or classify provenance insufficient.
4. `CALIFORNIA_INSURANCE_CODE_SET` — distinguish direct retained evidence from
   the repository assertion that cites the external SCO authority for
   `IN01-IN08` and `IN99`.
5. `CUSTOM_PROJECTOR_STANDARD_CSV_COMPATIBILITY` — preserve the exact boundary
   of the committed synthetic differential matrix and make no universal parser
   claim.

## 8. Allowed classification vocabulary

The future review may use only:

- `SUPPORTED_BY_REPOSITORY_EVIDENCE`;
- `REPOSITORY_ASSERTION_WITH_EXTERNAL_REFERENCE_NOT_ARCHIVED`;
- `PROVENANCE_INSUFFICIENT`.

Unknown or ambiguous provenance must fail closed to
`PROVENANCE_INSUFFICIENT`.

A repository URL pointing to external authority, without retained authority
content, must not be treated as direct offline proof.

## 9. Offline-only boundary

This proposal authorizes no source or authority access.

During this proposal task:

- no California SCO request is performed;
- no SCO source body is accessed;
- no authority PDF/document is downloaded;
- no new external authority lookup is performed;
- no source value is reconstructed or inferred;
- no network one-shot workflow is created.

Synthetic tests and comparisons among already-retained repository artifacts are
within scope only after the proposal receives its next human review.

## 10. Changes explicitly forbidden

This proposal does not authorize:

- regex modification or relaxation;
- trimming;
- uppercasing;
- normalization;
- parser changes;
- logging expansion;
- privacy-boundary expansion;
- a third real execution;
- source approval;
- registry activation;
- production classification;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- claim submission.

The existing runner and semantic regex remain untouched.

## 11. Governance state

Unchanged and fail-closed:

- source policy `PROPOSED`;
- registry disabled and unapproved;
- approved real sources `0`;
- semantic compatibility unresolved;
- production classification inactive;
- identity resolution blocked;
- genealogy blocked;
- beneficiary matching blocked;
- outreach blocked;
- claim submission blocked;
- one-shot source workflow absent.

## 12. Proposed machine artifacts

This candidate contains only:

- `schemas/common/property_type_code_shape_provenance_offline_proposal.schema.json`;
- `sources/proposals/ca_sco_segment_500_plus.property_type_code_shape_provenance_offline.v1.json`;
- `tests/contract/test_ca_sco_property_type_code_shape_provenance_offline_proposal.py`;
- this audit.

No runner, execution schema, source policy, registry or historical evidence file
is modified.

## 13. Acceptance criteria

Before the offline review may be authorized, human review must confirm:

- the proposal validates against its versioned schema;
- it is pinned to second-execution closure HEAD `9d024398...`;
- the canonical runner base remains `e97c1f62...`;
- consumed execution/privacy approvals are explicitly non-reusable;
- no SCO or authority network access is authorized;
- the unchanged regex is recorded but not silently elevated to proven authority;
- retained evidence, repository assertions and insufficient provenance are
  distinguishable;
- no parser, regex, privacy or logging change is authorized;
- the one-shot workflow remains absent;
- all downstream gates remain closed.

## 14. Next gate

`HUMAN_PROPERTY_TYPE_CODE_SHAPE_PROVENANCE_OFFLINE_PROPOSAL_REVIEW`

A positive review of this proposal would authorize only the repository-only
provenance classification task described above. It would not authorize external
research, SCO access, authority-document download, semantic-contract changes or
a third real execution.
