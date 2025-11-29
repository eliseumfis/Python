from astropy import units as u
import lightkurve as lk
import matplotlib.pyplot as plt

search_result = lk.search_targetpixelfile(
    "TYC 110-755-1", author="TESS", quarter=4, cadence="long"
)
tpf = search_result.download()

plt.plot(tpf, column="flux")
plt.show()
