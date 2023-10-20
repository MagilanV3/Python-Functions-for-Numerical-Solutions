# Using the in-built solve_bvp function to solve a system of ODEs and graphing the solution

# Import relavent libraries and functions
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

# Intialize the boundry condition values
T_5 = 120
T_10 = 60
r_5 = 5
r_10 = 10

# Intialize the number of points for the solution
number_of_points = 100

# Define the function that is needed to solve
def odes(r, variables):
    [T, u] = variables
    dxdr = [u, (-(u/r))]
    return dxdr

# Define the function for evalulating residuals of the boundry conditions
def bc(T5, T10):
    BC1 = T5[0] - T_5
    BC2 = T10[0] - T_10
    return [BC1, BC2]

# Create the template of values to provide to the solve_bvp function
# The x_values are the inital mesh
x_values = np.linspace(r_5, r_10, number_of_points)
# The y-values are the inital guess for the function values at each x value
y_values = np.zeros((2,number_of_points))

# Using the in-built function to solve the system
sol = solve_bvp(odes, bc, x_values, y_values)

# Graphing the solution, in order to visualize it
plt.figure()
plt.plot(sol.x, sol.y[0])
plt.title("Question 3: T(r) vs r")
plt.xlabel("r")
plt.ylabel("T(r)")
plt.show()