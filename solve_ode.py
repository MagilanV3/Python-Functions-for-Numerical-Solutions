# This Python script solves an Ordinary Differential Equation in various ways

# Import Relavent Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define variables that are constant throughout all methods
f = lambda t, y : (1.2 * (np.exp(-10.5*y*t))) + 100*  np.sin(0.2*y)
y0 = 1
t0 = 0

# Intialize the plot
plt.figure()

# Part a) Explicit Euler's method(h=0.002)
h = 0.002
t = np.arange(0, 1 + h, h)
length = len(t)
y = np.zeros(length)
y[0] = y0

for i in range(0, length - 1):
    y[i+1] = (h*(f(t[i], y[i]))) + y[i] 

plt.plot(t, y, label="Euler's method (h=0.002)")

# Part b) Explicit Euler's method(h=0.1)
h = 0.1
t = np.arange(0, 1 + h, h)
length = len(t)
y = np.zeros(length)
y[0] = y0

for i in range(0, length - 1):
    y[i+1] = (h*(f(t[i], y[i]))) + y[i] 

plt.plot(t, y, label="Euler's method (h=0.1)")

# Part c) Heun's Method (h=0.1)
t = np.arange(0, 1 + h, h)
y = np.zeros(length)
y[0] = y0
for i in range(0, length):
    y_hold = (h*(f(t[i-1], y[i-1]))) + y[i-1]
    y[i] = ((h*0.5) * ((f(t[i-1], y[i-1])) + (f(t[i], y_hold)))) + y[i-1] 

plt.plot(t, y, label="Heun's method (h=0.1)")

# Part d) Midpoint's Method (h=0.1)
t = np.arange(0, 1 + h, h)
y = np.zeros(length)
y[0] = y0
for i in range(0, length):
    y[i] = (h*((f(t[i-1]+(h/2), y[i-1]+((h*0.5)*(f(t[i-1], y[i-1]))) )))) + y[i-1] 

plt.plot(t, y, label="Midpoint's method (h=0.1)")

# Part e) Range-Jutta Fourth order Method (h=0.1)
t = np.arange(0, 1 + h, h)
y = np.zeros(length)
y[0] = y0
for i in range(0, length-1):
    k1 = f(t[i], y[i])
    k2 = f(t[i] + (h/2), y[i] + ((k1*h) /2))
    k3 = f(t[i] + (h/2), y[i] + ((k2*h) /2))
    k4 = f(t[i] + h, y[i] + (k3*h))
    y[i+1] = y[i] + (((k1+(2*k2)+(2*k3)+k4)*h)/6)

plt.plot(t, y, label="Range-Jutta Fourth order Method (h=0.1)")

# Part f) solve_ivp solver in scipy (h=0.1)
sol = solve_ivp(f,[t0,1], [y0])

plt.plot(sol.t, sol.y[0], label='solve_ivp ')

plt.title("Graphing the Solutions for dy/dt through various methods")
plt.xlabel("t-values")
plt.ylabel("y-values")
plt.legend()
plt.show()