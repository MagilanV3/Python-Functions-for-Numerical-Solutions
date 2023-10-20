# Showing and graphinthe Butterfly Effect in Statistical thermodynamics, with multiple variables

# Import relavent libraries and functions
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the 3 ODE functions that needs to be solved
def odes(t, variables , ro):
    [x,y,z] = variables
    dxdt = 10*(y-x)
    dydt = (ro*x) - y - (x*z)
    dzdt = (x*y) - ((8/3)*z)
    return np.hstack([dxdt,dydt,dzdt])

#Step 1
# Solving the ODEs for multiple rho-values and graphing them

# Solving ODEs when rho = 14
sol_1=solve_ivp(odes,[0,100],[0,1,0], args =(14,))
ax = plt.axes(projection='3d')
zline = sol_1.y[2]
xline = sol_1.y[0]
yline = sol_1.y[1]
ax.plot3D(xline, yline, zline)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('The Butterfly Effect, when rho = 14')
plt.show()

# Solving ODEs when rho = 15
sol_2=solve_ivp(odes,[0,100],[0,1,0], args =(15,))
bx = plt.axes(projection='3d')
zline = sol_2.y[2]
xline = sol_2.y[0]
yline = sol_2.y[1]
bx.plot3D(xline, yline, zline)
bx.set_xlabel('x')
bx.set_ylabel('y')
bx.set_zlabel('z')
bx.set_title('The Butterfly Effect, when rho = 15')
plt.show()

# Solving ODEs when rho = 28
sol_3=solve_ivp(odes,[0,100],[0,1,0], args =(28,))
cx = plt.axes(projection='3d')
zline = sol_3.y[2]
xline = sol_3.y[0]
yline = sol_3.y[1]
cx.plot3D(xline, yline, zline)
cx.set_xlabel('x')
cx.set_ylabel('y')
cx.set_zlabel('z')
cx.set_title('The Butterfly Effect, when rho = 28')
plt.show()

# Solving ODEs when rho = 96.98
sol_4=solve_ivp(odes,[0,100],[0,1,0], args =(96.98,))
dx = plt.axes(projection='3d')
zline = sol_4.y[2]
xline = sol_4.y[0]
yline = sol_4.y[1]
dx.plot3D(xline, yline, zline)
dx.set_xlabel('x')
dx.set_ylabel('y')
dx.set_zlabel('z')
dx.set_title('The Butterfly Effect, when rho = 96.98')
plt.show()

# Step 2
# Graph the ODEs solutions, when rho = 28, but the intial value of x varies
fig = plt.figure(figsize=(12,6))

# Solving the ODEs, when inital value of x is 0 and rho=28
ex = fig.add_subplot(1, 2, 1, projection='3d')
zline = sol_3.y[2]
xline = sol_3.y[0]
yline = sol_3.y[1]
ex.plot3D(xline, yline, zline)
ex.set_xlabel('x')
ex.set_ylabel('y')
ex.set_zlabel('z')
ex.set_title('The Butterfly Effect, Intial value of x = 0')

# Solving the ODEs, when inital value of x is 0.001 and rho=28
sol_5=solve_ivp(odes,[0,100],[0.001,1,0], args =(28,))
fx = fig.add_subplot(1, 2, 2, projection='3d')
zline = sol_5.y[2]
xline = sol_5.y[0]
yline = sol_5.y[1]
fx.plot3D(xline, yline, zline)
fx.set_xlabel('x')
fx.set_ylabel('y')
fx.set_zlabel('z')
fx.set_title('The Butterfly Effect, Intial value of x = 0.001')
plt.show()

#Comments on the Findings. 

# The values when the inital guess is 0 for x, increase at a slower rate than when the inital guess is 0.001.
# On the graph, the scale for the x-axis also differs, as when the intial guess is 0, the scale is from -20 to 20.
# When the inital guess is 0.001, the scale is from -15 to 15