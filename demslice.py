import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

def load_dem(dem_path):
    with rasterio.open(dem_path) as dem:
        elevation = dem.read(1)  # Reading the first band
    return elevation

def add_border(elevation_data, border_width, border_value):
    height, width = elevation_data.shape
    new_height, new_width = height + 2 * border_width, width + 2 * border_width
    bordered_data = np.full((new_height, new_width), border_value)
    bordered_data[border_width:-border_width, border_width:-border_width] = elevation_data
    return bordered_data

def generate_contours_and_save(elevation_data, num_slices, output_dir, border_width=10, border_value=0):
    elevation_data = add_border(elevation_data, border_width, border_value)

    min_elev = np.nanmin(elevation_data)
    max_elev = np.nanmax(elevation_data)

    if np.isnan(min_elev) or np.isnan(max_elev) or min_elev == max_elev:
        print("Invalid elevation range in DEM.")
        return

    slice_interval = (max_elev - min_elev) / num_slices

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_slices):
        slice_elevation = min_elev + i * slice_interval

        plt.figure()
        CS = plt.contour(elevation_data, levels=[slice_elevation], colors='black', linestyles='solid')
        plt.axis('off')
        output_filename = os.path.join(output_dir, f"slice_{i+1}.svg")
        plt.savefig(output_filename, format='svg', bbox_inches='tight', pad_inches=0)
        plt.close()

        print(f"Saved slice {i+1} to {output_filename}")

# Path to your DEM file
dem_path = "dem.tif"

# Load DEM
elevation_data = load_dem(dem_path)

# Generate Contours and Save as SVG
num_slices = 12
output_directory = "slices_output"
generate_contours_and_save(elevation_data, num_slices, output_directory)
