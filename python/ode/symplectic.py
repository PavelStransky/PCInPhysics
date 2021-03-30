import numpy as np
import matplotlib.pyplot as plt

import ode

def verlet(model, xv, t, dt):
    """ Verlet symplectic algorithm """
    x, v = xv
    v, a = model(xv, t)
    
    x1 = x + v * dt + 0.5 * a * dt**2
    
    a1 = model([x1, v], t)[1]    
    
    v1 = v + 0.5 * (a + a1) * dt
    t1 = t + dt
    
    return np.array([x1, v1]), t1


def euler_1_modified_v(model, xv, t, dt):
    """ First-order Euler method with advanced velocity """
    x, v = xv
    v1 = v + model([x, v], t)[1] * dt     # v calculated first
    x1 = x + model([x, v1], t)[0] * dt    # ... and used the new value for y
    t1 = t + dt
    return np.array([x1, v1]), t1


def euler_1_modified_x(model, xv, t, dt):
    """ First-order Euler method with advanced coordinate """
    x, v = xv
    x1 = x + model([x, v], t)[0] * dt     # y calculated first
    v1 = v + model([x1, v], t)[1] * dt    # ... and used the new value for v
    t1 = t + dt
    return np.array([x1, v1]), t1


def plot_energy(model, initial_condition, energy_function, index=0, integrators=[ode.euler_1, ode.euler_2, ode.runge_kutta_4, verlet, euler_1_modified_v, euler_1_modified_x], **kwargs):
    """ Compares solutions for different ODE methods in one graph.

        Arguments:
        model -- a function returning the right-hand side of the ODE
        energy_function -- function that calculates energy 
        index -- for a set of ODE the index of the function to be plotted
        kwargs -- addtitional parameters for ode_solve function (step, times, etc)
    """

    for integrator in integrators:
        ys, ts = ode.ode_solve(model, initial_condition, integrator=integrator, **kwargs)
        
        es = [energy_function(*xv) for xv in ys]
        plt.plot(ts, es, label=integrator.__name__)

    # Axes labels
    plt.xlabel("t")
    plt.ylabel("E")
    plt.legend()

    plt.show()
