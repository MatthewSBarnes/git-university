#"""Compute the discrete Fourier Transform of the 1D array x"""
import numpy as np

N = 200                         # sampling rate
T = 1.0/N                      # sampling interval
t = np.arange(0,1,T)            # time vector
ff = 20                          # frequency of the signal



def trigen(n, amp):
    y = 0
    x = 0
    # s = amp / (n/4)
    s = amp / (n/8)
    while x < n:
        yield y
        y += s
        if abs(y) > amp:
            y = 0
        x += 1

y = np.fromiter(trigen(N, 1), "d")	

#x= t
x= t*8

yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2) # N, T ? 

import matplotlib.pyplot as plt
plt.subplot(2,1,1)
plt.plot(x, y, 'k-')
#plt.grid()
#plt.show()
plt.subplot(2,1,2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]), 'r-')
plt.grid()
plt.show()

