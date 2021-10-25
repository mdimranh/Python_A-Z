student = {
    'id' : '181-15-1984',
    'name' : 'Imran',
    'age' : 23,
    'CGPA' : 3.55
}

print(student)

print(student['name'])

student['name'] = 'Muhammad'
print(student['name'])

student['sec'] = 'PCD'
print(student)

print('age :', student.get('age'))

del student['age']
print(student)

print('\nget value Using values:')

for i in student.values():
    print(i)

print('\nget value Using items:')

for i in student.items():
    print(i)

print('\nget value using loop:')

for i, j in student.items():
    print(i, ':', j)