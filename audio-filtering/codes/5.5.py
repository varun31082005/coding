import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

N = 14
n_vals = np.arange(N)
fn = (-1/2)**n_vals
hn1 = np.pad(fn, (0, 2), 'constant', constant_values=(0, 0))
hn2 = np.pad(fn, (2, 0), 'constant', constant_values=(0, 0))
h = hn1 + hn2
x_temp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(x_temp, (0, 10), 'constant', constant_values=(0))
dft_matrix = fft(np.eye(len(x)))
X = x @ dft_matrix
H = h @ dft_matrix
Y = H * X
inv_matrix = np.linalg.inv(dft_matrix)
y = (Y @ inv_matrix).real

# Plotting
plt.stem(range(0, 16), y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.title('Filter Output Using DFT Matrix Multiplication')
plt.grid()
plt.savefig('filter_output_dft_matrix.png')

