from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from .event_bus import Event


class EventLogger:
    def __init__(self, path: str = "logs/events.log") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, candidates: Iterable[Event], final_event: Event) -> None:
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "candidates": [{"type": e.event_type, "confidence": e.confidence} for e in candidates],
            "final": {"type": final_event.event_type, "confidence": final_event.confidence},
        }
        self.path.write_text(self.path.read_text(encoding="utf-8") + json.dumps(payload) + "\n", encoding="utf-8") if self.path.exists() else self.path.write_text(json.dumps(payload) + "\n", encoding="utf-8")
