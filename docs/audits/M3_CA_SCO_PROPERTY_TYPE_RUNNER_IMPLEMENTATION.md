# M3 California SCO — PROPERTY_TYPE Runner Implementation Audit

Date: 2026-09-15

## Scope

This audit records implementation of the bounded `PROPERTY_TYPE` semantic-verification runner under the explicit owner instruction:

`approvo implementazione bounded runner PROPERTY_TYPE con soli test synthetic/mock`

Approval reference:
`OWNER_CHAT_APPROVAL_2026-09-15_PROPERTY_TYPE_RUNNER_IMPLEMENTATION_SYNTHETIC_MOCK_ONLY`

This approval authorized runner implementation and synthetic/mock testing only. It did **not** authorize real network execution, real CSV row access, transient-row privacy exposure, source approval, registry activation, matching, or outreach.

## Branch / Baseline

Candidate branch:
`m3-ca-sco-property-type-runner-implementation`

Canonical base:
`6105c22a7d31df7afca00282eff7e9798e98b868`

Functional candidate HEAD before this audit/docs closure:
`d2b8977a0fd34474ecb545c6ecfefc354b551b30`

Compare against canonical at functional closure:
- ahead: `3`
- behind: `0`
- merge-base: exactly `6105c22a7d31df7afca00282eff7e9798e98b868`

## Implemented Files

Runner:
`scripts/ca_sco_property_type_semantic_verification.py`

Implementation-authorization schema:
`schemas/common/property_type_semantic_runner_implementation_authorization.schema.json`

Implementation-authorization evidence:
`sources/evidence/ca_sco_segment_500_plus.property_type_runner_implementation_approval.v1.json`

Runner unit tests:
`tests/unit/test_ca_sco_property_type_semantic_verification_runner.py`

Implementation authorization contract test:
`tests/contract/test_ca_sco_property_type_runner_implementation_authorization.py`

Historical proposal/design contract tests were adjusted only so that their historical `runner absent at proposal/design time` state is not incorrectly interpreted as a permanent prohibition on later implementation. Their non-authorizing and non-executed semantics remain intact, and the network workflow remains required to be absent.

## Runner Boundary

The runner preserves the canonical safety caps:
- 4 canonical CSV members;
- maximum 4 complete data rows/member;
- maximum 16 rows total;
- maximum 1 HEAD;
- maximum 4 Range GET;
- maximum 5 HTTP requests total;
- maximum 131,072 response-body bytes/Range;
- maximum 524,288 source response-body bytes total;
- maximum 262,144 uncompressed transient bytes/member;
- maximum 1,048,576 uncompressed transient bytes total;
- maximum 32,768 bytes/logical CSV record;
- no extra Range request;
- no full-body fallback;
- no automatic cap widening.

The transport endpoint, expected Content-Length, ETag, media type, `Accept-Ranges`, HTTPS host, and `If-Match` behavior remain fixed to the canonical design.

If a Range response is not HTTP 206, the runner stops before consuming the unexpected response body.

## Parsing / Projection Boundary

The runner:
1. requires non-empty execution and privacy approval references before transport access;
2. verifies HEAD metadata;
3. requests one fixed member-prefix Range per canonical member;
4. validates local ZIP member metadata;
5. incrementally DEFLATE-decompresses only inside fixed transient limits;
6. requires the exact canonical 25-column header;
7. reads at most four complete data records/member;
8. projects only zero-based column `1`, `PROPERTY_TYPE`, with a byte-level CSV field parser;
9. counts columns without persisting full rows;
10. rejects malformed/empty `PROPERTY_TYPE` and unknown `IN`-prefixed codes;
11. emits only the canonical derived execution summary.

`PROPERTY_ID` is not decoded for semantic use or persisted. Raw Range bodies, full rows, owner/holder values, and per-row `PROPERTY_TYPE` values are not part of the execution evidence schema.

## Synthetic / Mock Verification

Synthetic tests use in-memory mock transport and synthetic DEFLATE member prefixes. Covered cases include:
- compatible sample with official insurance codes;
- code-shape-compatible sample with no insurance codes -> inconclusive;
- unknown `IN` code -> fail closed;
- ignored Range / HTTP non-206 -> STOP with zero unexpected-body reads;
- header mismatch -> fail closed before accepting data rows;
- row column-count mismatch -> fail closed;
- missing privacy approval -> fail before transport;
- missing execution approval -> fail before transport;
- live CLI path is explicit opt-in;
- one-shot network workflow remains absent;
- execution payload validates against the canonical execution schema.

## CI History

Initial functional commit:
`2679964f8bd99893c2545faa1b153bc73f0adb00`

CI `34950942449`:
- `streamlit-candidate`: SUCCESS;
- `quality`: FAILED at Ruff only;
- exact issue: `Mapping` imported from `typing` instead of `collections.abc`.

Lint-fix commit:
`773dc427a8be4d97807c74fdf73c08692a35ac7c`

CI `34951326633`:
- Ruff: PASS;
- mypy: PASS;
- contract: FAILED because an older proposal test still asserted that the runner file must never exist;
- later quality steps skipped.

Historical-contract fix commit:
`d2b8977a0fd34474ecb545c6ecfefc354b551b30`

CI `34951460475`:
- Ruff: PASS;
- mypy: PASS;
- contract tests: PASS;
- smoke tests: PASS;
- full pytest: PASS, including the new synthetic/mock runner tests;
- frontend install/lint/typecheck/build: PASS;
- Streamlit safety/startup smoke: PASS;
- overall: SUCCESS for `quality` and `streamlit-candidate`.

The failed intermediate runs are retained as normal repository history; no force-push or history rewrite was used.

## Network / Data Access Evidence

During this implementation task:
- real SCO requests performed: `0`;
- real SCO response-body bytes read: `0`;
- real CSV rows read: `0`;
- real PII processed: `0`;
- network one-shot workflow created: `false`;
- source approval granted: `false`;
- registry activated: `false`.

The real HTTP transport class exists solely as the already-designed implementation path for a later separately authorized execution gate. It was not invoked by CI or by this task.

## Governance State

Unchanged:
- source policy: `PROPOSED`;
- real acquisition authorized: `false`;
- registry enabled: `false`;
- registry approved for use: `false`;
- approved real sources: `0`;
- semantic real execution: BLOCKED;
- transient-row privacy approval: ABSENT;
- real row access: BLOCKED;
- real PII processing: BLOCKED;
- identity resolution: BLOCKED;
- beneficiary matching: BLOCKED;
- outreach: BLOCKED.

## Result

`PROPERTY_TYPE` bounded runner implementation is **CANDIDATE + SYNTHETIC/MOCK CI VERIFIED**.

It is not yet canonical and it is not authorized for real execution.

## Next Gate

`HUMAN_PROPERTY_TYPE_RUNNER_CANDIDATE_PROMOTION`

A future promotion to `m2-state-governance-core` remains non-executing. Even after promotion, actual real SCO semantic sampling requires a separate explicit owner execution approval **and** a transient-row privacy approval.
