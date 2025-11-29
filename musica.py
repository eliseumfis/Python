import numpy as np
import matplotlib.pyplot as plt

# Configuración de la señal original
fs = 44100  # Frecuencia de muestreo
t = np.linspace(0, 0.05, int(0.05 * fs), endpoint=False)  # 50 ms de duración
f = 440  # Frecuencia de la señal (La4)
V_in = 0.5 * np.sin(2 * np.pi * f * t)  # Señal de entrada

# Efecto de Distorsión
V_c = 0.3
V_dist = np.clip(V_in, -V_c, V_c)

# Efecto de Chorus
tau_0 = 0.002
delta_tau = 0.001
omega_m = 2 * np.pi * 1.5
tau_chorus = tau_0 + delta_tau * np.sin(omega_m * t)
V_chorus = V_in + np.roll(V_in, int(fs * tau_0))  # Aproximación simple

# Efecto de Flanger
tau_flanger = int(0.001 * fs)
V_flanger = V_in + np.roll(V_in, tau_flanger)

# Efecto de Delay
tau_delay = int(0.03 * fs)
alpha = 0.5
V_delay = V_in + alpha * np.roll(V_in, tau_delay)

# Efecto de Reverb
num_echoes = 10
tau_reverb = int(0.005 * fs)
alpha_reverb = 0.5
V_reverb = V_in.copy()
for n in range(1, num_echoes + 1):
    V_reverb += (alpha_reverb**n) * np.roll(V_in, n * tau_reverb)

# Gráficos
fig, axs = plt.subplots(5, 1, figsize=(10, 15))
fig.suptitle("Efectos de Pedales de Guitarra", fontsize=16)

# Señal Original
axs[0].plot(t, V_in, label="Señal Original")
axs[0].legend()
axs[0].set_title("Señal Original")

# Efecto de Distorsión
axs[1].plot(t, V_dist, label="Distorsión", color="orange")
axs[1].legend()
axs[1].set_title("Efecto de Distorsión")

# Efecto de Chorus
axs[2].plot(t, V_chorus, label="Chorus", color="green")
axs[2].legend()
axs[2].set_title("Efecto de Chorus")

# Efecto de Flanger
axs[3].plot(t, V_flanger, label="Flanger", color="red")
axs[3].legend()
axs[3].set_title("Efecto de Flanger")

# Efecto de Delay
axs[4].plot(t, V_delay, label="Delay", color="purple")
axs[4].legend()
axs[4].set_title("Efecto de Delay")

# Efecto de Reverb (nuevo gráfico debido a la longitud)
plt.figure(figsize=(10, 5))
plt.plot(t, V_reverb, label="Reverb", color="blue")
plt.legend()
plt.title("Efecto de Reverb")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

# Ajuste de las etiquetas y leyendas
for ax in axs:
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Amplitud")
    ax.grid(True)

plt.tight_layout()
plt.show()
