# ADR-0001 — Deterministic orchestration core

## Status
Accepted for M0.

## Decision
State transitions, policy gates, budget controls and audit are owned by deterministic core modules. Domain agents may propose decisions but cannot bypass those gates. External LLM/provider SDKs are isolated behind adapters.

## Why
This preserves reproducibility, provenance, testing and fail-closed behavior while allowing agentic components to evolve independently.

## Consequence
Agent implementation starts only after versioned contracts and contract tests exist.
