import numpy as np
import matplotlib.pyplot as plt

# 11111111111111111111111111111111111111

x = np.linspace(-10, 10, 400)
y = 1 / (1 + x**2)

plt.plot(x, y, label='y = 1 / (1 + x^2)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres funkcji y = 1 / (1 + x^2)')
plt.grid(True)
plt.show()

#2222222222222222222222222222222222222222

import numpy as np
import matplotlib.pyplot as plt

# Przedział [0, 3]
x1 = np.linspace(0, 3, 400)
y1_1 = x1**2
y1_2 = np.exp(x1)
y1_3 = np.power(x1, x1)

plt.plot(x1, y1_1, label='y = x^2 (0-3)')
plt.plot(x1, y1_2, label='y = e^x (0-3)')
plt.plot(x1, y1_3, label='y = x^x (0-3)')

# Przedział [0, 4]
x2 = np.linspace(0, 4, 400)
y2_1 = x2**2
y2_2 = np.exp(x2)
y2_3 = np.power(x2, x2)

plt.plot(x2, y2_1, linestyle='--', label='y = x^2 (0-4)')
plt.plot(x2, y2_2, linestyle='--', label='y = e^x (0-4)')
plt.plot(x2, y2_3, linestyle='--', label='y = x^x (0-4)')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykresy funkcji w różnych przedziałach')
plt.grid(True)
plt.show()

#3333333333333333333333333333333333333333333333333

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 400)
y1 = x**2
y2 = np.exp(x)
y3 = np.power(x, x)

fig, axs = plt.subplots(3, 1, figsize=(6, 12))

axs[0].plot(x, y1)
axs[0].set_title('y = x^2')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].grid(True)

axs[1].plot(x, y2)
axs[1].set_title('y = e^x')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].grid(True)

axs[2].plot(x, y3)
axs[2].set_title('y = x^x')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].grid(True)

plt.tight_layout()
plt.show()
