"""This file prompts the user for a number and returns
a list of the divisors for that number"""

num = int(input("Enter an integer: "))

a = []

i = 1
while i <= num : 
    if not num % i : # number divides cleanly
        a.append(i)
    i += 1    

print(a)

