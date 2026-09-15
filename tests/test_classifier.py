from src.classifier import VehicleClassifier


def test_vehicle_classifier():
    classifier = VehicleClassifier()

    assert classifier.classify(0) == "car"
    assert classifier.classify(1) == "motorcycle"
    assert classifier.classify(2) == "bus"
    assert classifier.classify(3) == "truck"


def test_classify_detection():
    classifier = VehicleClassifier()

    detection = {
        "class_id": 0,
        "confidence": 0.90
    }

    result = classifier.classify_detection(detection)

    assert result["class_name"] == "car"