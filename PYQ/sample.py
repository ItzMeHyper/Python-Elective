import numpy as np

arr2d = np.array([[10, 20, 30],
                  [40, 50, 60],     
                  [70, 80, 90]])

result = arr2d[:, ::2]

print(result)