import numpy as np

import ode
import graphs
import symplectic

def ho(y, t):
    """ Derivatives for the harmonic oscillator """
    x, v = y
    return np.array([v, -x])


def ho_solution(t):
    return np.sin(t)


def ho_energy(x, v):
    return 0.5 * (x**2 + v**2)

dt = 0.1
maxt = 30

graphs.plot_compare_methods(ho, (0, 1), index=0, analytical_solution=ho_solution, dt=dt, maxt=maxt)
graphs.plot_compare_methods(ho, (0, 1), index=0, analytical_solution=ho_solution, integrators=[ode.euler_2, ode.runge_kutta_4, symplectic.verlet, symplectic.euler_1_modified_x], dt=dt, maxt=maxt)
graphs.plot_compare_steps(ho, (0, 1), ode.euler_1, analytical_solution=ho_solution, maxt=maxt)

symplectic.plot_energy(ho, (0, 1), energy_function=ho_energy, dt=dt, maxt=maxt)
symplectic.plot_energy(ho, (0, 1), energy_function=ho_energy, dt=dt, maxt=maxt, integrators=[ode.euler_2, ode.runge_kutta_4, symplectic.verlet])

graphs.plot_cummulative_error(ho, (0, 1), ho_solution, index=0, integrators=[ode.euler_1, ode.euler_2, ode.runge_kutta_4, symplectic.verlet, symplectic.euler_1_modified_x])
