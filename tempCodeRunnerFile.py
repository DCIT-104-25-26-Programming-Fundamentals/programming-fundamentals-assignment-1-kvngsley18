 PROGRAMMING FUNDAMENTALS — Assignment 4
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

# =============================================================================
# HELPER FUNCTIONS (Input & Display)
# =============================================================================

def print_matrix(matrix):
    """Helper function to display a matrix in a neat grid format."""
    for row in matrix:
        for val in row:
            print(f"{val:>4}", end=" ")
        print()


def read_matrix(rows, cols, name="Matrix"):
    """Helper function to read a matrix from user input row by row."""
    print(f"\nEntering {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"  Enter row {i + 1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Expected {cols} values, but got {len(row)}.")
        matrix.append(row)
    return matrix


# =============================================================================
# PART A — Transpose a Matrix
# =============================================================================
def transpose(matrix):
    """
    Transposes an M x N matrix to an N x M matrix.
    Rows become columns, and columns become rows.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# =============================================================================
# PART B — Add Two Matrices
# =============================================================================
def add_matrices(mat_a, mat_b):
    """Computes element-wise sum of two M x N matrices."""
    rows = len(mat_a)
    cols = len(mat_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat_a[i][j] + mat_b[i][j]

    return result


# =============================================================================
# PART C — Multiply Two Matrices
# =============================================================================
def multiply_matrices(mat_a, mat_b):
    """
    Multiplies an M x N matrix (mat_a) by an N x P matrix (mat_b).
    Resulting matrix is M x P.
    """
    m = len(mat_a)
    n = len(mat_a[0]) 
    p = len(mat_b[0])

    result = [[0 for _ in range(p)] for _ in range(m)]

    # Triple nested loop to compute dot products
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += mat_a[i][k] * mat_b[k][j]

    return result


# =============================================================================
# MAIN PROGRAM DRIVER
# =============================================================================
def main():
    print("=== MATRIX OPERATIONS PROGRAM ===")
    print("\n--- PART A: Transpose a Matrix ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    mat = read_matrix(m, n)

    print("\nOriginal Matrix:")
    print_matrix(mat)

    print("\nTransposed Matrix:")
    print_matrix(transpose(mat))

    print("\n--- PART B: Add Two Matrices ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    mat_a = read_matrix(m, n, "Matrix A")
    mat_b = read_matrix(m, n, "Matrix B")

    print("\nMatrix A + Matrix B:")
    print_matrix(add_matrices(mat_a, mat_b))

    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter rows for Matrix A (M): "))
    n = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter columns for Matrix B (P): "))

    mat_a = read_matrix(m, n, "Matrix A")
    mat_b = read_matrix(n, p, "Matrix B")

    print("\nMatrix A x Matrix B:")
    print_matrix(multiply_matrices(mat_a, mat_b))


if __name__ == "__main__":
    main()