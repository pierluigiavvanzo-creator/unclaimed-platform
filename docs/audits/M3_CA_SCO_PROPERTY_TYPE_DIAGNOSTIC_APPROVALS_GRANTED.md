# M3 California SCO — PROPERTY_TYPE Diagnostic Approvals Granted

Date: 2026-09-15

Status: **BOTH FRESH APPROVALS GRANTED — NOT YET CONSUMED**

Authorization package SHA:

`daeaa7bfb7f7d73a61f011d394cc88393625866c`

Granted approvals:

- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION_BOUNDED`
- `APPROVE_PROPERTY_TYPE_DIAGNOSTIC_TRANSIENT_ROW_PRIVACY_BOUNDED`

Both are single-use, non-reusable, and durably evidenced under `sources/evidence/` with status `GRANTED_NOT_YET_CONSUMED`.

This record does not itself perform source access, create a network workflow, consume either approval, authorize remediation, or alter parser/regex/runtime behavior.

The next bounded gate is:

`ONE_SHOT_PROPERTY_TYPE_DIAGNOSTIC_EXECUTION`

Before any source request, execution must verify both approval evidences and their exact package-SHA pin.
