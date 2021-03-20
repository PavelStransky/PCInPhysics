import matplotlib.pyplot as plt

def step_euler_1(model, y, t, dt):
    """ First-order Euler method """
    y1 = y + model(y, t) * dt
    t1 = t + dt
    return y1, t1


def step_euler_2(model, y, t, dt):
    """ Second-order Euler method """
    d1 = model(y, t)
    d2 = model(y + d1 * dt, t)
    y1 = y + 0.5 * (d1 + d2) * dt
    t1 = t + dt
    return y1, t1


def step_runge_kutta_4(model, y, t, dt):
    """ Fourth-order Runge-Kutta algoritm """
    d1 = model(y, t)
    d2 = model(y + 0.5 * d1 * dt, t + 0.5 * dt)
    d3 = model(y + 0.5 * d2 * dt, t + 0.5 * dt)
    d4 = model(y + d3 * dt, t + dt)
    
    y1 = y + (d1 + 2 * d2 + 2 * d3 + d4) * dt / 6
    t1 = t + dt
    
    return y1, t1


def ode_solve(model, step=step_euler_1, dt=0.1, maxt=10, initial_condition=1):
    """ Numerical solution of a differential equation by the specified integrator.

        Arguments:
        model -- a function returning the right-hand side of the ODE
        step -- the integrator
        dt -- step size
        maxt -- integration performed from t=0 to t=maxt

        Returns:
        list with solution [y0, y1, y2, ...]
        list with times [t0, t1, y2, ...]
        name of the integrator
    """
    y = initial_condition                    # Initial conditions
    ys = [y]                                # List with results
    
    t = 0                                   # Actual time
    ts = [t]                                # List with times
    
    while t < maxt:
        y, t = step(model, y, t, dt)        # Step
        
        ys.append(y)                        # Store position
        ts.append(t)                        # Store time
            
    return ys, ts, step.__name__


def show_graph(ode_solutions, analytical_solution=None, ylim=None):
    """ Shows multiple results in one graph.

        Arguments:
        ode_solutions -- a list of results returned from ode_solve
        analytical_solution -- if we want to show an extra panel with absolute deviations from the exact solution
        ylim -- limits for the vertical axis
    """
    if analytical_solution != None:
        plt.subplot(211)                    # First panel
        
    plt.xlabel('t')
    plt.ylabel('y')

    if ylim != None:
        plt.ylim(ylim)

    for ys, ts, methodName in ode_solutions:       
        plt.plot(ts, ys, label=methodName)  # We plot just the coordinate and disregard the velocity

    plt.legend()

    if analytical_solution != None:
        plt.subplot(212)                    # Second panel
        plt.xlabel('t')
        plt.ylabel('$\Delta$y')
        if ylim != None:
            plt.ylim(ylim)
        
        for ode_solution in ode_solutions:
            plt.plot(ode_solution[0], local_error(ode_solution, analytical_solution))
    
    plt.show()


def local_error(ode_solution, analytical_solution):
    """ Calculates local error (deviation of the exact solution from the numerical solution).

        Arguments:
        ode_solution -- a result returned from ode_solve
    """
    ys, ts, _ = ode_solution
    return [y - analytical_solution(t) for y, t in zip(ys, ts)]


def compare_methods(model, dt = 0.1, analytical_solution=None):
    """ Compares different methods for solving differential equations """
    ode_solutions = []

    ode_solutions.append(ode_solve(model, step=step_euler_1, dt=dt))
    ode_solutions.append(ode_solve(model, step=step_euler_2, dt=dt))
    ode_solutions.append(ode_solve(model, step=step_runge_kutta_4, dt=dt))

    #plt.figure(figsize=(8,8))

    show_graph(ode_solutions, analytical_solution=analytical_solution)
