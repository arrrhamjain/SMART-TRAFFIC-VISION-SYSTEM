import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.preprocessing import preprocess_image


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "data" / "input"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"


def test_preprocess_images():
    image_files = list(INPUT_DIR.glob("*.jpg"))

    assert len(image_files) > 0, "No JPG images found in data/input."

    for image_path in image_files:
        output_path = OUTPUT_DIR / f"processed_{image_path.name}"

        result = preprocess_image(image_path, output_path)

        assert Path(result).exists()
        assert Path(result).stat().st_size > 0