import numpy as np
from numpy.fft import fft, ifft, fftfreq
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])
N = len(x1)
T = 1 
frequencies = fftfreq(N, T)
X1 = fft(x1, N)
X2 = fft(x2, N)
a = 1
b = 1
x_combined = a * x1 + b * x2
X_combined = fft(x_combined, N)
X_combined_theoretical = a * X1 + b * X2
print("Linearity Property:")
print("DTFT of combined signal:", X_combined)
print("Theoretical DTFT of combined signal:", X_combined_theoretical)
print("Linearity holds:", np.allclose(X_combined, X_combined_theoretical))
