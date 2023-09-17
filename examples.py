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