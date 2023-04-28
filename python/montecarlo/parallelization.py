import numpy as np
import matplotlib.pyplot as plt 

import time

import multiprocessing as mp
from integration import *


def integrate_1D_Pool(p, n, function, a, b):
    """ Using Pool and map to perform the Monte-Carlo integration 
        
        Parameters: 
        p: Number of processes
        n: Total number of Monte-Carlo points
        function: Integrated function
        a, b: Integration limits
    """
    n1 = n // p             # Number of MC points calculated by each process

    with mp.Pool(processes=p) as pool:
        args = ((n1, function, a, b),) * p
        # Copies p-times the given n-tuple. The same as 
        # args = [(n, function, a, b) for _ in range(p)]
        
        results = pool.starmap(integrate_1D, args)
        #results = pool.starmap_async(integrate_1D, args).get() # Asynchronous procesing

    result = sum(results) / len(results)
    return result


def plot_1D_duration(processes=range(1, 25), n=1000000, function=f1, a=0, b=2*np.pi):
    """ Plots a graph with the total computation time depending on the number of processes """

    def duration(p):
        start_time = time.time()
        result = integrate_1D_Pool(p, n, function, a, b)
        duration = time.time() - start_time
        print(f"I({function.__name__}) = {result} (Doba výpočtu v {p} vláknech: {duration})")
        return duration

    durations = [duration(p) for p in processes]
    
    plt.plot(processes, durations)
    plt.title(f"Celkový čas výpočtu pro N={n}")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$T [s]$")
    plt.show()


def integrate_1D_parallel(result, *args, **kwargs):
    """ Wrapper for function Integrate1D to Process parallelization """
    result.value = integrate_1D(*args, **kwargs)


def integrate_1D_Process(p, n, function, a, b):
    """ Using Process for Monte-Carlo integration """
    processes = []
    results = []

    for _ in range(p):
        result = mp.Value('d', 0)
        process = mp.Process(target=integrate_1D_parallel, args=(result, n, function, a, b))
        process.start()
        processes.append(process)
        results.append(result)

    for process in processes:
        process.join()

    results = [result.value for result in results]
    return sum(results) / len(results)


if __name__ == "__main__":
    print("Počet logických jader:", mp.cpu_count())

    print(integrate_1D_Pool(8, 100000, f1, 0, 2 * np.pi))
    plot_1D_duration(n=1000000)
    plot_1D_duration(n=10000000)
    print(integrate_1D_Process(8, 100000, f1, 0, 2 * np.pi))