import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 100)
y = np.sin(2 * x)
y1 = 2 * np.sin(x)
y2 = np.sin(x)

plt.plot(x, y2, 'blue', linestyle="-", label="sin(x)")
plt.plot(x, y1, 'red', linestyle=":", label="2sin(x)")
plt.plot(x, y, 'green', linestyle="--", label="sin(2x)")
plt.legend(title='Wykres')
plt.show()
