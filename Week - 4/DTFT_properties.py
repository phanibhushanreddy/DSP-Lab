import numpy as np
from numpy.fft import fft, ifft, fftfreq

# Define the signals
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])
N = len(x1)
T = 1  # Sampling interval (arbitrary)

# Frequency bins for DTFT
frequencies = fftfreq(N, T)

# Compute DTFTs using FFT
X1 = fft(x1, N)
X2 = fft(x2, N)

# Linearity
a = 1
b = 1
x_combined = a * x1 + b * x2
X_combined = fft(x_combined, N)
X_combined_theoretical = a * X1 + b * X2

print("Linearity Property:")
print("DTFT of combined signal:", X_combined)
print("Theoretical DTFT of combined signal:", X_combined_theoretical)
print("Linearity holds:", np.allclose(X_combined, X_combined_theoretical))

# Convolution
x1_convolution = np.convolve(x1, x2, mode='full')
X1_convolution = fft(x1_convolution, len(x1_convolution))  # Length of convolution

print("\nConvolution Property:")
# Compute DTFT of convolution directly
X1_convolution_theoretical = fft(x1, N) * fft(x2, N)
# Zero padding to match length
X1_convolution_theoretical = np.concatenate([X1_convolution_theoretical, np.zeros(len(x1_convolution) - len(X1_convolution_theoretical))])
print("DTFT of convolution:", X1_convolution)
print("Theoretical DTFT of convolution:", X1_convolution_theoretical)
print("Convolution property holds:", np.allclose(X1_convolution, X1_convolution_theoretical))

# Time Shifting
n_shift = 1
x1_shifted = np.roll(x1, n_shift)
X1_shifted = fft(x1_shifted, N)

print("\nTime Shifting Property:")
# Phase shift calculation
phase_shift = np.exp(-1j * 2 * np.pi * frequencies * n_shift / N)
print("DTFT of shifted x1:", X1_shifted)
print("Expected DTFT with phase shift:", phase_shift * X1)
print("Time shifting property holds:", np.allclose(X1_shifted, phase_shift * X1))

# Energy Spectrum Density
energy_time = np.sum(np.abs(x1)**2)
energy_freq = np.sum(np.abs(X1)**2) * (T / N)  # Energy in frequency domain using Parseval's theorem

print("\nEnergy Spectrum Density Property:")
print(f"Energy in Time Domain = {energy_time}")
print(f"Energy in Frequency Domain = {energy_freq}")
print("Energy spectrum density property holds:", np.isclose(energy_time, energy_freq))
