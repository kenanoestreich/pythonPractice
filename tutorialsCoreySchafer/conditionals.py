
language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else: 
    print("No Match")

user = 'Admin'
logged_in = True
if user == 'Admin' and not logged_in:
    print('Admin Page')
else: 
    print('Bad Creds')

a = 1
b = a

print(id(a))
print(id(b))

print(a==b)
print(a is b)