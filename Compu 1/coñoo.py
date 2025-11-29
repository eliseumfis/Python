import numpy as np

a = np.zeros([2, 2], int)

a[0, 1] = 1
a[1, 0] = -1
print(a)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], float)
x = a[1, 2] + a[2, 1]
b = a * 2


print(a[0, :] * b[0, :])
"""
#print(sum(a[:,3]))
c=np.sqrt(a)
#print(c)
x=1
valores=np.loadtxt("TMP_VALPO.dat")
#print(valores.shape)
mean=sum(valores/len(valores))
#print(mean)
tmp=valores-273.16
#print(tmp)
tmp=tmp.round(2)
#print(tmp)
mc=sum(tmp*tmp/len(tmp))





"""

from numpy import log, exp

# print(tmp/len(tmp))
# print(sum(tmp*tmp/len(tmp)))
# print(exp(sum(log(tmp)/len(log(tmp)))))
