import algorithm as alg
import numpy as np

A = [
  [4.75, .49, .07, .33], 
  [.24, 5.68, .63, .74], 
  [.46, .98, 7.08, .92],
  [.53, .55, .76, 9.13]
]
b = [-14.3, 10.07, 8.53, 9.99]

print("Gauss (direct) method: ", alg.gauss(A, b))
print("Jakobi (iterative) method: ", alg.jakobi(A, b, 0.00001, 10000))
print("Numpy standard solution: ", np.linalg.solve(A, b))