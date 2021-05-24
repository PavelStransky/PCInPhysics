import numpy as np

def discrete_fourier_transform(signal):
    """ Discrete Fourier Transform """
    N = len(signal)

    argument = -2j * np.pi / N * np.arange(N)
    """ Temporary array with exponents for the exponential 
        - uses more memory, but makes the calculation much faster
    """

    H = np.array([sum(signal * np.exp(k * argument)) for k in range(N)]) / N
    return H


def inverse_discrete_fourier_transform(signal):
    """ Inverse Discrete Fourier Transform """
    N = len(signal)

    argument = 2j * np.pi / N * np.arange(N)
    h = np.array([sum(signal * np.exp(k * argument)) for k in range(N)])
    return h


def amplitude_spectrum(components, fs=1):
    """ Spectrum of Fourier amplitudes.

        Arguments:
        fs - Sampling frequency
    """
    N = len(components)
    power_spectrum = 2 * np.abs(components)
    power_spectrum[0] = 0.5 * power_spectrum[0]       # DC term is there just once
    return np.linspace(0, fs // 2, N // 2), power_spectrum[0:(N // 2)]