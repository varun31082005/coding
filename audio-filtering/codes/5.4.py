import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

N = 14
n = np.arange(N)
fn = (-1/2)**n
hn1 = np.pad(fn, (0, 2), 'constant', constant_values=(0))
hn2 = np.pad(fn, (2, 0), 'constant', constant_values=(0))
h = hn1 + hn2

xtemp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(xtemp, (0, 10), 'constant', constant_values=(0))

X = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * n * k / N)
        
H = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        H[k] += h[n] * np.exp(-1j * 2 * np.pi * n * k / N)

Y = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
    Y[k] = X[k] * H[k]

y = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
    for n in range(0, N):
        y[k] += Y[n] * np.exp(1j * 2 * np.pi * n * k / N)

y = np.real(y) / N

# Plotting y(n) by DFT
plt.stem(range(0, N), y, markerfmt='C0o')
plt.title("Filter Output (y(n)) using DFT")
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

# Compute using FFT and plot
X_fft = fft(x)
H_fft = fft(h)
Y_fft = H_fft * X_fft
y_ifft = ifft(Y_fft).real

# Plotting from IFFT
plt.stem(range(0, N), y_ifft[:N], markerfmt='C2o')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.legend(['Computed using DFT',  'Computed using FFT'])
plt.savefig('filter_output_comparison.png')

