# -*- coding: utf-8 -*-
"""PDB Numerik.ipynb

## Persamaan Differensial Biasa Numerik
"""

import matplotlib.pyplot as plt
import pandas as pd

def dydx(x,y):
  return x + y

"""Metode Euler"""

# Kondisi awal dan stepsize
y_0 = 1
x_0 = 0
n = 7
h = 0.1

# Nilai untuk plot
x = [x_0]
y = [y_0]

# Iterasi Euler
tabel_dydx = {x_0 : y_0}
for i in range (0,n):
  x_0 += h
  y_1 = y_0 + dydx(x_0, y_0)*h
  tabel_dydx[x_0] = y_1
  x.append(x_0)
  y.append(y_1)
  y_0 = y_1

# Tabel Iterasi
tabel_euler = pd.DataFrame(tabel_dydx.items(), columns=['x', 'y'])
tabel_euler

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metode Euler')
plt.show()

"""Metode Heun"""

# Kondisi awal dan stepsize
y_0 = 1
x_0 = 0
n = 7
h = 0.1

# Nilai untuk plot
x = [x_0]
y = [y_0]

# Iterasi Heun
tabel_dydx = {x_0 : y_0}
for i in range (0,n):
  x_0 += h
  y_1 = y_0 + (h/2)*(dydx(x_0, y_0) + dydx(x_0 + h, y_0+h*dydx(x_0, y_0)))
  tabel_dydx[x_0] = y_1
  x.append(x_0)
  y.append(y_1)
  y_0 = y_1

# Tabel Iterasi
tabel_heun = pd.DataFrame(tabel_dydx.items(), columns=['x', 'y'])
tabel_heun

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metode Heun')
plt.show()

"""Metode Runge-Kutta Orde 4"""

# Kondisi awal dan stepsize
y_0 = 1
x_0 = 0
n = 7
h = 0.1

# Nilai untuk plot
x = [x_0]
y = [y_0]

# Iterasi Runge-Kutta
tabel_dydx = {x_0 : y_0}
for i in range (0,n):
  k_1 = h * dydx(x_0, y_0)
  k_2 = h * dydx(x_0 + 0.5*h, y_0 + 0.5*k_1)
  k_3 = h * dydx(x_0 + 0.5*h, y_0 + 0.5*k_2)
  k_4 = h * dydx(x_0 + h, y_0 + k_3)
  y_1 = y_0 + (k_1 + 2*k_2 + 2*k_3 + k_4)/6
  x_0 += h
  tabel_dydx[x_0] = y_1
  x.append(x_0)
  y.append(y_1)
  y_0 = y_1

# Tabel Iterasi
tabel_rungekutta = pd.DataFrame(tabel_dydx.items(), columns=['x', 'y'])
tabel_rungekutta

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metode Runge-Kutta')
plt.show()
