# NY MVP-1 Follow-Up Cost Measurement — Ruff Patch-Loop Root Cause Audit

Date: 2026-09-18

## Trigger

Two consecutive corrective commits did not close the same CI lint defect, so the project patch-loop rule required a root-cause audit before another correction.

## Root cause

The first corrective edit attempted to split a long test assertion by inserting a newline through a connector-side string replacement. The replacement serialized the sequence as the literal characters `\\n` inside the Python source instead of an actual newline.

The second corrective edit targeted a different escaped representation and therefore did not match the repository content. The malformed literal sequence remained unchanged.

This is an edit-transport/serialization defect in the corrective patch, not a defect in the follow-up cost measurement domain logic or JSON contracts.

## Remediation

Do not perform another escape-sequence replacement.

Rewrite the complete final test function as canonical multiline Python source, with short local variables for the schema property maps. Then rerun the full GitHub CI.

No product logic, schema semantics, arithmetic or privacy boundary is changed by this remediation.
