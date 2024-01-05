import numpy as np
import matplotlib.pyplot as plt

# Define the function
def my_function(n):
    if n > 0:
        return 61 + 2 * n
    else:
        return 0

# Generate x values (integers)
x_values = np.arange(-10, 11, 1)

# Generate y values using the function
y_values = [my_function(n) for n in x_values]
# Plot the graph
plt.plot(x_values, y_values, marker='o', linestyle='-', color='r')
plt.xlabel('n')
plt.ylabel('61f(n-1) + 2nf(n-1)')
plt.grid(True)
plt.figtext(0.5, 0.01, 'Figure: Plot of x(n) = 61f(n-1) + 2nf(n-1)', ha='center', va='center')
plt.show()


