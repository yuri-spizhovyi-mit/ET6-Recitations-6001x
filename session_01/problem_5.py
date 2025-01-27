# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:39:16 2025
@author: Somaia

---  5: Scenario and Instructions: Logical Operators in Conditions ---

In this program, you'll explore how to combine multiple conditions using logical operators to create more complex decision-making. Logical operators like and, or, and not allow you to evaluate multiple conditions at once.

This program checks if a number is:
1. Positive and either even or odd.
2. Negative.
3. Zero.

Explanation of Logical Operators:
- and: Ensures all conditions connected by and must be True for the entire condition to be True.
    Example: x > 0 and x % 2 == 0 checks if x is positive and even.
- or: Only one of the conditions needs to be True for the overall condition to be True.
    Example: x < 0 or x == 0 would return True for any number that is negative or zero.
- not: Reverses the truth value of a condition.
    Example: not(x > 0) would be True if x is not greater than 0.

Instructions:
1. Input a Number:
    - The program will prompt the user to input an integer using input().
    - The input is converted to an integer using int().
2. Evaluate the Number:
    - If the number is positive and even (x > 0 and x % 2 == 0), the program will display:
        "x is a positive even number".
    - Elif the number is positive and odd (x > 0 and x % 2 != 0), the program will display:
        "x is a positive odd number".
    - Elif the number is negative (x < 0), the program will display:
        "x is a negative number".
    - Else, for numbers that are neither positive nor negative (i.e., zero), the program will display:
        "x is zero".
3. Test the Code:
    - Try entering various numbers (positive, negative, even, odd, and zero) to see how the program evaluates each case.

Example Scenarios:
- Scenario 1:
    Input: 6
    Output: "x is a positive even number"
- Scenario 2:
    Input: 9
    Output: "x is a positive odd number"
- Scenario 3:
    Input: -4
    Output: "x is a negative number"
- Scenario 4:
    Input: 0
    Output: "x is zero"
"""
# Take input from the user
x = int(input("Enter a number: "))

# Conditional checks with logical operators
if x > 0 and x % 2 == 0:
    print("x is a positive even number")
elif x > 0 and x % 2 != 0:
    print("x is a positive odd number")
elif x < 0:
    print("x is a negative number")
else:
    print("x is zero")
