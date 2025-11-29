import numpy as np
import pylab as plt
data = np.loadtxt("velocities.txt",float)
t = data[:,0]
v = data[:,1]
N = len(t)-1 # number of slices
a = t[0]
b = t[-1]

def trap(v,N):
    h = (b-a)/(N)
    
    weight = np.ones(N+1) # number of points is number of slices + 1
    weight[0] = 0.5
    weight[-1] = 0.5
    
    return h*sum(weight*v)

plt.title("Particle velocity (m/s) vs. time (s)")
plt.plot(t,v,color='purple')
plt.xlim(a,b)
plt.show()

area = trap(v,N)
print(f"The approximate distance travelled in the x-direction as a function of time is {round(area,2)} meters.")