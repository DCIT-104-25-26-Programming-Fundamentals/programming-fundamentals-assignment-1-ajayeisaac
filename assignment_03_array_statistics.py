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

def get_sum(nums):
    total = 0
    for x in nums:
        total = total + x
    return total

def get_avg(nums):
    return get_sum(nums) / len(nums)

def get_max(nums):
    hi = nums[0]
    for x in nums:
        if x > hi:
            hi = x
    return hi

def get_min(nums):
    lo = nums[0]
    for x in nums:
        if x < lo:
            lo = x
    return lo

n = int(input("How many numbers? "))

if n <= 0:
    print("Error: Enter a number bigger than 0.")
else:
    nums = []
    for i in range(n):
        val = float(input(f"Enter number {i + 1}: "))
        nums.append(val)

    print("\nResults:")
    print("Sum:    ", get_sum(nums))
    print("Average:", get_avg(nums))
    print("Maximum:", get_max(nums))
    print("Minimum:", get_min(nums))
