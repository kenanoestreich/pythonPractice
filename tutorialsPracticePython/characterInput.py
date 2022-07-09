from datetime import date

"""This file asks the user for their name and age and then returns the year
when they will turn 100"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(date.today())
year = int(date.today().strftime("%Y"))

print(year)

yearsTo100 = 100-age

yearTurning100 = year + yearsTo100

print('Hello ' + name + '! You will turn 100 in the year ' + str(yearTurning100))