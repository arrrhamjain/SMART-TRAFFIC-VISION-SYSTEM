from pathlib import Path

from src.preprocessing import preprocess_image
import csv
import matplotlib.pyplot as plt
from src.detector import VehicleDetector
from src.counter import VehicleCounter
from src.traffic_analyzer import TrafficAnalyzer


PROJECT_ROOT = Path(__file__).resolve().parent

INPUT_DIR = PROJECT_ROOT / "data" / "input"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"


def process_image(image_path, detector, counter, analyzer):
    """Run the complete traffic analysis pipeline on one image."""

    print(f"\nProcessing: {image_path.name}")

    # Step 1: Preprocess image
    processed_path = OUTPUT_DIR / f"processed_{image_path.name}"

    preprocess_image(
        image_path,
        processed_path
    )

    # Step 2: Detect vehicles
    detections = detector.detect(image_path)

    print(
        f"Vehicles detected: {len(detections)}"
    )

    # Step 3: Count vehicles
    counts = counter.count(detections)

    # Step 4: Analyze traffic
    analysis = analyzer.analyze(counts)

    # Step 5: Create annotated image
    annotated_path = (
        OUTPUT_DIR
        / f"detected_{image_path.name}"
    )

    detector.annotate_image(
        image_path,
        annotated_path
    )

    # Display results
    print("Vehicle Counts:")
    print(f"  Cars: {counts['car']}")
    print(f"  Motorcycles: {counts['motorcycle']}")
    print(f"  Buses: {counts['bus']}")
    print(f"  Trucks: {counts['truck']}")
    print(f"  Total: {counts['total']}")

    print(
        f"Traffic Density: "
        f"{analysis['density']}"
    )

    print(
        f"Annotated image: "
        f"{annotated_path}"
    )

    return {
        "image": image_path.name,
        "counts": counts,
        "analysis": analysis,
        "annotated_image": str(annotated_path),
    }


def main():
    """Run the Smart Traffic Vision System."""

    print("=" * 50)
    print("SMART TRAFFIC VISION SYSTEM")
    print("=" * 50)

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    detector = VehicleDetector(
        confidence=0.40
    )

    counter = VehicleCounter()

    analyzer = TrafficAnalyzer(
        low_threshold=10,
        medium_threshold=25
    )

    image_files = sorted(
        list(INPUT_DIR.glob("*.jpg"))
        + list(INPUT_DIR.glob("*.jpeg"))
        + list(INPUT_DIR.glob("*.png"))
    )

    if not image_files:
        print(
            "\nNo images found in "
            f"{INPUT_DIR}"
        )
        return

    print(
        f"\nFound {len(image_files)} "
        "input image(s)."
    )

    results = []

    for image_path in image_files:
        result = process_image(
            image_path,
            detector,
            counter,
            analyzer
        )

        results.append(result)
        # Save analysis results to CSV
    results_dir = PROJECT_ROOT / "results"
    results_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    csv_path = results_dir / "traffic_analysis.csv"

    with open(
        csv_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Image",
            "Cars",
            "Motorcycles",
            "Buses",
            "Trucks",
            "Total",
            "Traffic Density"
        ])

        for result in results:
            counts = result["counts"]

            writer.writerow([
                result["image"],
                counts["car"],
                counts["motorcycle"],
                counts["bus"],
                counts["truck"],
                counts["total"],
                result["analysis"]["density"]
            ])

    print(
        f"\nCSV report saved to: {csv_path}"
    )
        # Create traffic summary chart
    chart_path = results_dir / "traffic_summary.png"

    image_names = []
    total_vehicles = []

    for result in results:
        image_names.append(result["image"])
        total_vehicles.append(
            result["counts"]["total"]
        )

    plt.figure(figsize=(10, 6))

    plt.bar(
        image_names,
        total_vehicles
    )

    plt.title("Vehicle Count by Traffic Image")
    plt.xlabel("Input Image")
    plt.ylabel("Total Vehicles")

    plt.xticks(
        rotation=20,
        ha="right"
    )

    plt.tight_layout()

    plt.savefig(chart_path)
    plt.close()

    print(
        f"Traffic chart saved to: {chart_path}"
    )
    print("\n" + "=" * 50)
    print("PROCESSING COMPLETE")
    print("=" * 50)

    for result in results:
        print(
            f"{result['image']} → "
            f"{result['analysis']['density']} traffic "
            f"({result['counts']['total']} vehicles)"
        )


if __name__ == "__main__":
    main()