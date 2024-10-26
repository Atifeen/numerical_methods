import numpy as np
from fractions import Fraction

def input_system():
    n = int(input("Enter number of unknowns: "))
    matrix = np.empty((n, n))
    print("Input coefficient matrix:")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix[i] = row

    print("Input constant vector:")
    constants = list(map(float, input().split()))
    return matrix, np.array(constants)

def jacobi(matrix, constants, max_iter=50, tolerance=1e-6):
    n = len(constants)
    x = np.zeros(n)
    for it in range(max_iter):
        new_x = np.zeros(n)
        for i in range(n):
            sum = np.sum(matrix[i] * x) - matrix[i, i] * x[i]
            new_x[i] = (constants[i] - sum) / matrix[i, i]
        if max(abs(new_x - x)) < tolerance:
            return new_x, it+1
        x = new_x
    raise Exception("Jacobi method did not converge")

def gauss_seidel(matrix, constants, max_iter=50, tolerance=1e-6):
    n = len(constants)
    x = np.zeros(n)
    for it in range(max_iter):
        new_x = np.copy(x)
        for i in range(n):
            sum = np.sum(matrix[i] * new_x) - matrix[i, i] * new_x[i]
            new_x[i] = (constants[i] - sum) / matrix[i, i]
        if max(abs(new_x - x)) < tolerance:
            return new_x, it+1
        x = new_x
    raise Exception("Gauss-Seidel method did not converge")

def gauss_elimination(matrix, constants):
    n = len(constants)
    A = np.column_stack((matrix, constants))
    for i in range(n):
        if A[i, i] == 0:
            for j in range(i + 1, n):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]
                    break
            else:
                raise ValueError("Gauss elimination failed! Matrix is singular")
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (A[i, -1] - np.sum(A[i, i + 1:n] * x[i + 1:n])) / A[i, i]
    return x

def normal(matrix):
    n = len(matrix)
    A = matrix
    for i in range(n):
        if A[i, i] == 0:
            for j in range(i + 1, n):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]
                    break
            else:
                raise ValueError("Matrix is singular")
        A[i] /= A[i, i]
        for j in range(n):
            if i != j:
                A[j] -= A[i] * A[j, i]
    return A

def gauss_jordan(matrix, constants):
    n = len(constants)
    A = np.column_stack((matrix, constants))
    A = normal(A)
    return A[:, -1]

def lu_factorization(matrix, constants):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        if matrix[i, i] == 0:
            for j in range(i + 1, n):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    constants[[i, j]] = constants[[j, i]]
                    break
            else:
                raise ValueError("LU factorization failed! Matrix is singular")
        for j in range(i, n):
            U[i, j] = matrix[i, j] - np.sum(L[i, :i] * U[:i, j])
        L[i, i] = 1
        for j in range(i + 1, n):
            L[j, i] = (matrix[j, i] - np.sum(L[j, :i] * U[:i, i])) / U[i, i]
    y = np.zeros(n)
    for i in range(n):
        y[i] = (constants[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(U[i, i + 1:] * x[i + 1:])) / U[i, i]
    return x

def roots_to_str(roots_array):
    fraction_roots = []
    for root in roots_array:
        frac = Fraction(root).limit_denominator()
        fraction_str = str(frac.numerator) if frac.denominator == 1 else f"{frac.numerator}/{frac.denominator}"
        fraction_roots.append(fraction_str)
    return fraction_roots

def solve(matrix, constants):
    try:
        roots, iter = jacobi(matrix, constants)
        print(f"Solution using Jacobi method: {roots} (number of iterations: {iter})")
    except Exception as e:
        print("Jacobi method exception:", e)
        
    try:
        roots, iter = gauss_seidel(matrix, constants)
        print(f"Solution using Gauss-Seidel method: {roots} (number of iterations: {iter})")
    except Exception as e:
        print("Gauss-Seidel method exception:", e)
        
    try:
        roots = gauss_elimination(matrix, constants)
        formatted_roots = roots_to_str(roots)
        print("\nSolution using Gauss Elimination method:")
        print("Fraction format:", formatted_roots)
        print("Decimal format:", roots)
    except Exception as e:
        print("Gauss Elimination method exception:", e)
        
    try:       
        roots = gauss_jordan(matrix, constants)
        formatted_roots = roots_to_str(roots)
        print("\nSolution using Gauss-Jordan method:")
        print("Fraction format:", formatted_roots)
        print("Decimal format:", roots)
    except Exception as e:
        print("Gauss-Jordan method exception:", e)

    try:
        roots = lu_factorization(matrix, constants)
        formatted_roots = roots_to_str(roots)
        print("\nSolution using LU Factorization method:")
        print("Fraction format:", formatted_roots)
        print("Decimal format:", roots)
    except Exception as e:
        print("LU Factorization method exception:", e)

def main():
    matrix, constants = input_system()
    solve(matrix, constants)

if _name_ == "_main_":
    main()