#1)
import numpy as np

t=np.arange(51);y=2*t+5;x=10*t

import pylab as pl

pl.plot(x,y)
pl.xlabel("X");pl.ylabel("Y")
pl.show()

#2)
xs=[]
xi=0;x0=5;v=3;t=np.arange(21);x=x0+v*t
for t in x:
    xs.append(t)
    t=np.arange(21)
print(np.size(xs));print(np.size(t))
pl.plot(xs,t)
pl.xlabel("Posición [m]");pl.ylabel("Tiempo [s]");pl.title("Posicion en funcion del tiempo")
pl.show()





