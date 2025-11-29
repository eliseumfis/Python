import numpy as np

def f(x):
    return 2*x**4 - 3*x**3 + x**2 + 3*x + 1
h=0.5
x=np.arange(1,5+h,h)
y=f(x)
d1=[]


d1=[]
for k in x:
    array_x=np.array([k-h,k,k+h])
    array_y=f(array_x)
    derivada=np.gradient(array_y,h)[1]
    d1.append(derivada) 
print(d1)

d2=[]
for k in d1:
    array_y=np.array([k-h,k,k+h])
    derivada=np.gradient(array_y,h)[1]
    d2.append(derivada) 
print(d2)

"""
d1 = [] ; d2 = []

for i in x:
    d1.append((f(i + h) - f(i - h)) / (2 * h))              #Primera derivada
    d2.append( (f(i + h) - 2 * f(i) + f(i - h)) / (h ** 2) )                #Segunda derivada
print(d2)
"""