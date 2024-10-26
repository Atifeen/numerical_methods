import numpy as np
from linear import normal
from fractions import Fraction

    
def mat_to_str(float_matrix):
    fraction_matrix = np.empty(float_matrix.shape, dtype=object)
    for i in range(float_matrix.shape[0]):
        for j in range(float_matrix.shape[1]):
            frac = Fraction(float_matrix[i, j]).limit_denominator()
            fraction_matrix[i, j] = str(frac.numerator) if frac.denominator == 1 else f"{frac.numerator}/{frac.denominator}"
            print(fraction_matrix[i, j], end="\t")
        print()
        
def input_matrix():
    n = int(input("Enter the size of the matrix: "))
    matrix = np.empty((n, n))
    print("Enter the entries of the matrix: ")
    for i in range(n):
        row = list(map(float, input().split()))
        matrix[i] = row
    return matrix
        
def inverse(matrix):
    n = len(matrix)
    I = np.identity(n)
    A = np.hstack((matrix, I))
    A = normal(A)
    return A[:, n:]

def solve():
    matrix = input_matrix()
    try:
        matrix_inv = inverse(matrix)
         
        print("\nInverse of the matrix:")
        mat_to_str(matrix_inv)
        print("\nIn decimal fraction: ")
        print(matrix_inv)
    except ValueError as e:
        print("Error:", e)

def main(): 
    solve()
    
    
if __name__ == "__main__":
    main()
