# Using the in-built solve_ivp function to solve an ODE under various parameters

# Import relavent libraries and functions
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Step 1
# Define the ODE and solve it
dxdt = lambda t,x : -2*x
sol = solve_ivp(dxdt, [5, 15], [10] )

# Graphing the solution, in order to visualize it
plt.figure()
plt.plot(sol.t, sol.y[0])
plt.title("Step 1: dx/dt = -2x")
plt.xlabel("t-values")
plt.ylabel("x-values")
plt.show()

# Step 2
# Deterimining value of x(t=7)
sol = solve_ivp(dxdt, [5, 15], [10], t_eval = [7] )
print("This is the value for x(t=7): " + str(sol.y[0]))

# Step 3
# Adding a B parameter to the ODE
dxdt = lambda t,x, B: B*x

B=-2

# Solving the ODE with an additional parameter
sol = solve_ivp(dxdt, [5, 15], [10], args=(B,) )
# Graphing the solution, in order to visualize it
plt.figure()
plt.plot(sol.t, sol.y[0])
plt.title("Step 3: dx/dt = -2x")
plt.xlabel("t-values")
plt.ylabel("x-values")
plt.show()

# Step 4
# Solving the ODE for various B Parameter values
sol1 = solve_ivp(dxdt, [5, 15], [10], args=(-2,) )
sol2 = solve_ivp(dxdt, [5, 15], [10], args=(-4,) )
sol3 = solve_ivp(dxdt, [5, 15], [10], args=(-6,) )
sol4 = solve_ivp(dxdt, [5, 15], [10], args=(-8,) )

# Graphing the solutions, in order to visualize it
plt.figure()
plt.plot(sol1.t, sol1.y[0], label='B = -2')
plt.plot(sol2.t, sol2.y[0], label='B = -4')
plt.plot(sol3.t, sol3.y[0], label='B = -6')
plt.plot(sol4.t, sol4.y[0], label='B = -8')
plt.title("Step 4: dx/dt = Bx")
plt.xlabel("t-values")
plt.ylabel("x-values")
plt.legend()
plt.show()