import numpy as np
import matplotlib.pyplot as plt

import time

generator = np.random.default_rng()

def gaussian_distribution(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)


def generator_clt():
    """ Central Limit Theorem - sum of 6 uniformly distributed values """
    gaussian_number = sum(generator.random(12)) - 6
    return gaussian_number


def generator_hm():
    """ Hit-and-miss method in a rectangle [-6,6]x[0, 1/sqrt(2 pi) ~ 0.4] """
    while True:
        x = 12 * generator.random() - 6
        y = 0.4 * generator.random()
        if y < gaussian_distribution(x):
            return x


def execution_time_comparison(numValues=1000000):
    startTime = time.time()

    for _ in range(numValues):
        generator.normal()
    endTime = time.time()
    print(f"Numpy normal routine: {endTime - startTime}s")

    startTime = time.time()
    for _ in range(numValues):
        generator_clt()
    endTime = time.time()
    print(f"Generator using Central Limit Theorem: {endTime - startTime}s")

    startTime = time.time()
    for _ in range(numValues):
        generator_hm()
    endTime = time.time()
    print(f"Generator using Hit-and-miss: {endTime - startTime}s")

if __name__ == "__main__":
    execution_time_comparison()