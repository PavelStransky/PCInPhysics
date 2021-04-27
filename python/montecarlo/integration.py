
""" Monte-Carlo integration """
import numpy as np
import matplotlib.pyplot as plt

generator = np.random.default_rng()


def f1(x):
    return np.exp(-x) * np.sin(x)


def f2(x):
    return np.sin(x)**2 / np.sqrt(1 + x**4)


def integrate_1D(n, function, a, b):
    """ Basic Monte-Carlo 1D integration """
    result = 0
    for _ in range(n):
        x = (b - a) * generator.random() + a
        result += function(x)

    result = (b - a) / n * result
    return result


def integrate_1D_array(n, function, a, b):
    """ Monte Carlo integration via array. 
        It requieres more memory, but it is much faster. """
    x = (b - a) * generator.random(n) + a
    result = (b - a) / n * sum(function(x)) 
    return result

""" Specific function to integrate just the I3 integral """
def integral3(n):
    hits = 0
    result = 0

    for _ in range(n):
        x, y, z, w = generator.random(4)
        
        if (x - 0.5)**2 + (y - 0.5)**2 + (z - 0.5)**2 + (w - 0.5)**2 <= 0.25:
            hits += 1
            result += np.sin(np.sqrt(np.log(x + y + z + w + 2)))

    result = result / hits
    volume = hits / n

    print(f"I3 = {result} (number of hits: {hits}, volume of the integration region: {volume})")

    return result

""" More abstract way - works for any integration regions and any function """
def is_inside_region3(X):
    """ Returns true if the point X is inside the integration region """
    x, y, z, w = X
    return (x - 0.5)**2 + (y - 0.5)**2 + (z - 0.5)**2 + (w - 0.5)**2 <= 0.25


def f3(X):
    x, y, z, w = X
    return np.sin(np.sqrt(np.log(x + y + z + w + 2)))


def integral_ND(n, function, is_inside_region, dimension):
    """ Monte-Carlo integration of a general-dimensional function. """
    hits = 0
    result = 0

    for _ in range(n):
        X = generator.random(dimension)
        
        if is_inside_region(X):
            hits += 1
            result += function(X)

    result = result / hits
    volume = hits / n

    print(f"I3 = {result} (number of hits: {hits}, volume of the integration region: {volume})")

    return result


if __name__ == "__main__":
    print("I1 = {}".format(integrate_1D_array(1000000, f1, 0, 2 * np.pi)))
    print("I2 = {}".format(integrate_1D_array(1000000, f2, 0, np.sqrt(10 * np.pi))))
    print("I3 = {}".format(integral3(1000000)))
    print("I3 = {}".format(integral_ND(1000000, f3, is_inside_region3, dimension=4)))
