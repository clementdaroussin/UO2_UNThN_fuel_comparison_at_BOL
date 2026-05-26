# A comparative neutronic analysis of UN-ThN vs. traditional UO₂ fuel in a quasi-infinite pin-cell lattice at beginning of life
### Project Overview
This repository contains the simulation files and analysis for a preliminary neutronic assessment of **Uranium-Thorium Nitride (UN-ThN)** fuel as a high-performance alternative to traditional **Uranium Dioxide (UO₂)** in pressurized water reactors.

* **Author:** Clément DAROUSSIN
* **Date:** May 25, 2026
* **Software:** [OpenMC 15.3.0](https://docs.openmc.org/)
* **Nuclear Data Library:** JEFF-3.3 (Continuous Energy)
* **Project Type:** Self-initiated R&D Project – Advanced Fuel Cycle Study

### Abstract
This study evaluates Beginning-of-Life (BOL) characteristics using a quasi-infinite pin-cell model with reflective boundary conditions and axial leakage (modeled via water reflectors). The analysis focuses on three primary metrics: **inherent safety, neutronic spectral evolution, and breeding potential**. 

Key findings include:
* **Reactivity:** A 9.47% reactivity penalty for UN-ThN fuel, counterbalanced by long-term breeding benefits.
* **Conversion Ratio:** A 39.97% improvement in the conversion ratio (CR).
* **Safety Feedback:** A 72.21% increase in the magnitude of the negative Doppler feedback coefficient compared to UO₂.

The results suggest that while the nitride-thorium matrix requires specific N-15 isotopic enrichment, it offers a superior pathway toward enhanced passive safety and sustainable fuel cycle management.

### Repository Structure
* `Pincell_model_UO2_UNThN_comparative_analysis.ipynb`: Main Jupyter notebook containing the analysis, post-processing, and visualization of the OpenMC tallies.
* `geometry.xml`, `materials.xml`, `settings.xml`, `tallies.xml`: OpenMC input configuration files.
* `plotting_cross_section.py`: Script for generating nuclear data plots.
* `img/`: Directory containing generated figures, including fission density heatmaps, neutron spectra, and radial power profiles.

### Key Simulation Parameters
| Parameter | Value / Detail |
| :--- | :--- |
| **Fuel Temperature** | 900K and 1200K |
| **Total Histories (N)** | 12,500,000 |
| **Energy Treatment** | Continuous |
| **Transport Mode** | K-Eigenvalue |

---

### Acknowledgments
*For detailed methodologies and conclusions, please refer to the project PDF included in this repository.*

---
*Disclaimer: This project is a self-initiated R&D study. It acknowledges the industrial and economic constraints related to N-15 enrichment and fuel cycle infrastructure compatibility, which are addressed in the "Limits of the study" section of the full report.*
