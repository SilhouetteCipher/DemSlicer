
# Topographic Contour Slicing Scripts

## Overview

These Python scripts are designed for processing Digital Elevation Models (DEMs) to generate topographic contour slices and their offsets, suitable for papercraft, plotting, or cutting. The scripts take a DEM file as input and output a series of SVG files representing the contour lines.

## Scripts

1. **demslice.py**: Generates basic contour slices from a DEM file.
2. **demrings.py**: Generates contour slices with additional offset lines to create "ring" effects in each slice.

## Prerequisites

- Python 3.x
- Libraries: `rasterio`, `numpy`, `matplotlib`, `shapely`
  - Install these using `pip install rasterio numpy matplotlib shapely`

## Usage

### demslice.py

- **Purpose**: Generates individual SVG files for each contour slice based on the DEM's elevation range.
- **Parameters**:
  - `dem_path`: Path to the DEM file (e.g., `"dem.tif"`).
  - `num_slices`: Number of contour slices to generate (e.g., `12`).
  - `output_directory`: Directory where SVG files will be saved (e.g., `"slices_output"`).

### demrings.py

- **Purpose**: Similar to `demslice.py` but adds an offset to each contour line, creating "ring" effects.
- **Parameters**:
  - `dem_path`: Path to the DEM file.
  - `num_slices`: Number of contour slices to generate.
  - `output_directory`: Directory for SVG output.
  - `offset_distance`: Distance for the offset lines from the original contour lines (e.g., `5`).

## Running the Scripts

1. Set the parameters at the bottom of each script according to your requirements.
2. Run the script using Python, e.g., `python3 demslice.py`.

## Notes

- The scripts are designed for DEMs in GeoTIFF format but can be adapted for other formats.
- Ensure the DEM file is in the correct location as specified in the `dem_path`.
- The output SVG files can be used for various applications including papercraft, laser cutting, and educational purposes.
