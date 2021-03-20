import ode
import math

def relaxation(y, t):
    """ Derivatives for the relaxation system """
    return -y

def analytical_solution(t):
    return math.exp(-t)

ode.compare_methods(relaxation, dt=0.1, analytical_solution=analytical_solution)