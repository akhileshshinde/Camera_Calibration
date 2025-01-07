# Stereo Camera Calibration Using Oak-D Pro

This repository contains two Python scripts:  
1. **`cali.py`**: Captures stereo images using the Oak-D Pro camera.  
2. **`calibration.py`**: Calibrates the stereo camera and computes essential matrices for applications like depth estimation and 3D reconstruction.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Step-by-Step Guide](#step-by-step-guide)
  - [1. Capturing Images](#1-capturing-images)
  - [2. Stereo Camera Calibration](#2-stereo-camera-calibration)
- [Outputs](#outputs)
- [FAQs](#faqs)
- [Acknowledgments](#acknowledgments)

## Overview
Stereo camera calibration is essential for depth estimation and 3D reconstruction. This project provides a simple pipeline for:
1. Capturing stereo images.
2. Calibrating the stereo camera using a checkerboard pattern.
3. Generating intrinsic and extrinsic matrices for 3D applications.

## Requirements
- Python 3.7 or higher
- [DepthAI](https://docs.luxonis.com/projects/api/en/latest/) (for Oak-D Pro)
- OpenCV
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install opencv-python numpy matplotlib depthai
```

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/akhileshshinde/stereo-camera-calibration.git
   cd stereo-camera-calibration
   ```
2. Ensure your Oak-D Pro camera is connected to your system.

## Step-by-Step Guide

### 1. Capturing Images
Run `cali.py` to capture images using the Oak-D Pro stereo camera.

#### Instructions:
1. Place a 14x10 checkerboard in the camera's field of view.
2. Run the script:
   ```bash
   python cali.py
   ```
3. Use the following keys:
   - Press **`c`** to capture a stereo image pair.
   - Press **`q`** to quit.

Captured images are saved in:
- `images/left/` (left camera)
- `images/right/` (right camera)

### 2. Stereo Camera Calibration
Run `calibration.py` to calibrate the stereo camera.

#### Instructions:
1. Ensure `images/left` and `images/right` contain the captured stereo images.
2. Run the script:
   ```bash
   python calibration.py
   ```
3. The script will:
   - Detect checkerboard corners.
   - Compute intrinsic and extrinsic parameters.
   - Perform stereo rectification.
   - Save calibration data to `stereo_calibration.pkl`.

## Outputs
- **Intrinsic Parameters**: Camera matrices and distortion coefficients for both cameras.
- **Extrinsic Parameters**: Rotation and translation matrices.
- **Disparity-to-Depth Matrix (Q)**: For depth estimation.
- **Visualization**:
  - Original and undistorted images.
  - Rectified images with epipolar lines.

## FAQs

### Q: What checkerboard should I use?
A: A 14x10 checkerboard with square sizes specified in `calibration.py` (default: 20 mm).

### Q: How do I validate the calibration?
A: Check the alignment of rectified images and consistency of epipolar lines.

### Q: Can I use a different stereo camera?
A: Yes, modify `cali.py` to match your camera's SDK.

## Acknowledgments
- [OpenCV Documentation](https://docs.opencv.org/master/)
- [Luxonis DepthAI SDK](https://docs.luxonis.com/projects/api/en/latest/)

---
