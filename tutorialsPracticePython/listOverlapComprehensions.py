"""This file returns a list that contains the intersection 
between the two lists a and b"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [num for num in b if num in a] 

print(c)