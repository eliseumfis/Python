import numpy as np
import lightkurve as lk
import matplotlib.pyplot as plt

tpf_file = lk.search_targetpixelfile("TIC 307210830", mission="TESS", sector=5)
tppf_file = tpf_file.download()
