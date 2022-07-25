"""This file takes in a list and returns a new list
with the same contents as the first minus any duplicates"""

def removeDuplicates(list) :
    newlist = []
    for num in list : 
        if newlist.count(num)==0 :
            newlist.append(num)
    return newlist

a = [1, 1, 2, 3, 4, 6, 6, 6, 7, 8, 9, 9, 9, 9, 10]

b = removeDuplicates(a)
print(b)




