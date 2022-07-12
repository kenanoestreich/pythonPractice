"""This file defines a function to get the first and last 
elements in a list and prints them out for an example list"""

def getListEnds(list) :
    b = [list[0],list[len(list)-1]]
    return b


a = [5, 10, 15, 20, 25]
print(getListEnds(a))