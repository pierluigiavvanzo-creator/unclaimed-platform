# M3 CA SCO — Transport / Archive-Layout Revalidation Implementation Reuse Review

Date: 2026-09-17

Classification: `A/B — MVP-1 critical-path enabler`

Target blocker:

`FIRST_APPROVED_REAL_SOURCE -> transport/archive-layout baseline unresolved`

## Decision

Apply:

`REUSE -> INSPIRE -> minimal CUSTOM`

The implementation reuses the repository's already-tested exact-host `http.client`/TLS transport pattern and Python standard-library binary parsing primitives. It does not add a third-party remote-ZIP dependency.

## Candidates

### Existing project HTTPS transport pattern

- source: `scripts/ca_sco_property_type_semantic_verification.py`
- license: repository-native
- maintenance / maturity: already part of the CI-green project
- Python compatibility: Python 3.11
- security/privacy: exact HTTPS host; no redirect-following abstraction; explicit Range/body accounting pattern
- fit: high for the bounded HEAD/Range transport
- integration cost: low
- decision: `REUSE`
- reason: preserves the project's deterministic request accounting and avoids a new network dependency.

### Python standard library `struct`

- source: Python 3.11 standard library
- maintenance / maturity: Python standard library
- compatibility: exact project runtime
- security/privacy: local in-memory parsing only
- fit: high for the fixed classic-ZIP EOCD and central-directory record structures
- integration cost: minimal
- decision: `REUSE`
- reason: the accepted design needs only bounded structural metadata parsing, not a general archive reader.

### Python standard library `zipfile`

- source: https://docs.python.org/3/library/zipfile.html
- maintenance / maturity: Python standard library
- compatibility: Python 3.11+
- fit: useful reference implementation and synthetic-test generator
- integration cost: low
- decision: `INSPIRE / TEST-ONLY`
- reason: production `zipfile` is designed around seekable ZIP access and supports ZIP64, while this gate must explicitly reject ZIP64 and retain exact control over every network Range. It is used only to generate synthetic ZIP fixtures in unit tests.

### `remotezip`

- source: https://pypi.org/project/remotezip/
- repository: https://github.com/gtsystem/python-remotezip
- license: MIT (project metadata/repository)
- maintenance / maturity: established Python package for HTTP Range-backed ZIP access
- compatibility: Python HTTP/Range use case
- security/privacy: third-party networking layer
- fit: partial
- integration cost: moderate
- decision: `REJECT FOR THIS GATE`
- reason: remote seeks and central-directory discovery can result in additional Range requests depending on archive layout. The current authorization requires exact project-owned enforcement of 1 HEAD, at most 4 Range requests, 5 HTTP requests total, no widening and no retry.

### `Papyrine/RemoteZip`

- source: https://github.com/Papyrine/RemoteZip
- license: MIT
- fit: remote ZIP access with Range requests
- decision: `REJECT FOR THIS GATE`
- reason: its general-purpose behavior includes fallback / broader remote archive behavior that is unnecessary here and does not improve the strict fail-closed one-shot boundary.

## Result

No mature external component materially improves the exact authorized path without weakening request determinism or adding broader ZIP behavior.

The bounded implementation therefore uses:

1. repository-native HTTPS request mechanics;
2. standard-library `struct` for classic-ZIP metadata only;
3. `zipfile` only for synthetic tests;
4. no production decompression library;
5. no CSV parser;
6. no remote-ZIP third-party package.

This is intentionally not a reusable general ZIP client. It exists only to execute the already accepted bounded structural revalidation contract and should not be expanded without a new product need / gate.
