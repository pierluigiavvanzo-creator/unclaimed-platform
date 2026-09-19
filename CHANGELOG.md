# Changelog

All notable development changes are tracked here.

## Unreleased

### Added
- Structural-only NY OSC diagnostic telemetry for raw/structural/suppressed pipe and quote-state counts.
- Versioned transient-local execution result v1.1.0 carrying sanitized structural diagnostics end-to-end.
- Separate v1 JSON Schema for non-PII NY Owner Name structural diagnostics.
- Persisted non-PII fourth-attempt fail-closed execution evidence and consumed both fourth approvals.
- Synthetic regressions distinguishing true delimiter shortage from quote-suppressed delimiters.
- Registered both exact fourth-attempt NY OSC approvals offline as single-use, non-reusable and zero-retry.
- Bound the fourth-attempt grants to integrated runner `1c4be944...` and successful CI `35428062292`.
- Offline fourth-attempt NY OSC runner with pre-directory fail-closed authorization checks.
- Fourth-attempt approval contracts, ungranted templates, static tests and preparation audit.
- Versioned NY OSC fourth-attempt offline proposal with unchanged one-download/zero-retry bounds.
- Contract and audit gates preventing prior approval reuse, source access or implicit fourth execution.
- Byte-level streaming NY OSC parser for multiline quoted records without owner-field buffering.
- Synthetic LF/CRLF, quoted-pipe, doubled-quote and fail-closed multiline regression coverage.
- Offline NY OSC multiline quoted-record root-cause analysis and bounded remediation design.
- Machine-readable streaming-parser proposal, schema and contract tests with no fourth-attempt authorization.
- Persisted non-PII evidence for the consumed third NY OSC bounded attempt.
- Marked both third-attempt approvals consumed and non-reusable after fail-closed execution.
- Recorded the bounded offline diagnosis for `MALFORMED_QUOTED_RECORD` without claiming source corruption.
- Registered both exact NY OSC third-attempt approvals as granted and not consumed.
- Bound the single-use zero-retry grants to the integrated runner checkpoint and successful CI.
- Added policy, contract tests and audit evidence for the human-controlled third execution.
- Fail-closed NY OSC third-attempt runner bound to attempt-specific approvals.
- Third-attempt approval schemas and `NOT_GRANTED` templates with unchanged bounds.
- Runtime checks for matching attempt numbers, distinct approval refs and zero-retry policy.
- Versioned NY OSC third-attempt offline proposal with explicit `PROPOSED_NOT_AUTHORIZED` state.
- Contract tests preventing source access, approval reuse, automatic retry, or silent bound widening.
- Persisted non-PII evidence for the consumed second NY OSC bounded attempt.
- Byte-level quote-aware pipe record parsing with synthetic privacy regression coverage.
- Pre-download PowerShell checks that reject consumed second-attempt approvals.
- Blocked-result structural diagnostics using existing non-PII contract fields.
- M2 deterministic workflow state whitelist and A00 orchestrator skeleton.
- Fail-closed policy engine and budget ledger skeletons.
- Append-only SHA-256 audit hash-chain writer.
- Governance tests for allowed/forbidden transitions, missing policy, budget exhaustion and audit chaining.
- M2 REUSE-FIRST audit and ADR-0003.
- M1 machine contracts for Case, Evidence, Hypothesis, AgentMessage, Decision, AuditEvent, Source,
  SourceRegistry, and AgentRegistry.
- Positive and negative JSON fixtures plus contract tests.
- Canonical A00-A23 agent registry.
- ADR-0002 contract-versioning decision.

## 0.1.0 - 2026-09-13

### Added
- M0 repository and development harness.
