"""This file returns the intersection between these two 
lists (no duplicates)"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13]
c = []

aset = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
bset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13}

print(aset.intersection(bset))

for num in a : 
    if num in b : 
        # better way to do this with numpy 
        if not num in c : 
            c.append(num)

print(c)
