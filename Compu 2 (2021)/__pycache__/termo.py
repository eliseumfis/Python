a=0.050
b=-1*10**(-3)
def fem(t):
    return a*t + b*t**2
temps=[-100,200,400,500]
tem=[]
for k in temps:
    tem.append(fem(k))
print(tem)