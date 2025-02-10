"""
Created on Sat Feb  1 19:48:06 2025

@author: somai
(While Loop Version): Multiplication Table for Numbers 1-9
Explanation:
We use two while loops:
The outer loop iterates through numbers 1 to 9 (for which we generate tables).
The inner loop iterates from 1 to 10 to print the multiplication table for each number.
The output is formatted to display each table clearly.
Instructions:
1. Initialize a variable (num) for the multiplication table starting from 1.
2. Use a while loop to iterate num from 1 to 9.
3. Inside this loop, use another while loop for numbers 1 to 10.
4. Print each multiplication result, then increment counters properly.
5. If you have time implement it with for loop as well/
"""

# Initialize outer loop counter
outer_counter = 1
# Outer loop: Iterate through numbers 1 to 9
while outer_counter <= 10:
    # Initialize inner loop counter
    inner_counter = 1
    # Inner loop: Iterate from 1 to 10
    while inner_counter <= 10:
        result = outer_counter * inner_counter
        print(f"While Solution: {outer_counter} * {inner_counter} = {result}")
        # Increment inner loop counter
        inner_counter += 1
    # Increment outer loop counter
    outer_counter += 1

outer_for_counter = 1
for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"For Solution: {i} * {j} = {result}")
