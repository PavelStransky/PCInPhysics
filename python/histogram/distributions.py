import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

from histogram import histogram
import gaussian

generator = np.random.default_rng()

def plot_histogram(data, title="", distribution_function=None, **kwargs):
    """ Plots data and compares them with theoretic distributionFunction, if specified """
    x, h = histogram(data, **kwargs)

    plt.tight_layout()
    plt.plot(x, h, label="Histogram")
    plt.title(title)
    plt.xlabel(r"$x$")
    plt.ylabel(r"$\rho$")
    plt.ylim(0)

    if distribution_function is not None:
        plt.plot(x, distribution_function(x), label="Hustota pravděpodobnosti")
        plt.legend()

    plt.show()


def uniform(num_values=100000):
    """ Histogram of the uniform distribution """
    data = generator.random(num_values)

    def distribution_function(x):
        return np.where((x >= 0) & (x <= 1), 1, 0)

    plot_histogram(data, r"Rovnoměrné rozdělení na $\langle0,1\rangle$", distribution_function, normalize=True)


def sum_2_uniform(num_values=100000):
    """ Histogram of the sum of two uniform distributions """
    data = generator.random(num_values) + generator.random(num_values)

    def distribution_function(x):
        return np.where(x < 0, 0, np.where(x < 1, x, np.where(x < 2, 2 - x, 0)))

    plot_histogram(data, "Součet dvou rovnoměrně rozdělených čísel", distribution_function, normalize=True)


def sum_m_uniform(m=2, num_values=100000):
    """ Histogram of the sum of n uniform distributions, compared with the Gaussian distribution """
    data = np.zeros(num_values)

    for _ in range(m):
        data += generator.random(num_values)

    def distribution_function(x):
        sigma = np.sqrt(m / 12)
        return gaussian.gaussian_distribution((x - m / 2) / sigma) / sigma

    plot_histogram(data, f"Součet {n} rovnoměrně rozdělených čísel", distribution_function, normalize=True)


def gaussian_generator_clt(num_values=1000000):
    """ Histogram of the sum of 12 uniform distributions, giving quite precisely the Gaussian distribution """
    data = [gaussian.generator_clt() for _ in range(num_values)]

    plot_histogram(data, "Gaussovské rozdělení (Suma 12)", gaussian.gaussian_distribution, normalize=True) 


def gaussian_generator_hm(num_values=1000000):
    """ Histogram of numbers from the Gaussian distribution generated using the hit-and-miss method """
    data = [gaussian.generator_hm() for _ in range(num_values)]

    plot_histogram(data, "Gaussovské rozdělení (Hit-And-Miss)", gaussian.gaussian_distribution, normalize=True) 


def poisson(num_bins=100000, num_values=1000000):
    """ Histogram of the fluctuations in the histogram of uniformly distributed values """
    data = generator.random(num_values)
    h = histogram(data, num_bins=num_bins)[1]

    min_value = 0
    max_value = max(h)

    l = num_values / num_bins
    def distribution_function(x):
        return l**x / gamma(x + 1) * np.exp(-l)

    plot_histogram(h, "Poissonovo rozdělení", distribution_function, normalize=True, min_value=min_value, max_value=max_value, num_bins=int(max_value + 1))


def generator_F(size=1):
    F = generator.random(size=size)
    return np.tan(np.pi / 2 * (2*F - 1))


def cauchy(num_values=100000):
    data = generator_F(num_values)

    def distribution_function(x):
        return 1 / (np.pi * (1 + x**2))

    plot_histogram(data, "Cauchyho rozdělení", distribution_function, normalize=True, min_value=-10, max_value=10, num_bins=500)

uniform()
sum_2_uniform()

sum_m_uniform(3)
sum_m_uniform(4)
sum_m_uniform(20)

gaussian_generator_clt()
gaussian_generator_hm()
poisson()
cauchy()