import numpy as np

import ode
import graphs

def ho(y, t):
    """ Derivatives for the harmonic osciilator """
    x, v = y
    return np.array([v, -x])

def analytical_solution(t):
    return np.sin(t)

graphs.plot_compare_methods(ho, (0, 1), index=0, analytical_solution=analytical_solution, dt=0.5)
graphs.plot_compare_steps(ho, (0, 1), ode.euler_1, analytical_solution=analytical_solution)
graphs.plot_cummulative_error(ho, (0, 1), analytical_solution, index=0)