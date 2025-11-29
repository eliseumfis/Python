from matplotlib.pyplot import legend
import pylab as pl
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)
pl.plot(x,y,'--k',label='func.seno')
pl.legend()
pl.grid()
pl.xlabel='Puntos en X'
pl.ylabel='Sin(x)'
pl.show()