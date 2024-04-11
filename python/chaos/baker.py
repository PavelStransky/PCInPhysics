import matplotlib.pyplot as plt
import numpy as np

plt.ion()

def transformation(points):
    result = []

    for point in points:
        if 0 <= point[0] < 0.5:
            result.append([2 * point[0], 0.5 * point[1], point[2], point[3]])
        else:
            result.append([2 - 2 * point[0], 1 - 0.5 * point[1], point[2], point[3]])
    
    return result

points = []
dough = 0
raisin = 0

while dough < 200000:
    x = np.random.rand()
    y = np.random.rand()
    if (x - 0.3)**2 + (y - 0.3)**2 > (0.01)**2:
        dough += 1
        points.append([x, y, 1, 2])

while raisin < 3000:
    x = np.random.rand()
    y = np.random.rand()
    if (x - 0.3)**2 + (y - 0.3)**2 < (0.06)**2:
        raisin += 1
        points.append([x, y, 1, 1])

points = np.array(points)

fig, ax = plt.subplots()
fig.set_size_inches(7, 7)

for i in range(20):
    ax.cla()    
    ax.scatter(*points.T)

    fig.patch.set_visible(False)
    ax.axis('off')

    plt.title(i)
    plt.show()
    plt.pause(0.5)
    plt.savefig(f"d:/{i}.png")
    points = np.array(transformation(points))
