import numpy as np;
from itertools import chain;
import copy;

def gauss(param_A, param_b):
  n = len(param_A[0])
  A = copy.deepcopy(param_A)
  b = copy.deepcopy(param_b)

  for k in range(0, n - 1): 
    for j in range(k + 1, n):
      A[k][j] /= A[k][k]
    b[k] /= A[k][k]
    for i in range(k + 1, n):
      for j in range(k + 1, n):
        A[i][j] -= A[i][k] * A[k][j]
      b[i]= b[i] - A[i][k] * b[k]
  b[n - 1] /= A[n - 1][n - 1]
  for k in range(n - 2, -1, -1):
    for j in range(k + 1, n):
      b[k] -= A[k][j] * b[j]
  return b

def jakobi(A, b, e, max_iter): 
  n = len(A)
  C = np.reshape(list(chain.from_iterable(A)), (n, n))
  d = np.array(b)
  for i in range(0, n):
    for j in range(0, n):
      C[i][j] /= -A[i][i]
    C[i][i] = 0
  for i in range(0, n):
    d[i] /= A[i][i]

  return iter_method(C, d, e, max_iter)

def iter_method(C, d, e, max_iter):
  previous_estim = d
  for _ in range(max_iter):
    current_estim = np.dot(C, previous_estim) + d
    if abs(np.linalg.norm(current_estim - previous_estim)) <= e:
      break
    previous_estim = current_estim
  return current_estim
