import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm           # Colour maps for the contour graph

import scipy.optimize
import minimize
import metropolis

def f(X):
    """ Quadratic test function """ 
    x, y = X
    return x*x + y*y


def g(X, parameters=(1, 100)):
    """ Rosenbrock test function 
        https://en.wikipedia.org/wiki/Rosenbrock_function
    """
    x, y = X
    a, b = parameters
    return (a - x)**2 + b * (y - x * x)**2


def h(X):
    """ 4D test function """
    s, t, u, v = X
    sum2 = s*s + t*t + u*u + v*v
    if sum2 > 2:
        return float("inf")
    return 0.25 * sum2 - 0.5 * ((s*s + t*t) * (2 - sum2) + (s*u - t*v)**2) + 0.5 * s * np.sqrt(2 - sum2)

def r(X, parameters=(1,)):
    """ Double-well test function """
    x, y = X
    a, = parameters
    return x**4 - 2 * x*x + a * x + y*y


def show_graph(function, paths=(), box_size=1, num_contours=100):
    """ Plots a contour graphs of the give 2D function.

    Arguments:
    Function -- function to plot
    parameters -- additional parameters of the function
    paths -- curves to plot in the graph
    box_size -- limits of the x, y range
    num_contours -- number of contours in the graph
    """
    x = y = np.linspace(-box_size, box_size, 100)# Range of x and y values for the graph

    X, Y = np.meshgrid(x, y)                     # Grid for calculating values of the function
    Z = function([X, Y])

    plt.figure(figsize=(8,6))
    plt.contourf(X, Y, Z,num_contours, cmap=cm.hot)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.colorbar(label=function.__name__ + '(x,y)')  # Legend for the contour graph

    for path in paths:
        plt.plot(path[:,0], path[:,1])  
        plt.scatter(path[[0,-1],0], path[[0,-1],1])  # Indicate the initial and final points of the path
    plt.tight_layout()
    plt.show()


def multiple_paths(function, method=minimize.minimize, num_paths=10, initial_condition_box=1, **kwargs):
    """ Shows graph with a given number of random walk minimization paths. """
    paths = []

    for _ in range(num_paths):
        paths.append(method(function, initial_condition_box=initial_condition_box, **kwargs))

    show_graph(function, paths, box_size=1.2*initial_condition_box)

print("Function f:")
minimize.minimize(f, initial_condition=(2,0))
minimize.minimize_adaptive(f, initial_condition=(2,0))

print("Function g:")
minimize.minimize(g, initial_condition=(2,0))
minimize.minimize_adaptive(g, initial_condition=(2,0))

print("Function h:")
minimize.minimize(h, dimension=4)
minimize.minimize_adaptive(h, dimension=4)

print("Graphs:")
multiple_paths(g)
multiple_paths(g, method=minimize.minimize_adaptive)

multiple_paths(r, initial_condition_box=2)
multiple_paths(r, initial_condition_box=2, method=minimize.minimize_adaptive)
multiple_paths(r, initial_condition_box=2, method=metropolis.minimize)
multiple_paths(r, initial_condition_box=2, method=metropolis.minimize_adaptive)

print("SciPy minimize")
print(scipy.optimize.minimize(r, (2,2)))
print("SciPy basinhopping")
print(scipy.optimize.basinhopping(r, (2,2)))