from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Project directories
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"
MODEL_DIR = BASE_DIR / "models"
RESULTS_DIR = BASE_DIR / "results"

# Detection settings
CONFIDENCE_THRESHOLD = 0.40
IMAGE_SIZE = 640

# Vehicle classes used by the project
VEHICLE_CLASSES = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck",
}

# Traffic density thresholds
LOW_TRAFFIC_THRESHOLD = 10
MEDIUM_TRAFFIC_THRESHOLD = 25