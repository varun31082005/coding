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

# Generate x values (integers)
x_values = np.arange(-10, 11, 1)

# Generate y values using the function
y_values = [my_function(n) for n in x_values]
z_values = [my_function2(n) for n in x_values]

# Stem plot for the first function (red)
plt.stem(x_values, y_values, linefmt='r-', markerfmt='ro', basefmt='r-', label='x(n)')

# Stem plot for the second function (blue)
plt.stem(x_values, z_values, linefmt='b-', markerfmt='bo', basefmt='b-', label='y(n)')

plt.xlabel('n')
plt.legend()
plt.grid(True)
plt.show()

