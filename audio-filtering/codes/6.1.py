import soundfile as sf
from scipy import signal
import numpy as np
from scipy.fft import fft, ifft
from numpy.polynomial import Polynomial as P
from matplotlib import pyplot as plt

def myfiltfilt(b, a, input_signal):
    X = fft(input_signal)
    w = np.linspace(0, 1, len(X) + 1)
    W = np.exp(2j * np.pi * w[:-1])
    B = (np.absolute(np.polyval(b, W))) ** 2
    A = (np.absolute(np.polyval(a, W))) ** 2
    Y = B * (1 / A) * X
    return ifft(Y).real

# Read .wav file
input_signal, fs = sf.read('varun_singing.wav')

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4

# Cutoff frequency
cutoff_freq = 4000.0

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low')

# Print coefficients
print("Coefficients of b:", b)
print("Coefficients of a:", a)

# Filter the input signal with Butterworth filter
output_signal = signal.filtfilt(b, a, input_signal)

op1 = myfiltfilt(b, a, input_signal)
x_plt = np.arange(len(input_signal))

# Verify outputs by plotting
plt.plot(x_plt[1000:10000], output_signal[1000:10000], 'b.', label='Output by built-in function')
plt.plot(x_plt[1000:10000], op1[1000:10000], 'r.', label='Output by custom function')
plt.title("Verification of outputs of Audio Filter")
plt.grid()
plt.legend()
plt.savefig("Audio_Filter_verification.png")

