
from scipy.io import wavfile

fs, x = wavfile.read('/home/apiiit123/Desktop/Week - 1/n.wav')


def sampling(x, a):
    if a > 1:
        y=x[::a]
        wavfile.write('n.wav',fs,y)


a=int(input("Enter sampling factor:"))
sampling(x, a)
