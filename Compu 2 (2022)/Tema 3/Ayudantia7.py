import numpy as np

#1

array_x=np.array(np.linspace(0.5,1.0,50))
h=array_x[1]-array_x[0]


def f(x):
    return (x+np.sin(x)**2)**(1/3)
array_y=f(array_x)

derivadas=np.gradient(array_y,h)
#print(derivadas)
h=0.001
def g(x):
    return 5*np.exp(x)*np.sqrt(np.cos(x))
array5=np.array([5-h,5,5+h])
array5y=g(array5)
derivadaen5=np.gradient(array5y,h)[1]
print(derivadaen5)