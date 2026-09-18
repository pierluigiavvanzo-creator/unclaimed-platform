# Changelog

All notable development changes are tracked here.

## Unreleased

### Added
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
