# NY OSC Property Type Code Shape — Offline Diagnostic

Date: 2026-09-18

Status: `OFFLINE_REMEDIATION_IMPLEMENTED_SYNTHETIC_ONLY`

## Trigger

The first real bounded execution stopped fail-closed with:

`PROPERTY_TYPE_CODE_FIELD_SHAPE_UNEXPECTED`

No retry is authorized and no real file is used in this diagnostic.

## Evidence considered

Persisted non-PII execution metadata:

- archive byte count: `409,477,526`;
- archive member count: `1`;
- selected text member uncompressed bytes: `1,939,569,781`;
- failure occurred before schema confirmation.

Official OSC public property-type tables show alphanumeric codes such as `IN03`, `AC01`, and historical forms such as `1A`. The offline issue is therefore more consistent with overly strict byte formatting/header recognition than with a requirement for punctuation inside the code itself.

## Narrow remediation

The schema-discovery harness now, on synthetic fixtures only:

- strips leading/trailing ASCII whitespace from the Property Type Code field;
- strips one matching pair of single or double quotes;
- recognizes the documented 14-field header after the same bounded normalization;
- tolerates UTF-8 BOM only on the first header field;
- records `NORMALIZED_DOCUMENTED_HEADER` when normalization was required;
- still requires the normalized Property Type Code itself to be strictly ASCII alphanumeric;
- still rejects internal whitespace/punctuation such as `IN 03`.

Owner name/address fields remain undecoded and are never logged or returned.

## Important limitation

This remediation is a hypothesis-driven offline fix, not proof of the real file's exact formatting. A future real-file retry requires a new explicit authorization because the prior Gate 2 is consumed and zero retry was authorized.
