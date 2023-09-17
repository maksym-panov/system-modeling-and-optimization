import numpy as np
import pandas as pd
import math

# 1.2.1
a = np.array([1, 2, 3, 4, 5])
print(a)

print(np.append(np.array([1, 2, 3, 4, 5]), 6))
print(np.append(np.array([1, 2]), np.array([3, 4])))

print(np.arange(0, 1 + 0.1, 0.1))

x = np.array([0, math.pi / 2, math.pi])
print(np.sin(x))

# 1.2.3
print(np.reshape((1, 2, 3, 4, 5, 6), (2, 3), order = "F"))
print(np.reshape((1, 1, 1, 1), (2, 2)))
print(np.reshape((1, 2, 1, 2, 1, 2), (3, 2), order = "F"))
print(np.reshape((1, 2, 3, 4, 5, 6), (2, 3)))

column_names = ["length", "width"]
row_names = ["petal", "sepal"]

matrix = np.reshape((23, 31, 58, 16), (2, 2), order = "F")
df = pd.DataFrame(matrix, columns = column_names, index = row_names);
print(df)

A = np.reshape([i for i in range(1, 7)], (2, 3), order = "F")
print(A)

B = A.transpose()
print(B)

print(A.dot(B))
print(B.dot(A))

A = np.reshape([i for i in range(1, 5)], (2, 2), order = "F")
b = np.array([5, 8])

print(np.linalg.solve(A, b))
print(np.linalg.det(A))
print(np.linalg.inv(A))