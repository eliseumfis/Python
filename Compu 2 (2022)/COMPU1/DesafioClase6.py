#Un ladrillo cae desde el techo de una casa, cuya inclinación es θ = 45 , con una rapidez
#inicial de 10 (m/s). La altura del techo de la casa es h = 9.3 (m) .

#I. Calcule el tiempo que demora el ladrillo en llegar al suelo,
#II. Calcule la distancia horizontal que recorre el ladrillo,
#III. Con los mismos datos iniciales, ¿cuál debería ser el ángulo de inclinación del techo
#para que la distancia horizontal que alcanza el ladrillo al llegar al piso sea de x = 2.1 m?
#IV. Grafique el recorrido del ladrillo hasta que cae al suelo.

#I.
from numpy import *
theta = 45*pi/180

r = [0,9.3]
rf = [2.1,0]
v = [10*cos(theta),-10*sin(theta)]
g = [0,-9.81]

t1 = (v[1]+sqrt(v[1]**2-4*0.5*g[1]*r[1]))/(-g[1])
print(t1)

x = v[0]*t1
print(x)

a=range(-1,1)


for n in a:
    b=arccos(n)
    if b==1.31607:
        break
print("El angulo para que caiga 2.1 horizonatalmente es:",b)
v[0]=10*cos(b)
