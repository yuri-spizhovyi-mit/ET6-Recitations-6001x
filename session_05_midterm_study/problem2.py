# Write a function that satisfies the following docstring:

# def largest_odd_times(L):
#     """ Assumes L is a non-empty list of ints
#         Returns the largest element of L that occurs an odd number
#         of times in L. If no such element exists, returns None """
#     # Your code here
# For example, if

# largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns 9
# Paste your entire function, including the definition, in the box below.
# Do not leave any debugging print statements.
# ****************************************************************************
"""
Instructions:
1. Define a function `largest_odd_times(L)` that takes a non-empty list of integers as input.
2. The function should find the largest number that appears an odd number of times in the list.
3. If no number appears an odd number of times, return `None`.

Implementation Steps:
- Iterate through the list and count occurrences of each element.
- Identify numbers that occur an odd number of times.
- Return the largest such number, or `None` if no odd-occurring number exists.
"""


def largest_odd_times(L):
    """
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number
    of times in L. If no such element exists, returns None
    """


# Get unique elements


# Get the largest remaining element
# Check if it appears an odd number of times
# Remove and continue checking

# If no odd-occurring number is found


print(largest_odd_times([2, 5, 6, 7, 8, 9, 7, 7]))
