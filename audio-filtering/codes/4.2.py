import numpy as np
import matplotlib.pyplot as plt

n = np.arange(10)
fn = (-1/2)**n

hn1 = np.pad(fn, (0, 2), 'constant', constant_values=(0))
hn2 = np.pad(fn, (2, 0), 'constant', constant_values=(0))
combined_hn = hn1 + hn2  # Add the arrays element-wise

plt.stem(np.arange(12), combined_hn)
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()

plt.savefig('h_n.png')

