import matplotlib.pyplot as plt

x = 0
v = 1

xs = [x]
vs = [v]

dt = 0.001
tmax = 100

t = 0
ts = [t]

while t < tmax:
    x1 = x + v * dt
    v1 = v - x * dt
    t1 = t + dt

    xs.append(x1)
    vs.append(v1)
    ts.append(t1)

    x = x1
    v = v1
    t = t1

plt.plot(ts, xs)
plt.xlabel("t")
plt.ylabel("sin t")
plt.show()