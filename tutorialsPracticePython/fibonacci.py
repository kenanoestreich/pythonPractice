"""This file asks the user for a number x and outputs
the first x numbers in the fibonacci sequence"""

def calculateNextNumber(numMostRecent, numSecondMostRecent) :
    return numMostRecent+numSecondMostRecent

numOfNumbers = int(input("Enter a positive integer: "))

fibNums = []
i = 0
a = 1
b = 0
while i < numOfNumbers :
    if i == 0 :
        fibNums.append(a)
    else : 
        newB = a
        a = calculateNextNumber(a, b)
        b = newB
        fibNums.append(a)
    i += 1 

print(fibNums)
    








