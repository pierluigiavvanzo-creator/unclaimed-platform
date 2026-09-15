# M3 California SCO — PROPERTY_TYPE Diagnostic / Remediation Evidence Proposal Review

Date: 2026-09-15

Status: **HUMAN REVIEW COMPLETED — PASS — NO DIAGNOSTIC EXECUTION AUTHORIZED**

## Review gate

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

## Reviewed checkpoint

Proposal branch:

`m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal`

Proposal branch HEAD reviewed:

`847cdf5daaa1834c3ce11fc3d6f29e2bbc36b4b4`

Proposal package checkpoint:

`020044d3013449fabe566c5164b8f99f9d8cc9ab`

Proposal package CI:

`35015429439` — SUCCESS

Final proposal-branch CI reviewed:

`35015731733` — SUCCESS

Reviewed artifacts:

- `sources/proposals/ca_sco_segment_500_plus.property_type_diagnostic_remediation_evidence.v1.json`
- `schemas/common/property_type_diagnostic_remediation_evidence_proposal.schema.json`
- `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL.md`
- `tests/contract/test_ca_sco_property_type_diagnostic_remediation_evidence_proposal.py`
- `PROJECT_STATE.md`
- `ROADMAP.md`
- `docs/handovers/HANDOVER_CURRENT.md`

## Review scope

This review is repository-only.

It performs no California SCO or `claimit.ca.gov` request, no authority retrieval, no source-body access, no transient source-row inspection, no diagnostic execution, no workflow creation, no runtime modification and no remediation.

The previously unretained offending `PROPERTY_TYPE` value is not reconstructed, inferred, hashed, measured or otherwise recovered by this review.

## Decision

**PASS**

The proposal is acceptable as a bounded design for a later, separately authorized diagnostic execution artifact.

This PASS accepts only the design boundary. It does **not** authorize source access or execution.

## Why the proposal passes

### 1. Verified base is pinned

The proposal pins the completed authority provenance review and the second bounded semantic execution. The established evidence remains:

- second real run `34995672539`;
- schema `1.1.0`;
- result `STOPPED_FAIL_CLOSED`;
- stop `PROPERTY_TYPE_FORMAT_UNEXPECTED`;
- v1.1 already separates UTF-8 encoding failure from decoded format mismatch;
- the observed mismatch therefore reached a decoded, non-empty projected value that failed the unchanged regex;
- the exact offending content was intentionally not retained.

The archived authority does not contradict the current shape regex and does not authorize trimming, casing, normalization, parser change or regex relaxation.

### 2. Future source boundary is narrower than the prior semantic execution

The proposed future diagnostic, if later separately authorized, is bounded to:

- exact already-known endpoint and pinned source identity;
- first canonical member only;
- maximum 4 transient data rows;
- stop at the first reproduced format mismatch;
- maximum 1 HEAD;
- maximum 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- redirects forbidden;
- additional ranges forbidden;
- full-body fallback forbidden;
- automatic widening forbidden;
- source identity drift -> fail closed;
- mismatch not reproduced inside the bound -> fail closed.

### 3. Diagnostic evidence is deliberately non-value-bearing

The proposal allows only a fixed categorical classification and bounded execution metadata.

It forbids persistence/logging of:

- exact `PROPERTY_TYPE`;
- bytes;
- hash;
- exact length;
- fragments;
- codepoints;
- transformed values;
- full rows;
- raw response body;
- `PROPERTY_ID`;
- owner/holder values;
- source-derived free text;
- per-row values or distinct source code lists.

### 4. Diagnostic transforms do not become runtime transforms

The proposed in-memory whitespace/case predicates are diagnostic-only. The proposal explicitly forbids using their transformed result as an accepted source value and forbids applying remediation during the diagnostic.

The current regex remains unchanged:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

### 5. No diagnostic class automatically authorizes remediation

Every proposed class maps only to a possible later proposal or further diagnostic decision. All `authorized_by_this_proposal` flags remain `false`.

### 6. Existing approvals cannot be reused

The following approvals remain consumed and non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

The proposal creates no replacement token.

### 7. Runtime and downstream governance remain closed

The reviewed diff contains governance/test artifacts only. No runner, workflow, source policy, registry or application runtime file is changed by the proposal package.

Source policy remains `PROPOSED`; registry remains disabled/unapproved; production classification remains inactive; identity resolution, genealogy, beneficiary matching, outreach and claim submission remain blocked.

## Mandatory execution-stage tightening

A later diagnostic execution/authorization artifact must be at least as restrictive as this proposal and must make the classifier fully deterministic before any network request.

It must explicitly define and contract-test all of the following:

1. **Classification precedence** — evaluate in this fixed order:
   - `SURROUNDING_ASCII_WHITESPACE_ONLY`
   - `ASCII_CASE_ONLY`
   - `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
   - `NON_ASCII_OR_CONTROL_CONTENT`
   - `ASCII_STRUCTURAL_MISMATCH`

2. **ASCII uppercase semantics** — define the diagnostic case probe as an ASCII-only mapping of `a-z` to `A-Z`, with all other code points unchanged; do not use locale-sensitive or Unicode normalization behavior.

3. **Control-character semantics** — enumerate the exact ASCII control code points treated as disallowed by the `NON_ASCII_OR_CONTROL_CONTENT` predicate. The execution artifact must not leave the term `disallowed control` implementation-defined.

4. **Fail-closed output semantics** — when the result is `STOPPED_FAIL_CLOSED`, the execution contract must define whether `diagnostic_class` is absent or null and must persist a bounded enumerated reason code rather than source-derived free text.

5. **Classifier regression tests** — add synthetic tests for each class, precedence collisions, boundary cases, fail-closed outcomes, and non-persistence/non-logging of source values.

6. **No widening while tightening** — these clarifications may make semantics more explicit but may not increase members, rows, requests, byte budgets, persistence fields, privacy scope or network endpoints.

Failure to lock these details before execution must stop the line at human review rather than default to an implementation choice.

## What PASS does not authorize

This PASS does not authorize:

- SCO or `claimit.ca.gov` network access;
- creation or execution of a diagnostic network workflow;
- transient real-row privacy exposure;
- a third semantic/diagnostic real execution;
- reconstruction of the previously unretained value;
- persistence of exact/hash/length/fragments/codepoints of a future value;
- parser changes;
- regex changes or relaxation;
- trimming, uppercasing or normalization as runtime behavior;
- source approval;
- registry activation;
- production classification;
- identity resolution;
- genealogy;
- beneficiary matching;
- outreach;
- claim submission.

## Authorization state after review

- proposal review decision: `PASS`
- diagnostic execution authorized: `false`
- transient-row privacy exposure authorized: `false`
- network workflow authorized: `false`
- runtime change authorized: `false`
- remediation authorized: `false`
- third real execution authorized: `false`
- approval token created by this review: `false`

## Next action

Prepare a **separate diagnostic execution/authorization artifact offline**.

That artifact must:

- pin this review and the reviewed proposal checkpoint;
- preserve or tighten every request/row/byte/privacy boundary;
- implement the mandatory deterministic-classifier tightening above in contract form;
- define fresh execution and transient-row privacy approval placeholders;
- remain `NOT_AUTHORIZED` until the owner explicitly grants those fresh approvals;
- create no source request while the artifact is being prepared.

Do not perform the diagnostic execution while preparing the authorization artifact.
