# -*- coding: utf-8 -*-
"""Turunan & Integral Numerik.ipynb

Definisikan Fungsi dan titik x yang ingin dicari
"""

def function(x):
  return 5*x**4 - 2*x**3 + 7*x + 3
x = 1.5

"""## Turunan Numerik

Turunan Pertama
"""

h = 0.01

def f1f(f, x, h):
  return (f(x + h) - f(x)) / h
def f1b(f, x, h):
  return (f(x) - f(x - h)) / h
def f1c(f, x, h):
  return (f(x + h) - f(x - h)) / (2*h)

d1f = f1f(function, x, h)
print(f"turunan secara maju dari f di x = {x} adalah {d1f}")

d1b = f1b(function, x, h)
print(f"turunan secara maju dari f di x = {x} adalah {d1b}")

d1c = f1c(function, x, h)
print(f"turunan secara maju dari f di x = {x} adalah {d1c}")

"""Turunan Kedua"""

def f2f(f, x, h):
  return (f(x + 2*h) - 2*f(x + h) + f(x)) / (h**2)
def f2b(f, x, h):
  return (f(x) - 2*f(x - h) + f(x - 2*h)) / (h**2)
def f2c(f, x, h):
  return (f(x + h) - 2*f(x) + f(x - h)) / (2*h**2)

d2f = f2f(function, x, h)
print(f"turunan ke dua secara maju dari f di x = {x} adalah {d2f}")

d2b = f2f(function, x, h)
print(f"turunan ke dua secara mundur dari f di x = {x} adalah {d2b}")

d2c = f2f(function, x, h)
print(f"turunan ke dua secara pusat dari f di x = {x} adalah {d2c}")

"""Turunan ketiga"""

def f3f(f, x, h):
  return (f(x + 3*h) - 3*f(x + 2*h) + 3*f(x + h) - f(x)) / (h**3)
def f3b(f, x, h):
  return (f(x) - 3*f(x - h) + 3*f(x - 2*h) - f(x - 3*h)) / (h**3)
def f3c(f, x, h):
  return (f(x + 2*h) - 2*f(x + h) + 2*f(x - h) - f(x - 2*h)) / (2*h**3)

d3f = f3f(function, x, h)
print(f"turunan ketiga secara maju dari f di x = {x} adalah {d3f}")

d3b = f3f(function, x, h)
print(f"turunan ketiga secara mundur dari f di x = {x} adalah {d3b}")

d3c = f3f(function, x, h)
print(f"turunan ketiga secara pusat dari f di x = {x} adalah {d3c}")

"""## Integral Numerik

Jumlah Kanan
"""

def right_sum(f, a, b, n):
  h = (b - a) / n
  sum = 0
  for i in range(n):
    sum += f(a + (i)*h)
  return sum * h

a = 0
b = 1
n = 100
ika = right_sum(function, a, b, n)
print(f"Integral dari fungsi dengan jumlah kanan dari x = {a} sampai x = {b} sebanyak {n} partisi adalah {ika}")

"""Jumlah Kiri"""

def left_sum(f, a, b, n):
  h = (b - a) / n
  sum = 0
  for i in range(n):
    sum += f(a + (i - 1)*h)
  return sum * h

iki = left_sum(function, a, b, n)
print(f"Integral dari fungsi dengan jumlah kanan dari x = {a} sampai x = {b} sebanyak {n} partisi adalah {iki}")

"""Jumlah Pusat"""

def central_sum(f, a, b, n):
  h = (b - a) / n
  sum = 0
  for i in range(n):
    sum += f(a + (i + 0.5)*h)
  return sum * h

ipu = central_sum(function, a, b, n)
print(f"Integral dari fungsi dengan jumlah kanan dari x = {a} sampai x = {b} sebanyak {n} partisi adalah {ipu}")

"""Midpoint rule"""

def midpoint_sum(f, a, b, n):
  h = (b - a) / n
  sum = 0
  for i in range(n):
    sum += f(a + i*h - h/2)
  return sum * h

it = midpoint_sum(function, a, b, n)
print(f"Integral dari fungsi dengan aturan titik tengah dari x = {a} sampai x = {b} sebanyak {n} partisi adalah {it}")

"""Trapezoidal rule"""

def trapezoidal_sum(f, a, b, n):
  h = (b - a) / n
  sum = 0
  for i in range(n):
    sum +=  f(a + i*h)
  return (f(a) + 2*sum + f(b)) * (h/2)

tr = trapezoidal_sum(function, a, b, n)
print(f"Integral dari fungsi dengan aturan trapezoidal dari x = {a} sampai x = {b} sebanyak {n} partisi adalah {tr}")

"""Simpson 1/3"""

def simpson3_sum(f, a, b):
  h = (b - a) / 2
  return (f(a) + 4*f(h) + f(b)) * (h/3)

sp3 = simpson3_sum(function, a, b)
print(f"Integral dari fungsi dengan aturan simpson 1/3 dari x = {a} sampai x = {b} sebanyak {n} partisi adalah {sp3}")

"""Simpson 3/8"""

def simpson8_sum(f, a, b):
  h = (b - a) / 3
  return (f(a) + 3*f(h) + 3*f(2*h) + f(b)) * (3*h/8)

sp8 = simpson8_sum(function, a, b)
print(f"Integral dari fungsi dengan aturan simpson 3/8 dari x = {a} sampai x = {b} sebanyak {n} partisi adalah {sp8}")
