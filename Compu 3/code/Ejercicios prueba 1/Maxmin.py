import numpy as np
from scipy.optimize import fmin
def f(x):
    return -(-x**2 + 4*x -2)
fumax=fmin(f,1)
print(fumax)