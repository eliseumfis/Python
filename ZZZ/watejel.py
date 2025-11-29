import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from astropy.io import fits
from astropy.visualization import astropy_mpl_style

plt.style.use(astropy_mpl_style)
image = Image.open("Hs-2009-14-a-web.jpg")
xsize, ysize = image.size
print(f"Image size: {ysize} x {xsize}")
print(f"Image bands: {image.getbands()}")
ax = plt.imshow(image)
plt.show()
