#"""Compute the discrete Fourier Transform of the 1D array x"""
import numpy as np

# Number of sample points
N = 600
# sample spacing
T = 1.0 / N
x = np.linspace(0.0, N*T, N)
nPulse = 20
y = np.ones(nPulse)
y = np.append(y, np.zeros(N-nPulse))

yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.grid()
plt.show()

plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.grid()
plt.show()

