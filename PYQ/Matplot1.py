import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π
x = np.linspace(0, 2*np.pi, 100)

# Compute y values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the functions
plt.plot(x, y_sin, label="sin(x)", linestyle='-')   # solid line
plt.plot(x, y_cos, label="cos(x)", linestyle='--')  # dashed line

# Customize ticks
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])
plt.yticks([-1, -0.5, 0, 0.5, 1])

# Labels and title
plt.xlabel("x values")
plt.ylabel("Function values")
plt.title("Sine and Cosine Functions")

# Legend
plt.legend()

# Grid (optional but useful)
plt.grid()

# Show plot
plt.show()