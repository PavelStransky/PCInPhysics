import numpy as np
import matplotlib.pyplot as plt 

import time

from multiprocessing import Pool, Process, Value
from integration import *


def integrate_1D_Pool(p, n, function, a, b):
    """ Using Pool and map to perform the Monte-Carlo integration """
    with Pool(processes=p) as pool:
        args = ((n, function, a, b),) * p
        # Copies p-times the given n-tuple. The same as 
        # args = [(n, function, a, b) for _ in range(p)]
        results = pool.starmap(integrate_1D, args)

    average = sum(results) / len(results)
    return average


def plot_1D_duration(processes=range(1, 17), n=1000000, function=f1, a=0, b=2*np.pi):
    def duration(p):
        startTime = time.time()
        result = integrate_1D_Pool(p, n, function, a, b)
        duration = time.time() - startTime
        print(f"I({function.__name__}) = {result} (Doba výpočtu v {p} vláknech: {duration})")
        return duration

    durations = [duration(p) for p in processes]
    
    plt.plot(processes, durations)
    plt.title("Celkový čas výpočtu")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$T [s]$")
    plt.show()

    plt.plot(processes, np.array(durations) / np.array(processes))
    plt.title("Čas výpočtu na vlákno")
    plt.xlabel(r"$p$")
    plt.ylabel(r"$t [s]$")
    plt.show()


def integrate_1D_parallel(result, *args, **kwargs):
    """ Wrapper for function Integrate1D to Process parallelization """
    result.value = integrate_1D(*args, **kwargs)


def integrate_1D_Process(p, n, function, a, b):
    """ Using Process to perform Monte-Carlo integration """
    processes = []
    results = []

    for _ in range(p):
        result = Value('d', 0)
        process = Process(target=integrate_1D_parallel, args=(result, n, function, a, b))
        process.start()
        processes.append(process)
        results.append(result)

    for process in processes:
        process.join()

    results = [result.value for result in results]
    return sum(results) / len(results)


if __name__ == "__main__":
    print(integrate_1D_Pool(8, 100000, f1, 0, 2 * np.pi))
    plot_1D_duration()
    print(integrate_1D_Process(8, 100000, f1, 0, 2 * np.pi))