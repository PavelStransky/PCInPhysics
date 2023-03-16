import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm                       # Colour maps for the contour graph

import poisson

lengthx = 50                                    # Capacitor length
lengthy = 50                                    # Distance between plates - horizontal axis

initial = np.full((lengthx, lengthy), -1.0)
initial[:, 0] = 0                               # Bottom layer (ground)
initial[:, -1] = 10                             # Top layer

rod_index = 25
rod_length = 30
initial[rod_index, 0:rod_length] = 0            # Lightning rod

person_index = 20
person_length = 10
initial[person_index, 0:person_index] = 0       # Person

potential = poisson.solve_2d(initial, mask=-1.0, iterations=5000)

plt.pcolormesh(np.transpose(potential), cmap=cm.hsv)
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label=r"$\varphi$")                # Legend for the contour graph
plt.show()

plt.plot(potential[rod_index, :], label="Hromosvod")
plt.plot(potential[person_index, :], label="Člověk")
plt.xlabel("y")
plt.ylabel(r"$\varphi$")
plt.legend()
plt.show()

charge = poisson.charge_density(potential)

plt.pcolormesh(np.transpose(charge), cmap=cm.hsv) 
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label=r"$\rho$")
plt.show()

# Charge on the top of the lightning rod
plt.plot(charge[rod_index, :], label=f"Špička hromosvodu: {charge[rod_index, rod_length - 1]}")
plt.plot(charge[person_index, :], label=f"Hlava člověka: {charge[person_index, person_length - 1]}")
plt.xlabel("y")
plt.ylabel(r"$\rho$")
plt.legend()
plt.show()