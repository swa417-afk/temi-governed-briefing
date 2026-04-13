from __future__ import annotations

from typing import Dict, List, Tuple

from .event_bus import Event


class EventExecutor:
    def __init__(self) -> None:
        self.actions: List[Tuple[str, str]] = []

    def execute(self, event: Event) -> None:
        t = event.event_type
        if t == "NO_ACTION":
            return
        if t == "ALERT_HAZARD":
            self._speak("Safety alert. Please evacuate immediately.")
        elif t == "ALERT_CLINICAL_FALL":
            self._speak("Potential fall detected. Alerting care staff.")
        elif t == "FLAG_SECURITY_CONCERN":
            self._speak("Unauthorized presence detected.")
        elif t == "NAVIGATE_TO_PERSON":
            self._navigate_to_user()
        elif t == "OFFER_ASSISTANCE":
            self._speak("Would you like assistance?")
        elif t == "GREET_USER":
            self._speak("Hello. How can I assist you?")

    def _speak(self, text: str) -> None:
        self.actions.append(("speak", text))
        print(f"[Temi SPEAK]: {text}")

    def _navigate_to_user(self) -> None:
        self.actions.append(("navigate", "user"))
        print("[Temi NAVIGATE]: user")
