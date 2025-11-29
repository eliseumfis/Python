import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

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
    exp1 = np.exp(-term2)  # Adjusted for attenuation
    term3 = np.sqrt(1 + np.sqrt(1 + (mu_0 * sigma * c**2 / omega) ** 2))
    term4 = np.exp(1j * omega * x / (c * np.sqrt(0.5 * (1 + term3))) - 1j * omega * t)
    return E_0 * exp1 * term4


# Define the range of x and t
x = np.linspace(0, 1, 400)  # from 0 to 1 meter
t_values = np.linspace(0, 1e-8, 200)  # from 0 to 1e-8 seconds
X, T = np.meshgrid(x, t_values)

# Calculate the real part of the electric field for the entire surface
E_real = np.real(E_field(X, T))

# Initialize the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("$x$ (m)")
ax.set_ylabel("$t$ (s)")
ax.set_zlabel("$\\vec{E}(x, t)$")

# Plot initial surface
surf = ax.plot_surface(X, T, E_real, cmap="viridis")


# Define the update function for animation
def update(frame):
    ax.clear()  # Clear the current plot
    ax.set_xlabel("$x$ (m)")
    ax.set_ylabel("$t$ (s)")
    ax.set_zlabel("$\\vec{E}(x, t)$")
    ax.set_title("Electric Field $\\vec{E}(x, t)$")
    surf = ax.plot_surface(X, T, np.real(E_field(X, T + frame * 1e-10)), cmap="viridis")
    return (surf,)


# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(0, 200), interval=50, blit=False
)

# Display the animation
plt.show()
