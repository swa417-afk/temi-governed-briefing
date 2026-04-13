from __future__ import annotations

from typing import Dict, List

from .event_bus import Event


def process_ai_output(ai_json: Dict) -> List[Event]:
    event_type = str(ai_json.get("event_type", "NO_ACTION"))
    confidence = float(ai_json.get("confidence", 0.0))
    return [Event(event_type=event_type, confidence=confidence, data=ai_json)]
