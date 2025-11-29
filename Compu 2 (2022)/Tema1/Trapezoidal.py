###################### 1)
I=1.640533 #Valor de la integral numerica
def f(x): #Definir función
    return 0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
a=0.0;b=0.8 #Valores de limites de integración

for n in range(1,17,1): #Desde donde hasta donde y cada cuanto.
    h=abs(b-a)/n #Definimos cuán pequeño queremos la base
    suma_trapezoidal=0 #Varianle vacía para después redefinir

    for k in range(1,n): #Cte de multipliación
        suma_trapezoidal+=f(a+k*h)

area=h*((f(a)+f(b))/2+suma_trapezoidal)
print(area) #Valor de integral programada
error=abs(area-I)/I*100
print(error)






####################### 2)
def f(x):  #Definir funcion
    return x**4-2*x+1

a=0.0;b=2.0;n=100;h=abs(b-a)/n
s=0.5*f(a)+0.5*f(b)
for k in range(1,n):
    s+=f(a+k*h)
print(h*s)