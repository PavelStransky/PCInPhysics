import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm           # Colour maps for the contour graph

from nd import random_direction_gaussian

generator = np.random.default_rng()
   
def minimize(function, dimension=2, temperature=1, step_size=0.01, initial_condition=None, initial_condition_box=1, max_steps=20000):
    """ Simple minimization method using random walk and Metropolis algorithm.

    Arguments:
    function -- function to minimize
    dimension -- dimensionality of the function
    temperature -- temperature of the Metropolis algorithm
    initial_condition -- the starting point; if None, initial conditions chosen randomly from a box of size given by initial_condition_box
    max_steps -- total number of steps
    """
    if initial_condition is None:       # Random initial condition within box of size given by initialConditionBox
        initial_condition = initial_condition_box * (2 * generator.random(dimension) - 1)
    
    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    num_steps = 0                    # Total number of steps

    while num_steps < max_steps:
        new_position = position + step_size * random_direction_gaussian(dimension)
        newf = function(new_position)
        C = np.exp((f - newf) / temperature)    # Boltzmann coefficient (for step down C > 1)

        if C > generator.random():
            position = new_position
            f = newf

            path.append(position)

        num_steps += 1

    print(f"Minimum (Metropolis) = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)


def minimize_adaptive(function, dimension=2, initial_temperature=1, initial_step_size=1, final_step_size=1E-6, initial_condition=None, initial_condition_box=1, num_steps_change=100):
    """ Minimization method using random walk and Metropolis algorithm with adaptive temperature.

    Arguments:
    function -- function to minimize
    dimension -- dimensionality of the function
    initital_temperature -- initital temperature of the Metropolis algorithm
    initial_condition -- the starting point; if None, initial conditions chosen randomly from a box of size given by initial_condition_box
    num_steps_change -- number of steps to decrease the step size and temperature by factor 1/2
    """

    if initial_condition is None:       # Random initial condition within box of size given by initialConditionBox
        initial_condition = initial_condition_box * (2 * generator.random(dimension) - 1)
    
    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    num_steps = 0                    # Total number of steps
    step_size = initial_step_size
    temperature = initial_temperature

    while step_size > final_step_size:
        new_position = position + step_size * random_direction_gaussian(dimension)
        newf = function(new_position)
        C = np.exp((f - newf) / temperature)    # Boltzmann coefficient (for step down C > 1)

        if C > generator.random():
            position = new_position
            f = newf

            path.append(position)
    
        num_steps += 1

        if num_steps % num_steps_change == 0:
            step_size /= 2
            temperature /= 2

    print(f"Minimum (Metropolis adaptive step) = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)