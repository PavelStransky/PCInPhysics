import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm           # Colour maps for the contour graph

from nd import random_direction_gaussian

generator = np.random.default_rng()
   
def minimize(function, dimension=2, step_size=0.01, initial_condition=None, initial_condition_box=1, max_failed_steps=100):
    """ Simple minimization method using random walk.

    Arguments:
    function -- function to minimize
    dimension -- dimensionality of the function
    initial_condition -- the starting point; if None, initial conditions chosen randomly from a box of size given by initial_condition_box
    max_failed_steps -- number of steps to stop the calculation
    """
    if initial_condition is None:       # Random initial condition within box of size given by initialConditionBox
        initial_condition = initial_condition_box * (2 * generator.random(dimension) - 1)
    
    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    failed_steps = 0                    # Number of consecutive steps in which we haven't moved (criterion to stop the minimization) 
    num_steps = 0                       # Total number of steps

    while failed_steps < max_failed_steps:
        new_position = position + step_size * random_direction_gaussian(dimension)
        newf = function(new_position)

        if newf < f:
            position = new_position
            f = newf

            path.append(position)

            failed_steps = 0

        else:
            failed_steps += 1        # Rejected step

        num_steps += 1

    print(f"Minimum = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)


def minimize_adaptive(function, dimension=2, initial_step_size=0.1, final_step_size=1E-6, initial_condition=None, initial_condition_box=1, max_failed_steps=100):
    """ Minimization method using random walk and adaptive step size

    Arguments:
    function -- function to minimize
    dimension -- dimensionality of the function
    initial_condition -- the starting point; if None, initial conditions chosen randomly from a box of size given by initial_condition_box
    max_failed_steps -- number of steps to stop the calculation
    """
    if initial_condition is None:       # Random initial condition within box of size given by initialConditionBox
        initial_condition = initial_condition_box * (2 * generator.random(dimension) - 1)
    
    position = np.array(initial_condition)
    f = function(position)

    path = [position]

    failed_steps = 0                    # Number of consecutive steps in which we haven't moved (criterion to stop the minimization) 
    num_steps = 0                       # Total number of steps

    step_size = initial_step_size

    while step_size > final_step_size:
        new_position = position + step_size * random_direction_gaussian(dimension)
        newf = function(new_position)

        if newf < f:
            position = new_position
            f = newf

            path.append(position)

            failed_steps = 0

        else:
            failed_steps += 1           # Rejected step

            if failed_steps > max_failed_steps:
                failed_steps = 0
                step_size *= 0.5        # Step size reduced by half 

        num_steps += 1

    print(f"Minimum (adaptive step) = {position}, function value = {f}, steps = {num_steps}")

    return np.array(path)
