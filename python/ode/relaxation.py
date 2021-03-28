import numpy as np

import ode
import graphs

def relaxation(y, t):
    """ Derivatives for the relaxation system """
    return -y

def analytical_solution(t):
    return np.exp(-t)


graphs.plot_compare_methods(relaxation, 1, analytical_solution=analytical_solution, dt=0.5)
graphs.plot_compare_steps(relaxation, 1, ode.euler_1, analytical_solution=analytical_solution)
graphs.plot_cummulative_error(relaxation, 1, analytical_solution)