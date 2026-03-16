import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure()

plt.plot(x, y_sin, linestyle='-', label='y = sin(x)')

plt.plot(x, y_cos, linestyle='--', label='y = cos(x)')

plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ['0', 'π/2', 'π', '3π/2', '2π'])

plt.xlabel('x')
plt.ylabel('y')

plt.title('Plot of sin(x) and cos(x) from 0 to 2π')

plt.legend()

plt.grid(True)

plt.show()