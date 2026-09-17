# DECISIONS.md

## D-001 — PowerShell Windows orchestration

Date: 2026-09-13

Status: Accepted

Decision:
Use PowerShell as the Windows bootstrap/orchestration layer.

Reason:
The initial development and testing environment is Windows-based.

Alternatives considered:
- Python
- Bash
- Make

Consequences:
PowerShell scripts must remain idempotent, explicit on failure and free of secrets.

---

## D-002 — Deterministic governance core

Date: 2026-09-13

Status: Accepted

Context:
State transitions, policy gates, budgets and audit must be reproducible and must not depend on probabilistic model behavior.

Decision:
Keep state machine, policy gates, budget controls and audit in deterministic core modules. Domain agents can propose actions but cannot bypass core gates.

Reason:
This preserves fail-closed behavior, auditability and testability.

Alternatives considered:
- Agent-owned workflow transitions
- LLM-directed orchestration

Consequences:
A00 coordinates agents but governance authority remains in deterministic code.

---

## D-003 — Versioned JSON Schema contracts

Date: 2026-09-13

Status: Accepted

Context:
Independent agents and adapters require stable boundaries.

Decision:
Use JSON Schema draft 2020-12 as the canonical machine interchange contract with explicit versions and contract tests.

Reason:
Prevents silent schema drift and supports independent module development.

Alternatives considered:
- Pydantic-only runtime contracts
- Unversioned Python dictionaries

Consequences:
Breaking changes require explicit schema versioning and migration/adapter work.

---

## D-004 — Explicit M2 workflow whitelist

Date: 2026-09-13

Status: Accepted

Context:
M2 requires a deterministic lifecycle state machine. Mature FSM libraries exist, but the initial need is a small versioned whitelist with fail-closed semantics.

Decision:
Implement the M2 workflow whitelist using standard-library code and versioned JSON configuration. Missing policy routes to HUMAN_REVIEW, budget exhaustion stops progression, and terminal states cannot transition outward.

Reason:
The critical behavior remains directly auditable and testable without introducing a broader state-machine dependency. Reuse must be reconsidered if hierarchical or concurrent state complexity appears.

Alternatives considered:
- python-statemachine
- transitions

Consequences:
M2 has a small custom state core; future expansion requires an explicit superseding decision rather than silent framework growth.

---

## D-005 — Canonical development branch and main integration policy

Date: 2026-09-13

Status: Accepted

Context:
`main` diverged from the verified development history after two direct commits created and then expanded a file named `root` whose contents were intended to act as `AGENTS.md`. Meanwhile the verified development branch contains the actual `AGENTS.md` plus the M0-M3 implementation and governance history.

Decision:
- Treat `m2-state-governance-core` as the current canonical development/integration branch until it is explicitly renamed or superseded.
- Treat `main` as the stable milestone/release branch, not as the day-to-day development branch.
- Promote feature/candidate branches into the canonical development branch only after the relevant tests and gates pass.
- Update `main` only at meaningful verified milestone or gate boundaries.
- Reconcile the existing divergence with a history-preserving merge commit that has both histories as parents.
- Keep the actual canonical `AGENTS.md` unchanged as the governing development contract; do not carry the misnamed `root` file into the reconciled tree.
- Avoid direct commits to `main` except deliberate owner-approved integration or emergency/hotfix work.

Reason:
This preserves all Git history without replacing the more specific verified governance contract or allowing `main` and the active development history to drift independently.

Alternatives considered:
- Force-reset `main` to the development branch
- Replace canonical `AGENTS.md` with the generic `root` content
- Keep the branches permanently divergent

Consequences:
The first reconciliation into `main` is a non-fast-forward merge by design. After reconciliation, milestone merges should remain simple provided direct development on `main` is avoided. The misnamed `root` file remains recoverable from Git history but is intentionally absent from the reconciled working tree.

---

## D-006 — Streamlit replaces Vercel on the M3 reviewer critical path

Date: 2026-09-14

Status: Accepted

Context:
The owner explicitly directed the project to abandon Vercel after repeated project/deployment visibility inconsistencies and move the reviewer surface to Streamlit.

Decision:
Use Streamlit Community Cloud as the active M3 reviewer deployment target. Preserve deterministic governance and the existing versioned/typed read model as authority. Keep the existing Next.js/Vercel implementation only as rollback/history until Streamlit is remotely verified.

Reason:
This materially reduces deployment complexity and removes the need for a separate preview backend plus `REVIEWER_API_BASE_URL` wiring while preserving the current synthetic/read-only scope.

Alternatives considered:
- Continue Vercel diagnostics
- FastAPI templates
- Gradio

Consequences:
ADR-0005 supersedes the Vercel deployment-target portion of ADR-0004. No real acquisition, beneficiary matching, source approval, real PII or Supabase integration is enabled by this decision.

---

## D-007 — Decommission repository-side Vercel runtime integration

Date: 2026-09-14

Status: Accepted

Context:
Streamlit is the verified reviewer deployment target, while the owner continues to receive failed-deployment notifications from the historical Vercel path. Repository-side provider configuration is no longer required and creates avoidable ambiguity.

Decision:
- Remove all active Vercel deployment configuration from the canonical repository tree.
- Remove provider-specific deployment instructions from active application documentation.
- Keep the legacy Next.js reviewer only as a provider-neutral local/regression artifact.
- Add a contract test that rejects reintroduction of Vercel-named files or textual Vercel references in active runtime surfaces (`.github`, `apps`, `scripts`, `src`, and root runtime configuration files).
- Preserve historical ADRs/audits as inert records; history is not executable configuration.
- Treat any external Vercel Git/project connection as a provider-side integration that must be disconnected separately from the repository contents.

