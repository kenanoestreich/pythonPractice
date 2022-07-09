"""This file prompts for a string and returns
a string indicating if it's a palindrome or not"""

s = (input("Enter a string: "))

a = []

for char in s :
    a.insert(0,char)

# print(s)

a = ''.join(a)

# print(a)

if s == a :
    print("This is a palindrome")
else :
    print("Sorry, not a palindrome")

