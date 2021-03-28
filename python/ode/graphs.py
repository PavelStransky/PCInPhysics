import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

import ode

def plot_solution_error(ys, ts, analytical_solution=None):
    """ Shows results in one panel and local error in a second panel (if analytical_solution specified)

        Arguments:
        ys, ts, method_name -- results returned from ode_solve
        analytical_solution -- if we want to show an extra panel with absolute deviations from the exact solution
        ylim -- limits for the vertical axis (for limiting unstable or exponential results)
    """
    if analytical_solution is not None:         
        plt.subplot(211)                    # First panel
        
    plt.xlabel('t')
    plt.ylabel('y')

    plt.plot(ts, ys)    
    plt.legend()

    if analytical_solution is not None:
        plt.subplot(212)                    # Second panel
        plt.xlabel('t')
        plt.ylabel(r'$\Delta$y')

        plt.plot(ts, local_error(ys, ts, analytical_solution))

    plt.show()


def local_error(ys, ts, analytical_solution):
    """ Calculates local error (deviation of the exact solution from the numerical solution).

        Arguments:
        ys -- function values to be compared
        ts -- independent variable
    """
    return ys - analytical_solution(ts)


def average_cummulative_error(ys, ts, analytical_solution):
    """ Calculates average cumulative error (average deviation of the exact solution from the numerical solution).

        Arguments:
        ys -- function values to be compared
        ts -- independent variable
    """
    residua = local_error(ys, ts, analytical_solution)**2
    return np.sqrt(sum(residua) / len(residua))


def plot_compare_methods(model, initial_condition, index=0, analytical_solution=None, integrators=[ode.euler_1, ode.euler_2, ode.runge_kutta_4], **kwargs):
    """ Compares solutions for different ODE methods in one graph.

        Arguments:
        model -- a function returning the right-hand side of the ODE
        analytical_solution -- exact solution of the ODE (if available)
        index -- for a set of ODE the index of the function to be plotted
        kwargs -- addtitional parameters for ode_solve function (step, times, etc)
    """

    show_error = analytical_solution is not None

    figure, axes = plt.subplots(2 if show_error else 1, 1)

    ts = None
    for integrator in integrators:
        ys, ts = ode.ode_solve(model, initial_condition, integrator=integrator, **kwargs)
        if ys.ndim != 1:
            ys = ys[:, index]

        axes[0].plot(ts, ys, label=integrator.__name__)

        if show_error:
            axes[1].plot(ts, local_error(ys, ts, analytical_solution))

    if analytical_solution is not None:
        axes[0].plot(ts, analytical_solution(ts), label=analytical_solution.__name__)

    # Axes labels
    axes[0].set_xlabel("t")
    axes[0].set_ylabel("y")
    axes[0].legend()

    if show_error:
        axes[1].set_xlabel("t")
        axes[1].set_ylabel(r'$\Delta$y')

    plt.show()


def plot_cummulative_error(model, initial_condition, analytical_solution, index=0, integrators=[ode.euler_1, ode.euler_2, ode.runge_kutta_4], dts=np.linspace(0.002, 0.1, 100), **kwargs):
    """ Compares solutions for different ODE methods in one graph.

        Arguments:
        model -- a function returning the right-hand side of the ODE
        analytical_solution -- exact solution of the ODE (if available)
        index -- for a set of ODE the index of the function to be plotted
        kwargs -- addtitional parameters for ode_solve function (step, times, etc)
    """

    plt.figure()

    for integrator in integrators:

        errors = []
        for dt in dts:
            ys, ts = ode.ode_solve(model, initial_condition, integrator=integrator, dt=dt, **kwargs)

            if ys.ndim != 1:
                ys = ys[:, index]

            errors.append(average_cummulative_error(ys, ts, analytical_solution))


        slope, intercept, r_value, p_value, std_err = linregress(np.log(dts), np.log(errors))
        plt.loglog(dts, errors, label=f"{integrator.__name__} $\\alpha$={slope:.3}")
            
    plt.xlabel("$\Delta$t")
    plt.ylabel("$\mathcal{E}$")
    plt.legend()

    plt.show()