import openmc.data
import numpy as np
from scipy.signal import find_peaks
import os
import matplotlib.pyplot as plt

# 1. Path to data
os.environ["OPENMC_CROSS_SECTIONS"] = "/home/darou/openmc/nuclear_datas/jeff-3.3-hdf5/cross_sections.xml"
library = openmc.data.DataLibrary.from_xml(os.environ["OPENMC_CROSS_SECTIONS"])
th232_path = library.get_by_material('U238')['path']
th232 = openmc.data.IncidentNeutron.from_hdf5(th232_path)

# 2. Extract energy and cross-section
# The energy grid is defined at the IncidentNeutron level
energy = th232.energy['294K']

# Access the reaction and get the cross section function for 294K
capture = th232[102]
xs = capture.xs['294K'](energy)

# 3. Find all local peaks with a height threshold to ignore noise
peaks, _ = find_peaks(xs, height=50)
peak_energies = energy[peaks]

# 4. Filter to find the 4 target values
target_resonances = [21.8, 23.5, 59.5, 69.2]
extracted_peaks = []

for target in target_resonances:
    # Find the peak energy closest to the target
    closest_idx = (np.abs(peak_energies - target)).argmin()
    found_energy = peak_energies[closest_idx]
    
    # Verify it is within a reasonable tolerance (0.5 eV)
    if abs(found_energy - target) < 0.5:
        extracted_peaks.append(found_energy)

# 5. Output the results
print("Extracted resonance energies:")
for val in extracted_peaks:
    print(f"Peak detected at: {val:.2f} eV")

# Specify the path to your cross_sections.xml file
os.environ["OPENMC_CROSS_SECTIONS"] = "/home/darou/openmc/nuclear_datas/jeff-3.3-hdf5/cross_sections.xml"

# Generate the plot
fig = openmc.plot_xs({'Th232': ['capture']}, energy_axis_units='eV')
ax = fig.gca()

# List of resonance energies
resonances = extracted_peaks  # Use the extracted peaks from the previous step

# Add vertical lines and labels
for i, res in enumerate(resonances):
    # Add vertical line
    ax.axvline(x=res, color='red', linestyle='--', alpha=0.6)
    
    # Alternating logic:
    # i=0 (left), i=1 (right), i=2 (left), i=3 (right)
    if i % 2 == 0:
        # Place to the left
        ha = 'right'
        x_pos = res * 0.95 
    else:
        # Place to the right
        ha = 'left'
        x_pos = res * 1.05
    
    # Add text label
    ax.text(round(x_pos, 2), 10, f'{res} eV', 
            rotation=90, 
            verticalalignment='bottom', 
            horizontalalignment=ha, 
            color='red', fontsize=9)

# Graph adjustments
# Use set_title() instead of title()
ax.set_title('Th-232 Resonant Capture Cross Section (JEFF-3.3/Th232.h5)')
ax.set_xlim(15, 80)
ax.set_ylim(0.03, 4000)
ax.set_yscale('log')
ax.grid(True, which="both", ls="-", alpha=0.3)

# Save and show
plt.savefig('res/Th232_cross_section_with_resonances.png', dpi=300)
plt.show()
