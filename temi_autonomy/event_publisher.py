from __future__ import annotations

from .event_bus import Event


class EventPublisher:
    def publish(self, event: Event) -> None:
        print(f"[PUBLISH] {event.event_type} ({event.confidence})")
