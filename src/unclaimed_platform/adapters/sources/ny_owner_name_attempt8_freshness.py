"""Attempt-8 freshness handoff for the NY OSC bounded manual download.

This module performs no network access and handles no owner data.  It fixes the
attempt-7 timing defect by proving that the authorized manual download *started*
inside the fresh-preflight window.  Runtime processing may finish later without
retroactively invalidating a correctly started bounded download.
"""

from __future__ import annotations

from datetime import UTC, datetime

EXPECTED_PREFLIGHT_FRESHNESS_SECONDS = 900


def _parse_utc_timestamp(value: str, label: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label} timestamp is missing")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{label} timestamp is invalid") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{label} timestamp must include timezone")
    return parsed.astimezone(UTC)


def validate_authorized_download_started_at(
    *,
    preflight_performed_at_utc: str,
    authorized_download_started_at_utc: str,
    freshness_window_seconds: int,
    observed_now_utc: datetime | None = None,
) -> datetime:
    """Validate the fail-closed attempt-8 freshness handoff.

    The download start must be at/after the exact-match preflight and no later
    than its 900-second freshness deadline.  The recorded start must also not be
    in the future relative to the validating runtime.  No extension, retry, or
    network authority is granted by this function.
    """

    if freshness_window_seconds != EXPECTED_PREFLIGHT_FRESHNESS_SECONDS:
        raise ValueError("fresh preflight freshness policy mismatch")

    performed_at = _parse_utc_timestamp(
        preflight_performed_at_utc,
        "fresh preflight",
    )
    download_started_at = _parse_utc_timestamp(
        authorized_download_started_at_utc,
        "authorized download start",
    )
    now = (observed_now_utc or datetime.now(UTC)).astimezone(UTC)

    if download_started_at < performed_at:
        raise ValueError("authorized download start predates fresh preflight")

    elapsed = (download_started_at - performed_at).total_seconds()
    if elapsed > freshness_window_seconds:
        raise ValueError("authorized download start is outside fresh preflight window")

    if download_started_at > now:
        raise ValueError("authorized download start is future-dated")

    return download_started_at
