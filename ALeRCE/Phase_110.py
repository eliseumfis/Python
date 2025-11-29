import numpy as np
import lightkurve as lk
from astropy.timeseries import LombScargle
import matplotlib.pyplot as plt

# Descargar las curvas de luz del sector 5 y 32
lcfs_sector5 = lk.search_lightcurve(
    "TYC 110-755-1", mission="TESS", author="SPOC", sector=5
).download_all(flux_column="pdcsap_flux")
lcfs_sector32 = lk.search_lightcurve(
    "TYC 110-755-1", mission="TESS", author="SPOC", sector=32
).download_all(flux_column="pdcsap_flux")

# Combinar las curvas de luz y eliminar los valores nulos y atípicos
lc = lcfs_sector5.stitch().remove_outliers(sigma=10)
lc32 = lcfs_sector32.stitch().remove_outliers(sigma=10)

# Obtener los valores de tiempo para cada sector
time_values = lc.time.value
time_values32 = lc32.time.value

# Calcular el período dominante utilizando el método de Lomb-Scargle para cada sector
frequency, power = LombScargle(time_values, lc.flux).autopower()
period = 1 / frequency[np.argmax(power)]

frequency32, power32 = LombScargle(time_values32, lc32.flux).autopower()
period32 = 1 / frequency32[np.argmax(power32)]

# Calcular la fase de la señal para cada sector
phase = (time_values / period) % 3
phase32 = (time_values32 / period32) % 3  # Ajuste para el segundo ciclo

# Normalizar el flujo para cada sector
flux = lc.flux / np.mean(lc.flux)
flux32 = lc32.flux / np.mean(lc32.flux)

# Plotear
plt.figure(figsize=(10, 6))

plt.scatter(phase32, flux32, marker=".", color="silver", label="Sector 32", s=10)
plt.scatter(phase, flux, marker=".", color="black", label="Sector 5", s=10)

plt.xlabel("Fase de la señal fotométrica")
plt.ylabel("Flujo normalizado")
plt.title("Fase de la señal fotométrica vs Flujo normalizado (Período=0.87 días)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