Reason:
This prevents repository changes from intentionally invoking or configuring Vercel and makes Streamlit the only active reviewer deployment path represented by runtime configuration.

Alternatives considered:
- Keep `vercel.json` as dormant rollback configuration.
- Delete the entire legacy Next.js reviewer.
- Leave the repository unchanged and rely only on provider-side settings.

Consequences:
Vercel deployment is unsupported from the active repository tree. Reintroducing a Vercel runtime integration requires a new explicit owner decision and corresponding test/governance update. An already-installed external Git integration may still receive repository events until it is disconnected at the provider/GitHub integration layer.

---

## D-008 — Fail-closed handling design for nonconforming California SCO PROPERTY_TYPE

Date: 2026-09-16

Status: Accepted as design; implementation pending separate gate

Context:
The bounded California SCO diagnostics established, for one examined row, that strict UTF-8 decoding and strict stdlib CSV parsing succeeded, the canonical 25-column shape was produced, stdlib field index `1` agreed with the custom projector's `PROPERTY_TYPE` field, and the shared field still failed the unchanged regex `^(?:[A-Z]{2}[0-9]{2}|ZZZZ)$`. The exact value, frequency, cause and source intent remain unknown. A reviewed handling proposal required disposition, continuation and privacy boundaries to remain separate.

Decision:
Accept `WHOLE_SOURCE_STOP` as the deterministic handling **design decision** for a canonical `PROPERTY_TYPE` that fails the unchanged validation boundary. The design emits only non-value-bearing control status/reason metadata and does not continue to later rows after the triggering condition.

This decision does not itself authorize or perform runtime implementation, another real-source execution, source activation, registry activation, privacy expansion, real-row quarantine, row-specific human inspection, parser/projector changes, regex changes, trimming/casing/normalization or semantic acceptance of the source value.

Reason:
This preserves the current fail-closed behavior without silently omitting rows, inventing source semantics, enabling continuation or introducing a new privacy/persistence boundary while semantic compatibility remains unresolved.

Alternatives considered:
- Row-level metadata defer with separately governed later continuation
- Real-row quarantine
- Metadata-only human-review route

Consequences:
- Runtime behavior remains unchanged until a separate implementation gate is reviewed and authorized.
- Source continuation after the nonconforming condition remains unauthorized.
- The accepted future control vocabulary is `PROPERTY_TYPE_NONCONFORMING_STOPPED` with reason `PROPERTY_TYPE_STRUCTURAL_NONCONFORMANCE`, subject to separate implementation review.
- Exact/derived `PROPERTY_TYPE`, real row/field content, hashes, exact lengths, `PROPERTY_ID`, owner/holder values and source-derived free text remain outside the persistence boundary.
- Any future continuation, real-row retention or row-specific inspection requires a separately reviewed design and authorization path.
- Source policy remains `PROPOSED`, registry remains disabled/unapproved, production classification remains inactive and downstream gates remain closed.

---

## D-009 — MVP-1 commercial validation becomes the product-priority objective

Date: 2026-09-17

Status: Accepted

Context:
The platform has a strong verified engineering and governance foundation, but product/economic validation remains incomplete. The current repository state still has zero approved real sources, unresolved semantic compatibility and blocked downstream identity, genealogy, matching, outreach and claim flows. Continued governance and diagnostic expansion without a real product vertical slice risks producing technically correct work with diminishing usable and commercial value.

Decision:
Adopt `PRODUCT_STRATEGY_MVP1.md` as a priority strategic source and make `MVP-1 — First Economically Actionable Case` the governing product-validation objective.

M3 California work remains on the critical path only insofar as it safely and minimally enables an approved real source. After one approved real source exists, priority shifts immediately to the shortest lawful, privacy-safe and deterministic vertical slice:

`approved real source -> acquisition -> normalization -> insurance classification -> candidate case -> provenance/evidence -> case economics -> reviewer console -> human continue/stop decision`.

Every substantial task must be classified A/B/C/D and identify the MVP-1 blocker or exit criterion it advances. Infrastructure, governance and diagnostics that do not materially advance MVP-1 are deprioritized unless required to control a Product Critical risk.

The project must collect real commercial baseline measurements before broadening scope. No revenue, conversion, case-value or success threshold is invented by this decision.

Reason:
This aligns project execution with the guiding metric `ECONOMIC VALUE x USABLE PRODUCT VALUE / USER TIME` and tests whether the platform can create commercially useful cases before investing further in broad automation or infrastructure.

Alternatives considered:
- Continue the existing milestone sequence without an explicit commercial-validation gate.
- Expand downstream agents and infrastructure before obtaining an approved real source.
- Reduce existing safety/governance controls to accelerate execution.

Consequences:
- `PRODUCT_STRATEGY_MVP1.md` is read immediately after `AGENTS.md` in the canonical read order.
- Existing law, privacy, security, source-authorization, fail-closed and deterministic governance controls are not weakened.
- The current California transport/archive-layout blocker is treated as an A/B critical-path enabler, not as an open-ended diagnostic program.
- Product Owner manual technical work must be minimized; human involvement should concentrate on material commercial, legal/privacy, security and irreversible architecture gates.
- Reuse scouting is mandatory before substantial custom downstream implementation.
- Full multi-state expansion, broad agent automation, automatic outreach, claim submission and nonessential infrastructure work remain lower priority until MVP-1 evidence exists.
