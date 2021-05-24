import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm           # Colour maps for the contour graph

import time

import sound
from transform import *


def test_signal(N=2000, fs=2000):
    """ Task 12.3 """
    x = np.linspace(0, N / fs, N, endpoint=False)

    """ Test signal """
    y = 0.1 * np.sin(440 * 2 * np.pi * x) + 0.2 * np.sin(5 / 4 * 440 * 2 * np.pi * x) + 0.3 * np.sin(3 / 2 * 440 * 2 * np.pi * x)
    sound.Play(y, fs)

    plt.plot(x, y)
    plt.xlabel("$t$ [s]")
    plt.ylabel("$y$")
    plt.figure()

    ft = discrete_fourier_transform(y)
    plt.plot(*amplitude_spectrum(ft, fs))
    plt.title(f"$f_s={fs}$ Hz")
    plt.xlabel("$f$ [Hz]")
    plt.ylabel("$A$")
    plt.show()
    

def vowels(part):
    """ Task 12.4 """
    path = r"../../sounds/"
    files = ["a.wav", "e.wav", "i.wav", "o.wav", "u.wav"]

    for file in files:
        signal, fs = sound.Read(path + file)
        sound.Play(signal, fs)

        signal = signal[part]

        ft = discrete_fourier_transform(signal)
        plt.plot(*amplitude_spectrum(ft, fs), label=file)

    plt.xlim(0, 2000)       # Just the lowest part of the spectrum (it contains the important frequencies)
    plt.xlabel("$f$ [Hz]")
    plt.ylabel("$A$")
    plt.legend()
    plt.show()


def FT_methodsa_comparison():
    """ Task 9.6 """
    file = r"../../sounds/a.wav"

    signal, fs = sound.Read(file)
    sound.Play(signal, fs)

    signal = signal[3000:5000]
    N = len(signal)

    ft1 = discrete_fourier_transform(signal)
    plt.plot(*amplitude_spectrum(ft1, fs), label="FourierTransform")

    ft2 = np.fft.fft(signal) / N
    plt.plot(*amplitude_spectrum(ft2, fs), label="numpy.fft.fft")

    plt.xlabel("$f$ [Hz]")
    plt.ylabel("$A$")
    plt.legend()
    plt.show()


def black_holes(windowSize=2000, step=100):
    """ Task 9.5 """
    file = r"../../sounds/BlackHolesCollision.wav"
    signal, fs = sound.Read(file)
    sound.Play(signal, fs)

    signal = signal[:, 0]      # The input signal has two channels (amplitude and time) - we'll need just the amplitude
    N = len(signal)
    
    X, Y, Z = [], [], []    # For the contour plot 

    i = 0                   # Index of the window beginning

    while i + windowSize < N:
        window = signal[i:(i + windowSize)]
        
        ft = np.fft.fft(window) / windowSize
        #ft = FourierTransform(window)
        
        frequencies, amplitudes = amplitude_spectrum(ft, fs)
        X.append(np.linspace(i / fs, i / fs, windowSize // 2))
        Y.append(frequencies)
        Z.append(amplitudes)
        i += step

    plt.contourf(np.array(X), np.array(Y), np.array(Z), cmap=cm.hot)
    plt.xlabel("$t$ [s]")
    plt.ylabel("$f$ [Hz]")
    plt.colorbar()
    plt.ylim(0, 500)
    plt.show()

test_signal(2000, 2000)
test_signal(2000, 1842)
test_signal(1000, 1000)
vowels(slice(3000, 5000))
black_holes()
FT_methodsa_comparison()
