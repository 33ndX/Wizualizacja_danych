import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i) * flip)

#sns.set_style("whitegrid")
#sns.set_palette("husl")
sinplot()
# print(sns.axes_style())
# plt.show()

x = np.linspace(-2, 2, 400)
x_positive = np.linspace(0, 2, 400)

y1 = x
y2 = x**2
y3 = x**3
y4 = np.sqrt(x_positive)
y5 = np.cbrt(x_positive)

plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='y = x')
plt.plot(x, y2, label='y = x^2')
plt.plot(x, y3, label='y = x^3')
plt.plot(x_positive, y4, label='y = sqrt(x)')
plt.plot(x_positive, y5, label='y = cbrt(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Wykresy funkcji x, x^2, x^3, sqrt(x), cbrt(x)')
plt.grid(True)
plt.show()