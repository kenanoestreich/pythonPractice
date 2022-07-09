"""This file prints out all the numbers in list a with 
value less than 10"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

i = 0
while a[i] < 10 :
    print(a[i])
    i += 1 

for x in a : 
    if x < 10: print(x)

