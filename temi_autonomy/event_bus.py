from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List
import json

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None


DEFAULT_CONFIG: Dict[str, Any] = {
    "events": {
        "ALERT_HAZARD": {"priority": 100, "threshold": 0.85, "suppresses": ["ALL"], "temporal_frames": 2},
        "ALERT_CLINICAL_FALL": {
            "priority": 90,
            "threshold": 0.90,
            "suppresses": ["NAVIGATE_TO_PERSON", "OFFER_ASSISTANCE", "GREET_USER"],
            "temporal_frames": 3,
            "constraints": {"requires": ["posture_classification", "frame_sequence"], "interrupt": True},
        },
        "FLAG_SECURITY_CONCERN": {
            "priority": 80,
            "threshold": 0.75,
            "suppresses": ["NAVIGATE_TO_PERSON", "OFFER_ASSISTANCE", "GREET_USER", "INITIATE_BRIEFING"],
            "temporal_frames": 2,
            "constraints": {"no_movement": True, "no_identity_resolution": True},
        },
        "NAVIGATE_TO_PERSON": {
            "priority": 50,
            "threshold": 0.85,
            "suppresses": ["GREET_USER"],
            "constraints": {"requires": ["identity_verified", "explicit_command"]},
        },
        "OFFER_ASSISTANCE": {
            "priority": 40,
            "threshold": 0.65,
            "suppresses": ["GREET_USER"],
            "temporal_frames": 2,
            "constraints": {"requires_confirmation": True, "cooldown": True},
        },
        "MONITORING_EVENT": {"priority": 30, "threshold": 0.70, "suppresses": []},
        "GREET_USER": {"priority": 10, "threshold": 0.60, "suppresses": [], "constraints": {"cooldown": True}},
        "NO_ACTION": {"priority": 0, "threshold": 0.0, "suppresses": []},
    }
}


@dataclass(frozen=True)
class Event:
    event_type: str
    confidence: float
    data: Dict[str, Any] = field(default_factory=dict)


class EventBus:
    def __init__(self, config_path: str = "config/event_config.yaml") -> None:
        self.config = self._load_config(config_path)

    def _load_config(self, config_path: str) -> Dict[str, Any]:
        path = Path(config_path)
        if path.exists() and yaml is not None:
            with path.open("r", encoding="utf-8") as handle:
                parsed = yaml.safe_load(handle) or {}
            if "events" in parsed:
                return parsed
        return json.loads(json.dumps(DEFAULT_CONFIG))

    def event_cfg(self, event_type: str) -> Dict[str, Any]:
        return self.config["events"].get(event_type, self.config["events"]["NO_ACTION"])

    def threshold_pass(self, event: Event) -> bool:
        return event.confidence >= float(self.event_cfg(event.event_type).get("threshold", 1.0))

    def apply_thresholds(self, events: Iterable[Event]) -> List[Event]:
        valid = [e for e in events if self.threshold_pass(e)]
        return valid or [Event("NO_ACTION", 1.0, {})]

    def apply_suppression(self, events: List[Event]) -> List[Event]:
        if not events:
            return [Event("NO_ACTION", 1.0, {})]

        by_priority = sorted(
            events,
            key=lambda e: (self.event_cfg(e.event_type).get("priority", 0), e.confidence),
            reverse=True,
        )
        winner = by_priority[0]
        suppresses = set(self.event_cfg(winner.event_type).get("suppresses", []))
        if "ALL" in suppresses:
            return [winner]

        survivors = [winner]
        for event in by_priority[1:]:
            if event.event_type not in suppresses:
                survivors.append(event)
        return survivors

    def arbitrate(self, events: List[Event]) -> Event:
        return sorted(
            events,
            key=lambda e: (self.event_cfg(e.event_type).get("priority", 0), e.confidence),
            reverse=True,
        )[0]

    def process(self, events: Iterable[Event]) -> Event:
        gated = self.apply_thresholds(events)
        suppressed = self.apply_suppression(gated)
        return self.arbitrate(suppressed)
