import numpy as np
import sympy as sp

def input_function():
    func_str = input("Enter the LHS of the equation f(x) = 0: ")
    x = sp.symbols('x')
    f = sp.sympify(func_str)
    df = sp.diff(f, x)
    f = sp.lambdify(x, f, "numpy")
    df = sp.lambdify(x, df, "numpy")
    return f, df

def bisection(func, a, b, tolerance=1e-6, max_iter=50):
    if func(a) * func(b) >= 0:
        raise ValueError("Bisection method requires a sign change in the interval [a, b].")
    for it in range(max_iter):
        c = (a + b) / 2
        if abs(func(c)) < tolerance or (b - a) / 2 < tolerance:
            return c, it + 1
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    raise Exception("Bisection method did not converge.")

def false_position(func, a, b, tolerance=1e-6, max_iter=50):
    if func(a) * func(b) >= 0:
        raise ValueError("False Position method requires a sign change in the interval [a, b].")
    for it in range(max_iter):
        c = b - func(b) * (b - a) / (func(b) - func(a))
        if abs(func(c)) < tolerance or abs(b - a) < tolerance:
            return c, it + 1
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    raise Exception("False Position method did not converge.")

def newton_raphson(func, df, guess, tolerance=1e-6, max_iter=50):
    x = guess
    for it in range(max_iter):
        fx = func(x)
        if abs(fx) < tolerance:
            return x, it + 1
        dfx = df(x)
        x -= fx / dfx
    raise Exception("Newton-Raphson method did not converge.")

def secant(func, a, b, tolerance=1e-6, max_iter=50):
    for it in range(max_iter):
        x = b - func(b) * (b - a) / (func(b) - func(a))
        if abs(func(x)) < tolerance or abs(x - b) < tolerance:
            return x, it + 1
        a, b = b, x
    raise Exception("Secant method did not converge.")

def menu(func, df, a=0, b=2):
    while True:
        print("\nChoose method for solving the nonlinear equation:")
        print("1: Bracketing Method")
        print("2: Open-End Method")
        print("0: Return to Main Menu")
        method = int(input("\nEnter choice (0-2): "))
        
        if method == 0:
            return
        
        elif method == 1:
            a, b = map(float, input("\nEnter an interval to bracket the root (a b): ").split())
            try:
                root, iterations = bisection(func, a, b)
                print(f"\nBisection Method:\nRoot: {root:.6f} \nIterations: {iterations}\n")
            except Exception as e:
                print("Bisection method error:", e)
            try:
                root, iterations = false_position(func, a, b)
                print(f"\nFalse Position Method:\nRoot: {root:.6f} \nIterations: {iterations}\n")
            except Exception as e:
                print("False Position method error:", e)
                
        elif method == 2:
            a = float(input("Guess a root: "))
            b = a + 2
            try:
                root, iterations = newton_raphson(func, df, a)
                print(f"\nNewton-Raphson Method:\nRoot: {root:.6f} \nIterations: {iterations}\n")
            except Exception as e:
                print("Newton-Raphson method error:", e)
            try:
                root, iterations = secant(func, a, b)
                print(f"\nSecant Method:\nRoot: {root:.6f} \nIterations: {iterations}\n")
            except Exception as e:
                print("Secant method error:", e)
        else:
            print("Invalid choice. Please try again.")

def main():
    f, df = input_function()
    menu(f, df)

if __name__ == "__main__":
    main()
