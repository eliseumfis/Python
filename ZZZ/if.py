import numpy as np
from astropy import constants as const
from astropy import units as u

Teff = 5780 * u.K
R = const.R_sun
# Now the formula:
L = 4 * np.pi * R**2 * const.sigma_sb * Teff**4
# print the result:
print(L)
