from __future__ import annotations

from collections import defaultdict, deque
from typing import Deque, Dict

from .event_bus import Event


class TemporalBuffer:
    def __init__(self, size: int = 5) -> None:
        self.buffers: Dict[str, Deque[Event]] = defaultdict(lambda: deque(maxlen=size))

    def add(self, event: Event) -> None:
        self.buffers[event.event_type].append(event)

    def is_stable(self, event_type: str, required_frames: int) -> bool:
        return len(self.buffers[event_type]) >= max(1, required_frames)
