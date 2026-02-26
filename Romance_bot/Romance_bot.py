import matplotlib.pyplot as plt
import numpy as np

# Data for Transmission Wavelengths
wavelength_1_transmission = [623.8, 644.6, 638.0, 615.5, 628.3, 627.5, 636.2, 632.4, 622.2]
wavelength_2_transmission = [623.8, 632.4, 622.2, 615.5, 636.4, 622.2, 648.6, 644.6, 634.0]

# Corresponding Distance (r) for each data point
r_transmission = [10, 10, 10, 15, 15, 15, 20, 20, 20]  # Distances for each trial (in cm)

# Theoretical wavelength of He-Ne laser (constant value)
theoretical_wavelength = 632.8

# Create the plot for Transmission
plt.figure(figsize=(8, 6))

# Plot Trial 1 and Trial 2 wavelengths for transmission
plt.plot(r_transmission, wavelength_1_transmission, label='Trial 1', marker='o', linestyle='-', color='b')
plt.plot(r_transmission, wavelength_2_transmission, label='Trial 2', marker='x', linestyle='--', color='r')

# Plot the theoretical wavelength (horizontal line)
plt.axhline(theoretical_wavelength, color='g', linestyle='-', label='Theoretical Value (632.8 nm)')

# Adding titles and labels
plt.title('Transmission Diffraction Wavelengths')
plt.xlabel('Distance (r) in cm')
plt.ylabel('Wavelength (nm)')

# Display the legend
plt.legend()

# Enable grid for better visualization
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
