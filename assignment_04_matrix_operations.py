# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()


def transpose_matrix(matrix, rows, cols):
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result

def add_matrices(matrix_a, matrix_b, rows, cols):
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            sum_val = matrix_a[r][c] + matrix_b[r][c]
            new_row.append(sum_val)
        result.append(new_row)
    return result

def multiply_matrices(matrix_a, matrix_b, rows_a, cols_a, cols_b):
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum = cell_sum + (matrix_a[i][k] * matrix_b[k][j])
            new_row.append(cell_sum)
        result.append(new_row)
    return result

def read_matrix(rows):
    matrix = []
    for r in range(rows):
        line = input(f"Enter row {r + 1}: ")
        row_vals = []
        for x in line.split():
            row_vals.append(int(x))
        matrix.append(row_vals)
    return matrix

print("Transpose Matrix")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
mat = read_matrix(r)

print("\nOriginal Matrix:")
print_matrix(mat)

transposed = transpose_matrix(mat, r, c)
print("\nTransposed Matrix:")
print_matrix(transposed)

print(" Add Matrices")
r_b = int(input("Enter number of rows: "))
c_b = int(input("Enter number of columns: "))
print("Matrix 1:")
m1 = read_matrix(r_b)
print("Matrix 2:")
m2 = read_matrix(r_b)

added_result = add_matrices(m1, m2, r_b, c_b)
print("\nSum of Matrices:")
print_matrix(added_result)

print(" Multiply Matrices ")
r_a = int(input("Enter Matrix A rows: "))
c_a = int(input("Enter Matrix A columns (and Matrix B rows): "))
c_b2 = int(input("Enter Matrix B columns: "))

print("Matrix A:")
mat_a = read_matrix(r_a)
print("Matrix B:")
mat_b = read_matrix(c_a)

mult_result = multiply_matrices(mat_a, mat_b, r_a, c_a, c_b2)
print("\nProduct Matrix (A x B):")
print_matrix(mult_result)