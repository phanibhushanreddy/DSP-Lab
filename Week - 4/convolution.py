import numpy as np
from numpy.fft import fft, ifft, fftfreq
x1 = np.array([1,0])
x2 = np.array([0,1])
N = len(x1)
T = 1 
frequencies = fftfreq(N, T)
X1 = fft(x1, N)
X2 = fft(x2, N)
x1_convolution = np.convolve(x1, x2, mode='full')
X1_convolution = fft(x1_convolution, len(x1_convolution))

print("Convolution Property:")
X1_convolution_theoretical = fft(x1, N) * fft(x2, N)
X1_convolution_theoretical = np.concatenate([X1_convolution_theoretical, np.zeros(len(x1_convolution) - len(X1_convolution_theoretical))])
print("DTFT of convolution:", X1_convolution)
print("Theoretical DTFT of convolution:", X1_convolution_theoretical)
print("Convolution property holds:", np.allclose(X1_convolution, X1_convolution_theoretical))
