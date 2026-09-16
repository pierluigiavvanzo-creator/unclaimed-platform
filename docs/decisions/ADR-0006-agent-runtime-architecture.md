# ADR-0006 — Bounded Hybrid Agent Runtime Architecture

**Date:** 2026-09-16  
**Status:** Accepted — architecture direction; runtime implementation deferred  
**Scope:** Future agent runtime for A00–A23; no change to current M3 execution scope  
**Supersedes:** None  
**Extends:** ADR-0001 (Deterministic orchestration core), ADR-0002 (Versioned machine contracts), ADR-0003 (M2 governance core)

## Context

The canonical project architecture defines 24 logical capabilities, A00–A23. A logical capability is not required to be an independently running LLM agent.

The platform handles provenance-sensitive, privacy-sensitive and compliance-sensitive workflows. Turning every logical capability into an autonomous LLM process would increase orchestration complexity, latency, cost and nondeterminism without demonstrated product value.

The repository already separates domain capabilities under `src/unclaimed_platform/agents/`. That modular separation is retained. This ADR determines how those capabilities should be implemented when an agent runtime is introduced.

The current M3 California work remains the active development path. This ADR must not interrupt, re-scope or silently refactor that work.

## Decision

Adopt a **bounded hybrid runtime** with:

1. **A00 as the central orchestrator**, combining deterministic state-machine/gate enforcement with bounded AI-assisted routing or synthesis only where explicitly allowed.
2. **Approximately three core specialist AI roles at initial runtime pilot**, focused on tasks where ambiguity, unstructured evidence or research reasoning creates measurable value:
   - Identity/Candidate reasoning: primarily A05 + A07;
   - Genealogical/Research reasoning: primarily A06;
   - Evidence/Classification analysis: primarily A03 + A04, with A08 support where appropriate.
3. **Deterministic services as the default** for business-critical controls, including acquisition mechanics, normalization where deterministic parsing is sufficient, confidence thresholds, compliance, privacy, provenance controls, economics, deduplication, state transitions and audit.
4. **Hybrid/on-demand AI assistance** for capabilities where deterministic logic remains authoritative but AI may analyze unstructured inputs, prepare hypotheses, explain results or support human review.
5. **Human gates remain authoritative** for legal escalation, sensitive outreach/contracts, anti-fraud escalation, regulatory interpretation when required, and any existing policy-defined review gate.
6. **No capability may bypass deterministic policy, privacy, provenance, budget, contract or state-machine gates.** AI outputs are proposals/evidence/hypotheses unless a versioned contract explicitly grants a bounded automated action.
7. **No 24-agent runtime is authorized by this ADR.** Additional independent AI agents require benchmark evidence showing material product/economic value relative to added cost, latency, operational risk and maintenance.

## Capability classification

| ID | Capability | Target execution class |
|---|---|---|
| A00 | Orchestrator | HYBRID / ORCHESTRATOR |
| A01 | State Data Acquisition | DETERMINISTIC SERVICE |
| A02 | Data Normalization | SERVICE + AI FALLBACK |
| A03 | Insurance Classification | HYBRID |
| A04 | Death Evidence | HYBRID |
| A05 | Identity Resolution | AI SPECIALIST + DETERMINISTIC SCORING |
| A06 | Genealogical Research | AI SPECIALIST |
| A07 | Candidate Generation | AI SPECIALIST / HYBRID |
| A08 | Evidence Validation | SERVICE + AI ANALYSIS |
| A09 | Confidence Assessment | DETERMINISTIC |
| A10 | State Compliance Engine | DETERMINISTIC |
| A11 | Privacy & Data Governance | DETERMINISTIC |
| A12 | Legal Escalation | HUMAN GATE + AI SUPPORT |
| A13 | Source Verification | DETERMINISTIC / HYBRID |
| A14 | Market & Competitor Research | ON-DEMAND AI |
| A15 | Case Economics | DETERMINISTIC |
| A16 | Human Investigator Interface | HUMAN INTERFACE |
| A17 | Outreach Preparation | AI-ASSISTED + HUMAN GATE |
| A18 | Claim Management | WORKFLOW SERVICE |
| A19 | Case Linking & Deduplication | DETERMINISTIC |
| A20 | Contracts & Fee Agreement | TEMPLATE/RULE ENGINE + HUMAN GATE |
| A21 | Anti-Fraud / Claimant Verification | HYBRID + HUMAN GATE |
| A22 | Insurer Verification | HYBRID |
| A23 | Regulatory & Terms Monitoring | HYBRID + HUMAN VALIDATION |

These classifications are target defaults, not permission to implement or activate a capability before its roadmap/legal/privacy prerequisites are satisfied.

