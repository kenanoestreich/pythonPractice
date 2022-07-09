from modules import find_index, test
import sys
import random
import math # sin, rads, etc...
import datetime # 
import calendar # 
import os # access to operating system

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

random_course = random.choice(courses)

print(random_course)
print(sys.path)

print(os.__file__) # location of module 

