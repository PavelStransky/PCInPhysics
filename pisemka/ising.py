import numpy as np
import matplotlib.pyplot as plt

""" Constants """
N = 10
J = 1
RELAXATION_STEPS = 50
MEAN_STEPS = 50

def generate():
    model = np.random.randint(-1, 1, (N, N), dtype=np.int32)
    model = 2*model + 1
    return model

def energy(model):
    e = 0
    for i in range(N):
        for j in range(N):
            e -= model[i, j] * model[(i + 1) % N, j]
            e -= model[i, j] * model[i, (j + 1) % N]
    return e

def magnetisation(model):
    return sum(model.flatten()) / model.size

def metropolis(model, T):
    e0 = energy(model)
    for i in range(N):
        for j in range(N):
            model[i, j] = -model[i, j]
            ef = energy(model)

            if ef > e0:
                p = np.exp((e0 - ef) / T) if T > 0 else 0
                if np.random.random() > p:
                    model[i, j] = -model[i, j]
                    ef = e0

            e0 = ef
    return model

def calculate_ME(T):
    model = generate()
    for _ in range(RELAXATION_STEPS):
        model = metropolis(model, T)

    m = []
    e = []
    for _ in range(MEAN_STEPS):
        model = metropolis(model, T)
        m.append(magnetisation(model))
        e.append(energy(model))

    mean_m = np.array(m).mean()
    mean_e = np.array(e).mean()
    
    print(f"T = {T}, M = {mean_m}, E = {mean_e}")

    return mean_m, mean_e

ms = []
es = []
Ts = np.linspace(0, 4, 101)
for T in Ts:
    m, e = calculate_ME(T)
    ms.append(m)
    es.append(e)

plt.scatter(Ts, ms)
plt.xlabel("T")
plt.ylabel("M")
plt.show()

plt.scatter(Ts, es)
plt.xlabel("T")
plt.ylabel("E")
plt.show()