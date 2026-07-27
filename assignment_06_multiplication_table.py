# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_single_table():
    """PART A: Generates a single multiplication table from 1 to 12 for a given number."""
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid whole number.")
        return

    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i:>2} = {num * i}")


def generate_multiple_tables():
    """PART B: Generates multiplication tables from 1 to N (1 to 12 each)."""
    try:
        n = int(input("Enter N (tables from 1 to N): "))
        if n <= 0:
            print("Error: Please enter a positive integer greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a valid whole number.")
        return

    for current in range(1, n + 1):
        print(f"\nMultiplication Table for {current}:")
        for i in range(1, 13):
            print(f"{current} x {i:>2} = {current * i}")
        
        # Add a visual separator between tables
        if current < n:
            print("-" * 27)


def main():
    print("--- PART A: Single Table ---")
    generate_single_table()

    print("\n--- PART B: Tables 1 to N ---")
    generate_multiple_tables()


if __name__ == "__main__":
    main()