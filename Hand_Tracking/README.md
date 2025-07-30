# Hand Tracking

## Description
This project uses MediaPipe Hands with OpenCV to detect and track hand landmarks in real-time through a webcam feed. It provides foundational hand landmark detection and utility functions to simplify building hand-based computer vision applications.

## Files Overview
- `handtrackingMin.py`: Minimal example demonstrating raw hand landmark detection and drawing using MediaPipe and OpenCV.
- `Handtrackingmodule.py`: Custom module wrapping MediaPipe Hands to provide easy-to-use functions for hand detection and landmark extraction.
- `handtracking_example_project.py`: Example script showing how to use `Handtrackingmodule.py` for hand tracking with FPS display and landmark visualization.

## Features
- Real-time hand landmark detection
- Drawing landmarks and connections on the hand
- Frames per second (FPS) display for performance monitoring
- Modular design with reusable hand tracking module
