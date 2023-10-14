from colorama import Fore, Style

def half_division_method(F, a, b, e):
    count = 0
    while True:
        if abs(b - a) < e: 
            break

        x = (a + b) / 2
        if F(a) * F(x) < 0:
            b = x
        else:
            a = x

        count += 1
    print("Half division method -", count, "iterations")
    return (a + b) / 2

def chords_method(F, a, b, e): 
    x = a + abs(F(a) / (F(b) - F(a))) * (b - a)
    count = 0
    while True:
        if abs(F(x)) < e:
            break
        if F(a) * F(x) < 0:
            b = x
        else: 
            a = x
        x = a + abs((F(a) / (F(b) - F(a)))) * (b - a)
        count += 1
    print("Chords method -", count, "iterations")
    return x

# _f - the second derivative of F
def tangent_method(F, f, _f, x, e):
    if F(x) * _f(x) <= 0:
        print(Fore.RED + "Tangent method could not find a solution for starting estimate", x)
        return None

    count = 0
    while abs(F(x)) > e:
        x -= F(x) / f(x)
        count += 1
    print("Tangent method -", count, "iterations")
    return x

def simple_iteration_method(F, ƒ, _ƒ, x0, e): 
    x_previous = x0 
    x_current = ƒ(x_previous) 
    count = 1
    while abs(F(x_current)) > e: 
        if abs(_ƒ(x_previous)) >= 1:
            print(Fore.RED + "Simple iteration method meets divergent series when using", x0, "as a starting estimate" + Style.RESET_ALL)
            return None
        x_previous = x_current
        x_current = ƒ(x_current)
        count += 1
    print("Simple iteration method -", count, "iterations")
    return x_current











