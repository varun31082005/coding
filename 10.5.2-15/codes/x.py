import numpy as np
import matplotlib.pyplot as plt

def ap(a, d, start, end):
    n_values = np.arange(start, end + 1)
    return np.where(n_values >= 0, a + d * n_values, 0)

# Generate x values using linspace
x_values = np.linspace(-14, 14, 29)  # 29 points from -14 to 14

y_values = ap(63, 2, x_values[0], x_values[-1])

z_values = ap(3, 7, x_values[0], x_values[-1])

colors = ['r' if n != 12 else 'g' for n in x_values]

# Stem plot for the first function
plt.stem(x_values, y_values, linefmt='-', markerfmt='ro', basefmt='-', label='x_1(n)')

# Stem plot for the second function
plt.stem(x_values, z_values, linefmt='-', markerfmt='bo', basefmt='-', label='x_2(n)')

# Highlight the point at n=12 with a different color
plt.stem(12, ap(63, 2, 12, 12)[0], linefmt='-', markerfmt='go', basefmt='-', label='n=12')

plt.xlabel('n')
plt.legend()
plt.grid(True)
plt.show()

