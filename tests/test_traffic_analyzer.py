from src.traffic_analyzer import TrafficAnalyzer


def test_traffic_density():
    analyzer = TrafficAnalyzer(
        low_threshold=10,
        medium_threshold=25
    )

    assert analyzer.classify_density(5) == "Low"
    assert analyzer.classify_density(10) == "Low"

    assert analyzer.classify_density(15) == "Medium"
    assert analyzer.classify_density(25) == "Medium"

    assert analyzer.classify_density(30) == "High"


def test_traffic_analysis():
    analyzer = TrafficAnalyzer()

    counts = {
        "total": 20,
        "car": 12,
        "motorcycle": 5,
        "bus": 2,
        "truck": 1
    }

    result = analyzer.analyze(counts)

    assert result["total_vehicles"] == 20
    assert result["density"] == "Medium"
    assert result["cars"] == 12
    assert result["motorcycles"] == 5
    assert result["buses"] == 2
    assert result["trucks"] == 1

    print("\nTraffic Analysis:")
    print(result)