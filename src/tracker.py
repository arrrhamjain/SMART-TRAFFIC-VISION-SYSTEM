class VehicleTracker:
    """Track vehicles using simple centroid-based tracking."""

    def __init__(self, max_distance=80):
        self.max_distance = max_distance
        self.next_id = 1
        self.tracks = {}

    def _centroid(self, bbox):
        x1, y1, x2, y2 = bbox

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        return center_x, center_y

    def update(self, detections):
        """
        Update vehicle tracks using detection bounding boxes.

        Args:
            detections: List of detection dictionaries.

        Returns:
            List of detections with tracking IDs.
        """
        updated_detections = []
        used_ids = set()

        for detection in detections:
            centroid = self._centroid(
                detection["bbox"]
            )

            best_id = None
            best_distance = self.max_distance

            for track_id, track in self.tracks.items():
                if track_id in used_ids:
                    continue

                previous_centroid = track["centroid"]

                distance = (
                    (centroid[0] - previous_centroid[0]) ** 2
                    + (centroid[1] - previous_centroid[1]) ** 2
                ) ** 0.5

                if distance < best_distance:
                    best_distance = distance
                    best_id = track_id

            if best_id is None:
                best_id = self.next_id
                self.next_id += 1

            self.tracks[best_id] = {
                "centroid": centroid,
                "class_name": detection["class_name"],
            }

            used_ids.add(best_id)

            tracked_detection = detection.copy()
            tracked_detection["track_id"] = best_id

            updated_detections.append(
                tracked_detection
            )

        return updated_detections