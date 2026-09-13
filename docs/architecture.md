# Architecture — M0 baseline

## Principle

The platform is a deterministic workflow system with agent-assisted domain modules, not an uncontrolled agent mesh.

```text
Reviewer UI
   |
FastAPI application layer
   |
A00 Orchestrator + State Machine + Gate Engine
   |
Domain agents A01-A23
   |
Contracts + Policy Engine + Budget Engine
   |
Repositories / Adapters / Source Clients
   |
PostgreSQL + immutable raw storage + append-only audit
```

## M0 boundary

M0 establishes the repository, runtime, health endpoint, PostgreSQL development configuration, tests, lint/type gates, PowerShell automation and CI. Business agents remain placeholders until their contracts exist.

## Safety boundary

No outreach, legal decision, claimant verification, fee agreement or claim submission is enabled in M0.
