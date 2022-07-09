
def hello_func(greeting, name = 'You'):
    """this is a docstring"""
    return '{}, {}'.format(greeting, name)


print(hello_func('Hi', 'Kenan'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)




