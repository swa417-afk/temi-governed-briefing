from temi_autonomy.main_node import GovernedPipeline


def test_temporal_and_threshold_behavior():
    pipeline = GovernedPipeline()

    # Requires temporal_frames=2, so first pass should be NO_ACTION.
    event1 = pipeline.run_cycle({"event_type": "OFFER_ASSISTANCE", "confidence": 0.8})
    assert event1.event_type == "NO_ACTION"

    event2 = pipeline.run_cycle({"event_type": "OFFER_ASSISTANCE", "confidence": 0.8})
    assert event2.event_type == "OFFER_ASSISTANCE"

    low = pipeline.run_cycle({"event_type": "NAVIGATE_TO_PERSON", "confidence": 0.4})
    assert low.event_type == "NO_ACTION"


def test_high_priority_suppression():
    pipeline = GovernedPipeline()

    # Stabilize OFFER_ASSISTANCE once
    pipeline.run_cycle({"event_type": "OFFER_ASSISTANCE", "confidence": 0.8})
    assist = pipeline.run_cycle({"event_type": "OFFER_ASSISTANCE", "confidence": 0.8})
    assert assist.event_type == "OFFER_ASSISTANCE"

    # Hazard needs two frames too.
    first = pipeline.run_cycle({"event_type": "ALERT_HAZARD", "confidence": 0.9})
    assert first.event_type == "NO_ACTION"

    second = pipeline.run_cycle({"event_type": "ALERT_HAZARD", "confidence": 0.9})
    assert second.event_type == "ALERT_HAZARD"
