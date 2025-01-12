import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0  # Length of the rod (meters)
Nx = 50  # Number of spatial points
dx = L / (Nx - 1)  # Spatial step
alpha = 0.01  # Thermal diffusivity (m^2/s)
dt = 0.0005  # Time step (seconds)
Nt = 500  # Number of time steps

# Initial temperature distribution
T = np.zeros(Nx)
T[Nx//2 - 5:Nx//2 + 5] = 100  # Heat pulse in the center of the rod

# Precompute constant
C = alpha * dt / dx**2

# Ensure stability condition
if C > 0.5:
    raise ValueError("Stability condition violated! Reduce dt or increase dx.")

# Simulation
T_history = [T.copy()]
for _ in range(Nt):
    T_new = T.copy()
    for i in range(1, Nx - 1):
        T_new[i] = T[i] + C * (T[i+1] - 2*T[i] + T[i-1])
    T = T_new
    T_history.append(T.copy())

# Plot the results
x = np.linspace(0, L, Nx)
for i in range(0, Nt, Nt // 10):  # Plot every 10% of the simulation
    plt.plot(x, T_history[i], label=f"t={i*dt:.2f}s")

plt.xlabel("Position along the rod (m)")
plt.ylabel("Temperature (°C)")
plt.title("Heat Diffusion in a Rod")
plt.legend()
plt.grid()
plt.show()
