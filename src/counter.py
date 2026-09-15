from collections import Counter


class VehicleCounter:
    """Count detected vehicles by category."""

    def count(self, detections):
        """
        Count vehicles from YOLO detections.

        Args:
            detections: List of vehicle detection dictionaries.

        Returns:
            Dictionary containing vehicle counts.
        """
        vehicle_types = [
            detection["class_name"]
            for detection in detections
        ]

        counts = Counter(vehicle_types)

        return {
            "total": len(vehicle_types),
            "car": counts.get("car", 0),
            "motorcycle": counts.get("motorcycle", 0),
            "bus": counts.get("bus", 0),
            "truck": counts.get("truck", 0),
        }