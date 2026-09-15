class TrafficAnalyzer:
    """Analyze traffic density from vehicle counts."""

    def __init__(
        self,
        low_threshold=10,
        medium_threshold=25
    ):
        self.low_threshold = low_threshold
        self.medium_threshold = medium_threshold

    def classify_density(self, total_vehicles):
        """
        Classify traffic density based on total vehicles.

        Args:
            total_vehicles (int): Number of detected vehicles.

        Returns:
            Traffic density category.
        """
        if total_vehicles <= self.low_threshold:
            return "Low"

        if total_vehicles <= self.medium_threshold:
            return "Medium"

        return "High"

    def analyze(self, counts):
        """
        Analyze traffic using vehicle counts.

        Args:
            counts (dict): Vehicle count dictionary.

        Returns:
            Dictionary containing traffic analysis.
        """
        total = counts.get("total", 0)

        density = self.classify_density(total)

        return {
            "total_vehicles": total,
            "density": density,
            "cars": counts.get("car", 0),
            "motorcycles": counts.get("motorcycle", 0),
            "buses": counts.get("bus", 0),
            "trucks": counts.get("truck", 0),
        }