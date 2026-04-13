from __future__ import annotations

from typing import Dict

from .ai_processor import process_ai_output
from .event_bus import Event, EventBus
from .event_executor import EventExecutor
from .event_publisher import EventPublisher
from .temporal_buffer import TemporalBuffer


class GovernedPipeline:
    def __init__(self, config_path: str = "config/event_config.yaml") -> None:
        self.event_bus = EventBus(config_path=config_path)
        self.temporal = TemporalBuffer()
        self.executor = EventExecutor()
        self.publisher = EventPublisher()

    def run_cycle(self, sensor_input: Dict) -> Event:
        candidates = process_ai_output(sensor_input)
        stable = []
        for event in candidates:
            self.temporal.add(event)
            required = int(self.event_bus.event_cfg(event.event_type).get("temporal_frames", 1))
            if self.temporal.is_stable(event.event_type, required):
                stable.append(event)

        final_event = self.event_bus.process(stable)
        self.executor.execute(final_event)
        self.publisher.publish(final_event)
        return final_event
