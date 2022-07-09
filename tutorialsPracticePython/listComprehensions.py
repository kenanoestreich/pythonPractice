"""This file uses list comprehension to create
a new list using an existing list and a condition"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [num for num in a if num % 2 == 0] # this is a bit confusing

print(b)