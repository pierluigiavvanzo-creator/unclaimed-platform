# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Windows Ruff/mypy green, 12 tests passed, smoke green, GitHub CI green |
| M2 — State & Governance Core | VERIFIED | GitHub CI green; Windows Ruff/mypy green; 24 tests passed; smoke 2 passed |
| M3 — California Data Spike | RAW STORAGE / PRIVACY GATES CI VERIFIED ON CANDIDATE — HUMAN PROMOTION GATE | Source readiness, A01 acquisition contracts and raw persistence/governance boundary verified; real acquisition still blocked |

## M3 completed readiness work

- California source/legal inventory completed using authoritative government sources;
- California SCO public bulk CSV identified as the preferred future real-data candidate;
- deferred sources classified as mock/reference/deferred;
- A01 raw-acquisition request/result contracts defined at version `1.0.0`;
- `REAL` requests require an explicit approval identifier;
- acquisition scope constrained to `RAW_INGEST_ONLY`;
- immutable raw artifact metadata includes SHA-256, byte count, content type and storage reference;
- provenance includes source URI, authority, acquisition method, terms-review reference and retrieval time;
- California SCO adapter boundary implemented fail-closed with no network retrieval;
- deferred-source deterministic mock adapter and fixtures implemented;
- acquisition-contract candidate promoted to the canonical development branch and stable M0–M3 checkpoint reconciled to `main`;
- M3 raw-storage/privacy REUSE FIRST evaluation completed;
- content-addressed raw-byte persistence implemented behind `ImmutableRawStore`;
- immutable provenance records use separate deterministic SHA-256 record hashes and support append-only acquisition history for identical raw bytes;
- successful new persistence reuses the existing M2 audit SHA-256 hash-chain writer;
- trusted privacy/data-minimization policy is separated from acquisition context;
- fail-closed gates cover source approval, required provenance, processing purpose, retention, data scope, field minimization, PII and synthetic/real scope;
- no real-source policy or real-source registry entry was added;
- candidate branch `m3-raw-storage-privacy-gates` GitHub CI run `34766966136` green: Ruff PASS, mypy PASS on 16 source files, contract 17 passed, smoke 2 passed, full pytest 51 passed with 2 known dependency warnings.

## M3 still required before any real California acquisition

1. complete final documentation CI and obtain owner approval to promote `m3-raw-storage-privacy-gates` to the canonical development branch;
2. promote the verified candidate using history-preserving Git operations; do not force-push;
3. explicitly approve a versioned real-source governance policy and California SCO source entry through a separate human gate;
4. define production raw-storage/audit durability requirements as needed for the bounded real-data spike, without silently treating the local filesystem adapter as production WORM storage;
5. implement bounded read-only retrieval with transport, redirect, size, timeout and content validation;
6. only then execute a separately authorized bounded California spike with no unnecessary PII;
7. verify the actual CSV layout from authorized evidence before implementing A02 row normalization;
8. keep beneficiary matching blocked until the later matching/privacy/legal gates are satisfied.

## Still out of scope until later gates

- real California acquisition before explicit source/policy approval and retrieval verification;
- beneficiary matching on real data before M3 readiness approval;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.
