# Exoplanet Transit Detection via 1D Convolutional Neural Networks

## Overview
This computational astrophysics project simulates synthetic exoplanet transit light curves and trains a deep learning model to autonomously identify planetary signatures hidden in stellar flux data.

## Architecture
The pipeline is divided into two distinct computational domains:
1. **Physics Engine (Fortran):** A high-performance numerical generator that models Keplerian orbital mechanics and stellar flux dips. It outputs thousands of synthetic time-series light curves.
2. **AI Classifier (PyTorch):** A 1D Convolutional Neural Network (CNN) designed to process sequential time-series data. It learns spatial hierarchies in the 1D data to distinguish genuine U-shaped transit dips from background stellar noise.

## Tech Stack
* **Numerical Simulation:** Fortran (gfortran)
* **Deep Learning:** Python, PyTorch, NumPy
* **Visualization:** Matplotlib

## Results
The model successfully converges, minimizing Binary Cross Entropy (BCE) loss across 10 epochs. The network demonstrates the capability of replacing manual light-curve inspection with automated, high-throughput AI screening.
