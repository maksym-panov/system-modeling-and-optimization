import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import one_var_algorithms as under_test
from colorama import Fore, Style

F = lambda x: x**2 - np.exp(-x**2)
f = lambda x: 2*x + 2*x * np.exp(-x**2)
_f = lambda x: 2 - (4 * x**2 - 2) * np.exp(-x**2)

ƒ = lambda x: np.exp(-x**2) / x
_ƒ = lambda x: -(2 * x**2 + 1) * np.exp(-x**2) / x**2

def draw():
    a = -3
    b = 3
    n = 200

    x = np.linspace(a, b, n)
    y = [F(_x) for _x in x]

    plt.plot(x, y)
    plt.axhline(0, color = "k")
    plt.axvline(0, color = "k")

    plt.show()

def library_solution_test():
    print(Fore.BLUE + "Testing scipy library solutions")
    # Interval [-10, 0]
    a = -10
    b = 0
    neg_int_solution = fsolve(F, (a + b) / 2)
    # Interval [0, 10]
    a = 0
    b = 10
    pos_int_solution = fsolve(F, (a + b) / 2)

    print(Fore.LIGHTGREEN_EX + "Scipy has found a solution on interval [-10, 0]:", neg_int_solution)
    print("Scipy has found a solution on interval [0, 10]:", pos_int_solution)
    print(Style.RESET_ALL) 

def half_division_method_test():
    print(Fore.BLUE + "Testing Half-division method")
    # Interval [-10, 0]
    a = -10
    b = 0
    neg_int_solution = under_test.half_division_method(F, a, b, .00001)
    # Interval [0, 10]
    a = 0
    b = 10
    pos_int_solution = under_test.half_division_method(F, a, b, .00001)

    print(Fore.LIGHTGREEN_EX + "Half-division method has found a solution on interval [-10, 0]:", neg_int_solution)
    print("Half-division method has found a solution on interval [0, 10]:", pos_int_solution)
    print(Style.RESET_ALL)

def chords_method_test():
    print(Fore.BLUE + "Testing Chords method")
    # Interval [-10, 0]
    a = -10
    b = 0
    neg_int_solution = under_test.chords_method(F, a, b, .00001)
    # Interval [0, 10]
    a = 0
    b = 10
    pos_int_solution = under_test.chords_method(F, a, b, .00001)

    print(Fore.LIGHTGREEN_EX + "Chords method has found a solution on interval [-10, 0]:", neg_int_solution)
    print("Chords method has found a solution on interval [0, 10]:", pos_int_solution)
    print(Style.RESET_ALL)

def tangent_method_test():
    print(Fore.BLUE + "Testing Tangent method")
    # Starting estimate is closer to the negative solution
    starting_estimate = -30
    neg_estim_solution = under_test.tangent_method(
        F, f, _f, starting_estimate, .00001
    )
    # Starting estimate is closer to the positive solution
    starting_estimate = 50
    pos_estim_solution = under_test.tangent_method(
        F, f, _f, starting_estimate, .00001
    )
    # Starting estimate is evenly distant from equation solutions
    starting_estimate = 0.1
    print(Fore.YELLOW + "(!!!) Trying to find a solution with starting estimate 0" + Style.RESET_ALL)
    under_test.tangent_method(
        F, f, _f, starting_estimate, .00001
    )
    print(Fore.LIGHTGREEN_EX + "Tangent method has found a solution with starting estimate -30:", neg_estim_solution)
    print("Tangent method has found a solution with starting estimate 50:", pos_estim_solution)
    print(Style.RESET_ALL)


def simple_iteration_method_test():
    print(Fore.BLUE + "Testing Simple iteration method")
    # Starting estimate is closer to the negative solution
    starting_estimate = -10
    under_test.simple_iteration_method(F, ƒ, _ƒ, starting_estimate, .00001)
    # Starting estimate is closer to the positive solution
    starting_estimate = 10
    under_test.simple_iteration_method(F, ƒ, _ƒ, starting_estimate, .00001)
    # Starting estimate is evenly distant from equation solutions
    starting_estimate = 0.01
    print(Fore.YELLOW + "(!!!) Trying to find a solution with starting estimate 0.01" + Style.RESET_ALL)
    under_test.simple_iteration_method(F, ƒ, _ƒ, starting_estimate, .00001) 
    print(Style.RESET_ALL)

draw()
library_solution_test()
half_division_method_test()
chords_method_test()
tangent_method_test()
simple_iteration_method_test()

