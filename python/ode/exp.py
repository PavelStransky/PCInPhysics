import numpy as np

import ode
import graphs
import symplectic

def exp(y, t):
    """ Derivatives for the exponential system """
    x, v = y
    return np.array([v, x])


def exp_solution(t):
    return np.exp(-t)

dt = 0.1
maxt = 20

graphs.plot_compare_methods(exp, (1, -1), index=0, analytical_solution=exp_solution, dt=dt, maxt=maxt)
graphs.plot_compare_methods(exp, (1, -1), index=0, analytical_solution=exp_solution, integrators=[ode.euler_1, ode.euler_2, ode.runge_kutta_4, symplectic.verlet, symplectic.euler_1_modified_x], dt=dt, maxt=maxt)
graphs.plot_compare_steps(exp, (1, -1), ode.euler_1, analytical_solution=exp_solution, maxt=maxt)
graphs.plot_compare_steps(exp, (1, -1), ode.euler_2, analytical_solution=exp_solution, maxt=maxt)

graphs.plot_compare_steps(exp, (1, -1), symplectic.verlet, analytical_solution=exp_solution, maxt=maxt)
