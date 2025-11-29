import numpy as np
import lightkurve as lk
from astropy.timeseries import LombScargle
import matplotlib.pyplot as plt

# Descargar las curvas de luz para TYC 3858-1215-1 en los sectores 15, 16, 22 y 23
lcfs_sector15 = lk.search_lightcurve(
    "TYC 3858-1215-1", mission="TESS", author="SPOC", sector=15
).download_all(flux_column="pdcsap_flux")
lcfs_sector16 = lk.search_lightcurve(
    "TYC 3858-1215-1", mission="TESS", author="SPOC", sector=16
).download_all(flux_column="pdcsap_flux")
lcfs_sector22 = lk.search_lightcurve(
    "TYC 3858-1215-1", mission="TESS", author="SPOC", sector=22
).download_all(flux_column="pdcsap_flux")
lcfs_sector23 = lk.search_lightcurve(
    "TYC 3858-1215-1", mission="TESS", author="SPOC", sector=23
).download_all(flux_column="pdcsap_flux")

# Combinar las curvas de luz y eliminar los valores nulos y atípicos
lc15 = lcfs_sector15.stitch().remove_nans().remove_outliers(sigma=10)
lc16 = lcfs_sector16.stitch().remove_nans().remove_outliers(sigma=10)
lc22 = lcfs_sector22.stitch().remove_nans().remove_outliers(sigma=10)
lc23 = lcfs_sector23.stitch().remove_nans().remove_outliers(sigma=10)

# Obtener los valores de tiempo para cada sector
time_values15 = lc15.time.value
time_values16 = lc16.time.value
time_values22 = lc22.time.value
time_values23 = lc23.time.value

# Calcular el período dominante utilizando el método de Lomb-Scargle para cada sector
frequency15, power15 = LombScargle(time_values15, lc15.flux).autopower()
period15 = 1 / frequency15[np.argmax(power15)]

frequency16, power16 = LombScargle(time_values16, lc16.flux).autopower()
period16 = 1 / frequency16[np.argmax(power16)]

frequency22, power22 = LombScargle(time_values22, lc22.flux).autopower()
period22 = 1 / frequency22[np.argmax(power22)]

frequency23, power23 = LombScargle(time_values23, lc23.flux).autopower()
period23 = 1 / frequency23[np.argmax(power23)]

# Calcular la fase de la señal para cada sector
phase15 = (time_values15 / period15) % 1
phase16 = (time_values16 / period16) % 1
phase22 = (time_values22 / period22) % 1
phase23 = (time_values23 / period23) % 1

# Normalizar el flujo para cada sector
flux15 = lc15.flux / np.mean(lc15.flux)
flux16 = lc16.flux / np.mean(lc16.flux)
flux22 = lc22.flux / np.mean(lc22.flux)
flux23 = lc23.flux / np.mean(lc23.flux)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))  # Cambio en el número de filas

# Ajustar la escala del eje x para agregar dos ciclos adicionales
phase15_extended = np.concatenate([phase15, phase15 + 1, phase15 + 2])
phase16_extended = np.concatenate([phase16, phase16 + 1, phase16 + 2])

# Primer subgráfico
ax1.scatter(
    phase15_extended,
    np.tile(flux15, 3),
    marker=".",
    color="black",
    label="Sector 15",
    s=10,
)
ax1.scatter(
    phase16_extended,
    np.tile(flux16, 3),
    marker=".",
    color="silver",
    label="Sector 16",
    s=10,
)
ax1.grid()
ax1.set_xlabel("Fase de la señal fotométrica")
ax1.set_ylabel("Flujo normalizado")
ax1.legend()

# Ajustar la escala del eje x para agregar dos ciclos adicionales
phase22_extended = np.concatenate([phase22, phase22 + 1, phase22 + 2])
phase23_extended = np.concatenate([phase23, phase23 + 1, phase23 + 2])

# Segundo subgráfico

ax2.scatter(
    phase23_extended,
    np.tile(flux23, 3),
    marker=".",
    color="black",
    label="Sector 23",
    s=10,
)
ax2.scatter(
    phase22_extended,
    np.tile(flux22, 3),
    marker=".",
    color="silver",
    label="Sector 22",
    s=10,
)
ax2.grid()
ax2.set_xlabel("Fase de la señal fotométrica")
ax2.set_ylabel("Flujo normalizado")
plt.legend()
plt.tight_layout()
plt.show()
