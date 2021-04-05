import numpy as np
import matplotlib.pyplot as plt

import ode

sigma = 10
rho = 28
beta = 8/3

def lorenz(y, t):
    """ Lorenz model of atmospheric convection """
    x, ys, z = y

    dx = sigma * (ys - x)
    dy = x * (rho - z) - ys
    dz = x * ys - beta * z

    return np.array([dx, dy, dz])

ys, ts = ode.ode_solve(lorenz, (1,1,1), dt=0.01, maxt=100)

plt.figure()
plt.plot(ys[:,0], ys[:,2])
plt.xlabel("x")
plt.ylabel("z")
plt.title("Lorenz attractor")
plt.show()

# Thanks Samuel J. for this part of the code (plots a 3D interactive graph)
try:                                                                                            
    import plotly.express as px                                                                 
    
    fig = px.line_3d(x=ys[:,0], y=ys[:,1], z=ys[:,2])
    fig.show()
except:
    print("Missing Plotly module.")    
