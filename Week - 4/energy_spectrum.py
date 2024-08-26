import numpy as np
from numpy.fft import fft, ifft, fftfreq
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])
N = len(x1)
T = 1 
frequencies = fftfreq(N, T)
X1 = fft(x1, N)
X2 = fft(x2, N)
energy_time = np.sum(np.abs(x1)**2)
energy_freq = np.sum(np.abs(X1)**2) * (T / N) 
print("\nEnergy Spectrum Density Property:")
print(f"Energy in Time Domain = {energy_time}")
print(f"Energy in Frequency Domain = {energy_freq}")
print("Energy spectrum density property holds:", np.isclose(energy_time, energy_freq))
