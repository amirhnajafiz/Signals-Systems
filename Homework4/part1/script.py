import matplotlib.pyplot as plt
import numpy as np


T0 = 0.4
FC = 250

FS = 1000
TS = 0.0001

# Signal 
def input_signal(t):
    if t >= 0 and t <= T0:
        return np.sinc(100 * t)
    else:
        return 0

# Fourier transform with frequence bandwidth
def f_transform(x, fs, m):
    sig = np.fft.fft(x, m)
    shift_fft = np.abs(np.fft.fftshift(sig))
    frequence = np.linspace(-fs / 2, fs / 2, m)
    return (frequence, shift_fft)

# Carrier
def c(t):
    return np.cos(2 * np.pi * FC * t)

# DSB-AM signal
def modulate(t):
    return input_signal(t) * c(t)

def lowpassfilter(t):
    temp = []
    for x in t:
        if x >= -100 and t < 100:
            temp.append(x)
        else:
            temp.append(0)
    return temp

# Demodulation
def demodule(t):
    temp = [c(x) for x in t]
    temp = np.fft.fft(temp)
    temp = lowpassfilter(temp)
    temp = np.fft.ifft(temp)
    return temp


# Time 
time = np.linspace(0, TS, FS)

# System of input signal
y1 = [input_signal(x) for x in time]
# FT


# System of modulated signal
y2 = [modulate(x) for x in time]
# FT

fig, s1 = plt.subplots(3)
s1[0].plot(time, y1)
s1[1].plot(time, y2)
s1[2].plot(time, demodule(y2))

plt.show()