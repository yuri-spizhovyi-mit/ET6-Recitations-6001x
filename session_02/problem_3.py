"""
Created on Sat Feb  1 19:48:06 2025

@author: somai
Replacing Vowels in a String
Explanation:
We can replace characters in a string using loops and conditional statements. This example replaces all vowels in a string with *.

Instructions:
1. Ask the user to enter a sentence.
2. Replace all vowels (a, e, i, o, u) with *.
3. Print the modified sentence.

"""
# Define vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
sentence = input("Enter a sentence: ")
replaced_sentence = ''

# Replace vowels with '*'
for char in sentence: 
  if char in vowels:
    replaced_sentence += "*"
  else:
    replaced_sentence += char



# Print the modified sentence
print(replaced_sentence)
