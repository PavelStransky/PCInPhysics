import numpy as np
import matplotlib.pyplot as plt 

import time

from multiprocessing import Pool
from integration import *


def plot_duration(function, processes=range(1, 25), **kwargs):
    def duration(p):
        startTime = time.time()
        result = function(p, **kwargs)
        duration = time.time() - startTime
        print(f"I = {result} (Doba výpočtu v {p} vláknech: {duration})")
        return duration

    durations = [duration(p) for p in processes]
    
    plt.plot(processes, durations)
    plt.title("Celkový čas výpočtu")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$T [s]$")
    plt.show()

def integrate_4D_Pool(p, n):
    """ Using Pool and map to perform the Monte-Carlo integration for the 4D integral"""
    with Pool(processes=p) as pool:
        args = np.full(p, n // p)    # Array of length p, each element having value n
        results = pool.map(integral3, args)

    average = sum(results) / len(results)
    return average    


def scalar_product(v1, v2):
    return sum(v1 * v2)

def multiply_mv(p, matrix, vector):
    with Pool(processes=p) as pool:
        length = len(vector)

        args = ((matrix[i], vector) for i in range(length))
        result = pool.starmap(scalar_product, args)
    return np.array(result)


if __name__ == "__main__":
    #integrate_4D_Pool(1, 100000)
    #plot_duration(integrate_4D_Pool, n=100000)

    matrix = np.random.rand(5000,5000)
    vector = np.random.rand(5000)

    plot_duration(multiply_mv, matrix=matrix, vector=vector)

    np.dot(matrix, vector)
