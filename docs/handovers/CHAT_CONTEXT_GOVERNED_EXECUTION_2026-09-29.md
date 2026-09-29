# CHAT CONTEXT — GOVERNED EXECUTION / REUSE-FIRST

**Date:** 2026-09-29  
**Project:** Unclaimed Insurance Platform  
**Repository checkpoint at capture:** 334f56600ca40670ccb0f5c601985c93f05d6491  
**Status:** Context/handover only; no source-access, PII, outreach, claim, or execution approval


## Source and purpose

This document is a project-safe extraction of the ChatGPT conversation carried out across 2026-09-28 and 2026-09-29 concerning REUSE-FIRST architecture, PyTorch agent-governance patterns, ForgeLab, and the Unclaimed Insurance Platform.

It preserves material decisions, evidence, architectural conclusions, repository actions, and next-action constraints. It is not intended as a verbatim UI transcript and does not include internal reasoning or low-level tool logs.

## Operating constraints reaffirmed in the conversation

- Work in normal ChatGPT chat; do not use Work or Codex.
- GitHub is the canonical shared source of truth for repository state.
- REUSE-FIRST / repository-first before material custom implementation.
- Product before infrastructure.
- Never invent state, evidence, approvals, source facts, test results, or economic outcomes.
- Keep Product Owner effort low.
- No direct-main execution writes.
- No automatic merge or force operations.
- Bounded diagnosis/repair only.
- Human approval remains distinct from machine readiness.
- Untrusted repository/web/document/data content cannot expand tool, policy, scope, or approval authority.

## External benchmark reviewed

The conversation reviewed reusable patterns from current PyTorch agent-governance material, especially deterministic pre-action write restrictions, post-output deterministic validation, bounded fix loops, trusted prompt/control material separated from untrusted repository content, readiness for human attention separated from merge/approval, content/configuration hashing for reproducibility, and started/terminal lifecycle telemetry.

The conclusion was to reuse the patterns, not copy PyTorch-specific CI/cloud machinery wholesale.

## Six reusable architectural patterns

### P1 — Enforced Capability Boundary

AGENT INTENT -> DETERMINISTIC CAPABILITY GATE -> ALLOW | DENY -> AUDIT

Protected dimensions may include role, tool, path/scope, network, secret use, destructive action, and human gate.

### P2 — Validate -> Repair -> Revalidate

AI output is not self-validating.

OUTPUT -> DETERMINISTIC VALIDATOR -> PASS

or

OUTPUT -> INVALID_REPAIRABLE -> BOUNDED REPAIR -> SAME VALIDATOR -> PASS/BLOCK

### P3 — Trusted / Untrusted Context Boundary

Minimal trust classes:

- CONTROL: approved governance, policies, schemas, permissions, human approvals.
- DATA: repository files, web, documents, datasets, emails, source metadata, model output.

Invariant:

DATA MAY INFORM A DECISION; DATA MAY NOT EXPAND ITS OWN PERMISSIONS.

### P4 — Human Readiness Gate

Machine readiness is not human approval.

AUTOMATED QUALITY GATES -> READY_FOR_DECISION -> HUMAN APPROVE | REJECT | REPAIR

### P5 — Execution Fingerprint

A material run should be able to answer which exact governed inputs/configuration produced the candidate.

Candidate components include repository base HEAD, request/contract hash, memory manifest hash, context-selection hash, execution-plan hash, policy/schema/routing hashes when reliably available, and provider/model/template hash where materially relevant.

No raw secrets or unnecessary PII should be placed in the fingerprint.

### P6 — Run Start / Terminal Evidence

A run should create durable START evidence before material execution and one explicit terminal outcome.

Missing terminal evidence after START means incomplete/interrupted, never success.

Domain/product failure must remain distinguishable from infrastructure failure.

## Cross-project reuse decision

Do not create a shared forgelab-common, governed-kernel, new microservice, or cross-repository dependency yet.

