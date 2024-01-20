import numpy as np
import matplotlib.pyplot as plt

# Define the function
def my_function(n):
    if n >= 0:
        return 63 + 2 * n
    else:
        return 0

def my_function2(n):
    if n >= 0:
        return 3 + 7 * n
    else:
        return 0

# Generate x values using linspace
x_values = np.linspace(-14, 14, 29)  # 29 points from -14 to 14

# Generate y values using the function
y_values = [my_function(n) for n in x_values]
z_values = [my_function2(n) for n in x_values]

# Generate a list of colors for each stem
colors = ['r' if n != 12 else 'g' for n in x_values]

# Stem plot for the first function
plt.stem(x_values, y_values, linefmt='-', markerfmt='ro', basefmt='-', label='x_1(n)')

# Stem plot for the second function
plt.stem(x_values, z_values, linefmt='-', markerfmt='bo', basefmt='-', label='x_2(n)')

# Highlight the point at n=12 with a different color
plt.stem(12, my_function(12), linefmt='-', markerfmt='go', basefmt='-', label='n=12')

plt.xlabel('n')
plt.legend()
plt.grid(True)
plt.show()

