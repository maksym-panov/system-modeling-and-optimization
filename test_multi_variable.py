from math import *
import numpy as np
import multi_var_algorithms as under_test
from colorama import Fore, Style

F = lambda x: [
    sin(x[0]) + 2*x[1] - 2,
    cos(x[0]) + x[1] - 1.5
]

f = lambda x: np.array([
    [cos(x[0]), 2],
    [-sin(x[0]), 1]
])

ƒ = lambda x: [
    x[0] * (sin(x[0]) + 2 * x[1]) / 2,
    1.5 - cos(x[0])
]

_ƒ = lambda x: [
    [0.5 * (sin(x[0]) + x[0] * cos(x[0])) + x[1], x[0]],
    [sin(x[0]), 0]
]

def newtons_method_test():
    print(Fore.BLUE + "Testing Newton's method" + Style.RESET_ALL)
    result = under_test.newtons_method(F, f, [0, 0], .00001)
    print(Fore.LIGHTGREEN_EX + "Newton's method with starting estimation [0, 0] returned:", result)
    print("Values of F(x1) and F(x2):", F(result))

def iterative_method_test():
    print(Fore.BLUE + "Testing Iterative method" + Style.RESET_ALL)
    under_test.iterative_method(F, ƒ, _ƒ, [0.5, 0.5], .00001)

def sqrt_minimization_method_test():
    print(Fore.BLUE + "Testing Sqrt minimization method" + Style.RESET_ALL)
    result = under_test.sqrt_minimization_method(F, [0, 0])
    print(Fore.LIGHTGREEN_EX + "Sqrt minimization method with starting estimation [0, 0] returned:", result)
    print("Values of F(x1) and F(x2):", F(result))

newtons_method_test()
iterative_method_test()
sqrt_minimization_method_test()
 
