'''Write a Python program to find the roots of a quadratic equation, ax2 + bx + c = 0 .
   Consider the cases of both real and imaginary roots.'''

import cmath

# Read coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Calculate the roots
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

# Display the results
print("The roots of the equation are:")
print("Root 1:", root1)
print("Root 2:", root2)
