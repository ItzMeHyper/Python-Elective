import numpy as np

# Create two 3x3 matrices with random integers from 0 to 20
A = np.random.randint(0, 21, (3, 3))
B = np.random.randint(0, 21, (3, 3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
add = A + B
print("\nAddition (A + B):")
print(add)

# Matrix Multiplication
mul = np.dot(A, B)
print("\nMultiplication (A * B):")
print(mul)

# Transpose of the product matrix
transpose = mul.T
print("\nTranspose of Product Matrix:")
print(transpose)

# Element-wise Division (handle division by zero)
division = np.divide(A, B, where=B!=0)
print("\nDivision (A / B):")
print(division)

# Subtraction
sub = A - B
print("\nSubtraction (A - B):")
print(sub)