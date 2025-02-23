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

    num_counts = {}
    # Get unique elements
    for i in L:
        if i in num_counts:
            num_counts[i] += 1
        else:
            num_counts[i] = 1

    largest_odd = None
    for num in num_counts:
        if num_counts[num] % 2 != 0:
            if largest_odd is None or num > largest_odd:
                largest_odd = num
    return largest_odd
    # If no odd-occurring number is found


# print(largest_odd_times([]))
print(largest_odd_times([2, 2, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 7, 7]))
