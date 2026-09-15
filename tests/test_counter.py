from src.counter import VehicleCounter


def test_vehicle_counter():
    detections = [
        {"class_name": "car"},
        {"class_name": "car"},
        {"class_name": "motorcycle"},
        {"class_name": "bus"},
        {"class_name": "truck"},
    ]

    counter = VehicleCounter()

    counts = counter.count(detections)

    assert counts["total"] == 5
    assert counts["car"] == 2
    assert counts["motorcycle"] == 1
    assert counts["bus"] == 1
    assert counts["truck"] == 1

    print("\nVehicle Counts:")
    print(counts)