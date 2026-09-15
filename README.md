# Smart Traffic Vision System

## Overview

Smart Traffic Vision System is a computer vision-based application that analyzes traffic images and detects vehicles automatically. The system processes input traffic images, detects vehicles, classifies them into different categories, counts the vehicles, tracks detected vehicles, and analyzes the overall traffic density.

The system provides annotated output images and a CSV report containing the traffic analysis results.

## Features

- Traffic image preprocessing
- Vehicle detection using YOLO
- Vehicle classification
- Vehicle counting
- Vehicle tracking
- Traffic density analysis
- Annotated traffic images
- CSV-based traffic analysis report
- Traffic summary visualization
- Automated testing using pytest

## Vehicle Categories

The system identifies the following vehicle categories:

- Cars
- Motorcycles
- Buses
- Trucks

## Project Structure

```text
SMART-TRAFFIC-VISION-SYSTEM/
│
├── data/
│   ├── input/
│   │   ├── traffic_test1.jpg
│   │   ├── traffic_test2.jpg
│   │   ├── traffic_test3.jpg
│   │   └── traffic_test4.jpg
│   │
│   └── output/
│       ├── processed traffic images
│       └── detected traffic images
│
├── diagrams/
│
├── models/
│
├── results/
│   ├── traffic_analysis.csv
│   └── traffic_summary.png
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── detector.py
│   ├── classifier.py
│   ├── counter.py
│   ├── tracker.py
│   ├── traffic_analyzer.py
│   └── utils.py
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_detector.py
│   ├── test_classifier.py
│   ├── test_counter.py
│   ├── test_tracker.py
│   └── test_traffic_analyzer.py
│
├── config.py
├── main.py
├── requirements.txt
└── README.md

## System Architecture

The architecture of the Smart Traffic Vision System is shown below:

![System Architecture](diagrams/architecture.png)

## Project Workflow

The workflow of the Smart Traffic Vision System is shown below:

![Project Workflow](diagrams/workflow.png)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/arrrhamjain/SMART-TRAFFIC-VISION-SYSTEM.git
cd SMART-TRAFFIC-VISION-SYSTEM