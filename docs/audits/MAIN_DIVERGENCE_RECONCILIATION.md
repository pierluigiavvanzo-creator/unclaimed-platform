# Main Branch Divergence Reconciliation Audit

Date: 2026-09-13

Class: **B — Material Upgrade**

## Objective

Reconcile the divergence between `main` and the verified development branch without losing Git history, without overwriting the canonical development contract, and without introducing code changes.

## Baselines inspected

- `main`: `e694d8476b949384a108e08157074ad54d803717`
- canonical development branch `m2-state-governance-core`: `757202bb079cfeb01d0e1c5648ab26c9095be89e`
- merge base: `30c54cf50820e2d6204f4b06ac4b03e46b21b71d`

At audit time, the development branch was 15 commits ahead of the merge base while `main` had 2 exclusive commits.

## Main-only history

The two commits exclusive to `main` are:

1. `96b9bd1b2ad5ff3fd90e94e6766446b3c1e91c8f` — `Create AGENTS.md with operational guidelines`
2. `e694d8476b949384a108e08157074ad54d803717` — `Refactor AGENTS.md for clarity and structure`

Both commits actually modify a repository path named `root`, not `AGENTS.md`. The file contents identify themselves as `AGENTS.md`, but the filename is incorrect.

## Canonical governance comparison

The verified development branch already contains the actual root-level `AGENTS.md` used throughout M0-M3.

The canonical file is materially more specific to this project. It includes, among other controls:

- resolved A00-A23 agent IDs;
- target architecture and repository structure;
- REUSE-FIRST evaluation requirements;
- contract-first/schema-first development;
- mock-first development;
- fail-closed policy behavior;
- deterministic core constraints;
- explicit source/legal readiness gates;
- test pyramid and milestone gates;
- Git safety rules;
- checkpoint/rollback rules;
- handover requirements;
- context-health rules;
- human gates for legal and irreversible commercial decisions.

The generic `root` guidance contains useful general principles, but these are either already represented in the canonical `AGENTS.md` or are weaker than the existing verified rules.

## Conflicts intentionally not imported

Two parts of the generic `root` content must not overwrite current governance:

1. Its suggested generic M0-M7 roadmap does not match the milestone definitions already used and verified in `PROJECT_STATE.md` and `ROADMAP.md`.
2. Its generic instruction to commit changes after work conflicts with the canonical human-gate rule that commit/push decisions require explicit owner control.

No silent milestone renaming or Git-policy relaxation is therefore performed.

## Reconciliation decision

The integration candidate will:

- preserve `main` and `m2-state-governance-core` as parents of a single history-preserving merge commit;
- use the verified development tree as the content baseline;
- keep the actual `AGENTS.md` unchanged;
- intentionally omit the misnamed `root` file from the reconciled tree;
- record the branch/integration policy in `DECISIONS.md` as D-005;
- make no application-code, schema, source-registry, policy, or runtime behavior changes.

The old `root` contents remain permanently recoverable from Git history through the two `main` commits.

## Main integration policy after reconciliation

- Feature/candidate branches are used for bounded implementation and verification.
- Verified candidates are promoted into the canonical development branch.
- `main` is updated at meaningful verified milestone or gate boundaries rather than after each micro-task.
- Direct development commits to `main` should be avoided except owner-approved integration or emergency/hotfix work.

## Acceptance criteria

Before merging the integration candidate into `main`:

1. the merge commit must contain both histories as parents;
2. `root` must be absent from the resulting tree;
3. canonical `AGENTS.md` must remain present and unchanged;
4. the complete GitHub CI workflow must pass;
5. no runtime/code behavior may change as part of this reconciliation;
6. the final diff versus `main` must be reviewed before moving `main`.
