import numpy as np
import numpy.linalg as la
from colorama import Fore, Style
import scipy.optimize as opt

def newtons_method(F, f, x, e):
    y = F(x)
    
    while la.norm(y) > e:
        _y = f(x)
        x -= np.dot(la.inv(_y), y)
        y = F(x)
    return x

def iterative_method(F, ƒ, _ƒ, x, e):
    x_previous = None
    while abs(la.norm(F(x))) > e:
        if abs(la.norm(_ƒ(x))) >= 1:
            print(Fore.RED + "Iterative method met divergent series" + Style.RESET_ALL)
            return None
        if x_previous == x:
            print(Fore.RED + "Iterative method's got stuck in an infinite loop" + Style.RESET_ALL)
            return None 
        x_previous = x 
        x = ƒ(x)
    return x

def sqrt_minimization_method(F, x):
    ƒ = lambda x: la.norm(F(x))
    return opt.minimize(ƒ, x).x


