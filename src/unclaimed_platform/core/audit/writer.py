from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Mapping
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    case_id: str | None
    timestamp: str
    event_type: str
    actor_type: str
    actor_id: str
    payload: Mapping[str, Any]
    previous_event_hash: str | None
    event_hash: str


Clock = Callable[[], datetime]
IdFactory = Callable[[], UUID]


class AuditEventWriter:
    """Append-only in-memory hash-chain writer used by the M2 governance core."""

    def __init__(
        self,
        *,
        clock: Clock | None = None,
        id_factory: IdFactory | None = None,
    ) -> None:
        self._events: list[AuditEvent] = []
        self._clock = clock or (lambda: datetime.now(UTC))
        self._id_factory = id_factory or uuid4

    @property
    def events(self) -> tuple[AuditEvent, ...]:
        return tuple(self._events)

    def append(
        self,
        *,
        case_id: str | None,
        event_type: str,
        actor_type: str,
        actor_id: str,
        payload: Mapping[str, Any],
    ) -> AuditEvent:
        timestamp = self._clock().astimezone(UTC).isoformat().replace("+00:00", "Z")
        event_id = str(self._id_factory())
        previous_hash = self._events[-1].event_hash if self._events else None
        hash_material: dict[str, Any] = {
            "event_id": event_id,
            "case_id": case_id,
            "timestamp": timestamp,
            "event_type": event_type,
            "actor_type": actor_type,
            "actor_id": actor_id,
            "payload": dict(payload),
            "previous_event_hash": previous_hash,
        }
        encoded = json.dumps(
            hash_material,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")
        event_hash = hashlib.sha256(encoded).hexdigest()
        event = AuditEvent(
            event_id=event_id,
            case_id=case_id,
            timestamp=timestamp,
            event_type=event_type,
            actor_type=actor_type,
            actor_id=actor_id,
            payload=dict(payload),
            previous_event_hash=previous_hash,
            event_hash=event_hash,
        )
        self._events.append(event)
        return event

    def verify_chain(self) -> bool:
        previous_hash: str | None = None
        for event in self._events:
            data = asdict(event)
            stored_hash = data.pop("event_hash")
            if data["previous_event_hash"] != previous_hash:
                return False
            encoded = json.dumps(
                data,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode("utf-8")
            calculated = hashlib.sha256(encoded).hexdigest()
            if calculated != stored_hash:
                return False
            previous_hash = stored_hash
        return True
