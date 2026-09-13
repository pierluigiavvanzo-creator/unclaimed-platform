# Unclaimed Platform

Traceable, human-gated platform for investigating potentially unclaimed life-insurance benefits.

## Development status

Current milestone: **M0 — Repository & Development Harness**.

M0 provides the development foundation only: Python environment, FastAPI health endpoint, PostgreSQL development service, quality gates, PowerShell automation and CI. It does **not** implement beneficiary outreach, legal determinations, claims submission or autonomous contact.

## Architecture rule

The deterministic core owns orchestration, state transitions, policy gates, budgets and audit. Domain agents operate behind versioned contracts and adapters. LLM/provider SDKs must not leak into domain code.

## Windows bootstrap

```powershell
git clone https://github.com/pierluigiavvanzo-creator/unclaimed-platform.git
cd unclaimed-platform
git checkout m0-foundation
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\bootstrap.ps1
.\scripts\test.ps1
.\scripts\smoke.ps1
```
