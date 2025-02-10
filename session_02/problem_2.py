"""
Created on Sat Feb  1 19:48:06 2025

@author: somai

Problem 2: Checking for a Palindrome
Explanation:
A palindrome is a word or phrase that reads the same forward and backward (e.g., "madam", "racecar"). We can check for palindromes using string slicing and conditionals.

Instructions:
1. Ask the user to enter a word.
2. Convert the word to lowercase to ensure case insensitivity.
3. Check if the word is the same when reversed.
4. Print "It's a palindrome!" if true, otherwise print "Not a palindrome."
"""

## Get user input
text = input("Enter a word to check: ")

# Convert to lowercase for case insensitivity by calling lower() function
text = text.lower()

# Check if the word is the same forward and backward
if text == text[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
