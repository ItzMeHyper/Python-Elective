import numpy as np
array1 = np.random.randint(0,20,(3,3))

array2 = np.random.randint(0,20,(3,3))

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

array3 = array1 + array2
print("\nSum of two arrays is: ")
print(array3)

print("\nMean")
print(np.mean(array1))

print("\nStandard Deviation")
print(np.std(array1))

scalar = 3
array4 = array1 * scalar
print("\nMultiplication")
print(array4)

array5 = np.dot(array1, array2)
print("\nDot Product")
print(array5)