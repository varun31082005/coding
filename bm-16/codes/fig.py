

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt", skiprows=0)
omega_values, result_values= data[:, 0], data[:, 1]

plt.figure(figsize=(8, 6))
plt.plot(omega_values, result_values, label=r"$\frac{1}{\sqrt{1 + (\omega RC)^2}}$")
plt.xlabel(r"Angular Frequency $\omega$")
plt.ylabel("$|H(j\omega)|$")
plt.title("$|H(j\omega)|$ vs. Angular Frequency")
plt.grid(True)
plt.legend()
plt.show()
