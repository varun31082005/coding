import numpy as np
import matplotlib.pyplot as plt

# Define the function
def my_function(n):
    if n > 0:
        return -4 + 7 * n
    else:
        return 0

# Generate x values (integers)
x_values = np.arange(-10, 11, 1)

# Generate y values using the function
y_values = [my_function(n) for n in x_values]
# Plot the graph
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.xlabel('n')
plt.ylabel('-4 + 7n')
plt.grid(True)
plt.figtext(0.5, 0.01, 'Figure: Plot of y(n) = -4 + 7n', ha='center', va='center')
plt.show()


