from pathlib import Path

import cv2
from ultralytics import YOLO


class VehicleDetector:
    """Detect vehicles in images using a YOLO model."""

    def __init__(self, model_name="yolo11n.pt", confidence=0.40):
        self.model = YOLO(model_name)
        self.confidence = confidence

        self.vehicle_classes = {
            2: "car",
            3: "motorcycle",
            5: "bus",
            7: "truck",
        }

    def detect(self, image_path):
        """
        Detect vehicles in an image.

        Returns:
            List of vehicle detections.
        """
        image_path = Path(image_path)

        if not image_path.exists():
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        results = self.model.predict(
            source=str(image_path),
            conf=self.confidence,
            verbose=False
        )

        detections = []

        for result in results:
            if result.boxes is None:
                continue

            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                if class_id not in self.vehicle_classes:
                    continue

                coordinates = box.xyxy[0].tolist()

                detections.append({
                    "class_id": class_id,
                    "class_name": self.vehicle_classes[class_id],
                    "confidence": confidence,
                    "bbox": coordinates,
                })

        return detections

    def annotate_image(self, image_path, output_path):
        """
        Detect vehicles and save an annotated image
        containing bounding boxes and labels.
        """
        image_path = Path(image_path)
        output_path = Path(output_path)

        image = cv2.imread(str(image_path))

        if image is None:
            raise ValueError(
                f"Unable to read image: {image_path}"
            )

        detections = self.detect(image_path)

        for detection in detections:
            x1, y1, x2, y2 = map(
                int,
                detection["bbox"]
            )

            label = (
                f"{detection['class_name']} "
                f"{detection['confidence']:.2f}"
            )

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        cv2.imwrite(
            str(output_path),
            image
        )

        return str(output_path)