from alerce.core import Alerce
from alerce.core import Alerce

client = Alerce()
import numpy as np
import matplotlib.pyplot as plt


## Basic requirements
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import requests
import astropy.units as u
from astropy import coordinates
from astropy.time import Time
from astropy.table import Table, Column
from astropy.coordinates import Distance
from astropy.cosmology import WMAP7
from astroquery.irsa_dust import IrsaDust
from astroquery.ned import Ned
from IPython.display import HTML
from ipywidgets import Layout, Box, widgets


min_firstmjd = Time("2017-11-01T00:00:00", format="isot", scale="utc").mjd

AGNs = client.query_objects(
    classifier="lc_classifier",
    class_name="AGN",
    probability=0.9,
    ndet=[30, 200],
    order_by="probability",
    order_mode="DESC",
    first_mjd=[min_firstmjd, None],
    count=False,
    page_size=1000,
    format="pandas",
)
fig, ax = plt.subplots()
bins = np.linspace(-0.3, 1.5, 30)
ax.hist(
    AGNs.g_r_mean_corr,
    bins=bins,
    lw=2,
    histtype="step",
    color="firebrick",
    label="AGN candidates",
)
ax.set_xlabel(r"($g-r$)_mean_corr")
plt.legend()
plt.show()
