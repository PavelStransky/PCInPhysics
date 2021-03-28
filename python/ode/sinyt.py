import numpy as np
import matplotlib.pyplot as plt

import ode
import graphs

def model(y, t):
    return np.sin(y * t)

ys, ts = ode.ode_solve(model, 1, dt=0.02)
plt.plot(ts, ys)
plt.xlabel("t")
plt.ylabel("y")
plt.title(r"$\frac{dy}{dt}=sin(yt)$")
plt.show()