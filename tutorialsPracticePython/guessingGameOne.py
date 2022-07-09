"""This file generates a random number from [1:9] and 
asks the user to guess repeatedly until they get it right.
Between each guess, the program prints if they were too 
high, too low, or just right"""

from random import randint


numGuesses = 1
secretNum = randint(1,9)

while True :
    guess = int(input("Guess a number between 1 and 9, inclusive: "))
    if secretNum == guess :
        print("You guessed it right!")
        print("Total number of guesses: " + str(numGuesses))
        break 
    elif secretNum < guess : 
        print("Too high!")
        numGuesses += 1 
        continue
    elif secretNum > guess : 
        print("Too low!")
        numGuesses += 1 
        continue
