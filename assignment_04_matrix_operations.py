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

# =============================================================================
# HELPER FUNCTIONS (Input & Display)
# =============================================================================

def read_matrix(rows, cols, name="Matrix"):
    """Reads a matrix of given dimensions from user input."""
    matrix = []
    print(f"\nEntering {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").strip().split()
            if len(row_input) == cols:
                try:
                    row = [float(val) for val in row_input]
                    matrix.append(row)
                    break
                except ValueError:
                    print("  Invalid input. Please enter numbers only.")
            else:
                print(f"  Expected {cols} values, but got {len(row_input)}. Try again.")
    return matrix


def display_matrix(matrix, title="Matrix"):
    """Displays a matrix in a neatly aligned grid format."""
    print(f"\n{title}:")
    for row in matrix:
        # Formats integers cleanly while keeping decimals for float values
        formatted_row = " ".join(
            f"{int(val):>6}" if val.is_integer() else f"{val:>6.2f}" for val in row
        )
        print(formatted_row)


# =============================================================================
# PART A — Transpose a Matrix
# =============================================================================

def transpose(matrix):
    """
    Computes the transpose of a matrix (rows become columns, columns become rows).
    Matrix is M x N -> Transpose is N x M.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize an N x M result matrix filled with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Fill in transposed values using nested loops
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


# =============================================================================
# PART B — Add Two Matrices
# =============================================================================

def add_matrices(A, B):
    """
    Computes element-wise sum of two M x N matrices.
    """
    rows = len(A)
    cols = len(A[0])
    
    # Initialize an M x N result matrix filled with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Perform element-wise addition
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
            
    return result


# =============================================================================
# PART C — Multiply Two Matrices
# =============================================================================

def multiply_matrices(A, B):
    """
    Computes the matrix product A (M x N) * B (N x P).
    Result is of size M x P.
    """
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    
    # Initialize an M x P result matrix filled with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication using 3 nested loops
    for i in range(rows_A):          # Iterate through rows of A
        for j in range(cols_B):      # Iterate through columns of B
            for k in range(cols_A):  # Iterate through elements to dot-product
                result[i][j] += A[i][k] * B[k][j]
                
    return result


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    print("==========================================")
    print("        MATRIX OPERATIONS PROGRAM         ")
    print("==========================================")

    # --- PART A: Transpose ---
    print("\n--- PART A: TRANSPOSE A MATRIX ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix_a = read_matrix(rows, cols, "Original Matrix")
    display_matrix(matrix_a, "Original Matrix")
    
    transposed_a = transpose(matrix_a)
    display_matrix(transposed_a, "Transposed Matrix")

    # --- PART B: Addition ---
    print("\n------------------------------------------")
    print("--- PART B: ADD TWO MATRICES ---")
    print(f"Adding two matrices of size ({rows} x {cols}):")
    
    mat1 = read_matrix(rows, cols, "Matrix 1")
    mat2 = read_matrix(rows, cols, "Matrix 2")
    
    sum_matrix = add_matrices(mat1, mat2)
    
    display_matrix(mat1, "Matrix 1")
    display_matrix(mat2, "Matrix 2")
    display_matrix(sum_matrix, "Sum Matrix (Matrix 1 + Matrix 2)")

    # --- PART C: Multiplication ---
    print("\n------------------------------------------")
    print("--- PART C: MULTIPLY TWO MATRICES ---")
    print(f"Matrix A will be size ({rows} x {cols}).")
    print(f"Matrix B must have {cols} rows to be multiplicable (A x B).")
    
    cols_B = int(input(f"Enter number of columns for Matrix B: "))
    
    matrix_A = read_matrix(rows, cols, "Matrix A")
    matrix_B = read_matrix(cols, cols_B, "Matrix B")
    
    product_matrix = multiply_matrices(matrix_A, matrix_B)
    
    display_matrix(matrix_A, "Matrix A")
    display_matrix(matrix_B, "Matrix B")
    display_matrix(product_matrix, f"Product Matrix A x B ({rows} x {cols_B})")


if __name__ == "__main__":
    main()
