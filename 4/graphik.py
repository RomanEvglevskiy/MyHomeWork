import matplotlib.pyplot as plt
import numpy as np
ax = plt.subplot()
x = np.linspace(-5, 5, 100)
y = x ** 2 + 2 * x +1
ax.plot(x, y)
plt.show()
