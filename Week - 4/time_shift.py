import numpy as np
from numpy.fft import fft, ifft, fftfreq
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])
N = len(x1)
T = 1 
frequencies = fftfreq(N, T)
X1 = fft(x1, N)
X2 = fft(x2, N)
n_shift = 1
x1_shifted = np.roll(x1, n_shift)
X1_shifted = fft(x1_shifted, N)
print("\nTime Shifting Property:")
phase_shift = np.exp(-1j * 2 * np.pi * frequencies * n_shift / N)
print("DTFT of shifted x1:", X1_shifted)
print("Expected DTFT with phase shift:", phase_shift * X1)
print("Time shifting property holds:", np.allclose(X1_shifted, phase_shift * X1))