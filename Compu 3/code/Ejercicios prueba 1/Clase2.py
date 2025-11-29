from numpy import *
A=array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
print(A)
v=array([-4,3,9,7],float)
def gauss_pivot(A,v):
    N=len(v)
    #Partial pivotinh
    maxi=abs(A[:,0]).argmax()
    if maxi>0:
        #Matrix
        AA=A.copy
        rowmax=AA[maxi,:]
        row0=AA[0,:]
        A[maxi,:]=row0
        A[0,:]=rowmax

        #vector v
        vv=v.copy()
        rowmax=vv[maxi]
        row0=vv[0]
        v[maxi]=row0
        v[0]=rowmax
    #eliminacion gaussiana
    for m in range(N):
        div=A[m,m]
        A[m,:]/=div
        

