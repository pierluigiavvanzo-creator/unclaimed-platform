# ROADMAP.md

Last updated: 2026-09-13

| Milestone | Status | Exit evidence |
|---|---|---|
| M0 — Repository & Development Harness | VERIFIED | Windows harness and GitHub CI green |
| M1 — Machine Contracts | VERIFIED | Windows Ruff/mypy green, 12 tests passed, smoke green, GitHub CI green |
| M2 — State & Governance Core | VERIFIED | GitHub CI green; Windows Ruff/mypy green; 24 tests passed; smoke 2 passed |
| M3 — California Data Spike | READINESS GATE — CONTRACTS CI VERIFIED ON CANDIDATE | Source inventory and A01 acquisition boundary complete; real acquisition still blocked |

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
- candidate branch `m3-acquisition-contracts` GitHub CI green: Ruff PASS, mypy PASS, pytest 30 passed.

## M3 still required before any real California acquisition

1. promote the verified candidate to the canonical development branch after owner approval;
2. define immutable raw-storage persistence and retention behavior;
3. define provenance persistence into the append-only audit trail;
4. define privacy/data-minimization constraints for the bounded spike;
5. explicitly approve the California SCO source for real use;
6. implement bounded read-only retrieval with transport/size/content validation;
7. only then execute a bounded California spike with no unnecessary PII;
8. verify the actual CSV layout before implementing A02 row normalization.

## Still out of scope until later gates

- beneficiary matching on real data before M3 readiness approval;
- autonomous outreach;
- legal determinations;
- autonomous claimant verification;
- fee agreement execution;
- claim submission;
- unapproved scraping or restricted-source access.
