import numpy as np
def solve_2d(initial, mask=0, iterations=2000):   
    """ Calculates the Laplace equation in 2D with a Dirichlet boundary condition using
        the Gauss-Seidel method.
        
        Arguments:
        initial -- Initial matrix; elements without fixed boudary condition have value mask
        mask -- Special value marking elements where we look for the solution
        iterations -- Number of iterations
    """
    potential = np.copy(initial)
    potential[potential == mask] = 0

    lengthx, lengthy = initial.shape

    for _ in range(iterations):
        for i in range(lengthx):
            for j in range(lengthy):
                if initial[i, j] == mask:
                    v = 0
                    n = 0
                    if i > 0:
                        v += potential[i - 1, j]
                        n += 1
                    if i < lengthx - 1:
                        v += potential[i + 1, j]
                        n += 1
                    if j > 0:
                        v += potential[i, j - 1]
                        n += 1
                    if j < lengthy - 1:
                        v += potential[i, j + 1]
                        n += 1
                    potential[i, j] = v / n
        
    return potential

def solve_2d_periodic_x(initial, mask=0, iterations=2000):   
    """ Calculates the Laplace equation in 2D with a Dirichlet boundary condition using
        the Gauss-Seidel method. Periodic boundary in x.
        
        Arguments:
        initial -- Initial matrix; elements without fixed boudary condition have value mask
        mask -- Special value marking elements where we look for the solution
        iterations -- Number of iterations
    """
    potential = np.copy(initial)
    potential[potential == mask] = 0

    lengthx, lengthy = initial.shape

    for _ in range(iterations):
        for i in range(lengthx):
            for j in range(lengthy):
                if initial[i, j] == mask:
                    v = 0
                    n = 0

                    v += potential[i - 1, j]
                    v += potential[(i + 1) % lengthx, j]
                    n += 2

                    if j > 0:
                        v += potential[i, j - 1]
                        n += 1
                    if j < lengthy - 1:
                        v += potential[i, j + 1]
                        n += 1

                    potential[i, j] = v / n
        
    return potential

def charge_density(potential):
    """ Returns the charge density connected with the given 2D potential """
    result = np.zeros_like(potential)

    lengthx, lengthy = potential.shape

    for i in range(lengthx):
        for j in range(lengthy):
            v = 0
            if i > 0:
                v += potential[i - 1, j]
                v -= potential[i, j]
            if i < lengthx - 1:
                v += potential[i + 1, j]
                v -= potential[i, j]
            if j > 0:
                v += potential[i, j - 1]
                v -= potential[i, j]
            if j < lengthy - 1:
                v += potential[i, j + 1]
                v -= potential[i, j]

            result[i, j] = v
        
    return result

def force(potential):
    """ Returns the components of the electrostatical force connected with the potential """
    forcex = np.zeros_like(potential)
    forcey = np.zeros_like(potential)

    lengthx, lengthy = potential.shape

    for i in range(lengthx):
        for j in range(1, lengthy - 1):
            forcex[i, j] = -0.5 * (potential[(i + 1) % lengthx, j] - potential[i - 1, j])
            forcey[i, j] = -0.5 * (potential[i, j + 1] - potential[i, j - 1])

    return forcex, forcey