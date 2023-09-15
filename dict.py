a = {100: 'Hundred', 200: 'Two Hundred', 300:"Three Hundred"}
print(a[100])
print(a.get(200))
print(a.get(400))
print(a[400])
person = {'name': 'Phill', 'age': 22}
print('Name: ', person.get('name'))
print('Age: ', person.get('age'))
print('Salary: ', person.get('salary'))
print('Salary: ', person.get('salary', 0.0))