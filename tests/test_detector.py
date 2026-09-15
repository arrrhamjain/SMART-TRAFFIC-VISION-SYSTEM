import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from src.detector import VehicleDetector


PROJECT_ROOT = Path(__file__).resolve().parents[1]

INPUT_IMAGE = (
    PROJECT_ROOT
    / "data"
    / "input"
    / "traffic_test1.jpg"
)

OUTPUT_IMAGE = (
    PROJECT_ROOT
    / "data"
    / "output"
    / "detected_traffic_test1.jpg"
)


def test_vehicle_detector():
    detector = VehicleDetector()

    detections = detector.detect(INPUT_IMAGE)

    assert isinstance(detections, list)

    print(
        f"\nVehicles detected: "
        f"{len(detections)}"
    )

    for detection in detections:
        print(
            f"{detection['class_name']} - "
            f"{detection['confidence']:.2f}"
        )


def test_annotated_image():
    detector = VehicleDetector()

    output = detector.annotate_image(
        INPUT_IMAGE,
        OUTPUT_IMAGE
    )

    assert Path(output).exists()
    assert Path(output).stat().st_size > 0