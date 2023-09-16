import algorithm as alg
import numpy as np

test_vector = np.random.normal(loc = 5.5, scale = 1.5, size = 500)
alg.buildRelativeFrequenciesPolygon(test_vector)

test_vector = np.random.normal(loc = 5.5, scale = 1.5, size = 1000)
alg.buildRelativeFrequenciesPolygon(test_vector)

test_vector = np.random.normal(loc = 5.5, scale = 1.5, size = 2000)
alg.buildRelativeFrequenciesPolygon(test_vector)

test_vector = np.random.normal(loc = 5.5, scale = 1.5, size = 5000)
alg.buildRelativeFrequenciesPolygon(test_vector)

test_vector = np.random.normal(loc = 5.5, scale = 1.5, size = 10000)
alg.buildRelativeFrequenciesPolygon(test_vector)