## Runtime principles

### Deterministic authority

The deterministic control plane owns:

- state transitions;
- policy and compliance gates;
- privacy gates;
- provenance requirements;
- versioned machine contracts;
- budget limits;
- retry limits;
- confidence thresholds where policy-defined;
- audit events;
- fail-closed behavior.

### AI boundaries

AI components may:

- interpret unstructured evidence;
- generate competing hypotheses;
- perform bounded research/reasoning;
- propose entity links or candidates;
- summarize evidence and contradictions;
- prepare human-review material.

AI components must not:

- invent missing evidence or provenance;
- convert an unsupported hypothesis into a fact;
- bypass a policy/privacy/legal/human gate;
- silently alter thresholds, contracts or architecture;
- perform unrestricted retries or open-ended autonomous execution;
- use a source or authority not approved for the active task.

### Bounded execution lifecycle

Every AI-assisted execution should follow, where applicable:

`precheck → isolation/backup → execute → validate contract → deterministic gates → diagnostics/repair within retry budget → smoke/acceptance check → audit/report`

Escalate to `HUMAN_REVIEW`, `STOP` or `DEFER` when the relevant contract or gate requires it.

## Runtime pilot gate

Do **not** implement a new multi-agent framework during the current M3 work merely because this ADR exists.

A runtime pilot may start only when:

1. the relevant M3/M4 product workflow is sufficiently stable to benchmark;
2. input/output contracts and deterministic gates already exist;
3. a concrete user workflow can measure quality, latency, cost and human-time reduction;
4. REUSE FIRST scouting has evaluated mature orchestration/runtime options and licenses;
5. the pilot has a rollback path and does not block the active product milestone.

Initial pilot topology:

```text
Human Product Owner / Reviewer
            |
            v
   A00 Hybrid Orchestrator
            |
    +-------+-------+
    |       |       |
    v       v       v
Identity  Research  Analysis
A05/A07    A06     A03/A04
    \       |       /
     \      |      /
      v     v     v
 Deterministic Control Plane
 A01/A02/A08/A09/A10/A11/
 A13/A15/A19 + contracts/audit
            |
            v
       Human Gates
```

## Evaluation criteria for adding or splitting AI agents

An additional independent AI role is justified only when benchmark evidence shows a material improvement in one or more of:

- usable product outcome quality;
- evidence/provenance completeness;
- investigator time saved;
- case throughput;
- economically relevant conversion or case value;
- isolation/security benefit;

and that improvement outweighs:

- inference/runtime cost;
- latency;
- routing and coordination failure modes;
- observability/debugging burden;
- privacy/compliance exposure;
- maintenance complexity.

The optimization objective is **economic value × usable product value / user time**, subject to compliance, privacy, provenance and safety constraints.

## Consequences

### Positive

- preserves the existing A00–A23 capability architecture without requiring 24 autonomous LLMs;
- keeps high-risk controls reproducible and auditable;
- limits cost and latency until product evidence justifies expansion;
- allows AI reasoning where it has the highest expected value;
- keeps human authority at legally or operationally sensitive gates;
- permits future provider/runtime changes behind adapters without domain rewrites.

### Trade-offs

- some capabilities will remain less flexible than fully autonomous agents;
- hybrid boundaries require explicit contracts and observability;
- AI fallback paths need dedicated adversarial and regression testing;
- future agent specialization must be benchmark-driven rather than added ad hoc.

## Alternatives considered

### 1. One autonomous LLM for the whole platform

Rejected as the target architecture because it concentrates too much authority in a nondeterministic component and weakens separation of duties, testing and provenance boundaries.

### 2. Twenty-four independent LLM agents

Rejected as the default target because capability count does not justify runtime-agent count. It adds coordination, cost, latency and failure modes before value is demonstrated.

### 3. Fully deterministic platform with no AI runtime

Retained as the baseline for controls but rejected as the complete long-term architecture because identity, genealogy, unstructured evidence and research can benefit from bounded reasoning capabilities.

## Implementation impact now

**None on the active M3 execution path.**

This ADR is architectural documentation only. It does not authorize:

- SCO access;
- external authority downloads;
- parser/regex changes;
- reuse of consumed execution/privacy approvals;
- activation of new AI providers;
- refactoring of active M3 modules;
- changes to the current handover SINGLE NEXT ACTION.

Any future implementation must be introduced as a separately scoped task with its own acceptance criteria, tests and approvals.

## Review trigger

Review this ADR after the first measurable end-to-end identity/research workflow exists, or before adopting any multi-agent runtime/framework, whichever occurs first.
