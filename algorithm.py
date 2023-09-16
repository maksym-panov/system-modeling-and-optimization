import matplotlib.pyplot as plt
import math

def buildRelativeFrequenciesPolygon(vector):
  vector = sorted(vector)
  x = evalArgumentsVector(vector)
  y = evalRelativeFreqsVector(vector)

  plt.plot(x, y, "ko")
  plt.title("Relative frequencies polygon")
  plt.xlabel("Random variable value")
  plt.ylabel("Relative frequency")
  plt.show()

def evalArgumentsVector(vector):
  [_, k, inter] = evalNumericParams(vector)
  min = vector[0]
  return [( (min + inter * i) + (min + inter * (i + 1)) ) / 2 for i in range(k)]

def evalRelativeFreqsVector(vector): 
  [_, k, inter] = evalNumericParams(vector) 
  return [relFreqOnInterval(vector, inter, i) for i in range(k)]

def relFreqOnInterval(vector, inter, i):
  left = vector[0] + inter * i
  right = left + inter
  count = 0
  for el in vector:
    if (left <= el <= right): 
      count += 1
  return count / len(vector)

def evalNumericParams(vector):
  l = len(vector)
  k = math.ceil(l / 10)
  inter = (vector[l - 1] - vector[0]) / k
  return [l, k, inter]
