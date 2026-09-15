from src.tracker import VehicleTracker


def test_vehicle_tracker():
    tracker = VehicleTracker(max_distance=80)

    frame_1 = [
        {
            "class_name": "car",
            "bbox": [100, 100, 200, 200],
            "confidence": 0.90
        },
        {
            "class_name": "motorcycle",
            "bbox": [400, 100, 450, 180],
            "confidence": 0.85
        }
    ]

    tracked_1 = tracker.update(frame_1)

    assert len(tracked_1) == 2
    assert tracked_1[0]["track_id"] == 1
    assert tracked_1[1]["track_id"] == 2

    frame_2 = [
        {
            "class_name": "car",
            "bbox": [105, 105, 205, 205],
            "confidence": 0.91
        },
        {
            "class_name": "motorcycle",
            "bbox": [405, 105, 455, 185],
            "confidence": 0.86
        }
    ]

    tracked_2 = tracker.update(frame_2)

    assert len(tracked_2) == 2

    assert tracked_2[0]["track_id"] == 1
    assert tracked_2[1]["track_id"] == 2

    print("\nTracking results:")
    for detection in tracked_2:
        print(
            f"{detection['class_name']} "
            f"→ ID {detection['track_id']}"
        )