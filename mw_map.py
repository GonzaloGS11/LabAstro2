import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import *

filename = 'velocidades.txt'

ID, l, b, v1 = [],[],[],[]

with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        ID.append(value[0])
        l.append(value[1])
        b.append(value[2])
        v1.append(value[3])
        
Ro = 8.5
Vo = 220

CT = [(Ro * np.sin(l)) for l in zip(l)]

Vr =[(v1 + Vo*np.sin(l)) for v1, l in zip(v1,l)]
Vr2 = [(Vo*np.sin(l)*((Ro/CT)-1)) for CT, l in zip(CT,l)]

R = [(sqrt(((Ro*Vo*np.sin(l))/((Vo*np.sin(l))+ Vr ))**2)) for Vr,l in zip(Vr,l)]
R2 = [(sqrt(((Ro*Vo*np.sin(l))/((Vo*np.sin(l))+ Vr2 ))**2)) for Vr2,l in zip(Vr2,l)]

r = [(sqrt((sqrt(sqrt(((R*R) - ((Ro*Ro)*np.sin(l)*np.sin(l)))**2))+(Ro*np.cos(l)))**2)) for R, l in zip(R,l)]
#r2 = [((sqrt(R*R - Ro*Ro*np.sin(l)*np.sin(l)))+Ro*np.cos(l)) for R, l in zip(R,l)]

plt.scatter(R, Vr, s=8, marker=(5, 1))

plt.xlabel('Distancia Galactocentrica')
plt.ylabel('Velocidad rotacional')
plt.show()

x = [(R*np.cos(l-90)) for R, l in zip(R,l)]
y = [(R*np.sin(l-90)) for R, l in zip(R,l)]
plt.scatter(x, y, s=8, marker=(5, 1))

plt.show()
