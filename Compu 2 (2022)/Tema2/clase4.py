"""
import numpy as np
import matplotlib.pyplot as plt

# Interpolacion lineal

x = np.linspace(0, 2*np.pi, 10); y = np.sin(x)
xvals = np.linspace(0, 2*np.pi, 50);
yinterp = np.interp(xvals, x, y)
plt.clf();plt.plot(x,y,"o"); plt.plot(xvals,yinterp, "-b")
plt.xlabel("x"); plt.ylabel("Sin(x)")
#plt.axhline(y=0, xmin=0, xmax=2*np.pi, color="k")
#plt.show()
"""
#########################

### Interplaci ́on spline lineal y c ́ubico ####
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)
y = np.cos(-x**2/9.0); xnew = np.linspace(0, 10, 41)
f = interp1d(x, y)
f2 = interp1d(x, y, kind="cubic")
plt.plot(x, y, "o", xnew, f(xnew), "-", xnew, f2(xnew), "--")
plt.legend(["data", "linear", "cubic"], loc="best")
#plt.show()