import cmath
import numpy as np

R1 = R3 = R5 = 1e3  # 1 kW
R2 = R4 = R6 = 2e3  # 2 kW
C1 = 1e-6  # 1 μF
C2 = 0.5e-6  # 0.5 μF
x_plus = 3  # V
omega = 1000  # 1000 s^-1

# Define the complex matrix
matrix = [[1/R1 + 1/R4 + 1j*omega*C1, -1j*omega*C1, 0],
          [-1j*omega*C1, 1/R2 + 1/R5 + 1j*omega*C1 + 1j*omega*C2, -1j*omega*C2],
          [0, -1j*omega*C2, 1/R3 + 1/R6 + 1j*omega*C2]]

# Define the constant vector
vector = [x_plus/R1, x_plus/R2, x_plus/R3]

# Solve the equations
solutions = np.linalg.solve(matrix, vector)

# Calculate amplitudes and phases
amplitudes = [abs(x) for x in solutions]
phases = [cmath.phase(x) * 180 / cmath.pi for x in solutions]

# Print the results
for i in range(len(solutions)):
    print("V{} amplitude: {:.2f} V".format(i+1, amplitudes[i]))
    print("V{} phase: {:.2f} degrees".format(i+1, phases[i]))