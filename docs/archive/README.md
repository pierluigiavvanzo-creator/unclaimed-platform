# Documentation Archive

This directory contains point-in-time audit, diagnostic, execution-review and historical evidence narratives that were previously stored under `docs/audits/`.

## Authority

Files in this directory are retained for provenance and historical reproducibility. They are **not automatically current operating instructions**.

For current project state and next actions, use:

1. `AGENTS_MASTER.md`
2. `AGENTS.md`
3. `PRODUCT_STRATEGY_MVP1.md`
4. `PROJECT_STATE.md`
5. `ROADMAP.md`
6. `DECISIONS.md`
7. `docs/handovers/HANDOVER_CURRENT.md`

Historical approvals remain consumed/non-reusable exactly as recorded. Moving a document into this archive does not reactivate, renew or alter any approval.

## Path migration

On 2026-10-09, historical audit markdown files were moved from `docs/audits/<FILE>.md` to `docs/archive/<FILE>.md`.

Active code, tests and current machine proposals must reference the archive path when they need a historical provenance document.

Do not add new active audit snapshots under `docs/audits/`. Record current operating state in the canonical state/decision/handover files and archive point-in-time review artifacts here.