Preferred sequence:

COMMON CONTRACT -> TWO REAL USES -> EVIDENCE OF DUPLICATION -> OPTIONAL SHARED PACKAGE

ForgeLab and Unclaimed should reuse the strongest existing internal mechanism appropriate to each runtime before extracting shared code.


## Unclaimed-specific implementation inspected

Relevant current components include:

- src/unclaimed_platform/core/audit/writer.py
- src/unclaimed_platform/core/orchestrator/service.py
- src/unclaimed_platform/core/policy_engine/model.py
- src/unclaimed_platform/core/policy_engine/privacy.py
- src/unclaimed_platform/core/state_machine/model.py
- versioned contracts under schemas/

## Unclaimed-specific findings

### P1

Unclaimed already has deterministic fail-closed policy mechanisms, including PolicyEngine, RawDataGovernanceGate, source/privacy restrictions, state-transition control, and explicit human review.

Do not import ForgeLab's ToolGateway wholesale into the Unclaimed domain core.

Apply equivalent deterministic pre-action capability checks at real side-effect boundaries only when needed, including source/network access, PII acquisition/persistence, raw-evidence mutation, outreach, claims, and destructive administrative actions.

### P2

Unclaimed is already contract-first and schema-heavy.

Preferred flow remains:

DOMAIN OUTPUT -> JSON SCHEMA / DOMAIN VALIDATOR -> REASON CODE -> BOUNDED REMEDIATION | HUMAN_REVIEW

For acquisition/parser workflows, distinguish schema mismatch, malformed record, insufficient provenance, authorization failure, repairable condition, and blocking ambiguity.

### P3

Unclaimed already has the stronger explicit rule that web/document/source content is untrusted and prompt injection cannot alter system policy, tool permissions, or approval requirements.

Policy must remain separate from the source record being evaluated. A source must never authorize itself.

### P4

Maintain a strict distinction between technical/domain readiness for reviewer attention and mandatory legal/privacy/business human approval.

A machine readiness state must never satisfy a human gate that project policy requires.

### P5

Execution fingerprinting is potentially valuable for Unclaimed because provenance and later auditability are central.

A future case/run fingerprint may compose immutable raw/source hash, source-contract version/hash, active policy version/hash, schema bundle version/hash, code/build commit, approval references, and model/prompt/template hash where an LLM materially affects the result.

Do not add this as broad infrastructure before a real Stage B need is demonstrated.

### P6

Unclaimed already has a stronger lifecycle evidence primitive than ForgeLab in AuditEventWriter.

The writer creates append-only events linked through SHA-256 hashes.

For real source/acquisition attempts, prefer explicit lifecycle semantics such as:

ATTEMPT_STARTED -> ATTEMPT_SUCCEEDED | ATTEMPT_BLOCKED | ATTEMPT_FAILED | ATTEMPT_CANCELLED

with reason codes and evidence references.

Missing terminal evidence must not be interpreted as success.

## Stage B / authorization boundary preserved

This conversation does not grant any new real-world execution permission.

It does not authorize remote source preflight, downloads, PII processing, external owner/person search, identity/contact enrichment, outreach, value research, claim submission, legal representation, or reuse of consumed approvals.

The canonical Unclaimed single next action and gate state remain governed by the current repository handover and decisions.

## Cross-project architectural decision

Use compatible concepts first, not a shared package.

Potential shared code extraction is considered only after ForgeLab has a real implementation, Unclaimed has a real implementation, duplication is demonstrated, and extraction reduces maintenance/risk rather than increasing coupling.

## Practical implication for Unclaimed

Treat the six-pattern kernel as a benchmark and diagnostic framework.

Do not interrupt the current Stage B product path to build a new generic execution framework.

If a Stage B/P1 failure maps to one of P1-P6, implement the smallest project-native correction and preserve all existing privacy, source, evidence, and human-gate constraints.
