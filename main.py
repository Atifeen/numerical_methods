import linear
import nonlinear
import ode
import matrix_inverter
import matplotlib.pyplot as plt

def main_menu():
    print("\nSelect the type of calculation:")
    print("1: Solve linear system")
    print("2: Solve nonlinear equation")
    print("3: Solve differential equation using Runge-Kutta")
    print("4: Find matrix inverse")
    print("0: Exit")
    return int(input("\nEnter choice (0-4): "))



def main():
    while True:
        choice = main_menu()
        
        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            matrix, constants = linear.input_system()
            linear.solve(matrix, constants)
        elif choice == 2:
            func, df = nonlinear.input_function()
            nonlinear.menu(func, df)
        elif choice == 3:
            ode.solve()
        elif choice == 4:
            matrix_inverter.solve()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
