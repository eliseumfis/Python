# Importar las bibliotecas necesarias
import lightkurve as lk
import matplotlib.pyplot as plt

######################## SECTOR 5 ############################3
lc5_search = lk.search_lightcurve(
    "TYC 110-755-1", mission="TESS", author="SPOC", sector=5
)
# Descargar la curva de luz
lc5 = lc5_search.download()
# Eliminar los valores NaN
lc5 = lc5.remove_nans()
folded_lc5 = lc5.fold(period=1)


######################## SECTOR 32 ############################3
lc32_search = lk.search_lightcurve(
    "TYC 110-755-1", mission="TESS", author="SPOC", sector=32
)
# Descargar la curva de luz
lc32 = lc32_search.download()
# Eliminar los valores NaN
lc32 = lc32.remove_nans()
folded_lc32 = lc32.fold(period=1)

folded_lc5.plt.plot()
