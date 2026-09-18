# Changelog

All notable development changes are tracked here.

## Unreleased

### Added
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
