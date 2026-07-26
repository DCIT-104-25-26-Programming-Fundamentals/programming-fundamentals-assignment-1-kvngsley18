# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calc_sum(numbers):
    """Calculates the sum of a list of numbers using a loop."""
    total = 0
    for num in numbers:
        total += num
    return total


def calc_average(numbers):
    """Calculates the average of a list of numbers."""
    total = calc_sum(numbers)
    return total / len(numbers)


def calc_max(numbers):
    """Finds the maximum value in a list of numbers using a loop."""
    highest = numbers[0]
    for num in numbers[1:]:
        if num > highest:
            highest = num
    return highest


def calc_min(numbers):
    """Finds the minimum value in a list of numbers using a loop."""
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest


if __name__ == "__main__":
    count = int(input("How many numbers? "))
    
    if count <= 0:
        print("Error: Please enter a positive integer greater than 0.")
    else:
        num_list = []
        for i in range(1, count + 1):
            val = float(input(f"Enter number {i}: "))
            num_list.append(val)
        
        print("\nResults:")
        print(f"Sum:     {calc_sum(num_list)}")
        print(f"Average: {calc_average(num_list)}")
        
        max_val = calc_max(num_list)
        min_val = calc_min(num_list)
        
        print(f"Maximum: {int(max_val) if max_val.is_integer() else max_val}")
        print(f"Minimum: {int(min_val) if min_val.is_integer() else min_val}")