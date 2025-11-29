import numpy as np
#DFT (discreta)

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c
#cc = dft(y)

#plt.close('all')
#plt.plot(abs(c))
#plt.ylabel(r'Abs ($c_k$)')
#plt.xlabel('Múltiplos de frecuencia')
#plt.xlim(0, 500)


# Define the inverse DFT
def idft(c):
    N = 2*(len(c) - 1)
    yn = np.zeros(N, complex)
    for n in range(N):
        for k in range(N//2+1):  #
            yn[n] += c[k]*np.exp(2j*np.pi*k*n/N)/(N//2+1)
    return yn

#yn = idft(cc)

#plt.clf()
#plt.plot(xx, y, '-b', xx, yn, '-r')
#plt.hlines(0, -np.pi, np.pi, color='k', linewidth=2)
#plt.ylabel('f(x)'); plt.xlabel('X')
#plt.legend(('f(x)', 'IDFT'), loc=1)