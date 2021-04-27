import numpy as np
import matplotlib.pyplot as plt

generator = np.random.default_rng()

def volume(tries=1000000, dimension=3):
    """ Volume of the dimension-dimensional unit ball calculated by the Monte-Carlo Hit-And-Miss method """
    hits = 0
    
    for _ in range(tries):
        # The same code snippet as in RandomWalk in an arbitrary dimension
        random_vector = 2 * generator.random(dimension) - 1
        norm = np.linalg.norm(random_vector) # Norm of the vector
        
        if norm <= 1:
            hits += 1

    cube_volume = 2**dimension
    ball_volume = hits / tries * cube_volume
    error = np.sqrt(hits) / tries * cube_volume

    print(f"V{dimension}={ball_volume} += {error} (Počet zásahů: {hits})")

    return ball_volume, error


def plot_volumes(tries=1000000, dimensions=range(1, 16)):
    """ Graph of volumes of various dimensional balls (including error) """
    result = np.asarray([volume(tries, dimension) for dimension in dimensions])

    volumes = result[:, 0]
    errors = result[:, 1]

    plt.errorbar(dimensions, volumes, yerr=errors)
    plt.title("Objem $d$-rozměrné jednotkové koule")
    plt.xlabel("$d$")
    plt.ylabel("$V$")
    plt.show()

volume(dimension=15)