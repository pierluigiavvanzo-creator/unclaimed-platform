# M3 California SCO — PROPERTY_TYPE Diagnostic / Remediation Evidence Proposal

Date: 2026-09-15

Status: **PROPOSAL ONLY — NOT AUTHORIZED FOR EXECUTION**

## Purpose

This document defines the smallest fail-closed evidence design for the still-unresolved live `PROPERTY_TYPE` semantic mismatch.

The proposal does **not** access California SCO or `claimit.ca.gov`, does not reconstruct or infer the previously unretained source value, does not modify the runner, parser, regex, casing, trimming, normalization, logging or persistence behavior, and does not authorize a third real semantic execution.

The proposal exists only for the next human review gate:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

## Verified base state

Base branch:

`m3-ca-sco-property-type-authority-archive-provenance-review`

Base HEAD:

`961d6a908dd9656f5ce19823be074011010833bf`

Final base CI:

`35014204079` — SUCCESS

Authority provenance review decision:

`ARCHIVED_AUTHORITY_RESOLVES_TARGET_PROVENANCE_SOURCE_SEMANTIC_MISMATCH_REMAINS`

The authority review established that:

- `ZZZZ` is directly supported by the archived California SCO authority;
- `IN01` through `IN08` and `IN99` are directly supported by the authority;
- every authority-enumerated property type code other than `ZZZZ` has the observed two-uppercase-Latin-letter plus two-digit shape;
- this does not make every arbitrary `AA99` token semantically valid;
- the existing regex is not contradicted by the authority;
- trimming, uppercasing, normalization, parser change and regex relaxation remain unauthorized.

## Why this is not the earlier diagnostic remediation

The repository already contains the earlier offline diagnostic remediation documented in:

`docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION.md`

That remediation separated two previously conflated failure paths:

- invalid UTF-8 projection -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded non-empty shape mismatch -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

The second real execution used the remediated v1.1 runner and stopped with:

`PROPERTY_TYPE_FORMAT_UNEXPECTED`

Run:

`34995672539`

Therefore the current problem is narrower: the observed source field decoded successfully, was non-empty, and failed the unchanged rule:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The exact value, bytes, hash, length and fragments were intentionally not retained and must not be reconstructed or inferred.

## Diagnostic question

If a future, separately authorized bounded source execution reproduces the same decoded/non-empty format mismatch, can it derive **one coarse diagnostic class** without persisting the source value?

The proposed classes are:

1. `SURROUNDING_ASCII_WHITESPACE_ONLY`
2. `ASCII_CASE_ONLY`
3. `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
4. `NON_ASCII_OR_CONTROL_CONTENT`
5. `ASCII_STRUCTURAL_MISMATCH`

These are diagnostic categories only. They are not accepted source values and do not themselves authorize remediation.

## Proposed future execution boundary — not authorized by this proposal

Any later diagnostic execution must first pass a separate human authorization and fresh execution/privacy approvals.

If later approved, the proposal caps the diagnostic to:

- exact existing endpoint only;
- pinned source identity: content length, ETag, media type and byte-range support;
- first canonical ZIP member only;
- at most `4` transient data rows;
- stop immediately at the first reproduced `PROPERTY_TYPE_FORMAT_UNEXPECTED` condition;
- `1` HEAD maximum;
- `1` Range GET maximum;
- `2` HTTP requests maximum total;
- `131072` bytes maximum source response body total;
- `262144` bytes maximum uncompressed transient data;
- `32768` bytes maximum logical record;
- zero retries;
- zero redirects;
- no additional range;
- no full-body fallback;
- no automatic widening.

If the source identity drifts, or the mismatch is not reproduced inside this exact boundary, execution must stop fail-closed.

## Privacy-minimal diagnostic derivation

A later separately approved diagnostic may evaluate only fixed in-memory predicates against the first reproduced mismatching `PROPERTY_TYPE`:

- whether removing only surrounding ASCII space (`U+0020`) or tab (`U+0009`) would satisfy the unchanged regex;
- whether ASCII-only uppercasing without trimming would satisfy the unchanged regex;
- whether the combination would satisfy the unchanged regex when neither predicate alone does;
- whether otherwise the decoded value contains non-ASCII or disallowed control content.

No Unicode normalization probe is included.

No full-row `csv.reader` crosscheck is included. That would broaden transient exposure beyond the narrow PROPERTY_TYPE projector and therefore requires a separate privacy design if later needed.

The proposal does not permit diagnostic transforms to become runtime transforms or accepted values.

## Persistence and logging boundary

Even if a later diagnostic execution is separately authorized, it must not persist or log:

- exact `PROPERTY_TYPE`;
- PROPERTY_TYPE bytes;
- hash;
- exact length;
- fragments, prefixes or suffixes;
- codepoints;
- transformed values;
- full CSV rows;
- raw source response bodies;
- `PROPERTY_ID`;
- owner or holder values;
- source-derived free text;
- per-row values or distinct code lists.

Allowed persisted evidence is limited to the categorical result, source-identity verification state, bounded counters and safety flags defined by the machine-readable proposal.

## Remediation boundary

No diagnostic class automatically authorizes remediation.

A future classification may only inform another explicit human decision:

- whitespace-only -> consider a **separate trim-policy remediation proposal**;
- case-only -> consider a **separate case-policy remediation proposal**;
- whitespace + case -> consider a **separate combined policy proposal**;
- non-ASCII/control -> require a separate source-format or parser diagnostic proposal;
- ASCII structural mismatch -> require a separate source-format or authority diagnostic proposal.

The current regex is not relaxed by this proposal.

## Consumed approvals

The following approvals remain consumed and non-reusable:

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

This proposal defines no new approval token.

## Current implementation state

Proposal preparation only:

- source request performed: `false`
- diagnostic execution performed: `false`
- network workflow created: `false`
- runner modified: `false`
- parser modified: `false`
- regex modified: `false`
- normalization modified: `false`
- logging modified: `false`
- persistence modified: `false`

## Governance state

Unchanged:

- source policy: `PROPOSED`;
- registry: disabled and not approved;
- approved real sources: `0`;
- authority provenance: resolved within the recorded proof boundary;
- live semantic compatibility: unresolved;
- production classification: inactive;
- identity resolution: blocked;
- genealogy: blocked;
- beneficiary matching: blocked;
- outreach: blocked;
- claim submission: blocked.

## Acceptance criteria

The proposal package is acceptable only if repository CI proves that:

- the proposal validates against its versioned schema;
- the verified authority review and second real execution are correctly pinned;
- the future diagnostic boundary cannot be widened silently;
- the proposal cannot silently authorize execution, privacy exposure, runtime change or remediation;
- no raw or identifying source-value diagnostic output is allowed;
- consumed approvals cannot be reused;
- the existing runner regex remains unchanged;
- source policy and downstream safety gates remain closed;
- normal repository quality, contract, smoke, full pytest, frontend and Streamlit checks remain green.

## Next gate

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

A `PASS` at that gate would still not perform source access. Any real diagnostic requires a separate execution/authorization artifact and fresh explicit execution/privacy approvals. No canonical approval token is created here.
