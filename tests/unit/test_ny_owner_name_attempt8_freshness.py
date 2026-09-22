from __future__ import annotations

from datetime import UTC, datetime, timedelta

import pytest

from unclaimed_platform.adapters.sources.ny_owner_name_attempt8_freshness import (
    EXPECTED_PREFLIGHT_FRESHNESS_SECONDS,
    validate_authorized_download_started_at,
)


def _stamp(value: datetime) -> str:
    return value.astimezone(UTC).isoformat().replace("+00:00", "Z")


def test_attempt8_accepts_download_started_inside_window_even_if_processing_is_later() -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    started = performed + timedelta(minutes=14, seconds=59)
    processing = performed + timedelta(minutes=35)

    validated = validate_authorized_download_started_at(
        preflight_performed_at_utc=_stamp(performed),
        authorized_download_started_at_utc=_stamp(started),
        freshness_window_seconds=EXPECTED_PREFLIGHT_FRESHNESS_SECONDS,
        observed_now_utc=processing,
    )

    assert validated == started


def test_attempt8_accepts_exact_freshness_boundary() -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    started = performed + timedelta(seconds=900)

    assert validate_authorized_download_started_at(
        preflight_performed_at_utc=_stamp(performed),
        authorized_download_started_at_utc=_stamp(started),
        freshness_window_seconds=900,
        observed_now_utc=started,
    ) == started


def test_attempt8_rejects_download_started_after_window() -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    started = performed + timedelta(seconds=901)

    with pytest.raises(ValueError, match="outside fresh preflight window"):
        validate_authorized_download_started_at(
            preflight_performed_at_utc=_stamp(performed),
            authorized_download_started_at_utc=_stamp(started),
            freshness_window_seconds=900,
            observed_now_utc=started,
        )


def test_attempt8_rejects_download_started_before_preflight() -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    started = performed - timedelta(seconds=1)

    with pytest.raises(ValueError, match="predates fresh preflight"):
        validate_authorized_download_started_at(
            preflight_performed_at_utc=_stamp(performed),
            authorized_download_started_at_utc=_stamp(started),
            freshness_window_seconds=900,
            observed_now_utc=performed,
        )


def test_attempt8_rejects_future_download_start() -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)
    now = performed + timedelta(minutes=1)
    started = now + timedelta(seconds=1)

    with pytest.raises(ValueError, match="future-dated"):
        validate_authorized_download_started_at(
            preflight_performed_at_utc=_stamp(performed),
            authorized_download_started_at_utc=_stamp(started),
            freshness_window_seconds=900,
            observed_now_utc=now,
        )


def test_attempt8_rejects_non_900_second_policy() -> None:
    performed = datetime(2026, 9, 22, 14, 39, 31, tzinfo=UTC)

    with pytest.raises(ValueError, match="freshness policy mismatch"):
        validate_authorized_download_started_at(
            preflight_performed_at_utc=_stamp(performed),
            authorized_download_started_at_utc=_stamp(performed),
            freshness_window_seconds=901,
            observed_now_utc=performed,
        )
