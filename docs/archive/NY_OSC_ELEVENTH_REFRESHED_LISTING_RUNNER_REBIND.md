# NY OSC Attempt 11 — Refreshed Listing Runner Rebind

Date: 2026-09-23

Status: `PASS_RUNNER_REBOUND_NEW_HUMAN_GRANTS_REQUIRED`

## Trigger

The Product Owner supplied a fresh authenticated-listing screenshot showing an exact match to the newly accepted metadata snapshot:

- `FINDERS.zip`
- `390.51 MB`
- `9/23/2026, 1:12:44 PM`

Before creating an execution-usable fresh receipt, repository inspection found that the protected Gate-11 runner still hard-coded the prior expected last-modified value:

`9/16/2026, 1:33:31 PM`

Therefore the existing protected runner would have failed closed against the new listing even though the screenshot matched the refreshed metadata snapshot.

## Minimal remediation

Only the Gate-11 listing metadata binding was changed:

- old expected last modified: `9/16/2026, 1:33:31 PM`
- new expected last modified: `9/23/2026, 1:12:44 PM`

A regression test was added requiring the new value exactly twice in the runner and forbidding the old value.

No parser, projector, classification vocabulary, product-slice logic, privacy boundary, download count, retry count, freshness policy or network behavior was changed.

## New protected runner checkpoint

`bac89609e9069efc98fcd0866b89ee4ee16f1689`

CI:

`35859448715 — SUCCESS`

Verified jobs:

- quality — SUCCESS;
- streamlit-candidate — SUCCESS;
- Ruff — SUCCESS;
- mypy — SUCCESS;
- contract tests — SUCCESS;
- smoke tests — SUCCESS;
- full pytest suite — SUCCESS;
- frontend lint/typecheck/build — SUCCESS;
- Streamlit safety/startup — SUCCESS.

## Authorization consequence

The previously recorded Attempt-11 grants and refresh-4 preflight authorization are bound to the earlier protected runner checkpoint:

`ce005f08a3bbd23eb8fac6088917109f7864e924`

They were not consumed, but they cannot authorize execution of the new protected runner because Gate 11 requires exact checkpoint binding.

Therefore they are operationally:

`NON_REUSABLE_FOR_NEW_RUNNER_CHECKPOINT`

No fresh receipt was created from the latest screenshot because the corresponding preflight authorization was bound to the obsolete runner checkpoint.

## Next action

Request the first two Attempt-11 grants again, now specifically bound to runner checkpoint:

`bac89609e9069efc98fcd0866b89ee4ee16f1689`

Required phrases:

`APPROVO NY OSC ELEVENTH TRANSIENT LOCAL FILE BOUNDED ONCE`

`APPROVO NY OSC OWNER NAME FILE ELEVENTH BOUNDED TRANSIENT PII ATTEMPT ONCE`

After they are recorded, request a new separate:

`AUTHORIZE_NY_OSC_ELEVENTH_FRESH_LISTING_PREFLIGHT`

Then obtain a new exact-match screenshot before creating a fresh receipt.

No download is authorized by this remediation.
