import matplotlib.pyplot as plt
import math

# Receives a vector of random variable values 
# divides them into intervals of equal size
# and draws a relative frequencies polygon
def buildRelativeFrequenciesPolygon(vector):
  vector = sorted(vector)
  x = evalArgumentsVector(vector)
  y = evalRelativeFreqsVector(vector)
  plt.plot(x, y, "ko")
  plt.title("Relative frequencies polygon")
  plt.xlabel("Random variable value")
  plt.ylabel("Relative frequency")
  plt.show()

# Returns a list of midpoints of the intervals
def evalArgumentsVector(vector):
  [_, k, inter] = evalNumericParams(vector)
  min = vector[0]
  return [( (min + inter * i) + (min + inter * (i + 1)) ) / 2 for i in range(k)]

# Returns a list of frequencies for each interval
def evalRelativeFreqsVector(vector): 
  [_, k, inter] = evalNumericParams(vector) 
  return [relFreqOnInterval(vector, inter, i) for i in range(k)]

# Helper function that evaluates a 
# frequency for a specific interval
def relFreqOnInterval(vector, inter, i):
  left = vector[0] + inter * i
  right = left + inter
  count = 0
  for el in vector:
    if (left <= el <= right): 
      count += 1
  return count / len(vector)

# Returns list of vector lenght, 
# k parameter and interval length
def evalNumericParams(vector):
  l = len(vector)
  k = math.ceil(l / 10)
  inter = (vector[l - 1] - vector[0]) / k
  return [l, k, inter]
