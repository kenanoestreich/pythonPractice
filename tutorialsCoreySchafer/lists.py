courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Health', 'Triangles']

courses.extend(courses_2)

courses.append('Art')
courses.insert(0, 'Biology')
courses.remove('Math')
courses.reverse()
popped = courses.pop()
courses.sort(reverse=True)
sorted_courses = sorted(courses)

print(popped)
print(courses[3])
print(courses[-1])
print(courses)
print(sorted_courses)

for index, course in enumerate(courses): 
    print(index, course)
print('Art' in courses)

course_str = ' - '.join(courses)

print(course_str)

new_list = course_str.split(' - ')

print(new_list)

list_2 = courses

print(courses)
print(list_2)

courses[0] = 'P.E.'

print(courses)
print(list_2)

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses)) # also union and difference

print(cs_courses)
print('Math' in cs_courses)

