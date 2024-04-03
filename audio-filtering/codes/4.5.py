import numpy as np
import matplotlib.pyplot as plt

# Define impulse response
n = np.arange(14)
hn = (-1/2)**n
hn_padded_left = np.pad(hn, (0, 2), 'constant', constant_values=(0))
hn_padded_right = np.pad(hn, (2, 0), 'constant', constant_values=(0))
h = hn_padded_left + hn_padded_right

# Define input signal
x = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])

# Perform convolution
nh = len(h)
nx = len(x)
y = np.zeros(nx + nh - 1)

for k in range(0, nx + nh - 1):
    for n in range(0, nx):
        if k - n >= 0 and k - n < nh:
            y[k] += x[n] * h[k - n]

# Plot the result
plt.stem(range(0, nx + nh - 1), y)
plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.savefig('y_conv.png')

