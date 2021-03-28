import numpy as np

def euler_1(model, y, t, dt):
    """ First-order Euler method """
    y1 = y + model(y, t) * dt
    t1 = t + dt
    return y1, t1


def euler_2(model, y, t, dt):
    """ Second-order Euler method """
    d1 = model(y, t)
    d2 = model(y + d1 * dt, t)
    y1 = y + 0.5 * (d1 + d2) * dt
    t1 = t + dt
    return y1, t1


def runge_kutta_4(model, y, t, dt):
    """ Fourth-order Runge-Kutta algoritm """
    d1 = model(y, t)
    d2 = model(y + 0.5 * d1 * dt, t + 0.5 * dt)
    d3 = model(y + 0.5 * d2 * dt, t + 0.5 * dt)
    d4 = model(y + d3 * dt, t + dt)
    
    y1 = y + (d1 + 2 * d2 + 2 * d3 + d4) * dt / 6
    t1 = t + dt
    
    return y1, t1


def ode_solve(model, initial_condition, integrator=runge_kutta_4, dt=0.1, maxt=10):
    """ Numerical solution of a differential equation by the specified integrator.

        Arguments:
        model -- a function returning the right-hand side of the ODE
        dt -- step size
        maxt -- integration performed from t=0 to t=maxt

        Returns:
        list with solution [y0, y1, y2, ...]
        list with times [t0, t1, y2, ...]
    """
    y = np.array(initial_condition)         # Initial conditions
    ys = [y]                                # List with results
    
    t = 0                                   # Actual time
    ts = [t]                                # List with times
    
    while t < maxt:
        y, t = integrator(model, y, t, dt)  # Step
        
        ys.append(y)                        # Store position
        ts.append(t)                        # Store time
            
    return np.array(ys), np.array(ts)