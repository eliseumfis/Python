import numpy as np
import matplotlib.pyplot as plt

# Define constants
E_0 = 1  # Amplitude of the electric field
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (H/m)
sigma = 1e-3  # Conductivity (S/m)
omega = 1e9  # Angular frequency (rad/s)
c = 3e8  # Speed of light (m/s)


# Define the function to plot
def E_field(x, t):
    term1 = np.sqrt(1 + np.sqrt(1 + (mu_0 * sigma * c**2 / omega) ** 2))
    term2 = (mu_0 * sigma * omega * x) / np.sqrt(2 * (1 + term1))
    exp1 = np.exp(term2)
    term3 = np.sqrt(1 + np.sqrt(1 + (mu_0 * sigma * c**2 / omega) ** 2))
    term4 = np.exp(1j * omega * x / (c * np.sqrt(0.5 * (1 + term3))) - 1j * omega * t)
    return E_0 * exp1 * term4


# Define the range of x and t
x = np.linspace(0, 1, 400)  # from 0 to 1 meter
t = 0  # At time t = 0

# Calculate the real part of the electric field
E_real = np.real(E_field(x, t))
E_im = np.imag(E_field(x, t))

# Plot the electric field
plt.figure(figsize=(10, 6))
plt.plot(x, E_im, color="orange", label="Parte imaginaria")
plt.plot(x, E_real, label="Parte real")
plt.xlabel("$x$ (m)")
plt.ylabel("$\\vec{E}(x, 0)$")
plt.title(" $\\vec{E}(x, 0)$")
plt.legend()
plt.grid(True)
plt.show()
