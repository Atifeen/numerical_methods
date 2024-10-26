import sympy as sp
import matplotlib.pyplot as plt

def input_ode_function():
    func_str = input("Enter RHS of the eqn dy/dx = f(x, y): ")
    x, y = sp.symbols('x y')
    f = sp.sympify(func_str)
    f = sp.lambdify((x, y), f, "numpy")
    a = float(input("Enter the start of the interval: "))
    b = float(input("Enter the end of the interval: "))
    h = float(input("Enter the step size: "))
    init_value = float(input("Enter the initial value y(a): "))
    return f, a, b, h, init_value

def runge_kutta(f, a, b, init_value, h):
    x = a
    y = init_value
    xvalues = [x]
    yvalues = [y]
    
    for i in range(round((b-a)/h)):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        xvalues.append(x)
        yvalues.append(y)
    
    return xvalues, yvalues


def solve():
    f, a, b, h, init_value = input_ode_function()
    x_vals, y_vals = runge_kutta(f, a, b, init_value, h)
    print("Solution values:", y_vals)
    plt.plot(x_vals, y_vals)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Solution of the Differential Equation")
    plt.show()
    
    
    
def main():
    solve()
    

if __name__ == "__main__":
    main()