import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 10.0, 1000)
y = np.random.normal(5.0, 1.0, 10000)

plt.hist(y, 100)
plt.show()
plt.hist(x, 100)
plt.show()