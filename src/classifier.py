class VehicleClassifier:
    """
    Classifies detected vehicles into standard traffic categories.
    """

    VEHICLE_CLASSES = {
        0: "car",
        1: "motorcycle",
        2: "bus",
        3: "truck"
    }

    def classify(self, class_id):
        """
        Convert a numerical vehicle class ID into a readable class name.
        """
        return self.VEHICLE_CLASSES.get(class_id, "unknown")

    def classify_detection(self, detection):
        """
        Add a readable class name to a detection dictionary.
        """
        if "class_id" in detection:
            detection["class_name"] = self.classify(detection["class_id"])

        return detection