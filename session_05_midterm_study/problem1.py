# Problem 1
# 10/10 points (graded)
# Implement a function called closest_power that meets the specifications below.

# def closest_power(base, num):
"""
base: base of the exponential, integer > 1
num: number you want to be closest to, integer > 0
Find the integer exponent such that base**exponent is closest to num.
Note that the base**exponent may be either greater or smaller than num.
In case of a tie, return the smaller value.
Returns the exponent.
"""

# ***********************************************************************************************
"""
# -*- coding: utf-8 -*-

Created on Wed Feb 19 13:38:16 2025

@author: somai

Problem: Finding the Closest Power
Explanation:
The goal of this function is to determine the exponent exp such that base^exp is closest to the given number num.

Function Explanation:

closest_power(3, 12) → The powers of 3 are:
3^0 = 1
3^1 = 3
3^2 = 9
3^3 = 27
Since 3^2 = 9 is closer to 12 than 3^3 = 27, the function returns 2.

closest_power(4, 12) → The powers of 4 are:
4^0 = 1
4^1 = 4
4^2 = 16
Since 4^2 = 16 is closer to 12 than 4^1 = 4, the function returns 2.

closest_power(4, 1) → Since 4^0 = 1 is the closest, the function returns 0.

Instructions
1. Define a function closest_power(base, num) that takes two integers:
  - base: The base of the exponential function.
  -num: The target number.
2. Initialize exp to 0, which will track the exponent.
3. Convert num to an integer to ensure calculations work correctly.
4. Use a while loop to iterate through increasing powers of base until it surpasses num:
  - Calculate base^exp and base^(exp+1).
  - Compare their absolute differences from num to determine which is closer.
  - If base^exp is closer, return exp.
  - Otherwise, increment exp and continue the loop.
  """


def closest_power(base, num):
    """
    base: an integer greater than 1
    num: an integer greater than 0
    Returns: the exponent (int) such that base^exp is closest to num
    """
    # Define variables
    # Convert num to integer

    # Iterate to find the closest exponent

    # Compare which power is closer to num


# Example cases
print(closest_power(3, 12))  # Output: 2
print(closest_power(4, 12))  # Output: 2
print(closest_power(4, 1))  # Output: 0
