import matplotlib.pyplot as plt
from matplotlib import cm               # Colour maps for the contour graph
import numpy as np

def f(x, y):                            # Example of a function of two independent variables
    return x**4 - 2*x**2 + x + y**2

numSteps = 100                          # Number of points in the mesh
numContours = 30                        # Number of contours in the graph

x = y = np.linspace(-2.0, 2.0, numSteps)# Range of x and y values for the graph

X, Y = np.meshgrid(x, y)                # Grid for calculating values of the function
Z = f(X, Y)                             # numpy is powerful and can handle this

# cmap specifies one of the colour map. All colour maps are given in
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
plt.contourf(X, Y, Z, numContours, cmap=cm.hot) 
plt.colorbar()                          # Legend for the contour graph
plt.show()
