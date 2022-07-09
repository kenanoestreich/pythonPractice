"""This file prompts for an int and returns if the number
is prime or not"""

a = []

num = int(input("Enter an integer:" ))

i = 1
while i <= num : 
    if not num % i : # number divides cleanly
        a.append(i)
    i += 1    

print(a)

if len(a) == 2 :
    print("This number is prime! :)")
else :
    print("This number is not prime :(")