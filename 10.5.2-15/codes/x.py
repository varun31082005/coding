import numpy as np
import matplotlib.pyplot as plt

# Generate x values using linspace
x_values = np.linspace(0, 14, 15)  # 29 points from -14 to 14

y_values = np.where(x_values >= 0, 63 + 2 * x_values, 0)

z_values = np.where(x_values >= 0, 3 + 7 * x_values, 0)


# Plot the stem plots
plt.stem(x_values, y_values, linefmt='-', markerfmt='ro', basefmt='-', label='x_1(n)')
plt.stem(x_values, z_values, linefmt='-', markerfmt='bo', basefmt='-', label='x_2(n)')
plt.stem(12, 87, linefmt='-', markerfmt='go', basefmt='-', label='n=12')

# Set labels and legend
plt.xlabel('n')
plt.legend()
plt.grid(True)
plt.show()

