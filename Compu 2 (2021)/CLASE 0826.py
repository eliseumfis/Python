from math import exp
terms=1000;beta=1/100;S=0.0;Z=0.0
for n in range(terms):
    En=n+0.5
    weight=exp(-beta*En)
    S+=weight*En
    Z+=weight
print(S/Z)