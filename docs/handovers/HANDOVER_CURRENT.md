# HANDOVER — Unclaimed Insurance Platform

Date: 2026-09-15

## Purpose

Authoritative restart point. Verify remote heads before acting and use repository evidence rather than chat memory.

## Current Branch / Diagnostic Proposal Review Checkpoint

- repository: `pierluigiavvanzo-creator/unclaimed-platform`
- branch: `m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal-review`
- reviewed proposal branch: `m3-ca-sco-property-type-diagnostic-remediation-evidence-proposal`
- reviewed proposal HEAD: `847cdf5daaa1834c3ce11fc3d6f29e2bbc36b4b4`
- proposal package checkpoint SHA: `020044d3013449fabe566c5164b8f99f9d8cc9ab`
- proposal package CI: `35015429439` — SUCCESS
- final reviewed proposal CI: `35015731733` — SUCCESS
- review gate: `HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`
- review decision: `PASS`
- review audit: `docs/audits/M3_CA_SCO_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW.md`

## Verified Baseline

- M0: VERIFIED
- M1: VERIFIED
- M2: VERIFIED
- M3 authority target provenance: RESOLVED WITH BOUNDED AA99 INTERPRETATION
- M3 live PROPERTY_TYPE semantic compatibility: UNRESOLVED
- second bounded semantic run: `34995672539` -> `STOPPED_FAIL_CLOSED`
- second stop: `PROPERTY_TYPE_FORMAT_UNEXPECTED`
- current runner/schema: v1.1 separates encoding failure from decoded format mismatch
- previous semantic execution/privacy approvals: CONSUMED + NON-REUSABLE
- authority archival approval: CONSUMED + NON-REUSABLE
- source policy: `PROPOSED`
- registry: disabled / not approved
- approved real sources: `0`
- production classification: inactive
- identity/genealogy/beneficiary matching/outreach/claim submission: BLOCKED

## What Is Already Proven

The second real run used the v1.1 runner. Under that runner:

- invalid UTF-8 projection -> `PROPERTY_TYPE_ENCODING_UNEXPECTED`;
- decoded, non-empty shape mismatch -> `PROPERTY_TYPE_FORMAT_UNEXPECTED`.

Because run `34995672539` stopped with `PROPERTY_TYPE_FORMAT_UNEXPECTED`, the observed live mismatch is narrowed to a decoded, non-empty projected PROPERTY_TYPE that failed the unchanged regex:

`^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`

The exact offending value, bytes, hash, exact length, fragments and codepoints were intentionally not retained and must not be reconstructed or inferred from historical evidence.

The archived authority review separately established:

- `ZZZZ` is supported;
- `IN01` through `IN08` and `IN99` are supported;
- authority-enumerated non-`ZZZZ` property type codes use the observed two-uppercase-letter plus two-digit shape;
- arbitrary `AA99` membership is not established;
- the current regex is not contradicted by the authority;
- trimming, uppercasing, normalization, parser change and regex relaxation are not authorized.

## Proposal Review Result

Completed gate:

`HUMAN_PROPERTY_TYPE_DIAGNOSTIC_REMEDIATION_EVIDENCE_PROPOSAL_REVIEW`

Decision:

`PASS`

The PASS accepts only the bounded proposal design. It does **not** authorize network access, transient real-row exposure, diagnostic execution, runtime changes or remediation.

The accepted future diagnostic design remains limited to:

- exact existing endpoint and pinned source identity;
- first canonical member only;
- maximum 4 transient data rows;
- stop at the first reproduced format mismatch;
- maximum 1 HEAD;
- maximum 1 Range GET;
- maximum 2 HTTP requests total;
- maximum 131072 source response-body bytes total;
- maximum 262144 uncompressed transient bytes;
- maximum 32768 bytes per logical record;
- zero retries;
- redirects forbidden;
- additional range forbidden;
- full-body fallback forbidden;
- automatic widening forbidden;
- source identity drift -> fail closed;
- mismatch not reproduced inside boundary -> fail closed.

Persisted evidence may contain only a fixed coarse diagnostic class, source-identity state, bounded counters and safety flags. Exact values, bytes, hashes, lengths, fragments, codepoints, transformed values, full rows, raw bodies, PROPERTY_ID and owner/holder values remain forbidden from persistence/logging.

No diagnostic class automatically authorizes remediation.

## Mandatory Tightening Before Any Diagnostic Execution

The separate execution/authorization artifact must make classifier semantics deterministic before any network request.

It must contract-test:

1. fixed classification precedence:
   - `SURROUNDING_ASCII_WHITESPACE_ONLY`
   - `ASCII_CASE_ONLY`
   - `SURROUNDING_ASCII_WHITESPACE_AND_CASE`
   - `NON_ASCII_OR_CONTROL_CONTENT`
   - `ASCII_STRUCTURAL_MISMATCH`

2. ASCII-only case mapping: `a-z` -> `A-Z`, all other code points unchanged;
3. exact enumeration of ASCII control code points considered disallowed;
4. explicit fail-closed reason-code enum;
5. explicit null/absent semantics for `diagnostic_class` when stopped fail-closed;
6. synthetic tests for all classes, precedence collisions, boundary cases and non-persistence/non-logging.

These tightenings may not widen network, row, byte, persistence or privacy scope.

## Current Authorization Boundary

After review:

- proposal review decision: `PASS`
- diagnostic execution authorized: `false`
- transient-row privacy exposure authorized: `false`
- network workflow authorized: `false`
- runtime change authorized: `false`
- remediation authorized: `false`
- third real execution authorized: `false`
- approval token created by review: `false`

The review performed no source network access, no diagnostic execution, no authority retrieval and no runtime/parser/regex/normalization/logging/persistence change.

## Consumed Approvals — Do Not Reuse

- `APPROVE_SECOND_PROPERTY_TYPE_SEMANTIC_EXECUTION_BOUNDED`
- `APPROVE_SECOND_PROPERTY_TYPE_TRANSIENT_ROW_PRIVACY_BOUNDED`
- `APPROVE_PROPERTY_TYPE_AUTHORITY_ARCHIVAL_EXECUTION_ONE_SHOT`

All remain consumed and non-reusable.

## Current Safety Boundary

Do not:

- reuse any consumed approval;
- access SCO or `claimit.ca.gov` while preparing the next authorization artifact;
- reconstruct or infer the historical unretained offending PROPERTY_TYPE value;
- persist/hash/measure exact source value content;
- create or execute a diagnostic network workflow before fresh explicit approvals;
- change parser, regex, trimming, casing or normalization;
- apply remediation from any diagnostic class;
- perform a real-row full-parser crosscheck under the accepted proposal;
- run another real PROPERTY_TYPE semantic/diagnostic execution;
- activate source policy, registry or production classification;
- perform identity resolution, genealogy, beneficiary matching, outreach or claim submission.

## SINGLE NEXT ACTION

Prepare exclusively a **separate diagnostic execution/authorization artifact offline**.

That artifact must:

- pin this review PASS and the reviewed proposal checkpoint;
- preserve or tighten every accepted request/row/byte/privacy boundary;
- encode the mandatory deterministic-classifier tightening above;
- define fresh execution and transient-row privacy approval placeholders;
- remain NOT AUTHORIZED until the owner explicitly grants those fresh approvals;
- perform no source request during preparation.

Do **not** run the diagnostic while preparing the artifact. A later real diagnostic requires a separate human authorization decision after that artifact is reviewed.
