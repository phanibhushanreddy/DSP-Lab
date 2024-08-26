from scipy.io import wavfile
import numpy as np
fs, x = wavfile.read('/home/apiiit123/Desktop/Week - 1/n.wav')
def upsampling(x1, a):
    if a > 1:
        y = np.zeros((len(x1) * a, x1.shape[1])) 
        y[::a] = x1
        wavfile.write('n.wav', fs, y)
a = float(input("Enter upsampling factor: "))
upsampling(x, a)
