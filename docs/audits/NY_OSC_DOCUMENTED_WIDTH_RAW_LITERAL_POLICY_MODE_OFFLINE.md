# NY OSC Documented-Width RAW-Literal Policy Mode — Offline Implementation

Date: 2026-09-21

Classification: `A — Product Critical / Offline Parser Implementation`

Status:

`IMPLEMENTED_OFFLINE / SYNTHETIC_ONLY / ZERO SOURCE ACCESS / NOT RUNTIME-ACTIVATED`

## Requested action

`IMPLEMENT_NY_OSC_DOCUMENTED_WIDTH_RAW_LITERAL_POLICY_MODE_OFFLINE`

## Preconditions

Baseline branch:

`ny-osc-documented-width-quote-arbitration-proposal-remediation-offline`

Baseline HEAD:

`d16d36307202cc386c6c391f656b4239cf017165`

Baseline CI:

`35587779920 — SUCCESS`

Active architecture decision:

`D-011 — NY OSC quote interpretation statistical fallback policy`

The preceding remediation review returned:

`HUMAN_REVIEW_NY_OSC_DOCUMENTED_WIDTH_QUOTE_ARBITRATION_PROPOSAL_REMEDIATION_OFFLINE = PASS`

The Product Owner then explicitly requested this offline implementation.

## Implemented mode

New explicit schema-discovery mode:

`DOCUMENTED_WIDTH_RAW_LITERAL_POLICY`

The mode is additive. Existing modes remain available:

- `MULTILINE_LEGACY`;
- `LINE_LOCAL_ARBITRATION`.

The existing default remains:

`MULTILINE_LEGACY`.

No existing mode is redirected to the new behavior.

## Structural semantics

The new mode implements the current D-011 Product Owner fallback without claiming OSC
source semantics.

Rules:

- LF and CRLF are hard physical-record boundaries;
- quote state does not exist in this mode;
- every pipe byte `|` is a structural delimiter;
- double quote `"` is an ordinary field byte for record-structure purposes;
- exactly 14 fields are required;
- any other field count stops fail-closed through the existing
  `UNEXPECTED_DATA_FIELD_COUNT` path;
- existing Property Type Code shape validation remains unchanged;
- existing header recognition remains unchanged;
- existing privacy/persistence guarantees remain unchanged.

Quoted-header and Property Type Code wrapper handling remain existing field-level behavior.
D-011 changes record structure only; it does not silently broaden those existing matchers.

## Reuse-first

No external parser dependency was introduced.

The implementation reuses the repository's existing:

- `_LogicalRecordScanner`;
- bounded 64 KiB streaming pattern;
- ZIP/member/uncompressed-byte caps;
- header matcher;
- Property Type Code matcher;
- blocked-result contract;
- structural diagnostic contract.

A small dedicated `_RawLiteralPhysicalLineScanner` was added because the two historical
quote scanners encode semantics that D-011 explicitly must not reuse for RAW structure.

## Synthetic regression coverage

Added synthetic tests verify:

1. the retained sixth-attempt shape `RAW 14 / quote candidate open` is accepted as a
   14-field RAW record without carrying quote state;
2. a same-line quoted pipe that produces RAW 15 fields remains blocked, even though a
   quote-aware grammar could produce 14;
3. a true 13-field row remains fail-closed;
4. CRLF is a hard boundary even with an unmatched double quote;
5. CRLF split across the 64 KiB stream-chunk boundary is handled correctly;
6. existing normalized quoted-header recognition remains available while quote bytes are
   literal for record structure.

All fixtures are synthetic. No owner value from the real OSC file was accessed or used.

## Functional verification

Checkpoint:

`5a6bc104ff4f5b34bf57b4f0cbd41e069c150f59`

GitHub CI:

`35594503935 — SUCCESS`

Results:

- Ruff: PASS;
- mypy core: 19 source files PASS;
- mypy NY OSC runtime: 2 source files PASS;
- contract tests: 379 passed;
- smoke tests: 16 passed;
- full pytest: 548 passed;
- Streamlit safety/startup: PASS;
- frontend lint/typecheck/build: PASS.

## Preserved boundaries

No OSC access.
No remote preflight.
No download.
No real owner-PII processing.
No sixth retry.
No seventh-attempt proposal, runner, approval or execution.
No runtime bridge change.
No execution-result contract change.
No runner change.
No default-mode change.
No source activation.
No identity resolution, matching, outreach or claim activity.

## Rollback

Return to baseline:

`d16d36307202cc386c6c391f656b4239cf017165`

or remove the explicit `DOCUMENTED_WIDTH_RAW_LITERAL_POLICY` scanner/dispatch and its
synthetic tests. No persisted source/runtime state depends on the new mode.

## Next gate

`HUMAN_REVIEW_NY_OSC_DOCUMENTED_WIDTH_RAW_LITERAL_POLICY_MODE_OFFLINE`
